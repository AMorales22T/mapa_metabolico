#!/usr/bin/env python3
"""
CONECTOR AUTOMÁTICO DE RUTAS DEL MAPA METABÓLICO INTEGRADO
==========================================================
Genera el mapa base (generar_prueba_visual_integrada.py) SIN MODIFICAR NADA de su
contenido y le añade, en una capa independiente, las conexiones entre rutas
(piruvato ➔ mitocondria, citrato ➔ lipogénesis, NH₄⁺ ➔ urea, R5P ➔ PRPP, etc.).

Cómo funciona
-------------
1. Lee el SVG del mapa y calcula la caja de cada rótulo, molécula, recuadro,
   lupa y flecha existente.
2. Rasteriza todo en una rejilla de costes:
     · texto / moléculas / recuadros / lupas  ➔ prohibido (coste muy alto)
     · flechas existentes                      ➔ caro cruzarlas, carísimo recorrerlas
     · membranas mitocondriales               ➔ se pueden cruzar (coste bajo)
3. Cada conexión se traza con A* (8 direcciones, penalización por giro) desde el
   borde del metabolito origen hasta el borde del destino. Si hay transportador
   (MPC, CIC, AGC…) la ruta pasa obligatoriamente por él.
4. Cada conexión trazada se convierte en obstáculo para las siguientes, así que
   las conexiones nuevas tampoco se solapan entre sí. Su rótulo se coloca en el
   tramo más despejado.
5. Escribe:  prueba_visual_integrada_conectada.svg / .html / _preview.png

Uso
---
    python3 conectar_rutas.py              # genera todo
    python3 conectar_rutas.py --celda 10   # rejilla más fina (más lento, más preciso)
    python3 conectar_rutas.py --sin-png    # no renderiza la vista previa

Para añadir/quitar conexiones edita la lista CONEXIONES (más abajo).
"""
import heapq
import math
import os
import re
import shutil
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_SCRIPT) if os.path.basename(DIR_SCRIPT) == "01_fuente_python" else DIR_SCRIPT
DIR_HTML = os.path.join(DIR_BASE, "02_versiones_html")
DIR_PREVIEWS = os.path.join(DIR_BASE, "04_capturas_y_pruebas")
sys.path.insert(0, DIR_SCRIPT)
sys.path.insert(0, DIR_BASE)

import detectar_solapamientos as ds  # noqa: E402  (reutiliza su geometría SVG)

NS = "{http://www.w3.org/2000/svg}"

# ---------------------------------------------------------------------------
# Transportadores / anclas sin id propio en el SVG (coordenadas absolutas)
# ---------------------------------------------------------------------------
MPC = (1645, 2105, 1715, 2147)          # Carrier de Piruvato (MPC1/2)
CIC = (1915, 2115, 1975, 2143)          # Carrier de Citrato
AGC = (2015, 2110, 2105, 2165)          # Carrier de Glutamato (AGC / GC1) con rótulo inferior
CITRINA = (4330, 2135, 4510, 2205)      # Carrier SLC25A13 (Citrina) en MMI con rótulo
ORNT1 = (4570, 2135, 4710, 2205)        # Carrier SLC25A15 (ORNT1) en MMI con rótulo
TXT_SUCCINIL = (788, 2822, 962, 2840)   # rótulo "➔ Succinil-CoA [4C] (Krebs)" (vía Propionil-CoA)


def sangre(x):
    """Punto de llegada al torrente sanguíneo (cara interna de la membrana plasmática)."""
    return {"rect": (x - 25, 84, x + 25, 92), "lado": "bottom"}


# ---------------------------------------------------------------------------
# CONEXIONES ENTRE RUTAS  (orden = prioridad de trazado)
#   src / dst : {"id": <id SVG>} o {"rect": (x1, y1, x2, y2)}
#               "lado": "top" | "bottom" | "left" | "right"  (opcional, fuerza la cara)
#   via       : caja de un transportador por el que debe pasar (entra/sale por
#               las caras indicadas en via_in / via_out)
# ---------------------------------------------------------------------------
NARANJA, MORADO, VERDE, AZUL = "#ea580c", "#7c3aed", "#059669", "#0284c7"
TEAL, MARRON, AZUL_N, ROSA = "#0d9488", "#b45309", "#2563eb", "#db2777"
ROJO, GRANATE, PIZARRA = "#dc2626", "#be123c", "#475569"

