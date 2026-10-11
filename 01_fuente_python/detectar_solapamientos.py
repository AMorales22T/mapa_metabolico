#!/usr/bin/env python3
"""
DETECTOR AUTOMÁTICO DE SOLAPAMIENTOS EN EL SVG DEL MAPA
========================================================
Analiza prueba_visual_integrada.svg (sin navegador) y reporta:
  1. TEXTO-TEXTO   : dos rótulos que se pisan.
  2. FLECHA-TEXTO  : una flecha / conector que atraviesa un rótulo.
  3. TEXTO-ESTRUC. : un rótulo que cae encima del dibujo de una molécula.
  4. FLECHA-ESTRUC.: una flecha que atraviesa una molécula (sin contar sus extremos).

El ancho del texto se estima (≈0.6·font-size por carácter), por lo que puede
haber algún falso positivo leve. Genera también un SVG de control con los
problemas marcados en rojo:  solapamientos_debug.svg

Uso:
    python3 detectar_solapamientos.py [archivo.svg] [--debug] [--max N]
"""
import math
import re
import sys
import xml.etree.ElementTree as ET

NS = "{http://www.w3.org/2000/svg}"

# Grupos que no se analizan (decorado de fondo o insertos con diseño propio cerrado)
GRUPOS_EXCLUIDOS = {
    "mitocondria_biologica", "eritrocitos_torrente",
}
# Dentro de estos grupos sólo se comprueba su propio contorno, no su interior
GRUPOS_INSERTO = {
    "lupa_cadena_respiratoria",
    "lupa_piruvato_deshidrogenasa",
    "lupa_lanzadera_malato_aspartato",
    "lupa_lanzadera_glicerol_p",
}

ANCHO_CHAR = {"mono": 0.62, "sans": 0.60}


# --------------------------------------------------------------------------
# Álgebra afín
# --------------------------------------------------------------------------
def mat_mul(a, b):
    return (
        a[0] * b[0] + a[2] * b[1], a[1] * b[0] + a[3] * b[1],
        a[0] * b[2] + a[2] * b[3], a[1] * b[2] + a[3] * b[3],
        a[0] * b[4] + a[2] * b[5] + a[4], a[1] * b[4] + a[3] * b[5] + a[5],
    )


def aplicar(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


IDENT = (1, 0, 0, 1, 0, 0)


def parse_transform(t):
    m = IDENT
    if not t:
        return m
    for nombre, args in re.findall(r"(\w+)\s*\(([^)]*)\)", t):
        v = [float(n) for n in re.findall(r"-?[\d.]+(?:e-?\d+)?", args)]
        if nombre == "translate":
            mm = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif nombre == "scale":
            sx = v[0]
            sy = v[1] if len(v) > 1 else sx
            mm = (sx, 0, 0, sy, 0, 0)
        elif nombre == "rotate":
            a = math.radians(v[0])
            c, s = math.cos(a), math.sin(a)
            r = (c, s, -s, c, 0, 0)
            if len(v) == 3:
                cx, cy = v[1], v[2]
                mm = mat_mul(mat_mul((1, 0, 0, 1, cx, cy), r), (1, 0, 0, 1, -cx, -cy))
            else:
                mm = r
        elif nombre == "matrix":
            mm = tuple(v[:6])
        else:
            continue
        m = mat_mul(m, mm)
    return m


# --------------------------------------------------------------------------
# Geometría de paths
# --------------------------------------------------------------------------
def tokens_path(d):
    for cmd, args in re.findall(r"([MmLlHhVvCcSsQqTtAaZz])([^MmLlHhVvCcSsQqTtAaZz]*)", d):
        yield cmd, [float(n) for n in re.findall(r"-?\d*\.?\d+(?:e-?\d+)?", args)]


def bezier(p0, p1, p2, p3, n=10):
    pts = []
    for i in range(1, n + 1):
        t = i / n
        u = 1 - t
        pts.append((
            u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
            u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1],
        ))
    return pts


