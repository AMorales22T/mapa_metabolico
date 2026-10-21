#!/usr/bin/env python3
"""
GENERADOR DE PRUEBA VISUAL INTEGRADA (ENTORNO BIOLÓGICO REAL - SIN GLOBOS NI CAJAS)
==================================================================================
Implementa fielmente el diseño orgánico celular:
- Fondo acuoso citosólico continuo con gradientes biológicos y halo citoplasmático.
- Membrana plasmática ondulada continua bicapa lipídica arriba, con receptor GLUT-4.
- Citoesqueleto y polirribosomas tenues flotando libremente.
- Gran Mitocondria anatómica arriñonada con doble membrana (MME y MMI con espacio intermembrana) y crestas onduladas.
- TODAS las moléculas y estructuras químicas flotan LIBRES en el espacio biológico:
  * CERO globos, CERO tarjetas blancas, CERO cajas envolventes o marcos artificiales.
  * Texto mínimo: Nombre del metabolito, conteo de carbonos [6C], enzima concisa y arcos de energía.
  * Agrupaciones con 'data-arrastrable="1"' para mover en editor_arrastrable.html.
"""

import os
import sys

import sys
import os

DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_SCRIPT) if os.path.basename(DIR_SCRIPT) == "scripts_generacion" else DIR_SCRIPT
DIR_HTML = os.path.join(DIR_BASE, "versiones_html")
sys.path.append(os.path.join(DIR_BASE, "06_REGULACION_Y_LEYENDA"))
import regulacion

sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "via_02_gluconeogenesis"))
from estructuras_gluconeogenesis import (
    OXALACETATO as GLUCONEO_OXALACETATO,
    MALATO as GLUCONEO_MALATO,
    RE_GLUCOSA_6_FOSFATASA,
    LACTATO as GLUCONEO_LACTATO,
    GLICEROL as GLUCONEO_GLICEROL,
    GLICEROL_3_FOSFATO as GLUCONEO_G3P,
    FRUCTOSA_2_6_BISFOSFATO as GLUCONEO_F26BP
)

sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "via_01_glucolisis"))
sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "via_03_glucogenogenesis_y_glucogenolisis"))
sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "via_04_pentosas_fosfato"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "via_05_complejo_pdh"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "via_06_ciclo_de_krebs"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "via_07_cadena_respiratoria_atp_sintasa"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "via_08_lanzaderas"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "via_09_beta_oxidacion"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "via_10_lipogenesis"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "via_11_cetogenesis_y_cetolisis"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "via_12_colesterol_y_lipoproteinas"))
sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "via_13_transaminacion_y_desaminacion"))
sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "via_14_ciclo_de_la_urea"))
sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "via_12b_destinos_esqueletos_carbonados"))
sys.path.append(os.path.join(DIR_BASE, "05_NUCLEOTIDOS_Y_OTRAS", "via_15_sintesis_purinas_y_pirimidinas"))
sys.path.append(os.path.join(DIR_BASE, "05_NUCLEOTIDOS_Y_OTRAS", "via_16_degradacion_y_acido_urico"))
from estructuras_nucleotidos import (
    PRPP, FOSFORRIBOSILAMINA_5 as NUC_5_PRA, IMP, AMP as NUC_AMP, GMP as NUC_GMP,
    CARBAMOIL_FOSFATO as NUC_CARBAMOIL_P, DIHIDROOROTATO as NUC_DHO,
    OROTATO as NUC_OROTATO, UMP as NUC_UMP, CTP as NUC_CTP, DTMP as NUC_DTMP
)
from estructuras_degradacion import (
    HIPOXANTINA, XANTINA, ACIDO_URICO, URACILO as DEG_URACILO,
    DIHIDROURACILO as DEG_DIHIDROURACILO, BETA_UREIDOPROPIONATO, BETA_ALANINA
)
from estructuras_lanzadera import (
    GLICEROL_3_FOSFATO as LANZ_G3P
)
from estructuras_destinos_aa import (
    FENILALANINA as AA_FENILALANINA,
    TIROSINA as AA_TIROSINA,
    PROPIONIL_COA as AA_PROPIONIL_COA,
    METILMALONIL_COA as AA_METILMALONIL_COA,
    HOMOCISTEINA as AA_HOMOCISTEINA
)

from estructuras_pdh import (
    HIDROXIETIL_TPP as PDH_HIDROXIETIL_TPP,
    ACETIL_LIPOAMIDA as PDH_ACETIL_LIPOAMIDA,
    DIHIDROLIPOAMIDA as PDH_DIHIDROLIPOAMIDA,
    LIPOAMIDA_OXIDADA as PDH_LIPOAMIDA_OXIDADA
)

# Estructuras químicas
from estructuras_aminoacidos import (
    ALANINA as AMINO_ALANINA,
    GLUTAMATO as AMINO_GLUTAMATO,
    ALFA_CETOGLUTARATO as AMINO_AKG,
    ASPARTATO_AMINO as AMINO_ASPARTATO,
    OXALACETATO_AMINO as AMINO_OAA,
    ION_AMONIO as AMINO_NH4,
    GLUTAMINA as AMINO_GLUTAMINA,
    PLP_COENZIMA as AMINO_PLP
)
from estructuras_urea import (
    IONES_INICIALES as UREA_IONES_INICIALES,
    CARBAMOIL_FOSFATO as UREA_CARBAMOIL_P,
    ORNITINA as UREA_ORNITINA,
    CITRULINA as UREA_CITRULINA,
    ASPARTATO as UREA_ASPARTATO,
    ARGININOSUCCINATO as UREA_ARGININOSUCCINATO,
    FUMARATO as UREA_FUMARATO,
    ARGININA as UREA_ARGININA,
    UREA as UREA_MOL,
    N_ACETILGLUTAMATO as UREA_NAG
)
from estructuras_glucosa import (
    GLUCOSA, GLUCOSA_6_FOSFATO, FRUCTOSA_6_FOSFATO, FRUCTOSA_1_6_BISFOSFATO,
    DIHIDROXIACETONA_FOSFATO, GLICERALDEHIDO_3_FOSFATO, BISFOSFOGLICERATO_1_3,
    FOSFOGLICERATO_3, FOSFOGLICERATO_2, FOSFOENOLPIRUVATO, PIRUVATO
)
from estructuras_glucogeno import (
    GLUCOSA_1_FOSFATO, UDP_GLUCOSA, CADENA_GLUCOGENO
)
from estructuras_pentosas import (
    FOSFOGLUCONO_LACTONA_6, FOSFOGLUCONATO_6, RIBULOSA_5_FOSFATO,
    RIBOSA_5_FOSFATO, XILULOSA_5_FOSFATO, SEDOHEPTULOSA_7_FOSFATO, ERITROSA_4_FOSFATO,
    GLICERALDEHIDO_3_FOSFATO as PENTOSAS_GAP, FRUCTOSA_6_FOSFATO as PENTOSAS_F6P
)
from estructuras_krebs import (
    ACETIL_COA, OXALACETATO as KREBS_OXALACETATO, CITRATO, ISOCITRATO,
    ALFA_CETOGLUTARATO as KREBS_ALFA_CETOGLUTARATO, SUCCINIL_COA, SUCCINATO, FUMARATO, MALATO as KREBS_MALATO
)
from estructuras_lanzadera import (
    OXALACETATO as LANZ_OAA, MALATO as LANZ_MALATO,
    ASPARTATO as LANZ_ASP, GLUTAMATO as LANZ_GLU, ALFA_CETOGLUTARATO as LANZ_AKG
)
from estructuras_cadena_transporte import (
    UBIQUINONA, CITOCROMO_C, OXIGENO, AGUA, NADH as CTE_NADH, FADH2 as CTE_FADH2
)
from estructuras_beta_oxidacion import (
    PALMITATO, PALMITOIL_COA, CARNITINA, PALMITOIL_CARNITINA, TRANS_DELTA2_ENOIL_COA, L_BETA_HIDROXIACIL_COA, BETA_CETOACIL_COA, ACETIL_COA_BETA, MIRISTOIL_COA
)
from estructuras_lipogenesis import (
    MALONIL_COA, ACETOACETIL_ACP, D_BETA_HIDROXIACIL_ACP, TRANS_DELTA2_ENOIL_ACP, BUTIRIL_ACP, PALMITATO_LIBRE
)
from estructuras_ceto import (
    ACETOACETIL_COA, HMG_COA, ACETOACETATO, D_BETA_HIDROXIBUTIRATO, ACETONA
)
from estructuras_colesterol import (
    ACETOACETIL_COA_COLEST, HMG_COA_CITOSOL, MEVALONATO, ISOPENTENIL_PP, FARNESIL_PP, ESCUALENO, LANOSTEROL, COLESTEROL
)

ANCHO_CANVAS = 5800
ALTO_CANVAS = 5120
Y_OFFSET = 350
MOSTRAR_CONEXIONES_INTER_RUTA = False

GLICEROL_MOL = """
<g class="molecula-glicerol" stroke="#0f172a" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="35" y="18" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0284c7" text-anchor="middle">CH₂OH</text>
  <line x1="35" y1="22" x2="35" y2="35" />
  <text x="35" y="48" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="45" y1="44" x2="55" y2="44" stroke="#0284c7" stroke-width="1.8"/>
  <text x="66" y="48" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0284c7" text-anchor="middle">OH</text>
  <line x1="35" y1="52" x2="35" y2="65" />
  <text x="35" y="78" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0284c7" text-anchor="middle">CH₂OH</text>
</g>
"""

def nodo_libre(x, y, nombre, carbonos, svg_mol, id_nodo="", text_right=True, dx=135, dy=24, text_pos="side", detalle=""):
    """Metabolito 100% libre sin tarjetas ni globos."""
    if text_pos == "top":
        align = 'text-anchor="middle"'
        tx = dx if dx != 135 else 70
        ty = dy if dy != 24 else -22
        txt_det = f'<text x="{tx}" y="{ty + 30}" fill="#64748b" font-size="9.5" font-weight="600" font-family="\'Inter\', sans-serif" {align}>{detalle}</text>' if detalle else ""
        return f"""
        <!-- Metabolito Libre: {nombre} -->
        <g id="{id_nodo}" data-arrastrable="1" transform="translate({x}, {y})">
          <g>{svg_mol}</g>
          <text x="{tx}" y="{ty}" fill="#0f172a" font-size="14.5" font-weight="800" font-family="'Inter', sans-serif" {align}>{nombre}</text>
          <text x="{tx}" y="{ty + 16}" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace" {align}>[{carbonos}]</text>
          {txt_det}
        </g>
        """
    elif text_pos == "bottom":
        align = 'text-anchor="middle"'
        tx = dx if dx != 135 else 50
        ty = dy if dy != 24 else 135
        txt_det = f'<text x="{tx}" y="{ty + 28}" fill="#64748b" font-size="9.5" font-weight="600" font-family="\'Inter\', sans-serif" {align}>{detalle}</text>' if detalle else ""
        return f"""
        <!-- Metabolito Libre: {nombre} -->
        <g id="{id_nodo}" data-arrastrable="1" transform="translate({x}, {y})">
          <g>{svg_mol}</g>
          <text x="{tx}" y="{ty}" fill="#0f172a" font-size="14.5" font-weight="800" font-family="'Inter', sans-serif" {align}>{nombre}</text>
          <text x="{tx}" y="{ty + 15}" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace" {align}>[{carbonos}]</text>
          {txt_det}
        </g>
        """
    if text_right:
        tx = dx
    else:
        tx = dx if dx != 135 else -20
    align = "" if text_right else 'text-anchor="end"'
    txt_det = f'<text x="{tx}" y="{dy + 32}" fill="#64748b" font-size="9.5" font-weight="600" font-family="\'Inter\', sans-serif" {align}>{detalle}</text>' if detalle else ""
    return f"""
    <!-- Metabolito Libre: {nombre} -->
    <g id="{id_nodo}" data-arrastrable="1" transform="translate({x}, {y})">
      <g>{svg_mol}</g>
      <text x="{tx}" y="{dy}" fill="#0f172a" font-size="15" font-weight="800" font-family="'Inter', sans-serif" {align}>{nombre}</text>
      <text x="{tx}" y="{dy + 17}" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace" {align}>[{carbonos}]</text>
      {txt_det}
    </g>
    """


def nodo_aa(x, y, nombre, carbonos, clasificacion="glu", detalle="", id_nodo=""):
    """
    Rótulo tipográfico orgánico para aminoácidos sin cajas contenedoras ni puntos de carbono.
    Clasificación: glu (verde), ceto (rojo), mixto (púrpura).
    """
    colores = {
        "glu": {"dot": "#16a34a", "txt": "#14532d"},
        "ceto": {"dot": "#dc2626", "txt": "#881337"},
        "mixto": {"dot": "#9333ea", "txt": "#581c87"}
    }
    cfg = colores.get(clasificacion, colores["glu"])
    detalle_svg = f'<text x="0" y="27" fill="#64748b" font-size="9" font-weight="600" font-family="\'Inter\', sans-serif">{detalle}</text>' if detalle else ""
    id_attr = f'id="{id_nodo}"' if id_nodo else ""

    return f"""
    <!-- AA: {nombre} -->
    <g {id_attr} data-arrastrable="1" transform="translate({x}, {y})">
      <circle cx="-10" cy="-4" r="4.5" fill="{cfg['dot']}" />
      <text x="0" y="0" fill="{cfg['txt']}" font-size="13.5" font-weight="800" font-family="'Inter', sans-serif">{nombre}</text>
      <text x="0" y="15" fill="#ea580c" font-size="10.5" font-weight="800" font-family="'JetBrains Mono', monospace">[{carbonos}]</text>
      {detalle_svg}
    </g>
    """


def badge_clinico(x, y, texto, es_alerta=True, rx=11):
    """
    Píldora reducida para patologías o cofactores anclada a diana.
    """
    fill = "#fee2e2" if es_alerta else "#e0e7ff"
    stroke = "#dc2626" if es_alerta else "#4f46e5"
    txt_col = "#991b1b" if es_alerta else "#312e81"
    ancho = max(len(texto) * 6.8 + 20, 95)

    return f"""
    <!-- Badge clínico: {texto} -->
    <g data-arrastrable="1" transform="translate({x}, {y})">
      <rect x="0" y="0" width="{ancho}" height="22" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.2" opacity="0.95"/>
      <text x="{ancho/2}" y="15" fill="{txt_col}" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">{texto}</text>
    </g>
    """


def badge_via(n, x, y, id_badge=None):
    """Badge circular numerado de vía metabólica para la leyenda (arrastrable)."""
    bid = id_badge or f"badge_via_{str(n).replace(' ', '_')}"
    return f"""
    <g id="{bid}" data-arrastrable="1" class="badge-via" transform="translate({x}, {y})" style="cursor: grab;">
      <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.2" />
      <text x="0" y="4.5" fill="#ffffff" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{n}</text>
    </g>
    """

def badge_rodeo_gng(num_rodeo, x, y, id_badge=None):
    """Badge distintivo para los 3 rodeos (bypasses) de la gluconeogénesis."""
    bid = id_badge or f"badge_rodeo_gng_{num_rodeo}"
    return f"""
    <g id="{bid}" data-arrastrable="1" class="badge-rodeo-gng" transform="translate({x}, {y})">
      <rect x="-38" y="-12" width="76" height="24" rx="6" fill="#7c3aed" stroke="#ffffff" stroke-width="1.8" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
      <text x="0" y="4" fill="#ffffff" font-size="10" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">RODEO {num_rodeo}</text>
    </g>
    """

def etiqueta_regulacion(id_enzima, x, y, dx=0, dy=0, anchor="start"):
    """
    Genera etiqueta compacta de regulación alostérica y covalente:
    (+) Verde para activadores, (-) Rojo para inhibidores, (P) Amarillo para fosforilación, [Hormonal] Azul para control hormonal.
    """
    e = regulacion.ENZIMAS_POR_ID.get(id_enzima)
    if not e:
        return ""
    lineas = []
    if e.get("activadores"):
        lineas.append((f"(+) {', '.join(e['activadores'])}", "#16a34a"))
    if e.get("inhibidores"):
        lineas.append((f"(-) {', '.join(e['inhibidores'])}", "#dc2626"))
    if e.get("mapa_cov"):
        lineas.append((f"(P) {e['mapa_cov']}", "#ca8a04"))
    if e.get("mapa_hor"):
        lineas.append((f"[Hormonal] {e['mapa_hor']}", "#0284c7"))

    if not lineas:
        return ""

    spans = []
    curr_y = dy
    for txt, col in lineas:
        anchor_attr = f'text-anchor="{anchor}"' if anchor != "start" else ""
        font_attr = "font-family=\"'Inter', sans-serif\""
        spans.append(f'<text x="{dx}" y="{curr_y}" fill="{col}" font-size="9" font-weight="800" {font_attr} {anchor_attr}>{txt}</text>')
        curr_y += 12

    return f"""
    <g class="etiqueta-regulacion" transform="translate({x}, {y})">
      {''.join(spans)}
    </g>
    """

def reaccion_libre(x, y, h, enzima, entra="", sale="", es_ganancia=False, reversible=False, id_rx="", text_dx=14, text_anchor="start"):
    """Flecha de reacción libre con enzima y curvas Bézier de energía."""
    curvas = ""
    if entra:
        col_in = "#dc2626" if not es_ganancia else "#475569"
        curvas += f"""
        <path d="M -65 6 Q -20 6 -4 16" fill="none" stroke="{col_in}" stroke-width="1.8" marker-end="url(#arrowRed)"/>
        <text x="-70" y="9" fill="{col_in}" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{entra}</text>
        """
    if sale:
        col_out = "#059669" if es_ganancia else "#475569"
        curvas += f"""
        <path d="M -4 22 Q -20 32 -65 32" fill="none" stroke="{col_out}" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
        <text x="-70" y="36" fill="{col_out}" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{sale}</text>
        """

    if reversible:
        lineas = f"""
        <line x1="-3" y1="0" x2="-3" y2="{h}" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        <line x1="3" y1="{h}" x2="3" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        """
    else:
        lineas = f"""<line x1="0" y1="0" x2="0" y2="{h}" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>"""

    anchor_attr = f'text-anchor="{text_anchor}"' if text_anchor != "start" else ""
    return f"""
    <!-- Reacción: {enzima} -->
    <g id="{id_rx}" data-arrastrable="1" transform="translate({x}, {y})">
      {lineas}
      {curvas}
      <text x="{text_dx}" y="{h//2 + 4}" fill="#0f172a" font-size="12" font-weight="700" font-family="'Inter', sans-serif" {anchor_attr}>{enzima}</text>
    </g>
    """


def generar_bloque_leyenda(x=120, y=4220):
    """
    Genera la Leyenda General con:
    1. Lista numerada de 14 vías con sus badges coincidentes con el mapa.
    2. Clave de símbolos ((+), (-), (P), [Hormonal], ⇄, →, - - →, ▭, [nC]).
    3. Código de colores biológicos.
    """
    filas_vias = []
    # Dividir las vías en 2 columnas equilibradas dinámicamente
    mid = (len(regulacion.VIAS) + 1) // 2
    col1 = regulacion.VIAS[:mid]
    col2 = regulacion.VIAS[mid:]

    color_vias = {
        1: "#0284c7", 2: "#7c3aed", 3: "#ea580c", 4: "#059669",
        5: "#c2410c", 6: "#d97706", 7: "#16a34a", 8: "#0284c7",
        9: "#b45309", 10: "#0d9488", 11: "#be123c", 12: "#4f46e5",
        "12B": "#6366f1", 13: "#2563eb", 14: "#0891b2", 15: "#0284c7",
        16: "#475569", 17: "#be123c"
    }

    svg_col1 = []
    y_pos = 0
    for v in col1:
        c_v = color_vias.get(v['n'], "#0284c7")
        svg_col1.append(f"""
        <g id="badge_leyenda_{v['n']}" class="badge-via" data-via="{v['n']}" transform="translate(0, {y_pos})" style="cursor: pointer;">
          <circle cx="12" cy="0" r="10" fill="{c_v}" />
          <text x="12" y="3.5" fill="#ffffff" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{v['n']}</text>
          <text x="30" y="3" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif">{v['nombre']}</text>
          <text x="30" y="16" fill="#64748b" font-size="9" font-family="'Inter', sans-serif">{v['resumen'][:55]}</text>
        </g>
        """)
        y_pos += 44

    svg_col2 = []
    y_pos = 0
    for v in col2:
        c_v = color_vias.get(v['n'], "#0284c7")
        svg_col2.append(f"""
        <g id="badge_leyenda_{v['n']}" class="badge-via" data-via="{v['n']}" transform="translate(0, {y_pos})" style="cursor: pointer;">
          <circle cx="12" cy="0" r="10" fill="{c_v}" />
          <text x="12" y="3.5" fill="#ffffff" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{v['n']}</text>
          <text x="30" y="3" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif">{v['nombre']}</text>
          <text x="30" y="16" fill="#64748b" font-size="9" font-family="'Inter', sans-serif">{v['resumen'][:55]}</text>
        </g>
        """)
        y_pos += 44

    # Símbolos y colores (Columna 3)
    simbolos_items = []
    y_sim = 0
    simbolos_limpios = [
        ("(+)", "Activador alostérico (efector positivo)"),
        ("(-)", "Inhibidor alostérico (efector negativo / retroinhibición)"),
        ("(P)", "Modificación covalente por fosforilación (forma activa)"),
        ("⇄", "Reacción reversible (doble flecha)"),
        ("→", "Reacción irreversible (flecha simple, punto de control)"),
        ("- - →", "Conexión entre vías / transporte"),
        ("▭", "Transportador de membrana (GLUT, MPC, CACT, AGC…)"),
        ("[nC]", "Número de átomos de carbono del metabolito")
    ]
    for sim, desc in simbolos_limpios:
        simbolos_items.append(f"""
        <g transform="translate(0, {y_sim})">
          <rect x="0" y="-10" width="40" height="18" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
          <text x="20" y="3" fill="#0f172a" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{sim}</text>
          <text x="50" y="3" fill="#334155" font-size="10" font-weight="700" font-family="'Inter', sans-serif">{desc}</text>
        </g>
        """)
        y_sim += 26

    colores = [
        ("#ea580c", "Flujo principal de carbono"),
        ("#7c3aed", "Reacciones de Gluconeogénesis (4 enzimas)"),
        ("#b45309", "Glucógeno (Síntesis y lisis)"),
        ("#059669", "Pentosas fosfato &amp; Shunt"),
        ("#2563eb", "Aminoácidos &amp; Ciclo de la Urea"),
        ("#16a34a", "(+) Activador alostérico"),
        ("#dc2626", "(-) Inhibidor alostérico / Gasto ATP"),
        ("#ca8a04", "(P) Modificación covalente activa/inactiva")
    ]
    colores_items = []
    y_col = 0
    for c_hex, c_desc in colores:
        colores_items.append(f"""
        <g transform="translate(0, {y_col})">
          <circle cx="6" cy="0" r="5" fill="{c_hex}"/>
          <text x="18" y="3.5" fill="#334155" font-size="9.5" font-weight="600" font-family="'Inter', sans-serif">{c_desc}</text>
        </g>
        """)
        y_col += 24

    return f"""
    <!-- BLOQUE INSTITUCIONAL: LEYENDA GENERAL DE VÍAS METABÓLICAS Y REGULACIÓN -->
    <g id="bloque_leyenda" data-arrastrable="1" transform="translate({x}, {y})" filter="url(#shadowCard)">
      <!-- Fondo -->
      <rect width="3650" height="480" rx="22" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" />
      <path d="M 0 22 Q 0 0 22 0 L 3628 0 Q 3650 0 3650 22 L 3650 10 L 0 10 Z" fill="url(#gradHeaderAutoria)" />

      <!-- Encabezado -->
      <g transform="translate(35, 30)">
        <rect x="0" y="0" width="230" height="24" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2" />
        <text x="115" y="16" fill="#0369a1" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="1">GUÍA Y CONVENCIONES</text>
        <text x="250" y="18" fill="#0f172a" font-size="19" font-weight="900" font-family="'Inter', sans-serif">LEYENDA DE VÍAS METABÓLICAS &amp; CONTROL ALOSTÉRICO / COVALENTE</text>
        <rect x="1350" y="-3" width="760" height="28" rx="7" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
        <text x="1360" y="15" fill="#92400e" font-size="11" font-weight="800" font-family="'Inter', sans-serif">[Nota] Célula didáctica/hepática: Gluconeogénesis, Cetogénesis y Ciclo de la Urea ocurren primordialmente en hepatocito</text>
      </g>
      <line x1="35" y1="68" x2="3615" y2="68" stroke="#e2e8f0" stroke-width="1.5" />

      <!-- Columnas 1 y 2: Vías (1 a 15) -->
      <g transform="translate(40, 100)">
        <text x="0" y="-12" fill="#0284c7" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">VÍAS METABÓLICAS (1–{mid}):</text>
        {''.join(svg_col1)}
      </g>
      <g transform="translate(940, 100)">
        <text x="0" y="-12" fill="#0284c7" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">VÍAS METABÓLICAS ({mid+1}–{len(regulacion.VIAS)}):</text>
        {''.join(svg_col2)}
      </g>

      <line x1="1840" y1="85" x2="1840" y2="430" stroke="#f1f5f9" stroke-width="2" />

      <!-- Columna 3: Símbolos -->
      <g transform="translate(1870, 100)">
        <text x="0" y="-12" fill="#0f766e" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">CONVENCIONES Y EFECTORES:</text>
        {''.join(simbolos_items)}
      </g>

      <line x1="2670" y1="85" x2="2670" y2="430" stroke="#f1f5f9" stroke-width="2" />

      <!-- Columna 4: Código de Colores -->
      <g transform="translate(2700, 100)">
        <text x="0" y="-12" fill="#b45309" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">CÓDIGO DE COLORES:</text>
        {''.join(colores_items)}
      </g>

      <line x1="3050" y1="85" x2="3050" y2="430" stroke="#f1f5f9" stroke-width="2" />

      <!-- Columna 5: Clasificación Enzimática EC -->
      <g id="leyenda_col_ec" transform="translate(3080, 100)">
        <text x="0" y="-12" fill="#7c3aed" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">NOMENCLATURA ENZIMÁTICA (EC):</text>
        
        <!-- Header badge y título -->
        <g transform="translate(0, -2)">
          <rect x="0" y="-8" width="84" height="21" rx="5" fill="#f5f3ff" stroke="#c4b5fd" stroke-width="1.2"/>
          <text x="42" y="6.5" fill="#6d28d9" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC x.x.x.x</text>
          <text x="96" y="6.5" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif">Comisión de Enzimas (Enzyme Commission)</text>
        </g>
        
        <!-- Intro -->
        <text x="0" y="34" fill="#475569" font-size="10" font-weight="600" font-family="'Inter', sans-serif">Código numérico de 4 cifras que identifica cada enzima por la reacción que cataliza:</text>

        <!-- 1.ª Cifra -->
        <text x="0" y="58" fill="#1e293b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif"><tspan fill="#7c3aed" font-weight="900">1.ª cifra</tspan> · Clase principal de reacción (1 a 7):</text>

        <!-- 7 Clases en 2 columnas -->
        <!-- Columna A (1-4) -->
        <g transform="translate(0, 70)">
          <g transform="translate(0, 0)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">1</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Oxidorreductasas</tspan> (redox / electrones)</text>
          </g>
          <g transform="translate(0, 23)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">2</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Transferasas</tspan> (transferencia de grupos)</text>
          </g>
          <g transform="translate(0, 46)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Hidrolasas</tspan> (ruptura de enlaces por H₂O)</text>
          </g>
          <g transform="translate(0, 69)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">4</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Liasas</tspan> (ruptura/adición sin agua)</text>
          </g>
        </g>

        <!-- Columna B (5-7) -->
        <g transform="translate(265, 70)">
          <g transform="translate(0, 0)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">5</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Isomerasas</tspan> (isomerización estructural)</text>
          </g>
          <g transform="translate(0, 23)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">6</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Ligasas</tspan> (unión molecular + hidrólisis ATP)</text>
          </g>
          <g transform="translate(0, 46)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">7</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Translocasas</tspan> (transporte de membrana)</text>
          </g>
        </g>

        <!-- 2.ª y 3.ª Cifras -->
        <g transform="translate(0, 168)">
          <rect x="0" y="-8" width="54" height="18" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
          <text x="27" y="4.5" fill="#0f172a" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">2.ª, 3.ª</text>
          <text x="63" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Subclase y sub-subclase:</tspan> tipo de grupo funcional o sustrato donador/aceptor.</text>
        </g>

        <!-- 4.ª Cifra -->
        <g transform="translate(0, 196)">
          <rect x="0" y="-8" width="54" height="18" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
          <text x="27" y="4.5" fill="#0f172a" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">4.ª</text>
          <text x="63" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Número de orden:</tspan> identificador secuencial de la enzima dentro de su sub-subclase.</text>
        </g>

        <!-- Micro-tarjeta de ejemplo -->
        <g transform="translate(0, 226)">
          <rect x="0" y="0" width="530" height="44" rx="7" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2"/>
          <text x="12" y="18" fill="#64748b" font-size="9" font-weight="800" font-family="'JetBrains Mono', monospace">Ejemplo:</text>
          <text x="74" y="18" fill="#0f172a" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace">EC 2.7.1.1 · Hexoquinasa</text>
          <text x="12" y="33" fill="#64748b" font-size="8.5" font-family="'Inter', sans-serif">2: Transferasa ➔ 7: Fosfotransferasa ➔ 1: Aceptor grupo -OH ➔ 1: D-hexosa-6-fosfotransferasa</text>
        </g>
      </g>
    </g>
    """

