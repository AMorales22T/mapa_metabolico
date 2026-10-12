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
DIR_BASE = os.path.dirname(DIR_SCRIPT) if os.path.basename(DIR_SCRIPT) == "01_fuente_python" else DIR_SCRIPT
DIR_HTML = os.path.join(DIR_BASE, "02_versiones_html")
sys.path.append(os.path.join(DIR_BASE, "06_REGULACION_Y_LEYENDA"))
import regulacion

sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "02_gluconeogenesis"))
from estructuras_gluconeogenesis import (
    OXALACETATO as GLUCONEO_OXALACETATO,
    MALATO as GLUCONEO_MALATO,
    RE_GLUCOSA_6_FOSFATASA,
    LACTATO as GLUCONEO_LACTATO
)

sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "01_glucolisis"))
sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "03_glucogenogenesis_y_glucogenolisis"))
sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "04_via_pentosas_fosfato"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "01_complejo_piruvato_deshidrogenasa"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "02_ciclo_de_krebs"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "03_cadena_transporte_electrones_y_atp_sintasa"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "04_lanzaderas_malato_aspartato_y_glicerol_p"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "01_beta_oxidacion"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "02_sintesis_acidos_grasos_lipogenesis"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "03_cetogenesis_y_cetolisis"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "04_colesterol_y_lipoproteinas"))
sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "01_transaminacion_y_desaminacion"))
sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "02_ciclo_de_la_urea"))
sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "03_destinos_esqueletos_carbonados"))
sys.path.append(os.path.join(DIR_BASE, "05_NUCLEOTIDOS_Y_OTRAS", "01_sintesis_purinas_y_pirimidinas"))
sys.path.append(os.path.join(DIR_BASE, "05_NUCLEOTIDOS_Y_OTRAS", "02_degradacion_y_acido_urico"))
from estructuras_nucleotidos import (
    PRPP, IMP, AMP as NUC_AMP, GMP as NUC_GMP,
    CARBAMOIL_FOSFATO as NUC_CARBAMOIL_P,
    OROTATO as NUC_OROTATO, UMP as NUC_UMP, CTP as NUC_CTP, DTMP as NUC_DTMP
)
from estructuras_degradacion import (
    HIPOXANTINA, XANTINA, ACIDO_URICO, URACILO as DEG_URACILO,
    BETA_UREIDOPROPIONATO, BETA_ALANINA
)
from estructuras_lanzadera import (
    GLICEROL_3_FOSFATO as LANZ_G3P
)
from estructuras_destinos_aa import (
    FENILALANINA as AA_FENILALANINA,
    TIROSINA as AA_TIROSINA,
    PROPIONIL_COA as AA_PROPIONIL_COA,
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
    RIBOSA_5_FOSFATO, XILULOSA_5_FOSFATO, SEDOHEPTULOSA_7_FOSFATO, ERITROSA_4_FOSFATO
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
    MALONIL_COA, ACETOACETIL_ACP, D_BETA_HIDROXIACIL_ACP, BUTIRIL_ACP, PALMITATO_LIBRE
)
from estructuras_ceto import (
    ACETOACETIL_COA, HMG_COA, ACETOACETATO, D_BETA_HIDROXIBUTIRATO, ACETONA
)
from estructuras_colesterol import (
    ACETOACETIL_COA_COLEST, HMG_COA_CITOSOL, MEVALONATO, ISOPENTENIL_PP, FARNESIL_PP, ESCUALENO, LANOSTEROL, COLESTEROL
)

ANCHO_CANVAS = 5800
ALTO_CANVAS = 4750
MOSTRAR_CONEXIONES_INTER_RUTA = False

GLICEROL_MOL = """
<g class="molecula-glicerol" stroke="#0f172a" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="35" y="18" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0284c7" text-anchor="middle">CH₂OH</text>
  <line x1="35" y1="22" x2="35" y2="38" />
  <circle cx="35" cy="44" r="2.5" fill="#0f172a"/>
  <line x1="38" y1="44" x2="52" y2="44" stroke="#0284c7" stroke-width="1.8"/>
  <text x="64" y="48" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0284c7" text-anchor="middle">OH</text>
  <line x1="35" y1="48" x2="35" y2="64" />
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

    svg_col1 = []
    y_pos = 0
    for v in col1:
        svg_col1.append(f"""
        <g transform="translate(0, {y_pos})">
          <circle cx="12" cy="0" r="10" fill="#0284c7" />
          <text x="12" y="3.5" fill="#ffffff" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{v['n']}</text>
          <text x="30" y="3" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif">{v['nombre']}</text>
          <text x="30" y="16" fill="#64748b" font-size="9" font-family="'Inter', sans-serif">{v['resumen'][:55]}</text>
        </g>
        """)
        y_pos += 44

    svg_col2 = []
    y_pos = 0
    for v in col2:
        svg_col2.append(f"""
        <g transform="translate(0, {y_pos})">
          <circle cx="12" cy="0" r="10" fill="#0284c7" />
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
        <text x="0" y="-12" fill="#b45309" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">CÓDIGO DE COLORES EDITORIAL:</text>
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