CONEXIONES = [
    # --- Carbohidratos ➔ Mitocondria & Gluconeogénesis ------------------------------
    dict(id="piruvato_mpc", src={"id": "m_pyr_cito"}, dst={"rect": MPC, "lado": "top"},
         color=NARANJA, rotulo="Piruvato ➔ MPC (Matriz)"),
    dict(id="mpc_pdh_accoa", src={"rect": MPC, "lado": "bottom"}, dst={"id": "m_accoa"},
         color=NARANJA, rotulo="PDH: Piruvato ➔ Acetil-CoA"),
    dict(id="sangre_lactato", src=sangre(1620), dst={"id": "m_lactato", "lado": "top"},
         color=MORADO, rotulo="Lactato (Ciclo de Cori) ➔"),
    dict(id="sangre_glicerol", src=sangre(980), dst={"id": "m_glicerol", "lado": "top"},
         color=MORADO, rotulo="Glicerol (Lipólisis TAG) ➔"),
    dict(id="g6p_g1p", src={"id": "m_g6p"}, dst={"id": "m_g1p"},
         color=MARRON, rotulo="PGM: G6P ⇄ G1P (Glucógeno)"),
    dict(id="g1p_g6p", src={"id": "m_g1p"}, dst={"id": "m_g6p"},
         color=MARRON, rotulo="Glucogenólisis ➔ G6P"),
    dict(id="piruvato_ala_pool", src={"id": "m_pyr_ala_integ"}, dst={"id": "m_pyr_cito"},
         color=NARANJA, rotulo="Pool de Piruvato (ALT)"),

    # --- Pentosas ⇄ Glucólisis / Nucleótidos ----------------------------------------
    dict(id="s7p_f6p", src={"id": "m_s7p"}, dst={"id": "m_f6p"},
         color=VERDE, rotulo="Transaldolasa ➔ F6P"),
    dict(id="xu5p_gap", src={"id": "m_xu5p"}, dst={"id": "m_gap"},
         color=VERDE, rotulo="Transcetolasa ➔ GAP"),
    dict(id="e4p_f6p", src={"id": "m_e4p"}, dst={"id": "m_f6p"},
         color=VERDE, rotulo="Transaldolasa ➔ F6P"),
    dict(id="r5p_prpp", src={"id": "m_r5p"}, dst={"id": "m_nuc_prpp", "lado": "left"},
         color=VERDE, rotulo="Ribosa-5-P ➔ PRPP (Nucleótidos)"),

    # --- Krebs ⇄ Lípidos & Respiración Celular --------------------------------------
    dict(id="citrato_cic", src={"id": "m_citrato"}, dst={"id": "m_citrato_cito"},
         via=CIC, via_in="bottom", via_out="top",
         color=AZUL, rotulo="Lanzadera de Citrato (CIC)"),
    dict(id="acetilcoa_colesterol", src={"id": "m_acetil_coa_cito"}, dst={"id": "m_acetoac_col"},
         color=MARRON, rotulo="Tiolasa ➔ Colesterol"),
    dict(id="betaox_krebs", src={"id": "m_acetil_coa_beta"}, dst={"id": "m_accoa"},
         color=NARANJA, rotulo="Acetil-CoA (β-ox) ➔ Krebs"),
    dict(id="betaox_cetogenesis", src={"id": "m_acetil_coa_beta"}, dst={"id": "m_acetoac_coa"},
         color=ROSA, rotulo="Tiolasa ➔ Cetogénesis"),
    dict(id="propionil_succinil", src={"rect": TXT_SUCCINIL, "lado": "right"}, dst={"id": "m_succoa"},
         color=NARANJA, rotulo="Propionil ➔ Succinil-CoA"),
    dict(id="krebs_cte", src={"id": "m_succinato"}, dst={"id": "lupa_cadena_respiratoria", "lado": "left"},
         color=PIZARRA, rotulo="NADH / FADH₂ ➔ Cadena Respiratoria"),
    dict(id="lanz_malato_krebs", src={"id": "lupa_lanzadera_malato_aspartato", "lado": "bottom"}, dst={"id": "m_malato"},
         color=AZUL, rotulo="Malato mitocondrial (NADH) ➔ Krebs"),

    # --- Lípidos: Captación, Síntesis y Secreción a Sangre --------------------------
    dict(id="palmitato_sangre_cito", src={"id": "m_palmitato_sangre"}, dst={"id": "m_palmitato_cito"},
         color=NARANJA, rotulo="CD36 / FATP: Captación Palmitato"),
    dict(id="palmitato_pool", src={"id": "m_palmitato_libre"}, dst={"id": "m_palmitato_cito"},
         color=NARANJA, rotulo="Palmitato de novo ➔ Pool citosólico"),
    dict(id="colesterol_sangre", src={"id": "m_colesterol_integ"}, dst=sangre(3680),
         color=MARRON, rotulo="VLDL / HDL: Colesterol ➔ Sangre"),
    dict(id="cetonicos_sangre", src={"id": "m_betahidroxi"}, dst=sangre(40),
         color=ROSA, rotulo="Cuerpos cetónicos ➔ Sangre"),
    dict(id="acetoacetato_sangre", src={"id": "m_acetoacetato"}, dst=sangre(80),
         color=ROSA, rotulo="Acetoacetato ➔ Sangre"),

    # --- Nitrógeno & Destinos Esqueletos Carbonados AA ------------------------------
    dict(id="glutamato_agc", src={"id": "m_glu_integ"}, dst={"id": "m_glu_mito_integ"},
         via=AGC, via_in="top", via_out="bottom",
         color=TEAL, rotulo="Glutamato ➔ AGC (Matriz)"),
    dict(id="akg_gldh_krebs", src={"id": "m_akg_gldh_integ"}, dst={"id": "m_akg"},
         color=MARRON, rotulo="α-KG ➔ Ciclo de Krebs"),
    dict(id="nh4_urea", src={"id": "m_nh4_integ"}, dst={"id": "m_u_sustratos_inicio"},
         color=AZUL_N, rotulo="NH₄⁺ ➔ CPS-1 (Ciclo de la Urea)"),
    dict(id="gln_sangre", src={"id": "m_gln_integ"}, dst=sangre(2340),
         color=TEAL, rotulo="Glutamina ➔ Sangre"),
    dict(id="tyr_fumarato", src={"id": "m_tyr_aa"}, dst={"id": "m_fumarato"},
         color=VERDE, rotulo="FAH: Fumarato ➔ Krebs"),
    dict(id="tyr_acetoacetato", src={"id": "m_tyr_aa"}, dst={"id": "m_acetoacetato"},
         color=ROSA, rotulo="FAH: Acetoacetato ➔ Cuerpos Cetónicos"),
    dict(id="cistat_propionil", src={"id": "m_cistat_aa"}, dst={"id": "m_prop_aa_matriz"},
         color=NARANJA, rotulo="CTH: Cistationina ➔ Propionil-CoA"),

    # --- Ciclo de la Urea & Shunt Biciclo --------------------------------------------
    dict(id="citrulina_translocacion", src={"id": "m_u_citrulina_mito"}, dst={"id": "m_u_citrulina_cito"},
         via=CITRINA, via_in="bottom", via_out="top",
         color=TEAL, rotulo="SLC25A13 (Citrina): Citrulina ➔ Citosol"),
    dict(id="ornitina_retorno", src={"id": "m_u_ornitina_cito"}, dst={"id": "m_u_ornitina_mito"},
         via=ORNT1, via_in="top", via_out="bottom",
         color=AZUL_N, rotulo="ORNT1: Retorno Ornitina ➔ Matriz"),
    dict(id="oaa_got2_asp", src={"id": "m_oaa"}, dst={"id": "m_u_aspartato"},
         color=TEAL, rotulo="GOT2: OAA ➔ Aspartato"),
    dict(id="biciclo_krebs", src={"id": "m_u_fumarato"}, dst={"id": "m_u_aspartato"},
         color=NARANJA, rotulo="Biciclo: Fumarato ➔ Malato ➔ OAA ➔ Asp"),
    dict(id="urea_fumarato_krebs", src={"id": "m_u_fumarato"}, dst={"id": "m_fumarato"},
         color=NARANJA, rotulo="Fumarato (ASL) ➔ Krebs"),
    dict(id="urea_sangre", src={"id": "m_u_urea"}, dst=sangre(4556),
         color=ROJO, rotulo="Urea ➔ Sangre (Riñón)"),

    # --- Nucleótidos & Lanzaderas Redox ----------------------------------------------
    dict(id="glutamina_cps2", src={"id": "m_gln_integ"}, dst={"id": "m_nuc_cp"},
         color=TEAL, rotulo="Gln ➔ CPS-II (Pirimidinas)"),
    dict(id="amp_hipoxantina", src={"id": "m_nuc_amp"}, dst={"id": "m_deg_hipo"},
         color=GRANATE, rotulo="AMP ➔ IMP ➔ Hipoxantina"),
    dict(id="gmp_xantina", src={"id": "m_nuc_gmp"}, dst={"id": "m_deg_xantina"},
         color=GRANATE, rotulo="GMP ➔ Guanina ➔ Xantina"),
    dict(id="ctp_uracilo", src={"id": "m_nuc_ctp"}, dst={"id": "m_deg_uracilo"},
         color=GRANATE, rotulo="CMP / UMP ➔ Citosina / Uracilo"),
    dict(id="urato_sangre", src={"id": "m_deg_urato"}, dst=sangre(5500),
         color=ROJO, rotulo="URAT1: Ácido Úrico ➔ Sangre"),
    dict(id="beta_ala_sangre", src={"id": "m_deg_beta_ala"}, dst=sangre(5380),
         color=AZUL, rotulo="β-Alanina ➔ Sangre"),
    dict(id="glucolisis_lanz_malato", src={"id": "m_gap"}, dst={"id": "lupa_lanzadera_malato_aspartato", "lado": "top"},
         color=AZUL, rotulo="GAPDH: NADH citosólico ➔ Lanzadera Malato-Aspartato"),
    dict(id="dhap_lanzadera_g3p", src={"id": "m_dhap"}, dst={"id": "lupa_lanzadera_glicerol_p", "lado": "top"},
         color=NARANJA, rotulo="DHAP ➔ Lanzadera Glicerol-3-P"),
    dict(id="lanz_g3p_coq", src={"id": "m_lanz_g3p"}, dst={"id": "lupa_cadena_respiratoria", "lado": "right"},
         color=NARANJA, rotulo="mGPDH (FAD) ➔ CoQ"),
]

