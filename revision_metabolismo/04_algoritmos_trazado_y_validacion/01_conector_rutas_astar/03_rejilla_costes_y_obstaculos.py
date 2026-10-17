# =============================================================================
# MÓDULO DE REVISIÓN: Rejilla de Costes y Rasterización de Obstáculos
# =============================================================================
# Archivo original : scripts_generacion/conectar_rutas.py (líneas 334 a 449 de 850)
# Descripción      : Clase Rejilla y función construir_rejilla que penaliza textos, moléculas, lupas y flechas previas.
# =============================================================================

# ===========================================================================
# 2. REJILLA DE COSTES
# ===========================================================================
class Rejilla:
    def __init__(self, ancho, alto, celda):
        self.c = celda
        self.W = int(math.ceil(ancho / celda))
        self.H = int(math.ceil(alto / celda))
        self.coste = [0] * (self.W * self.H)

    def idx(self, cx, cy):
        return cy * self.W + cx

    def celda_de(self, x, y):
        return (min(self.W - 1, max(0, int(x // self.c))), min(self.H - 1, max(0, int(y // self.c))))

    def centro(self, i):
        return ((i % self.W + 0.5) * self.c, (i // self.W + 0.5) * self.c)

    def caja(self, b, valor, margen=0.0):
        x0, y0 = self.celda_de(b[0] - margen, b[1] - margen)
        x1, y1 = self.celda_de(b[2] + margen, b[3] + margen)
        C, W = self.coste, self.W
        for cy in range(y0, y1 + 1):
            fila = cy * W
            for cx in range(x0, x1 + 1):
                if C[fila + cx] < valor:
                    C[fila + cx] = valor

    def segmento(self, p, q, valor, halo=0, valor_halo=0):
        L = math.dist(p, q)
        n = max(1, int(L / (self.c * 0.4)))
        C, W, H = self.coste, self.W, self.H
        vistos = set()
        for k in range(n + 1):
            t = k / n
            cx, cy = self.celda_de(p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t)
            if (cx, cy) in vistos:
                continue
            vistos.add((cx, cy))
            if halo:
                for dy in range(-halo, halo + 1):
                    for dx in range(-halo, halo + 1):
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < W and 0 <= ny < H and C[ny * W + nx] < valor_halo:
                            C[ny * W + nx] = valor_halo
            i = cy * W + cx
            if C[i] < valor:
                C[i] = valor

    def coste_caja(self, b):
        x0, y0 = self.celda_de(b[0], b[1])
        x1, y1 = self.celda_de(b[2], b[3])
        s = 0
        for cy in range(y0, y1 + 1):
            fila = cy * self.W
            for cx in range(x0, x1 + 1):
                s += self.coste[fila + cx]
        return s


def construir_rejilla(elems, cajas, ancho, alto, celda):
    rj = Rejilla(ancho, alto, celda)
    mol_cajas = {}
    duras = []
    for e in elems:
        if any(i in GRUPOS_INSERTO for i in e.ids):
            continue
        if e.mol:
            b = mol_cajas.get(e.mol)
            mol_cajas[e.mol] = e.bbox if b is None else (min(b[0], e.bbox[0]), min(b[1], e.bbox[1]),
                                                           max(b[2], e.bbox[2]), max(b[3], e.bbox[3]))
            continue
        bw, bh = e.bbox[2] - e.bbox[0], e.bbox[3] - e.bbox[1]
        if e.tipo == "text":
            duras.append((e.bbox, 4))
            continue
        en_mito = GRUPO_MITO in e.ids
        cerrado = e.tipo in ("rect", "circle", "ellipse", "polygon", "image") or (
            e.tipo == "path" and e.segs and math.dist(e.segs[0][0], e.segs[-1][1]) < 2)
        if e.solido and cerrado and bw < 3000 and bh < 1500 and not (en_mito and e.tipo == "path"):
            if bw * bh < 150 and e.opac < 0.5:
                continue            # partículas decorativas
            duras.append((e.bbox, 3))
            continue
        # Trazos (flechas, líneas, contornos)
        if bw > 5000 and bh > 4000:
            continue                # fondo del lienzo
        if en_mito and e.tipo == "path":
            val, halo, vh = MEMBRANA, 0, 0
        elif e.opac < 0.5:
            val, halo, vh = TRAZO_TENUE, 0, 0
        else:
            val, halo, vh = TRAZO, 1, TRAZO_HALO
        for p, q in e.segs:
            rj.segmento(p, q, val, halo, vh)
    # Halo suave y cuerpo duro
    for b, mg in duras:
        rj.caja(b, HALO_DURO, mg + rj.c)
    for b in mol_cajas.values():
        rj.caja(b, HALO_DURO, 6 + rj.c)
    for b, mg in duras:
        rj.caja(b, DURO, mg)
    for b in mol_cajas.values():
        rj.caja(b, DURO, 6)
    for g in GRUPOS_INSERTO:
        if g in cajas:
            rj.caja(cajas[g], DURO, 8)
    # Torrente sanguíneo y bordes del lienzo: prohibidos
    rj.caja((0, 0, ancho, 80), DURO)
    rj.caja((0, 0, 12, alto), DURO)
    rj.caja((ancho - 12, 0, ancho, alto), DURO)
    rj.caja((0, alto - 12, ancho, alto), DURO)
    return rj