def generar_bloque_autoria(x=3820, y=4230):
    """
    Genera el bloque institucional / autoría de código abierto en la esquina inferior derecha
    con código QR escaneable vectorial de alta resolución hacia el repositorio de GitHub.
    """
    qr_path = "M2,2H3V3H2zM3,2H4V3H3zM4,2H5V3H4zM5,2H6V3H5zM6,2H7V3H6zM7,2H8V3H7zM8,2H9V3H8zM13,2H14V3H13zM16,2H17V3H16zM17,2H18V3H17zM18,2H19V3H18zM20,2H21V3H20zM21,2H22V3H21zM22,2H23V3H22zM23,2H24V3H23zM25,2H26V3H25zM28,2H29V3H28zM29,2H30V3H29zM30,2H31V3H30zM31,2H32V3H31zM32,2H33V3H32zM33,2H34V3H33zM34,2H35V3H34zM2,3H3V4H2zM8,3H9V4H8zM11,3H12V4H11zM12,3H13V4H12zM13,3H14V4H13zM14,3H15V4H14zM17,3H18V4H17zM20,3H21V4H20zM22,3H23V4H22zM28,3H29V4H28zM34,3H35V4H34zM2,4H3V5H2zM4,4H5V5H4zM5,4H6V5H5zM6,4H7V5H6zM8,4H9V5H8zM10,4H11V5H10zM12,4H13V5H12zM16,4H17V5H16zM22,4H23V5H22zM23,4H24V5H23zM24,4H25V5H24zM28,4H29V5H28zM30,4H31V5H30zM31,4H32V5H31zM32,4H33V5H32zM34,4H35V5H34zM2,5H3V6H2zM4,5H5V6H4zM5,5H6V6H5zM6,5H7V6H6zM8,5H9V6H8zM10,5H11V6H10zM11,5H12V6H11zM12,5H13V6H12zM14,5H15V6H14zM17,5H18V6H17zM20,5H21V6H20zM21,5H22V6H21zM24,5H25V6H24zM26,5H27V6H26zM28,5H29V6H28zM30,5H31V6H30zM31,5H32V6H31zM32,5H33V6H32zM34,5H35V6H34zM2,6H3V7H2zM4,6H5V7H4zM5,6H6V7H5zM6,6H7V7H6zM8,6H9V7H8zM10,6H11V7H10zM11,6H12V7H11zM16,6H17V7H16zM17,6H18V7H17zM18,6H19V7H18zM19,6H20V7H19zM22,6H23V7H22zM23,6H24V7H23zM25,6H26V7H25zM28,6H29V7H28zM30,6H31V7H30zM31,6H32V7H31zM32,6H33V7H32zM34,6H35V7H34zM2,7H3V8H2zM8,7H9V8H8zM10,7H11V8H10zM11,7H12V8H11zM12,7H13V8H12zM16,7H17V8H16zM19,7H20V8H19zM21,7H22V8H21zM28,7H29V8H28zM34,7H35V8H34zM2,8H3V9H2zM3,8H4V9H3zM4,8H5V9H4zM5,8H6V9H5zM6,8H7V9H6zM7,8H8V9H7zM8,8H9V9H8zM10,8H11V9H10zM12,8H13V9H12zM14,8H15V9H14zM16,8H17V9H16zM18,8H19V9H18zM20,8H21V9H20zM22,8H23V9H22zM24,8H25V9H24zM26,8H27V9H26zM28,8H29V9H28zM29,8H30V9H29zM30,8H31V9H30zM31,8H32V9H31zM32,8H33V9H32zM33,8H34V9H33zM34,8H35V9H34zM10,9H11V10H10zM11,9H12V10H11zM12,9H13V10H12zM13,9H14V10H13zM14,9H15V10H14zM18,9H19V10H18zM21,9H22V10H21zM22,9H23V10H22zM23,9H24V10H23zM26,9H27V10H26zM2,10H3V11H2zM4,10H5V11H4zM5,10H6V11H5zM6,10H7V11H6zM7,10H8V11H7zM8,10H9V11H8zM11,10H12V11H11zM12,10H13V11H12zM14,10H15V11H14zM15,10H16V11H15zM18,10H19V11H18zM19,10H20V11H19zM21,10H22V11H21zM25,10H26V11H25zM28,10H29V11H28zM29,10H30V11H29zM30,10H31V11H30zM31,10H32V11H31zM32,10H33V11H32zM2,11H3V12H2zM3,11H4V12H3zM5,11H6V12H5zM6,11H7V12H6zM11,11H12V12H11zM13,11H14V12H13zM14,11H15V12H14zM15,11H16V12H15zM19,11H20V12H19zM22,11H23V12H22zM25,11H26V12H25zM28,11H29V12H28zM29,11H30V12H29zM31,11H32V12H31zM32,11H33V12H32zM33,11H34V12H33zM34,11H35V12H34zM2,12H3V13H2zM3,12H4V13H3zM5,12H6V13H5zM7,12H8V13H7zM8,12H9V13H8zM11,12H12V13H11zM12,12H13V13H12zM15,12H16V13H15zM16,12H17V13H16zM17,12H18V13H17zM19,12H20V13H19zM22,12H23V13H22zM24,12H25V13H24zM26,12H27V13H26zM27,12H28V13H27zM30,12H31V13H30zM32,12H33V13H32zM33,12H34V13H33zM2,13H3V14H2zM3,13H4V14H3zM5,13H6V14H5zM11,13H12V14H11zM12,13H13V14H12zM13,13H14V14H13zM15,13H16V14H15zM19,13H20V14H19zM20,13H21V14H20zM23,13H24V14H23zM24,13H25V14H24zM26,13H27V14H26zM30,13H31V14H30zM31,13H32V14H31zM32,13H33V14H32zM33,13H34V14H33zM2,14H3V15H2zM5,14H6V15H5zM6,14H7V15H6zM7,14H8V15H7zM8,14H9V15H8zM10,14H11V15H10zM13,14H14V15H13zM14,14H15V15H14zM16,14H17V15H16zM17,14H18V15H17zM18,14H19V15H18zM22,14H23V15H22zM25,14H26V15H25zM26,14H27V15H26zM27,14H28V15H27zM30,14H31V15H30zM31,14H32V15H31zM3,15H4V16H3zM4,15H5V16H4zM6,15H7V16H6zM9,15H10V16H9zM10,15H11V16H10zM11,15H12V16H11zM14,15H15V16H14zM17,15H18V16H17zM20,15H21V16H20zM25,15H26V16H25zM28,15H29V16H28zM32,15H33V16H32zM33,15H34V16H33zM34,15H35V16H34zM2,16H3V17H2zM3,16H4V17H3zM8,16H9V17H8zM9,16H10V17H9zM12,16H13V17H12zM13,16H14V17H13zM15,16H16V17H15zM17,16H18V17H17zM18,16H19V17H18zM19,16H20V17H19zM20,16H21V17H20zM22,16H23V17H22zM24,16H25V17H24zM26,16H27V17H26zM27,16H28V17H27zM28,16H29V17H28zM32,16H33V17H32zM33,16H34V17H33zM4,17H5V18H4zM6,17H7V18H6zM9,17H10V18H9zM10,17H11V18H10zM11,17H12V18H11zM12,17H13V18H12zM13,17H14V18H13zM14,17H15V18H14zM16,17H17V18H16zM17,17H18V18H17zM20,17H21V18H20zM23,17H24V18H23zM27,17H28V18H27zM28,17H29V18H28zM31,17H32V18H31zM32,17H33V18H32zM4,18H5V19H4zM8,18H9V19H8zM11,18H12V19H11zM12,18H13V19H12zM13,18H14V19H13zM17,18H18V19H17zM18,18H19V19H18zM19,18H20V19H19zM24,18H25V19H24zM25,18H26V19H25zM26,18H27V19H26zM27,18H28V19H27zM29,18H30V19H29zM30,18H31V19H30zM34,18H35V19H34zM3,19H4V20H3zM5,19H6V20H5zM13,19H14V20H13zM14,19H15V20H14zM15,19H16V20H15zM20,19H21V20H20zM22,19H23V20H22zM25,19H26V20H25zM28,19H29V20H28zM29,19H30V20H29zM31,19H32V20H31zM32,19H33V20H32zM34,19H35V20H34zM2,20H3V21H2zM5,20H6V21H5zM6,20H7V21H6zM7,20H8V21H7zM8,20H9V21H8zM12,20H13V21H12zM16,20H17V21H16zM17,20H18V21H17zM18,20H19V21H18zM20,20H21V21H20zM22,20H23V21H22zM23,20H24V21H23zM24,20H25V21H24zM26,20H27V21H26zM29,20H30V21H29zM30,20H31V21H30zM32,20H33V21H32zM33,20H34V21H33zM4,21H5V22H4zM6,21H7V22H6zM7,21H8V22H7zM10,21H11V22H10zM13,21H14V22H13zM15,21H16V22H15zM21,21H22V22H21zM22,21H23V22H22zM23,21H24V22H23zM24,21H25V22H24zM27,21H28V22H27zM29,21H30V22H29zM30,21H31V22H30zM31,21H32V22H31zM32,21H33V22H32zM33,21H34V22H33zM2,22H3V23H2zM3,22H4V23H3zM4,22H5V23H4zM5,22H6V23H5zM8,22H9V23H8zM10,22H11V23H10zM16,22H17V23H16zM17,22H18V23H17zM20,22H21V23H20zM21,22H22V23H21zM23,22H24V23H23zM26,22H27V23H26zM27,22H28V23H27zM29,22H30V23H29zM30,22H31V23H30zM31,22H32V23H31zM33,22H34V23H33zM34,22H35V23H34zM2,23H3V24H2zM5,23H6V24H5zM9,23H10V24H9zM12,23H13V24H12zM13,23H14V24H13zM15,23H16V24H15zM17,23H18V24H17zM18,23H19V24H18zM22,23H23V24H22zM23,23H24V24H23zM25,23H26V24H25zM28,23H29V24H28zM32,23H33V24H32zM34,23H35V24H34zM2,24H3V25H2zM6,24H7V25H6zM8,24H9V25H8zM11,24H12V25H11zM12,24H13V25H12zM13,24H14V25H13zM14,24H15V25H14zM15,24H16V25H15zM16,24H17V25H16zM20,24H21V25H20zM21,24H22V25H21zM27,24H28V25H27zM31,24H32V25H31zM32,24H33V25H32zM33,24H34V25H33zM2,25H3V26H2zM4,25H5V26H4zM5,25H6V26H5zM6,25H7V26H6zM7,25H8V26H7zM11,25H12V26H11zM13,25H14V26H13zM14,25H15V26H14zM15,25H16V26H15zM16,25H17V26H16zM18,25H19V26H18zM21,25H22V26H21zM22,25H23V26H22zM23,25H24V26H23zM24,25H25V26H24zM25,25H26V26H25zM27,25H28V26H27zM28,25H29V26H28zM30,25H31V26H30zM31,25H32V26H31zM32,25H33V26H32zM33,25H34V26H33zM34,25H35V26H34zM2,26H3V27H2zM4,26H5V27H4zM6,26H7V27H6zM8,26H9V27H8zM9,26H10V27H9zM11,26H12V27H11zM14,26H15V27H14zM18,26H19V27H18zM19,26H20V27H19zM21,26H22V27H21zM24,26H25V27H24zM25,26H26V27H25zM26,26H27V27H26zM27,26H28V27H27zM28,26H29V27H28zM29,26H30V27H29zM30,26H31V27H30zM31,26H32V27H31zM32,26H33V27H32zM33,26H34V27H33zM34,26H35V27H34zM10,27H11V28H10zM11,27H12V28H11zM12,27H13V28H12zM13,27H14V28H13zM14,27H15V28H14zM15,27H16V28H15zM18,27H19V28H18zM19,27H20V28H19zM20,27H21V28H20zM21,27H22V28H21zM25,27H26V28H25zM26,27H27V28H26zM30,27H31V28H30zM32,27H33V28H32zM34,27H35V28H34zM2,28H3V29H2zM3,28H4V29H3zM4,28H5V29H4zM5,28H6V29H5zM6,28H7V29H6zM7,28H8V29H7zM8,28H9V29H8zM11,28H12V29H11zM15,28H16V29H15zM16,28H17V29H16zM17,28H18V29H17zM18,28H19V29H18zM19,28H20V29H19zM22,28H23V29H22zM24,28H25V29H24zM25,28H26V29H25zM26,28H27V29H26zM28,28H29V29H28zM30,28H31V29H30zM32,28H33V29H32zM33,28H34V29H33zM2,29H3V30H2zM8,29H9V30H8zM10,29H11V30H10zM11,29H12V30H11zM12,29H13V30H12zM14,29H15V30H14zM15,29H16V30H15zM17,29H18V30H17zM18,29H19V30H18zM19,29H20V30H19zM20,29H21V30H20zM22,29H23V30H22zM25,29H26V30H25zM26,29H27V30H26zM30,29H31V30H30zM31,29H32V30H31zM32,29H33V30H32zM33,29H34V30H33zM34,29H35V30H34zM2,30H3V31H2zM4,30H5V31H4zM5,30H6V31H5zM6,30H7V31H6zM8,30H9V31H8zM10,30H11V31H10zM11,30H12V31H11zM12,30H13V31H12zM15,30H16V31H15zM16,30H17V31H16zM17,30H18V31H17zM18,30H19V31H18zM21,30H22V31H21zM22,30H23V31H22zM23,30H24V31H23zM24,30H25V31H24zM26,30H27V31H26zM27,30H28V31H27zM28,30H29V31H28zM29,30H30V31H29zM30,30H31V31H30zM31,30H32V31H31zM33,30H34V31H33zM34,30H35V31H34zM2,31H3V32H2zM4,31H5V32H4zM5,31H6V32H5zM6,31H7V32H6zM8,31H9V32H8zM10,31H11V32H10zM13,31H14V32H13zM15,31H16V32H15zM17,31H18V32H17zM19,31H20V32H19zM20,31H21V32H20zM25,31H26V32H25zM26,31H27V32H26zM27,31H28V32H27zM30,31H31V32H30zM31,31H32V32H31zM34,31H35V32H34zM2,32H3V33H2zM4,32H5V33H4zM5,32H6V33H5zM6,32H7V33H6zM8,32H9V33H8zM10,32H11V33H10zM11,32H12V33H11zM13,32H14V33H13zM15,32H16V33H15zM17,32H18V33H17zM18,32H19V33H18zM22,32H23V33H22zM24,32H25V33H24zM28,32H29V33H28zM29,32H30V33H29zM31,32H32V33H31zM2,33H3V34H2zM8,33H9V34H8zM11,33H12V34H11zM13,33H14V34H13zM14,33H15V34H14zM15,33H16V34H15zM16,33H17V34H16zM17,33H18V34H17zM20,33H21V34H20zM23,33H24V34H23zM24,33H25V34H24zM30,33H31V34H30zM31,33H32V34H31zM32,33H33V34H32zM2,34H3V35H2zM3,34H4V35H3zM4,34H5V35H4zM5,34H6V35H5zM6,34H7V35H6zM7,34H8V35H7zM8,34H9V35H8zM10,34H11V35H10zM13,34H14V35H13zM14,34H15V35H14zM17,34H18V35H17zM19,34H20V35H19zM24,34H25V35H24zM25,34H26V35H25zM26,34H27V35H26zM28,34H29V35H28zM29,34H30V35H29zM33,34H34V35H33z"
    return f'''
    <!-- BLOQUE INSTITUCIONAL Y AUTORÍA DE CÓDIGO ABIERTO (ADOLFO MORALES TENA) -->
    <g id="bloque_autoria" data-arrastrable="1" transform="translate({x}, {y})" filter="url(#shadowCard)">
      <!-- Fondo de la tarjeta -->
      <rect width="740" height="440" rx="22" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" />
      
      <!-- Barra superior de acento degradado -->
      <path d="M 0 22 Q 0 0 22 0 L 718 0 Q 740 0 740 22 L 740 10 L 0 10 Z" fill="url(#gradHeaderAutoria)" />

      <!-- Badge superior -->
      <rect x="35" y="26" width="275" height="24" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2" />
      <text x="172" y="42" fill="#0369a1" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="1">METABOLISMO Y SU REGULACIÓN</text>

      <!-- Título principal -->
      <text x="35" y="80" fill="#0f172a" font-size="21" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="0.5">MAPA METABÓLICO INTEGRADO</text>
      <text x="35" y="102" fill="#475569" font-size="12.5" font-weight="700" font-family="'Inter', sans-serif">Topología Celular &amp; Arquitectura Vectorial Algorítmica</text>

      <line x1="35" y1="118" x2="705" y2="118" stroke="#e2e8f0" stroke-width="1.5" />

      <!-- Columna Izquierda: Autor y Tecnologías -->
      <text x="35" y="146" fill="#64748b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" letter-spacing="1.2">AUTOR:</text>
      <text x="35" y="174" fill="#0f172a" font-size="20" font-weight="900" font-family="'Inter', sans-serif">Adolfo Morales Tena</text>
      <text x="35" y="195" fill="#0284c7" font-size="12.5" font-weight="700" font-family="'Inter', sans-serif">Estudiante • Investigador</text>

      <text x="35" y="230" fill="#64748b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" letter-spacing="1.2">TECNOLOGÍAS &amp; METODOLOGÍA:</text>
      <text x="35" y="252" fill="#334155" font-size="11.5" font-weight="600" font-family="'Inter', sans-serif">• Código abierto desarrollado algorítmicamente en Python 3</text>
      <text x="35" y="272" fill="#334155" font-size="11.5" font-weight="600" font-family="'Inter', sans-serif">• Renderizado nativo SVG 1.1 sin pérdida de resolución (Ultra HD)</text>
      <text x="35" y="292" fill="#334155" font-size="11.5" font-weight="600" font-family="'Inter', sans-serif">• Interactividad web: HTML5, CSS3, JavaScript (Drag &amp; Drop / Zoom)</text>
      <text x="35" y="312" fill="#334155" font-size="11.5" font-weight="600" font-family="'Inter', sans-serif">• Rigor bioquímico: Célula eucariota, enzimas EC y cofactores</text>

      <!-- Badge Licencia -->
      <g transform="translate(35, 332)">
        <rect x="0" y="0" width="135" height="22" rx="5" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
        <text x="67" y="15" fill="#475569" font-size="10" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">Licencia MIT</text>
      </g>

      <!-- Botón / Enlace GitHub -->
      <g transform="translate(35, 368)">
        <a href="https://github.com/AMorales22T/mapa_metabolico-" target="_blank">
          <rect x="0" y="0" width="475" height="50" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" style="cursor: pointer;" />
          <g transform="translate(14, 13)">
            <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" fill="#ffffff" />
          </g>
          <text x="48" y="22" fill="#94a3b8" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">REPOSITORIO DE CÓDIGO ABIERTO EN GITHUB:</text>
          <text x="48" y="39" fill="#38bdf8" font-size="12" font-weight="700" font-family="'JetBrains Mono', monospace">https://github.com/AMorales22T/mapa_metabolico-</text>
        </a>
      </g>

      <!-- Columna Derecha: Código QR limpio sin texto innecesario -->
      <g transform="translate(535, 140)">
        <rect x="0" y="0" width="170" height="170" rx="14" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.5" />
        
        <!-- Marco blanco para el QR -->
        <g transform="translate(13, 13)">
          <rect x="0" y="0" width="144" height="144" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
          <!-- QR escalado a 130px (130 / 37 = 3.5135) -->
          <g transform="translate(7, 7) scale(3.5135)">
            <path d="{qr_path}" fill="#0f172a" />
          </g>
        </g>
      </g>
    </g>
    '''