# ---------------------------------------------------------------------------
# Parámetros de la rejilla de costes
# ---------------------------------------------------------------------------
DURO = 3000          # texto, moléculas, recuadros, lupas
TRAZO = 70           # flecha existente (cruzar ≈ 2 celdas ➔ ~140)
TRAZO_HALO = 12      # celda vecina de una flecha existente
TRAZO_TENUE = 6      # trazos semitransparentes (conos de lupa, decoración)
MEMBRANA = 8         # membranas / crestas mitocondriales
RUTA = 90            # conexión nueva ya trazada
RUTA_HALO = 25
HALO_DURO = 4        # holgura alrededor de obstáculos duros
GIRO = {0: 0.0, 1: 3.0, 2: 12.0}   # penalización por giro de 0°, 45°, 90°
GRUPOS_INSERTO = set(ds.GRUPOS_INSERTO)
GRUPOS_IGNORADOS = {"eritrocitos_torrente"}
GRUPO_MITO = "mitocondria_biologica"


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


# ===========================================================================
# 6. ORQUESTACIÓN
# ===========================================================================
def caja_endpoint(ep, cajas):
    if "rect" in ep:
        return ep["rect"]
    if ep["id"] not in cajas:
        raise KeyError(f"id '{ep['id']}' no encontrado en el SVG")
    return cajas[ep["id"]]