def puntos_path(d):
    """Devuelve lista de polilíneas (listas de puntos) aproximando el path."""
    polis, actual = [], []
    x = y = 0.0
    sx = sy = 0.0
    last_ctrl = None
    for cmd, v in tokens_path(d):
        rel = cmd.islower()
        c = cmd.upper()
        if c == "Z":
            if actual:
                actual.append((sx, sy))
            x, y = sx, sy
            continue
        i = 0
        while True:
            if c == "M":
                if i + 2 > len(v):
                    break
                nx, ny = v[i], v[i + 1]
                if rel:
                    nx, ny = x + nx, y + ny
                if actual:
                    polis.append(actual)
                actual = [(nx, ny)]
                x, y, sx, sy = nx, ny, nx, ny
                i += 2
                c = "L"  # pares siguientes son L implícitos
                last_ctrl = None
            elif c == "L":
                if i + 2 > len(v):
                    break
                nx, ny = v[i], v[i + 1]
                if rel:
                    nx, ny = x + nx, y + ny
                actual.append((nx, ny))
                x, y = nx, ny
                i += 2
                last_ctrl = None
            elif c == "H":
                if i + 1 > len(v):
                    break
                x = x + v[i] if rel else v[i]
                actual.append((x, y))
                i += 1
            elif c == "V":
                if i + 1 > len(v):
                    break
                y = y + v[i] if rel else v[i]
                actual.append((x, y))
                i += 1
            elif c == "C":
                if i + 6 > len(v):
                    break
                p = v[i:i + 6]
                if rel:
                    p = [p[0] + x, p[1] + y, p[2] + x, p[3] + y, p[4] + x, p[5] + y]
                actual += bezier((x, y), (p[0], p[1]), (p[2], p[3]), (p[4], p[5]))
                last_ctrl = (p[2], p[3])
                x, y = p[4], p[5]
                i += 6
            elif c == "S":
                if i + 4 > len(v):
                    break
                p = v[i:i + 4]
                if rel:
                    p = [p[0] + x, p[1] + y, p[2] + x, p[3] + y]
                c1 = (2 * x - last_ctrl[0], 2 * y - last_ctrl[1]) if last_ctrl else (x, y)
                actual += bezier((x, y), c1, (p[0], p[1]), (p[2], p[3]))
                last_ctrl = (p[0], p[1])
                x, y = p[2], p[3]
                i += 4
            elif c == "Q":
                if i + 4 > len(v):
                    break
                p = v[i:i + 4]
                if rel:
                    p = [p[0] + x, p[1] + y, p[2] + x, p[3] + y]
                c1 = (x + 2 / 3 * (p[0] - x), y + 2 / 3 * (p[1] - y))
                c2 = (p[2] + 2 / 3 * (p[0] - p[2]), p[3] + 2 / 3 * (p[1] - p[3]))
                actual += bezier((x, y), c1, c2, (p[2], p[3]))
                last_ctrl = (p[0], p[1])
                x, y = p[2], p[3]
                i += 4
            elif c == "T":
                if i + 2 > len(v):
                    break
                q = (2 * x - last_ctrl[0], 2 * y - last_ctrl[1]) if last_ctrl else (x, y)
                nx, ny = v[i], v[i + 1]
                if rel:
                    nx, ny = x + nx, y + ny
                c1 = (x + 2 / 3 * (q[0] - x), y + 2 / 3 * (q[1] - y))
                c2 = (nx + 2 / 3 * (q[0] - nx), ny + 2 / 3 * (q[1] - ny))
                actual += bezier((x, y), c1, c2, (nx, ny))
                last_ctrl = q
                x, y = nx, ny
                i += 2
            elif c == "A":
                if i + 7 > len(v):
                    break
                nx, ny = v[i + 5], v[i + 6]
                if rel:
                    nx, ny = x + nx, y + ny
                actual.append((nx, ny))
                x, y = nx, ny
                i += 7
            else:
                break
            if i >= len(v):
                break
    if actual:
        polis.append(actual)
    return polis


# --------------------------------------------------------------------------
# Recorrido del árbol
# --------------------------------------------------------------------------
class Elem:
    __slots__ = ("tipo", "bbox", "texto", "segs", "grupo_mol", "nodo", "ruta", "es_flecha", "inserto")


def heredado(attrs_stack, clave, defecto=None):
    for a in reversed(attrs_stack):
        if clave in a:
            return a[clave]
    return defecto


def estilo(el):
    d = dict(el.attrib)
    st = el.get("style")
    if st:
        for par in st.split(";"):
            if ":" in par:
                k, v = par.split(":", 1)
                d[k.strip()] = v.strip()
    return d


