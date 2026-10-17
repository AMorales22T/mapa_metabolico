# =============================================================================
# MÓDULO DE REVISIÓN: Lector de Geometría y Cajas Envolventes del SVG
# =============================================================================
# Archivo original : scripts_generacion/conectar_rutas.py (líneas 219 a 333 de 850)
# Descripción      : Recorre el árbol XML aplicando transformaciones afines y calcula el bounding box de cada elemento.
# =============================================================================

# ===========================================================================
# 1. LECTURA DEL SVG
# ===========================================================================
class Elem:
    __slots__ = ("tipo", "bbox", "segs", "ids", "mol", "opac", "solido", "texto")


def _num(v, defecto=0.0):
    try:
        return float(re.findall(r"-?[\d.]+(?:e-?\d+)?", str(v))[0])
    except (IndexError, ValueError):
        return defecto


def leer_svg(root):
    elems = []

    def visitar(el, m, pila, ids, mol, opac):
        tag = el.tag.replace(NS, "")
        if tag in ("defs", "clipPath", "marker", "linearGradient", "radialGradient",
                   "filter", "pattern", "style", "title", "script"):
            return
        a = ds.estilo(el)
        eid = el.get("id", "")
        if eid in GRUPOS_IGNORADOS:
            return
        if a.get("opacity"):
            opac *= _num(a["opacity"], 1.0)
        if opac < 0.12:
            return
        m = ds.mat_mul(m, ds.parse_transform(el.get("transform")))
        pila = pila + [a]
        ids = ids + ((eid,) if eid else ())

        if tag in ("g", "svg", "a"):
            hijos = list(el)
            es_nodo = eid.startswith("m_") and hijos and hijos[0].tag.replace(NS, "") == "g"
            for k, h in enumerate(hijos):
                visitar(h, m, pila, ids, (eid if es_nodo and k == 0 else mol), opac)
            return

        e = Elem()
        e.ids, e.mol, e.opac, e.segs, e.texto, e.solido = ids, mol, opac, [], None, False
        if tag == "text":
            txt = " ".join("".join(el.itertext()).split())
            if not txt:
                return
            fs = _num(ds.heredado(pila, "font-size", "12"), 12)
            fam = str(ds.heredado(pila, "font-family", ""))
            ls = _num(ds.heredado(pila, "letter-spacing", "0"), 0)
            k = ds.ANCHO_CHAR["mono" if "mono" in fam.lower() else "sans"]
            w = len(txt) * (fs * k + ls)
            anchor = ds.heredado(pila, "text-anchor", "start")
            x, y = _num(el.get("x", 0)), _num(el.get("y", 0))
            x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
            esq = [ds.aplicar(m, x0, y - 0.75 * fs), ds.aplicar(m, x0 + w, y - 0.75 * fs),
                   ds.aplicar(m, x0, y + 0.22 * fs), ds.aplicar(m, x0 + w, y + 0.22 * fs)]
            e.tipo, e.bbox, e.texto = "text", ds.bbox_puntos(esq), txt
            elems.append(e)
            return

        polis = []
        if tag == "line":
            p = [_num(el.get(k, 0)) for k in ("x1", "y1", "x2", "y2")]
            polis = [[(p[0], p[1]), (p[2], p[3])]]
        elif tag == "path":
            polis = ds.puntos_path(el.get("d", ""))
        elif tag in ("polyline", "polygon"):
            nums = [float(n) for n in re.findall(r"-?[\d.]+", el.get("points", ""))]
            pts = list(zip(nums[0::2], nums[1::2]))
            if tag == "polygon" and pts:
                pts.append(pts[0])
            polis = [pts]
        elif tag in ("rect", "circle", "ellipse"):
            if tag == "rect":
                x, y = _num(el.get("x", 0)), _num(el.get("y", 0))
                w, h = _num(el.get("width", 0)), _num(el.get("height", 0))
            else:
                cx, cy = _num(el.get("cx", 0)), _num(el.get("cy", 0))
                rx = _num(el.get("r", el.get("rx", 0)))
                ry = _num(el.get("r", el.get("ry", 0)))
                x, y, w, h = cx - rx, cy - ry, 2 * rx, 2 * ry
            polis = [[(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]]
        elif tag == "image":
            x, y = _num(el.get("x", 0)), _num(el.get("y", 0))
            w, h = _num(el.get("width", 0)), _num(el.get("height", 0))
            polis = [[(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)]]
        polis = [[ds.aplicar(m, *p) for p in pl] for pl in polis if pl]
        todos = [p for pl in polis for p in pl]
        if not todos:
            return
        e.tipo = tag
        e.bbox = ds.bbox_puntos(todos)
        e.segs = [(pl[i], pl[i + 1]) for pl in polis for i in range(len(pl) - 1)]
        fill = str(ds.heredado(pila, "fill", "black"))
        fop = _num(ds.heredado(pila, "fill-opacity", "1"), 1.0)
        e.solido = fill not in ("none", "transparent") and fop * opac >= 0.3
        if tag == "image":
            e.solido = True
        elems.append(e)

    visitar(root, ds.IDENT, [], (), None, 1.0)
    return elems


def cajas_por_id(elems):
    cajas = {}
    for e in elems:
        for i in e.ids:
            b = cajas.get(i)
            cajas[i] = e.bbox if b is None else (min(b[0], e.bbox[0]), min(b[1], e.bbox[1]),
                                                   max(b[2], e.bbox[2]), max(b[3], e.bbox[3]))
    return cajas


