# =============================================================================
# MÓDULO DE REVISIÓN: Simplificación Geométrica, Chaflanes Bézier y Rótulos
# =============================================================================
# Archivo original : scripts_generacion/conectar_rutas.py (líneas 550 a 670 de 850)
# Descripción      : Funciones simplificar, path_redondeado y colocar_rotulo (elige el tramo más despejado para el texto).
# =============================================================================

# ===========================================================================
# 4. GEOMETRÍA DEL TRAZADO
# ===========================================================================
def simplificar(pts):
    if len(pts) < 3:
        return pts
    out = [pts[0]]
    for k in range(1, len(pts) - 1):
        a, b, c = out[-1], pts[k], pts[k + 1]
        if abs((b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])) > 1e-6:
            out.append(b)
    out.append(pts[-1])
    return out


def punto_en_borde(b, p, holgura):
    """Punto del borde de la caja b más cercano a p, desplazado 'holgura' hacia p."""
    x = min(max(p[0], b[0]), b[2])
    y = min(max(p[1], b[1]), b[3])
    d = math.dist((x, y), p)
    if d < 1e-6:
        return (x, y)
    return (x + (p[0] - x) / d * holgura, y + (p[1] - y) / d * holgura)


def alinear_stub(b, p0, p1):
    """Ajusta el punto de contacto para que el último tramo entre perpendicular a la cara."""
    x, y = p1
    if y < b[1] or y > b[3]:
        x = min(max(x, b[0] + 4), b[2] - 4)
        return (x, p0[1]) if abs(p0[0] - x) > 0.1 else p0
    return p0


def path_redondeado(pts, radio=16):
    if len(pts) < 2:
        return ""
    d = [f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"]
    for k in range(1, len(pts) - 1):
        a, p, b = pts[k - 1], pts[k], pts[k + 1]
        la, lb = math.dist(a, p), math.dist(p, b)
        if la < 1e-6 or lb < 1e-6:
            continue
        r = min(radio, la / 2, lb / 2)
        p1 = (p[0] + (a[0] - p[0]) / la * r, p[1] + (a[1] - p[1]) / la * r)
        p2 = (p[0] + (b[0] - p[0]) / lb * r, p[1] + (b[1] - p[1]) / lb * r)
        d.append(f"L {p1[0]:.1f} {p1[1]:.1f} Q {p[0]:.1f} {p[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}")
    d.append(f"L {pts[-1][0]:.1f} {pts[-1][1]:.1f}")
    return " ".join(d)


def recortar_final(pts, cuanto):
    if len(pts) < 2:
        return pts
    a, b = pts[-2], pts[-1]
    L = math.dist(a, b)
    if L <= cuanto + 2:
        return pts
    return pts[:-1] + [(b[0] - (b[0] - a[0]) / L * cuanto, b[1] - (b[1] - a[1]) / L * cuanto)]


# ===========================================================================
# 5. RÓTULOS
# ===========================================================================
FS_ROTULO = 10.5


def ancho_texto(t, fs=FS_ROTULO):
    return len(t) * fs * ds.ANCHO_CHAR["sans"]


def colocar_rotulo(rj, pts, texto):
    """Busca la posición más despejada junto a la conexión. Devuelve (x, y, anchor, bbox) o None."""
    w = ancho_texto(texto)
    hh = FS_ROTULO
    total = sum(math.dist(pts[k], pts[k + 1]) for k in range(len(pts) - 1))
    if total < 1:
        return None
    segs = list(zip(pts[:-1], pts[1:]))
    candidatos = []
    acc = 0.0
    for a, b in segs:
        L = math.dist(a, b)
        if L < 24:
            acc += L
            continue
        ux, uy = (b[0] - a[0]) / L, (b[1] - a[1]) / L
        n = max(1, int(L / 40))
        for k in range(n + 1):
            t = 0.15 + 0.7 * k / n if n else 0.5
            px, py = a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t
            pos_global = (acc + L * t) / total
            if pos_global < 0.08 or pos_global > 0.92:
                continue
            if abs(uy) < 0.35:      # tramo horizontal: encima / debajo
                opciones = [(px, py - 7, "middle"), (px, py + hh + 5, "middle")]
            elif abs(ux) < 0.35:    # tramo vertical: izquierda / derecha
                opciones = [(px + 8, py + hh * 0.35, "start"), (px - 8, py + hh * 0.35, "end")]
            else:                   # diagonal
                opciones = [(px + 9, py + hh * 0.35, "start"), (px - 9, py + hh * 0.35, "end"),
                            (px, py - 9, "middle"), (px, py + hh + 7, "middle")]
            for x, y, anc in opciones:
                x0 = x - w / 2 if anc == "middle" else (x - w if anc == "end" else x)
                caja = (x0 - 3, y - 0.75 * FS_ROTULO - 2, x0 + w + 3, y + 0.22 * FS_ROTULO + 2)
                candidatos.append((x, y, anc, caja, abs(pos_global - 0.5)))
        acc += L
    mejor, mejor_s = None, 1e18
    for x, y, anc, caja, dmed in candidatos:
        if caja[0] < 15 or caja[2] > rj.W * rj.c - 15 or caja[1] < 95:
            continue
        if any(ds.seg_corta_caja(p, q, caja) for p, q in segs):
            continue
        cc = rj.coste_caja(caja)
        s = cc * 1000 + dmed * 40
        if s < mejor_s:
            mejor, mejor_s = (x, y, anc, caja), s
    if mejor is None or mejor_s >= TRAZO * 500:
        return None
    return mejor