def generar_bloque_autoria(x=3800, y=4220):
    """
    Genera el bloque institucional / autoría de código abierto de formato ampliado
    (1860 × 505 px) con fuentes científicas completas, herramientas de ingeniería,
    enlace a GitHub y código QR escaneable de alta definición.
    """
    qr_path = "M0,0h7v1h-7zM9,0h1v1h-1zM12,0h1v1h-1zM14,0h2v1h-2zM19,0h1v1h-1zM22,0h7v1h-7zM0,1h1v1h-1zM6,1h1v1h-1zM8,1h1v1h-1zM11,1h2v1h-2zM14,1h2v1h-2zM17,1h2v1h-2zM20,1h1v1h-1zM22,1h1v1h-1zM28,1h1v1h-1zM0,2h1v1h-1zM2,2h3v1h-3zM6,2h1v1h-1zM8,2h5v1h-5zM14,2h1v1h-1zM17,2h2v1h-2zM22,2h1v1h-1zM24,2h3v1h-3zM28,2h1v1h-1zM0,3h1v1h-1zM2,3h3v1h-3zM6,3h1v1h-1zM9,3h3v1h-3zM14,3h1v1h-1zM18,3h1v1h-1zM22,3h1v1h-1zM24,3h3v1h-3zM28,3h1v1h-1zM0,4h1v1h-1zM2,4h3v1h-3zM6,4h1v1h-1zM8,4h1v1h-1zM13,4h1v1h-1zM15,4h4v1h-4zM22,4h1v1h-1zM24,4h3v1h-3zM28,4h1v1h-1zM0,5h1v1h-1zM6,5h1v1h-1zM8,5h2v1h-2zM11,5h1v1h-1zM13,5h1v1h-1zM15,5h2v1h-2zM19,5h1v1h-1zM22,5h1v1h-1zM28,5h1v1h-1zM0,6h7v1h-7zM8,6h1v1h-1zM10,6h1v1h-1zM12,6h1v1h-1zM14,6h1v1h-1zM16,6h1v1h-1zM18,6h1v1h-1zM20,6h1v1h-1zM22,6h7v1h-7zM8,7h2v1h-2zM12,7h1v1h-1zM17,7h1v1h-1zM19,7h2v1h-2zM0,8h2v1h-2zM3,8h1v1h-1zM6,8h2v1h-2zM10,8h1v1h-1zM13,8h3v1h-3zM22,8h3v1h-3zM26,8h2v1h-2zM10,9h2v1h-2zM13,9h1v1h-1zM15,9h4v1h-4zM20,9h3v1h-3zM25,9h1v1h-1zM28,9h1v1h-1zM0,10h1v1h-1zM2,10h2v1h-2zM6,10h1v1h-1zM9,10h2v1h-2zM13,10h2v1h-2zM16,10h1v1h-1zM19,10h2v1h-2zM25,10h3v1h-3zM2,11h3v1h-3zM7,11h2v1h-2zM13,11h1v1h-1zM15,11h1v1h-1zM18,11h1v1h-1zM26,11h2v1h-2zM0,12h1v1h-1zM6,12h2v1h-2zM12,12h2v1h-2zM16,12h2v1h-2zM19,12h5v1h-5zM25,12h1v1h-1zM27,12h2v1h-2zM0,13h2v1h-2zM3,13h1v1h-1zM7,13h1v1h-1zM10,13h3v1h-3zM17,13h1v1h-1zM19,13h1v1h-1zM21,13h1v1h-1zM0,14h1v1h-1zM3,14h5v1h-5zM10,14h1v1h-1zM12,14h2v1h-2zM16,14h1v1h-1zM18,14h1v1h-1zM21,14h1v1h-1zM25,14h4v1h-4zM1,15h2v1h-2zM5,15h1v1h-1zM9,15h1v1h-1zM12,15h2v1h-2zM15,15h1v1h-1zM17,15h1v1h-1zM19,15h3v1h-3zM24,15h2v1h-2zM27,15h1v1h-1zM0,16h1v1h-1zM6,16h1v1h-1zM8,16h1v1h-1zM11,16h2v1h-2zM16,16h4v1h-4zM21,16h1v1h-1zM27,16h1v1h-1zM1,17h2v1h-2zM4,17h1v1h-1zM7,17h1v1h-1zM10,17h1v1h-1zM14,17h1v1h-1zM16,17h2v1h-2zM21,17h3v1h-3zM25,17h1v1h-1zM28,17h1v1h-1zM0,18h1v1h-1zM2,18h1v1h-1zM4,18h1v1h-1zM6,18h1v1h-1zM9,18h1v1h-1zM13,18h1v1h-1zM17,18h1v1h-1zM20,18h5v1h-5zM27,18h2v1h-2zM2,19h2v1h-2zM5,19h1v1h-1zM7,19h1v1h-1zM12,19h1v1h-1zM14,19h4v1h-4zM19,19h1v1h-1zM22,19h1v1h-1zM24,19h1v1h-1zM27,19h2v1h-2zM0,20h1v1h-1zM2,20h1v1h-1zM4,20h1v1h-1zM6,20h1v1h-1zM8,20h3v1h-3zM12,20h3v1h-3zM16,20h1v1h-1zM20,20h5v1h-5zM26,20h1v1h-1zM8,21h1v1h-1zM10,21h1v1h-1zM16,21h1v1h-1zM20,21h1v1h-1zM24,21h1v1h-1zM26,21h3v1h-3zM0,22h7v1h-7zM8,22h1v1h-1zM13,22h1v1h-1zM16,22h1v1h-1zM18,22h1v1h-1zM20,22h1v1h-1zM22,22h1v1h-1zM24,22h1v1h-1zM27,22h1v1h-1zM0,23h1v1h-1zM6,23h1v1h-1zM11,23h6v1h-6zM18,23h3v1h-3zM24,23h5v1h-5zM0,24h1v1h-1zM2,24h3v1h-3zM6,24h1v1h-1zM9,24h5v1h-5zM15,24h3v1h-3zM20,24h5v1h-5zM27,24h1v1h-1zM0,25h1v1h-1zM2,25h3v1h-3zM6,25h1v1h-1zM8,25h3v1h-3zM12,25h2v1h-2zM20,25h1v1h-1zM22,25h6v1h-6zM0,26h1v1h-1zM2,26h3v1h-3zM6,26h1v1h-1zM9,26h3v1h-3zM21,26h1v1h-1zM24,26h3v1h-3zM28,26h1v1h-1zM0,27h1v1h-1zM6,27h1v1h-1zM8,27h2v1h-2zM13,27h2v1h-2zM16,27h3v1h-3zM20,27h2v1h-2zM27,27h1v1h-1zM0,28h7v1h-7zM8,28h2v1h-2zM12,28h1v1h-1zM15,28h1v1h-1zM17,28h6v1h-6zM24,28h2v1h-2zM27,28h1v1h-1z"
    return f'''
    <!-- BLOQUE INSTITUCIONAL Y AUTORÍA DE CÓDIGO ABIERTO (ADOLFO MORALES TENA) - FORMATO AMPLIADO -->
    <g id="bloque_autoria" data-arrastrable="1" transform="translate({x}, {y})" filter="url(#shadowCard)">
      <!-- Fondo de la tarjeta -->
      <rect width="1860" height="561" rx="22" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" />
      
      <!-- Barra superior de acento degradado -->
      <path d="M 0 22 Q 0 0 22 0 L 1838 0 Q 1860 0 1860 22 L 1860 10 L 0 10 Z" fill="url(#gradHeaderAutoria)" />

      <!-- Encabezado superior -->
      <g transform="translate(35, 26)">
        <rect x="0" y="23" width="310" height="24" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2" />
        <text x="155" y="39" fill="#0369a1" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="1">METABOLISMO Y SU REGULACIÓN</text>
        <!-- Título en Arte ASCII: Mapa Metabólico -->
        <text x="340" y="10" fill="#0f172a" font-family="'JetBrains Mono', monospace" font-size="16" font-weight="700" xml:space="preserve" style="font-family: 'JetBrains Mono', 'DejaVu Sans Mono', Menlo, Consolas, monospace; font-variant-ligatures: none; font-feature-settings: 'liga' 0, 'calt' 0; white-space: pre; line-height: 20px;">
          <tspan x="340" y="10"> __  __   _   ___  _     __  __ ___ _____ _   ___  ___  _    ___ ___ ___  </tspan>
          <tspan x="340" y="30">|  \/  | /_\ | _ \/_\   |  \/  | __|_   _/_\ | _ )/ _ \| |  |_ _/ __/ _ \ </tspan>
          <tspan x="340" y="50">| |\/| |/ _ \|  _/ _ \  | |\/| | _|  | |/ _ \| _ \ (_) | |__ | | (__ (_) |</tspan>
          <tspan x="340" y="70">|_|  |_/_/ \_\_|/_/ \_\ |_|  |_|___| |_/_/ \_\___/\___/|____|___\___\___/ </tspan>
        </text>
        <rect x="1330" y="21" width="490" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
        <text x="1575" y="38" fill="#475569" font-size="10.5" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">ARQUITECTURA DE CÓDIGO ABIERTO • FORMATO ULTRA-HD</text>
      </g>
      <line x1="35" y1="120" x2="1825" y2="120" stroke="#e2e8f0" stroke-width="1.5" />

      <!-- ================= COLUMNA 1: AUTORÍA Y PROYECTO ================= -->
      <g transform="translate(35, 138)">
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" letter-spacing="1.2">AUTOR &amp; DESARROLLO:</text>
        <text x="0" y="48" fill="#0f172a" font-size="24" font-weight="900" font-family="'Inter', sans-serif">Adolfo Morales Tena</text>
        <text x="0" y="72" fill="#0284c7" font-size="13" font-weight="700" font-family="'Inter', sans-serif">Estudiante de Bioquímica y Biología Molecular</text>
        
        <rect x="0" y="94" width="465" height="42" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2" />
        <text x="16" y="112" fill="#334155" font-size="10" font-weight="700" font-family="'Inter', sans-serif">PROYECTO UNIVERSITARIO DE BIOQUÍMICA MÉDICA</text>
        <text x="16" y="126" fill="#64748b" font-size="9.5" font-family="'Inter', sans-serif">Mapas Metabólicos Integrados • Redes Bioquímicas de Alta Fidelidad</text>

        <!-- Botón interactivo de GitHub -->
        <g transform="translate(0, 155)">
          <a href="https://github.com/AMorales22T/mapa_metabolico" target="_blank">
            <rect x="0" y="0" width="465" height="52" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" style="cursor: pointer;" />
            <g transform="translate(16, 14)">
              <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" fill="#ffffff" />
            </g>
            <text x="52" y="22" fill="#94a3b8" font-size="10" font-weight="800" font-family="'Inter', sans-serif">REPOSITORIO ABIERTO EN GITHUB:</text>
            <text x="52" y="40" fill="#38bdf8" font-size="13" font-weight="700" font-family="'JetBrains Mono', monospace">https://amorales22t.github.io/mapa_metabolico</text>
          </a>
        </g>

        <!-- Bloque de licencia MIT -->
        <g transform="translate(0, 226)">
          <rect x="0" y="0" width="465" height="42" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
          <rect x="12" y="10" width="95" height="22" rx="5" fill="#e2e8f0" />
          <text x="59.5" y="25" fill="#334155" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MIT LICENSE</text>
          <text x="120" y="26" fill="#475569" font-size="10" font-weight="700" font-family="'Inter', sans-serif">Libre distribución, estudio y docencia biomédica</text>
        </g>
        
        <text x="0" y="302" fill="#64748b" font-size="10" font-weight="600" font-family="'Inter', sans-serif">Contribuciones, issues y sugerencias bienvenidas en GitHub.</text>
        <text x="0" y="320" fill="#94a3b8" font-size="9" font-family="'Inter', sans-serif">Diseñado y validado según estándares docentes internacionales.</text>
      </g>

      <!-- Divisor vertical 1 -->
      <line x1="535" y1="136" x2="535" y2="536" stroke="#e2e8f0" stroke-width="1.5" />

      <!-- ================= COLUMNA 2: FUENTES CIENTÍFICAS Y HERRAMIENTAS ================= -->
      <g transform="translate(565, 138)">
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" letter-spacing="1.2">FUENTES CIENTÍFICAS &amp; BIBLIOGRAFÍA DE REFERENCIA:</text>
        
        <g transform="translate(0, 32)">
          <text x="0" y="0" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">Lehninger: Principios de Bioquímica</tspan> (D. L. Nelson, M. M. Cox — 7.ª y 8.ª Ed., W. H. Freeman)</text>
          <text x="0" y="21" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">Harper: Bioquímica Ilustrada</tspan> (V. Rodwell, D. Bender, K. Botham, P. Kennelly, A. Weil — 31.ª y 32.ª Ed.)</text>
          <text x="0" y="42" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">Bioquímica con Aplicaciones Clínicas</tspan> (Thomas M. Devlin — 4.ª y 5.ª Ed., Ed. Reverté)</text>
          <text x="0" y="63" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">Bioquímica</tspan> (J. M. Berg, J. L. Tymoczko, G. J. Gatto Jr., L. Stryer — 8.ª y 9.ª Ed., Ed. Reverté / W.H. Freeman)</text>
          <text x="0" y="84" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">Biochemical Pathways: An Atlas of Biochemistry and Molecular Biology</tspan> (G. Michal &amp; D. Schomburg / Roche)</text>
          <text x="0" y="105" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">KEGG Pathway Database</tspan> &amp; Nomenclatura Enzimática Internacional (Comisión de Enzimas NC-IUBMB / IUPAC)</text>
        </g>

        <!-- Divisor interno horizontal -->
        <line x1="0" y1="165" x2="875" y2="165" stroke="#f1f5f9" stroke-width="1.5" />

        <text x="0" y="190" fill="#64748b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" letter-spacing="1.2">HERRAMIENTAS DE INGENIERÍA &amp; ARQUITECTURA TECNOLÓGICA:</text>
        <g transform="translate(0, 206)">
          <text x="0" y="0" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">Python 3:</tspan> Motor de generación algorítmica, geometría analítica de curvas Bézier y cálculo estequiométrico.</text>
          <text x="0" y="21" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">Algoritmo A* de Enrutamiento:</tspan> Conexión libre de colisiones entre metabolitos de vías cruzadas.</text>
          <text x="0" y="42" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">SVG 1.1 W3C:</tspan> Renderizado vectorial puro escalable sin pérdida de calidad (85+ metabolitos con fórmula química).</text>
          <text x="0" y="63" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">Stack Web (HTML5 / CSS3 / ES6):</tspan> Visores interactivos con zoom/pan (CTM), buscador reactivo y aislamiento de rutas.</text>
          <text x="0" y="84" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">librsvg (rsvg-convert) &amp; libqrencode:</tspan> Exportación a PDF Ultra-HD (1200×900 mm a 300 DPI) y QR vectorial.</text>
          <text x="0" y="105" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">Git &amp; GitHub Actions:</tspan> Control de versiones, integración continua e interoperabilidad abierta.</text>
        </g>
      </g>

      <!-- Divisor vertical 2 -->
      <line x1="1470" y1="136" x2="1470" y2="536" stroke="#e2e8f0" stroke-width="1.5" />

      <!-- ================= COLUMNA 3: CÓDIGO QR Y ESCANEO DIRECTO ================= -->
      <g transform="translate(1495, 138)">
        <text x="165" y="16" fill="#64748b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" letter-spacing="1.2" text-anchor="middle">ACCESO MÓVIL DIRECTO:</text>

        <!-- Contenedor QR estilizado -->
        <g transform="translate(20, 32)">
          <rect x="0" y="0" width="290" height="290" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.5" />
          <!-- Marco interior blanco -->
          <rect x="14" y="14" width="262" height="262" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
          <!-- QR escalado a 8.0x (29 módulos * 8.0 = 232 px, centrado en 262 con margen 15 px) -->
          <g transform="translate(29, 29) scale(8.0)">
            <path d="{qr_path}" fill="#0f172a" />
          </g>
        </g>

        <!-- Textos bajo el QR -->
        <text x="165" y="348" fill="#0f172a" font-size="13" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">ESCANEAR CON SMARTPHONE</text>
        <text x="165" y="368" fill="#0284c7" font-size="10" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">amorales22t.github.io/mapa_metabolico</text>
        <text x="165" y="388" fill="#64748b" font-size="9.5" font-weight="600" font-family="'Inter', sans-serif" text-anchor="middle">Acceso instantáneo al visor interactivo web,</text>
        <text x="165" y="402" fill="#64748b" font-size="9.5" font-weight="600" font-family="'Inter', sans-serif" text-anchor="middle">simuladores redox y descargas vectoriales PDF</text>
      </g>
    </g>
    '''

def cargar_cte_original_usuario():
    """
    Carga directamente el diseño vectorial exacto del archivo SVG que el usuario ya realizó:
    02_RESPIRACION_Y_ENERGIA/via_07_cadena_respiratoria_atp_sintasa/Cadena_Transporte_Electrones.svg
    """
    import re
    path_cte = os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "via_07_cadena_respiratoria_atp_sintasa", "Cadena_Transporte_Electrones.svg")
    with open(path_cte, "r", encoding="utf-8") as f:
        svg_content = f.read()

    defs_match = re.search(r'<defs>([\s\S]*?)</defs>', svg_content)
    cte_defs = defs_match.group(1) if defs_match else ""

    # Filtrar marcadores duplicados para no crear colisiones en el SVG principal
    for marker_id in ['arrowFlow', 'arrowRed', 'arrowGreen', 'arrowBlue']:
        cte_defs = re.sub(rf'<marker id="{marker_id}"[\s\S]*?</marker>', '', cte_defs)

    body_match = re.search(r'</defs>([\s\S]*?)</svg>', svg_content)
    cte_body = body_match.group(1) if body_match else ""

    # Ajustar el fondo matricial de 1740 a 820 para ceñirse a las reacciones activas
    cte_body = cte_body.replace('height="1740"', 'height="820"')
    
    # Eliminar la cresta derecha que protruye más allá del marco (forma en D de color melocotón en X=1150)
    cte_body = re.sub(r'<path d="M 1150 500 C 1080 500[^"]*" />', '', cte_body)

    return cte_defs, cte_body

def generar_seccion_ciclo_cori_y_musculo():
    """
    Genera el compartimento anatómico extendido del Músculo Esquelético (Vía 17: Ciclo de Cori)
    como franja horizontal continua de extremo a extremo (X=0 a X=5800, Y=10 a Y=340),
    bañado por el torrente sanguíneo vascular (Y=340 a Y=425) que comunica con el hepatocito.
    """
    # 1. Bandas A (Miosina - anisotropas densas periódicas)
    bandas_a = []
    for bx in range(75, 5740, 50):
        bandas_a.append(f'<rect x="{bx}" y="30" width="25" height="274" rx="3" fill="#be123c" opacity="0.055"/>')

    # 2. Discos Z (Líneas Z transversales con α-actinina)
    discos_z = []
    for zx in range(100, 5740, 50):
        discos_z.append(f'<line x1="{zx}" y1="28" x2="{zx}" y2="310" stroke="#9f1239" stroke-width="1.2" stroke-dasharray="4 2" opacity="0.3"/>')

    # 3. Miofibrillas longitudinales continuas
    miofibrillas = []
    for my in [55, 100, 145, 190, 235, 280]:
        miofibrillas.append(f'<line x1="55" y1="{my}" x2="5745" y2="{my}" stroke="#f43f5e" stroke-width="1.2" stroke-dasharray="28 14" opacity="0.22"/>')

    # 4. Túbulos T (invaginaciones sarcolémicas transversales periódicas)
    tubulos_t = []
    for tx in range(180, 5730, 160):
        tubulos_t.append(f'<line x1="{tx}" y1="340" x2="{tx}" y2="315" stroke="#f43f5e" stroke-width="2.2" stroke-linecap="round" opacity="0.65"/><circle cx="{tx}" cy="315" r="2.2" fill="#fda4af"/>')

    # 5. Núcleos periféricos subsarcolémicos multinucleados
    nucleos_sup = [350, 850, 1450, 2050, 2650, 3250, 3850, 4450, 5050, 5500]
    nucleos_inf = [600, 1150, 1750, 2350, 2950, 3550, 4150, 4750, 5300, 5650]
    nucleos_items = []
    for i, nx in enumerate(nucleos_sup, 1):
        nucleos_items.append(f'''
        <g transform="translate({nx}, 24)">
          <ellipse cx="0" cy="0" rx="30" ry="7.5" fill="#312e81" stroke="#4338ca" stroke-width="1.5"/>
          <ellipse cx="-2" cy="0" rx="15" ry="3.5" fill="#6366f1" opacity="0.8"/>
          <circle cx="6" cy="-1" r="1.8" fill="#e0e7ff"/>
          <text x="38" y="3" fill="#4338ca" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif">Núcleo subsarcolémico S{i}</text>
        </g>''')
    for j, nx in enumerate(nucleos_inf, 1):
        nucleos_items.append(f'''
        <g transform="translate({nx}, 325)">
          <ellipse cx="0" cy="0" rx="30" ry="7.5" fill="#312e81" stroke="#4338ca" stroke-width="1.5"/>
          <ellipse cx="-2" cy="0" rx="15" ry="3.5" fill="#6366f1" opacity="0.8"/>
          <circle cx="6" cy="-1" r="1.8" fill="#e0e7ff"/>
          <text x="-38" y="3" fill="#4338ca" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Núcleo subsarcolémico I{j}</text>
        </g>''')

    # 6. Gránulos de glucógeno sarcoplásmico
    glucogeno_pos = [280, 1620, 2520, 3420, 4320, 5220]
    glucogeno_items = []
    for gx in glucogeno_pos:
        glucogeno_items.append(f'''
        <g transform="translate({gx}, 285)" opacity="0.85">
          <circle cx="0" cy="0" r="3.5" fill="#f59e0b" stroke="#d97706" stroke-width="0.8"/>
          <circle cx="7" cy="-3" r="2.8" fill="#fbbf24"/>
          <circle cx="12" cy="2" r="3" fill="#f59e0b"/>
          <circle cx="5" cy="5" r="2.5" fill="#fbbf24"/>
          <text x="20" y="3" fill="#b45309" font-size="7" font-weight="800" font-family="'Inter', sans-serif">Glucógeno muscular (reserva contráctil)</text>
        </g>''')

    # 7. Sarcosomas (Mitocondrias interfibrilares)
    sarcosomas_pos = [1920, 2820, 3720, 4620, 5450]
    sarcosomas_items = []
    for sx in sarcosomas_pos:
        sarcosomas_items.append(f'''
        <g transform="translate({sx}, 210)" opacity="0.85">
          <ellipse cx="0" cy="0" rx="22" ry="12" fill="url(#gradMitocondria)" stroke="#92400e" stroke-width="1.6"/>
          <path d="M -12 0 C -6 -6, 0 6, 8 0" stroke="#b45309" stroke-width="1.8" fill="none" opacity="0.75"/>
          <text x="0" y="22" fill="#92400e" font-size="7" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Sarcosoma (ATP oxidativo)</text>
        </g>''')

    tubulos_str = ''.join(tubulos_t)
    bandas_str = ''.join(bandas_a)
    discos_str = ''.join(discos_z)
    miofibrillas_str = ''.join(miofibrillas)
    nucleos_str = ''.join(nucleos_items)
    glucogeno_str = ''.join(glucogeno_items)
    sarcosomas_str = ''.join(sarcosomas_items)

    return f"""
    <!-- ================================================================= -->
    <!-- RUTA 17: CICLO DE CORI (ACOPLAMIENTO MÚSCULO ESQUELÉTICO ⇄ HÍGADO) -->
    <!-- ================================================================= -->
    <g id="ruta_ciclo_cori" data-arrastrable="1">
      <!-- 1. COMPARTIMENTO ANATÓMICO EXTENDIDO DEL MÚSCULO ESQUELÉTICO (FRANJA COMPLETA 0 A 5800 PX) -->
      <g id="miocito_cori">
        <!-- Fondo y entorno biológico de la fibra muscular estriada -->
        <g id="musculo_esqueletico_biologico">
          <!-- Vientre Anatómico del Fascículo Muscular (Epimisio / Perimisio) -->
          <rect x="0" y="12" width="5800" height="328" fill="url(#gradVientreMuscular)" stroke="#9f1239" stroke-width="3"/>
          <rect x="0" y="16" width="5800" height="320" fill="url(#gradSarcoplasma)" opacity="0.92"/>

          <!-- Inserción Tendinosa / Aponeurosis Fascial Izquierda (X=0 a 55) -->
          <path d="M 0 12 L 55 12 L 55 340 L 0 340 Z" fill="url(#gradFasciaTendinosa)" stroke="#94a3b8" stroke-width="2"/>
          <g fill="none" stroke="#cbd5e1" stroke-width="1.3" stroke-linecap="round" opacity="0.75">
            <path d="M 5 60 Q 25 55 55 58"/>
            <path d="M 5 110 Q 28 105 55 108"/>
            <path d="M 5 160 Q 30 160 55 160"/>
            <path d="M 5 210 Q 28 215 55 212"/>
            <path d="M 5 260 Q 25 265 55 262"/>
            <path d="M 5 300 Q 25 305 55 302"/>
          </g>
          <text x="28" y="176" fill="#64748b" font-size="8" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle" transform="rotate(-90 28 176)" letter-spacing="1.5">INSERCIÓN TENDINOSA (FASCIA)</text>

          <!-- Inserción Tendinosa / Aponeurosis Fascial Derecha (X=5745 a 5800) -->
          <path d="M 5745 12 L 5800 12 L 5800 340 L 5745 340 Z" fill="url(#gradFasciaTendinosa)" stroke="#94a3b8" stroke-width="2"/>
          <g fill="none" stroke="#cbd5e1" stroke-width="1.3" stroke-linecap="round" opacity="0.75">
            <path d="M 5745 58 Q 5775 55 5795 60"/>
            <path d="M 5745 108 Q 5772 105 5795 110"/>
            <path d="M 5745 160 Q 5770 160 5795 160"/>
            <path d="M 5745 212 Q 5772 215 5795 210"/>
            <path d="M 5745 262 Q 5775 265 5795 260"/>
            <path d="M 5745 302 Q 5775 305 5795 300"/>
          </g>
          <text x="5772" y="176" fill="#64748b" font-size="8" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle" transform="rotate(-90 5772 176)" letter-spacing="1.5">INSERCIÓN TENDINOSA (FASCIA)</text>

          <!-- Sarcolema continuo inferior (Membrana plasmática excitable limitante en Y=340) -->
          <line x1="0" y1="340" x2="5800" y2="340" stroke="#9f1239" stroke-width="5" stroke-linecap="square"/>
          <line x1="0" y1="337" x2="5800" y2="337" stroke="#e11d48" stroke-width="2" stroke-dasharray="14 4"/>

          <!-- Túbulos T (Invaginaciones sarcolémicas transversales periódicas hacia el sarcoplasma) -->
          {tubulos_str}

          <!-- Estriaciones Histológicas Periódicas (Bandas A - Miosina Anisótropa) -->
          <g>
            {bandas_str}
          </g>

          <!-- Discos Z (Líneas Z transversales que delimitan cada sarcómero periódico) -->
          <g>
            {discos_str}
          </g>

          <!-- Miofibrillas longitudinales continuas (Haces paralelos de F-Actina y Miosina II) -->
          <g>
            {miofibrillas_str}
          </g>

          <!-- Núcleos Periféricos Subsarcolémicos (Sincitio multinucleado típico del miocito esquelético) -->
          {nucleos_str}

          <!-- Gránulos de Glucógeno Muscular Sarcoplásmico -->
          {glucogeno_str}

          <!-- Sarcosomas (Mitocondrias interfibrilares del miocito) -->
          {sarcosomas_str}

          <!-- Infografías ultraestructurales educativas integradas a lo largo de la fibra -->
          <!-- 1. Módulo Arquitectura del Sarcómero (X=2050) -->
          <g transform="translate(2050, 95)" opacity="0.9">
            <rect x="-200" y="-18" width="400" height="42" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.2"/>
            <text x="0" y="-4" fill="#9f1239" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">|◀───────────── SARCÓMERO (~2.5 µm) ─────────────▶|</text>
            <text x="0" y="10" fill="#be123c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Línea Z (α-Actinina) • Banda I (Actina F) • Banda A (Miosina II) • Zona H • Línea M</text>
            <text x="0" y="19" fill="#881337" font-size="6.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Unidad morfofuncional contráctil delimitada entre dos discos Z consecutivos</text>
          </g>

          <!-- 2. Módulo Tríada Sarcoplásmica (X=2950) -->
          <g transform="translate(2950, 95)" opacity="0.9">
            <rect x="-210" y="-18" width="420" height="42" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.2"/>
            <text x="0" y="-4" fill="#9f1239" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">TRÍADA SARCOPLÁSMICA &amp; ACOPLAMIENTO EXCITACIÓN-CONTRACCIÓN</text>
            <text x="0" y="10" fill="#be123c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Invaginación de Túbulo T flanqueada por 2 Cisternas terminales del Retículo Sarcoplásmico</text>
            <text x="0" y="19" fill="#881337" font-size="6.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Potencial de acción ➔ Sensor DHPR (Cav1.1) ➔ Canal Ryanodina (RyR1) ➔ Salida masiva de Ca²⁺</text>
          </g>

          <!-- 3. Módulo Puentes Cruzados (X=3890) -->
          <g transform="translate(3890, 95)" opacity="0.9">
            <rect x="-210" y="-18" width="420" height="42" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.2"/>
            <text x="0" y="-4" fill="#9f1239" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">CICLO DE PUENTES CRUZADOS &amp; DESLIZAMIENTO DE FILAMENTOS</text>
            <text x="0" y="10" fill="#be123c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Ca²⁺ se une a Troponina C ➔ Tropomiosina expone sitios activos de F-Actina</text>
            <text x="0" y="19" fill="#881337" font-size="6.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Cabezas de Miosina hidrolizan ATP (Miosina ATPasa) ➔ Golpe de fuerza contráctil (Power Stroke)</text>
          </g>

          <!-- 4. Módulo Bioenergética y Fosfágenos (X=4810) -->
          <g transform="translate(4810, 95)" opacity="0.9">
            <rect x="-210" y="-18" width="420" height="42" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.2"/>
            <text x="0" y="-4" fill="#9f1239" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">SISTEMA DE FOSFÁGENOS &amp; BIOENERGÉTICA CONTRÁCTIL INMEDIATA</text>
            <text x="0" y="10" fill="#be123c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Fosfocreatina (PCr) + ADP ⇄ Creatina + ATP (Creatina Cinasa CK-MM / Amortiguador primario)</text>
            <text x="0" y="19" fill="#881337" font-size="6.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Activación alostérica de Glucógeno Fosforilasa b por 5'-AMP muscular ➔ G1P ➔ Glucólisis rápida</text>
          </g>

          <!-- 5. Módulo Diferenciación de Fibras (X=5530) -->
          <g transform="translate(5530, 95)" opacity="0.9">
            <rect x="-170" y="-18" width="340" height="42" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.2"/>
            <text x="0" y="-4" fill="#9f1239" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">TIPOS DE FIBRAS MUSCULARES</text>
            <text x="0" y="10" fill="#be123c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Tipo I (Rojas, lentas, ricas en mioglobina y sarcosomas / Oxidativas)</text>
            <text x="0" y="19" fill="#881337" font-size="6.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Tipo IIb (Blancas, rápidas, anaerobias / Glucolíticas de alto poder)</text>
          </g>
        </g>

        <!-- Header y Título Editorial del Miocito Esquelético con Badge Vía 17 -->
        {badge_via(17, 85, 38)}
        <g transform="translate(120, 38)">
          <text x="0" y="0" fill="#881337" font-size="13.5" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="0.5">MÚSCULO ESQUELÉTICO (FIBRA SARCOLÉMICA ESTRIADA · CICLO DE CORI)</text>
          <text x="0" y="14" fill="#be123c" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Contracción anaerobia vigorosa • Glucólisis anaerobia rápida (+2 ATP netos) • Regeneración de NAD⁺ (LDH-M) • Exportación de Lactato</text>
        </g>

        <!-- Transportador muscular GLUT-4 en el sarcolema inferior (X=140, Y=340) -->
        <g id="carrier_glut4_musculo" transform="translate(107, 327)">
          <rect x="0" y="0" width="66" height="30" rx="6" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
          <text x="33" y="14" fill="#ffffff" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-4</text>
          <text x="33" y="24" fill="#e0f2fe" font-size="7" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">SLC2A4</text>
        </g>
        <!-- Flecha de captación: Glucosa entra desde el sarcolema inferior hacia el sarcoplasma -->
        <line x1="140" y1="327" x2="140" y2="238" stroke="#0284c7" stroke-width="2.4" marker-end="url(#arrowBlue)"/>
        <text x="150" y="285" fill="#0369a1" font-size="8" font-weight="800" font-family="'Inter', sans-serif">Captación ➔</text>

        <!-- Molécula 1: D-Glucosa Muscular (Estructura química completa) -->
        <g id="m_cori_glc_musc" data-arrastrable="1" transform="translate(95, 85)">
          <g>{GLUCOSA}</g>
          <text x="45" y="102" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">D-Glucosa</text>
          <text x="45" y="117" fill="#ea580c" font-size="10.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[6C] Muscular</text>
        </g>

        <!-- Reacción 1: Hexoquinasa muscular (HK-II) -->
        <g transform="translate(210, 130)">
          <line x1="0" y1="0" x2="150" y2="0" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
          <text x="75" y="-12" fill="#c2410c" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Hexoquinasa (HK-II)</text>
          <text x="75" y="-23" fill="#64748b" font-size="7.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 2.7.1.1</text>
          <rect x="43" y="8" width="64" height="18" rx="9" fill="#fee2e2" stroke="#dc2626" stroke-width="1.2"/>
          <text x="75" y="21" fill="#b91c1c" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">− 1 ATP</text>
        </g>

        <!-- Molécula 2: Glucosa-6-Fosfato (Atrapada en el miocito por ausencia de G6Pasa) -->
        <g id="m_cori_g6p_musc" data-arrastrable="1" transform="translate(385, 85)">
          <g>{GLUCOSA_6_FOSFATO}</g>
          <text x="45" y="102" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Glucosa-6-P</text>
          <text x="45" y="117" fill="#ea580c" font-size="10.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[6C] Atrapada</text>
          <rect x="-20" y="125" width="130" height="17" rx="8.5" fill="#fee2e2" stroke="#dc2626" stroke-width="1.1"/>
          <text x="45" y="137" fill="#b91c1c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">✕ Sin G6Pasa en músculo</text>
        </g>

        <!-- Reacción 2: Glucólisis anaerobia (PFK-1 ➔ Aldolasa ➔ GAPDH ➔ Piruvato Quinasa) -->
        <g transform="translate(520, 130)">
          <line x1="0" y1="0" x2="150" y2="0" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
          <text x="75" y="-12" fill="#c2410c" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">PFK-1 ➔ Piruvato Quinasa</text>
          <text x="75" y="-23" fill="#64748b" font-size="7.5" font-family="'Inter', sans-serif" text-anchor="middle">Glucólisis anaerobia</text>
          <rect x="37" y="8" width="76" height="18" rx="9" fill="#dcfce7" stroke="#16a34a" stroke-width="1.2"/>
          <text x="75" y="21" fill="#15803d" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">+ 2 ATP (neto)</text>
        </g>

        <!-- Molécula 3: Piruvato Muscular (Estructura química completa) -->
        <g id="m_cori_pyr_musc" data-arrastrable="1" transform="translate(695, 85)">
          <g>{PIRUVATO}</g>
          <text x="45" y="102" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Piruvato (x2)</text>
          <text x="45" y="117" fill="#ea580c" font-size="10.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[3C]</text>
        </g>

        <!-- Reacción 3: Lactato Deshidrogenasa muscular (LDH-M / LDHA) -->
        <g transform="translate(805, 130)">
          <line x1="0" y1="0" x2="160" y2="0" stroke="#e11d48" stroke-width="2.6" marker-end="url(#arrowRed)"/>
          <text x="80" y="-17" fill="#be123c" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">LDH-M (LDHA)</text>
          <text x="80" y="-6" fill="#64748b" font-size="8" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 1.1.1.27</text>
          <rect x="18" y="8" width="124" height="18" rx="9" fill="#fee2e2" stroke="#dc2626" stroke-width="1.2"/>
          <text x="80" y="21" fill="#b91c1c" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">+ 2 NADH ➔ + 2 NAD⁺</text>
        </g>

        <!-- Molécula 4: L-Lactato Muscular (Estructura química completa) -->
        <g id="m_cori_lac_musc" data-arrastrable="1" transform="translate(990, 85)">
          <g>{GLUCONEO_LACTATO}</g>
          <text x="45" y="102" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Lactato (x2)</text>
          <text x="45" y="117" fill="#e11d48" font-size="10.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[3C]</text>
        </g>

        <!-- Exportación de Lactato hacia MCT4 en el sarcolema inferior -->
        <path d="M 1085 130 C 1170 130, 1220 200, 1245 320" fill="none" stroke="#e11d48" stroke-width="2.4" marker-end="url(#arrowRed)"/>
        <text x="1135" y="112" fill="#be123c" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">Exporta ➔</text>

        <!-- Transportador sarcolémico MCT4 (SLC16A3) en el sarcolema inferior (X=1248, Y=340) -->
        <g id="carrier_mct4_musculo" transform="translate(1215, 327)">
          <rect x="0" y="0" width="66" height="30" rx="6" fill="#be123c" stroke="#881337" stroke-width="2"/>
          <text x="33" y="14" fill="#ffffff" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MCT4</text>
          <text x="33" y="24" fill="#fecdd3" font-size="7" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">SLC16A3</text>
        </g>
      </g>

      <!-- 2. FLUJOS SANGUÍNEOS CONECTORES Y BIOMOLÉCULAS EN EL TORRENTE VASCULAR -->
      <!-- Biomolécula real de L-Lactato flotando en el torrente sanguíneo (Cori ➔ Hígado) -->
      <g id="m_cori_lac_sangre" data-arrastrable="1" transform="translate(1533, 382)">
        <!-- Cápsula vascular flotante con sombra plasmática -->
        <rect x="-34" y="-28" width="68" height="58" rx="8" fill="#fff1f2" stroke="#e11d48" stroke-width="1.6" filter="drop-shadow(0 2px 5px rgba(190,18,60,0.2))"/>
        
        <!-- Estructura molecular de L-Lactato en sangre -->
        <g transform="translate(-30, -26) scale(0.64)">
          <!-- C1: Carboxilato Superior -->
          <text x="47" y="15" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
          <line x1="47" y1="20" x2="47" y2="30" stroke="#0f172a" stroke-width="1.8" />

          <!-- C2: Carbono quiral H-C-OH -->
          <line x1="40" y1="37" x2="31" y2="37" stroke="#0f172a" stroke-width="1.6" />
          <text x="25" y="41" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#64748b" text-anchor="end">H</text>
          <text x="47" y="41" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" text-anchor="middle">C</text>
          <line x1="54" y1="37" x2="63" y2="37" stroke="#0284c7" stroke-width="1.6" />
          <text x="70" y="41" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0284c7">OH</text>

          <!-- Enlace C2 - C3 -->
          <line x1="47" y1="45" x2="47" y2="55" stroke="#0f172a" stroke-width="1.8" />

          <!-- C3: Grupo Metilo -->
          <text x="47" y="67" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">CH₃</text>
        </g>
        <!-- Rótulo contenido dentro de la cápsula -->
        <text x="0" y="24" font-family="'Inter', sans-serif" font-size="7" font-weight="900" fill="#9f1239" text-anchor="middle">L-Lactato [3C]</text>
      </g>

      <!-- Flujo 1: Lactato muscular sale de MCT4 y viaja a la molécula de L-Lactato en sangre -->
      <path d="M 1248 358 L 1248 398 L 1495 398 L 1499 382" fill="none" stroke="#fb7185" stroke-width="3" stroke-dasharray="6 3" marker-end="url(#arrowRed)"/>

      <!-- Flujo 2: L-Lactato sanguíneo continúa hacia MCT1 hepático -->
      <path d="M 1567 382 L 1587 382 L 1587 403" fill="none" stroke="#fb7185" stroke-width="3" stroke-dasharray="6 3" marker-end="url(#arrowRed)"/>

      <!-- Flujo 3: Glucosa neoglucogénica sale de GLUT-2 hepático y viaja hacia GLUT-4 muscular -->
      <path d="M 1480 415 L 1480 368 L 140 368 L 140 358" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="8 4" marker-end="url(#arrowBlue)"/>
      <g transform="translate(750, 352)">
        <rect x="-110" y="-9" width="220" height="18" rx="5" fill="#082f49" stroke="#0284c7" stroke-width="1" opacity="0.95"/>
        <text x="0" y="3.5" fill="#e0f2fe" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">Glucosa neoglucogénica ➔ Músculo (GLUT-4)</text>
      </g>

      <!-- 3. BALANCE BIOEDITORIAL DEL CICLO EN PILLS COMPACTAS (EN EL LUMEN VASCULAR) -->
      <g id="balance_pills_cori">
        <!-- Pill Músculo -->
        <g transform="translate(1840, 385)">
          <rect x="-135" y="-10" width="270" height="20" rx="10" fill="#ffe4e6" stroke="#be123c" stroke-width="1.5"/>
          <text x="0" y="4" fill="#be123c" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">MÚSCULO · Glucólisis anaerobia · +2 ATP netos</text>
        </g>

        <!-- Pill Hígado -->
        <g transform="translate(2200, 385)">
          <rect x="-165" y="-10" width="330" height="20" rx="10" fill="#fef3c7" stroke="#a16207" stroke-width="1.5"/>
          <text x="0" y="4" fill="#a16207" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">HÍGADO · Gluconeogénesis · −6 ~P (−4 ATP, −2 GTP)</text>
        </g>

        <!-- Pill Balance Neto -->
        <g transform="translate(2580, 385)">
          <rect x="-165" y="-10" width="330" height="20" rx="10" fill="#fee2e2" stroke="#b91c1c" stroke-width="1.5"/>
          <text x="0" y="4" fill="#b91c1c" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">BALANCE NETO · −4 ATP (Deuda de O₂ saldada)</text>
        </g>
      </g>

      <!-- 4. CONTINUIDAD DE LA CIRCULACIÓN SISTÉMICA & ÓRGANOS EXTRAHEPÁTICOS -->
      <g id="sistema_vascular_extrahepatico">
        <g transform="translate(3400, 385)">
          <rect x="-180" y="-11" width="360" height="22" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1" opacity="0.9"/>
          <text x="0" y="4" fill="#fecdd3" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="0.5">CIRCULACIÓN SISTÉMICA VASCULAR · HOMEOSTASIS DEL ORGANISMO</text>
        </g>

        <g transform="translate(4250, 385)">
          <rect x="-190" y="-11" width="380" height="22" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1" opacity="0.9"/>
          <text x="0" y="4" fill="#fecdd3" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="0.5">TRANSPORTE DE LÍPIDOS &amp; CUERPOS CETÓNICOS (ALBÚMINA / LIPOPROTEÍNAS)</text>
        </g>

        <g transform="translate(5150, 385)">
          <rect x="-170" y="-11" width="340" height="22" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1" opacity="0.9"/>
          <text x="0" y="4" fill="#fecdd3" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="0.5">DEPURACIÓN RENAL · EXCRECIÓN DE UREA Y ÁCIDO ÚRICO</text>
        </g>
      </g>
    </g>
    """

