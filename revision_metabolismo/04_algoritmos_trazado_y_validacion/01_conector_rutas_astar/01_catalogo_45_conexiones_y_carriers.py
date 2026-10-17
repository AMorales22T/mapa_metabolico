# =============================================================================
# MÓDULO DE REVISIÓN: Catálogo de las 45 Conexiones Inter-Ruta y Transportadores
# =============================================================================
# Archivo original : scripts_generacion/conectar_rutas.py (líneas 1 a 218 de 850)
# Descripción      : Coordenadas de transportadores (MPC, CIC, AGC, Citrina, ORNT1), lista CONEXIONES y pesos de la rejilla.
# =============================================================================

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
DIR_BASE = os.path.dirname(DIR_SCRIPT) if os.path.basename(DIR_SCRIPT) == "scripts_generacion" else DIR_SCRIPT
DIR_HTML = os.path.join(DIR_BASE, "versiones_html")
DIR_PREVIEWS = os.path.join(DIR_BASE, "capturas_y_pruebas")
sys.path.insert(0, DIR_SCRIPT)
sys.path.insert(0, DIR_BASE)

import detectar_solapamientos as ds  # noqa: E402  (reutiliza su geometría SVG)

NS = "{http://www.w3.org/2000/svg}"

# ---------------------------------------------------------------------------
# Transportadores / anclas sin id propio en el SVG (coordenadas absolutas)
# ---------------------------------------------------------------------------
Y_OFFSET = 350
MPC = (1645, 2105 + Y_OFFSET, 1715, 2147 + Y_OFFSET)          # Carrier de Piruvato (MPC1/2)
CIC = (1915, 2115 + Y_OFFSET, 1975, 2143 + Y_OFFSET)          # Carrier de Citrato
AGC = (2015, 2110 + Y_OFFSET, 2105, 2165 + Y_OFFSET)          # Carrier de Glutamato (AGC / GC1) con rótulo inferior
CITRINA = (4330, 2135 + Y_OFFSET, 4510, 2205 + Y_OFFSET)      # Carrier SLC25A13 (Citrina) en MMI con rótulo
ORNT1 = (4570, 2135 + Y_OFFSET, 4710, 2205 + Y_OFFSET)        # Carrier SLC25A15 (ORNT1) en MMI con rótulo
TXT_SUCCINIL = (650, 2814 + Y_OFFSET, 785, 2836 + Y_OFFSET)   # rótulo "➔ Succinil-CoA [4C] (Krebs)" (vía Propionil-CoA)


def sangre(x):
    """Punto de llegada al torrente sanguíneo (cara interna de la membrana plasmática)."""
    return {"rect": (x - 25, 84 + Y_OFFSET, x + 25, 92 + Y_OFFSET), "lado": "bottom"}


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
    dict(id="sangre_lactato", src=sangre(1620), dst={"id": "m_lactato", "lado": "top"},
         color=MORADO, rotulo="Lactato (Ciclo de Cori) ➔"),
    dict(id="sangre_glicerol", src=sangre(760), dst={"id": "m_glicerol", "lado": "top"},
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
    dict(id="r5p_prpp", src={"id": "m_r5p"}, dst={"id": "m_nuc_r5p_in", "lado": "left"},
         color=VERDE, rotulo="Ribosa-5-P ➔ PRPP Sintetasa (Nucleótidos)"),

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
    dict(id="krebs_icdh_cte", src={"id": "m_isocitrato"}, dst={"id": "lupa_cadena_respiratoria", "lado": "left"},
         color=VERDE, rotulo="Isocitrato DH (NADH) ➔ Complejo I"),
    dict(id="krebs_akgdh_cte", src={"id": "m_akg"}, dst={"id": "lupa_cadena_respiratoria", "lado": "left"},
         color=VERDE, rotulo="α-KG DH (NADH) ➔ Complejo I"),
    dict(id="krebs_cte", src={"id": "m_succinato"}, dst={"id": "lupa_cadena_respiratoria", "lado": "left"},
         color=PIZARRA, rotulo="Succinato DH (FADH₂) ➔ Complejo II"),
    dict(id="krebs_mdh_cte", src={"id": "m_malato"}, dst={"id": "lupa_cadena_respiratoria", "lado": "left"},
         color=VERDE, rotulo="Malato DH (NADH) ➔ Complejo I"),
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
    dict(id="urea_fumarato_krebs", src={"id": "m_u_fumarato"}, dst={"id": "m_fumarato"},
         color=NARANJA, rotulo="Fumarato (ASL) ➔ Krebs"),
    dict(id="urea_sangre", src={"id": "m_u_urea"}, dst=sangre(4556),
         color=ROJO, rotulo="Urea ➔ Sangre (Riñón)"),

    # --- Nucleótidos & Lanzaderas Redox ----------------------------------------------
    dict(id="glutamina_cps2", src={"id": "m_gln_integ"}, dst={"id": "m_nuc_pir_sustratos", "lado": "left"},
         color=TEAL, rotulo="Gln ➔ CPS-II (Pirimidinas)"),
    dict(id="dhodh_coq_cte", src={"id": "m_nuc_dho", "lado": "left"}, dst={"id": "lupa_cadena_respiratoria", "lado": "right"},
         color=AZUL, rotulo="DHODH (MMI): CoQH₂ ➔ Complejo III (CTE)"),
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
    dict(id="lanz_malato_cte_comp1", src={"id": "lupa_lanzadera_malato_aspartato", "lado": "bottom"}, dst={"id": "lupa_cadena_respiratoria", "lado": "left"},
         color=VERDE, rotulo="NADH mitocondrial (mMDH) ➔ Complejo I"),
    dict(id="lanz_asp_urea", src={"id": "lupa_lanzadera_malato_aspartato", "lado": "right"}, dst={"id": "m_u_aspartato"},
         color=TEAL, rotulo="Aspartato citosólico (Aralar) ➔ Ciclo de la Urea (ASS1)"),
    dict(id="betaox_etf_cte", src={"id": "m_palmitoil", "lado": "right"}, dst={"id": "lupa_cadena_respiratoria", "lado": "left"},
         color=NARANJA, rotulo="Acil-CoA DH (FADH₂ / ETF) ➔ CoQ (Cadena Respiratoria)"),
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