def bbox_puntos(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return (min(xs), min(ys), max(xs), max(ys))


def recorrer(root):
    elems = []

    def visitar(el, m, attrs_stack, ruta, nodo, grupo_mol, inserto):
        tag = el.tag.replace(NS, "")
        if tag in ("defs", "clipPath", "marker", "linearGradient", "radialGradient", "filter", "pattern", "style", "title"):
            return
        a = estilo(el)
        eid = el.get("id", "")
        if eid in GRUPOS_EXCLUIDOS:
            return
        if a.get("opacity") and float(a["opacity"]) < 0.5:
            return
        m = mat_mul(m, parse_transform(el.get("transform")))
        attrs_stack = attrs_stack + [a]
        ruta = ruta + ([eid] if eid else [])
        if eid in GRUPOS_INSERTO:
            inserto = eid

        if tag in ("g", "svg"):
            hijos = list(el)
            # nodo_libre: <g id="m_xxx"><g>{molécula}</g><text>...
            es_nodo = eid.startswith("m_") and hijos and hijos[0].tag.replace(NS, "") == "g"
            for k, h in enumerate(hijos):
                gm = grupo_mol
                nd = eid if es_nodo else nodo
                if es_nodo and k == 0:
                    gm = eid
                visitar(h, m, attrs_stack, ruta, nd, gm, inserto)
            return
        if tag == "a":
            for h in el:
                visitar(h, m, attrs_stack, ruta, nodo, grupo_mol, inserto)
            return

        e = Elem()
        e.grupo_mol, e.nodo, e.ruta, e.inserto = grupo_mol, nodo, "/".join(ruta[-2:]), inserto
        e.texto, e.segs, e.es_flecha = None, [], False

        if tag == "text":
            txt = " ".join("".join(el.itertext()).split())
            if not txt:
                return
            try:
                fs = float(str(heredado(attrs_stack, "font-size", "12")).replace("px", ""))
            except ValueError:
                fs = 12
            fam = str(heredado(attrs_stack, "font-family", ""))
            ls = float(str(heredado(attrs_stack, "letter-spacing", "0")).replace("px", "") or 0)
            k = ANCHO_CHAR["mono" if "Mono" in fam or "mono" in fam else "sans"]
            w = len(txt) * (fs * k + ls)
            anchor = heredado(attrs_stack, "text-anchor", "start")
            x = float(re.findall(r"-?[\d.]+", el.get("x", "0"))[0]) if el.get("x") else 0
            y = float(re.findall(r"-?[\d.]+", el.get("y", "0"))[0]) if el.get("y") else 0
            x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
            esquinas = [aplicar(m, x0, y - 0.72 * fs), aplicar(m, x0 + w, y - 0.72 * fs),
                        aplicar(m, x0, y + 0.18 * fs), aplicar(m, x0 + w, y + 0.18 * fs)]
            e.tipo, e.bbox, e.texto = "text", bbox_puntos(esquinas), txt
            elems.append(e)
            return

        polis = []
        if tag == "line":
            p = [float(el.get(k, 0)) for k in ("x1", "y1", "x2", "y2")]
            polis = [[(p[0], p[1]), (p[2], p[3])]]
        elif tag == "path":
            polis = puntos_path(el.get("d", ""))
        elif tag in ("polyline", "polygon"):
            nums = [float(n) for n in re.findall(r"-?[\d.]+", el.get("points", ""))]
            pts = list(zip(nums[0::2], nums[1::2]))
            if tag == "polygon" and pts:
                pts.append(pts[0])
            polis = [pts]
        elif tag in ("rect", "circle", "ellipse"):
            if tag == "rect":
                x, y = float(el.get("x", 0)), float(el.get("y", 0))
                w, h = float(el.get("width", 0) or 0), float(el.get("height", 0) or 0)
            else:
                cx, cy = float(el.get("cx", 0)), float(el.get("cy", 0))
                rx = float(el.get("r", el.get("rx", 0)) or 0)
                ry = float(el.get("r", el.get("ry", 0)) or 0)
                x, y, w, h = cx - rx, cy - ry, 2 * rx, 2 * ry
            polis = [[(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]]
        if not polis:
            return
        polis = [[aplicar(m, *p) for p in pl] for pl in polis if len(pl) >= 1]
        todos = [p for pl in polis for p in pl]
        if not todos:
            return
        e.tipo = tag
        e.bbox = bbox_puntos(todos)
        e.segs = [(pl[i], pl[i + 1]) for pl in polis for i in range(len(pl) - 1)]
        stroke = heredado(attrs_stack, "stroke", "none")
        fill = heredado(attrs_stack, "fill", "black")
        e.es_flecha = (
            grupo_mol is None and tag in ("line", "path", "polyline")
            and stroke not in ("none", None)
            and (a.get("marker-end") or a.get("marker-start") or heredado(attrs_stack, "stroke-dasharray") or fill == "none")
        )
        elems.append(e)

    visitar(root, IDENT, [], [], None, None, None)
    return elems


# --------------------------------------------------------------------------
# Pruebas de colisión
# --------------------------------------------------------------------------
def inter_area(a, b):
    w = min(a[2], b[2]) - max(a[0], b[0])
    h = min(a[3], b[3]) - max(a[1], b[1])
    return w * h if w > 0 and h > 0 else 0


def area(b):
    return max(0, b[2] - b[0]) * max(0, b[3] - b[1])


def encoger(b, d):
    return (b[0] + d, b[1] + d, b[2] - d, b[3] - d)


def seg_corta_caja(p, q, b):
    """Liang–Barsky."""
    x0, y0 = p
    dx, dy = q[0] - p[0], q[1] - p[1]
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, x0 - b[0]), (dx, b[2] - x0), (-dy, y0 - b[1]), (dy, b[3] - y0)):
        if pp == 0:
            if qq < 0:
                return False
        else:
            r = qq / pp
            if pp < 0:
                if r > t1:
                    return False
                t0 = max(t0, r)
            else:
                if r < t0:
                    return False
                t1 = min(t1, r)
    return t0 <= t1