def cargar_cte_original_usuario():
    """
    Carga directamente el diseño vectorial exacto del archivo SVG que el usuario ya realizó:
    02_RESPIRACION_Y_ENERGIA/03_cadena_transporte_electrones_y_atp_sintasa/Cadena_Transporte_Electrones.svg
    """
    import re
    path_cte = os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "03_cadena_transporte_electrones_y_atp_sintasa", "Cadena_Transporte_Electrones.svg")
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
    <g transform="translate(140, 180)" opacity="0.8">
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

    <!-- ================================================================= -->
    <!-- CAPA SANGUÍNEA: TORRENTE VASCULAR / LUMEN CAPILAR REAL             -->
    <!-- ================================================================= -->
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
      <path d="M 100 {y_mito + 180} 
               C 260 {y_mito - 30}, 850 {y_mito - 90}, 1520 {y_mito - 40}
               C 1950 {y_mito - 110}, 2650 {y_mito - 80}, 3350 {y_mito - 30}
               C 3850 {y_mito - 40}, 4350 {y_mito - 20}, 4740 {y_mito + 20}
               C 4880 {y_mito + 100}, 4880 {y_mito + 500}, 4850 {y_mito + 900}
               C 4820 {y_mito + 1400}, 4760 {y_mito + 1800}, 4400 {y_mito + 1940}
               C 3900 {y_mito + 1960}, 2850 {y_mito + 1950}, 1900 {y_mito + 1930}
               C 1100 {y_mito + 1950}, 300 {y_mito + 1850}, 140 {y_mito + 1300}
               C 60 {y_mito + 800}, 50 {y_mito + 400}, 100 {y_mito + 180} Z"
            fill="url(#gradMitocondria)" stroke="#92400e" stroke-width="6"/>

      <!-- Espacio Intermembrana (EIM) -->
      <path d="M 150 {y_mito + 195} 
               C 300 {y_mito}, 870 {y_mito - 55}, 1520 {y_mito - 10}
               C 1940 {y_mito - 75}, 2640 {y_mito - 45}, 3320 {y_mito}
               C 3820 {y_mito - 10}, 4320 {y_mito + 10}, 4700 {y_mito + 45}
               C 4830 {y_mito + 115}, 4830 {y_mito + 490}, 4805 {y_mito + 880}
               C 4775 {y_mito + 1370}, 4715 {y_mito + 1750}, 4370 {y_mito + 1895}
               C 3880 {y_mito + 1910}, 2830 {y_mito + 1900}, 1900 {y_mito + 1885}
               C 1120 {y_mito + 1900}, 350 {y_mito + 1805}, 190 {y_mito + 1275}
               C 110 {y_mito + 790}, 100 {y_mito + 405}, 150 {y_mito + 195} Z"
            fill="#fffbeb" fill-opacity="0.6" stroke="#b45309" stroke-width="3" stroke-dasharray="12 7"/>

      <!-- Matriz Mitocondrial (MMI Contorno interno) -->
      <path d="M 210 {y_mito + 220} 
               C 360 {y_mito + 45}, 900 {y_mito}, 1520 {y_mito + 35}
               C 1920 {y_mito - 25}, 2620 {y_mito}, 3280 {y_mito + 45}
               C 3780 {y_mito + 35}, 4280 {y_mito + 50}, 4650 {y_mito + 80}
               C 4770 {y_mito + 140}, 4770 {y_mito + 480}, 4750 {y_mito + 850}
               C 4720 {y_mito + 1330}, 4660 {y_mito + 1700}, 4330 {y_mito + 1845}
               C 3850 {y_mito + 1855}, 2800 {y_mito + 1845}, 1900 {y_mito + 1830}
               C 1150 {y_mito + 1845}, 410 {y_mito + 1755}, 260 {y_mito + 1245}
               C 180 {y_mito + 780}, 170 {y_mito + 425}, 210 {y_mito + 220} Z"
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
    partes.append(nodo_libre(x_g - 250, y_g + paso_y * 4, "Dihidroxiacetona-P", "3C", DIHIDROXIACETONA_FOSFATO, "m_dhap", text_right=False))
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
      {badge_via(2, 940, 110)}
      <!-- Título y balance global de la vía -->
      <g id="titulo_gluconeogenesis" transform="translate(980, 105)">
        <text x="0" y="5" fill="#7c3aed" font-size="14" font-weight="900" font-family="'Inter', sans-serif">GLUCONEOGÉNESIS (VÍA ANABÓLICA HEPÁTICA)</text>
        <text x="0" y="18" fill="#64748b" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Síntesis de novo • 3 Rodeos (Bypasses) + 7 Pasos Reversibles</text>
        <text x="0" y="29" fill="#0284c7" font-size="8" font-weight="700" font-family="'Inter', sans-serif">Gasto neto: 4 ATP + 2 GTP + 2 NADH por Glucosa formada</text>
      </g>
    ''')

    # RODEO 3: Retículo Endoplásmico y Glucosa-6-Fosfatasa (G6Pasa) ➔ Sortea Hexocinasa
    partes.append(f'''
    <g id="rodeo3_g6pasa" data-arrastrable="1">
      {badge_rodeo_gng(3, 1030, 220)}

      <!-- Ficha descriptiva de la G6Pasa -->
      <g transform="translate(990, 245)">
        <text x="0" y="0" fill="#6d28d9" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Glucosa-6-Fosfatasa (RE)</text>
        <text x="0" y="13" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">EC 3.1.3.9 (+ H₂O ➔ + Pi)</text>
        <text x="0" y="25" fill="#b45309" font-size="8" font-weight="800" font-family="'Inter', sans-serif">Sortea Hexocinasa • Lumen del RE</text>
        <text x="0" y="37" fill="#0284c7" font-size="8" font-weight="700" font-family="'Inter', sans-serif">Hepatocito y Corteza Renal</text>
      </g>

      <!-- Complejo del Retículo Endoplásmico con translocadores T1 y T2/T3 -->
      <g id="organelo_re_g6pasa" transform="translate(1220, 200)">
        {RE_GLUCOSA_6_FOSFATASA}
      </g>

      <!-- Flujo 1: G-6-P citosólica entra por T1 al Lumen del RE (comienza fuera de m_g6p) -->
      <path d="M 1560 345 C 1460 345, 1360 280, 1260 250" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <text x="1420" y="295" fill="#7c3aed" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">G6P ➔ RE (T1)</text>

      <!-- Flujo 2 y 3: Salida de Glucosa libre desde T2/T3 hacia transportador GLUT-2 en membrana -->
      <g id="carrier_glut2_gng">
        <!-- Cápsula transportadora de GLUT-2 en la membrana plasmática (despejado en X=1480, Y=68) -->
        <rect x="1455" y="53" width="50" height="30" rx="6" fill="#7c3aed" stroke="#5b21b6" stroke-width="1.8"/>
        <text x="1480" y="72" fill="#ffffff" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-2</text>
        <!-- Flecha desde RE T2/T3 hacia GLUT-2 -->
        <path d="M 1375 220 Q 1425 140, 1475 88" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        <text x="1380" y="150" fill="#7c3aed" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Glucosa libre ➔ Citosol</text>
        <!-- Flecha hacia la sangre -->
        <line x1="1480" y1="53" x2="1480" y2="20" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
        <text x="1495" y="38" fill="#7c3aed" font-size="9" font-weight="800" font-family="'Inter', sans-serif">Glucosa ➔ Sangre (Glucemia)</text>
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

    # PRECURSOR 1: Glicerol desde lipólisis ➔ DHAP
    partes.append(nodo_libre(980, 860, "Glicerol", "3C", GLICEROL_MOL, "m_glicerol", text_pos="top", dx=35, dy=-40, detalle="Lipólisis (Tejido adiposo)"))
    partes.append(f'''
    <g id="rx_gng_glicerol" data-arrastrable="1" transform="translate(1050, 885)">
      <line x1="0" y1="20" x2="140" y2="20" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <g transform="translate(70, -2)">
        <text x="0" y="-12" fill="#7c3aed" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">[Precursor]</text>
        <text x="0" y="0" fill="#6d28d9" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Glicerol Cinasa (-1 ATP) ➔ G-3-P</text>
        <text x="0" y="12" fill="#059669" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">G3PDH (+ NAD⁺ ➔ + NADH) ➔ DHAP</text>
      </g>
    </g>
    <!-- Confluencia de DHAP hacia Aldolasa -->
    <g id="rx_gng_dhap_confluencia" data-arrastrable="1">
      <path d="M 1520 860 L 1630 860" fill="none" stroke="#7c3aed" stroke-width="2.4" stroke-dasharray="6 3" marker-end="url(#arrowFlow)"/>
      <text x="1525" y="852" fill="#7c3aed" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">↳ + 1 DHAP (Glicerol)</text>
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
      <g transform="translate(1660, 1900)">
        <text x="0" y="0" fill="#6d28d9" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">LDH: Lactato ➔ Piruvato</text>
        <text x="0" y="11" fill="#059669" font-size="8" font-weight="800" font-family="'Inter', sans-serif">+ NAD⁺ ➔ + NADH + H⁺</text>
      </g>
    </g>
    ''')

    # RODEO 1: Piruvato Carboxilasa (PC) y PEPCK con Lanzadera de Malato ➔ Sortea Piruvato Cinasa
    # A. En la Matriz Mitocondrial (Anaplerosis y Cataplerosis con el Ciclo de Krebs):
    partes.append(f'''
    <g id="rodeo1_matriz_pc" data-arrastrable="1">
      <!-- Desvío de Piruvato que entra por MPC hacia PC en la matriz superior -->
      <path d="M 1640 2145 L 1555 2145" fill="none" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
      {badge_rodeo_gng(1, 1480, 2105)}
      <!-- Ficha de la Piruvato Carboxilasa -->
      <g transform="translate(1480, 2145)">
        <rect x="-68" y="-13" width="136" height="26" rx="6" fill="#fdf4ff" stroke="#d946ef" stroke-width="1.2"/>
        <text x="0" y="2" fill="#86198f" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">PC (Piruvato Carboxilasa)</text>
        <text x="0" y="13" fill="#64748b" font-size="7.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">- 1 ATP, Biotina • ⊕ Acetil-CoA</text>
      </g>

      <!-- Conversión a Malato y salida por OGC (mMDH / Enzima Málica) -->
      <path d="M 1405 2145 L 1305 2145" fill="none" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      <g transform="translate(1355, 2163)">
        <text x="0" y="0" fill="#6d28d9" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">mMDH (OAA ➔ Malato)</text>
        <text x="0" y="10" fill="#0284c7" font-size="7.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">- 1 NADH matricial</text>
      </g>

      <!-- Retorno cataplerótico desde Krebs hacia OGC -->
      <path d="M 1160 2145 L 1245 2145" fill="none" stroke="#b45309" stroke-width="2.2" stroke-dasharray="6 3" marker-end="url(#arrowFlow)"/>
      <text x="1240" y="2138" fill="#b45309" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Cataplerosis Krebs (Malato / AA) ➔ OGC</text>
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
      <path d="M {x_glc + 450} {y_glc + 20} C {x_glc + 380} {y_glc + 20}, {x_glc + 320} {y_udpg + 35}, {x_glc + 365} {y_udpg + 35}" fill="none" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="{x_glc + 365}" y="{y_udpg - 55}" fill="#d97706" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">UDP-Glucosa Pirofosforilasa (+UTP)</text>
    </g>
    """)

    # Cadena de Glucógeno
    partes.append(nodo_libre(x_glc - 80, y_glc + 260, "Glucógeno (n+1)", "Polímero", CADENA_GLUCOGENO, "m_glucogeno_cadena", text_pos="top", dx=45, dy=-48))
    partes.append(f"""
    <g id="rx_sintesis_degradacion_glucogeno" data-arrastrable="1">
      <!-- Síntesis -->
      <path d="M {x_glc + 150} {y_udpg + 65} Q {x_glc + 70} {y_glc + 150} {x_glc + 10} {y_glc + 215}" fill="none" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="{x_glc + 120}" y="{y_glc + 145}" fill="#b45309" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">Glucógeno Sintasa</text>
      <g transform="translate({x_glc + 120}, {y_glc + 160})">
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
    x_p = 2580
    y_p = 300
    partes.append(f'<g id="ruta_pentosas">')
    partes.append(badge_via(4, 2520, 260))

    # Entrada G6PDH desde G6P
    partes.append(f"""
    <g id="rx_g6pdh" data-arrastrable="1">
      <path d="M {x_g + 265} {y_g + paso_y + 35} Q 2180 235 {x_p - 40} {y_p + 35}" fill="none" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>
      <text x="{(x_g + 265 + x_p - 40)//2}" y="218" fill="#059669" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">G6PDH (+ NADP⁺ ➔ + NADPH + H⁺) • [Precursor Reductor: Lipogénesis / GSH]</text>
    </g>
    """)

    # 1. Lactona
    partes.append(etiqueta_regulacion("g6pdh", x_p - 110, y_p + 15, dx=0, dy=0, anchor="end"))
    partes.append(nodo_libre(x_p, y_p, "6-P-Gluconolactona", "6C", FOSFOGLUCONO_LACTONA_6, "m_lactona", text_right=True, dx=145))
    partes.append(reaccion_libre(x_p + 50, y_p + 105, 36, "Lactonasa (+ H₂O)", id_rx="rx_lactonasa"))

    # 2. 6-Fosfogluconato
    partes.append(nodo_libre(x_p, y_p + 160, "6-Fosfogluconato", "6C", FOSFOGLUCONATO_6, "m_6pg", text_right=True, dx=145))
    partes.append(reaccion_libre(x_p + 50, y_p + 315, 36, "6-Fosfogluconato DH (+ NADP⁺ ➔ + NADPH + CO₂)", es_ganancia=True, id_rx="rx_6pgdh"))

    # 3. Ribulosa-5-P
    partes.append(nodo_libre(x_p, y_p + 370, "Ribulosa-5-Fosfato", "5C", RIBULOSA_5_FOSFATO, "m_ru5p", text_right=True, dx=145, detalle="[Precursor] Ribosa-5-P"))

    # Ramas: Xilulosa-5P y Ribosa-5P (texto despejado de flechas y columnas adyacentes)
    partes.append(nodo_libre(x_p - 110, y_p + 500, "Xilulosa-5-P", "5C", XILULOSA_5_FOSFATO, "m_xu5p", text_right=False, dx=15, dy=20, detalle="[Regulador] ChREBP"))
    partes.append(nodo_libre(x_p + 280, y_p + 500, "Ribosa-5-P", "5C", RIBOSA_5_FOSFATO, "m_r5p", text_pos="bottom", dx=40, dy=105, detalle="[Precursor] PRPP"))
    partes.append(f"""
    <path d="M {x_p + 20} {y_p + 430} L {x_p - 50} {y_p + 495}" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="{x_p - 50}" y="{y_p + 460}" fill="#047857" font-size="10.5" font-family="'Inter', sans-serif" text-anchor="end">Fosfopentosa Epimerasa</text>

    <path d="M {x_p + 80} {y_p + 430} L {x_p + 270} {y_p + 495}" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="{x_p + 200}" y="{y_p + 460}" fill="#047857" font-size="10.5" font-family="'Inter', sans-serif">Fosfopentosa Isomerasa</text>
    """)

    # Sedoheptulosa-7P y Eritrosa-4P (texto centrado arriba / izquierda para no tocar columnas adyacentes)
    partes.append(nodo_libre(x_p - 110, y_p + 660, "Sedoheptulosa-7-P", "7C", SEDOHEPTULOSA_7_FOSFATO, "m_s7p", text_pos="top", dy=-20))
    partes.append(nodo_libre(x_p + 280, y_p + 660, "Eritrosa-4-P", "4C", ERITROSA_4_FOSFATO, "m_e4p", text_right=False, dx=15, dy=20, detalle="[Precursor] AA Aromáticos (Phe, Tyr, Trp)"))
    partes.append(f"""
    <text x="{x_p + 90}" y="{y_p + 600}" fill="#047857" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Transcetolasa 1 (TK1) ⇄</text>
    <text x="{x_p + 90}" y="{y_p + 760}" fill="#047857" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Transaldolasa ⇄ Retorno a F6P y GAP</text>

    <!-- Retornos de Transaldolasa y Transcetolasa hacia Glucólisis -->
    """ + (f"""
    <path d="M {x_p - 140} {y_p + 760} C 2550 430, 2450 370, 2080 370 C 1960 370, 1880 440, {x_g + 160} {y_g + paso_y * 2 + 35}" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <text x="2020" y="360" fill="#059669" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Retorno a Glucólisis: Fructosa-6-P ➔</text>

    <path d="M {x_p - 140} {y_p + 800} C 2500 1150, 2180 1150, {x_g + 200} {y_g + paso_y * 4 + 35}" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <text x="2350" y="1140" fill="#059669" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Retorno a Glucólisis: GAP ➔</text>
    """ if MOSTRAR_CONEXIONES_INTER_RUTA else "") + f"""
    """)
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

      <!-- 4. Contenido Interior con Aumento y Diferenciación Clara de Compartimentos -->
      <g clip-path="url(#clipLupaLanzadera)">
        <!-- Fondo CITOPLASMA (Mitad Superior en Verde Suave) -->
        <rect x="{cx_lupa - r_lupa - 10}" y="{cy_lupa - r_lupa - 10}" width="{r_lupa * 2 + 20}" height="{r_lupa + 10}" fill="#f0fdf4"/>

        <!-- Fondo MATRIZ MITOCONDRIAL (Mitad Inferior en Ámbar Suave) -->
        <rect x="{cx_lupa - r_lupa - 10}" y="{cy_lupa}" width="{r_lupa * 2 + 20}" height="{r_lupa + 10}" fill="#fffbeb"/>

        <!-- Bicapa MMI transversal divisoria en la lupa -->
        <rect x="{cx_lupa - r_lupa - 10}" y="{cy_lupa - 20}" width="{r_lupa * 2 + 20}" height="40" fill="#fed7aa" stroke="#d97706" stroke-width="2.5"/>
        <text x="{cx_lupa - 180}" y="{cy_lupa + 5}" fill="#92400e" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace">MMI (MEMBRANA)</text>

        <!-- Cabezas de fosfolípidos en MMI -->
        <g fill="#d97706" opacity="0.6">
          <circle cx="{cx_lupa - 270}" cy="{cy_lupa - 14}" r="2.8"/><circle cx="{cx_lupa - 250}" cy="{cy_lupa - 14}" r="2.8"/>
          <circle cx="{cx_lupa - 270}" cy="{cy_lupa + 14}" r="2.8"/><circle cx="{cx_lupa - 250}" cy="{cy_lupa + 14}" r="2.8"/>
          <circle cx="{cx_lupa + 250}" cy="{cy_lupa - 14}" r="2.8"/><circle cx="{cx_lupa + 270}" cy="{cy_lupa - 14}" r="2.8"/>
          <circle cx="{cx_lupa + 250}" cy="{cy_lupa + 14}" r="2.8"/><circle cx="{cx_lupa + 270}" cy="{cy_lupa + 14}" r="2.8"/>
        </g>

        <!-- Transportador 1: SLC25A11 (OGC) -->
        <g transform="translate({cx_lupa + 90}, {cy_lupa - 24})">
          <rect x="-35" y="0" width="70" height="48" rx="10" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
          <text x="0" y="20" fill="#78350f" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">OGC</text>
          <text x="0" y="36" fill="#92400e" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Mal²⁻ ⇄ α-KG²⁻</text>
        </g>

        <!-- Transportador 2: SLC25A12 (Aralar / AGC) -->
        <g transform="translate({cx_lupa - 90}, {cy_lupa - 24})">
          <rect x="-35" y="0" width="70" height="48" rx="10" fill="#ec4899" stroke="#db2777" stroke-width="2"/>
          <text x="0" y="20" fill="#831843" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">Aralar</text>
          <text x="0" y="36" fill="#9d174d" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Asp⁻ ⇄ Glu⁻</text>
        </g>

        <!-- =========================================================== -->
        <!-- ZONA 1: CITOPLASMA (ARRIBA) - SÍNTESIS DE MALATO Y GOT1     -->
        <!-- =========================================================== -->
        <g transform="translate({cx_lupa}, {cy_lupa - 260})">
          <rect x="-200" y="-14" width="400" height="26" rx="13" fill="#f1f5f9" stroke="#0284c7" stroke-width="1.8"/>
          <text x="0" y="4" fill="#0369a1" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
            CITOSOL: cMDH (REDUCCIÓN) &amp; GOT1 / cAST
          </text>
        </g>

        <!-- Estructura Citosólica 1: Oxalacetato -->
        <g transform="translate({cx_lupa - 235}, {cy_lupa - 220})">
          {LANZ_OAA}
          <text x="40" y="145" fill="#0f172a" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Oxalacetato</text>
          <text x="40" y="160" fill="#ea580c" font-size="10" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C]</text>
        </g>

        <!-- Reacción cMDH horizontal -->
        <g transform="translate({cx_lupa - 75}, {cy_lupa - 155})">
          <line x1="0" y1="0" x2="130" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
          <text x="65" y="-12" fill="#0f172a" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">cMDH</text>
          <path d="M 10 14 Q 65 38 120 14" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
          <text x="65" y="44" fill="#dc2626" font-size="10" font-weight="800" text-anchor="middle">- NADH + H⁺ ➔ + NAD⁺</text>
          <text x="65" y="58" fill="#64748b" font-size="8.5" font-family="'Inter', sans-serif" text-anchor="middle">(regenera NAD⁺ para Glucólisis)</text>
        </g>

        <!-- Estructura Citosólica 2: L-Malato -->
        <g transform="translate({cx_lupa + 55}, {cy_lupa - 220})">
          {LANZ_MALATO}
          <text x="40" y="145" fill="#0f172a" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Malato</text>
          <text x="40" y="160" fill="#ea580c" font-size="10" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C]</text>
        </g>

        <!-- FLECHA: Malato baja desde el citoplasma y cruza la membrana por OGC -->
        <path d="M {cx_lupa + 95} {cy_lupa - 70} L {cx_lupa + 95} {cy_lupa + 65}" stroke="#0284c7" stroke-width="3.2" marker-end="url(#arrowBlue)"/>
        <text x="{cx_lupa + 140}" y="{cy_lupa - 35}" fill="#0284c7" font-size="9.5" font-weight="800">Malato²⁻ cruza hacia matriz ➔</text>

        <!-- Transaminación Citosólica GOT1 (Aspartato que sube por Aralar ➔ regenera Oxalacetato) -->
        <g transform="translate({cx_lupa - 95}, {cy_lupa - 85})">
          <path d="M 5 20 C -15 -5, -60 -15, -95 -45" fill="none" stroke="#db2777" stroke-width="2.6" marker-end="url(#arrowRed)"/>
          <text x="0" y="-5" fill="#be123c" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">GOT1 (cAST)</text>
          <text x="0" y="8" fill="#64748b" font-size="8.5" font-family="'Inter', sans-serif" text-anchor="middle">+ α-KG ➔ + Glu</text>
        </g>

        <!-- =========================================================== -->
        <!-- ZONA 2: MATRIZ MITOCONDRIAL (ABAJO) - REOXIDACIÓN Y GOT2    -->
        <!-- =========================================================== -->
        <!-- Estructura Matricial 1: L-Malato en la Matriz -->
        <g transform="translate({cx_lupa + 55}, {cy_lupa + 75})">
          {LANZ_MALATO}
          <text x="40" y="145" fill="#0f172a" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Malato (Matriz)</text>
        </g>

        <!-- Reacción mMDH horizontal hacia la izquierda -->
        <g transform="translate({cx_lupa + 55}, {cy_lupa + 140})">
          <line x1="0" y1="0" x2="-130" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
          <text x="-65" y="-12" fill="#0f172a" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">mMDH</text>
          <path d="M 0 14 Q -65 38 -130 14" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
          <text x="-50" y="44" fill="#059669" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">+ NADH + H⁺</text>
          <text x="-50" y="58" fill="#047857" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">➔ Complejo I (2.5 ATP)</text>
        </g>

        <!-- Estructura Matricial 2: Oxalacetato en la Matriz -->
        <g transform="translate({cx_lupa - 200}, {cy_lupa + 65})">
          {LANZ_OAA}
          <text x="40" y="140" fill="#0f172a" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Oxalacetato (Matriz)</text>
        </g>

        <!-- Transaminación Matricial GOT2 (Oxalacetato ➔ Aspartato) -->
        <g transform="translate({cx_lupa - 130}, {cy_lupa + 45})">
          <path d="M -25 25 C -5 0, 30 -5, 50 15" fill="none" stroke="#db2777" stroke-width="2.6" marker-end="url(#arrowRed)"/>
          <text x="10" y="-3" fill="#be123c" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">GOT2 (mAST)</text>
          <text x="10" y="10" fill="#64748b" font-size="8.5" font-family="'Inter', sans-serif" text-anchor="middle">+ Glu ➔ + α-KG</text>
        </g>

        <!-- Retorno de Aspartato hacia el citoplasma a través de Aralar -->
        <path d="M {cx_lupa - 90} {cy_lupa + 65} L {cx_lupa - 90} {cy_lupa - 70}" stroke="#db2777" stroke-width="2.8" marker-end="url(#arrowRed)"/>
        <text x="{cx_lupa - 98}" y="{cy_lupa - 35}" fill="#db2777" font-size="9" font-weight="800" text-anchor="end">Aspartato retorna al citosol ➔</text>

        <!-- Banner Explicativo Inferior -->
        <g transform="translate({cx_lupa}, {cy_lupa + 260})">
          <rect x="-210" y="-14" width="420" height="28" rx="14" fill="#0f172a" opacity="0.95"/>
          <text x="0" y="4" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
            LANZADERA MALATO-ASPARTATO
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
    partes.append(badge_via(5, x_k + 545, y_k - 10))
    partes.append(badge_via(6, x_k - 40, y_k + paso_k * 4 + 40))

    # Complejo PDH (Transición MPC ➔ Acetil-CoA)
    partes.append(f"""
    <!-- Reacción PDH con Ancla de Zoom y flecha guía punteada -->
    <path d="M 1680 {y_mito - 10} C 1680 {y_k - 20}, {x_k + 400} {y_k - 20}, {x_k + 370} {y_k + 10}" fill="none" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    
    <!-- Flecha punteada guía visual hacia el panel de detalle PDH -->
    <path d="M 1580 {y_k + 40} C 1530 {y_k + 120}, 1530 3300, 1530 3435" fill="none" stroke="#0284c7" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowBlue)"/>

    <g id="ancla_pdh_molecular" transform="translate({x_k + 580}, {y_k - 10})">
      <text x="0" y="5" fill="#c2410c" font-size="13" font-weight="900" font-family="'Inter', sans-serif">Complejo PDH (E1, E2, E3)</text>
      <text x="0" y="24" fill="#64748b" font-size="11" font-family="'Inter', sans-serif">+ CoA-SH + NAD⁺ ➔ CO₂ + NADH</text>
      <g transform="translate(0, 40)">
        <text x="0" y="0" fill="#16a34a" font-size="9" font-weight="800">(+) Piruvato, ADP, NAD⁺, Ca²⁺</text>
        <text x="0" y="12" fill="#dc2626" font-size="9" font-weight="800">(-) Acetil-CoA, NADH, ATP</text>
        <text x="0" y="24" fill="#ca8a04" font-size="9" font-weight="800">(P) Inactiva por PDK · Activa por PDP (Ca²⁺/Insulina)</text>
      </g>
    </g>
    """)

    # Acetil-CoA
    partes.append(nodo_libre(x_k + 240, y_k + 15, "Acetil-CoA", "2C", ACETIL_COA, "m_accoa", text_right=False, dx=-15, dy=40))

    # Oxalacetato (inicio del ciclo de Krebs)
    partes.append(nodo_libre(x_k - 240, y_k + 15, "Oxalacetato", "4C", KREBS_OXALACETATO, "m_oaa", text_right=False))
    partes.append(f"""
    <!-- Condensación Citrato Sintasa -->
    <path d="M {x_k - 110} {y_k + 60} L {x_k + 220} {y_k + 60}" stroke="#b45309" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
    <path d="M {x_k + 55} {y_k + 60} L {x_k + 55} {y_k + 160}" stroke="#b45309" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    <text x="{x_k + 75}" y="{y_k + 110}" fill="#78350f" font-size="12" font-weight="800" font-family="'Inter', sans-serif">Citrato Sintasa</text>
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
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 3 + 130, 38, "α-KG Deshidrogenasa", entra="+ CoA + NAD⁺", sale="+ NADH + CO₂", es_ganancia=True, id_rx="rx_akgdh", text_dx=-16, text_anchor="end"))
    partes.append(etiqueta_regulacion("akgdh", x_k + 69, y_k + paso_k * 3 + 138, dx=0, dy=0, anchor="start"))

    # Succinil-CoA
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 4, "Succinil-CoA", "4C", SUCCINIL_COA, "m_succoa", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 4 + 130, 38, "Succinil-CoA Sintetasa", entra="+ GDP + Pi", sale="+ GTP (+CoA)", es_ganancia=True, id_rx="rx_scas", text_dx=-16, text_anchor="end"))

    # Succinato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 5, "Succinato", "4C", SUCCINATO, "m_succinato", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 5 + 130, 38, "Succinato DH (Complejo II)", entra="+ FAD", sale="+ FADH₂", es_ganancia=True, id_rx="rx_sdh", text_dx=-16, text_anchor="end"))

    # Fumarato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 6, "Fumarato", "4C", FUMARATO, "m_fumarato", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 6 + 130, 38, "Fumarasa (+ H₂O)", reversible=True, id_rx="rx_fum", text_dx=-16, text_anchor="end"))

    # L-Malato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 7, "L-Malato", "4C", KREBS_MALATO, "m_malato", text_right=True, dx=140))

    # Cierre del Ciclo: Retorno de Malato a Oxalacetato (100% dentro de la matriz mitocondrial)
    y_mdh_txt = y_k + int(paso_k * 6.2)
    partes.append(f"""
    <g id="rx_mdh_retorno" data-arrastrable="1">
      <path d="M {x_k} {y_k + paso_k * 7 + 60} C 870 {y_k + paso_k * 7 + 60}, 870 {y_k + 90}, {x_k - 235} {y_k + 20}" fill="none" stroke="#b45309" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <text x="895" y="3455" fill="#78350f" font-size="12" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 895 3400)">
        Malato DH (+ NAD⁺ ➔ + NADH + H⁺)
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
            <text x="0" y="12" fill="#c2410c" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">I. MECANISMO DE REACCIÓN MULTIENZIMÁTICO</text>

            <!-- 1. Piruvato entra -->
            <g transform="translate(10, 28)">
              <rect x="0" y="0" width="125" height="28" rx="6" fill="#ffedd5" stroke="#ea580c" stroke-width="1.5"/>
              <text x="62" y="18" fill="#9a3412" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">Piruvato (3C)</text>
              <text x="140" y="18" fill="#64748b" font-size="9.5" font-family="'Inter', sans-serif">Sustrato alimentador</text>
            </g>

            <!-- Reacción E1 -->
            <path d="M 72 60 L 72 115" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
            <path d="M 68 85 Q 30 95 10 95" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
            <text x="5" y="99" fill="#dc2626" font-size="10" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">+ CO₂ ↑</text>
            <g transform="translate(90, 78)">
              <text x="0" y="0" fill="#0f172a" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">E1: Piruvato DH (TPP)</text>
              <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">Descarboxilación oxidativa</text>
              <text x="0" y="25" fill="#ea580c" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Ataque nucleofílico del TPP</text>
            </g>

            <!-- Intermediario 1: Hidroxietil-TPP -->
            <g transform="translate(10, 120)">
              <rect x="0" y="0" width="155" height="30" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.2"/>
              <text x="77" y="19" fill="#1e293b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Hidroxietil-TPP (E1)</text>
              <text x="170" y="19" fill="#64748b" font-size="9" font-family="'Inter', sans-serif">Intermediario carbanión</text>
            </g>

            <!-- Reacción E2 Paso 1: Oxidación -->
            <path d="M 72 155 L 72 210" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
            <path d="M 12 178 Q 42 178 68 185" fill="none" stroke="#d97706" stroke-width="1.8" marker-end="url(#arrowAmber)"/>
            <text x="8" y="182" fill="#b45309" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ Lipoamida (S-S)</text>
            <g transform="translate(90, 168)">
              <text x="0" y="0" fill="#0f172a" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">E2: Transacetilasa (Oxidación)</text>
              <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">Brazo oscilante de 14 Å</text>
            </g>

            <!-- Intermediario 2: Acetil-Lipoamida -->
            <g transform="translate(10, 215)">
              <rect x="0" y="0" width="160" height="30" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.2"/>
              <text x="80" y="19" fill="#1e293b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Acetil-Lipoamida (E2)</text>
            </g>

            <!-- Reacción E2 Paso 2: Transacetilación a CoA -->
            <path d="M 72 250 L 72 305" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
            <path d="M 12 272 Q 42 272 68 280" fill="none" stroke="#7c3aed" stroke-width="1.8" marker-end="url(#arrowPurple)"/>
            <text x="8" y="276" fill="#7c3aed" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">+ CoA-SH</text>
            <path d="M 78 285 Q 110 295 135 295" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
            <text x="140" y="299" fill="#ea580c" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">➔ Acetil-CoA</text>

            <!-- Intermediario 3: Dihidrolipoamida reducida -->
            <g transform="translate(10, 310)">
              <rect x="0" y="0" width="170" height="30" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
              <text x="85" y="19" fill="#991b1b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Dihidrolipoamida (SH HS)</text>
            </g>

            <!-- Reacción E3: Reoxidación por FAD y NAD+ -->
            <path d="M 72 345 L 72 405" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
            <path d="M 12 365 Q 42 365 68 373" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
            <text x="8" y="369" fill="#475569" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ NAD⁺</text>
            <path d="M 76 380 Q 115 390 140 390" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
            <text x="145" y="394" fill="#059669" font-size="10" font-weight="900" font-family="'Inter', sans-serif">+ NADH + H⁺</text>
            <g transform="translate(85, 355)">
              <text x="0" y="0" fill="#0f172a" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">E3: Dihidrolipoil DH</text>
              <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">FAD prostético ➔ NAD⁺</text>
            </g>

            <!-- Lipoamida regenerada -->
            <g transform="translate(10, 410)">
              <rect x="0" y="0" width="170" height="30" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
              <text x="85" y="19" fill="#15803d" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Lipoamida Oxidada (S-S) ↺</text>
            </g>

            <!-- Retorno cíclico de lipoamida oxidada bordeando por x=275 -->
            <path d="M 185 425 C 275 425, 275 190, 180 190" fill="none" stroke="#d97706" stroke-width="1.8" stroke-dasharray="6 4" marker-end="url(#arrowAmber)"/>
            <text x="282" y="310" fill="#b45309" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" transform="rotate(90 282 310)">↺ CICLO REDOX E2-E3</text>
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
                <path d="M 0 17 L 0 35" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
              </g>

              <!-- Nodo E1 Activa -->
              <g transform="translate(10, 60)">
                <ellipse cx="55" cy="0" rx="55" ry="20" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
                <text x="55" y="-2" fill="#15803d" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">E1 ACTIVA</text>
                <text x="55" y="10" fill="#166534" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Ser-OH (Desfosforilada)</text>
              </g>

              <!-- Flecha PDK Inactivadora arqueada bien por encima -->
              <path d="M 125 44 C 155 12, 205 12, 235 44" fill="none" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
              <g transform="translate(180, 24)">
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

          <!-- 3. Estructura real de Ubiquinona en la bicapa (zona libre) -->
          <g transform="translate(390, 460) scale(0.46)">
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
    partes.append(f'<g id="ruta_lipogenesis">')
    partes.append(badge_via(10, x_lipo - 30, y_lipo - paso_l*2 - 20))

    partes.append(nodo_libre(x_lipo, y_lipo - paso_l*2 - 60, "Citrato (Citosólico)", "6C", CITRATO, "m_citrato_cito", text_right=True, dx=220))
    partes.append(reaccion_libre(x_lipo + 90, y_lipo - paso_l*2 + 65, 52, "ATP Citrato Liasa", entra="+ ATP + CoA", sale="+ OAA", id_rx="rx_acly"))
    partes.append(etiqueta_regulacion("acly", x_lipo + 260, y_lipo - paso_l*2 + 75, dx=0, dy=0))
    
    partes.append(nodo_libre(x_lipo, y_lipo - paso_l, "Acetil-CoA (Citosólico)", "2C", ACETIL_COA, "m_acetil_coa_cito", text_pos="top", dx=60, dy=-22))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo - paso_l + 75, 48, "ACC (Acetil-CoA Carboxilasa)", entra="+ ATP + CO2", sale="+ ADP", id_rx="rx_acc"))
    partes.append(etiqueta_regulacion("acc", x_lipo + 260, y_lipo - paso_l + 85, dx=0, dy=0))
    
    partes.append(f'''
    <!-- Transportador CIC en MMI (Lanzadera de Citrato) -->
    <g id="transportador_cic" data-arrastrable="1" transform="translate(1915, 2115)">
      <rect x="0" y="0" width="60" height="28" rx="7" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <text x="30" y="18" fill="#ffffff" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CIC</text>
    </g>
    ''')

    partes.append(nodo_libre(x_lipo, y_lipo, "Malonil-CoA", "3C", MALONIL_COA, "m_malonil", text_right=True, dx=180))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + 75, 48, "FAS (Condensación)", entra="+ Acetil-CoA", sale="+ CO2", id_rx="rx_fas1"))
    partes.append(etiqueta_regulacion("fas", x_lipo + 220, y_lipo + 85, dx=0, dy=0))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_l, "Acetoacetil-ACP", "4C", ACETOACETIL_ACP, "m_acetoac_acp", text_right=True, dx=190))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_l + 75, 48, "FAS (Reducción 1)", entra="+ NADPH", sale="+ NADP+", id_rx="rx_fas2"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_l*2, "D-β-Hidroxiacil-ACP", "4C", D_BETA_HIDROXIACIL_ACP, "m_hidroxi_acp", text_right=True, dx=190))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_l*2 + 75, 48, "FAS (Deshidratación)", entra="", sale="+ H2O", id_rx="rx_fas3"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_l*3, "Butiril-ACP", "4C", BUTIRIL_ACP, "m_butiril_acp", text_right=True, dx=190))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_l*3 + 75, 48, "FAS (x7 Ciclos)", entra="+ NADPH", sale="+ NADP+", id_rx="rx_fas4"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_l*4, "Palmitato", "16C", PALMITATO_LIBRE, "m_palmitato_libre", text_right=True, dx=255))
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
    <path d="M {x_lipo + 140} 810 C 3500 810, 3500 520, {x_col - 20} 520" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <text x="3340" y="830" fill="#9a3412" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">➔ Vía del Mevalonato (2 Acetil-CoA)</text>
    ''')

    partes.append(nodo_libre(x_col, y_acetoac_col, "Acetoacetil-CoA (Citosol)", "4C", ACETOACETIL_COA_COLEST, "m_acetoac_col", text_pos="top", dx=70, dy=-22))
    partes.append(reaccion_libre(x_col + 60, y_acetoac_col + 65, 45, "HMG-CoA Sintasa (Citosólica)", entra="+ Acetil-CoA", id_rx="rx_hmgs_cito"))

    partes.append(nodo_libre(x_col, y_hmg_col, "HMG-CoA (Citosol)", "6C", HMG_COA_CITOSOL, "m_hmg_col", text_pos="top", dx=70, dy=-22))
    partes.append(reaccion_libre(x_col + 60, y_hmg_col + 65, 48, "HMG-CoA Reductasa (HMGCR)", entra="- 2 NADPH", sale="+ CoA", id_rx="rx_hmgcr"))
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
    partes.append(reaccion_libre(x_box + 60, y_box - 1200 + 80, 50, "Acil-CoA Sintetasa (ACS)", entra="+ ATP + CoA", sale="+ AMP + PPi", id_rx="rx_acs"))
    
    # 2. Palmitoil-CoA Citosólico (Nombre encima de la estructura)
    partes.append(nodo_libre(x_box, y_box - 800, "Palmitoil-CoA (Citosólico)", "16C", PALMITOIL_COA, "m_palmitoil_cito", text_pos="top", dx=110, dy=-22))
    partes.append(reaccion_libre(x_box + 60, y_box - 800 + 80, 50, "CPT-1 (Lanzadera de Carnitina)", entra="+ Carnitina", sale="- CoA", id_rx="rx_cpt1"))
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
    partes.append(reaccion_libre(x_cact, y_cact + 25, 40, "CPT-2 (Cara Interna MMI)", entra="+ CoA", sale="- Carnitina", id_rx="rx_cpt2"))

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
    partes.append(reaccion_libre(x_box + 60, y_m_ceto + 70, 42, "Tiolasa", entra="+ CoA", id_rx="rx_box3"))
    
    # 8. Clivaje tiolítico: Acetil-CoA y Miristoil-CoA
    y_m_split = y_m_ceto + 160
    partes.append(nodo_libre(60, y_m_split, "Acetil-CoA", "2C", ACETIL_COA_BETA, "m_acetil_coa_beta", text_pos="top", dx=50, dy=65))
    partes.append(nodo_libre(230, y_m_split, "Miristoil-CoA", "14C", MIRISTOIL_COA, "m_miristoil_coa", text_pos="top", dx=95, dy=-16))
    
    partes.append(f"""
    <path d="M {x_box+60} {y_m_ceto + 115} L 110 {y_m_split - 22}" stroke="#ea580c" stroke-width="2.6" fill="none" marker-end="url(#arrowFlow)"/>
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
    
    partes.append(nodo_libre(x_ceto, y_ceto, "Acetoacetil-CoA", "4C", ACETOACETIL_COA, "m_acetoac_coa", text_right=True, dx=200))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + 70, 40, "HMG-CoA Sintasa", entra="+ Acetil-CoA", id_rx="rx_ceto1"))
    partes.append(etiqueta_regulacion("hmgcs2", x_ceto + 200, y_ceto + 80, dx=0, dy=0))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c, "HMG-CoA", "6C", HMG_COA, "m_hmg_coa", text_right=True, dx=200))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + paso_c + 70, 40, "HMG-CoA Liasa", sale="+ Acetil-CoA", id_rx="rx_ceto2"))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c*2, "Acetoacetato", "4C", ACETOACETATO, "m_acetoacetato", text_right=True, dx=200))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + paso_c*2 + 70, 40, "β-Hidroxibutirato DH", entra="+ NADH", sale="+ NAD+", id_rx="rx_ceto3"))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c*3, "D-β-Hidroxibutirato", "4C", D_BETA_HIDROXIBUTIRATO, "m_betahidroxi", text_right=True, dx=220))
    
    # Línea rosa de exportación hacia sangre
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        y_ceto_bottom = y_ceto + paso_c*3 + 70
        partes.append(f'''
        <path d="M {x_ceto + 40} {y_ceto + paso_c*3 + 45} L {x_ceto + 40} {y_ceto_bottom} L 35 {y_ceto_bottom} L 35 40" fill="none" stroke="#ec4899" stroke-width="3.2" stroke-dasharray="10 5" marker-end="url(#arrowFlow)"/>
        <text x="22" y="1600" fill="#db2777" font-size="13" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 22 1600)" stroke="none">EXPORTACIÓN DE CUERPOS CETÓNICOS A SANGRE (PARA CEREBRO/MÚSCULO) ➔</text>
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
      <path d="M 2520 1765 Q 2480 1775 2480 1810 L 2480 1995 Q 2480 2010 2465 2010 L 1575 2010 Q 1560 2010 1560 2025 L 1560 3265 Q 1560 3280 1545 3280 L 1260 3280" fill="none" stroke="#16a34a" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
      <text x="2470" y="1805" fill="#15803d" font-size="9.5" font-weight="800" text-anchor="end">Fumarato</text>

      <!-- Rama Cetogénica: Acetoacetato hacia Cetogénesis (m_acetoacetato) -->
      <path d="M 2520 1765 Q 2560 1775 2560 1810 L 2560 2015 Q 2560 2030 2545 2030 L 1015 2030 Q 1000 2030 1000 2045 L 1000 3055 Q 1000 3070 985 3070 L 765 3070 Q 750 3070 750 3085 L 750 3135" fill="none" stroke="#dc2626" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowRed)"/>
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

      <!-- Rama hacia Propionil-CoA (m_prop_aa_matriz en Matriz) -->
      <path id="conn_transsulf_prop" d="M 2810 1715 L 2800 1715 Q 2780 1715 2780 1730 L 2780 2035 Q 2780 2050 2765 2050 L 1035 2050 Q 1020 2050 1020 2065 L 1020 2585 Q 1020 2600 1005 2600 L 795 2600" fill="none" stroke="#16a34a" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>

      <!-- Rama hacia L-Cisteína (nodo citosólico en afluentes a Piruvato) -->
      <path id="conn_transsulf_cys" d="M 2810 1715 L 2810 1745 Q 2810 1760 2825 1760 L 2970 1760 Q 2985 1760 2985 1745 L 2985 625 Q 2985 610 2970 610 L 2385 610 Q 2370 610 2370 595 L 2370 575 Q 2370 565 2362 565" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
    </g>
    ''')

    # -------------------------------------------------------------------------
    # C. MATRIZ MITOCONDRIAL: BCAA Y PROPIONIL-CoA ➔ SUCCINIL-CoA
    # (Zona 100% despejada: X ≈ 590 - 750, Y ≈ 2370 - 2850)
    # -------------------------------------------------------------------------
    # Nodos AA BCAA (Val, Ile)
    partes.append(nodo_aa(610, 2380, "L-Valina", "5C", clasificacion="glu", detalle="BCAA Glucogénico"))
    partes.append(nodo_aa(610, 2420, "L-Isoleucina", "6C", clasificacion="mixto", detalle="BCAA Mixto"))

    # Complejo BCKDH
    partes.append(f'''
    <g id="rx_bckdh" data-arrastrable="1" transform="translate(640, 2470)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <g transform="translate(15, 18)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Complejo BCKDH</text>
        <text x="0" y="12" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">Cofactores: TPP, Lipoamida, FAD</text>
      </g>
    </g>
    ''')
    partes.append(badge_clinico(580, 2515, "[Clínica] MSUD • Jarabe de Arce (BCKDH)", es_alerta=True))

    # Propionil-CoA [3C]
    partes.append(nodo_libre(610, 2570, "Propionil-CoA", "3C", AA_PROPIONIL_COA, "m_prop_aa_matriz", text_pos="top", dx=50, dy=-20))

    # Reacción PCC (Propionil-CoA Carboxilasa)
    partes.append(f'''
    <g id="rx_pcc" data-arrastrable="1" transform="translate(640, 2660)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <path d="M -8 10 Q -25 10 -30 20" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-35" y="15" fill="#dc2626" font-size="8" font-weight="800" text-anchor="end">+ ATP + HCO₃⁻</text>
      <g transform="translate(15, 18)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Propionil-CoA Carboxilasa (PCC)</text>
        <text x="0" y="12" fill="#0284c7" font-size="8.5" font-weight="800">EC 6.4.1.3 (Biotina)</text>
      </g>
    </g>
    ''')

    # Reacción MCM (Metilmalonil-CoA Mutasa)
    partes.append(f'''
    <g id="rx_mcm" data-arrastrable="1" transform="translate(640, 2730)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <g transform="translate(15, 18)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Metilmalonil-CoA Mutasa (MCM)</text>
        <text x="0" y="12" fill="#0284c7" font-size="8.5" font-weight="800">EC 5.4.99.2 (Vitamina B₁₂)</text>
      </g>
    </g>
    ''')
    partes.append(badge_clinico(590, 2770, "[Clínica] Acidemia Metilmalónica • MCM / B₁₂", es_alerta=True))

    # Conexión directa anaplerótica a Succinil-CoA de Krebs
    partes.append(f'''
    <path d="M 640 2800 L 640 2830 L 780 2830" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="790" y="2834" fill="#c2410c" font-size="9.5" font-weight="800">➔ Succinil-CoA [4C] (Krebs)</text>
    ''')

    # Aminoácidos Cetogénicos Puros (Leu, Lys) en Matriz (a la izquierda de Acetoacetil-CoA)
    partes.append(nodo_aa(470, 2870, "L-Leucina", "6C", clasificacion="ceto"))
    partes.append(nodo_aa(470, 2910, "L-Lisina", "6C", clasificacion="ceto"))
    partes.append(f'''
    <path d="M 530 2880 L 620 2865" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
    <text x="390" y="2890" fill="#881337" font-size="8.5" font-weight="800" text-anchor="end">Leu, Lys ➔ Acetoacetil-CoA</text>
    ''')

    # -------------------------------------------------------------------------
    # D. AFLUENTES A PIRUVATO, GLUTAMATO Y OXALACETATO
    # -------------------------------------------------------------------------
    # Afluentes Ser, Gly, Cys, Thr ➔ Piruvato (Zona despejada: X ≈ 2280, Y ≈ 465-580)
    partes.append('''<text x="2280" y="465" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif">Ser, Gly, Cys ➔ Piruvato</text>''')
    partes.append(nodo_aa(2280, 485, "L-Serina", "3C", clasificacion="glu", detalle="Serina deshidratasa (PLP)"))
    partes.append(nodo_aa(2280, 525, "Glicina", "2C", clasificacion="glu", detalle="Sistema escisión (GCS)"))
    partes.append(nodo_aa(2280, 565, "L-Cisteína", "3C", clasificacion="glu", detalle="Desulfuración"))
    partes.append(f'''
    <path d="M 2280 585 C 2280 610, 2220 610, 2180 610" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
    ''')

    # Afluentes Pro, His, Arg ➔ Glutamato (Zona despejada: X ≈ 2040, Y ≈ 760-880)
    partes.append('''<text x="2040" y="760" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif">Pro, His, Arg ➔ Glutamato ➔</text>''')
    partes.append(nodo_aa(2040, 780, "L-Prolina", "5C", clasificacion="glu", detalle="Oxidación a Glutamato"))
    partes.append(nodo_aa(2040, 820, "L-Histidina", "6C", clasificacion="glu", detalle="Histidasa ➔ FIGLU ➔ Glu"))
    partes.append(nodo_aa(2040, 860, "L-Arginina", "6C", clasificacion="glu", detalle="Urea ➔ Ornitina ➔ Glu"))
    partes.append(f'''
    <path d="M 2160 755 L 2255 755" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
    ''')

    # Afluentes Asn, Asp ➔ Oxalacetato (Zona despejada: X ≈ 500, Y ≈ 2215-2260)
    partes.append('''<text x="500" y="2195" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif">Asn, Asp ➔ Oxalacetato ➔</text>''')
    partes.append(nodo_aa(500, 2215, "L-Asparagina", "4C", clasificacion="glu", detalle="Asparaginasa ➔ Aspartato"))
    partes.append(nodo_aa(500, 2255, "L-Aspartato", "4C", clasificacion="glu", detalle="AST / GOT ➔ Oxalacetato"))
    partes.append(f'''
    <path d="M 640 2235 L 720 2235" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
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
    # FASE CITOSÓLICA (Y < 2160)
    # -------------------------------------------------------------------------

    # 5. L-Citrulina en Citosol
    partes.append(nodo_libre(
        x_u_c - 22, 1865,
        "L-Citrulina (Citosol)", "6C",
        UREA_CITRULINA, "m_u_citrulina_cito",
        text_right=True, dx=160,
        detalle="Recibida por SLC25A13 para condensación"
    ))

    # 6. Donador lateral de nitrógeno: L-Aspartato (en carril izquierdo)
    partes.append(nodo_libre(
        3417, 2109,
        "L-Aspartato", "4C",
        UREA_ASPARTATO, "m_u_aspartato",
        text_right=False, dx=-15,
        detalle="Aporta el 2º nitrógeno de la urea"
    ))

    # Reacción 3: ASS (Argininosuccinato Sintetasa)
    partes.append(f'''
    <g id="rx_u_ass" data-arrastrable="1" transform="translate({x_u_c}, 1610)">
      <!-- Flecha ascendente desde Citrulina -->
      <line x1="0" y1="240" x2="0" y2="-10" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Entrada diagonal de L-Aspartato desde carril izquierdo -->
      <path d="M -900 490 Q -300 250 -4 25" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de 1 ATP (lado derecho) -->
      <path d="M 65 65 Q 25 65 4 45" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="70" y="68" fill="#dc2626" font-size="11" font-weight="800" font-family="'Inter', sans-serif">- 1 ATP</text>

      <!-- Salida de AMP + PPi (lado derecho) -->
      <path d="M 4 15 Q 25 5 65 5" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="70" y="9" fill="#475569" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">+ AMP + PPi (➔ 2 Pi)</text>

      <!-- Metadatos de ASS -->
      <g transform="translate(-18, -12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Argininosuccinato</text>
        <text x="0" y="13" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Sintetasa (ASS)</text>
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

    # 8. Fumarato libre resultante (carril izquierdo, X=4080, Y=1340)
    partes.append(nodo_libre(
        x_u_l - 60, 1190,
        "Fumarato", "4C",
        UREA_FUMARATO, "m_u_fumarato",
        text_right=False, dx=-20,
        detalle="Subproducto de escisión trans"
    ))

    # Biciclo de Krebs (Krebs Bicycle Shunt)
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="biciclo_krebs_shunt" data-arrastrable="1">
          <path d="M {x_u_l - 20} 1260 C {x_u_l - 120} 1300, {x_u_l - 120} 1600, {x_u_l - 20} 1640" fill="none" stroke="#ea580c" stroke-width="2.6" stroke-dasharray="7 4" marker-end="url(#arrowFlow)"/>
          <g transform="translate({x_u_l - 120}, 1410)">
            <text x="0" y="0" fill="#c2410c" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">BICICLO DE KREBS ↻</text>
            <text x="0" y="14" fill="#475569" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">+ H₂O (Fumarasa) ➔ L-Malato</text>
            <text x="0" y="27" fill="#475569" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">+ NAD⁺ (MDH1) ➔ OAA</text>
            <text x="0" y="40" fill="#475569" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">+ Glu (GOT1) ➔ Asp</text>
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

      <!-- Flecha curva hacia la derecha hacia Ornitina citosólica (X=4700) -->
      <path d="M 0 50 Q 75 50 140 25" fill="none" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowTeal)"/>
      <text x="45" y="24" fill="#0f766e" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">➔ Retorno Ornitina</text>

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
    partes.append(badge_via(15, x_nuc - 40, 190))
    partes.append(f'''
    <g transform="translate({x_nuc}, 190)" data-arrastrable="1">
      <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="900" font-family="'Inter', sans-serif">BIOSÍNTESIS DE NUCLEÓTIDOS (DE NOVO Y SALVAMENTO)</text>
      <text x="0" y="16" fill="#0284c7" font-size="11" font-weight="800" font-family="'Inter', sans-serif">Rutas convergentes sobre PRPP • Purinas (IMP) y Pirimidinas (UMP)</text>
    </g>
    ''')

    # Enlace hacia Pentosas
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="conexion_pentosas_prpp" data-arrastrable="1">
          <path d="M 2560 880 C 3600 700, 4600 320, 5080 320" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
        </g>
        ''')
    partes.append(f'''
    <text x="{x_nuc + 80}" y="255" fill="#059669" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">➔ de Ribosa-5-P (Vía Pentosas Fosfato)</text>
    ''')

    # 1. PRPP (5-Fosforribosil-1-Pirofosfato)
    partes.append(nodo_libre(x_nuc + 80, 290, "PRPP", "5C", PRPP, "m_nuc_prpp", dx=165, detalle="5-Fosforribosil-1-Pirofosfato"))
    partes.append(reaccion_libre(x_nuc + 130, 410, 45, "PRPP Sintetasa", entra="-1 ATP", sale="+1 AMP", id_rx="rx_prpps"))
    partes.append(etiqueta_regulacion("prpp_s", x_nuc + 240, 420, dx=0, dy=0))

    # 2. IMP (Inosina Monofosfato - Bifurcación purínica)
    partes.append(reaccion_libre(x_nuc + 130, 495, 45, "PRPP Amidotransferasa", entra="+ Gln", sale="+ Glu + PPi", id_rx="rx_prppat"))
    partes.append(etiqueta_regulacion("prpp_at", x_nuc + 310, 505, dx=0, dy=0))
    partes.append(nodo_libre(x_nuc + 80, 575, "Inosina Monofosfato (IMP)", "Base Hipoxantina", IMP, "m_nuc_imp", dx=120, detalle="Punto de ramificación purínica"))

    # 3. Bifurcación hacia AMP (izquierda) y GMP (derecha)
    partes.append(f'''
    <path d="M {x_nuc + 90} 705 Q {x_nuc} 740 {x_nuc - 20} 775" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc - 30}" y="745" fill="#0f172a" font-size="10" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">AdSL (+GTP)</text>
    ''')
    partes.append(nodo_libre(x_nuc - 110, 785, "AMP (Adenosina-5'-P)", "Adenina", NUC_AMP, "m_nuc_amp", text_right=False, dx=-55, detalle="➔ ATP (Energía / ARN)"))

    partes.append(f'''
    <path d="M {x_nuc + 170} 705 Q {x_nuc + 260} 740 {x_nuc + 280} 775" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc + 290}" y="745" fill="#0f172a" font-size="10" font-weight="700" font-family="'Inter', sans-serif">IMPDH (+ATP)</text>
    ''')
    partes.append(nodo_libre(x_nuc + 220, 785, "GMP (Guanosina-5'-P)", "Guanina", NUC_GMP, "m_nuc_gmp", text_right=True, dx=115, detalle="➔ GTP (Señalización / ARN)"))

    # 4. Rama Pirimidinas
    y_pir = 960
    partes.append(reaccion_libre(x_nuc + 50, y_pir, 45, "CPS-II Citosólica", entra="2 ATP + Gln", sale="2 ADP + Glu", id_rx="rx_cps2"))
    partes.append(etiqueta_regulacion("cps2", x_nuc + 205, y_pir + 10, dx=0, dy=0))
    partes.append(nodo_libre(x_nuc - 50, y_pir + 60, "Carbamoil-Fosfato", "Citosol", NUC_CARBAMOIL_P, "m_nuc_cp", dx=115, detalle="Precursor pirimidínico citosólico"))

    partes.append(reaccion_libre(x_nuc + 50, y_pir + 145, 45, "ATCasa ➔ DHODH (MMI)", id_rx="rx_atcasa"))
    partes.append(etiqueta_regulacion("atcasa", x_nuc + 235, y_pir + 155, dx=0, dy=0))
    partes.append(nodo_libre(x_nuc - 50, y_pir + 205, "Ácido Orotato", "Anillo Pirimidina", NUC_OROTATO, "m_nuc_orotato", dx=115, detalle="DHODH acoplada a CoQ en MMI"))

    partes.append(reaccion_libre(x_nuc + 50, y_pir + 295, 45, "UMP Sintasa (OPRT + ODC)", entra="+ PRPP", sale="- CO₂", id_rx="rx_umps"))
    partes.append(nodo_libre(x_nuc - 50, y_pir + 355, "UMP (Uridina Monofosfato)", "Uracilo", NUC_UMP, "m_nuc_ump", dx=115, detalle="Precursor común pirimidinas"))

    # Bifurcación UMP ➔ CTP y dTMP
    partes.append(f'''
    <path d="M {x_nuc - 37} {y_pir + 472} Q {x_nuc - 51} {y_pir + 486} {x_nuc - 60} {y_pir + 500}" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc - 70}" y="{y_pir + 475}" fill="#0f172a" font-size="10" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">CTP Sintetasa (+Gln)</text>
    ''')
    partes.append(nodo_libre(x_nuc - 140, y_pir + 530, "CTP (Citidina-5'-P)", "Citosina", NUC_CTP, "m_nuc_ctp", text_right=False, dx=-55, detalle="Precursor de ARN / Lípidos"))

    partes.append(f'''
    <path d="M {x_nuc + 120} {y_pir + 440} Q {x_nuc + 160} {y_pir + 470} {x_nuc + 180} {y_pir + 500}" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc + 190}" y="{y_pir + 475}" fill="#0f172a" font-size="10" font-weight="700" font-family="'Inter', sans-serif">RNR ➔ Timidilato Sintasa</text>
    ''')
    partes.append(nodo_libre(x_nuc + 130, y_pir + 530, "dTMP (Timidilato)", "Timina [ADN]", NUC_DTMP, "m_nuc_dtmp", text_right=True, dx=145, detalle="Diana 5-FU y Metotrexato"))
    partes.append(etiqueta_regulacion("ts", x_nuc + 280, y_pir + 600, dx=0, dy=0))

    partes.append(f'</g>')

    # =========================================================================
    # 16. RUTA 16: CATABOLISMO DE NUCLEÓTIDOS Y ÁCIDO ÚRICO
    # =========================================================================
    partes.append(f'<g id="ruta_degradacion_nucleotidos">')
    
    y_deg = 1720
    partes.append(badge_via(16, x_nuc - 40, y_deg))
    partes.append(f'''
    <g transform="translate({x_nuc}, {y_deg})" data-arrastrable="1">
      <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="900" font-family="'Inter', sans-serif">CATABOLISMO DE NUCLEÓTIDOS Y ÁCIDO ÚRICO</text>
      <text x="0" y="16" fill="#dc2626" font-size="11" font-weight="800" font-family="'Inter', sans-serif">Convergencia en XOD ➔ Ácido Úrico (Gota) y Apertura Soluble (β-Alanina)</text>
    </g>
    ''')

    # Degradación de Purinas: Hipoxantina ➔ Xantina ➔ Ácido Úrico
    partes.append(nodo_libre(x_nuc + 30, y_deg + 60, "Hipoxantina (de AMP)", "Purina", HIPOXANTINA, "m_deg_hipo", dx=115, detalle="Vía ADA (diana SCID)"))
    partes.append(etiqueta_regulacion("ada", x_nuc + 160, y_deg + 130, dx=0, dy=0))

    partes.append(reaccion_libre(x_nuc + 80, y_deg + 155, 45, "XOD (Paso 1)", entra="+ O₂", sale="+ H₂O₂", id_rx="rx_xod1"))
    partes.append(nodo_libre(x_nuc + 30, y_deg + 215, "Xantina", "Dioxipurina", XANTINA, "m_deg_xantina", dx=115, detalle="Convergencia de Adenina y Guanina"))

    partes.append(reaccion_libre(x_nuc + 80, y_deg + 305, 45, "XOD (Paso 2 · Alopurinol)", entra="+ O₂", sale="+ H₂O₂", id_rx="rx_xod2"))
    partes.append(etiqueta_regulacion("xod", x_nuc + 270, y_deg + 315, dx=0, dy=0))
    partes.append(nodo_libre(x_nuc + 30, y_deg + 370, "ÁCIDO ÚRICO (URATO)", "Trioxipurina", ACIDO_URICO, "m_deg_urato", dx=115, detalle="Poco soluble · Precipita en gota"))

    # Trazo de excreción renal de Urato hacia el torrente vascular capilar superior
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="excrecion_urato_sangre" data-arrastrable="1">
          <path d="M {x_nuc + 120} {y_deg + 370} C {x_nuc + 380} {y_deg + 180}, {x_nuc + 480} 500, {x_nuc + 480} 74" fill="none" stroke="#dc2626" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowRed)"/>
        </g>
        ''')
    partes.append(f'''
    <g id="indicador_urato_excrecion" transform="translate({x_nuc + 160}, {y_deg + 370})">
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

    # Degradación de Pirimidinas (Apertura de cadena soluble)
    y_deg_pir = y_deg + 530
    partes.append(nodo_libre(x_nuc + 30, y_deg_pir, "Uracilo / Citosina", "Pirimidina libre", DEG_URACILO, "m_deg_uracilo", dx=115, detalle="Sustrato de DPD (NADPH)"))
    partes.append(reaccion_libre(x_nuc + 80, y_deg_pir + 85, 45, "Dihidropirimidina DH (DPD)", entra="+ NADPH", sale="+ NADP⁺", id_rx="rx_dpd"))
    
    partes.append(reaccion_libre(x_nuc + 80, y_deg_pir + 165, 45, "DHPasa (Apertura hidrolítica)", entra="+ H₂O", id_rx="rx_dhpasa"))
    partes.append(nodo_libre(x_nuc + 30, y_deg_pir + 225, "β-Ureidopropionato", "Cadena abierta acíclica", BETA_UREIDOPROPIONATO, "m_deg_ureido", dx=175, detalle="Apertura hidrolítica del anillo"))

    partes.append(reaccion_libre(x_nuc + 80, y_deg_pir + 315, 45, "β-Ureidopropionasa", entra="+ H₂O", sale="+ NH₄⁺ + CO₂", id_rx="rx_ureidopropionasa"))
    partes.append(nodo_libre(x_nuc + 30, y_deg_pir + 375, "β-Alanina Soluble", "Producto soluble", BETA_ALANINA, "m_deg_beta_ala", dx=120, detalle="Excreción inocua en orina"))

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
    partes.append(generar_bloque_leyenda(100, 4230))
    partes.append(generar_bloque_autoria(4950, 4230))

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