def construir_mapa_organico():
    partes = []

    # =========================================================================
    # 1. ENTORNO BIOLÓGICO CONTINUO (SIN GLOBOS)
    # =========================================================================
    partes.append(f"""
    <!-- ================================================================= -->
    <!-- CAPA FONDO CITOPLASMÁTICO ACUOSO                                  -->
    <!-- ================================================================= -->
    <rect width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" fill="url(#gradCitosolUnificado)"/>
    <ellipse cx="{ANCHO_CANVAS/2}" cy="1200" rx="{ANCHO_CANVAS*0.48}" ry="1050" fill="url(#haloCitosolUnificado)"/>

    <!-- Etiqueta de orientación sutil -->
    <g transform="translate(140, 480)" opacity="0.8">
      <text x="0" y="0" fill="#334155" font-size="20" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="3">CITOSOL</text>
      <path d="M 0 10 Q 100 20 200 10" fill="none" stroke="#94a3b8" stroke-width="2"/>
    </g>

    <!-- Microfilamentos del citoesqueleto atravesando el citoplasma -->
    <g fill="none" stroke="#cbd5e1" opacity="0.3">
      <path d="M 60 480 Q 800 420 1600 500 T 3200 460 T 3750 510" stroke-width="2.5" stroke-dasharray="16 12"/>
      <path d="M 60 920 Q 750 990 1500 910 T 3000 950 T 3750 890" stroke-width="2" stroke-dasharray="12 14"/>
      <path d="M 60 1480 Q 900 1400 1800 1490 T 3300 1450 T 3750 1500" stroke-width="2.2" stroke-dasharray="14 10"/>
      <path d="M 60 1980 Q 800 2060 1700 1980 T 3200 2020 T 3750 1970" stroke-width="2" stroke-dasharray="12 12"/>
    </g>

    <!-- Polirribosomas en racimos tenues -->
    <g fill="#64748b" opacity="0.22">
      <g transform="translate(180, 360)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/><circle cx="7" cy="15" r="2.8"/><circle cx="-2" cy="11" r="3.2"/></g>
      <g transform="translate(1120, 480)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/><circle cx="7" cy="15" r="2.8"/><circle cx="-2" cy="11" r="3.2"/></g>
      <g transform="translate(2350, 420)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/><circle cx="7" cy="15" r="2.8"/><circle cx="-2" cy="11" r="3.2"/></g>
      <g transform="translate(3450, 560)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/><circle cx="7" cy="15" r="2.8"/><circle cx="-2" cy="11" r="3.2"/></g>
      <g transform="translate(1080, 1680)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/></g>
      <g transform="translate(2420, 1720)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/></g>
    </g>

    <!-- Vesículas citosólicas translúcidas -->
    <g opacity="0.32">
      <circle cx="260" cy="520" r="26" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
      <circle cx="1250" cy="740" r="24" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2"/>
      <circle cx="2300" cy="800" r="22" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
      <circle cx="3480" cy="980" r="28" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
    </g>
    """)

    # =========================================================================
    # 0. BANDA SUPERIOR: CICLO DE CORI (ACOPLAMIENTO MÚSCULO ⇄ HÍGADO) - VÍA 17
    # =========================================================================
    partes.append(generar_seccion_ciclo_cori_y_musculo())

    # =========================================================================
    # ENTORNO HEPATOCELULAR PRINCIPAL (DESPLAZADO POR Y_OFFSET)
    # =========================================================================
    partes.append(f'<g id="entorno_hepatocito" transform="translate(0, {Y_OFFSET})">')

    # =========================================================================
    # CAPA SANGUÍNEA: TORRENTE VASCULAR / LUMEN CAPILAR REAL
    # =========================================================================
    partes.append(f"""
    <!-- Fondo del Plasma Sanguíneo con Gradiente Vascular Profundo -->
    <path d="M 0 0 L {ANCHO_CANVAS} 0 L {ANCHO_CANVAS} 68 Q {ANCHO_CANVAS*0.5} 95 0 68 Z" fill="url(#gradPlasmaSanguineo)"/>
    
    <!-- Corriente de plasma / flujo sanguíneo laminar -->
    <g fill="none" stroke="#ef4444" opacity="0.3" stroke-linecap="round">
      <path d="M 0 16 Q 800 24 1600 18 T 3200 22 T {ANCHO_CANVAS} 18" stroke-width="2.5" stroke-dasharray="25 15"/>
      <path d="M 0 35 Q 900 42 1800 34 T 3400 38 T {ANCHO_CANVAS} 36" stroke-width="3" stroke-dasharray="35 20"/>
      <path d="M 0 52 Q 750 60 1500 52 T 3100 58 T {ANCHO_CANVAS} 54" stroke-width="2" stroke-dasharray="20 18"/>
    </g>

    <!-- Eritrocitos / Glóbulos Rojos (Bicóncavos) flotando en la sangre -->
    <g id="eritrocitos_torrente" opacity="0.88">
      <!-- Eritrocito 1 (Zona izquierda, cerca de Palmitato) -->
      <g transform="translate(220, 36) rotate(-12)">
        <ellipse cx="0" cy="0" rx="26" ry="17" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="14" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(360, 48) rotate(18)">
        <ellipse cx="0" cy="0" rx="22" ry="14" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.5"/>
        <ellipse cx="0" cy="0" rx="11" ry="6" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
      <g transform="translate(680, 28) rotate(-8)">
        <ellipse cx="0" cy="0" rx="25" ry="16" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="13" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>

      <!-- Eritrocitos 2 (Zona central, cerca de Glucosa / GLUT-4) -->
      <g transform="translate(1200, 38) rotate(15)">
        <ellipse cx="0" cy="0" rx="27" ry="18" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="14" ry="9" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(1480, 26) rotate(-20)">
        <ellipse cx="0" cy="0" rx="24" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6"/>
        <ellipse cx="0" cy="0" rx="12" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
      <g transform="translate(1880, 32) rotate(10)">
        <ellipse cx="0" cy="0" rx="26" ry="17" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="13" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>

      <!-- Eritrocitos 3 (Zona derecha, cerca de Pentosas y Lípidos) -->
      <g transform="translate(2400, 42) rotate(-14)">
        <ellipse cx="0" cy="0" rx="25" ry="16" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="13" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(2750, 24) rotate(22)">
        <ellipse cx="0" cy="0" rx="23" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6"/>
        <ellipse cx="0" cy="0" rx="11" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
      <g transform="translate(3250, 38) rotate(-6)">
        <ellipse cx="0" cy="0" rx="26" ry="17" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="14" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(3580, 28) rotate(16)">
        <ellipse cx="0" cy="0" rx="24" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6"/>
        <ellipse cx="0" cy="0" rx="12" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
      <!-- Eritrocitos 4 (Zona derecha ampliada - Ciclo de la Urea y Excreción) -->
      <g transform="translate(4150, 36) rotate(12)">
        <ellipse cx="0" cy="0" rx="25" ry="16" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="13" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(4650, 42) rotate(-15)">
        <ellipse cx="0" cy="0" rx="24" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6"/>
        <ellipse cx="0" cy="0" rx="12" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
      <!-- Eritrocitos 5 (Zona extendida derecha - Nucleótidos y Eliminación de Urato) -->
      <g transform="translate(5080, 34) rotate(14)">
        <ellipse cx="0" cy="0" rx="25" ry="16" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="13" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(5450, 40) rotate(-10)">
        <ellipse cx="0" cy="0" rx="24" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6"/>
        <ellipse cx="0" cy="0" rx="12" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
    </g>

    <!-- Albúmina sérica y Lipoproteínas en el plasma -->
    <g opacity="0.6">
      <ellipse cx="490" cy="24" rx="16" ry="11" fill="#fef08a" stroke="#ca8a04" stroke-width="1.2"/>
      <text x="490" y="27" fill="#854d0e" font-size="7.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">ALBÚMINA</text>
      <ellipse cx="2950" cy="28" rx="18" ry="12" fill="#fed7aa" stroke="#ea580c" stroke-width="1.2"/>
      <text x="2950" y="32" fill="#9a3412" font-size="7.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">VLDL / HDL</text>
    </g>

    <!-- Rótulo Principal del Torrente Sanguíneo -->
    <g transform="translate(60, 32)">
      <rect x="0" y="-18" width="230" height="28" rx="6" fill="#450a0a" stroke="#b91c1c" stroke-width="1.5" opacity="0.85"/>
      <text x="14" y="2" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#fecaca" letter-spacing="2.5">
        TORRENTE SANGUÍNEO
      </text>
    </g>

    <!-- ================================================================= -->
    <!-- MEMBRANA PLASMÁTICA CONTINUA Y CANAL GLUT-4 (ARRIBA)              -->
    <!-- ================================================================= -->
    <!-- Doble Bicapa Fosfolipídica Ondulada (Límite Celular) -->
    <path d="M 0 68 Q 1225 95 2450 68 T 4900 68 T {ANCHO_CANVAS} 68" fill="none" stroke="#0284c7" stroke-width="10" stroke-linecap="round"/>
    <path d="M 0 78 Q 1225 105 2450 78 T 4900 78 T {ANCHO_CANVAS} 78" fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>

    <!-- Cabezas polares fosfolipídicas -->
    <g fill="#0284c7" opacity="0.75">
      <circle cx="150" cy="73" r="3.4"/><circle cx="168" cy="75" r="3.4"/><circle cx="186" cy="77" r="3.4"/>
      <circle cx="950" cy="82" r="3.4"/><circle cx="968" cy="81" r="3.4"/><circle cx="986" cy="79" r="3.4"/>
      <circle cx="2800" cy="79" r="3.4"/><circle cx="2818" cy="77" r="3.4"/><circle cx="2836" cy="75" r="3.4"/>
    </g>

    <!-- Canal Transportador GLUT-4 (alineado con la Glucólisis en X=1680) -->
    <g transform="translate(1640, 80)">
      <path d="M 0 6 C 10 -14, 28 -14, 34 6 C 38 20, 34 38, 25 44 C 12 47, 2 37, 0 24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
      <path d="M 80 6 C 70 -14, 52 -14, 46 6 C 42 20, 46 38, 55 44 C 68 47, 78 37, 80 24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
      <ellipse cx="40" cy="22" rx="12" ry="20" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
      <!-- Glucosa entrando desde la sangre -->
      <polygon points="40,15 46,18 46,25 40,28 34,25 34,18" fill="#ffffff" stroke="#ea580c" stroke-width="1.8"/>
      <circle cx="34" cy="18" r="2.2" fill="#dc2626"/>
      <text x="40" y="52" fill="#0369a1" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-4</text>
    </g>

    <!-- Flujo de Glucosa desde la sangre hacia la primera reacción -->
    <line x1="1680" y1="52" x2="1680" y2="80" stroke="#ea580c" stroke-width="2.6"/>
    <line x1="1680" y1="135" x2="1680" y2="152" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

    <!-- Receptor GLUT-4 en membrana plasmática -->
    """)

    # =========================================================================
    # 2. GRAN MITOCONDRIA BIOLÓGICA (BASE INFERIOR AMPLIA)
    # =========================================================================
    y_mito = 2160
    partes.append(f"""
    <!-- ================================================================= -->
    <!-- CAPA MATRIZ MITOCONDRIAL ARRIÑONADA Y CRESTAS INTERNAS            -->
    <!-- ================================================================= -->
    <g id="mitocondria_biologica">
      <!-- Membrana Mitocondrial Externa (MME) -->
      <path d="M 35 {y_mito + 180} 
               C 160 {y_mito - 30}, 850 {y_mito - 90}, 1520 {y_mito - 40}
               C 1950 {y_mito - 110}, 2650 {y_mito - 80}, 3350 {y_mito - 30}
               C 3850 {y_mito - 40}, 4350 {y_mito - 20}, 4740 {y_mito + 20}
               C 4880 {y_mito + 100}, 4880 {y_mito + 500}, 4850 {y_mito + 900}
               C 4820 {y_mito + 1400}, 4760 {y_mito + 1800}, 4400 {y_mito + 1940}
               C 3900 {y_mito + 1960}, 2850 {y_mito + 1950}, 1900 {y_mito + 1930}
               C 1100 {y_mito + 1950}, 260 {y_mito + 1850}, 65 {y_mito + 1300}
               C 20 {y_mito + 800}, 18 {y_mito + 400}, 35 {y_mito + 180} Z"
            fill="url(#gradMitocondria)" stroke="#92400e" stroke-width="6"/>

      <!-- Espacio Intermembrana (EIM) -->
      <path d="M 65 {y_mito + 195} 
               C 200 {y_mito}, 870 {y_mito - 55}, 1520 {y_mito - 10}
               C 1940 {y_mito - 75}, 2640 {y_mito - 45}, 3320 {y_mito}
               C 3820 {y_mito - 10}, 4320 {y_mito + 10}, 4700 {y_mito + 45}
               C 4830 {y_mito + 115}, 4830 {y_mito + 490}, 4805 {y_mito + 880}
               C 4775 {y_mito + 1370}, 4715 {y_mito + 1750}, 4370 {y_mito + 1895}
               C 3880 {y_mito + 1910}, 2830 {y_mito + 1900}, 1900 {y_mito + 1885}
               C 1120 {y_mito + 1900}, 300 {y_mito + 1805}, 95 {y_mito + 1275}
               C 48 {y_mito + 790}, 45 {y_mito + 405}, 65 {y_mito + 195} Z"
            fill="#fffbeb" fill-opacity="0.6" stroke="#b45309" stroke-width="3" stroke-dasharray="12 7"/>

      <!-- Matriz Mitocondrial (MMI Contorno interno) -->
      <path d="M 100 {y_mito + 220} 
               C 250 {y_mito + 45}, 900 {y_mito}, 1520 {y_mito + 35}
               C 1920 {y_mito - 25}, 2620 {y_mito}, 3280 {y_mito + 45}
               C 3780 {y_mito + 35}, 4280 {y_mito + 50}, 4650 {y_mito + 80}
               C 4770 {y_mito + 140}, 4770 {y_mito + 480}, 4750 {y_mito + 850}
               C 4720 {y_mito + 1330}, 4660 {y_mito + 1700}, 4330 {y_mito + 1845}
               C 3850 {y_mito + 1855}, 2800 {y_mito + 1845}, 1900 {y_mito + 1830}
               C 1150 {y_mito + 1845}, 350 {y_mito + 1755}, 130 {y_mito + 1245}
               C 80 {y_mito + 780}, 75 {y_mito + 425}, 100 {y_mito + 220} Z"
            fill="#fef3c7" fill-opacity="0.4" stroke="#d97706" stroke-width="3.5"/>

      <!-- Crestas Mitocondriales Profundas (Pliegues de MMI) -->
      <g fill="none" stroke="#b45309" stroke-width="5" stroke-linecap="round" opacity="0.65">
        <path d="M 450 {y_mito + 780} C 580 {y_mito + 620}, 720 {y_mito + 850}, 860 {y_mito + 710}"/>
        <!-- Cresta ajustada para no cortar el Ciclo de Krebs (α-KG DH en X=1195, Y=2795) -->
        <path d="M 960 {y_mito + 980} C 1090 {y_mito + 880}, 1240 {y_mito + 1020}, 1380 {y_mito + 920}"/>
        <path d="M 1520 {y_mito + 820} C 1650 {y_mito + 650}, 1800 {y_mito + 870}, 1940 {y_mito + 720}"/>
        <path d="M 2100 {y_mito + 850} C 2240 {y_mito + 670}, 2390 {y_mito + 890}, 2530 {y_mito + 740}"/>
        <path d="M 2700 {y_mito + 810} C 2850 {y_mito + 630}, 3000 {y_mito + 860}, 3150 {y_mito + 710}"/>
        <path d="M 650 {y_mito + 1380} C 820 {y_mito + 1220}, 1020 {y_mito + 1450}, 1200 {y_mito + 1310}"/>
        <path d="M 1600 {y_mito + 1420} C 1800 {y_mito + 1240}, 2050 {y_mito + 1480}, 2250 {y_mito + 1320}"/>
      </g>

      <!-- Rótulo de la Matriz integrado orgánicamente (reubicado en la franja inferior libre de la matriz,
           entre la lupa PDH y el borde inferior, para no estorbar a MPC / PC / Acetil-CoA ni a las conexiones) -->
      <g id="rotulo_matriz_mitocondrial" transform="translate(3300, {y_mito + 1720})" opacity="0.85">
        <text x="0" y="0" fill="#78350f" font-size="22" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="4" text-anchor="middle">MATRIZ MITOCONDRIAL</text>
        <text x="0" y="20" fill="#92400e" font-size="12" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Oxidación celular • Descarboxilación • Respiración</text>
      </g>

      <!-- Transportador MPC en el punto de contacto con el Piruvato (X=1680) -->
      <g transform="translate(1645, {y_mito - 55})">
        <rect x="0" y="0" width="70" height="42" rx="10" fill="#92400e" stroke="#78350f" stroke-width="2.5"/>
        <text x="35" y="27" fill="#ffffff" font-size="16" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MPC</text>
      </g>
      <text x="1730" y="{y_mito - 30}" fill="#78350f" font-size="12" font-weight="800" font-family="'Inter', sans-serif">Carrier de Piruvato (MPC1/2)</text>

      <!-- Ancla anatómica sobre la MME lateral derecha para la Lanzadera de Glicerol-3-P -->
      <g id="ancla_lanzadera_g3p" transform="translate(4850, 3060)">
        <rect x="-55" y="-16" width="110" height="32" rx="8" fill="#ea580c" stroke="#c2410c" stroke-width="2"/>
        <text x="0" y="4" fill="#ffffff" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MME / VDAC</text>
        <text x="0" y="25" fill="#9a3412" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Lanzadera G-3-P</text>
      </g>

      <!-- ================================================================= -->
      <!-- CONOS DE PROYECCIÓN CIENTÍFICOS PARA LAS 4 LUPAS (ZOOM CALLOUTS)   -->
      <!-- ================================================================= -->
      <g id="conos_proyeccion_lupas" opacity="0.45">
        <!-- 1. Cono hacia Lupa Lanzadera Malato-Aspartato (MMI superior ➔ Lupa 8A) -->
        <polygon points="1026,{y_mito - 16} 716,1854 1336,1854" fill="#0284c7" fill-opacity="0.04"/>
        <line x1="1026" y1="{y_mito - 16}" x2="716" y2="1854" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="6 4"/>
        <line x1="1026" y1="{y_mito - 16}" x2="1336" y2="1854" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="6 4"/>

        <!-- 2. Cono hacia Lupa CTE (Cresta MMI ➔ Marco panorámico CTE) -->
        <polygon points="2633,{y_mito + 25} 2553,2440 3743,2440" fill="#0284c7" fill-opacity="0.04"/>
        <line x1="2633" y1="{y_mito + 25}" x2="2553" y2="2440" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="6 4"/>
        <line x1="2633" y1="{y_mito + 25}" x2="3743" y2="2440" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="6 4"/>

        <!-- 4. Cono hacia Lupa Lanzadera Glicerol-3-P (MME derecha ➔ Panel Vía 8B) -->
        <polygon points="4850,3060 5070,2935 5070,3330" fill="#ea580c" fill-opacity="0.04"/>
        <line x1="4850" y1="3060" x2="5070" y2="2935" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="6 4"/>
        <line x1="4850" y1="3060" x2="5070" y2="3330" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="6 4"/>
      </g>
    </g>
    """)

    # =========================================================================
    # 3. EJE CENTRAL: GLUCÓLISIS VERTICAL (LIBRE EN CITOSOL)
    # =========================================================================
    x_g = 1680
    y_g = 160
    paso_y = 175

    partes.append(f'<g id="ruta_glucolisis">')
    
    # 1. Glucosa
    partes.append(nodo_libre(x_g - 40, y_g, "D-Glucosa", "6C", GLUCOSA, "m_glucosa"))
    partes.append(badge_via(1, x_g - 80, y_g + 30))
    partes.append(reaccion_libre(x_g, y_g + 105, 52, "Hexocinasa", entra="-1 ATP", sale="+1 ADP", id_rx="rx_hk"))
    partes.append(etiqueta_regulacion("hk", x_g + 95, y_g + 115, dx=0, dy=0))

    # 2. G6P
    partes.append(nodo_libre(x_g - 40, y_g + paso_y, "Glucosa-6-Fosfato", "6C", GLUCOSA_6_FOSFATO, "m_g6p"))
    partes.append(reaccion_libre(x_g, y_g + paso_y + 105, 52, "Fosfoglucosa Isomerasa", reversible=True, id_rx="rx_pgi"))

    # 3. F6P
    partes.append(nodo_libre(x_g - 40, y_g + paso_y * 2, "Fructosa-6-Fosfato", "6C", FRUCTOSA_6_FOSFATO, "m_f6p"))
    partes.append(reaccion_libre(x_g, y_g + paso_y * 2 + 105, 52, "PFK-1", entra="-1 ATP", sale="+1 ADP", id_rx="rx_pfk1"))
    partes.append(etiqueta_regulacion("pfk1", x_g + 95, y_g + paso_y * 2 + 115, dx=0, dy=0))
    partes.append("""
      <!-- Mini-recuadro regulador: Enzima Bifuncional PFK-2 / FBPasa-2 -->
      <g id="recuadro_pfk2_fbpasa2" transform="translate(1260, 485)">
        <rect x="0" y="0" width="220" height="90" rx="8" fill="#f8fafc" stroke="#7c3aed" stroke-width="1.8" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.06))"/>
        <text x="110" y="18" fill="#5b21b6" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">PFK-2 / FBPasa-2</text>
        <text x="110" y="32" fill="#6d28d9" font-size="9.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Enzima Tándem Reguladora</text>
        <line x1="12" y1="40" x2="208" y2="40" stroke="#ddd6fe" stroke-width="1"/>
        <text x="15" y="55" fill="#16a34a" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">[Hormonal] Insulina (PP2A) ➔ ↑ F-2,6-BP</text>
        <text x="15" y="69" fill="#dc2626" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">[Hormonal] Glucagón (PKA) ➔ ↓ F-2,6-BP</text>
        <text x="15" y="82" fill="#0284c7" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">F-2,6-BP: (+) PFK-1 / (-) FBPasa-1</text>
      </g>
""")

    # 4. F-1,6-BP
    partes.append(nodo_libre(x_g - 40, y_g + paso_y * 3, "Fructosa-1,6-Bisfosfato", "6C", FRUCTOSA_1_6_BISFOSFATO, "m_fbp"))
    partes.append(reaccion_libre(x_g, y_g + paso_y * 3 + 105, 52, "Aldolasa", reversible=True, id_rx="rx_aldo"))

    # 5. DHAP y GAP
    partes.append(nodo_libre(x_g - 250, y_g + paso_y * 4, "Dihidroxiacetona-P", "3C", DIHIDROXIACETONA_FOSFATO, "m_dhap", text_pos="top", dy=-32))
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 4, "Gliceraldehído-3-P", "3C", GLICERALDEHIDO_3_FOSFATO, "m_gap", text_pos="top", dy=-20))
    # Conexión TPI
    partes.append(f"""
    <g id="rx_tpi" data-arrastrable="1">
      <line x1="{x_g - 40}" y1="{y_g + paso_y * 4 + 40}" x2="{x_g + 160}" y2="{y_g + paso_y * 4 + 40}" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="{x_g + 160}" y1="{y_g + paso_y * 4 + 48}" x2="{x_g - 40}" y2="{y_g + paso_y * 4 + 48}" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <text x="{x_g + 60}" y="{y_g + paso_y * 4 + 28}" fill="#0f172a" font-size="11" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Triosa Fosfato Isomerasa</text>
    </g>
    """)

    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 4 + 115, 45, "GAPDH", entra="+ NAD⁺", sale="+ NADH + H⁺", es_ganancia=True, reversible=True, id_rx="rx_gapdh"))

    # 6. 1,3-BPG
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 5, "1,3-Bisfosfoglicerato", "3C", BISFOSFOGLICERATO_1_3, "m_bpg"))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 5 + 115, 45, "Fosfoglicerato Cinasa", entra="+ ADP", sale="+ ATP", es_ganancia=True, reversible=True, id_rx="rx_pgk"))

    # 7. 3-PG
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 6, "3-Fosfoglicerato", "3C", FOSFOGLICERATO_3, "m_3pg"))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 6 + 115, 45, "Fosfoglicerato Mutasa", reversible=True, id_rx="rx_pgm"))

    # 8. 2-PG
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 7, "2-Fosfoglicerato", "3C", FOSFOGLICERATO_2, "m_2pg"))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 7 + 105, 52, "Enolasa (-H₂O)", reversible=True, id_rx="rx_eno"))

    # 9. PEP
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 8, "Fosfoenolpiruvato", "3C", FOSFOENOLPIRUVATO, "m_pep", dx=115))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 8 + 105, 52, "Piruvato Cinasa", entra="+ ADP", sale="+ ATP", es_ganancia=True, id_rx="rx_pk"))
    partes.append(etiqueta_regulacion("pk", x_g + 325, y_g + paso_y * 8 + 115, dx=0, dy=0))

    # 10. Piruvato (Citosol)
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 9, "Piruvato", "3C", PIRUVATO, "m_pyr_cito"))

    # Flecha Piruvato Citosol ➔ MPC (entra directo al centro del transportador en x=1680)
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f"""
        <path d="M {x_g + 220} {y_g + paso_y * 9 + 100} Q {x_g + 120} {y_g + paso_y * 9 + 135}, 1680 {y_mito - 60}" fill="none" stroke="#ea580c" stroke-width="3" stroke-dasharray="10 6" marker-end="url(#arrowFlow)"/>
        """)
    partes.append('</g>')


    # =========================================================================
    # 3B. VÍA DE LA GLUCONEOGÉNESIS (VÍA ANABÓLICA HEPÁTICA) - VÍA 2
    # =========================================================================
    partes.append(f'''
    <!-- RUTA 2: GLUCONEOGÉNESIS (VÍA ANABÓLICA HEPÁTICA DE NOVO) -->
    <g id="ruta_gluconeogenesis" data-arrastrable="1">
      {badge_via(2, 785, 110)}
      <!-- Título y balance global de la vía -->
      <g id="titulo_gluconeogenesis" transform="translate(820, 105)">
        <text x="0" y="5" fill="#7c3aed" font-size="14" font-weight="900" font-family="'Inter', sans-serif">GLUCONEOGÉNESIS (VÍA ANABÓLICA HEPÁTICA)</text>
        <text x="0" y="18" fill="#64748b" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Síntesis de novo • 3 Rodeos (Bypasses) + 7 Pasos Reversibles</text>
        <text x="0" y="29" fill="#0284c7" font-size="8" font-weight="700" font-family="'Inter', sans-serif">Gasto neto: 4 ATP + 2 GTP + 2 NADH por Glucosa formada</text>
      </g>
    ''')

    # RODEO 3: Retículo Endoplásmico y Glucosa-6-Fosfatasa (G6Pasa) ➔ Sortea Hexocinasa
    partes.append(f'''
    <g id="rodeo3_g6pasa" data-arrastrable="1">
      {badge_rodeo_gng(3, 830, 155)}

      <!-- Ficha descriptiva de la G6Pasa -->
      <g transform="translate(880, 145)">
        <text x="0" y="0" fill="#6d28d9" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Glucosa-6-Fosfatasa (RE)</text>
        <text x="0" y="13" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">EC 3.1.3.9 (+ H₂O ➔ + Pi)</text>
        <text x="0" y="25" fill="#b45309" font-size="8" font-weight="800" font-family="'Inter', sans-serif">Sortea Hexocinasa • Lumen del RE</text>
        <text x="0" y="37" fill="#0284c7" font-size="8" font-weight="700" font-family="'Inter', sans-serif">Hepatocito y Corteza Renal</text>
      </g>

      <!-- Complejo del Retículo Endoplásmico con translocadores T1 y T2/T3 -->
      <g id="organelo_re_g6pasa" transform="translate(1120, 80) scale(0.65)">
        {RE_GLUCOSA_6_FOSFATASA}
      </g>

      <!-- Flujo 1: G-6-P citosólica entra por T1 al Lumen del RE (comienza fuera de m_g6p) -->
      <path d="M 1580 335 C 1520 335, 1460 305, 1406 292" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <text x="1490" y="300" fill="#7c3aed" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">G6P ➔ RE (T1)</text>

      <!-- Flujo 2 y 3: Salida de Glucosa libre desde T2/T3 hacia transportador GLUT-2 en membrana -->
      <g id="carrier_glut2_gng">
        <!-- Cápsula transportadora de GLUT-2 en la membrana plasmática (despejado en X=1480, Y=68) -->
        <rect x="1455" y="53" width="50" height="30" rx="6" fill="#7c3aed" stroke="#5b21b6" stroke-width="1.8"/>
        <text x="1480" y="72" fill="#ffffff" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-2</text>
        <!-- Flecha desde RE T2/T3 hacia GLUT-2 -->
        <path d="M 1404 100 Q 1440 85, 1475 75" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        <text x="1435" y="115" fill="#7c3aed" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Glucosa libre</text>
        <!-- Flecha hacia la sangre -->
        <line x1="1480" y1="53" x2="1480" y2="20" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
        <text x="1465" y="38" fill="#7c3aed" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Glucosa ➔ Sangre (Glucemia)</text>
      </g>

      <!-- Transportador MCT1 en la membrana plasmática del hepatocito (captación de lactato) -->
      <g id="carrier_mct1_gng">
        <rect x="1560" y="53" width="54" height="30" rx="6" fill="#be123c" stroke="#881337" stroke-width="1.8"/>
        <text x="1587" y="72" fill="#ffffff" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MCT1</text>
        <text x="1587" y="96" fill="#be123c" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">SLC16A1 (Lactato)</text>
      </g>
    </g>
    ''')

    # RODEO 2: Fructosa-1,6-Bisfosfatasa-1 (FBPasa-1) ➔ Sortea PFK-1
    partes.append(f'''
    <g id="rodeo2_fbpasa1" data-arrastrable="1">
      <!-- Flecha ascendente morada paralela a PFK-1 (desplazada a X=1550 para no tocar +1 ADP) -->
      <path d="M 1550 660 C 1515 635, 1515 555, 1550 530" fill="none" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      
      {badge_rodeo_gng(2, 1240, 605)}
      <!-- Ficha de enzima y regulación (despejada a X=1200) -->
      <g transform="translate(1200, 630)">
        <text x="0" y="0" fill="#6d28d9" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Fructosa-1,6-Bisfosfatasa-1 (FBPasa-1)</text>
        <text x="0" y="13" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">EC 3.1.3.11 (+ H₂O ➔ + Pi) • Sortea PFK-1</text>
        <text x="0" y="25" fill="#16a34a" font-size="8" font-weight="800" font-family="'Inter', sans-serif">⊕ Citrato (señal de carga energética)</text>
        <text x="0" y="37" fill="#dc2626" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">⊖ AMP, F-2,6-BP (inhibición recíproca)</text>
        <text x="0" y="49" fill="#0284c7" font-size="8" font-weight="700" font-family="'Inter', sans-serif">F6P ➔ PGI ⇄ ➔ G6P (Isomerización)</text>
      </g>
    </g>
    ''')

    # PRECURSOR 1: Glicerol desde lipólisis ➔ Glicerol-3-P ➔ DHAP (con estructuras completas)
    partes.append(nodo_libre(760, 860, "Glicerol", "3C", GLUCONEO_GLICEROL, "m_glicerol", text_pos="top", dx=40, dy=-40, detalle="Lipólisis (Adipocitos)"))
    partes.append(f'''
    <g id="rx_gng_glicerol_cinasa" data-arrastrable="1" transform="translate(860, 885)">
      <line x1="0" y1="20" x2="100" y2="20" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <g transform="translate(50, -4)">
        <text x="0" y="-10" fill="#7c3aed" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">[Fosforilación]</text>
        <text x="0" y="2" fill="#6d28d9" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Glicerol Cinasa (GK)</text>
        <text x="0" y="14" fill="#dc2626" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">- 1 ATP (Mg²⁺)</text>
      </g>
    </g>
    ''')

    # Nodo intermediario Glicerol-3-Fosfato (G3P) con estructura química completa
    partes.append(nodo_libre(1020, 860, "Glicerol-3-P", "3C", GLUCONEO_G3P, "m_g3p", text_pos="top", dx=40, dy=-40, detalle="Triosa fosfato precursora"))

    partes.append(f'''
    <g id="rx_gng_g3pdh" data-arrastrable="1" transform="translate(1150, 885)">
      <line x1="0" y1="20" x2="180" y2="20" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <g transform="translate(90, -4)">
        <text x="0" y="-10" fill="#7c3aed" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">[Deshidrogenación]</text>
        <text x="0" y="2" fill="#6d28d9" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">G3PDH Citosólica (➔ DHAP)</text>
        <text x="0" y="14" fill="#059669" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">+ NAD⁺ ➔ + NADH + H⁺</text>
      </g>
    </g>
    ''')

    # EJE REVERSIBLE: Indicador visual segmentado para no cruzar TPI ni Aldolasa
    partes.append(f'''
    <g id="gng_eje_reversible" data-arrastrable="1">
      <!-- Segmento 1: desde PEP (1520) hasta antes de TPI (915) -->
      <path d="M 1740 1520 L 1740 915" fill="none" stroke="#7c3aed" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowFlow)"/>
      <g transform="translate(1728, 1420)">
        <text x="0" y="0" fill="#6d28d9" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">⇡ Enolasa (+ H₂O)</text>
      </g>
      <g transform="translate(1728, 1260)">
        <text x="0" y="0" fill="#6d28d9" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">⇡ PGM (2-PG ➔ 3-PG)</text>
      </g>
      <g transform="translate(1728, 1100)">
        <text x="0" y="0" fill="#dc2626" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">⇡ PGK (- 1 ATP)</text>
      </g>
      <g transform="translate(1728, 940)">
        <text x="0" y="0" fill="#dc2626" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">⇡ GAPDH (- 1 NADH)</text>
      </g>

      <!-- Segmento 2: por encima de TPI (865) hasta antes de Aldolasa (835) -->
      <path d="M 1740 865 L 1740 835" fill="none" stroke="#7c3aed" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>

      <!-- Segmento 3: por encima de Aldolasa (785) hasta F-1,6-BP (725) -->
      <path d="M 1740 780 L 1740 725" fill="none" stroke="#7c3aed" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
      <g transform="translate(1728, 795)">
        <text x="0" y="0" fill="#6d28d9" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">⇡ Aldolasa (Condensación)</text>
      </g>
    </g>
    ''')

    # PRECURSOR 2: L-Lactato desde Ciclo de Cori ➔ Piruvato (con estructura química completa)
    partes.append(nodo_libre(1550, 1830, "L-Lactato", "3C", GLUCONEO_LACTATO, "m_lactato", text_pos="top", dx=45, dy=-42, detalle="[Precursor] Ciclo de Cori"))
    partes.append(f'''
    <g id="rx_gng_ldh" data-arrastrable="1">
      <!-- Flecha limpia hacia Piruvato citosólico en (1860, 1735) -->
      <path d="M 1635 1860 Q 1720 1810, 1815 1745" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <g transform="translate(1645, 1720)">
        <text x="0" y="0" fill="#6d28d9" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">LDH: Lactato ➔ Piruvato</text>
        <text x="0" y="11" fill="#059669" font-size="8" font-weight="800" font-family="'Inter', sans-serif">+ NAD⁺ ➔ + NADH + H⁺</text>
      </g>
    </g>
    ''')

    # PRECURSOR 3: L-Alanina desde músculo (Ciclo de Cahill / Glucosa-Alanina) ➔ Piruvato
    partes.append(nodo_libre(1380, 1940, "L-Alanina", "3C", AMINO_ALANINA, "m_alanina_cahill", text_pos="top", dx=45, dy=-40, detalle="[Precursor] Ciclo de Cahill"))
    partes.append(f'''
    <g id="rx_cahill_alt" data-arrastrable="1">
      <path d="M 1485 1960 C 1620 1980, 1750 1980, 1830 1765" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <g transform="translate(1480, 1990)">
        <text x="0" y="0" fill="#6d28d9" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">ALT (Alanina Aminotransferasa)</text>
        <text x="0" y="12" fill="#475569" font-size="8" font-family="'JetBrains Mono', monospace">EC 2.6.1.2 (PLP) • Alanina + α-KG ⇄ Piruvato + Glutamato</text>
        <text x="0" y="24" fill="#0284c7" font-size="8" font-weight="800">Ciclo Glucosa-Alanina (Músculo ➔ Hígado)</text>
      </g>
    </g>
    ''')

    # RODEO 1: Piruvato Carboxilasa (PC) y PEPCK con Lanzadera de Malato ➔ Sortea Piruvato Cinasa
    # A. En la Matriz Mitocondrial (Anaplerosis y Cataplerosis con el Ciclo de Krebs):
    partes.append(f'''
    <g id="rodeo1_matriz_pc" data-arrastrable="1">
      <!-- Desvío de Piruvato que entra por MPC hacia PC en la matriz superior -->
      <path d="M 1630 2145 L 1555 2145" fill="none" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
      {badge_rodeo_gng(1, 1480, 2105)}
      <!-- Ficha de la Piruvato Carboxilasa -->
      <g transform="translate(1480, 2145)">
        <rect x="-68" y="-13" width="136" height="26" rx="6" fill="#fdf4ff" stroke="#d946ef" stroke-width="1.2"/>
        <text x="0" y="2" fill="#86198f" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">PC (Piruvato Carboxilasa)</text>
        <text x="0" y="13" fill="#64748b" font-size="7.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">- 1 ATP, Biotina • ⊕ Acetil-CoA</text>
      </g>

      <!-- Conexión Anaplerótica directa de PC hacia Oxalacetato (m_oaa) del Ciclo de Krebs -->
      <path d="M 1445 2160 L 1445 2195 L 965 2195 L 965 2230" fill="none" stroke="#86198f" stroke-width="2.2" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
      <text x="1120" y="2184" fill="#86198f" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">⬅ Anaplerosis (PC): + HCO₃⁻ + ATP ➔ OAA (4C)</text>

      <!-- Conversión a Malato y salida por OGC (mMDH / Enzima Málica) -->
      <path d="M 1405 2145 L 1305 2145" fill="none" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      <g transform="translate(1355, 2163)">
        <text x="0" y="0" fill="#6d28d9" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">mMDH (OAA ➔ Malato)</text>
        <text x="0" y="10" fill="#0284c7" font-size="7.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">- 1 NADH matricial</text>
      </g>

      <!-- Retorno cataplerótico conectado desde Oxalacetato (Krebs) hacia OGC -->
      <path d="M 995 2230 L 995 2208 L 1275 2208 L 1275 2120" fill="none" stroke="#b45309" stroke-width="2.0" stroke-dasharray="5 3" marker-end="url(#arrowFlow)"/>
      <text x="1140" y="2222" fill="#b45309" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Cataplerosis OAA / Malato ➔ OGC ↑</text>
    </g>
    ''')

    # B. Transportador OGC en la Membrana Mitocondrial Interna:
    partes.append(f'''
    <g id="carrier_ogc_gng" data-arrastrable="1">
      <g transform="translate(1250, {y_mito - 55})">
        <rect x="0" y="0" width="50" height="30" rx="6" fill="#047857" stroke="#064e3b" stroke-width="1.8"/>
        <text x="25" y="19" fill="#ffffff" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">OGC</text>
      </g>
      <text x="1308" y="{y_mito - 36}" fill="#047857" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="start">Carrier Malato/α-KG</text>

      <!-- Flecha de salida de Malato cruzando la MMI hacia el citosol -->
      <path d="M 1275 {y_mito - 55} L 1275 1950 Q 1275 1860 1340 1800 L 1375 1785" fill="none" stroke="#047857" stroke-width="2.5" stroke-dasharray="6 3" marker-end="url(#arrowGreen)"/>
      <text x="1265" y="2000" fill="#047857" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Malato²⁻ sale al citosol ↑</text>
    </g>
    ''')

    # C. En el Citosol (cMDH y PEPCK-C con estructuras químicas completas):
    # 1. Nodo L-Malato Citosólico (con estructura completa)
    partes.append(nodo_libre(1380, 1715, "L-Malato (Citosol)", "4C", GLUCONEO_MALATO, "m_malato_gng_cito", text_right=True, dx=115, dy=22, detalle="Lanzadera Malato (OGC ↑)"))

    partes.append(f'''
    <g id="rodeo1_citosol_pepck" data-arrastrable="1">
      <!-- Reacción cMDH: L-Malato ➔ OAA citosólico -->
      <line x1="1430" y1="1710" x2="1430" y2="1655" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <g transform="translate(1445, 1680)">
        <text x="0" y="0" fill="#6d28d9" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif">cMDH (+ NAD⁺ ➔ + NADH + H⁺)</text>
        <text x="0" y="11" fill="#0284c7" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif">Regenera NADH citosólico</text>
      </g>
    ''')

    # 2. Nodo Oxalacetato Citosólico (con estructura completa)
    partes.append(nodo_libre(1380, 1530, "Oxalacetato (Citosol)", "4C", GLUCONEO_OXALACETATO, "m_oaa_gng_cito", text_pos="top", dx=45, dy=-25, detalle="Sustrato de PEPCK"))

    partes.append(f'''
      <!-- Reacción PEPCK: OAA ➔ PEP en (1860, 1560) -->
      <line x1="1470" y1="1560" x2="1815" y2="1560" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(1520, 1515)">
        <text x="0" y="0" fill="#6d28d9" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">RODEO 1: PEPCK Citosólica (PCK1)</text>
        <text x="0" y="12" fill="#64748b" font-size="8" font-family="'JetBrains Mono', monospace">EC 4.1.1.32 (- 1 GTP ➔ + GDP + CO₂) • Sortea PK</text>
        <text x="0" y="23" fill="#0284c7" font-size="8" font-weight="800" font-family="'Inter', sans-serif">[Hormonal] Glucagón / Cortisol ↑ (inducción génica)</text>
      </g>
    </g>
    ''')

    partes.append('</g>')

    # =========================================================================
    # 4. IZQUIERDA: METABOLISMO DEL GLUCÓGENO (LIBRE EN CITOSOL)
    # =========================================================================
    x_glc = 520
    y_glc = 340
    partes.append(f'<g id="ruta_glucogeno">')
    partes.append(badge_via(3, 440, 310))
    
    # G1P
    partes.append(nodo_libre(x_glc + 450, y_glc, "Glucosa-1-Fosfato", "6C", GLUCOSA_1_FOSFATO, "m_g1p", text_pos="top", dx=60, dy=-20))

    # Conexión G6P ⇄ G1P
    partes.append(f"""
    <g id="rx_pgm_glucogeno" data-arrastrable="1">
      <path d="M {x_g - 75} {y_g + paso_y + 35} L {x_glc + 600} {y_glc + 35}" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <text x="{(x_g - 75 + x_glc + 630)//2}" y="{y_glc + 20}" fill="#b45309" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Fosfoglucomutasa ⇄</text>
    </g>
    """)

    # UDP-Glucosa (nombre arriba, estructura centrada y flecha de pirofosforilasa arqueada por encima)
    y_udpg = y_glc - 70
    partes.append(nodo_libre(x_glc + 120, y_udpg, "UDP-Glucosa", "6C", UDP_GLUCOSA, "m_udpg", text_pos="top", dx=65, dy=-20))
    partes.append(f"""
    <g id="rx_udpg" data-arrastrable="1">
      <path d="M {x_glc + 450} {y_glc + 20} C {x_glc + 420} {y_glc + 20}, {x_glc + 395} {y_udpg + 35}, {x_glc + 380} {y_udpg + 35}" fill="none" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="{x_glc + 365}" y="{y_udpg - 55}" fill="#d97706" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">UDP-Glucosa Pirofosforilasa (+UTP)</text>
    </g>
    """)

    # Cadena de Glucógeno
    partes.append(nodo_libre(x_glc - 80, y_glc + 260, "Glucógeno (n+1)", "Polímero", CADENA_GLUCOGENO, "m_glucogeno_cadena", text_pos="top", dx=30, dy=-60))
    partes.append(f"""
    <g id="rx_sintesis_degradacion_glucogeno" data-arrastrable="1">
      <!-- Síntesis -->
      <path d="M {x_glc + 120} {y_udpg + 65} Q {x_glc + 45} {y_glc + 140} {x_glc + 45} {y_glc + 232}" fill="none" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="{x_glc + 140}" y="{y_glc + 145}" fill="#b45309" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">Glucógeno Sintasa</text>
      <g transform="translate({x_glc + 140}, {y_glc + 160})">
        <text x="0" y="0" fill="#16a34a" font-size="9" font-weight="800">(+) G6P</text>
        <text x="0" y="12" fill="#ca8a04" font-size="9" font-weight="800">(P) Inactiva (GSK-3/PKA)</text>
        <text x="0" y="24" fill="#0284c7" font-size="9" font-weight="800">[Hormonal] Insulina ↑ · Glucagón ↓</text>
      </g>

      <!-- Glucogenólisis (degradación) -->
      """ + (f"""<path d="M {x_glc + 80} {y_glc + 310} Q {x_glc + 320} {y_glc + 360} {x_glc + 500} {y_glc + 85}" fill="none" stroke="#ea580c" stroke-width="2.2" stroke-dasharray="7 5" marker-end="url(#arrowFlow)"/>""" if MOSTRAR_CONEXIONES_INTER_RUTA else "") + f"""
      <text x="{x_glc + 330}" y="{y_glc + 345}" fill="#c2410c" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">Glucógeno Fosforilasa (+Pi ➔ G1P)</text>
      <g transform="translate({x_glc + 330}, {y_glc + 360})">
        <text x="0" y="0" fill="#16a34a" font-size="9" font-weight="800">(+) AMP, Ca²⁺</text>
        <text x="0" y="12" fill="#dc2626" font-size="9" font-weight="800">(-) ATP, G6P, Glucosa</text>
        <text x="0" y="24" fill="#ca8a04" font-size="9" font-weight="800">(P) Activa (Fosforilasa quinasa)</text>
        <text x="0" y="36" fill="#0284c7" font-size="9" font-weight="800">[Hormonal] Glucagón/Adrenalina ↑</text>
      </g>
    </g>
    """)
    partes.append('</g>')

    # =========================================================================
    # 5. DERECHA: VÍA DE LAS PENTOSAS FOSFATO (LIBRE EN CITOSOL)
    # =========================================================================
    x_p_center = 2680
    x_p_left = 2520
    x_p_right = 2840
    partes.append(f'<g id="ruta_pentosas">')

    # Badges de la vía y fase oxidativa
    partes.append(badge_via(4, 2520, 144))
    partes.append(f'''
    <g transform="translate({x_p_center - 110}, 144)">
      <rect x="0" y="0" width="220" height="20" rx="10" fill="#d1fae5" stroke="#059669" stroke-width="1.5"/>
      <text x="110" y="14" fill="#047857" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">FASE OXIDATIVA (IRREVERSIBLE)</text>
    </g>
    ''')

    # Entrada G6PDH desde G6P citosólica con cofactores (NADP⁺ ➔ NADPH + H⁺)
    partes.append(f"""
    <g id="rx_g6pdh" data-arrastrable="1">
      <path d="M {x_g + 265} {y_g + paso_y + 35} Q 2200 170 {x_p_center - 35} 200" fill="none" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>
      <text x="2220" y="156" fill="#0f172a" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Glucosa-6-P Deshidrogenasa (G6PDH)</text>
      <!-- Curva entrada NADP⁺ -->
      <path d="M 2150 195 Q 2175 195 2190 230" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="2140" y="199" fill="#475569" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ NADP⁺</text>
      <!-- Curva salida NADPH + H⁺ -->
      <path d="M 2260 225 Q 2280 260 2310 260" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="2320" y="264" fill="#059669" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="start">+ NADPH + H⁺</text>
    </g>
    """)

    # 1. 6-P-Gluconolactona
    partes.append(etiqueta_regulacion("g6pdh", x_p_center - 110, 240, dx=0, dy=0, anchor="end"))
    partes.append(nodo_libre(x_p_center, 195, "6-P-Gluconolactona", "6C", FOSFOGLUCONO_LACTONA_6, "m_lactona", text_right=True, dx=115))
    partes.append(reaccion_libre(x_p_center + 45, 285, 36, "6-Fosfogluconolactonasa", entra="+ H₂O", id_rx="rx_lactonasa"))

    # 2. 6-Fosfogluconato
    partes.append(nodo_libre(x_p_center, 330, "6-Fosfogluconato", "6C", FOSFOGLUCONATO_6, "m_6pg", text_right=True, dx=115))
    partes.append(reaccion_libre(x_p_center + 45, 468, 38, "6-Fosfogluconato DH", entra="+ NADP⁺", sale="+ NADPH + CO₂", es_ganancia=True, id_rx="rx_6pgdh"))

    # 3. Ribulosa-5-P (Punto de confluencia y ramificación)
    partes.append(nodo_libre(x_p_center, 510, "Ribulosa-5-P", "5C", RIBULOSA_5_FOSFATO, "m_ru5p", text_right=True, dx=115))

    # Badge Rama Ribosa (Morada)
    partes.append(f'''
    <g transform="translate({x_p_right - 40}, 625)">
      <rect x="0" y="0" width="190" height="18" rx="9" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.4"/>
      <text x="95" y="13" fill="#6d28d9" font-size="8" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">PRECURSOR DE NUCLEÓTIDOS (PRPP)</text>
    </g>
    ''')

    # Ramas: Xilulosa-5P (izquierda) y Ribosa-5P (derecha)
    partes.append(f"""
    <path d="M {x_p_center - 20} 635 L {x_p_left + 45} 670" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="{x_p_left + 15}" y="650" fill="#047857" font-size="9" font-family="'Inter', sans-serif" text-anchor="middle">Epimerasa</text>

    <path d="M {x_p_center + 20} 635 L {x_p_right + 45} 670" stroke="#7c3aed" stroke-width="2.4" marker-end="url(#arrowPurple)"/>
    <text x="{x_p_right + 85}" y="650" fill="#6d28d9" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Isomerasa</text>
    """)

    # -------------------------------------------------------------------------
    # FASE NO OXIDATIVA: REORDENAMIENTO ESTEQUIOMÉTRICO (3 NIVELES DESPEJADOS)
    # -------------------------------------------------------------------------
    # Nivel 0: Xilulosa-5-P (izquierda) y Ribosa-5-P (derecha)
    partes.append(nodo_libre(x_p_left, 675, "Xilulosa-5-P", "5C", XILULOSA_5_FOSFATO, "m_xu5p", text_right=False, dx=-15, dy=25, detalle="[Regulador] ChREBP"))
    partes.append(nodo_libre(x_p_right, 675, "Ribosa-5-P", "5C", RIBOSA_5_FOSFATO, "m_r5p", text_right=True, dx=115, dy=25, detalle="Precursora PRPP / ADN"))

    # Paso 1: Transcetolasa 1 (TK1) con flechas de convergencia/divergencia de 2C
    partes.append(f"""
    <g id="rx_tk1_pnt" data-arrastrable="1" transform="translate({x_p_center - 60}, 740)">
      <path d="M -22 -2 L -4 12 M 22 -2 L 4 12 M -4 28 L -22 42 M 4 28 L 22 42" fill="none" stroke="#ea580c" stroke-width="1.6"/>
      <line x1="-3" y1="0" x2="-3" y2="40" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="40" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(24, 10)">
        <text x="0" y="0" fill="#0f172a" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">Transcetolasa 1 (TK1, 2C)</text>
        <text x="0" y="13" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">EC 2.2.1.1 (TPP) • +GAP [3C]</text>
        <text x="0" y="25" fill="#c2410c" font-size="8.5" font-weight="700">X5P + R5P ⇄ S7P + GAP</text>
      </g>
    </g>
    """)

    # Nivel 1: Sedoheptulosa-7-P (7C, izq) y Eritrosa-4-P (4C, der)
    partes.append(nodo_libre(x_p_left, 835, "Sedoheptulosa-7-P", "7C", SEDOHEPTULOSA_7_FOSFATO, "m_s7p", text_right=False, dx=-15, dy=25, detalle="Intermediario 7C (de TK1)"))
    partes.append(nodo_libre(x_p_right, 835, "Eritrosa-4-P", "4C", ERITROSA_4_FOSFATO, "m_e4p", text_right=True, dx=115, dy=25, detalle="De TA (S7P+GAP) • Precursor AA"))

    # Paso 2 y 3: Transaldolasa (TA) y Transcetolasa 2 (TK2) con flechas de convergencia/divergencia
    partes.append(f"""
    <g id="rx_ta_pnt" data-arrastrable="1" transform="translate({x_p_center - 60}, 900)">
      <path d="M -22 -2 L -4 12 M 22 -2 L 4 12 M -4 28 L -22 42 M 4 28 L 22 42" fill="none" stroke="#ea580c" stroke-width="1.6"/>
      <line x1="-3" y1="0" x2="-3" y2="40" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="40" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(24, 10)">
        <text x="0" y="0" fill="#0f172a" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">Transaldolasa (3C) + TK2 (2C)</text>
        <text x="0" y="13" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">EC 2.2.1.2 / EC 2.2.1.1 (TPP)</text>
        <text x="0" y="25" fill="#c2410c" font-size="8.5" font-weight="700">S7P+GAP+X5P ⇄ 2 F6P + GAP</text>
      </g>
    </g>
    """)

    # Nivel 2: Productos finales de reingreso al eje glucolítico
    partes.append(nodo_libre(x_p_left, 995, "Fructosa-6-P (x2)", "6C", PENTOSAS_F6P, "m_f6p_pnt", text_right=False, dx=-36, dy=25, detalle="➔ Glucólisis"))
    partes.append(nodo_libre(x_p_right, 995, "Gliceraldehído-3-P", "3C", PENTOSAS_GAP, "m_gap_pnt", text_right=False, dx=-15, dy=25, detalle="➔ Reingreso a Glucólisis"))

    partes.append('</g>')

    # =========================================================================
    # 6. LANZADERA MALATO-ASPARTATO: PANEL TÉCNICO REGULATORIO
    # =========================================================================
    cx_lupa = 1026
    cy_lupa = 1544
    r_lupa = 310
    x_ancla_mmi = 1026
    y_ancla_mmi = y_mito - 16

    partes.append(badge_via(8, 956, y_ancla_mmi - 25))
    partes.append(f"""
    <!-- ================================================================= -->
    <!-- PANEL TÉCNICO: LANZADERA MALATO-ASPARTATO                         -->
    <!-- ================================================================= -->
    <g id="lupa_lanzadera_malato_aspartato" data-arrastrable="1">

      <!-- 1. Punto de Anclaje sobre la Membrana Mitocondrial Real -->
      <g id="ancla_lanzadera_mmi" transform="translate({x_ancla_mmi}, {y_ancla_mmi})">
        <rect x="-55" y="-18" width="110" height="36" rx="8" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
        <text x="0" y="5" fill="#ffffff" font-size="13" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">OGC / AGC</text>
        <text x="0" y="34" fill="#78350f" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Lanzadera Malato-Aspartato</text>
      </g>

      <!-- 2. Cuerpo y Bisel del Panel Técnico -->
      <rect x="{cx_lupa - r_lupa}" y="{cy_lupa - r_lupa}" width="{r_lupa * 2}" height="{r_lupa * 2}" rx="18" fill="#ffffff" stroke="#0284c7" stroke-width="2.5"/>

      <!-- ClipPath para recortar el interior del panel -->
      <defs>
        <clipPath id="clipLupaLanzadera">
          <rect x="{cx_lupa - r_lupa}" y="{cy_lupa - r_lupa}" width="{r_lupa * 2}" height="{r_lupa * 2}" rx="18"/>
        </clipPath>
      </defs>

      <!-- 4. Contenido Interior con Ciclo Cerrado, 5 Estructuras y Flechas Punteadas -->
      <g clip-path="url(#clipLupaLanzadera)">
        <!-- Fondo CITOPLASMA (Mitad Superior en Verde Suave) -->
        <rect x="{cx_lupa - r_lupa - 10}" y="{cy_lupa - r_lupa - 10}" width="{r_lupa * 2 + 20}" height="{r_lupa + 10}" fill="#f0fdf4"/>

        <!-- Fondo MATRIZ MITOCONDRIAL (Mitad Inferior en Ámbar Suave) -->
        <rect x="{cx_lupa - r_lupa - 10}" y="{cy_lupa}" width="{r_lupa * 2 + 20}" height="{r_lupa + 10}" fill="#fffbeb"/>

        <!-- Bicapa MMI transversal divisoria en la lupa -->
        <rect x="{cx_lupa - r_lupa - 10}" y="{cy_lupa - 20}" width="{r_lupa * 2 + 20}" height="40" fill="#fed7aa" stroke="#d97706" stroke-width="2.5"/>
        <text x="{cx_lupa}" y="{cy_lupa + 4}" fill="#92400e" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MMI (BICAPA INTERNA)</text>

        <!-- Cabezas de fosfolípidos en MMI -->
        <g fill="#d97706" opacity="0.6">
          <circle cx="{cx_lupa - 290}" cy="{cy_lupa - 14}" r="2.6"/><circle cx="{cx_lupa - 275}" cy="{cy_lupa - 14}" r="2.6"/>
          <circle cx="{cx_lupa - 290}" cy="{cy_lupa + 14}" r="2.6"/><circle cx="{cx_lupa - 275}" cy="{cy_lupa + 14}" r="2.6"/>
          <circle cx="{cx_lupa + 275}" cy="{cy_lupa - 14}" r="2.6"/><circle cx="{cx_lupa + 290}" cy="{cy_lupa - 14}" r="2.6"/>
          <circle cx="{cx_lupa + 275}" cy="{cy_lupa + 14}" r="2.6"/><circle cx="{cx_lupa + 290}" cy="{cy_lupa + 14}" r="2.6"/>
        </g>

        <!-- Transportador Izquierdo: SLC25A12 (Aralar / AGC1) -->
        <g transform="translate({cx_lupa - 220}, {cy_lupa - 24})">
          <rect x="-38" y="0" width="76" height="48" rx="10" fill="#ec4899" stroke="#db2777" stroke-width="2"/>
          <text x="0" y="19" fill="#831843" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">Aralar</text>
          <text x="0" y="35" fill="#9d174d" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Asp⁻ ⇄ Glu⁻</text>
        </g>

        <!-- Transportador Derecho: SLC25A11 (OGC) -->
        <g transform="translate({cx_lupa + 220}, {cy_lupa - 24})">
          <rect x="-38" y="0" width="76" height="48" rx="10" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
          <text x="0" y="19" fill="#78350f" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">OGC</text>
          <text x="0" y="35" fill="#92400e" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Mal²⁻ ⇄ α-KG²⁻</text>
        </g>

        <!-- =========================================================== -->
        <!-- ZONA 1: CITOPLASMA (ARRIBA) - GOT1 Y cMDH                   -->
        <!-- =========================================================== -->
        <g transform="translate({cx_lupa}, {cy_lupa - 282})">
          <rect x="-220" y="-12" width="440" height="24" rx="12" fill="#f1f5f9" stroke="#0284c7" stroke-width="1.6"/>
          <text x="0" y="4" fill="#0369a1" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="0.8">
            CITOSOL: GOT1 / cAST (TRANSAMINACIÓN) &amp; cMDH (REDUCCIÓN)
          </text>
        </g>

        <!-- Estructura Citosólica 1 (Izquierda): L-Aspartato (Citosol) -->
        <g transform="translate({cx_lupa - 245}, {cy_lupa - 252})">
          <g transform="scale(0.60)">{LANZ_ASP}</g>
          <text x="24" y="86" fill="#831843" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Aspartato</text>
          <text x="24" y="98" fill="#db2777" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Citosol</text>
        </g>

        <!-- Reacción 1 (Izquierda ➔ Centro): GOT1 / cAST (Punteada) -->
        <g transform="translate({cx_lupa - 185}, {cy_lupa - 212})">
          <line x1="0" y1="0" x2="142" y2="0" stroke="#db2777" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowRed)"/>
          <text x="71" y="-10" fill="#be123c" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">GOT1 (cAST)</text>
          <text x="71" y="15" fill="#64748b" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">+ α-KG ➔ + L-Glu</text>
        </g>

        <!-- Estructura Citosólica 2 (Centro): Oxalacetato (Citosol) -->
        <g transform="translate({cx_lupa - 24}, {cy_lupa - 252})">
          <g transform="scale(0.60)">{LANZ_OAA}</g>
          <text x="24" y="86" fill="#0f172a" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Oxalacetato</text>
          <text x="24" y="98" fill="#ea580c" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Citosol</text>
        </g>

        <!-- Reacción 2 (Centro ➔ Derecha): cMDH (Punteada) -->
        <g transform="translate({cx_lupa + 38}, {cy_lupa - 212})">
          <line x1="0" y1="0" x2="146" y2="0" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
          <text x="73" y="-10" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">cMDH</text>
          <path d="M 12 10 Q 73 28 134 10" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
          <text x="73" y="34" fill="#dc2626" font-size="9" font-weight="800" text-anchor="middle">- NADH + H⁺ ➔ + NAD⁺</text>
          <text x="73" y="45" fill="#047857" font-size="8" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">(regenera NAD⁺ p/ Glucólisis)</text>
        </g>

        <!-- Estructura Citosólica 3 (Derecha): L-Malato (Citosol) -->
        <g transform="translate({cx_lupa + 196}, {cy_lupa - 252})">
          <g transform="scale(0.60)">{LANZ_MALATO}</g>
          <text x="24" y="86" fill="#0f172a" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Malato</text>
          <text x="24" y="98" fill="#0284c7" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Citosol</text>
        </g>

        <!-- =========================================================== -->
        <!-- SUB-CICLO CENTRAL DE ANTIPUERTO: L-GLUTAMATO Y α-KG         -->
        <!-- =========================================================== -->
        <!-- Estructura acoplada: L-Glutamato [5C] -->
        <g transform="translate({cx_lupa - 148}, {cy_lupa - 134})">
          <g transform="scale(0.48)">{LANZ_GLU}</g>
          <text x="48" y="28" fill="#9d174d" font-size="9" font-weight="800" font-family="'Inter', sans-serif">L-Glutamato</text>
          <text x="48" y="40" fill="#be185d" font-size="8" font-weight="700" font-family="'JetBrains Mono', monospace">[5C] (entra a matriz)</text>
        </g>
        <!-- Flecha punteada de L-Glutamato bajando hacia GOT2 (cruza MMI en hueco libre cx-115) -->
        <path d="M {cx_lupa - 115} {cy_lupa - 62} L {cx_lupa - 115} {cy_lupa + 84}" fill="none" stroke="#be185d" stroke-width="1.9" stroke-dasharray="5 3" marker-end="url(#arrowRed)"/>

        <!-- Estructura acoplada: α-Cetoglutarato [5C] -->
        <g transform="translate({cx_lupa + 32}, {cy_lupa - 134})">
          <g transform="scale(0.48)">{LANZ_AKG}</g>
          <text x="44" y="28" fill="#92400e" font-size="9" font-weight="800" font-family="'Inter', sans-serif">α-Cetoglutarato</text>
          <text x="44" y="40" fill="#d97706" font-size="8" font-weight="700" font-family="'JetBrains Mono', monospace">[5C] (sale a citosol)</text>
        </g>
        <!-- Flecha punteada de α-KG subiendo desde GOT2 hacia GOT1 (pasa en cy+42 sobre OAA y cruza MMI en cx+95) -->
        <path d="M {cx_lupa - 85} {cy_lupa + 84} L {cx_lupa - 85} {cy_lupa + 42} L {cx_lupa + 95} {cy_lupa + 42} L {cx_lupa + 95} {cy_lupa - 62}" fill="none" stroke="#d97706" stroke-width="1.9" stroke-dasharray="5 3" marker-end="url(#arrowFlow)"/>

        <!-- =========================================================== -->
        <!-- FLECHAS VERTICALES DE TRANSPORTE TRANSMEMBRANA (PUNTEADAS)  -->
        <!-- =========================================================== -->
        <!-- Derecha: L-Malato baja desde el citosol, entra a OGC y sale hacia la matriz -->
        <path d="M {cx_lupa + 220} {cy_lupa - 144} L {cx_lupa + 220} {cy_lupa - 28}" fill="none" stroke="#0284c7" stroke-width="2.8" stroke-dasharray="6 4" marker-end="url(#arrowBlue)"/>
        <path d="M {cx_lupa + 220} {cy_lupa + 26} L {cx_lupa + 220} {cy_lupa + 58}" fill="none" stroke="#0284c7" stroke-width="2.8" stroke-dasharray="6 4" marker-end="url(#arrowBlue)"/>
        <text x="{cx_lupa + 206}" y="{cy_lupa - 44}" fill="#0284c7" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Malato²⁻ ↓</text>

        <!-- Izquierda: L-Aspartato sube desde la matriz, entra a Aralar y retorna al citosol -->
        <path d="M {cx_lupa - 220} {cy_lupa + 58} L {cx_lupa - 220} {cy_lupa + 28}" fill="none" stroke="#db2777" stroke-width="2.8" stroke-dasharray="6 4" marker-end="url(#arrowRed)"/>
        <path d="M {cx_lupa - 220} {cy_lupa - 26} L {cx_lupa - 220} {cy_lupa - 144}" fill="none" stroke="#db2777" stroke-width="2.8" stroke-dasharray="6 4" marker-end="url(#arrowRed)"/>
        <text x="{cx_lupa - 206}" y="{cy_lupa - 44}" fill="#db2777" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="start">↑ Aspartato</text>

        <!-- =========================================================== -->
        <!-- ZONA 2: MATRIZ MITOCONDRIAL (ABAJO) - mMDH Y GOT2           -->
        <!-- =========================================================== -->
        <!-- Estructura Matricial 1 (Derecha): L-Malato (Matriz) -->
        <g transform="translate({cx_lupa + 196}, {cy_lupa + 66})">
          <g transform="scale(0.60)">{LANZ_MALATO}</g>
          <text x="24" y="86" fill="#0f172a" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Malato (Matriz)</text>
          <text x="24" y="98" fill="#0284c7" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Pool Krebs</text>
        </g>

        <!-- Reacción 3 (Derecha ➔ Centro): mMDH (Punteada hacia la izquierda) -->
        <g transform="translate({cx_lupa + 184}, {cy_lupa + 106})">
          <line x1="0" y1="0" x2="-146" y2="0" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
          <text x="-73" y="-10" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">mMDH</text>
          <path d="M -12 10 Q -73 28 -134 10" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
          <text x="-73" y="34" fill="#059669" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">+ NAD⁺ ➔ + NADH + H⁺</text>
          <text x="-73" y="46" fill="#047857" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">➔ Complejo I (2.5 ATP)</text>
        </g>

        <!-- Estructura Matricial 2 (Centro): Oxalacetato (Matriz) -->
        <g transform="translate({cx_lupa - 24}, {cy_lupa + 66})">
          <g transform="scale(0.60)">{LANZ_OAA}</g>
          <text x="24" y="86" fill="#0f172a" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Oxalacetato</text>
          <text x="24" y="98" fill="#ea580c" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Matriz</text>
        </g>

        <!-- Reacción 4 (Centro ➔ Izquierda): GOT2 / mAST (Punteada hacia la izquierda) -->
        <g transform="translate({cx_lupa - 43}, {cy_lupa + 106})">
          <line x1="0" y1="0" x2="-142" y2="0" stroke="#db2777" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowRed)"/>
          <text x="-71" y="-10" fill="#be123c" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">GOT2 (mAST)</text>
          <text x="-71" y="15" fill="#64748b" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">+ L-Glu ➔ + α-KG</text>
        </g>

        <!-- Estructura Matricial 3 (Izquierda): L-Aspartato (Matriz) -->
        <g transform="translate({cx_lupa - 245}, {cy_lupa + 66})">
          <g transform="scale(0.60)">{LANZ_ASP}</g>
          <text x="24" y="86" fill="#831843" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Aspartato</text>
          <text x="24" y="98" fill="#db2777" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Matriz</text>
        </g>

        <!-- Banner Explicativo Inferior -->
        <g transform="translate({cx_lupa}, {cy_lupa + 268})">
          <rect x="-215" y="-13" width="430" height="26" rx="13" fill="#0f172a" opacity="0.95"/>
          <text x="0" y="4" fill="#ffffff" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
            LANZADERA MALATO-ASPARTATO (CICLO CERRADO)
          </text>
        </g>
      </g>
    </g>
    """)

    # =========================================================================
    # 7. MATRIZ MITOCONDRIAL: PDH Y CICLO DE KREBS (ESPACIOSO Y NÍTIDO)
    # =========================================================================
    x_k = 1140
    y_k = y_mito + 80
    paso_k = 175  # Paso vertical holgado para que cada intermediario de Krebs respire plenamente

    partes.append(f'<g id="ruta_krebs">')
    partes.append(badge_via(5, 1695, 2185))
    partes.append(badge_via(6, x_k - 40, y_k + paso_k * 4 + 40))

    # 0. Piruvato (Matriz) recién ingresado por el transportador MPC (X=1680)
    partes.append(f"""
    <g id="m_pyr_mito" transform="translate(1632, 2132)">
      <rect x="0" y="0" width="116" height="28" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1.8"/>
      <text x="58" y="13" fill="#9a3412" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">Piruvato (Matriz)</text>
      <text x="58" y="24" fill="#c2410c" font-size="8" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">[3C] CH₃–CO–COO⁻</text>
    </g>

    <!-- Reacción única y clara del Complejo PDH: Piruvato (Matriz) ➔ Acetil-CoA -->
    <path d="M 1680 2162 L 1680 2253 Q 1680 2265 1668 2265 L 1490 2265" fill="none" stroke="#ea580c" stroke-width="3.0" marker-end="url(#arrowFlow)"/>
    <path d="M 1640 2235 Q 1620 2235 1610 2261" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
    <text x="1605" y="2229" fill="#475569" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">+ CoA-SH + NAD⁺</text>
    <path d="M 1625 2269 Q 1615 2292 1595 2292" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
    <text x="1580" y="2308" fill="#059669" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="start">+ CO₂ ↑ + NADH + H⁺</text>

    <!-- Flecha punteada guía visual hacia el panel de detalle PDH -->
    <path d="M 1530 2272 L 1530 3435" fill="none" stroke="#0284c7" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowBlue)"/>

    <g id="ancla_pdh_molecular" transform="translate({x_k + 580}, {y_k - 10})">
      <text x="0" y="5" fill="#c2410c" font-size="13" font-weight="900" font-family="'Inter', sans-serif">Complejo PDH (E1, E2, E3)</text>
      <text x="0" y="24" fill="#64748b" font-size="11" font-family="'Inter', sans-serif">Descarboxilación oxidativa (Piruvato ➔ Acetil-CoA)</text>
      <g transform="translate(0, 40)">
        <text x="0" y="0" fill="#16a34a" font-size="9" font-weight="800">(+) Piruvato, ADP, NAD⁺, Ca²⁺</text>
        <text x="0" y="12" fill="#dc2626" font-size="9" font-weight="800">(-) Acetil-CoA, NADH, ATP</text>
        <text x="0" y="24" fill="#ca8a04" font-size="9" font-weight="800">(P) Inactiva por PDK · Activa por PDP (Ca²⁺/Insulina)</text>
      </g>
    </g>
    """)

    # Acetil-CoA (2C, derecha del inicio del ciclo, título arriba para despejar la convergencia en Y)
    partes.append(nodo_libre(x_k + 220, y_k + 15, "Acetil-CoA", "2C", ACETIL_COA, "m_accoa", text_pos="top", dx=55, dy=-16))

    # Oxalacetato (4C, izquierda del inicio del ciclo)
    partes.append(nodo_libre(x_k - 240, y_k + 15, "Oxalacetato", "4C", KREBS_OXALACETATO, "m_oaa", text_right=False))
    partes.append(f"""
    <!-- Condensación en Y de Citrato Sintasa: Oxalacetato (4C) + Acetil-CoA (2C) ➔ Citrato (6C) -->
    <g id="rx_citrato_sintasa">
      <path d="M 1015 {y_k + 48} L {x_k + 35} {y_k + 48} Q {x_k + 55} {y_k + 48} {x_k + 55} {y_k + 68}" fill="none" stroke="#b45309" stroke-width="2.6"/>
      <path d="M 1348 {y_k + 48} L {x_k + 75} {y_k + 48} Q {x_k + 55} {y_k + 48} {x_k + 55} {y_k + 68}" fill="none" stroke="#ea580c" stroke-width="2.6"/>
      <path d="M {x_k + 55} {y_k + 60} L {x_k + 55} {y_k + 160}" fill="none" stroke="#b45309" stroke-width="3.0" marker-end="url(#arrowFlow)"/>
      <!-- Entrada de + H2O y salida de - CoA-SH -->
      <path d="M {x_k + 5} {y_k + 80} Q {x_k + 35} {y_k + 80} {x_k + 51} {y_k + 96}" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="{x_k}" y="{y_k + 84}" fill="#0284c7" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ H₂O</text>
      <path d="M {x_k + 51} {y_k + 118} Q {x_k + 35} {y_k + 134} {x_k + 5} {y_k + 134}" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="{x_k}" y="{y_k + 138}" fill="#dc2626" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">- CoA-SH</text>
      <!-- Nombre enzimático, mecanismo y regulación alostérica -->
      <text x="{x_k + 72}" y="{y_k + 85}" fill="#78350f" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">Citrato Sintasa</text>
      <text x="{x_k + 72}" y="{y_k + 98}" fill="#64748b" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace">Condensación: OAA (4C) + Ac-CoA (2C)</text>
      <text x="{x_k + 72}" y="{y_k + 111}" fill="#16a34a" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">⊕ ADP (carga energética baja)</text>
      <text x="{x_k + 72}" y="{y_k + 123}" fill="#dc2626" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">⊖ ATP, NADH, Succinil-CoA, Citrato</text>
    </g>
    """)

    # Citrato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k, "Citrato", "6C", CITRATO, "m_citrato", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k + 130, 38, "Aconitasa ⇄", reversible=True, id_rx="rx_acon", text_dx=-16, text_anchor="end"))

    # Isocitrato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 2, "Isocitrato", "6C", ISOCITRATO, "m_isocitrato", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 2 + 130, 38, "Isocitrato DH", entra="+ NAD⁺", sale="+ NADH + CO₂", es_ganancia=True, id_rx="rx_icdh", text_dx=-16, text_anchor="end"))
    partes.append(etiqueta_regulacion("icdh", x_k + 69, y_k + paso_k * 2 + 135, dx=0, dy=0, anchor="start"))

    # Alfa-Cetoglutarato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 3, "α-Cetoglutarato", "5C", KREBS_ALFA_CETOGLUTARATO, "m_akg", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 3 + 130, 38, "α-KG Deshidrogenasa", entra="+ CoA-SH + NAD⁺", sale="+ NADH + CO₂", es_ganancia=True, id_rx="rx_akgdh", text_dx=-16, text_anchor="end"))
    partes.append(etiqueta_regulacion("akgdh", x_k + 69, y_k + paso_k * 3 + 138, dx=0, dy=0, anchor="start"))

    # Succinil-CoA
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 4, "Succinil-CoA", "4C", SUCCINIL_COA, "m_succoa", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 4 + 130, 38, "Succinil-CoA Sintetasa", entra="+ GDP + Pi", sale="+ GTP (+CoA-SH)", es_ganancia=True, id_rx="rx_scas", text_dx=-16, text_anchor="end"))

    # Succinato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 5, "Succinato", "4C", SUCCINATO, "m_succinato", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 5 + 130, 38, "Succinato DH (Complejo II)", entra="+ FAD", sale="+ FADH₂", es_ganancia=True, id_rx="rx_sdh", text_dx=-16, text_anchor="end"))

    # Fumarato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 6, "Fumarato", "4C", FUMARATO, "m_fumarato", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 6 + 130, 38, "Fumarasa (+ H₂O)", reversible=True, id_rx="rx_fum", text_dx=-16, text_anchor="end"))

    # L-Malato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 7, "L-Malato", "4C", KREBS_MALATO, "m_malato", text_right=True, dx=140))

    # Cierre del Ciclo: Retorno completo de L-Malato hasta tocar Oxalacetato con sus cofactores
    partes.append(f"""
    <g id="rx_mdh_retorno" data-arrastrable="1">
      <path d="M {x_k} {y_k + paso_k * 7 + 60} C 945 {y_k + paso_k * 7 + 60}, 945 3300, 945 2750 L 945 2378" fill="none" stroke="#b45309" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M 905 2620 Q 930 2620 941 2595" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="900" y="2624" fill="#475569" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ NAD⁺</text>
      <path d="M 941 2545 Q 930 2520 905 2520" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="900" y="2524" fill="#059669" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">+ NADH + H⁺</text>
      <text x="968" y="2570" fill="#78350f" font-size="11" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 968 2570)" text-anchor="middle">
        Malato DH (mMDH: L-Malato ➔ Oxalacetato)
      </text>
    </g>
    """)
    partes.append('</g>')

    # =========================================================================
    # 7B. COMPLEJO PIRUVATO DESHIDROGENASA (PDH) - VÍA 5
    # =========================================================================
    # Marco panorámico rectangular con bisel cian (idéntico a la Lupa de la CTE)
    # Ubicado en la zona matricial media-inferior: X=1460, Y=3440, W=800, H=700
    x_pdh_marco = 1460
    y_pdh_marco = 3440
    w_pdh_marco = 800
    h_pdh_marco = 700

    partes.append(f"""
    <!-- ================================================================= -->
    <!-- PANEL DETALLADO: COMPLEJO PIRUVATO DESHIDROGENASA (PDH)           -->
    <!-- ================================================================= -->
    <g id="lupa_piruvato_deshidrogenasa" data-arrastrable="1">

      <!-- 2. Cuerpo y Bisel de la Lente Panorámica de Zoom (Estilo CTE) -->
      <rect x="{x_pdh_marco - 6}" y="{y_pdh_marco - 6}" width="{w_pdh_marco + 12}" height="{h_pdh_marco + 12}" rx="24" fill="#ffffff" stroke="#0284c7" stroke-width="5"/>
      <rect x="{x_pdh_marco}" y="{y_pdh_marco}" width="{w_pdh_marco}" height="{h_pdh_marco}" rx="20" fill="#ffffff" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8 4"/>

      <!-- ClipPath para recortar el interior panorámico -->
      <defs>
        <clipPath id="clipLupaPDH">
          <rect x="{x_pdh_marco}" y="{y_pdh_marco}" width="{w_pdh_marco}" height="{h_pdh_marco}" rx="20"/>
        </clipPath>
      </defs>

      <!-- 3. Contenido Interior con Aumento: Mecanismo + Regulación + Toxicología -->
      <g clip-path="url(#clipLupaPDH)">
        <!-- Fondo cálido de matriz ampliada -->
        <rect x="{x_pdh_marco}" y="{y_pdh_marco}" width="{w_pdh_marco}" height="{h_pdh_marco}" fill="#fffdf7"/>

        <g transform="translate({x_pdh_marco + 20}, {y_pdh_marco + 15})">
          <!-- Cabecera Interior de la Lupa -->
          <g transform="translate(0, 8)">
            <rect x="0" y="0" width="32" height="26" rx="6" fill="#ea580c"/>
            <text x="16" y="18" fill="#ffffff" font-size="14" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">5</text>
            <text x="42" y="17" fill="#0f172a" font-size="14.5" font-weight="900" font-family="'Inter', sans-serif">COMPLEJO PIRUVATO DESHIDROGENASA (PDH)</text>
            <text x="42" y="31" fill="#ea580c" font-size="9.5" font-weight="700" font-family="'Inter', sans-serif">Detalle en alta resolución de la reacción: Piruvato ➔ Acetil-CoA (Entrada MPC superior)</text>
          </g>

          <!-- Línea divisoria vertical entre mecanismo (izq) y regulación (der) -->
          <line x1="385" y1="50" x2="385" y2="665" stroke="#e2e8f0" stroke-width="1.5" stroke-dasharray="4 4"/>

          <!-- =========================================================== -->
          <!-- COLUMNA IZQUIERDA: MECANISMO CATALÍTICO PASO A PASO         -->
          <!-- =========================================================== -->
          <g transform="translate(0, 52)">
            <text x="0" y="10" fill="#c2410c" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">I. MECANISMO CATALÍTICO CON ESTRUCTURAS QUÍMICAS</text>

            <!-- 1. Piruvato (Sustrato 3C) -->
            <g transform="translate(55, 16)">
              <rect x="0" y="0" width="128" height="44" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1.4"/>
              <g transform="translate(8, 2) scale(0.40)">
                {PIRUVATO}
              </g>
              <text x="136" y="17" fill="#9a3412" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">1. Piruvato (3C)</text>
              <text x="136" y="30" fill="#64748b" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">α-Cetoácido alimentador</text>
            </g>

            <!-- PASO 1: E1 Piruvato Deshidrogenasa (TPP) -->
            <path d="M 118 62 L 118 98" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
            <path d="M 114 78 Q 82 86 58 86" fill="none" stroke="#dc2626" stroke-width="1.7" marker-end="url(#arrowRed)"/>
            <text x="53" y="90" fill="#dc2626" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">+ CO₂ ↑</text>
            <g transform="translate(130, 72)">
              <text x="0" y="0" fill="#0f172a" font-size="10" font-weight="900" font-family="'Inter', sans-serif">Paso 1 — E₁: Piruvato DH (TPP)</text>
              <text x="0" y="12" fill="#ea580c" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Descarboxilación: carbanión TPP ataca C=O</text>
            </g>

            <!-- 2. Hidroxietil-TPP (Intermediario E1) -->
            <g transform="translate(48, 100)">
              <rect x="0" y="0" width="142" height="44" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.3"/>
              <g transform="translate(6, 2) scale(0.42)">
                {PDH_HIDROXIETIL_TPP}
              </g>
              <text x="150" y="17" fill="#1e293b" font-size="10" font-weight="900" font-family="'Inter', sans-serif">2. Hidroxietil-TPP (E₁)</text>
              <text x="150" y="30" fill="#64748b" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Unidad 2C activa unida a B₁</text>
            </g>

            <!-- PASO 2A: E2 Dihidrolipoil Transacetilasa (Oxidación y transferencia al brazo lipoilo) -->
            <path d="M 118 146 L 118 182" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
            <path d="M 68 160 Q 94 160 114 168" fill="none" stroke="#d97706" stroke-width="1.7" marker-end="url(#arrowAmber)"/>
            <text x="64" y="164" fill="#b45309" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ Lipoamida</text>
            <g transform="translate(130, 158)">
              <text x="0" y="0" fill="#0f172a" font-size="10" font-weight="900" font-family="'Inter', sans-serif">Paso 2a — E₂: Oxidación (Brazo 14 Å)</text>
              <text x="0" y="12" fill="#64748b" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Abre puente S–S y forma tioéster de alta E</text>
            </g>

            <!-- 3. Acetil-Lipoamida (Intermediario E2) -->
            <g transform="translate(42, 184)">
              <rect x="0" y="0" width="154" height="44" rx="6" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.3"/>
              <g transform="translate(6, 2) scale(0.42)">
                {PDH_ACETIL_LIPOAMIDA}
              </g>
              <text x="162" y="17" fill="#92400e" font-size="10" font-weight="900" font-family="'Inter', sans-serif">3. Acetil-Lipoamida (E₂)</text>
              <text x="162" y="30" fill="#b45309" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Tioéster (~S–C=O) en Lys-E₂</text>
            </g>

            <!-- PASO 2B: E2 Transacetilación a CoA-SH -->
            <path d="M 118 230 L 118 268" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
            <path d="M 68 242 Q 94 242 114 250" fill="none" stroke="#7c3aed" stroke-width="1.7" marker-end="url(#arrowPurple)"/>
            <text x="64" y="246" fill="#7c3aed" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">+ CoA-SH</text>
            <path d="M 122 252 Q 152 260 178 260" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
            <text x="184" y="253" fill="#ea580c" font-size="10" font-weight="900" font-family="'Inter', sans-serif">➔ Acetil-CoA (2C)</text>
            <text x="184" y="264" fill="#0f172a" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">Paso 2b: Transesterificación</text>

            <!-- 4. Dihidrolipoamida reducida (-SH HS-) -->
            <g transform="translate(42, 270)">
              <rect x="0" y="0" width="154" height="44" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.3"/>
              <g transform="translate(6, 2) scale(0.42)">
                {PDH_DIHIDROLIPOAMIDA}
              </g>
              <text x="162" y="17" fill="#991b1b" font-size="10" font-weight="900" font-family="'Inter', sans-serif">4. Dihidrolipoamida (E₂)</text>
              <text x="162" y="30" fill="#b91c1c" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Ditiol reducido (–SH HS–)</text>
            </g>

            <!-- PASO 3: E3 Dihidrolipoil Deshidrogenasa (FAD -> NAD+) -->
            <path d="M 118 316 L 118 354" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
            <path d="M 68 328 Q 94 328 114 336" fill="none" stroke="#475569" stroke-width="1.7" marker-end="url(#arrowSlate)"/>
            <text x="64" y="332" fill="#475569" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ NAD⁺</text>
            <path d="M 122 338 Q 152 346 178 346" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
            <text x="184" y="336" fill="#0f172a" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">Paso 3 — E₃: Dihidrolipoil DH</text>
            <text x="184" y="349" fill="#059669" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">+ NADH + H⁺ <tspan fill="#64748b" font-size="8.5">(vía FAD ➔ FADH₂)</tspan></text>

            <!-- 5. Lipoamida Oxidada regenerada (S-S) -->
            <g transform="translate(42, 356)">
              <rect x="0" y="0" width="154" height="44" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.3"/>
              <g transform="translate(6, 2) scale(0.42)">
                {PDH_LIPOAMIDA_OXIDADA}
              </g>
              <text x="162" y="17" fill="#15803d" font-size="10" font-weight="900" font-family="'Inter', sans-serif">5. Lipoamida Oxidada (S–S)</text>
              <text x="162" y="30" fill="#166534" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Puente disulfuro regenerado ↺</text>
            </g>

            <!-- Retorno cíclico punteado de la Lipoamida Oxidada hacia el Paso 2a (por el margen izquierdo seguro X=12) -->
            <path d="M 42 378 L 14 378 Q 6 378 6 370 L 6 154 Q 6 146 14 146 L 62 146" fill="none" stroke="#d97706" stroke-width="1.9" stroke-dasharray="5 3" marker-end="url(#arrowAmber)"/>
            <text x="18" y="285" fill="#b45309" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 18 285)" text-anchor="middle">↺ RETORNO CÍCLICO LIPOAMIDA (E₃ ➔ E₂)</text>

            <!-- Barra inferior de Balance Estequiométrico Global y 5 Cofactores -->
            <rect x="4" y="408" width="372" height="36" rx="6" fill="#fff7ed" stroke="#fdba74" stroke-width="1.2"/>
            <text x="190" y="422" fill="#9a3412" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">ESTEQUIOMETRÍA: Piruvato + CoA-SH + NAD⁺ ➔ Acetil-CoA + CO₂ + NADH + H⁺</text>
            <text x="190" y="436" fill="#c2410c" font-size="8.2" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">5 Cofactores: TPP (B₁) • Lipoamida • CoA-SH (B₅) • FAD (B₂) • NAD⁺ (B₃)</text>
          </g>

          <!-- =========================================================== -->
          <!-- COLUMNA DERECHA: REGULACIÓN DINÁMICA Y DIANAS TOXICOLÓGICAS  -->
          <!-- =========================================================== -->
          <g transform="translate(405, 52)">
            <text x="0" y="12" fill="#0f172a" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">II. CONTROL COVALENTE Y ALOSTÉRICO</text>

            <!-- Circuito PDK / PDP -->
            <g transform="translate(0, 30)">
              <!-- Estimuladores de PDK -->
              <g transform="translate(180, -10)">
                <text x="0" y="0" fill="#dc2626" font-size="10" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">(+) Estimulan PDK (Inactivan):</text>
                <text x="0" y="13" fill="#7f1d1d" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">NADH, Acetil-CoA, ATP</text>
                <path d="M 0 15 L 0 26" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
              </g>

              <!-- Nodo E1 Activa -->
              <g transform="translate(10, 60)">
                <ellipse cx="55" cy="0" rx="55" ry="20" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
                <text x="55" y="-2" fill="#15803d" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">E1 ACTIVA</text>
                <text x="55" y="10" fill="#166534" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Ser-OH (Desfosforilada)</text>
              </g>

              <!-- Flecha PDK Inactivadora arqueada bien por encima -->
              <path d="M 125 44 C 155 12, 205 12, 235 44" fill="none" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
              <g transform="translate(180, 40)">
                <text x="0" y="0" fill="#dc2626" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">PDK (+ATP)</text>
              </g>

              <!-- Nodo E1 Inactiva -->
              <g transform="translate(245, 60)">
                <ellipse cx="58" cy="0" rx="58" ry="20" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
                <text x="58" y="-2" fill="#991b1b" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">E1 INACTIVA</text>
                <text x="58" y="10" fill="#7f1d1d" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">(P) Ser-O-P (Fosforilada)</text>
              </g>

              <!-- Flecha PDP Activadora arqueada bien por debajo -->
              <path d="M 235 76 C 205 116, 155 116, 125 76" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
              <g transform="translate(180, 94)">
                <text x="0" y="0" fill="#16a34a" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">PDP (+H₂O)</text>
              </g>

              <!-- Estimuladores de PDP -->
              <g transform="translate(180, 128)">
                <path d="M 0 0 L 0 -10" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
                <text x="0" y="14" fill="#16a34a" font-size="10" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">(+) Estimulan PDP (Activan):</text>
                <text x="0" y="27" fill="#14532d" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Ca²⁺ (músculo) • Insulina (hígado)</text>
              </g>

              <!-- Inhibidores de PDK -->
              <g transform="translate(10, 128)">
                <text x="0" y="0" fill="#15803d" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">⊣ Inhiben PDK:</text>
                <text x="0" y="13" fill="#334155" font-size="8.5" font-family="'Inter', sans-serif">Piruvato, ADP, NAD⁺</text>
              </g>
            </g>

            <!-- Retroinhibición directa por producto -->
            <g transform="translate(0, 195)">
              <line x1="0" y1="0" x2="360" y2="0" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="3 3"/>
              <text x="0" y="18" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">RETROINHIBICIÓN DIRECTA POR PRODUCTO</text>
              
              <g transform="translate(0, 34)">
                <path d="M 5 6 L 45 6" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#inhibitionT)"/>
                <text x="52" y="10" fill="#dc2626" font-size="10" font-weight="900" font-family="'Inter', sans-serif">⊣ E2:</text>
                <text x="85" y="10" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif">Inhibida por <tspan font-weight="800" fill="#b91c1c">Acetil-CoA</tspan> (competitivo)</text>
              </g>

              <g transform="translate(0, 56)">
                <path d="M 5 6 L 45 6" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#inhibitionT)"/>
                <text x="52" y="10" fill="#dc2626" font-size="10" font-weight="900" font-family="'Inter', sans-serif">⊣ E3:</text>
                <text x="85" y="10" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif">Inhibida por cociente elevado <tspan font-weight="800" fill="#b91c1c">NADH/NAD⁺</tspan></text>
              </g>
            </g>

            <!-- =========================================================== -->
            <!-- CORRELACIÓN CLÍNICA Y FARMACOLÓGICA DIRECTA                  -->
            <!-- =========================================================== -->
            <g transform="translate(0, 290)">
              <line x1="0" y1="0" x2="360" y2="0" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="3 3"/>
              <text x="0" y="18" fill="#be123c" font-size="11" font-weight="900" font-family="'Inter', sans-serif">III. CORRELACIÓN CLÍNICA Y TOXICOLOGÍA</text>

              <!-- Diana 1: E1 / TPP -->
              <g transform="translate(0, 34)">
                <rect x="0" y="0" width="355" height="58" rx="6" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.2"/>
                <g transform="translate(10, 15)">
                  <text x="0" y="0" fill="#be123c" font-size="10" font-weight="900" font-family="'Inter', sans-serif">DIANA E1: DÉFICIT DE TIAMINA (B₁) &amp; ACIDOSIS LÁCTICA</text>
                  <text x="0" y="13" fill="#334155" font-size="8.5" font-family="'Inter', sans-serif">• Carencia B₁ ➔ Agota TPP ➔ <tspan font-weight="700">Beriberi</tspan> y <tspan font-weight="700">Wernicke-Korsakoff</tspan></text>
                  <text x="0" y="25" fill="#be123c" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">• Piruvato acumulado se reduce a Lactato por la LDH</text>
                </g>
              </g>

              <!-- Diana 2: E2 / Arsenito -->
              <g transform="translate(0, 102)">
                <rect x="0" y="0" width="355" height="58" rx="6" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.2"/>
                <g transform="translate(10, 15)">
                  <text x="0" y="0" fill="#be123c" font-size="10" font-weight="900" font-family="'Inter', sans-serif">DIANA E2: ENVENENAMIENTO POR ARSENITO (AsO₂⁻)</text>
                  <text x="0" y="13" fill="#334155" font-size="8.5" font-family="'Inter', sans-serif">• Quelato cíclico irreversible con tioles (-SH) de lipoamida</text>
                  <text x="0" y="25" fill="#15803d" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">• Antídoto de rescate: BAL (Dimercaprol ditiol)</text>
                </g>
              </g>
            </g>
          </g>
        </g>
      </g>
    </g>
    """)

    # =========================================================================
    # 8. MATRIZ DERECHA: CADENA RESPIRATORIA REAL DEL USUARIO (CON ZOOM)
    # =========================================================================
    cte_defs, cte_body = cargar_cte_original_usuario()

    x_ancla_cresta = 2633
    y_ancla_cresta = y_mito + 25

    x_cte_marco = 2553
    y_cte_marco = 2440
    w_cte_marco = 1190
    h_cte_marco = 820

    partes.append(badge_via(7, x_ancla_cresta - 95, y_ancla_cresta - 5))
    partes.append(f"""
    <!-- ================================================================= -->
    <!-- CADENA DE TRANSPORTE DE ELECTRONES Y ATP SINTASA                  -->
    <!-- ================================================================= -->
    <g id="lupa_cadena_respiratoria" data-arrastrable="1">

      <!-- 1. Punto de Anclaje sobre la Cresta Mitocondrial Real -->
      <g id="ancla_cresta_mmi" transform="translate({x_ancla_cresta}, {y_ancla_cresta})">
        <rect x="-65" y="-18" width="130" height="36" rx="10" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
        <text x="0" y="5" fill="#ffffff" font-size="12.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CRESTA MMI</text>
        <text x="0" y="34" fill="#78350f" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Cresta Respiratoria: Complejos I–IV &amp; F₀F₁</text>
      </g>

      <!-- 4. Cuerpo y Bisel de la Lente Panorámica de Zoom -->
      <rect x="{x_cte_marco - 6}" y="{y_cte_marco - 6}" width="{w_cte_marco + 12}" height="{h_cte_marco + 12}" rx="28" fill="#ffffff" stroke="#0284c7" stroke-width="6"/>
      <rect x="{x_cte_marco}" y="{y_cte_marco}" width="{w_cte_marco}" height="{h_cte_marco}" rx="24" fill="none" stroke="#38bdf8" stroke-width="2.2" stroke-dasharray="8 4"/>

      <!-- ClipPath para recortar el interior panorámico -->
      <defs>
        <clipPath id="clipLupaCTE">
          <rect x="{x_cte_marco}" y="{y_cte_marco}" width="{w_cte_marco}" height="{h_cte_marco}" rx="24"/>
        </clipPath>
      </defs>

      <!-- 5. Contenido Real Exacto del archivo del usuario: Cadena_Transporte_Electrones.svg -->
      <g clip-path="url(#clipLupaCTE)">
        <g transform="translate({x_cte_marco + 20}, {y_cte_marco + 10})">
          {cte_body}

          <!-- Figuritas moleculares vectoriales añadidas sobre el diseño del usuario con espaciado óptimo -->
          <!-- 1. Estructura real de NADH entrando a Complejo I -->
          <g transform="translate(75, 690) scale(0.48)">
            {CTE_NADH}
          </g>

          <!-- 2. Estructura real de FADH2 entrando a Complejo II -->
          <g transform="translate(275, 690) scale(0.48)">
            {CTE_FADH2}
          </g>

          <!-- 3. Estructura real de Ubiquinona debajo de los títulos de MMI/Matriz (sin amontonar) -->
          <g transform="translate(375, 520) scale(0.46)">
            {UBIQUINONA}
          </g>

          <!-- 4. Estructura real de Citocromo c en el EIM (zona libre superior) -->
          <g transform="translate(605, 175) scale(0.44)">
            {CITOCROMO_C}
          </g>

          <!-- 5. Estructuras de Oxígeno y Agua en Complejo IV -->
          <g transform="translate(660, 560) scale(0.48)">
            {OXIGENO}
          </g>
          <g transform="translate(740, 560) scale(0.48)">
            {AGUA}
          </g>
        </g>

        <!-- Badge Identificador Inferior -->
        <rect x="{x_cte_marco + w_cte_marco//2 - 350}" y="{y_cte_marco + h_cte_marco - 34}" width="700" height="28" rx="14" fill="#0f172a" opacity="0.95"/>
        <text x="{x_cte_marco + w_cte_marco//2}" y="{y_cte_marco + h_cte_marco - 16}" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
          CADENA DE TRANSPORTE DE ELECTRONES Y ATP SINTASA
        </text>
      </g>
    </g>
    """)

    # =========================================================================
    # 9. LÍPIDOS: LIPOGÉNESIS (CITOSOL)
    # =========================================================================
    x_lipo = 3080
    y_lipo = 1000
    paso_l = 175
    paso_fas = 152
    partes.append(f'<g id="ruta_lipogenesis">')
    partes.append(badge_via(10, x_lipo - 30, y_lipo - paso_l*2 - 20))

    partes.append(nodo_libre(x_lipo, y_lipo - paso_l*2 - 60, "Citrato (Citosólico)", "6C", CITRATO, "m_citrato_cito", text_right=True, dx=220))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo - paso_l*2 + 65, 52, "ATP Citrato Liasa", entra="+ ATP + CoA-SH", sale="+ OAA", id_rx="rx_acly"))
    partes.append(f'''
    <g id="retorno_malico_lanzadera_citrato" transform="translate({x_lipo + 74}, {y_lipo - paso_l*2 + 104})">
      <text x="0" y="0" fill="#047857" font-size="8" font-weight="800" font-family="'Inter', sans-serif">↳ OAA ➔ Malato (MDH1)</text>
      <text x="0" y="10" fill="#059669" font-size="8" font-weight="800" font-family="'Inter', sans-serif">➔ Piruvato + NADPH (ME1)</text>
    </g>
    ''')
    partes.append(etiqueta_regulacion("acly", x_lipo + 255, y_lipo - paso_l*2 + 52, dx=0, dy=0))
    
    partes.append(nodo_libre(x_lipo, y_lipo - paso_l, "Acetil-CoA (Citosólico)", "2C", ACETIL_COA, "m_acetil_coa_cito", text_pos="top", dx=60, dy=-22))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo - paso_l + 75, 48, "ACC (Acetil-CoA Carboxilasa)", entra="+ ATP + HCO₃⁻", sale="+ ADP + Pi", id_rx="rx_acc"))
    partes.append(etiqueta_regulacion("acc", x_lipo + 260, y_lipo - paso_l + 85, dx=0, dy=0))
    
    partes.append(f'''
    <!-- Transportador CIC en MMI (Lanzadera de Citrato) -->
    <g id="transportador_cic" data-arrastrable="1" transform="translate(1915, 2115)">
      <rect x="0" y="0" width="60" height="28" rx="7" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <text x="30" y="18" fill="#ffffff" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CIC</text>
    </g>
    ''')

    partes.append(nodo_libre(x_lipo, y_lipo, "Malonil-CoA", "3C", MALONIL_COA, "m_malonil", text_right=True, dx=185))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + 68, 42, "FAS: Condensación (KS)", entra="+ Acetil-ACP", sale="- CO₂", id_rx="rx_fas1"))
    partes.append(etiqueta_regulacion("fas", x_lipo + 245, y_lipo + 74, dx=0, dy=0))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_fas, "Acetoacetil-ACP", "4C", ACETOACETIL_ACP, "m_acetoac_acp", text_right=True, dx=190))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_fas + 68, 42, "FAS: 1ª Reducción (KR)", entra="+ NADPH", sale="+ NADP⁺", id_rx="rx_fas2"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_fas*2, "D-β-Hidroxiacil-ACP", "4C", D_BETA_HIDROXIACIL_ACP, "m_hidroxi_acp", text_right=True, dx=190))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_fas*2 + 68, 42, "FAS: Deshidratación (DH)", entra="", sale="- H₂O", id_rx="rx_fas3"))

    partes.append(nodo_libre(x_lipo, y_lipo + paso_fas*3, "trans-Δ²-Enoil-ACP", "4C", TRANS_DELTA2_ENOIL_ACP, "m_enoil_acp", text_right=True, dx=190, detalle="Crotonil-ACP (α,β-insaturado)"))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_fas*3 + 68, 42, "FAS: 2ª Reducción (ER)", entra="+ NADPH", sale="+ NADP⁺", id_rx="rx_fas3b"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_fas*4, "Butiril-ACP", "4C", BUTIRIL_ACP, "m_butiril_acp", text_right=True, dx=190, detalle="Acilo saturado (1ᵉʳ ciclo)"))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_fas*4 + 68, 42, "FAS (x6 Ciclos + Tioesterasa)", entra="+ 6 Malonil", sale="+ H₂O (-ACP)", id_rx="rx_fas4"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_fas*5, "Palmitato", "16C", PALMITATO_LIBRE, "m_palmitato_libre", text_right=True, dx=255))
    partes.append(f'</g>')

    # =========================================================================
    # 9B. LÍPIDOS: SÍNTESIS DE COLESTEROL (CITOSOL Y MEMBRANA DEL REL)
    # =========================================================================
    # Se ramifica directamente desde el pool citosólico de Acetil-CoA
    x_col = 3560
    y_col = 920
    paso_col = 165
    partes.append(f'<g id="ruta_colesterol">')
    partes.append(badge_via(12, x_col - 40, y_col - 260))

    # Inserción de Acetoacetil-CoA y HMG-CoA citosólicos + HMG-CoA Reductasa
    # Espaciado holgado: Acetoacetil-CoA (Y=520), HMG-CoA (Y=680), Mevalonato (Y=860)
    y_acetoac_col = 520
    y_hmg_col = 680
    y_mev = 890
    
    # Conexión fluida desde Acetil-CoA citosólico (X=3080, Y=825) hacia Acetoacetil-CoA citosólico (X=3560, Y=520)
    # Bordeando suavemente hacia arriba para no atravesar ningún texto
    partes.append(f'''
    <path d="M 3245 855 L 3290 855 Q 3300 855 3300 845 L 3300 470 Q 3300 460 3310 460 L 3495 460 Q 3505 460 3505 470 L 3505 525 Q 3505 535 3515 535 L 3550 535" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <text x="3400" y="450" fill="#9a3412" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">➔ Vía del Mevalonato (2 Acetil-CoA)</text>
    ''')

    partes.append(nodo_libre(x_col, y_acetoac_col, "Acetoacetil-CoA (Citosol)", "4C", ACETOACETIL_COA_COLEST, "m_acetoac_col", text_pos="top", dx=70, dy=-22))
    partes.append(reaccion_libre(x_col + 60, y_acetoac_col + 65, 45, "HMG-CoA Sintasa (Citosólica)", entra="+ Acetil-CoA", sale="- CoA-SH", id_rx="rx_hmgs_cito"))

    partes.append(nodo_libre(x_col, y_hmg_col, "HMG-CoA (Citosol)", "6C", HMG_COA_CITOSOL, "m_hmg_col", text_pos="top", dx=70, dy=-22))
    partes.append(reaccion_libre(x_col + 60, y_hmg_col + 65, 48, "HMG-CoA Reductasa (HMGCR)", entra="- 2 NADPH", sale="+ CoA-SH", id_rx="rx_hmgcr"))
    partes.append(etiqueta_regulacion("hmgcr", x_col + 250, y_hmg_col + 70, dx=0, dy=0))

    # Mevalonato (producto irreversible del marcapasos HMGCR)
    partes.append(nodo_libre(x_col, y_mev, "Mevalonato", "6C", MEVALONATO, "m_mevalonato_integ", text_pos="top", dx=70, dy=-22))
    partes.append(reaccion_libre(x_col + 60, y_mev + 75, 45, "Mevalonato Quinasa / Descarboxilasa", entra="- 3 ATP", sale="+ CO2 + Pi", id_rx="rx_col1"))
    
    # Isopentenil Pirofosfato (IPP)
    partes.append(nodo_libre(x_col, y_mev + paso_col, "Isopentenil-PP (IPP)", "5C", ISOPENTENIL_PP, "m_ipp_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_mev + paso_col + 75, 45, "Preniltransferasas", entra="+ 2 IPP", sale="+ 2 PPi", id_rx="rx_col2"))
    
    # Farnesil Pirofosfato (FPP)
    partes.append(nodo_libre(x_col, y_mev + paso_col*2, "Farnesil-PP (FPP)", "15C", FARNESIL_PP, "m_fpp_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_mev + paso_col*2 + 75, 45, "Escualeno Sintasa", entra="- NADPH", sale="+ 2 PPi", es_ganancia=False, id_rx="rx_col3"))
    
    # Escualeno
    partes.append(nodo_libre(x_col, y_mev + paso_col*3, "Escualeno", "30C", ESCUALENO, "m_escualeno_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_mev + paso_col*3 + 75, 45, "Oxidoscualeno Ciclasa", entra="- NADPH + O2", sale="+ H2O", id_rx="rx_col4"))
    
    # Lanosterol
    partes.append(nodo_libre(x_col, y_mev + paso_col*4, "Lanosterol", "30C", LANOSTEROL, "m_lanosterol_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_mev + paso_col*4 + 75, 45, "Vías de Bloch &amp; Kandutsch (19 pasos)", entra="- NADPH + O2", sale="+ 3 CO2", id_rx="rx_col5"))
    
    # Colesterol Final
    partes.append(nodo_libre(x_col, y_mev + paso_col*5, "COLESTEROL", "27C", COLESTEROL, "m_colesterol_integ", text_pos="top", dy=-18))
    
    # Conexiones funcionales de destino del Colesterol
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <path d="M {x_col + 240} {y_mev + paso_col*5 + 35} Q 3860 {y_mev + paso_col*5 + 35}, 3860 74" fill="none" stroke="#0284c7" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowBlue)"/>
        <text x="3875" y="500" fill="#0369a1" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 3875 500)">➔ DESTINO A MEMBRANA PLASMÁTICA (BALSAS LIPÍDICAS)</text>
        ''')
    partes.append(f'</g>')

    # =========================================================================
    # 10. LÍPIDOS: BETA-OXIDACIÓN (MATRIZ MITOCONDRIAL)
    # =========================================================================
    x_box = 180
    y_box = y_mito + 100
    paso_b = 160
    partes.append(f'<g id="ruta_beta_ox">')
    partes.append(badge_via(9, x_box - 20, y_box - 1220))
    

    # Sangre -> Citosol -> Mitocondria
    # Palmitato en sangre (unido a Albúmina dentro del torrente vascular superior)
    x_palm_sangre = 510
    partes.append(nodo_libre(x_palm_sangre, 24, "Palmitato (Sanguíneo / Albúmina)", "16C", PALMITATO_LIBRE, "m_palmitato_sangre", text_right=True, dx=265))
    
    # Cruce de la membrana plasmática hacia citosol por transportador CD36 / FAT
    partes.append(f'''
    <path d="M 500 98 L {x_box + 20} {y_box - 1220}" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <g transform="translate(460, 68)">
      <rect x="0" y="0" width="80" height="26" rx="6" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <text x="40" y="17" fill="#ffffff" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CD36/FAT</text>
    </g>
    <text x="550" y="110" fill="#0284c7" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">Captación celular ➔</text>
    ''')
    
    # 1. Palmitato Citosólico
    partes.append(nodo_libre(x_box, y_box - 1200, "Palmitato (Citosólico)", "16C", PALMITATO_LIBRE, "m_palmitato_cito", text_right=True, dx=265))
    partes.append(reaccion_libre(x_box + 60, y_box - 1200 + 80, 50, "Acil-CoA Sintetasa (ACS)", entra="+ ATP + CoA-SH", sale="+ AMP + PPi", id_rx="rx_acs"))
    
    # 2. Palmitoil-CoA Citosólico (Nombre encima de la estructura)
    partes.append(nodo_libre(x_box, y_box - 800, "Palmitoil-CoA (Citosólico)", "16C", PALMITOIL_COA, "m_palmitoil_cito", text_pos="top", dx=110, dy=-22))
    partes.append(reaccion_libre(x_box + 60, y_box - 800 + 80, 50, "CPT-1 (Lanzadera de Carnitina)", entra="+ Carnitina", sale="- CoA-SH", id_rx="rx_cpt1"))
    partes.append(etiqueta_regulacion("cpt1", x_box + 260, y_box - 800 + 90, dx=0, dy=0))
    
    # 3. Palmitoil-Carnitina (Espacio Citosol / EIM exterior)
    partes.append(nodo_libre(x_box, y_box - 280, "Palmitoil-Carnitina", "16C", PALMITOIL_CARNITINA, "m_palm_carnitina", text_right=True, dx=145))
    
    # Cruce del Espacio Intermembrana (EIM) e inserción de CACT directamente incrustado en la Membrana Mitocondrial Interna (MMI)
    x_cact = 240
    y_cact = 2305
    partes.append(f'''
    <!-- Lanzadera de Carnitina: Transportador CACT en la MMI -->
    <g id="transportador_cact" data-arrastrable="1" transform="translate({x_cact - 48}, {y_cact - 20})">
      <rect x="0" y="0" width="96" height="40" rx="10" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
      <text x="48" y="18" fill="#ffffff" font-size="12.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" stroke="none">CACT</text>
      <text x="48" y="32" fill="#e0f2fe" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle" stroke="none">Antipuerto MMI</text>
    </g>
    ''')
    
    # CPT-2 en la cara interna de la membrana mitocondrial interna (Matriz despejada)
    partes.append(reaccion_libre(x_cact, y_cact + 25, 40, "CPT-2 (Cara Interna MMI)", entra="+ CoA-SH", sale="- Carnitina", id_rx="rx_cpt2"))

    # 4. Palmitoil-CoA en la matriz mitocondrial
    y_m_palm = 2390
    partes.append(nodo_libre(x_box, y_m_palm + 35, "Palmitoil-CoA (Matriz)", "16C", PALMITOIL_COA, "m_palmitoil", text_pos="top", dx=110, dy=-20))
    partes.append(reaccion_libre(x_box + 60, y_m_palm + 105, 42, "Acil-CoA DH", entra="+ FAD", sale="+ FADH2", es_ganancia=True, id_rx="rx_box1"))
    
    # 5. trans-Δ²-Enoil-CoA (Paso añadido)
    y_m_enoil = y_m_palm + 140
    partes.append(nodo_libre(x_box, y_m_enoil, "trans-Δ²-Enoil-CoA", "16C", TRANS_DELTA2_ENOIL_COA, "m_trans_enoil", text_right=True, dx=265))
    partes.append(reaccion_libre(x_box + 60, y_m_enoil + 70, 42, "Enoil-CoA Hidratasa", entra="+ H₂O", id_rx="rx_box1b"))

    # 6. L-β-Hidroxiacil-CoA
    y_m_hidro = y_m_enoil + 140
    partes.append(nodo_libre(x_box, y_m_hidro, "L-β-Hidroxiacil-CoA", "16C", L_BETA_HIDROXIACIL_COA, "m_hidroxi_coa", text_right=True, dx=210))
    partes.append(reaccion_libre(x_box + 60, y_m_hidro + 70, 42, "β-Hidroxiacil-CoA DH", entra="+ NAD+", sale="+ NADH + H+", es_ganancia=True, id_rx="rx_box2"))
    
    # 7. β-Cetoacil-CoA
    y_m_ceto = y_m_hidro + 140
    partes.append(nodo_libre(x_box, y_m_ceto, "β-Cetoacil-CoA", "16C", BETA_CETOACIL_COA, "m_cetoacil_coa", text_right=True, dx=265))
    partes.append(reaccion_libre(x_box + 60, y_m_ceto + 70, 42, "Tiolasa", entra="+ CoA-SH", id_rx="rx_box3"))
    
    # 8. Clivaje tiolítico: Acetil-CoA y Miristoil-CoA
    y_m_split = y_m_ceto + 160
    partes.append(nodo_libre(85, y_m_split, "Acetil-CoA", "2C", ACETIL_COA_BETA, "m_acetil_coa_beta", text_pos="top", dx=50, dy=65))
    partes.append(nodo_libre(230, y_m_split, "Miristoil-CoA", "14C", MIRISTOIL_COA, "m_miristoil_coa", text_pos="top", dx=95, dy=-16))
    
    partes.append(f"""
    <path d="M {x_box+60} {y_m_ceto + 115} L 135 {y_m_split - 22}" stroke="#ea580c" stroke-width="2.6" fill="none" marker-end="url(#arrowFlow)"/>
    <path d="M {x_box+60} {y_m_ceto + 115} L 270 {y_m_split - 22}" stroke="#ea580c" stroke-width="2.6" fill="none" marker-end="url(#arrowFlow)"/>
    """)
    partes.append(f'</g>')

    # =========================================================================
    # 11. CETOGÉNESIS (MATRIZ MITOCONDRIAL)
    # =========================================================================
    x_ceto = 570
    y_ceto = y_mito + 700
    paso_c = 140
    partes.append(f'<g id="ruta_ceto">')
    partes.append(badge_via(11, x_ceto - 40, y_ceto - 20))
    partes.append(f'''
    <text x="{x_ceto + 10}" y="{y_ceto - 8}" fill="#9d174d" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">Paso 1: Tiolasa (ACAT1) • 2 Acetil-CoA ⇄</text>
    ''')
    
    partes.append(nodo_libre(x_ceto, y_ceto, "Acetoacetil-CoA", "4C", ACETOACETIL_COA, "m_acetoac_coa", text_right=True, dx=200))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + 70, 40, "HMG-CoA Sintasa 2 (HMGCS2)", entra="+ Acetil-CoA", sale="- CoA-SH", id_rx="rx_ceto1"))
    partes.append(etiqueta_regulacion("hmgcs2", x_ceto + 74, y_ceto + 108, dx=0, dy=0))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c, "HMG-CoA", "6C", HMG_COA, "m_hmg_coa", text_right=True, dx=200))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + paso_c + 70, 40, "HMG-CoA Liasa", sale="+ Acetil-CoA", id_rx="rx_ceto2"))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c*2, "Acetoacetato", "4C", ACETOACETATO, "m_acetoacetato", text_right=True, dx=200))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + paso_c*2 + 70, 40, "β-Hidroxibutirato DH", entra="+ NADH", sale="+ NAD+", id_rx="rx_ceto3"))

    # Rama lateral de descarboxilación espontánea: Acetoacetato ➔ Acetona [3C] + CO₂ ↑
    partes.append(f'''
    <g id="rx_ceto_acetona" data-arrastrable="1">
      <path d="M {x_ceto - 5} {y_ceto + paso_c*2 + 25} L 465 {y_ceto + paso_c*2 + 25}" fill="none" stroke="#db2777" stroke-width="2.2" stroke-dasharray="5 3" marker-end="url(#arrowRed)"/>
      <text x="512" y="{y_ceto + paso_c*2 + 15}" fill="#be185d" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Espontánea (- CO₂ ↑)</text>
    </g>
    ''')
    partes.append(nodo_libre(335, y_ceto + paso_c*2 + 2, "Acetona", "3C", ACETONA, "m_acetona_ceto", text_pos="bottom", dx=58, dy=52, detalle="Volátil • Exhalación pulmonar"))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c*3, "D-β-Hidroxibutirato", "4C", D_BETA_HIDROXIBUTIRATO, "m_betahidroxi", text_right=True, dx=220))
    
    # Línea rosa de exportación hacia sangre
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        y_ceto_bottom = y_ceto + paso_c*3 + 70
        partes.append(f'''
        <path d="M {x_ceto + 40} {y_ceto + paso_c*3 + 45} L {x_ceto + 40} {y_ceto_bottom} L 55 {y_ceto_bottom} L 55 40" fill="none" stroke="#ec4899" stroke-width="3.2" stroke-dasharray="10 5" marker-end="url(#arrowFlow)"/>
        <text x="42" y="1600" fill="#db2777" font-size="13" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 42 1600)" stroke="none">EXPORTACIÓN DE CUERPOS CETÓNICOS A SANGRE (PARA CEREBRO/MÚSCULO) ➔</text>
        ''')
    
    partes.append(f'</g>')

    # =========================================================================
    # 12. METABOLISMO DEL NITRÓGENO Y AMINOÁCIDOS: TRANSAMINACIÓN Y DESAMINACIÓN
    # =========================================================================
    x_aa = 2140
    y_aa = 380
    partes.append(f'<g id="ruta_transaminacion_desaminacion">')
    partes.append(badge_via(13, x_aa - 190, 170))

    # Rótulo de la vía en el citosol (elevado a Y=170 para no interferir con G6PDH en Y=335)
    partes.append(f'''
    <g id="banner_aminoacidos" data-arrastrable="1" transform="translate({x_aa}, 170)">
      <rect x="-170" y="-14" width="340" height="28" rx="14" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.8"/>
      <text x="0" y="4" fill="#0f766e" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
        TRANSAMINACIÓN Y DESAMINACIÓN OXIDATIVA
      </text>
    </g>
    ''')

    # 1. Transportador en membrana plasmática: Captación de Alanina desde sangre
    partes.append(f'''
    <g id="carrier_lat1" data-arrastrable="1" transform="translate({x_aa - 40}, 55)">
      <rect x="0" y="0" width="80" height="26" rx="6" fill="#0d9488" stroke="#0f766e" stroke-width="2"/>
      <text x="40" y="17" fill="#ffffff" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">LAT-1 / ASCT2</text>
      <line x1="40" y1="26" x2="40" y2="70" stroke="#0d9488" stroke-width="2.4" marker-end="url(#arrowTeal)"/>
    </g>
    ''')

    # 2. L-Alanina en citosol (entró de sangre / ciclo glucosa-alanina)
    partes.append(nodo_libre(x_aa, y_aa, "L-Alanina", "3C", AMINO_ALANINA, "m_ala_integ", text_pos="top", dy=-20))

    # Reacción ALT / GPT (Alanina + α-KG ⇄ Piruvato + Glutamato)
    partes.append(f'''
    <g id="rx_alt_integ" data-arrastrable="1" transform="translate({x_aa}, {y_aa + 115})">
      <line x1="-3" y1="0" x2="-3" y2="75" stroke="#0d9488" stroke-width="2" marker-end="url(#arrowTeal)"/>
      <line x1="3" y1="75" x2="3" y2="0" stroke="#0d9488" stroke-width="2" marker-end="url(#arrowTeal)"/>
      <!-- Arco de recolección de nitrógeno acoplado con α-KG ➔ Glutamato -->
      <path d="M 65 10 Q 15 38 65 65" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrowBlueAmino)"/>
      <text x="70" y="-4" fill="#64748b" font-size="9.5" font-family="'Inter', sans-serif">α-Cetoglutarato</text>
      <text x="70" y="72" fill="#1d4ed8" font-size="10" font-weight="800" font-family="'Inter', sans-serif">Glutamato</text>

      <g transform="translate(-15, 38)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">ALT / GPT</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 2.6.1.2 (PLP)</text>
      </g>
    </g>
    ''')

    # 3. Piruvato resultante de ALT en citosol
    partes.append(nodo_libre(x_aa, y_aa + 230, "Piruvato (de Alanina)", "3C", PIRUVATO, "m_pyr_ala_integ", text_right=True, dx=110))

    # Conexión directa hacia la Glucólisis
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <text x="{x_aa + 30}" y="{y_aa + 305}" fill="#c2410c" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Pool de Piruvato (➔ MPC) ↓</text>
        <path d="M {x_aa} {y_aa + 320} C 1960 {y_aa + 345}, 1960 800, 1960 1550 C 1960 1630, 1920 1675, 1880 1675" fill="none" stroke="#ea580c" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowFlow)"/>
        ''')

    # 4. L-Glutamato (colector común de nitrógeno en citosol - centrado en X=2280 con texto superior)
    partes.append(nodo_libre(2280, y_aa + 380, "L-Glutamato", "5C", AMINO_GLUTAMATO, "m_glu_integ", text_pos="top", dy=-18))

    # 5. Rama Citosólica de Glutamina Sintetasa (Destoxificación a Glutamina)
    partes.append(nodo_libre(2280, y_aa + 630, "L-Glutamina", "5C", AMINO_GLUTAMINA, "m_gln_integ", text_pos="top", dx=70, dy=-38, detalle="Destino: Torrente Sanguíneo"))
    partes.append(f'''
    <g id="rx_glns_integ" data-arrastrable="1" transform="translate(2280, {y_aa + 505})">
      <line x1="0" y1="0" x2="0" y2="70" stroke="#0d9488" stroke-width="2.4" marker-end="url(#arrowTeal)"/>
      <path d="M -25 15 Q -8 15 -3 30" fill="none" stroke="#2563eb" stroke-width="1.8" marker-end="url(#arrowBlueAmino)"/>
      <text x="-28" y="18" fill="#1d4ed8" font-size="9" font-weight="800" text-anchor="end">+ NH₄⁺</text>
      <path d="M -25 35 Q -10 35 -3 45" fill="none" stroke="#dc2626" stroke-width="1.6" marker-end="url(#arrowRed)"/>
      <text x="-28" y="38" fill="#dc2626" font-size="9" font-weight="800" text-anchor="end">- 1 ATP</text>
      <g transform="translate(15, 38)">
        <text x="0" y="0" fill="#0f172a" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">Glutamina Sintetasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 6.3.1.2</text>
      </g>
    </g>
    ''')

    # Exportación de Glutamina al torrente sanguíneo
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <path d="M 2340 {y_aa + 640} Q 2420 {y_aa + 640} 2420 850 L 2420 74" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
        <text x="2435" y="520" fill="#0f766e" font-size="11" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 2435 520)">EXPORTACIÓN DE GLUTAMINA A SANGRE ➔</text>
        ''')

    # 6. Importación de Glutamato a la Mitocondria a través de AGC / GC1
    x_agc = 2060
    y_agc = y_mito - 35
    y_gldh_start = y_mito + 110
    partes.append(f'''
    <g id="carrier_agc_mmi" data-arrastrable="1" transform="translate({x_agc - 45}, {y_agc - 15})">
      <rect x="0" y="0" width="90" height="34" rx="8" fill="#b45309" stroke="#78350f" stroke-width="2"/>
      <text x="45" y="21" fill="#ffffff" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">AGC / GC1</text>
      <text x="45" y="47" fill="#78350f" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Carrier Glutamato</text>
    </g>
    ''')
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <path d="M 2240 {y_aa + 400} C 2220 {y_aa + 440}, 2220 950, 2220 1200 C 2220 1500, {x_agc} 1750, {x_agc} {y_agc - 18}" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
        <path d="M {x_agc} {y_agc + 22} L {x_agc} {y_gldh_start - 10}" fill="none" stroke="#0d9488" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowTeal)"/>
        ''')

    # 7. MATRIZ MITOCONDRIAL: Glutamato en la Matriz (elevado para no interferir con Krebs->CTE)
    partes.append(nodo_libre(x_agc - 40, y_gldh_start, "L-Glutamato (Matriz)", "5C", AMINO_GLUTAMATO, "m_glu_mito_integ", text_right=True, dx=145))

    # Reacción GLDH (Glutamato Deshidrogenasa) - Arquitectura espaciosa y despejada
    partes.append(f'''
    <g id="rx_gldh_integ" data-arrastrable="1" transform="translate({x_agc + 10}, {y_gldh_start + 135})">
      <line x1="-3" y1="0" x2="-3" y2="70" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
      <line x1="3" y1="70" x2="3" y2="0" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
      
      <!-- Entrada NAD(P)+ / Salida NAD(P)H en arco izquierdo despejado -->
      <path d="M -90 10 Q -35 10 -4 20" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-95" y="14" fill="#059669" font-size="9.5" font-weight="800" text-anchor="end">+ NAD(P)⁺ + H₂O</text>
      
      <path d="M -4 46 Q -35 56 -90 56" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-95" y="60" fill="#059669" font-size="9.5" font-weight="800" text-anchor="end">+ NAD(P)H + H⁺</text>

      <!-- Salida de Amonio libre hacia la derecha -->
      <path d="M 4 35 Q 60 35 120 60" fill="none" stroke="#2563eb" stroke-width="2.4" marker-end="url(#arrowBlueAmino)"/>
      <text x="125" y="68" fill="#1d4ed8" font-size="11" font-weight="900" font-family="'Inter', sans-serif">➔ + NH₄⁺</text>

      <!-- Textos y Alosterismo a la derecha bien despejados -->
      <g transform="translate(45, -10)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif">Glutamato Deshidrogenasa (GLDH)</text>
        <text x="0" y="14" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">EC 1.4.1.3 (Mitocondrial)</text>
        <text x="0" y="27" fill="#16a34a" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">(+) ADP, GDP (activa)</text>
        <text x="0" y="39" fill="#e11d48" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">(-) ATP, GTP (inhibe)</text>
      </g>
    </g>
    ''')

    # 8. Productos de GLDH:
    # A. α-Cetoglutarato regenerado en matriz mitocondrial (hacia la izquierda, espaciado a X=x_agc - 260)
    partes.append(nodo_libre(x_agc - 260, y_gldh_start + 225, "α-Cetoglutarato", "5C", AMINO_AKG, "m_akg_gldh_integ", text_right=False, dx=-30))
    # Ramificación de la flecha de GLDH hacia la estructura de α-Cetoglutarato
    partes.append(f'''
    <path d="M {x_agc - 5} {y_gldh_start + 205} Q {x_agc - 80} {y_gldh_start + 245} {x_agc - 150} {y_gldh_start + 245}" fill="none" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
    ''')
    # Conexión directa hacia el Ciclo de Krebs
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <path d="M {x_agc - 260} {y_gldh_start + 270} C 1720 2520, 1500 2550, 1420 2620 C 1370 2660, 1330 2710, {x_k + 160} {y_k + paso_k * 3 - 10}" fill="none" stroke="#b45309" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowFlow)"/>
        <text x="1650" y="2520" fill="#78350f" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">➔ Reingreso al Ciclo de Krebs (α-KG)</text>
        ''')

    # B. Ion Amonio (NH4+) libre en matriz (hacia la derecha, espaciado a X=x_agc + 160)
    partes.append(nodo_libre(x_agc + 170, y_gldh_start + 225, "Ion Amonio (NH₄⁺)", "Nitrógeno", AMINO_NH4, "m_nh4_integ", text_right=True, dx=85))
    # Conexión directa hacia el Ciclo de la Urea
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <!-- Canal conductor de Amonio hacia CPS-1 -->
        <g id="canal_amonio_hacia_urea" data-arrastrable="1">
          <path d="M {x_agc + 190} {y_gldh_start + 185} Q {x_agc + 230} {y_gldh_start + 200} {x_agc + 230} 2520 L {x_agc + 230} 3360 Q {x_agc + 230} 3380 {x_agc + 250} 3380 L 4120 3380 Q 4140 3380 4140 3340 L 4140 3260" fill="none" stroke="#2563eb" stroke-width="3" stroke-dasharray="8 5" marker-end="url(#arrowBlueAmino)"/>
          <g transform="translate(3050, 3368)">
            <rect x="-195" y="-13" width="390" height="26" rx="8" fill="#1e293b" opacity="0.9" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="0" y="4" fill="#93c5fd" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CANAL MATRICIAL DE NH₄⁺ ➔ SÍNTESIS DE UREA (CPS-1)</text>
          </g>
        </g>
        ''')

    partes.append(f'</g>')

    # =========================================================================
    # 12B. DESTINOS DE LOS ESQUELETOS CARBONADOS DE AMINOÁCIDOS (VÍA 12B)
    # =========================================================================
    partes.append(f'<g id="ruta_destinos_aa">')

    # 1. Rótulo principal de la Vía 12B en corredor citosólico central
    partes.append(badge_via("12B", 2480, 1195))
    partes.append(f'''
    <g id="banner_destinos_aa" data-arrastrable="1" transform="translate(2660, 1195)">
      <rect x="-165" y="-14" width="330" height="28" rx="14" fill="#fdf4ff" stroke="#a855f7" stroke-width="1.8"/>
      <text x="0" y="4" fill="#7e22ce" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
        DESTINOS DE ESQUELETOS CARBONADOS (20 AA)
      </text>
    </g>
    ''')

    # -------------------------------------------------------------------------
    # A. CASCADA AROMÁTICA CITOSÓLICA (Phe ➔ Tyr ➔ Fumarato + Acetoacetato)
    # (Zona despejada: X ≈ 2480 - 2680, Y ≈ 1240 - 1840)
    # -------------------------------------------------------------------------
    # L-Fenilalanina
    partes.append(nodo_libre(2480, 1250, "L-Fenilalanina", "9C", AA_FENILALANINA, "m_phe_aa", text_right=True, dx=115, detalle="Esencial • Mixto"))

    # Reacción PAH (Fenilalanina Hidroxilasa)
    partes.append(f'''
    <g id="rx_pah" data-arrastrable="1" transform="translate(2520, 1410)">
      <line x1="0" y1="0" x2="0" y2="55" stroke="#9333ea" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <path d="M 12 12 Q 35 12 40 28" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="45" y="24" fill="#0284c7" font-size="8.5" font-weight="800">+ O₂ + BH₄ ➔ H₂O + BH₂</text>
      <g transform="translate(-15, 28)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Fenilalanina Hidroxilasa (PAH)</text>
        <text x="0" y="13" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 1.14.16.1 (BH₄)</text>
      </g>
    </g>
    ''')
    partes.append(badge_clinico(2530, 1455, "[Clínica] PKU • Déficit PAH / BH₄", es_alerta=True))

    # L-Tirosina
    partes.append(nodo_libre(2480, 1500, "L-Tirosina", "9C", AA_TIROSINA, "m_tyr_aa", text_right=True, dx=115, detalle="Condicionalmente esencial"))

    # Cascada catabólica: HGD y FAH
    partes.append(f'''
    <g id="rx_tirosina_catabolismo" data-arrastrable="1" transform="translate(2520, 1690)">
      <line x1="0" y1="0" x2="0" y2="65" stroke="#9333ea" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="-15" y="20" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Homogentisato 1,2-Dioxigenasa (HGD)</text>
      <text x="-15" y="32" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 1.13.11.5</text>
      <text x="-15" y="50" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Fumarilacetoacetasa (FAH)</text>
      <text x="-15" y="62" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 3.7.1.2</text>
    </g>
    ''')
    partes.append(badge_clinico(2530, 1705, "[Clínica] Alcaptonuria • Déficit HGD", es_alerta=True))
    partes.append(badge_clinico(2530, 1745, "[Clínica] Tirosinemia I • Déficit FAH", es_alerta=True))

    # Bifurcación Fumarato (➔ Krebs) y Acetoacetato (➔ Cetogénesis)
    partes.append(f'''
    <!-- Conectores continuos de convergencia de esqueletos carbonados -->
    <g id="conectores_catabolismo_phe_tyr">
      <!-- Rama Glucogénica: Fumarato hacia Ciclo de Krebs (m_fumarato) -->
      <path d="M 2520 1765 Q 2480 1775 2480 1810 L 2480 2025 Q 2480 2040 2465 2040 L 1575 2040 Q 1560 2040 1560 2055 L 1560 3265 Q 1560 3280 1545 3280 L 1260 3280" fill="none" stroke="#16a34a" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
      <text x="2470" y="1805" fill="#15803d" font-size="9.5" font-weight="800" text-anchor="end">Fumarato</text>

      <!-- Rama Cetogénica: Acetoacetato hacia Cetogénesis (m_acetoacetato) -->
      <path d="M 2520 1765 Q 2560 1775 2560 1810 L 2560 2040 Q 2560 2055 2545 2055 L 1015 2055 Q 1000 2055 1000 2070 L 1000 3055 Q 1000 3070 985 3070 L 765 3070 Q 750 3070 750 3085 L 750 3135" fill="none" stroke="#dc2626" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowRed)"/>
      <text x="2570" y="1805" fill="#b91c1c" font-size="9.5" font-weight="800" text-anchor="start">Acetoacetato</text>
    </g>
    ''')

    # -------------------------------------------------------------------------
    # B. VÍA DE METIONINA, HOMOCISTEÍNA Y TRANSULFURACIÓN (CITOSOL)
    # (Zona despejada: X ≈ 2740 - 2940, Y ≈ 1240 - 1700)
    # -------------------------------------------------------------------------
    partes.append(nodo_aa(2740, 1250, "L-Metionina", "5C", clasificacion="glu", detalle="Esencial • Inicia SAM"))
    partes.append(f'''
    <g id="rx_transmetilacion" data-arrastrable="1" transform="translate(2760, 1300)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#16a34a" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <text x="12" y="22" fill="#64748b" font-size="8.5" font-family="'Inter', sans-serif">SAM ➔ SAH</text>
    </g>
    ''')
    partes.append(nodo_libre(2730, 1350, "L-Homocisteína", "4C", AA_HOMOCISTEINA, "m_hcy_aa", text_right=True, dx=85, detalle="Tiol reactivo"))

    # Reacción CBS (Cistationina β-Sintetasa)
    partes.append(f'''
    <g id="rx_cbs" data-arrastrable="1" transform="translate(2760, 1510)">
      <line x1="0" y1="0" x2="0" y2="50" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <path d="M -8 15 Q -25 15 -30 28" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-35" y="22" fill="#15803d" font-size="8.5" font-weight="800" text-anchor="end">+ Serina</text>
      <g transform="translate(15, 24)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Cistationina β-Sintetasa (CBS)</text>
        <text x="0" y="13" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">EC 4.2.1.22 (PLP / Vit B₆)</text>
      </g>
    </g>
    ''')
    partes.append(badge_clinico(2680, 1580, "[Clínica] Homocistinuria • CBS / B₆", es_alerta=True))

    # Tránsito hacia L-Cistationina y bifurcación a Propionil-CoA y L-Cisteína
    partes.append(f'''
    <!-- Conector CBS -> L-Cistationina -->
    <path d="M 2760 1610 L 2780 1610 Q 2795 1610 2795 1625 L 2795 1630" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    ''')
    partes.append(nodo_aa(2795, 1640, "L-Cistationina", "7C", clasificacion="glu", detalle="Condensado Hcy + Ser", id_nodo="m_cistat_aa"))

    partes.append(f'''
    <!-- Reacción CTH (Cistationina γ-Liasa) -->
    <g id="rx_cth" data-arrastrable="1" transform="translate(2810, 1680)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(-15, 18)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Cistationina γ-Liasa (CTH)</text>
        <text x="0" y="12" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 4.4.1.1 (PLP / Vit B₆)</text>
      </g>
    </g>
    ''')

    partes.append(f'''
    <!-- Conectores continuos de convergencia de Cistationina -->
    <g id="conectores_transsulfuracion">
      <!-- Rótulos de salida de bifurcación -->
      <text x="2770" y="1735" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Propionil-CoA</text>
      <text x="2825" y="1735" fill="#0f766e" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="start">L-Cisteína</text>
    ''' + (f'''
      <!-- Rama hacia Propionil-CoA (m_prop_aa_matriz en Matriz) -->
      <path id="conn_transsulf_prop" d="M 2810 1715 L 2800 1715 Q 2780 1715 2780 1730 L 2780 2035 Q 2780 2050 2765 2050 L 1035 2050 Q 1020 2050 1020 2065 L 1020 2585 Q 1020 2600 1005 2600 L 795 2600" fill="none" stroke="#16a34a" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>

      <!-- Rama hacia L-Cisteína (nodo citosólico en afluentes a Piruvato) -->
      <path id="conn_transsulf_cys" d="M 2810 1715 L 2945 1715 Q 2960 1715 2960 1700 L 2960 1195 Q 2960 1180 2945 1180 L 2415 1180 Q 2400 1180 2400 1165 L 2400 580 Q 2400 565 2385 565 L 2345 565" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
    ''' if MOSTRAR_CONEXIONES_INTER_RUTA else '') + f'''
    </g>
    ''')

    # -------------------------------------------------------------------------
    # C. MATRIZ MITOCONDRIAL: BCAA Y PROPIONIL-CoA ➔ METILMALONIL-CoA ➔ SUCCINIL-CoA
    # (Zona 100% despejada: X ≈ 590 - 750, Y ≈ 2360 - 2850)
    # -------------------------------------------------------------------------
    # Nodos AA BCAA (Val, Ile) con colector hacia BCKDH
    partes.append(nodo_aa(610, 2360, "L-Valina", "5C", clasificacion="glu", detalle="BCAA Glucogénico"))
    partes.append(nodo_aa(610, 2398, "L-Isoleucina", "6C", clasificacion="mixto", detalle="BCAA Mixto"))
    partes.append('''
    <path d="M 600 2368 L 590 2368 L 590 2432 L 640 2432 M 600 2406 L 590 2406" fill="none" stroke="#ea580c" stroke-width="1.8"/>
    ''')

    # Complejo BCKDH
    partes.append(f'''
    <g id="rx_bckdh" data-arrastrable="1" transform="translate(640, 2436)">
      <line x1="0" y1="0" x2="0" y2="28" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <g transform="translate(15, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Complejo BCKDH</text>
        <text x="0" y="12" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">Cofactores: TPP, Lipoamida, CoA-SH, FAD, NAD⁺</text>
      </g>
    </g>
    ''')
    partes.append(badge_clinico(580, 2472, "[Clínica] MSUD • Jarabe de Arce (BCKDH)", es_alerta=True))

    # Propionil-CoA [3C]
    partes.append(nodo_libre(610, 2525, "Propionil-CoA", "3C", AA_PROPIONIL_COA, "m_prop_aa_matriz", text_pos="top", dx=55, dy=-18))

    # Reacción PCC (Propionil-CoA Carboxilasa)
    partes.append(f'''
    <g id="rx_pcc" data-arrastrable="1" transform="translate(640, 2572)">
      <line x1="0" y1="0" x2="0" y2="24" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <path d="M -8 8 Q -25 8 -30 18" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-35" y="14" fill="#dc2626" font-size="8" font-weight="800" text-anchor="end">+ ATP + HCO₃⁻</text>
      <g transform="translate(15, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Propionil-CoA Carboxilasa (PCC)</text>
        <text x="0" y="12" fill="#0284c7" font-size="8.5" font-weight="800">EC 6.4.1.3 (Biotina)</text>
      </g>
    </g>
    ''')

    # Intermediario D/L-Metilmalonil-CoA [4C]
    partes.append(nodo_libre(610, 2652, "D/L-Metilmalonil-CoA", "4C", AA_METILMALONIL_COA, "m_metilmalonil_aa", text_pos="top", dx=65, dy=-22))

    # Reacción MCM (Metilmalonil-CoA Mutasa)
    partes.append(f'''
    <g id="rx_mcm" data-arrastrable="1" transform="translate(640, 2700)">
      <line x1="0" y1="0" x2="0" y2="28" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <g transform="translate(15, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Metilmalonil-CoA Mutasa (MCM)</text>
        <text x="0" y="12" fill="#0284c7" font-size="8.5" font-weight="800">EC 5.4.99.2 (Vitamina B₁₂)</text>
      </g>
    </g>
    ''')
    partes.append(badge_clinico(590, 2740, "[Clínica] Acidemia Metilmalónica • MCM / B₁₂", es_alerta=True))

    # Conexión directa anaplerótica a Succinil-CoA de Krebs
    partes.append(f'''
    <path d="M 640 2778 L 640 2830 L 780 2830" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="650" y="2824" fill="#c2410c" font-size="9.5" font-weight="800">➔ Succinil-CoA [4C] (Krebs)</text>
    ''')

    # Aminoácidos Cetogénicos Puros (Leu, Lys) en Matriz con línea colectora hacia Acetoacetil-CoA
    partes.append(nodo_aa(455, 2875, "L-Leucina", "6C", clasificacion="ceto"))
    partes.append(nodo_aa(455, 2912, "L-Lisina", "6C", clasificacion="ceto"))
    partes.append(f'''
    <path d="M 535 2882 L 548 2882 L 548 2919 L 535 2919 M 548 2895 L 566 2885" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
    <text x="435" y="2900" fill="#881337" font-size="8.5" font-weight="800" text-anchor="end">Leu, Lys ➔ Acetoacetil-CoA</text>
    ''')

    # -------------------------------------------------------------------------
    # D. AFLUENTES A PIRUVATO, GLUTAMATO Y OXALACETATO
    # -------------------------------------------------------------------------
    # Afluentes Ser, Gly, Cys, Thr ➔ Piruvato (Zona despejada: X ≈ 2295, Y ≈ 465-580)
    partes.append('''<text x="2295" y="465" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif">Ser, Gly, Cys ➔ Piruvato</text>''')
    partes.append(nodo_aa(2295, 485, "L-Serina", "3C", clasificacion="glu", detalle="Serina deshidratasa (PLP)"))
    partes.append(nodo_aa(2295, 525, "Glicina", "2C", clasificacion="glu", detalle="Sistema escisión (GCS)"))
    partes.append(nodo_aa(2295, 565, "L-Cisteína", "3C", clasificacion="glu", detalle="Desulfuración"))
    partes.append(f'''
    <path d="M 2285 492 L 2275 492 L 2275 572 L 2285 572 M 2285 532 L 2275 532" fill="none" stroke="#16a34a" stroke-width="1.8"/>
    <path d="M 2275 572 L 2275 602 L 2205 602" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
    ''')

    # Afluentes Pro, His, Arg ➔ Glutamato (Zona despejada: X ≈ 2040, Y ≈ 760-880)
    partes.append('''<text x="2040" y="760" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif">Pro, His, Arg ➔ Glutamato ➔</text>''')
    partes.append(nodo_aa(2040, 780, "L-Prolina", "5C", clasificacion="glu", detalle="Oxidación a Glutamato"))
    partes.append(nodo_aa(2040, 820, "L-Histidina", "6C", clasificacion="glu", detalle="Histidasa ➔ FIGLU ➔ Glu"))
    partes.append(nodo_aa(2040, 860, "L-Arginina", "6C", clasificacion="glu", detalle="Urea ➔ Ornitina ➔ Glu"))
    partes.append(f'''
    <path d="M 2182 788 L 2198 788 L 2198 868 L 2182 868 M 2182 828 L 2198 828" fill="none" stroke="#16a34a" stroke-width="1.8"/>
    <path d="M 2198 788 L 2265 788" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
    ''')

    # Afluentes Asn, Asp ➔ Oxalacetato (Zona despejada: X ≈ 500, Y ≈ 2215-2260)
    partes.append('''<text x="500" y="2195" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif">Asn, Asp ➔ Oxalacetato ➔</text>''')
    partes.append(nodo_aa(500, 2215, "L-Asparagina", "4C", clasificacion="glu", detalle="Asparaginasa ➔ Aspartato"))
    partes.append(nodo_aa(500, 2255, "L-Aspartato", "4C", clasificacion="glu", detalle="AST / GOT ➔ Oxalacetato"))
    partes.append(f'''
    <path d="M 640 2235 L 735 2235 Q 750 2235 750 2222 L 885 2222 Q 895 2222 895 2235" fill="none" stroke="#16a34a" stroke-width="2.3" stroke-dasharray="6 4" marker-end="url(#arrowGreen)"/>
    ''')

    partes.append(f'</g>')

    # =========================================================================
    # 13. CICLO DE LA UREA Y BICICLO DE KREBS (CUADRANTE DERECHO - ENTORNO REAL)
    # =========================================================================
    x_u_l = 4100  # Carril Izquierdo (Carbamoil-P, CPS-1, Aspartato, Fumarato, Biciclo)
    x_u_c = 4420  # Carril Central (Flujo principal: Citrulina, Arg-Succ, Arginina, Urea)
    x_u_r = 4640  # Carril Derecho (Lanzadera de Ornitina, ORNT1)

    partes.append(f'''
    <!-- ================================================================= -->
    <!-- RUTA 13: CICLO DE LA UREA (DESINTOXICACIÓN HEPÁTICA DE NITRÓGENO)   -->
    <!-- ================================================================= -->
    <g id="ruta_ciclo_urea">
      <!-- Rótulo de la Ruta flotando libremente en citosol superior (despejado a la izquierda de la excreción) -->
      {badge_via(14, 4040, 230)}
      <g id="rotulo_ciclo_urea" data-arrastrable="1" transform="translate(4210, 235)">
        <text x="0" y="0" fill="#0f766e" font-size="24" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="3">CICLO DE LA UREA</text>
        <text x="0" y="24" fill="#64748b" font-size="12" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Desintoxicación Hepática de Amonio • Biciclo de Krebs • Excreción Renal</text>
      </g>
    ''')

    # -------------------------------------------------------------------------
    # FASE MATRICIAL MITOCONDRIAL (Y > 2160)
    # -------------------------------------------------------------------------

    # 1. Sustratos Iniciales (NH4+ libre + HCO3-)
    partes.append(nodo_libre(
        x_u_l - 40, 3240,
        "Sustratos de Nitrógeno", "NH₄⁺ + HCO₃⁻",
        UREA_IONES_INICIALES, "m_u_sustratos_inicio",
        text_right=True, dx=190,
        detalle="Amonio aportado por GLDH matricial"
    ))

    # Reacción 1: CPS-1 (Carbamoil Fosfato Sintetasa I)
    partes.append(f'''
    <g id="rx_u_cps1" data-arrastrable="1" transform="translate({x_u_l}, 3060)">
      <!-- Flecha vertical ascendente -->
      <line x1="0" y1="120" x2="0" y2="-10" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de 2 ATP (lado izquierdo) -->
      <path d="M -75 90 Q -25 90 -4 65" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-80" y="93" fill="#dc2626" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">- 2 ATP</text>

      <!-- Salida de 2 ADP + Pi (lado izquierdo) -->
      <path d="M -4 35 Q -25 20 -75 20" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-80" y="24" fill="#475569" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ 2 ADP + Pi</text>

      <!-- Metadatos de CPS-1 -->
      <g transform="translate(20, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="12.5" font-weight="900" font-family="'Inter', sans-serif">Carbamoil Fosfato Sintetasa I (CPS-1)</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">EC 6.3.4.16 (Mitocondrial)</text>
        <text x="0" y="27" fill="#16a34a" font-size="10" font-weight="800" font-family="'Inter', sans-serif">⊕ N-Acetilglutamato (NAG) activador obligado</text>
        <text x="0" y="40" fill="#b45309" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Paso limitante irreversible</text>
      </g>
    </g>
    ''')

    # 2. Carbamoil Fosfato (1C)
    partes.append(nodo_libre(
        x_u_l - 40, 2860,
        "Carbamoil Fosfato", "1C",
        UREA_CARBAMOIL_P, "m_u_carbamoil_p",
        text_right=True, dx=140,
        detalle="1ᵉʳ nitrógeno activado en anhidro fosfato"
    ))

    # 3. L-Ornitina en Matriz Mitocondrial (X=4700, texto orientado hacia el interior de la matriz)
    partes.append(nodo_libre(
        x_u_r - 40, 2860,
        "L-Ornitina (Matriz)", "5C",
        UREA_ORNITINA, "m_u_ornitina_mito",
        text_right=False, dx=-15,
        detalle="Aceptor regenerado por ORNT1 ↻"
    ))

    # Reacción 2: OTC (Ornitina Transcarbamilasa)
    partes.append(f'''
    <g id="rx_u_otc" data-arrastrable="1" transform="translate({x_u_c}, 2670)">
      <!-- Curva desde Carbamoil-P hacia OTC -->
      <path d="M -200 160 Q -70 60 -4 20" fill="none" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

      <!-- Curva desde Ornitina matricial hacia OTC -->
      <path d="M 220 160 Q 90 60 4 20" fill="none" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

      <!-- Flecha vertical ascendente hacia Citrulina -->
      <line x1="0" y1="20" x2="0" y2="-65" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Salida de Pi libre (lado izquierdo) -->
      <path d="M -4 -15 Q -35 -25 -75 -25" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-80" y="-21" fill="#475569" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ Pi (Fosfato libre)</text>

      <!-- Metadatos de OTC -->
      <g transform="translate(18, -35)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif">Ornitina Transcarbamilasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">OTC • EC 2.1.3.3 (Mitocondrial)</text>
        <text x="0" y="25" fill="#0f766e" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Formación del grupo ureido</text>
      </g>
    </g>
    ''')

    # 4. L-Citrulina en Matriz Mitocondrial
    partes.append(nodo_libre(
        x_u_c - 40, 2370,
        "L-Citrulina (Matriz)", "6C",
        UREA_CITRULINA, "m_u_citrulina_mito",
        text_right=True, dx=140,
        detalle="1ᵉʳ nitrógeno fijado ➔ Exportación"
    ))

    # -------------------------------------------------------------------------
    # FASE TRANSLOCACIÓN MMI (Y ≈ 2160)
    # -------------------------------------------------------------------------

    # A. Transportador SLC25A13 (Citrina) en el carril central
    partes.append(f'''
    <g id="trans_u_citrina" data-arrastrable="1" transform="translate({x_u_c}, 2160)">
      <!-- Flechas de translocación ascendente de Citrulina -->
      <path d="M 0 160 L 0 25" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)" fill="none"/>
      <path d="M 0 -25 L 0 -85" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)" fill="none"/>

      <!-- Cápsula del transportador sobre MMI -->
      <rect x="-60" y="-18" width="120" height="36" rx="8" fill="#92400e" stroke="#78350f" stroke-width="2"/>
      <text x="0" y="4" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">SLC25A13</text>
      <text x="0" y="30" fill="#78350f" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Citrina (Exportador Citrulina)</text>
    </g>
    ''')

    # B. Transportador SLC25A15 (ORNT1) en el carril derecho
    partes.append(f'''
    <g id="trans_u_ornt1" data-arrastrable="1" transform="translate({x_u_r}, 2160)">
      <!-- Cápsula del transportador sobre MMI -->
      <rect x="-60" y="-18" width="120" height="36" rx="8" fill="#1d4ed8" stroke="#1e3a8a" stroke-width="2"/>
      <text x="0" y="4" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">SLC25A15</text>
      <text x="0" y="30" fill="#1e40af" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">ORNT1 (Carrier Ornitina)</text>
    </g>
    ''')

    # -------------------------------------------------------------------------
    # FASE CITOSÓLICA Y BICICLO DE KREBS-HENSELEIT (Y < 2160)
    # -------------------------------------------------------------------------

    # 5. L-Citrulina en Citosol
    partes.append(nodo_libre(
        x_u_c - 22, 1865,
        "L-Citrulina (Citosol)", "6C",
        UREA_CITRULINA, "m_u_citrulina_cito",
        text_right=True, dx=160,
        detalle="Recibida por SLC25A13 para condensación"
    ))

    # 6. BICICLO DE KREBS-HENSELEIT EN CARRIL IZQUIERDO (Fumarato ➔ L-Malato ➔ OAA ➔ L-Aspartato)
    # 6A. Fumarato libre resultante de ASL (X=4040, Y=1130)
    partes.append(nodo_libre(
        x_u_l - 60, 1130,
        "Fumarato", "4C",
        UREA_FUMARATO, "m_u_fumarato",
        text_right=False, dx=-20,
        detalle="Subproducto de escisión trans (ASL)"
    ))

    # Paso 1 del Biciclo: Fumarasa Citosólica (Fumarato + H2O ➔ L-Malato)
    partes.append(f'''
    <g id="rx_u_biciclo_fumarasa" data-arrastrable="1" transform="translate({x_u_l - 15}, 1248)">
      <line x1="0" y1="0" x2="0" y2="38" stroke="#ea580c" stroke-width="2.4" stroke-dasharray="6 3" marker-end="url(#arrowFlow)"/>
      <text x="14" y="16" fill="#c2410c" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">BICICLO: Fumarasa Citosólica</text>
      <text x="14" y="28" fill="#0284c7" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">+ H₂O (Hidratación)</text>
    </g>
    ''')

    # 6B. Intermediario 1 del Biciclo: L-Malato (Citosol) [4C]
    partes.append(nodo_libre(
        x_u_l - 60, 1295,
        "L-Malato (Biciclo)", "4C",
        GLUCONEO_MALATO, "m_u_malato_biciclo",
        text_right=False, dx=-20,
        detalle="Intermediario citosólico"
    ))

    # Paso 2 del Biciclo: MDH1 Citosólica (L-Malato + NAD+ ➔ OAA + NADH)
    partes.append(f'''
    <g id="rx_u_biciclo_mdh1" data-arrastrable="1" transform="translate({x_u_l - 15}, 1415)">
      <line x1="0" y1="0" x2="0" y2="38" stroke="#ea580c" stroke-width="2.4" stroke-dasharray="6 3" marker-end="url(#arrowFlow)"/>
      <text x="14" y="16" fill="#c2410c" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">MDH1 (Malato DH Citosólica)</text>
      <text x="14" y="28" fill="#059669" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">+ NAD⁺ ➔ + NADH + H⁺</text>
    </g>
    ''')

    # 6C. Intermediario 2 del Biciclo: Oxalacetato (Citosol) [4C]
    partes.append(nodo_libre(
        x_u_l - 60, 1465,
        "Oxalacetato (Biciclo)", "4C",
        GLUCONEO_OXALACETATO, "m_u_oaa_biciclo",
        text_right=False, dx=-20,
        detalle="Aceptor de grupo amino"
    ))

    # Paso 3 del Biciclo: AST / GOT1 Citosólica (OAA + L-Glutamato ➔ L-Aspartato + α-KG)
    partes.append(f'''
    <g id="rx_u_biciclo_got1" data-arrastrable="1" transform="translate({x_u_l - 15}, 1585)">
      <line x1="0" y1="0" x2="0" y2="38" stroke="#0d9488" stroke-width="2.4" stroke-dasharray="6 3" marker-end="url(#arrowTeal)"/>
      <text x="14" y="16" fill="#0f766e" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">AST / GOT1 (PLP)</text>
      <text x="14" y="28" fill="#2563eb" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">+ L-Glutamato ➔ + α-KG</text>
    </g>
    ''')

    # 6D. Donador lateral de nitrógeno: L-Aspartato (regenerado por el Biciclo y por Aralar)
    partes.append(nodo_libre(
        x_u_l - 60, 1635,
        "L-Aspartato", "4C",
        UREA_ASPARTATO, "m_u_aspartato",
        text_right=False, dx=-20,
        detalle="Aporta el 2º nitrógeno de la urea"
    ))

    # Reacción 3: ASS (Argininosuccinato Sintetasa)
    partes.append(f'''
    <g id="rx_u_ass" data-arrastrable="1" transform="translate({x_u_c}, 1610)">
      <!-- Flecha ascendente desde Citrulina -->
      <line x1="0" y1="240" x2="0" y2="-10" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de L-Aspartato desde el Biciclo de Krebs en el carril izquierdo -->
      <path d="M -275 115 Q -120 95 -4 25" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de 1 ATP (lado derecho) -->
      <path d="M 65 65 Q 25 65 4 45" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="70" y="68" fill="#dc2626" font-size="11" font-weight="800" font-family="'Inter', sans-serif">- 1 ATP</text>

      <!-- Salida de AMP + PPi (lado derecho) -->
      <path d="M 4 15 Q 25 5 65 5" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="70" y="9" fill="#475569" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">+ AMP + PPi (➔ 2 Pi)</text>

      <!-- Metadatos de ASS -->
      <g transform="translate(-18, -12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Argininosuccinato</text>
        <text x="0" y="13" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Sintetasa (ASS1)</text>
        <text x="0" y="26" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 6.3.4.5 (Citosólica)</text>
        <text x="0" y="38" fill="#15803d" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">Intermedio Citrulil-AMP activado</text>
      </g>
    </g>
    ''')

    # 7. L-Argininosuccinato (10C) - Intermediario que une ambos nitrógenos
    partes.append(nodo_libre(
        x_u_c - 50, 1330,
        "L-Argininosuccinato", "10C",
        UREA_ARGININOSUCCINATO, "m_u_argininosuccinato",
        text_right=True, dx=165,
        detalle="Condensado Citrulina-Aspartato"
    ))

    # Reacción 4: ASL (Argininosuccinato Liasa)
    partes.append(f'''
    <g id="rx_u_asl" data-arrastrable="1" transform="translate({x_u_c}, 1190)">
      <!-- Flecha vertical ascendente hacia Arginina -->
      <line x1="0" y1="100" x2="0" y2="-10" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Salida lateral hacia la IZQUIERDA de FUMARATO -->
      <path d="M -4 45 Q -80 45 -180 45" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      <text x="-110" y="25" fill="#c2410c" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">⮜ + Fumarato (4C)</text>

      <!-- Metadatos de la ASL -->
      <g transform="translate(18, 15)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif">Argininosuccinato Liasa (ASL)</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">EC 4.3.2.1 (Eliminación trans)</text>
        <text x="0" y="25" fill="#be185d" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Escisión del esqueleto de 4C</text>
      </g>
    </g>
    ''')

    # 9. L-Arginina (6C) (carril central, X=4420, Y=1160)
    partes.append(nodo_libre(
        x_u_c - 40, 1010,
        "L-Arginina", "6C",
        UREA_ARGININA, "m_u_arginina",
        text_right=True, dx=145,
        detalle="Grupo guanidino cargado"
    ))

    # Reacción 5: Arginasa 1 (ARG1) - Bifurcación hacia Urea y Ornitina
    partes.append(f'''
    <g id="rx_u_arg1" data-arrastrable="1" transform="translate({x_u_c}, 830)">
      <!-- Entrada de Agua para la hidrólisis -->
      <path d="M -75 35 Q -25 35 -4 50" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="-80" y="38" fill="#0284c7" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">+ H₂O</text>

      <!-- Flecha vertical hacia UREA -->
      <line x1="0" y1="120" x2="0" y2="-90" stroke="#dc2626" stroke-width="2.8" marker-end="url(#arrowRed)"/>

      <!-- Flecha horizontal hacia L-Ornitina citosólica (X=4570) -->
      <path d="M 0 50 L 148 50" fill="none" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowTeal)"/>
      <text x="74" y="40" fill="#0f766e" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">+ L-Ornitina</text>

      <!-- Metadatos de ARG1 (lado izquierdo) -->
      <g transform="translate(-20, -10)">
        <text x="0" y="-15" fill="#0f172a" font-size="12.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Arginasa 1 (ARG1)</text>
        <text x="0" y="-2" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 3.5.3.1 (Mn²⁺)</text>
        <text x="0" y="11" fill="#15803d" font-size="9.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">Hidrólisis terminal hepática</text>
      </g>
    </g>
    ''')

    # 10. L-Ornitina Citosólica (Regenerada, X=4700, Y=960)
    partes.append(nodo_libre(
        4570, 810,
        "L-Ornitina (Citosol)", "5C",
        UREA_ORNITINA, "m_u_ornitina_cito",
        text_right=True, dx=110,
        detalle="Regenerada tras hidrólisis"
    ))

    # Canal de retorno de Ornitina hacia ORNT1
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="canal_retorno_ornitina" data-arrastrable="1">
          <path d="M {x_u_r} 910 L {x_u_r} 2140" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-dasharray="8 5" marker-end="url(#arrowBlueAmino)"/>
          <path d="M {x_u_r} 2180 L {x_u_r} 2850" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-dasharray="8 5" marker-end="url(#arrowBlueAmino)"/>
          <g transform="translate({x_u_r}, 1600)">
            <rect x="-85" y="-12" width="170" height="24" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.2"/>
            <text x="0" y="4" fill="#1d4ed8" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">↓ ORNT1 (SLC25A15)</text>
          </g>
        </g>
        ''')

    # 11. UREA (Carbamida) - Producto final de desecho (X=4420, Y=780)
    partes.append(nodo_libre(
        x_u_c - 30, 630,
        "UREA (Carbamida)", "1C",
        UREA_MOL, "m_u_urea",
        text_right=True, dx=110,
        detalle="Diamida neutra no tóxica (2 nitrógenos)"
    ))

    # 12. Excreción directa de Urea al torrente sanguíneo superior
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="excrecion_urea_sangre" data-arrastrable="1">
          <path d="M {x_u_c} 600 L {x_u_c} 74" fill="none" stroke="#dc2626" stroke-width="3.2" stroke-dasharray="8 4" marker-end="url(#arrowRed)"/>
          <text x="{x_u_c + 18}" y="380" fill="#b91c1c" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 {x_u_c + 18} 380)">➔ EXCRECIÓN DE UREA AL TORRENTE SANGUÍNEO HEPÁTICO (➔ RIÑÓN)</text>

          <!-- Biomarcador vascular en el capilar superior -->
          <ellipse cx="{x_u_c}" cy="38" rx="26" ry="16" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
          <text x="{x_u_c}" y="42" fill="#dc2626" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">UREA</text>
          <text x="{x_u_c}" y="60" fill="#fca5a5" font-size="7.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Excreción</text>
        </g>
        ''')

    partes.append(f'</g>')

    # =========================================================================
    # 15. RUTA 15: BIOSÍNTESIS DE NUCLEÓTIDOS (PURINAS Y PIRIMIDINAS)
    # =========================================================================
    partes.append(f'<g id="ruta_sintesis_nucleotidos">')
    
    x_nuc = 5120
    partes.append(badge_via(15, x_nuc - 40, 185))
    partes.append(f'''
    <g transform="translate({x_nuc}, 185)" data-arrastrable="1">
      <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="900" font-family="'Inter', sans-serif">BIOSÍNTESIS DE NUCLEÓTIDOS (DE NOVO Y SALVAMENTO)</text>
      <text x="0" y="16" fill="#0284c7" font-size="11" font-weight="800" font-family="'Inter', sans-serif">Rutas convergentes sobre PRPP • Purinas (IMP) y Pirimidinas (UMP)</text>
    </g>
    ''')

    # Enlace hacia Pentosas y nodo precursor Ribosa-5-P antes de PRPP Sintetasa
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="conexion_pentosas_prpp" data-arrastrable="1">
          <path d="M 2560 880 C 3600 700, 4600 245, 5080 245" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
        </g>
        ''')
    partes.append(f'''
    <g id="m_nuc_r5p_in" data-arrastrable="1" transform="translate({x_nuc + 45}, 228)">
      <rect x="0" y="0" width="250" height="24" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
      <text x="125" y="16" fill="#047857" font-size="10" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">Ribosa-5-Fosfato [5C] (de Vía Pentosas)</text>
    </g>
    ''')

    # Paso 0: PRPP Sintetasa (Ribosa-5-P + ATP ➔ PRPP + AMP)
    partes.append(reaccion_libre(x_nuc + 130, 260, 38, "PRPP Sintetasa (PRS1)", entra="- 1 ATP", sale="+ 1 AMP", id_rx="rx_prpps"))
    partes.append(etiqueta_regulacion("prpp_s", x_nuc + 295, 266, dx=0, dy=0))

    # 1. PRPP (5-Fosforribosil-1-Pirofosfato)
    partes.append(nodo_libre(x_nuc + 80, 315, "PRPP", "5C", PRPP, "m_nuc_prpp", dx=165, detalle="5-Fosforribosil-1-Pirofosfato"))

    # Paso 1 comprometido de Purinas: PRPP Amidotransferasa (GPAT)
    partes.append(reaccion_libre(x_nuc + 130, 430, 38, "PRPP Amidotransferasa (GPAT)", entra="+ Gln + H₂O", sale="+ Glu + PPi", id_rx="rx_prppat"))
    partes.append(etiqueta_regulacion("prpp_at", x_nuc + 335, 436, dx=0, dy=0))

    # 1B. Intermediario comprometido: 5-Fosforribosilamina (5-PRA)
    partes.append(nodo_libre(x_nuc + 80, 485, "5-Fosforribosilamina (5-PRA)", "5C", NUC_5_PRA, "m_nuc_5pra", dx=140, detalle="1ᵉʳ intermediario purínico (N9)"))

    # Ensamblaje de los 9 pasos hacia IMP (GAR ➔ FGAR ➔ AIR ➔ AICAR ➔ FAICAR ➔ IMP)
    partes.append(reaccion_libre(x_nuc + 130, 590, 38, "Ensamblaje Purínico (9 pasos: GAR ➔ FAICAR)", entra="+ Gly, +2 Formil-THF", sale="+ Gln, +Asp, +CO₂", id_rx="rx_pur_9pasos"))

    # 2. IMP (Inosina Monofosfato - Bifurcación purínica)
    partes.append(nodo_libre(x_nuc + 80, 645, "Inosina Monofosfato (IMP)", "Base Hipoxantina", IMP, "m_nuc_imp", dx=120, detalle="Punto de ramificación purínica"))

    # 3. Bifurcación hacia AMP (izquierda) y GMP (derecha)
    partes.append(f'''
    <path d="M {x_nuc + 90} 770 Q {x_nuc} 795 {x_nuc - 20} 820" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc - 25}" y="795" fill="#0f172a" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">AdSS (+Asp, +GTP) ➔ AdSL</text>
    ''')
    partes.append(nodo_libre(x_nuc - 110, 825, "AMP (Adenosina-5'-P)", "Adenina", NUC_AMP, "m_nuc_amp", text_right=False, dx=-55, detalle="➔ ATP (Energía / ARN)"))

    partes.append(f'''
    <path d="M {x_nuc + 170} 770 Q {x_nuc + 260} 795 {x_nuc + 280} 820" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc + 285}" y="795" fill="#0f172a" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">IMPDH (+NAD⁺) ➔ GMPS (+Gln, +ATP)</text>
    ''')
    partes.append(nodo_libre(x_nuc + 220, 825, "GMP (Guanosina-5'-P)", "Guanina", NUC_GMP, "m_nuc_gmp", text_right=True, dx=115, detalle="➔ GTP (Señalización / ARN)"))

    # 4. Rama Pirimidinas (Síntesis de novo del anillo antes de unir PRPP)
    y_pir = 980
    partes.append(f'''
    <g id="m_nuc_pir_sustratos" data-arrastrable="1" transform="translate({x_nuc - 50}, {y_pir - 38})">
      <rect x="0" y="0" width="235" height="24" rx="8" fill="#eff6ff" stroke="#0284c7" stroke-width="1.5"/>
      <text x="117" y="16" fill="#0369a1" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">HCO₃⁻ + L-Glutamina + 2 ATP (Citosol)</text>
    </g>
    ''')
    partes.append(reaccion_libre(x_nuc + 50, y_pir - 6, 38, "CPS-II Citosólica (CAD)", entra="2 ATP + Gln", sale="2 ADP + Glu", id_rx="rx_cps2"))
    partes.append(etiqueta_regulacion("cps2", x_nuc + 275, y_pir, dx=0, dy=0))
    partes.append(nodo_libre(x_nuc - 50, y_pir + 45, "Carbamoil-Fosfato", "1C • Citosol", NUC_CARBAMOIL_P, "m_nuc_cp", dx=115, detalle="Precursor pirimidínico citosólico"))

    partes.append(reaccion_libre(x_nuc + 50, y_pir + 115, 38, "ATCasa + Dihidroorotasa", entra="+ L-Aspartato", sale="- Pi - H₂O", id_rx="rx_atcasa"))
    partes.append(etiqueta_regulacion("atcasa", x_nuc + 275, y_pir + 121, dx=0, dy=0))
    partes.append(nodo_libre(x_nuc - 50, y_pir + 168, "L-Dihidroorotato (DHO)", "4C • Vía Carbamoil-Asp", NUC_DHO, "m_nuc_dho", dx=115, detalle="Sustrato de DHODH mitocondrial"))

    partes.append(reaccion_libre(x_nuc + 50, y_pir + 260, 38, "Dihidroorotato DH (DHODH • MMI)", entra="+ CoQ (MMI)", sale="+ CoQH₂ (➔ CTE)", es_ganancia=True, id_rx="rx_dhodh"))
    partes.append(nodo_libre(x_nuc - 50, y_pir + 312, "Ácido Orotato", "Anillo Pirimidina", NUC_OROTATO, "m_nuc_orotato", dx=115, detalle="Acoplado a CoQ en cara externa MMI"))

    partes.append(reaccion_libre(x_nuc + 50, y_pir + 402, 38, "UMP Sintasa (OPRT + ODC)", entra="+ PRPP", sale="- PPi - CO₂", id_rx="rx_umps"))
    partes.append(nodo_libre(x_nuc - 50, y_pir + 455, "UMP (Uridina Monofosfato)", "Uracilo", NUC_UMP, "m_nuc_ump", dx=115, detalle="Precursor común pirimidinas"))

    # Bifurcación UMP ➔ CTP y dTMP
    partes.append(f'''
    <path d="M {x_nuc - 37} {y_pir + 568} Q {x_nuc - 51} {y_pir + 582} {x_nuc - 60} {y_pir + 595}" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc - 70}" y="{y_pir + 572}" fill="#0f172a" font-size="10" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">CTP Sintetasa (+Gln, -ATP)</text>
    ''')
    partes.append(nodo_libre(x_nuc - 140, y_pir + 605, "CTP (Citidina-5'-P)", "Citosina", NUC_CTP, "m_nuc_ctp", text_right=False, dx=-55, detalle="Precursor de ARN / Lípidos"))

    partes.append(f'''
    <path d="M {x_nuc + 120} {y_pir + 545} Q {x_nuc + 160} {y_pir + 572} {x_nuc + 180} {y_pir + 595}" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc + 190}" y="{y_pir + 572}" fill="#0f172a" font-size="10" font-weight="700" font-family="'Inter', sans-serif">RNR ➔ Timidilato Sintasa (N⁵,N¹⁰-CH₂-THF)</text>
    ''')
    partes.append(nodo_libre(x_nuc + 130, y_pir + 605, "dTMP (Timidilato)", "Timina [ADN]", NUC_DTMP, "m_nuc_dtmp", text_right=True, dx=145, detalle="Diana 5-FU y Metotrexato"))
    partes.append(etiqueta_regulacion("ts", x_nuc + 280, y_pir + 675, dx=0, dy=0))

    partes.append(f'</g>')

    # =========================================================================
    # 16. RUTA 16: CATABOLISMO DE NUCLEÓTIDOS Y ÁCIDO ÚRICO
    # =========================================================================
    partes.append(f'<g id="ruta_degradacion_nucleotidos">')
    
    y_deg = 1765
    partes.append(badge_via(16, x_nuc - 40, y_deg))
    partes.append(f'''
    <g transform="translate({x_nuc}, {y_deg})" data-arrastrable="1">
      <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="900" font-family="'Inter', sans-serif">CATABOLISMO DE NUCLEÓTIDOS Y ÁCIDO ÚRICO</text>
      <text x="0" y="16" fill="#dc2626" font-size="11" font-weight="800" font-family="'Inter', sans-serif">Convergencia en XOD ➔ Ácido Úrico (Gota) y Apertura Soluble (β-Alanina)</text>
    </g>
    ''')

    # Degradación de Purinas: Hipoxantina ➔ Xantina ➔ Ácido Úrico
    partes.append(nodo_libre(x_nuc + 30, y_deg + 55, "Hipoxantina (de AMP)", "Purina", HIPOXANTINA, "m_deg_hipo", dx=115, detalle="Vía ADA (diana SCID) y PNP"))
    partes.append(etiqueta_regulacion("ada", x_nuc + 160, y_deg + 120, dx=0, dy=0))

    partes.append(reaccion_libre(x_nuc + 80, y_deg + 145, 42, "XOD (Paso 1)", entra="+ O₂ + H₂O", sale="+ H₂O₂", id_rx="rx_xod1"))
    partes.append(nodo_libre(x_nuc + 30, y_deg + 202, "Xantina", "Dioxipurina", XANTINA, "m_deg_xantina", dx=115, detalle="Convergencia de Adenina y Guanina (Guanasa)"))

    partes.append(reaccion_libre(x_nuc + 80, y_deg + 288, 42, "XOD (Paso 2 · Alopurinol)", entra="+ O₂ + H₂O", sale="+ H₂O₂", id_rx="rx_xod2"))
    partes.append(etiqueta_regulacion("xod", x_nuc + 270, y_deg + 296, dx=0, dy=0))
    partes.append(nodo_libre(x_nuc + 30, y_deg + 350, "ÁCIDO ÚRICO (URATO)", "Trioxipurina", ACIDO_URICO, "m_deg_urato", dx=115, detalle="Poco soluble · Precipita en gota"))

    # Trazo de excreción renal de Urato hacia el torrente vascular capilar superior
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="excrecion_urato_sangre" data-arrastrable="1">
          <path d="M {x_nuc + 120} {y_deg + 350} C {x_nuc + 380} {y_deg + 180}, {x_nuc + 480} 500, {x_nuc + 480} 74" fill="none" stroke="#dc2626" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowRed)"/>
        </g>
        ''')
    partes.append(f'''
    <g id="indicador_urato_excrecion" transform="translate({x_nuc + 160}, {y_deg + 350})">
      <path d="M 0 0 Q 70 -30 110 -30" fill="none" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
      <text x="120" y="-26" fill="#dc2626" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">➔ Excreción renal de Urato (URAT1) / Hiperuricemia</text>
    </g>
    <!-- Biomarcador vascular de Urato en torrente capilar superior -->
    <g transform="translate(5550, 38)">
      <ellipse cx="0" cy="0" rx="28" ry="16" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
      <text x="0" y="4" fill="#dc2626" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">URATO</text>
      <text x="0" y="19" fill="#fca5a5" font-size="7" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Filtro Renal</text>
    </g>
    ''')

    # Degradación de Pirimidinas (con intermediario Dihidrouracilo y apertura soluble)
    y_deg_pir = y_deg + 495
    partes.append(nodo_libre(x_nuc + 30, y_deg_pir, "Uracilo / Citosina", "Pirimidina libre", DEG_URACILO, "m_deg_uracilo", dx=115, detalle="Sustrato de DPD (NADPH)"))
    partes.append(reaccion_libre(x_nuc + 80, y_deg_pir + 68, 38, "Dihidropirimidina DH (DPD)", entra="+ NADPH", sale="+ NADP⁺", id_rx="rx_dpd"))

    partes.append(nodo_libre(x_nuc + 30, y_deg_pir + 128, "Dihidrouracilo (DHU)", "4C • Anillo saturado", DEG_DIHIDROURACILO, "m_deg_dhu", dx=115, detalle="Reducción C5=C6 completada"))
    partes.append(reaccion_libre(x_nuc + 80, y_deg_pir + 198, 38, "DHPasa (Apertura hidrolítica)", entra="+ H₂O", id_rx="rx_dhpasa"))

    partes.append(nodo_libre(x_nuc + 30, y_deg_pir + 250, "β-Ureidopropionato", "Cadena abierta acíclica", BETA_UREIDOPROPIONATO, "m_deg_ureido", dx=175, detalle="Apertura hidrolítica del anillo"))
    partes.append(reaccion_libre(x_nuc + 80, y_deg_pir + 318, 38, "β-Ureidopropionasa", entra="+ H₂O", sale="+ NH₄⁺ + CO₂", id_rx="rx_ureidopropionasa"))
    partes.append(nodo_libre(x_nuc + 30, y_deg_pir + 370, "β-Alanina Soluble", "Producto soluble", BETA_ALANINA, "m_deg_beta_ala", dx=120, detalle="Excreción inocua en orina"))

    partes.append(f'</g>')

    # =========================================================================
    # 17. RUTA 8B: LANZADERA DE GLICEROL-3-FOSFATO (G-3-P / DHAP) - LUPA ANATÓMICA
    # =========================================================================
    partes.append(f'<g id="lupa_lanzadera_glicerol_p" data-arrastrable="1">')
    
    y_lanz = 2950
    x_g3p_marco = 4980
    y_g3p_marco = y_lanz - 25
    w_g3p_marco = 810
    h_g3p_marco = 440

    # 1. Bisel y Marco Panorámico de Zoom para Lanzadera Glicerol-P
    partes.append(f'''
    <rect x="{x_g3p_marco - 5}" y="{y_g3p_marco - 5}" width="{w_g3p_marco + 10}" height="{h_g3p_marco + 10}" rx="24" fill="#ffffff" stroke="#ea580c" stroke-width="4"/>
    <rect x="{x_g3p_marco}" y="{y_g3p_marco}" width="{w_g3p_marco}" height="{h_g3p_marco}" rx="20" fill="#ffffff" stroke="#fb923c" stroke-width="1.8" stroke-dasharray="8 4"/>

    <!-- ClipPath para recortar el interior del marco de la lupa -->
    <defs>
      <clipPath id="clipLupaG3P">
        <rect x="{x_g3p_marco}" y="{y_g3p_marco}" width="{w_g3p_marco}" height="{h_g3p_marco}" rx="20"/>
      </clipPath>
    </defs>

    <!-- 2. Estratificación Biológica de Compartimentos Celulares -->
    <g clip-path="url(#clipLupaG3P)">
      <!-- Zona 1: Citosol Celular -->
      <rect x="{x_g3p_marco}" y="{y_g3p_marco}" width="390" height="{h_g3p_marco}" fill="#f8fafc"/>

      <!-- Zona 2: Membrana Mitocondrial Externa (MME con VDAC) -->
      <rect x="{x_g3p_marco + 390}" y="{y_g3p_marco}" width="80" height="{h_g3p_marco}" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.4"/>

      <!-- Zona 3: Espacio Intermembrana (EIM) -->
      <rect x="{x_g3p_marco + 470}" y="{y_g3p_marco}" width="70" height="{h_g3p_marco}" fill="#fff7ed" stroke="#fed7aa" stroke-width="1" stroke-dasharray="4 2"/>

      <!-- Zona 4: Membrana Mitocondrial Interna (MMI) - Cara Externa -->
      <rect x="{x_g3p_marco + 540}" y="{y_g3p_marco}" width="{w_g3p_marco - 540}" height="{h_g3p_marco}" fill="#fef3c7" fill-opacity="0.5" stroke="#ea580c" stroke-width="2"/>

      <!-- Rótulos de Compartimentos en la Cabecera Interna -->
      <g opacity="0.85">
        <text x="{x_g3p_marco + 195}" y="{y_g3p_marco + 20}" fill="#64748b" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="1">CITOSOL CELULAR</text>
        <text x="{x_g3p_marco + 430}" y="{y_g3p_marco + 20}" fill="#475569" font-size="8.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="0.5">MME</text>
        <text x="{x_g3p_marco + 505}" y="{y_g3p_marco + 20}" fill="#c2410c" font-size="8.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="0.5">EIM</text>
        <text x="{x_g3p_marco + 675}" y="{y_g3p_marco + 20}" fill="#9a3412" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="1">MMI (CARA EXTERNA)</text>
      </g>
    </g>
    ''')

    partes.append(badge_via("8B", x_nuc - 35, y_lanz + 15))
    partes.append(f'''
    <g transform="translate({x_nuc + 5}, {y_lanz + 15})" data-arrastrable="1">
      <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="900" font-family="'Inter', sans-serif">LANZADERA DE GLICEROL-3-FOSFATO (VÍA 8B)</text>
      <text x="0" y="15" fill="#ea580c" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">Inserto Anatómico de Envoltura Mitocondrial • Reoxidación de NADH (1.5 ATP)</text>
    </g>
    ''')

    # Enlace hacia Glucólisis
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="conexion_glucolisis_lanz_g3p" data-arrastrable="1">
          <path d="M 1430 920 C 1430 1800, 4800 3050, 5120 3050" fill="none" stroke="#ea580c" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowFlow)"/>
        </g>
        ''')
    partes.append(f'''
    <text x="{x_nuc + 20}" y="{y_lanz + 55}" fill="#ea580c" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">➔ de DHAP (Glucólisis Citosólica)</text>
    ''')

    partes.append(nodo_libre(x_nuc + 20, y_lanz + 70, "Dihidroxiacetona-P (DHAP)", "3C", DIHIDROXIACETONA_FOSFATO, "m_lanz_dhap", dx=120, detalle="Aceptor citosólico de electrones"))
    partes.append(reaccion_libre(x_nuc + 75, y_lanz + 185, 45, "cGPDH Citosólica (GPD1)", entra="- NADH + H⁺", sale="+ NAD⁺ (Regenerado)", id_rx="rx_cgpdh"))
    partes.append(nodo_libre(x_nuc + 20, y_lanz + 250, "L-Glicerol-3-Fosfato", "3C", LANZ_G3P, "m_lanz_g3p", dx=100, detalle="Transporta electrones a la MMI"))

    # Cruce VDAC y mGPDH flavoproteína
    partes.append(f'''
    <g id="lanz_mgpdh_mmi" transform="translate({x_nuc + 260}, {y_lanz + 150})" data-arrastrable="1">
      <!-- Porina VDAC en MME -->
      <g transform="translate(10, 42)">
        <rect x="0" y="0" width="46" height="34" rx="7" fill="#cbd5e1" stroke="#475569" stroke-width="1.8"/>
        <text x="23" y="15" fill="#1e293b" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">VDAC</text>
        <text x="23" y="27" fill="#475569" font-size="7.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">Porina MME</text>
      </g>

      <!-- Proteína integral mGPDH anclada a MMI -->
      <g transform="translate(75, 30)">
        <path d="M 0,0 Q 40,-15 50,40 Q 55,90 15,80 Q 0,55 0,25 Z" fill="#fed7aa" stroke="#c2410c" stroke-width="2"/>
        <circle cx="20" cy="40" r="10" fill="#ffedd5" stroke="#ea580c" stroke-width="1.6"/>
        <text x="20" y="43" fill="#9a3412" font-size="7.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">FAD</text>
        <text x="56" y="20" fill="#0f172a" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">mGPDH (GPD2)</text>
        <text x="56" y="32" fill="#9a3412" font-size="8" font-weight="800" font-family="'Inter', sans-serif">Flavoproteína</text>
      </g>

      <!-- Flujo de G-3-P a mGPDH (pasa limpio por debajo de VDAC) -->
      <path d="M 15 110 C 35 110, 55 98, 75 75" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>

      <!-- Retorno de DHAP al citosol (pasa limpio por encima de VDAC) -->
      <path d="M 75 14 C 45 8, 15 8, -15 8" fill="none" stroke="#ea580c" stroke-width="2.2" stroke-dasharray="5 3" marker-end="url(#arrowFlow)"/>
      <text x="30" y="2" fill="#64748b" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Retorno DHAP ➔ Citosol</text>

      <!-- Coenzima Q y Complejo III -->
      <path d="M 135 70 Q 165 70 195 70" fill="none" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arrowBlue)"/>
      <g transform="translate(204, 54)">
        <rect x="0" y="0" width="76" height="30" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
        <text x="38" y="13" fill="#0369a1" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">CoQ ➔ CoQH₂</text>
        <text x="38" y="23" fill="#0284c7" font-size="7" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">Ubiquinona</text>
      </g>
      <path d="M 284 69 L 298 69" fill="none" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arrowBlue)"/>
      <g transform="translate(302, 54)">
        <rect x="0" y="0" width="84" height="30" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
        <text x="42" y="13" fill="#15803d" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">COMPLEJO III</text>
        <text x="42" y="23" fill="#16a34a" font-size="7" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">➔ 1.5 ATP neto</text>
      </g>
    </g>
    ''')

    partes.append(f'</g>')

    # 14. BLOQUE INSTITUCIONAL Y AUTORÍA DE CÓDIGO ABIERTO
    partes.append(generar_bloque_leyenda(100, 4220))
    partes.append(generar_bloque_autoria(3800, 4220))
    partes.append('</g> <!-- Fin entorno_hepatocito -->')

    # Defs y Marcadores
    defs_svg = f"""
    <defs>
      <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
      </marker>
      <marker id="arrowTeal" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#0d9488" />
      </marker>
      <marker id="arrowBlueAmino" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#2563eb" />
      </marker>
      <marker id="arrowCobalt" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#1d4ed8" />
      </marker>
      <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
        <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
      </marker>
      <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
        <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
      </marker>
      <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
        <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
      </marker>
      <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
        <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
      </marker>
      <marker id="arrowPurple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
      </marker>
      <marker id="arrowAmber" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#b45309" />
      </marker>

      <linearGradient id="gradMiocitoCori" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#fff1f2" stop-opacity="0.95" />
        <stop offset="100%" stop-color="#ffe4e6" stop-opacity="0.9" />
      </linearGradient>

      <!-- Gradientes histológicos anatómicos del músculo esquelético -->
      <linearGradient id="gradVientreMuscular" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#fff1f2" stop-opacity="0.96" />
        <stop offset="30%" stop-color="#ffe4e6" stop-opacity="0.92" />
        <stop offset="70%" stop-color="#fecdd3" stop-opacity="0.88" />
        <stop offset="100%" stop-color="#fda4af" stop-opacity="0.82" />
      </linearGradient>

      <linearGradient id="gradFasciaTendinosa" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#f1f5f9" stop-opacity="0.95"/>
        <stop offset="45%" stop-color="#e2e8f0" stop-opacity="0.9"/>
        <stop offset="100%" stop-color="#fff1f2" stop-opacity="0.1"/>
      </linearGradient>

      <linearGradient id="gradSarcoplasma" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#fff5f5" stop-opacity="0.95" />
        <stop offset="50%" stop-color="#ffe4e6" stop-opacity="0.75" />
        <stop offset="100%" stop-color="#fff1f2" stop-opacity="0.95" />
      </linearGradient>

      <linearGradient id="gradCapilarMuscular" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#7f1d1d" stop-opacity="0.9" />
        <stop offset="50%" stop-color="#991b1b" stop-opacity="0.8" />
        <stop offset="100%" stop-color="#b91c1c" stop-opacity="0.85" />
      </linearGradient>

      <linearGradient id="gradHeaderAutoria" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#0284c7" />
        <stop offset="50%" stop-color="#0d9488" />
        <stop offset="100%" stop-color="#10b981" />
      </linearGradient>

      <filter id="shadowCard" x="-5%" y="-5%" width="110%" height="115%">
        <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0f172a" flood-opacity="0.12" />
      </filter>

      <linearGradient id="gradCitosolUnificado" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
        <stop offset="15%" stop-color="#f1f5f9" stop-opacity="0.8" />
        <stop offset="50%" stop-color="#f8fafc" stop-opacity="0.6" />
        <stop offset="85%" stop-color="#f1f5f9" stop-opacity="0.75" />
        <stop offset="100%" stop-color="#f8fafc" stop-opacity="1" />
      </linearGradient>

      <radialGradient id="haloCitosolUnificado" cx="50%" cy="48%" r="72%">
        <stop offset="0%" stop-color="#e2e8f0" stop-opacity="0.22" />
        <stop offset="55%" stop-color="#f1f5f9" stop-opacity="0.10" />
        <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
      </radialGradient>

      <radialGradient id="gradMitocondria" cx="50%" cy="100%" r="90%">
        <stop offset="0%" stop-color="#fef3c7" stop-opacity="1" />
        <stop offset="45%" stop-color="#fffbeb" stop-opacity="0.95" />
        <stop offset="75%" stop-color="#fed7aa" stop-opacity="0.9" />
        <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.8" />
      </radialGradient>

      <linearGradient id="gradTorrenteSanguineo" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#7f1d1d" stop-opacity="0.95" />
        <stop offset="15%" stop-color="#991b1b" stop-opacity="0.9" />
        <stop offset="50%" stop-color="#b91c1c" stop-opacity="0.85" />
        <stop offset="85%" stop-color="#991b1b" stop-opacity="0.9" />
        <stop offset="100%" stop-color="#7f1d1d" stop-opacity="0.95" />
      </linearGradient>

      <linearGradient id="gradPlasmaSanguineo" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" stop-color="#450a0a" stop-opacity="0.95" />
        <stop offset="60%" stop-color="#7f1d1d" stop-opacity="0.88" />
        <stop offset="100%" stop-color="#991b1b" stop-opacity="0.82" />
      </linearGradient>

      <radialGradient id="gradEritrocito" cx="38%" cy="38%" r="62%">
        <stop offset="0%" stop-color="#ef4444" stop-opacity="0.95" />
        <stop offset="45%" stop-color="#dc2626" stop-opacity="0.9" />
        <stop offset="70%" stop-color="#b91c1c" stop-opacity="0.95" />
        <stop offset="100%" stop-color="#7f1d1d" stop-opacity="1" />
      </radialGradient>

      <radialGradient id="gradEritrocitoCentro" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stop-color="#7f1d1d" stop-opacity="0.8" />
        <stop offset="100%" stop-color="#ef4444" stop-opacity="0" />
      </radialGradient>

      <!-- Defs originales de la Cadena Transportadora de Electrones del usuario -->
      {cte_defs}
    </defs>
    """

    svg_completo = f"""<svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      {defs_svg}
      {''.join(partes)}
    </svg>"""

    html_out = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Prueba Visual Integrada — Entorno Celular Real (Sin Globos)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #0f172a;
      color: #f8fafc;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }}
    .header-bar {{
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1e293b;
      padding: 10px 24px;
      border-bottom: 1px solid #334155;
      z-index: 10;
    }}
    .controls {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .controls button {{
      background: #0284c7;
      color: #ffffff;
      border: none;
      padding: 6px 12px;
      border-radius: 6px;
      font-weight: 800;
      font-size: 0.82rem;
      cursor: pointer;
    }}
    .controls button:hover {{ background: #0369a1; }}
    #zoomLevel {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 800;
      color: #38bdf8;
      min-width: 52px;
      text-align: center;
    }}
    .viewport {{
      flex: 1;
      width: 100%;
      overflow: hidden;
      position: relative;
      cursor: grab;
      background: #1e293b;
    }}
    .viewport.grabbing {{ cursor: grabbing; }}
    #panLayer {{
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: 0 0;
      width: {ANCHO_CANVAS}px;
      height: {ALTO_CANVAS}px;
    }}
    svg {{ display: block; width: 100%; height: 100%; }}
  </style>
</head>
<body>
  <div class="header-bar">
    <div>
      <h2 style="color: #38bdf8; font-size: 1.1rem;">Entorno Celular: Citosol y Gran Mitocondria</h2>
      <p style="color: #94a3b8; font-size: 0.78rem;">Glucólisis • Glucógeno • Pentosas • Lanzadera • Krebs • Cadena Respiratoria • β-Oxidación • Cetogénesis</p>
    </div>
    <div class="controls">
      <button onclick="zoomOut()">−</button>
      <span id="zoomLevel">100%</span>
      <button onclick="zoomIn()">+</button>
      <button onclick="resetView()">Reset</button>
      <button style="background: #16a34a;" onclick="fitView()">Ajustar</button>
      <div style="width: 1px; height: 20px; background: #475569; margin: 0 4px;"></div>
      <button id="btnCopiarSvg" style="background: #7c3aed;" onclick="copiarSvgModificado()">💾 Copiar SVG</button>
      <button id="btnCopiarJson" style="background: #0284c7;" onclick="copiarAjustesJson()">📋 Copiar Ajustes JSON</button>
      <button style="background: #dc2626;" onclick="resetearPosiciones()">↺ Resetear Ajustes</button>
      <span id="statusStorage" style="font-size: 0.75rem; color: #a7f3d0; margin-left: 6px;"></span>
    </div>
  </div>
  <div class="viewport" id="viewport">
    <div id="panLayer">
      {svg_completo}
    </div>
  </div>

  <script>
    const viewport = document.getElementById('viewport');
    const panLayer = document.getElementById('panLayer');
    const zoomLevelEl = document.getElementById('zoomLevel');
    const statusStorage = document.getElementById('statusStorage');
    
    let scale = 1;
    let pointX = 0;
    let pointY = 0;
    let startX = 0;
    let startY = 0;
    let isPanning = false;

    // --- SISTEMA DE ARRASTRE Y PERSISTENCIA (localStorage) ---
    const STORAGE_KEY = 'mapa_metabolico_offsets_v1';
    let offsetsGuardados = {{}};
    try {{
      offsetsGuardados = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{{}}');
    }} catch (e) {{
      offsetsGuardados = {{}};
    }}

    let arrastrandoElemento = null;
    let dragStartX = 0;
    let dragStartY = 0;
    let elemOrigTx = 0;
    let elemOrigTy = 0;

    function parseTranslate(transformAttr) {{
      if (!transformAttr) return {{ x: 0, y: 0 }};
      const m = transformAttr.match(/translate\\(([-0-9.]+)[,\\s]+([-0-9.]+)\\)/);
      if (m) return {{ x: parseFloat(m[1]), y: parseFloat(m[2]) }};
      return {{ x: 0, y: 0 }};
    }}

    function aplicarOffsetsGuardados() {{
      let count = 0;
      for (const [id, offset] of Object.entries(offsetsGuardados)) {{
        const el = document.getElementById(id);
        if (el) {{
          if (!el.hasAttribute('data-base-transform')) {{
            el.setAttribute('data-base-transform', el.getAttribute('transform') || '');
          }}
          const baseTrans = el.getAttribute('data-base-transform');
          const base = parseTranslate(baseTrans);
          const finalX = base.x + offset.dx;
          const finalY = base.y + offset.dy;
          const otherTransforms = baseTrans.replace(/translate\\([ -0-9.,]+\\)/g, '').trim();
          el.setAttribute('transform', `translate(${{finalX}}, ${{finalY}}) ${{otherTransforms}}`.trim());
          count++;
        }}
      }}
      if (count > 0 && statusStorage) {{
        statusStorage.textContent = `✓ ${{count}} elementos restaurados`;
      }}
    }}

    function guardarOffset(id, dx, dy) {{
      offsetsGuardados[id] = {{ dx, dy }};
      localStorage.setItem(STORAGE_KEY, JSON.stringify(offsetsGuardados));
      const count = Object.keys(offsetsGuardados).length;
      if (statusStorage) statusStorage.textContent = `✓ Guardado (${{count}} movidos)`;
    }}

    function resetearPosiciones() {{
      if (confirm("¿Deseas resetear todas las posiciones manuales y volver al diseño original?")) {{
        localStorage.removeItem(STORAGE_KEY);
        offsetsGuardados = {{}};
        location.reload();
      }}
    }}

    function copiarAjustesJson() {{
      const dataStr = JSON.stringify(offsetsGuardados, null, 2);
      navigator.clipboard.writeText(dataStr).then(() => {{
        alert("¡Ajustes copiados al portapapeles en formato JSON! Puedes pegarlos en el chat.");
      }}).catch(() => {{
        prompt("Copia los ajustes JSON:", dataStr);
      }});
    }}

    function copiarSvgModificado() {{
      const svgEl = document.querySelector('#panLayer svg');
      if (!svgEl) return;
      const svgText = svgEl.outerHTML;
      navigator.clipboard.writeText(svgText).then(() => {{
        alert("¡SVG completo con tus posiciones exactas copiado al portapapeles!");
      }}).catch(() => {{
        alert("No se pudo copiar automáticamente. Puedes usar la consola del navegador.");
      }});
    }}

    function updateTransform() {{
      panLayer.style.transform = `translate(${{pointX}}px, ${{pointY}}px) scale(${{scale}})`;
      zoomLevelEl.textContent = `${{Math.round(scale * 100)}}%`;
    }}

    function zoom(delta, clientX, clientY) {{
      const rect = viewport.getBoundingClientRect();
      const cx = (clientX !== undefined ? clientX : rect.left + rect.width / 2) - rect.left;
      const cy = (clientY !== undefined ? clientY : rect.top + rect.height / 2) - rect.top;

      const prevScale = scale;
      scale *= delta;
      scale = Math.max(0.15, Math.min(scale, 5));

      pointX = cx - (cx - pointX) * (scale / prevScale);
      pointY = cy - (cy - pointY) * (scale / prevScale);
      updateTransform();
    }}

    function zoomIn() {{ zoom(1.25); }}
    function zoomOut() {{ zoom(0.8); }}
    
    function resetView() {{
      scale = 1;
      pointX = 0;
      pointY = 0;
      updateTransform();
    }}

    function fitView() {{
      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;
      scale = Math.min(vw / {ANCHO_CANVAS}, vh / {ALTO_CANVAS});
      pointX = (vw - {ANCHO_CANVAS} * scale) / 2;
      pointY = (vh - {ALTO_CANVAS} * scale) / 2;
      updateTransform();
    }}

    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const delta = e.deltaY < 0 ? 1.15 : 0.85;
      zoom(delta, e.clientX, e.clientY);
    }}, {{ passive: false }});

    viewport.addEventListener('mousedown', (e) => {{
      if (e.button !== 0) return;

      // Comprobar si el clic fue en un elemento arrastrable
      const arrastrable = e.target.closest('[data-arrastrable="1"]');
      if (arrastrable && arrastrable.id) {{
        arrastrandoElemento = arrastrable;
        dragStartX = e.clientX;
        dragStartY = e.clientY;

        if (!arrastrable.hasAttribute('data-base-transform')) {{
          arrastrable.setAttribute('data-base-transform', arrastrable.getAttribute('transform') || '');
        }}

        const baseTrans = arrastrable.getAttribute('data-base-transform');
        const base = parseTranslate(baseTrans);
        const currentOffset = offsetsGuardados[arrastrable.id] || {{ dx: 0, dy: 0 }};
        elemOrigTx = base.x + currentOffset.dx;
        elemOrigTy = base.y + currentOffset.dy;

        arrastrable.style.cursor = 'grabbing';
        e.stopPropagation();
        return;
      }}

      isPanning = true;
      startX = e.clientX - pointX;
      startY = e.clientY - pointY;
      viewport.classList.add('grabbing');
    }});

    window.addEventListener('mousemove', (e) => {{
      if (arrastrandoElemento) {{
        const dxScreen = e.clientX - dragStartX;
        const dyScreen = e.clientY - dragStartY;
        const dxSvg = dxScreen / scale;
        const dySvg = dyScreen / scale;

        const baseTrans = arrastrandoElemento.getAttribute('data-base-transform');
        const base = parseTranslate(baseTrans);
        const totalDx = (elemOrigTx - base.x) + dxSvg;
        const totalDy = (elemOrigTy - base.y) + dySvg;

        const finalX = base.x + totalDx;
        const finalY = base.y + totalDy;
        const otherTransforms = baseTrans.replace(/translate\\([ -0-9.,]+\\)/g, '').trim();
        arrastrandoElemento.setAttribute('transform', `translate(${{finalX}}, ${{finalY}}) ${{otherTransforms}}`.trim());
        return;
      }}

      if (!isPanning) return;
      pointX = e.clientX - startX;
      pointY = e.clientY - startY;
      updateTransform();
    }});

    window.addEventListener('mouseup', (e) => {{
      if (arrastrandoElemento) {{
        const dxScreen = e.clientX - dragStartX;
        const dyScreen = e.clientY - dragStartY;
        const dxSvg = dxScreen / scale;
        const dySvg = dyScreen / scale;

        const baseTrans = arrastrandoElemento.getAttribute('data-base-transform');
        const base = parseTranslate(baseTrans);
        const totalDx = Math.round((elemOrigTx - base.x) + dxSvg);
        const totalDy = Math.round((elemOrigTy - base.y) + dySvg);

        guardarOffset(arrastrandoElemento.id, totalDx, totalDy);
        arrastrandoElemento.style.cursor = '';
        arrastrandoElemento = null;
        return;
      }}

      isPanning = false;
      viewport.classList.remove('grabbing');
    }});

    // Ajustar vista y restaurar posiciones manuales al inicio
    window.addEventListener('load', () => {{
      fitView();
      aplicarOffsetsGuardados();
    }});
  </script>
</body>
</html>
"""
    return html_out, svg_completo

if __name__ == "__main__":
    html_str, svg_str = construir_mapa_organico()
    
    ruta_html = os.path.join(DIR_HTML, "prueba_visual_integrada.html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html_str)

    ruta_svg = os.path.join(DIR_HTML, "prueba_visual_integrada.svg")
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_str)

    print(f"Mapa Orgánico Celular generado en HTML: {ruta_html}")
    print(f"Mapa Orgánico Celular generado en SVG: {ruta_svg}")