def recortar_extremos(segs, margen):
    """Quita 'margen' px al principio y al final de la polilínea (zonas de anclaje)."""
    if not segs:
        return segs
    longitudes = [math.dist(a, b) for a, b in segs]
    total = sum(longitudes)
    if total <= 2 * margen:
        return []
    out, acc = [], 0.0
    for (a, b), L in zip(segs, longitudes):
        s0, s1 = acc, acc + L
        acc = s1
        lo, hi = max(s0, margen), min(s1, total - margen)
        if hi <= lo or L == 0:
            continue
        t0, t1 = (lo - s0) / L, (hi - s0) / L
        out.append(((a[0] + (b[0] - a[0]) * t0, a[1] + (b[1] - a[1]) * t0),
                    (a[0] + (b[0] - a[0]) * t1, a[1] + (b[1] - a[1]) * t1)))
    return out


def analizar(ruta_svg):
    root = ET.parse(ruta_svg).getroot()
    elems = recorrer(root)
    textos_libres = [e for e in elems if e.tipo == "text" and e.grupo_mol is None and not e.inserto]
    textos_mol = [e for e in elems if e.tipo == "text" and e.grupo_mol is not None and not e.inserto]
    flechas = [e for e in elems if e.es_flecha and not e.inserto]

    # Caja de cada molécula
    mol_bbox = {}
    for e in elems:
        if e.grupo_mol and not e.inserto:
            b = e.bbox
            if e.grupo_mol in mol_bbox:
                o = mol_bbox[e.grupo_mol]
                mol_bbox[e.grupo_mol] = (min(o[0], b[0]), min(o[1], b[1]), max(o[2], b[2]), max(o[3], b[3]))
            else:
                mol_bbox[e.grupo_mol] = b

    problemas = []

    # 1. TEXTO-TEXTO
    todos_textos = textos_libres + textos_mol
    for i in range(len(todos_textos)):
        a = todos_textos[i]
        for j in range(i + 1, len(todos_textos)):
            b = todos_textos[j]
            if a.grupo_mol and a.grupo_mol == b.grupo_mol:
                continue
            ia = inter_area(a.bbox, b.bbox)
            if ia > 0.12 * min(area(a.bbox), area(b.bbox)) and ia > 12:
                problemas.append(("TEXTO-TEXTO", a.bbox, f"«{a.texto[:40]}» ⟂ «{b.texto[:40]}»"))

    # 2. FLECHA-TEXTO
    for f in flechas:
        segs = recortar_extremos(f.segs, 6)
        for t in todos_textos:
            if t.texto in ("", None):
                continue
            caja = encoger(t.bbox, 1.5)
            if caja[2] <= caja[0] or caja[3] <= caja[1]:
                continue
            if f.bbox[2] < caja[0] or f.bbox[0] > caja[2] or f.bbox[3] < caja[1] or f.bbox[1] > caja[3]:
                continue
            if any(seg_corta_caja(p, q, caja) for p, q in segs):
                problemas.append(("FLECHA-TEXTO", t.bbox, f"flecha {f.ruta or f.tipo} cruza «{t.texto[:45]}»"))

    # 3. TEXTO-ESTRUCTURA (rótulos libres y nombres sobre dibujos de moléculas)
    for t in textos_libres:
        for gm, mb in mol_bbox.items():
            caja = encoger(mb, 4)
            ia = inter_area(t.bbox, caja)
            if ia > 0.18 * area(t.bbox) and ia > 20:
                problemas.append(("TEXTO-ESTRUCTURA", t.bbox, f"«{t.texto[:40]}» sobre molécula {gm}"))

    # 4. FLECHA-ESTRUCTURA (excluye 40 px de cada extremo: anclajes legítimos)
    for f in flechas:
        segs = recortar_extremos(f.segs, 40)
        if not segs:
            continue
        for gm, mb in mol_bbox.items():
            caja = encoger(mb, 10)
            if caja[2] <= caja[0] or caja[3] <= caja[1]:
                continue
            if f.bbox[2] < caja[0] or f.bbox[0] > caja[2] or f.bbox[3] < caja[1] or f.bbox[1] > caja[3]:
                continue
            if any(seg_corta_caja(p, q, caja) for p, q in segs):
                problemas.append(("FLECHA-ESTRUCTURA", mb, f"flecha {f.ruta or f.tipo} atraviesa {gm}"))

    # Fuera del lienzo
    W = float(root.get("width", 0))
    H = float(root.get("height", 0))
    for t in textos_libres + textos_mol:
        if t.bbox[2] > W + 2 or t.bbox[0] < -2 or t.bbox[3] > H + 2:
            problemas.append(("FUERA-LIENZO", t.bbox, f"«{t.texto[:40]}»"))

    # Deduplicar
    vistos, unicos = set(), []
    for p in problemas:
        k = (p[0], p[2])
        if k not in vistos:
            vistos.add(k)
            unicos.append(p)
    return unicos, root