def trazar_tramo(rj, b_src, lado_src, b_dst, lado_dst):
    ini = anillo(rj, b_src, lado_src)
    met = anillo(rj, b_dst, lado_dst)
    # El origen/destino propios no deben bloquear su anillo
    camino, coste, exp = astar(rj, ini, met, b_dst)
    if camino is None:
        return None, None, exp
    pts = simplificar([rj.centro(i) for i in camino])
    p_ini = punto_en_borde(b_src, pts[0], 2)
    p_fin = punto_en_borde(b_dst, pts[-1], 3)
    p_ini = alinear_stub(b_src, p_ini, pts[0])
    p_fin = alinear_stub(b_dst, p_fin, pts[-1])
    pts = simplificar([p_ini] + pts + [p_fin])
    return pts, coste, exp


def marcar_ruta(rj, pts):
    for p, q in zip(pts[:-1], pts[1:]):
        rj.segmento(p, q, RUTA, 1, RUTA_HALO)


def color_oscuro(hexc, f=0.72):
    r, g, b = (int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02x%02x%02x" % (int(r * f), int(g * f), int(b * f))


def generar_capa(svg_str, celda=12, verbose=True):
    root = ET.fromstring(svg_str)
    ancho, alto = _num(root.get("width")), _num(root.get("height"))
    t0 = time.time()
    elems = leer_svg(root)
    cajas = cajas_por_id(elems)
    rj = construir_rejilla(elems, cajas, ancho, alto, celda)
    if verbose:
        print(f"· {len(elems)} elementos leídos, rejilla {rj.W}×{rj.H} (celda {celda}px) "
              f"en {time.time() - t0:.1f}s")

    colores = sorted({c["color"] for c in CONEXIONES})
    defs = ["<defs>"]
    for col in colores:
        defs.append(f'<marker id="cxFlecha{col[1:]}" markerWidth="7" markerHeight="7" refX="5.5" refY="3.5" '
                    f'orient="auto" markerUnits="strokeWidth"><path d="M 0 0 L 7 3.5 L 0 7 Z" fill="{col}"/></marker>')
    defs.append("</defs>")

    trazos, rotulos, informe = [], [], []
    for cx in CONEXIONES:
        t1 = time.time()
        try:
            b_src = caja_endpoint(cx["src"], cajas)
            b_dst = caja_endpoint(cx["dst"], cajas)
        except KeyError as err:
            informe.append((cx["id"], "OMITIDA", str(err)))
            continue
        tramos = []
        if cx.get("via"):
            v = cx["via"]
            pa, _, _ = trazar_tramo(rj, b_src, cx["src"].get("lado"), v, cx["via_in"])
            if pa:
                marcar_ruta(rj, pa)
            pb, _, _ = trazar_tramo(rj, v, cx["via_out"], b_dst, cx["dst"].get("lado"))
            if pa is None or pb is None:
                informe.append((cx["id"], "SIN RUTA", ""))
                continue
            tramos = [(pa, False), (pb, True)]
        else:
            p, _, _ = trazar_tramo(rj, b_src, cx["src"].get("lado"), b_dst, cx["dst"].get("lado"))
            if p is None:
                informe.append((cx["id"], "SIN RUTA", ""))
                continue
            tramos = [(p, True)]

        # Diagnóstico: obstáculos atravesados (antes de marcar la ruta propia)
        cruces_duros = cruces_trazo = 0
        for pts, _ in tramos:
            for p, q in zip(pts[1:-2], pts[2:-1]):
                n = max(1, int(math.dist(p, q) / rj.c))
                for k in range(n + 1):
                    x, y = p[0] + (q[0] - p[0]) * k / n, p[1] + (q[1] - p[1]) * k / n
                    cval = rj.coste[rj.idx(*rj.celda_de(x, y))]
                    if cval >= DURO:
                        cruces_duros += 1
                    elif cval >= TRAZO:
                        cruces_trazo += 1

        # Rótulo en el tramo más largo
        todos = [pt for pts, _ in tramos for pt in pts]
        mejor_tramo = max((pts for pts, _ in tramos), key=lambda P: sum(math.dist(a, b) for a, b in zip(P, P[1:])))
        rot = colocar_rotulo(rj, mejor_tramo, cx["rotulo"]) if cx.get("rotulo") else None
        for pts, _ in tramos:
            marcar_ruta(rj, pts)
        if rot:
            rj.caja(rot[3], DURO)

        col = cx["color"]
        g = [f'<g id="cx_{cx["id"]}" class="conexion-inter-ruta">']
        for pts, con_flecha in tramos:
            pts_d = recortar_final(pts, 2) if con_flecha else pts
            mk = f' marker-end="url(#cxFlecha{col[1:]})"' if con_flecha else ""
            g.append(f'<path d="{path_redondeado(pts_d)}" fill="none" stroke="#ffffff" stroke-width="6" '
                     f'stroke-linecap="round" stroke-linejoin="round" opacity="0.55"/>')
            g.append(f'<path d="{path_redondeado(pts_d)}" fill="none" stroke="{col}" stroke-width="2.6" '
                     f'stroke-dasharray="10 6" stroke-linecap="round" stroke-linejoin="round"{mk}/>')
        g.append("</g>")
        trazos.append("".join(g))
        if rot:
            x, y, anc, _ = rot
            rotulos.append(
                f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anc}" fill="{color_oscuro(col)}" '
                f'font-size="{FS_ROTULO}" font-weight="800" font-family="\'Inter\', sans-serif" '
                f'stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">'
                f'{cx["rotulo"]}</text>')
        largo = sum(math.dist(a, b) for pts, _ in tramos for a, b in zip(pts, pts[1:]))
        informe.append((cx["id"], "OK", f"{largo:6.0f}px  cruces flecha≈{cruces_trazo:2d}  "
                        f"obstáculos={cruces_duros}  rótulo={'sí' if rot else 'NO'}  ({time.time() - t1:.1f}s)"))
        if verbose:
            print(f"  ✓ {cx['id']:<22s} {informe[-1][2]}")
        del todos

    capa = ('\n<!-- ================= CAPA DE CONEXIONES ENTRE RUTAS (conectar_rutas.py) ================= -->\n'
            '<g id="capa_conexiones_inter_ruta">' + "".join(defs) +
            '<g id="cx_trazos">' + "\n".join(trazos) + "</g>" +
            '<g id="cx_rotulos">' + "\n".join(rotulos) + "</g></g>\n")
    return capa, informe


