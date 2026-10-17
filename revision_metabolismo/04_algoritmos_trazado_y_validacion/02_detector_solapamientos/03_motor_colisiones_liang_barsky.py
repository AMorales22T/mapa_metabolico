# =============================================================================
# MÓDULO DE REVISIÓN: Motor de Detección de Colisiones (Liang-Barsky y Cajas)
# =============================================================================
# Archivo original : scripts_generacion/detectar_solapamientos.py (líneas 359 a 511 de 552)
# Descripción      : Detecta solapamientos TEXTO-TEXTO, FLECHA-TEXTO, TEXTO-ESTRUCTURA, FLECHA-ESTRUCTURA y FUERA-LIENZO.
# =============================================================================

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
    vb = root.get("viewBox")
    if vb:
        vx, vy, vw, vh = [float(x) for x in vb.split()]
        min_x, max_x = vx, vx + vw
        min_y, max_y = vy, vy + vh
    else:
        min_x = 0.0
        min_y = 0.0
        max_x = float(root.get("width", 0))
        max_y = float(root.get("height", 0))

    for t in textos_libres + textos_mol:
        if t.bbox[2] > max_x + 2 or t.bbox[0] < min_x - 2 or t.bbox[3] > max_y + 2 or t.bbox[1] < min_y - 2:
            problemas.append(("FUERA-LIENZO", t.bbox, f"«{t.texto[:40]}»"))

    # Deduplicar
    vistos, unicos = set(), []
    for p in problemas:
        k = (p[0], p[2])
        if k not in vistos:
            vistos.add(k)
            unicos.append(p)
    return unicos, root

