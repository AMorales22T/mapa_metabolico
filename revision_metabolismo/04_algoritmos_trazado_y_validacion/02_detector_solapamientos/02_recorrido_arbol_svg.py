# =============================================================================
# MÓDULO DE REVISIÓN: Extractor y Clasificador de Elementos del SVG
# =============================================================================
# Archivo original : scripts_generacion/detectar_solapamientos.py (líneas 248 a 358 de 552)
# Descripción      : Recorre el documento identificando textos libres, textos de moléculas, estructuras químicas y flechas.
# =============================================================================

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