def insertar_capa(svg_str, capa):
    k = svg_str.rfind("</svg>")
    return svg_str[:k] + capa + svg_str[k:]


def main():
    celda = 12
    if "--celda" in sys.argv:
        celda = int(sys.argv[sys.argv.index("--celda") + 1])

    import generar_prueba_visual_integrada as gen
    print("Generando mapa base (sin modificaciones)…")
    html_base, svg_base = gen.construir_mapa_organico()

    capa, informe = generar_capa(svg_base, celda)
    svg_nuevo = insertar_capa(svg_base, capa)
    html_nuevo = html_base.replace(svg_base, svg_nuevo, 1)

    salida = DIR_HTML
    if "--salida" in sys.argv:
        salida = sys.argv[sys.argv.index("--salida") + 1]
    r_svg = os.path.join(salida, "prueba_visual_integrada_conectada.svg")
    r_html = os.path.join(salida, "prueba_visual_integrada_conectada.html")
    with open(r_svg, "w", encoding="utf-8") as f:
        f.write(svg_nuevo)
    with open(r_html, "w", encoding="utf-8") as f:
        f.write(html_nuevo)

    print("\nRESUMEN DE CONEXIONES")
    ok = sum(1 for _, est, _ in informe if est == "OK")
    for cid, est, msg in informe:
        if est != "OK":
            print(f"  ✗ {cid:<22s} {est} {msg}")
    print(f"  {ok}/{len(CONEXIONES)} conexiones trazadas")
    print(f"\nSVG : {r_svg}\nHTML: {r_html}")

    if "--sin-png" not in sys.argv and shutil.which("rsvg-convert"):
        r_png = os.path.join(DIR_PREVIEWS, "prueba_visual_integrada_conectada_preview.png")
        subprocess.run(["rsvg-convert", "-w", "2900", "-o", r_png, r_svg], check=False)
        print(f"PNG : {r_png}")


if __name__ == "__main__":
    main()
