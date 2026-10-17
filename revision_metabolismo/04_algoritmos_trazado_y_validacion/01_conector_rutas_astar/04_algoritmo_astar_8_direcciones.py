# =============================================================================
# MÓDULO DE REVISIÓN: Motor de Búsqueda A* Direccional con Penalización de Giros
# =============================================================================
# Archivo original : scripts_generacion/conectar_rutas.py (líneas 450 a 549 de 850)
# Descripción      : Funciones anillo (puntos de salida/entrada) y astar (búsqueda heurística en 8 direcciones).
# =============================================================================

# ===========================================================================
# 3. ENRUTADOR A*
# ===========================================================================
DIRS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
NORMAL = {"right": 0, "bottom": 2, "left": 4, "top": 6}


def anillo(rj, b, lado=None, margen=8.0):
    """Celdas justo fuera de la caja b (origen/destino) con su dirección normal saliente."""
    c = rj.c
    x0, y0 = rj.celda_de(b[0] - margen - c, b[1] - margen - c)
    x1, y1 = rj.celda_de(b[2] + margen + c, b[3] + margen + c)
    celdas = {}

    def add(cx, cy, d):
        if 0 <= cx < rj.W and 0 <= cy < rj.H:
            celdas[rj.idx(cx, cy)] = d

    def tramo(a, z):
        if z - a < 4:
            return range(a, z + 1)
        rec = max(1, int((z - a) * 0.12))
        return range(a + rec, z - rec + 1)

    lados = [lado] if lado else ["top", "bottom", "left", "right"]
    for l in lados:
        if l == "top":
            for cx in tramo(x0 + 1, x1 - 1):
                add(cx, y0, 6)
        elif l == "bottom":
            for cx in tramo(x0 + 1, x1 - 1):
                add(cx, y1, 2)
        elif l == "left":
            for cy in tramo(y0 + 1, y1 - 1):
                add(x0, cy, 4)
        elif l == "right":
            for cy in tramo(y0 + 1, y1 - 1):
                add(x1, cy, 0)
    return celdas


def astar(rj, inicios, metas, caja_meta, peso_h=1.15):
    W, H, C = rj.W, rj.H, rj.coste
    gx0, gy0 = rj.celda_de(caja_meta[0], caja_meta[1])
    gx1, gy1 = rj.celda_de(caja_meta[2], caja_meta[3])

    def h(i):
        x, y = i % W, i // W
        dx = max(0, gx0 - x, x - gx1)
        dy = max(0, gy0 - y, y - gy1)
        return (max(dx, dy) + 0.4142 * min(dx, dy)) * peso_h

    g = {}
    padre = {}
    heap = []
    for i, d in inicios.items():
        s = i * 8 + d
        g[s] = C[i] * 0.2
        padre[s] = None
        heapq.heappush(heap, (g[s] + h(i), g[s], s))
    expandidos = 0
    while heap:
        f, gc, s = heapq.heappop(heap)
        if gc > g.get(s, 1e18):
            continue
        i, d = divmod(s, 8)
        if i in metas:
            # Penaliza llegar de lado (queremos entrar perpendicular a la cara)
            dentro = (metas[i] + 4) % 8
            giro = min(abs(d - dentro), 8 - abs(d - dentro))
            if giro <= 2:
                camino = []
                while s is not None:
                    camino.append(s // 8)
                    s = padre[s]
                return camino[::-1], gc, expandidos
        expandidos += 1
        if expandidos > 2_500_000:
            break
        x, y = i % W, i // W
        for giro in (-2, -1, 0, 1, 2):
            nd = (d + giro) % 8
            dx, dy = DIRS[nd]
            nx, ny = x + dx, y + dy
            if not (0 <= nx < W and 0 <= ny < H):
                continue
            ni = ny * W + nx
            paso = 1.4142 if dx and dy else 1.0
            c = C[ni]
            if dx and dy:   # diagonal: no "cortar esquinas" de obstáculos
                c = max(c, (C[y * W + nx] + C[ny * W + x]) * 0.5)
            ng = gc + paso * (1.0 + c) + GIRO[abs(giro)]
            ns = ni * 8 + nd
            if ng < g.get(ns, 1e18):
                g[ns] = ng
                padre[ns] = s
                heapq.heappush(heap, (ng + h(ni), ng, ns))
    return None, None, expandidos