def escribir_debug(ruta_svg, problemas, salida):
    with open(ruta_svg, encoding="utf-8") as f:
        s = f.read()
    marcas = []
    colores = {"TEXTO-TEXTO": "#ff0000", "FLECHA-TEXTO": "#ff00ff", "TEXTO-ESTRUCTURA": "#ff8800",
               "FLECHA-ESTRUCTURA": "#0088ff", "FUERA-LIENZO": "#000000"}
    for n, (tipo, b, _) in enumerate(problemas, 1):
        c = colores.get(tipo, "#ff0000")
        marcas.append(f'<rect x="{b[0]:.0f}" y="{b[1]:.0f}" width="{b[2]-b[0]:.0f}" height="{b[3]-b[1]:.0f}" '
                      f'fill="{c}" fill-opacity="0.15" stroke="{c}" stroke-width="3"/>'
                      f'<text x="{b[0]:.0f}" y="{b[1]-3:.0f}" fill="{c}" font-size="16" font-weight="900">{n}</text>')
    s = s.replace("</svg>", "<g id='debug_solapamientos'>" + "".join(marcas) + "</g></svg>")
    with open(salida, "w", encoding="utf-8") as f:
        f.write(s)


if __name__ == "__main__":
    default_svg = "prueba_visual_integrada.svg"
    if not os.path.exists(default_svg):
        dir_s = os.path.dirname(os.path.abspath(__file__))
        cand = os.path.join(os.path.dirname(dir_s), "02_versiones_html", "prueba_visual_integrada.svg")
        if os.path.exists(cand):
            default_svg = cand
    ruta = args[0] if args else default_svg
    problemas, _ = analizar(ruta)
    resumen = {}
    for tipo, b, msg in problemas:
        resumen[tipo] = resumen.get(tipo, 0) + 1
    maxn = 9999
    if "--max" in sys.argv:
        maxn = int(sys.argv[sys.argv.index("--max") + 1])
    for n, (tipo, b, msg) in enumerate(problemas[:maxn], 1):
        print(f"{n:3d}. [{tipo:17s}] ({b[0]:.0f},{b[1]:.0f}) {msg}")
    print("\nRESUMEN:", ", ".join(f"{k}={v}" for k, v in sorted(resumen.items())) or "sin solapamientos ✓")
    print("TOTAL:", len(problemas))
    if "--debug" in sys.argv:
        escribir_debug(ruta, problemas, "solapamientos_debug.svg")
        print("→ solapamientos_debug.svg generado")
    sys.exit(1 if problemas else 0)
