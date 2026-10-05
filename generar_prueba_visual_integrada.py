#!/usr/bin/env python3
"""
GENERADOR DE PRUEBA VISUAL INTEGRADA (ENTORNO BIOLÓGICO REAL - SIN GLOBOS NI CAJAS)
==================================================================================
Implementa fielmente el diseño orgánico celular:
- Fondo acuoso citosólico continuo con gradientes biológicos y halo citoplasmático.
- Membrana plasmática ondulada continua bicapa lipídica arriba, con receptor GLUT-4 y su lupa molecular.
- Citoesqueleto y polirribosomas tenues flotando libremente.
- Gran Mitocondria anatómica arriñonada con doble membrana (MME y MMI con espacio intermembrana) y crestas onduladas.
- TODAS las moléculas y estructuras químicas flotan LIBRES en el espacio biológico:
  * CERO globos, CERO tarjetas blancas, CERO cajas envolventes o marcos artificiales.
  * Texto mínimo: Nombre del metabolito, conteo de carbonos [6C], enzima concisa y arcos de energía.
  * Agrupaciones con 'data-arrastrable="1"' para mover en editor_arrastrable.html.
"""

import os
import sys

DIR_BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "01_glucolisis"))
sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "03_glucogenogenesis_y_glucogenolisis"))
sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "04_via_pentosas_fosfato"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "02_ciclo_de_krebs"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "03_cadena_transporte_electrones_y_atp_sintasa"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "04_lanzaderas_malato_aspartato_y_glicerol_p"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "01_beta_oxidacion"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "02_sintesis_acidos_grasos_lipogenesis"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "03_cetogenesis_y_cetolisis"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "04_colesterol_y_lipoproteinas"))
sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "01_transaminacion_y_desaminacion"))
sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "02_ciclo_de_la_urea"))

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
    MEVALONATO, ISOPENTENIL_PP, FARNESIL_PP, ESCUALENO, LANOSTEROL, COLESTEROL
)

ANCHO_CANVAS = 4900
ALTO_CANVAS = 4200

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

def generar_bloque_autoria(x=3820, y=3540):
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
        <text x="67" y="15" fill="#475569" font-size="10" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">⚖ Licencia MIT</text>
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
    Carga directamente el diseño original exacto del archivo SVG que el usuario ya realizó:
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
    </g>

    <!-- Albúmina sérica y Lipoproteínas en el plasma -->
    <g opacity="0.6">
      <ellipse cx="420" cy="24" rx="16" ry="11" fill="#fef08a" stroke="#ca8a04" stroke-width="1.2"/>
      <text x="420" y="27" fill="#854d0e" font-size="7.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">ALBÚMINA</text>
      <ellipse cx="2950" cy="28" rx="18" ry="12" fill="#fed7aa" stroke="#ea580c" stroke-width="1.2"/>
      <text x="2950" y="32" fill="#9a3412" font-size="7.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">VLDL / HDL</text>
    </g>

    <!-- Rótulo Principal del Torrente Sanguíneo -->
    <g transform="translate(60, 32)">
      <rect x="0" y="-18" width="370" height="28" rx="6" fill="#450a0a" stroke="#b91c1c" stroke-width="1.5" opacity="0.85"/>
      <text x="14" y="2" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#fecaca" letter-spacing="2.5">
        🩸 TORRENTE SANGUÍNEO (LUMEN VASCULAR)
      </text>
    </g>

    <!-- ================================================================= -->
    <!-- MEMBRANA PLASMÁTICA CONTINUA Y CANAL GLUT-4 (ARRIBA)              -->
    <!-- ================================================================= -->
    <!-- Doble Bicapa Fosfolipídica Ondulada (Límite Celular) -->
    <path d="M 0 68 Q {ANCHO_CANVAS*0.25} 95 {ANCHO_CANVAS*0.5} 68 T {ANCHO_CANVAS} 68" fill="none" stroke="#0284c7" stroke-width="10" stroke-linecap="round"/>
    <path d="M 0 78 Q {ANCHO_CANVAS*0.25} 105 {ANCHO_CANVAS*0.5} 78 T {ANCHO_CANVAS} 78" fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>

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
    <line x1="1680" y1="122" x2="1680" y2="150" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

    <!-- Lupa Molecular del GLUT-4 (Difusión facilitada) -->
    <g stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.7">
      <line x1="1640" y1="95" x2="1490" y2="120" />
      <line x1="1650" y1="75" x2="1460" y2="70" />
    </g>
    <g transform="translate(1390, 115)">
      <circle cx="0" cy="0" r="72" fill="#ffffff" stroke="#0284c7" stroke-width="3.5"/>
      <circle cx="0" cy="0" r="68" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2"/>
      <path d="M -20 -24 C -10 -28, -5 -16, -5 0 C -5 16, -10 28, -20 24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <path d="M 20 -24 C 10 -28, 5 -16, 5 0 C 5 16, 10 28, 20 24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <ellipse cx="0" cy="0" rx="7" ry="18" fill="#bae6fd" opacity="0.6"/>
      <text x="0" y="58" fill="#0369a1" font-size="8.5" font-weight="900" text-anchor="middle" letter-spacing="1">DIFUSIÓN FACILITADA</text>
    </g>
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

      <!-- Rótulo de la Matriz integrado orgánicamente (despejado en la zona superior de la matriz sobre Krebs) -->
      <g transform="translate(1140, {y_mito + 45})" opacity="0.85">
        <text x="0" y="0" fill="#78350f" font-size="22" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="4" text-anchor="middle">MATRIZ MITOCONDRIAL</text>
        <text x="0" y="20" fill="#92400e" font-size="12" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Oxidación celular • Descarboxilación • Respiración</text>
      </g>

      <!-- Transportador MPC en el punto de contacto con el Piruvato (X=1680) -->
      <g transform="translate(1645, {y_mito - 55})">
        <rect x="0" y="0" width="70" height="42" rx="10" fill="#92400e" stroke="#78350f" stroke-width="2.5"/>
        <text x="35" y="27" fill="#ffffff" font-size="16" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MPC</text>
      </g>
      <text x="1730" y="{y_mito - 30}" fill="#78350f" font-size="12" font-weight="800" font-family="'Inter', sans-serif">Carrier de Piruvato (MPC1/2)</text>
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
    partes.append(reaccion_libre(x_g, y_g + 105, 52, "Hexocinasa", entra="-1 ATP", sale="+1 ADP", id_rx="rx_hk"))

    # 2. G6P
    partes.append(nodo_libre(x_g - 40, y_g + paso_y, "Glucosa-6-Fosfato", "6C", GLUCOSA_6_FOSFATO, "m_g6p"))
    partes.append(reaccion_libre(x_g, y_g + paso_y + 105, 52, "Fosfoglucosa Isomerasa", reversible=True, id_rx="rx_pgi"))

    # 3. F6P
    partes.append(nodo_libre(x_g - 40, y_g + paso_y * 2, "Fructosa-6-Fosfato", "6C", FRUCTOSA_6_FOSFATO, "m_f6p"))
    partes.append(reaccion_libre(x_g, y_g + paso_y * 2 + 105, 52, "PFK-1", entra="-1 ATP", sale="+1 ADP", id_rx="rx_pfk1"))

    # 4. F-1,6-BP
    partes.append(nodo_libre(x_g - 40, y_g + paso_y * 3, "Fructosa-1,6-Bisfosfato", "6C", FRUCTOSA_1_6_BISFOSFATO, "m_fbp"))
    partes.append(reaccion_libre(x_g, y_g + paso_y * 3 + 105, 52, "Aldolasa", reversible=True, id_rx="rx_aldo"))

    # 5. DHAP y GAP
    partes.append(nodo_libre(x_g - 250, y_g + paso_y * 4, "Dihidroxiacetona-P", "3C", DIHIDROXIACETONA_FOSFATO, "m_dhap", text_right=False))
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 4, "Gliceraldehído-3-P", "3C", GLICERALDEHIDO_3_FOSFATO, "m_gap"))
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

    # 10. Piruvato (Citosol)
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 9, "Piruvato", "3C", PIRUVATO, "m_pyr_cito"))

    # Flecha Piruvato Citosol ➔ MPC (entra directo al centro del transportador en x=1680)
    partes.append(f"""
    <path d="M {x_g + 220} {y_g + paso_y * 9 + 100} Q {x_g + 120} {y_g + paso_y * 9 + 135}, 1680 {y_mito - 60}" fill="none" stroke="#ea580c" stroke-width="3" stroke-dasharray="10 6" marker-end="url(#arrowFlow)"/>
    """)
    partes.append('</g>')

    # =========================================================================
    # 4. IZQUIERDA: METABOLISMO DEL GLUCÓGENO (LIBRE EN CITOSOL)
    # =========================================================================
    x_glc = 520
    y_glc = 340
    partes.append(f'<g id="ruta_glucogeno">')
    
    # G1P
    partes.append(nodo_libre(x_glc + 450, y_glc, "Glucosa-1-Fosfato", "6C", GLUCOSA_1_FOSFATO, "m_g1p"))

    # Conexión G6P ⇄ G1P
    partes.append(f"""
    <g id="rx_pgm_glucogeno" data-arrastrable="1">
      <path d="M {x_g - 75} {y_g + paso_y + 35} L {x_glc + 630} {y_glc + 35}" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <text x="{(x_g - 75 + x_glc + 630)//2}" y="{y_glc + 20}" fill="#b45309" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Fosfoglucomutasa ⇄</text>
    </g>
    """)

    # UDP-Glucosa (nombre arriba, estructura centrada y flecha de pirofosforilasa arqueada por encima)
    y_udpg = y_glc - 70
    partes.append(nodo_libre(x_glc + 120, y_udpg, "UDP-Glucosa", "6C", UDP_GLUCOSA, "m_udpg", text_pos="top", dx=130, dy=-18))
    partes.append(f"""
    <g id="rx_udpg" data-arrastrable="1">
      <path d="M {x_glc + 450} {y_glc + 20} C {x_glc + 410} {y_udpg - 45}, {x_glc + 320} {y_udpg - 45}, {x_glc + 270} {y_udpg - 5}" fill="none" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="{x_glc + 365}" y="{y_udpg - 55}" fill="#d97706" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">UDP-Glucosa Pirofosforilasa (+UTP)</text>
    </g>
    """)

    # Cadena de Glucógeno
    partes.append(nodo_libre(x_glc - 80, y_glc + 220, "Glucógeno (n+1)", "Polímero", CADENA_GLUCOGENO, "m_glucogeno_cadena"))
    partes.append(f"""
    <g id="rx_sintesis_degradacion_glucogeno" data-arrastrable="1">
      <!-- Síntesis -->
      <path d="M {x_glc + 150} {y_udpg + 65} Q {x_glc + 70} {y_glc + 150} {x_glc + 10} {y_glc + 215}" fill="none" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="{x_glc + 120}" y="{y_glc + 145}" fill="#b45309" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">Glucógeno Sintasa</text>

      <!-- Glucogenólisis (degradación) -->
      <path d="M {x_glc + 80} {y_glc + 310} Q {x_glc + 320} {y_glc + 360} {x_glc + 500} {y_glc + 85}" fill="none" stroke="#ea580c" stroke-width="2.2" stroke-dasharray="7 5" marker-end="url(#arrowFlow)"/>
      <text x="{x_glc + 330}" y="{y_glc + 345}" fill="#c2410c" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">Glucógeno Fosforilasa (+Pi ➔ G1P)</text>
    </g>
    """)
    partes.append('</g>')

    # =========================================================================
    # 5. DERECHA: VÍA DE LAS PENTOSAS FOSFATO (LIBRE EN CITOSOL)
    # =========================================================================
    x_p = 2580
    y_p = 300
    partes.append(f'<g id="ruta_pentosas">')

    # Entrada G6PDH desde G6P
    partes.append(f"""
    <g id="rx_g6pdh" data-arrastrable="1">
      <path d="M {x_g + 140} {y_g + paso_y + 35} L {x_p - 40} {y_p + 35}" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>
      <text x="{(x_g + 140 + x_p - 40)//2}" y="{y_p + 20}" fill="#059669" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">G6PDH (+ NADP⁺ ➔ + NADPH + H⁺)</text>
    </g>
    """)

    # 1. Lactona
    partes.append(nodo_libre(x_p, y_p, "6-P-Gluconolactona", "6C", FOSFOGLUCONO_LACTONA_6, "m_lactona", text_right=True, dx=145))
    partes.append(reaccion_libre(x_p + 50, y_p + 105, 36, "Lactonasa (+ H₂O)", id_rx="rx_lactonasa"))

    # 2. 6-Fosfogluconato
    partes.append(nodo_libre(x_p, y_p + 160, "6-Fosfogluconato", "6C", FOSFOGLUCONATO_6, "m_6pg", text_right=True, dx=145))
    partes.append(reaccion_libre(x_p + 50, y_p + 315, 36, "6-Fosfogluconato DH (+ NADP⁺ ➔ + NADPH + CO₂)", es_ganancia=True, id_rx="rx_6pgdh"))

    # 3. Ribulosa-5-P
    partes.append(nodo_libre(x_p, y_p + 370, "Ribulosa-5-Fosfato", "5C", RIBULOSA_5_FOSFATO, "m_ru5p", text_right=True, dx=145))

    # Ramas: Xilulosa-5P y Ribosa-5P (texto de Xilulosa superior para despejar el canal citosólico)
    partes.append(nodo_libre(x_p - 110, y_p + 500, "Xilulosa-5-P", "5C", XILULOSA_5_FOSFATO, "m_xu5p", text_pos="top", dy=-20))
    partes.append(nodo_libre(x_p + 280, y_p + 500, "Ribosa-5-P", "5C", RIBOSA_5_FOSFATO, "m_r5p"))
    partes.append(f"""
    <path d="M {x_p + 20} {y_p + 430} L {x_p - 50} {y_p + 495}" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="{x_p - 50}" y="{y_p + 460}" fill="#047857" font-size="10.5" font-family="'Inter', sans-serif" text-anchor="end">Fosfopentosa Epimerasa</text>

    <path d="M {x_p + 80} {y_p + 430} L {x_p + 270} {y_p + 495}" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="{x_p + 200}" y="{y_p + 460}" fill="#047857" font-size="10.5" font-family="'Inter', sans-serif">Fosfopentosa Isomerasa</text>
    """)

    # Sedoheptulosa-7P y Eritrosa-4P (texto de Sedoheptulosa superior para despejar el canal citosólico)
    partes.append(nodo_libre(x_p - 110, y_p + 660, "Sedoheptulosa-7-P", "7C", SEDOHEPTULOSA_7_FOSFATO, "m_s7p", text_pos="top", dy=-20))
    partes.append(nodo_libre(x_p + 280, y_p + 660, "Eritrosa-4-P", "4C", ERITROSA_4_FOSFATO, "m_e4p"))
    partes.append(f"""
    <text x="{x_p + 90}" y="{y_p + 600}" fill="#047857" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Transcetolasa 1 (TK1) ⇄</text>
    <text x="{x_p + 90}" y="{y_p + 760}" fill="#047857" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Transaldolasa ⇄ Retorno a F6P y GAP</text>

    <!-- Retornos de Transaldolasa y Transcetolasa hacia Glucólisis (rutas despejadas sin colisiones) -->
    <path d="M {x_p - 140} {y_p + 760} C 2420 700, 2350 455, 2180 455 C 2060 455, 1940 475, {x_g + 160} {y_g + paso_y * 2 + 35}" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <text x="2020" y="440" fill="#059669" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Retorno a Glucólisis: Fructosa-6-P ➔</text>

    <path d="M {x_p - 140} {y_p + 800} C 2280 1100, 2120 920, {x_g + 200} {y_g + paso_y * 4 + 35}" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <text x="2350" y="1080" fill="#059669" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Retorno a Glucólisis: GAP ➔</text>
    """)
    partes.append('</g>')

    # =========================================================================
    # 6. LANZADERA MALATO-ASPARTATO: LUPA MOLECULAR CON ZOOM DIDÁCTICO
    # =========================================================================
    cx_lupa = 780
    cy_lupa = 1530
    r_lupa = 310
    x_ancla_mmi = 780
    y_ancla_mmi = y_mito - 30

    partes.append(f"""
    <!-- ================================================================= -->
    <!-- LUPA DE AUMENTO MOLECULAR: LANZADERA MALATO-ASPARTATO             -->
    <!-- ================================================================= -->
    <g id="lupa_lanzadera_malato_aspartato" data-arrastrable="1">

      <!-- 1. Punto de Anclaje sobre la Membrana Mitocondrial Real -->
      <g id="ancla_lanzadera_mmi" transform="translate({x_ancla_mmi}, {y_ancla_mmi})">
        <rect x="-55" y="-18" width="110" height="36" rx="8" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
        <text x="0" y="5" fill="#ffffff" font-size="13" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">OGC / AGC</text>
        <circle cx="0" cy="0" r="28" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 3"/>
        <text x="0" y="34" fill="#78350f" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Lanzadera Malato-Aspartato</text>
      </g>

      <!-- 2. Rayos de Proyección Cónica hacia la Lente Circular de Zoom -->
      <g stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="6 4" opacity="0.75" fill="none">
        <line x1="{x_ancla_mmi - 55}" y1="{y_ancla_mmi}" x2="{cx_lupa - r_lupa * 0.7}" y2="{cy_lupa + r_lupa * 0.7}"/>
        <line x1="{x_ancla_mmi + 55}" y1="{y_ancla_mmi}" x2="{cx_lupa + r_lupa * 0.7}" y2="{cy_lupa + r_lupa * 0.7}"/>
      </g>

      <!-- 3. Cuerpo y Bisel de la Lente de Zoom -->
      <circle cx="{cx_lupa}" cy="{cy_lupa}" r="{r_lupa + 8}" fill="#ffffff" stroke="#0284c7" stroke-width="6"/>
      <circle cx="{cx_lupa}" cy="{cy_lupa}" r="{r_lupa + 2}" fill="none" stroke="#38bdf8" stroke-width="2.2" stroke-dasharray="8 4"/>

      <!-- ClipPath para recortar el interior de la lupa -->
      <defs>
        <clipPath id="clipLupaLanzadera">
          <circle cx="{cx_lupa}" cy="{cy_lupa}" r="{r_lupa}"/>
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
            🔍 LUPA MOLECULAR: LANZADERA MALATO-ASPARTATO
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

    # Complejo PDH (Transición MPC ➔ Acetil-CoA)
    partes.append(f"""
    <!-- Reacción PDH -->
    <path d="M 1680 {y_mito - 10} C 1680 {y_k - 20}, {x_k + 400} {y_k - 20}, {x_k + 370} {y_k + 10}" fill="none" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    <text x="{x_k + 500}" y="{y_k - 5}" fill="#c2410c" font-size="13" font-weight="900" font-family="'Inter', sans-serif">Complejo PDH (E1, E2, E3)</text>
    <text x="{x_k + 500}" y="{y_k + 14}" fill="#64748b" font-size="11" font-family="'Inter', sans-serif">+ CoA-SH + NAD⁺ ➔ CO₂ + NADH</text>
    """)

    # Acetil-CoA
    partes.append(nodo_libre(x_k + 240, y_k + 15, "Acetil-CoA", "2C", ACETIL_COA, "m_accoa", text_right=True, dx=170))

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

    # Alfa-Cetoglutarato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 3, "α-Cetoglutarato", "5C", KREBS_ALFA_CETOGLUTARATO, "m_akg", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 3 + 130, 38, "α-KG Deshidrogenasa", entra="+ CoA + NAD⁺", sale="+ NADH + CO₂", es_ganancia=True, id_rx="rx_akgdh", text_dx=-16, text_anchor="end"))

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
    partes.append(f"""
    <g id="rx_mdh_retorno" data-arrastrable="1">
      <path d="M {x_k} {y_k + paso_k * 7 + 60} C {x_k - 300} {y_k + paso_k * 7 + 60}, {x_k - 300} {y_k + 60}, {x_k - 240} {y_k + 60}" fill="none" stroke="#b45309" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <text x="{x_k - 310}" y="{y_k + paso_k * 4}" fill="#78350f" font-size="12" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 {x_k - 310} {y_k + paso_k * 4})">
        Malato DH (+ NAD⁺ ➔ + NADH + H⁺)
      </text>
    </g>
    """)
    partes.append('</g>')

    # =========================================================================
    # 8. MATRIZ DERECHA: CADENA RESPIRATORIA REAL DEL USUARIO (CON ZOOM)
    # =========================================================================
    cte_defs, cte_body = cargar_cte_original_usuario()

    x_ancla_cresta = 2480
    y_ancla_cresta = y_mito + 25

    x_cte_marco = 2400
    y_cte_marco = 2440
    w_cte_marco = 1190
    h_cte_marco = 820

    partes.append(f"""
    <!-- ================================================================= -->
    <!-- CADENA TRANSPORTADORA DE ELECTRONES Y ATP SINTASA (DISEÑO REAL)    -->
    <!-- ================================================================= -->
    <g id="lupa_cadena_respiratoria" data-arrastrable="1">

      <!-- 1. Punto de Anclaje sobre la Cresta Mitocondrial Real -->
      <g id="ancla_cresta_mmi" transform="translate({x_ancla_cresta}, {y_ancla_cresta})">
        <rect x="-65" y="-18" width="130" height="36" rx="10" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
        <text x="0" y="5" fill="#ffffff" font-size="12.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CRESTA MMI</text>
        <circle cx="0" cy="0" r="28" fill="none" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 3"/>
        <text x="0" y="34" fill="#78350f" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Cresta Respiratoria: Complejos I–IV &amp; F₀F₁</text>
      </g>

      <!-- 2. Rayos de Proyección Cónica hacia la Lente Panorámica -->
      <g stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="6 4" opacity="0.75" fill="none">
        <line x1="{x_ancla_cresta - 65}" y1="{y_ancla_cresta}" x2="{x_cte_marco + 100}" y2="{y_cte_marco}"/>
        <line x1="{x_ancla_cresta + 65}" y1="{y_ancla_cresta}" x2="{x_cte_marco + w_cte_marco - 100}" y2="{y_cte_marco}"/>
      </g>

      <!-- 3. Flecha de Flujo desde Krebs hacia la Lupa de la CTE -->
      <path d="M {x_k + 280} {y_k + paso_k * 3} C 1700 {y_k + paso_k * 3}, 1880 {y_cte_marco + 200}, {x_cte_marco} {y_cte_marco + 220}" fill="none" stroke="#059669" stroke-width="3.2" stroke-dasharray="10 6" marker-end="url(#arrowGreen)"/>
      <g transform="translate(1780, {y_k + paso_k * 3 - 5})">
        <rect x="-10" y="-16" width="270" height="28" rx="8" fill="#f0fdf4" stroke="#059669" stroke-width="1.6"/>
        <text x="125" y="3" fill="#047857" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">NADH &amp; FADH₂ de Krebs ➔</text>
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
          🔍 CADENA TRANSPORTADORA DE ELECTRONES Y ATP SINTASA (DISEÑO ORIGINAL)
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

    partes.append(nodo_libre(x_lipo, y_lipo - paso_l*2, "Citrato (Citosólico)", "6C", CITRATO, "m_citrato_cito", text_right=True, dx=175))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo - paso_l*2 + 75, 48, "ATP Citrato Liasa", entra="+ ATP + CoA", sale="+ OAA", id_rx="rx_acly"))
    
    partes.append(nodo_libre(x_lipo, y_lipo - paso_l, "Acetil-CoA (Citosólico)", "2C", ACETIL_COA, "m_acetil_coa_cito", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo - paso_l + 75, 48, "ACC (Acetil-CoA Carboxilasa)", entra="+ ATP + CO2", sale="+ ADP", id_rx="rx_acc"))
    
    partes.append(f'''
    <!-- Lanzadera de Citrato: Translocación desde matriz a citosol vía transportador CIC en MMI (X=1915), evitando MPC -->
    <path d="M 1250 2380 C 1500 2380, 1750 2260, 1945 2140 C 2080 1980, 2500 1300, {x_lipo - 30} 690" fill="none" stroke="#0ea5e9" stroke-width="2.6" stroke-dasharray="10 5" marker-end="url(#arrowBlue)"/>
    <g id="transportador_cic" data-arrastrable="1" transform="translate(1915, 2115)">
      <rect x="0" y="0" width="60" height="28" rx="7" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <text x="30" y="18" fill="#ffffff" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CIC</text>
    </g>
    <text x="1945" y="2100" fill="#0284c7" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Lanzadera de Citrato ➔</text>
    ''')

    partes.append(nodo_libre(x_lipo, y_lipo, "Malonil-CoA", "3C", MALONIL_COA, "m_malonil", text_right=True, dx=180))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + 75, 48, "FAS (Condensación)", entra="+ Acetil-CoA", sale="+ CO2", id_rx="rx_fas1"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_l, "Acetoacetil-ACP", "4C", ACETOACETIL_ACP, "m_acetoac_acp", text_right=True))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_l + 75, 48, "FAS (Reducción 1)", entra="+ NADPH", sale="+ NADP+", id_rx="rx_fas2"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_l*2, "D-β-Hidroxiacil-ACP", "4C", D_BETA_HIDROXIACIL_ACP, "m_hidroxi_acp", text_right=True))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_l*2 + 75, 48, "FAS (Deshidratación)", entra="", sale="+ H2O", id_rx="rx_fas3"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_l*3, "Butiril-ACP", "4C", BUTIRIL_ACP, "m_butiril_acp", text_right=True))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_l*3 + 75, 48, "FAS (x7 Ciclos)", entra="+ NADPH", sale="+ NADP+", id_rx="rx_fas4"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_l*4, "Palmitato", "16C", PALMITATO_LIBRE, "m_palmitato_libre", text_right=True))
    partes.append(f'</g>')

    # =========================================================================
    # 9B. LÍPIDOS: SÍNTESIS DE COLESTEROL (CITOSOL Y MEMBRANA DEL REL)
    # =========================================================================
    # Se ramifica directamente desde el pool citosólico de Acetil-CoA
    x_col = 3560
    y_col = 920
    paso_col = 165
    partes.append(f'<g id="ruta_colesterol">')
    
    # Conexión desde Acetil-CoA citosólico hacia la vía del colesterol
    partes.append(f'''
    <path d="M {x_lipo + 100} {y_lipo - paso_l + 30} Q {x_col - 80} {y_lipo - paso_l + 30}, {x_col} {y_col}" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <text x="3340" y="{y_lipo - paso_l + 15}" fill="#9a3412" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">➔ Vía del Mevalonato</text>
    ''')

    # Mevalonato (producto irreversible del marcapasos HMGCR)
    partes.append(nodo_libre(x_col, y_col, "Mevalonato", "6C", MEVALONATO, "m_mevalonato_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_col + 75, 45, "Mevalonato Quinasa / Descarboxilasa", entra="- 3 ATP", sale="+ CO2 + Pi", id_rx="rx_col1"))
    
    # Isopentenil Pirofosfato (IPP)
    partes.append(nodo_libre(x_col, y_col + paso_col, "Isopentenil-PP (IPP)", "5C", ISOPENTENIL_PP, "m_ipp_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_col + paso_col + 75, 45, "Preniltransferasas", entra="+ 2 IPP", sale="+ 2 PPi", id_rx="rx_col2"))
    
    # Farnesil Pirofosfato (FPP)
    partes.append(nodo_libre(x_col, y_col + paso_col*2, "Farnesil-PP (FPP)", "15C", FARNESIL_PP, "m_fpp_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_col + paso_col*2 + 75, 45, "Escualeno Sintasa", entra="- NADPH", sale="+ 2 PPi", es_ganancia=False, id_rx="rx_col3"))
    
    # Escualeno
    partes.append(nodo_libre(x_col, y_col + paso_col*3, "Escualeno", "30C", ESCUALENO, "m_escualeno_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_col + paso_col*3 + 75, 45, "Oxidoscualeno Ciclasa", entra="- NADPH + O2", sale="+ H2O", id_rx="rx_col4"))
    
    # Lanosterol
    partes.append(nodo_libre(x_col, y_col + paso_col*4, "Lanosterol", "30C", LANOSTEROL, "m_lanosterol_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_col + paso_col*4 + 75, 45, "Vías de Bloch &amp; Kandutsch (19 pasos)", entra="- NADPH + O2", sale="+ 3 CO2", id_rx="rx_col5"))
    
    # Colesterol Final
    partes.append(nodo_libre(x_col, y_col + paso_col*5, "COLESTEROL", "27C", COLESTEROL, "m_colesterol_integ", text_pos="top", dy=-18))
    
    # Conexiones funcionales de destino del Colesterol (asciende por X=3860 hasta la membrana plasmática en Y=74)
    partes.append(f'''
    <path d="M {x_col + 240} {y_col + paso_col*5 + 35} Q 3860 {y_col + paso_col*5 + 35}, 3860 74" fill="none" stroke="#0284c7" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowBlue)"/>
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
    

    # Sangre -> Citosol -> Mitocondria
    # Palmitato en sangre (unido a Albúmina dentro del torrente vascular superior)
    x_palm_sangre = 510
    partes.append(nodo_libre(x_palm_sangre, 24, "Palmitato (Sanguíneo / Albúmina)", "16C", PALMITATO_LIBRE, "m_palmitato_sangre", text_right=True, dx=140))
    
    # Cruce de la membrana plasmática hacia citosol por transportador CD36 / FAT
    partes.append(f'''
    <path d="M 500 55 L 500 96 L {x_box + 20} {y_box - 1220}" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <g transform="translate(460, 68)">
      <rect x="0" y="0" width="80" height="26" rx="6" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <text x="40" y="17" fill="#ffffff" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CD36/FAT</text>
    </g>
    <text x="550" y="110" fill="#0284c7" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">Captación celular ➔</text>
    ''')
    
    # 1. Palmitato Citosólico
    partes.append(nodo_libre(x_box, y_box - 1200, "Palmitato (Citosólico)", "16C", PALMITATO_LIBRE, "m_palmitato_cito", text_right=True, dx=235))
    partes.append(reaccion_libre(x_box + 60, y_box - 1200 + 80, 50, "Acil-CoA Sintetasa (ACS)", entra="+ ATP + CoA", sale="+ AMP + PPi", id_rx="rx_acs"))
    
    # 2. Palmitoil-CoA Citosólico (Nombre encima de la estructura)
    partes.append(nodo_libre(x_box, y_box - 800, "Palmitoil-CoA (Citosólico)", "16C", PALMITOIL_COA, "m_palmitoil_cito", text_pos="top", dx=110, dy=-22))
    partes.append(reaccion_libre(x_box + 60, y_box - 800 + 80, 50, "CPT-1 (Lanzadera de Carnitina)", entra="+ Carnitina", sale="- CoA", id_rx="rx_cpt1"))
    
    # 3. Palmitoil-Carnitina (Espacio Citosol / EIM exterior)
    partes.append(nodo_libre(x_box, y_box - 280, "Palmitoil-Carnitina", "16C", PALMITOIL_CARNITINA, "m_palm_carnitina", text_right=True, dx=145))
    
    # Cruce del Espacio Intermembrana (EIM) e inserción de CACT directamente incrustado en la Membrana Mitocondrial Interna (MMI)
    x_cact = 240
    y_cact = 2305
    partes.append(f'''
    <!-- Lanzadera de Carnitina: Translocación a través del EIM hacia el transportador CACT en la MMI -->
    <path d="M {x_box+60} {y_box - 280 + 86} L {x_cact} {y_cact - 22}" fill="none" stroke="#0ea5e9" stroke-width="3" stroke-dasharray="8 4" marker-end="url(#arrowBlue)"/>
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
    partes.append(nodo_libre(x_box, y_m_palm, "Palmitoil-CoA (Matriz)", "16C", PALMITOIL_COA, "m_palmitoil", text_right=True, dx=235))
    partes.append(reaccion_libre(x_box + 60, y_m_palm + 70, 42, "Acil-CoA DH", entra="+ FAD", sale="+ FADH2", es_ganancia=True, id_rx="rx_box1"))
    
    # 5. trans-Δ²-Enoil-CoA (Paso añadido)
    y_m_enoil = y_m_palm + 140
    partes.append(nodo_libre(x_box, y_m_enoil, "trans-Δ²-Enoil-CoA", "16C", TRANS_DELTA2_ENOIL_COA, "m_trans_enoil", text_right=True, dx=225))
    partes.append(reaccion_libre(x_box + 60, y_m_enoil + 70, 42, "Enoil-CoA Hidratasa", entra="+ H₂O", id_rx="rx_box1b"))

    # 6. L-β-Hidroxiacil-CoA
    y_m_hidro = y_m_enoil + 140
    partes.append(nodo_libre(x_box, y_m_hidro, "L-β-Hidroxiacil-CoA", "16C", L_BETA_HIDROXIACIL_COA, "m_hidroxi_coa", text_right=True, dx=210))
    partes.append(reaccion_libre(x_box + 60, y_m_hidro + 70, 42, "β-Hidroxiacil-CoA DH", entra="+ NAD+", sale="+ NADH + H+", es_ganancia=True, id_rx="rx_box2"))
    
    # 7. β-Cetoacil-CoA
    y_m_ceto = y_m_hidro + 140
    partes.append(nodo_libre(x_box, y_m_ceto, "β-Cetoacil-CoA", "16C", BETA_CETOACIL_COA, "m_cetoacil_coa", text_right=True, dx=210))
    partes.append(reaccion_libre(x_box + 60, y_m_ceto + 70, 42, "Tiolasa", entra="+ CoA", id_rx="rx_box3"))
    
    # 8. Clivaje tiolítico: Acetil-CoA y Miristoil-CoA
    y_m_split = y_m_ceto + 160
    partes.append(nodo_libre(60, y_m_split, "Acetil-CoA", "2C", ACETIL_COA_BETA, "m_acetil_coa_beta", text_pos="top", dx=50, dy=-16))
    partes.append(nodo_libre(230, y_m_split, "Miristoil-CoA", "14C", MIRISTOIL_COA, "m_miristoil_coa", text_pos="top", dx=95, dy=-16))
    
    partes.append(f"""
    <path d="M {x_box+60} {y_m_ceto + 115} L 110 {y_m_split - 22}" stroke="#ea580c" stroke-width="2.6" fill="none" marker-end="url(#arrowFlow)"/>
    <path d="M {x_box+60} {y_m_ceto + 115} L 270 {y_m_split - 22}" stroke="#ea580c" stroke-width="2.6" fill="none" marker-end="url(#arrowFlow)"/>
    """)
    partes.append(f'</g>')

    # =========================================================================
    # 11. CETOGÉNESIS (MATRIZ MITOCONDRIAL)
    # =========================================================================
    x_ceto = 630
    y_ceto = y_mito + 700
    paso_c = 140
    partes.append(f'<g id="ruta_ceto">')
    
    partes.append(nodo_libre(x_ceto, y_ceto, "Acetoacetil-CoA", "4C", ACETOACETIL_COA, "m_acetoac_coa", text_right=True, dx=160))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + 70, 40, "HMG-CoA Sintasa", entra="+ Acetil-CoA", id_rx="rx_ceto1"))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c, "HMG-CoA", "6C", HMG_COA, "m_hmg_coa", text_right=True, dx=160))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + paso_c + 70, 40, "HMG-CoA Liasa", sale="+ Acetil-CoA", id_rx="rx_ceto2"))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c*2, "Acetoacetato", "4C", ACETOACETATO, "m_acetoacetato", text_right=True, dx=160))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + paso_c*2 + 70, 40, "β-Hidroxibutirato DH", entra="+ NADH", sale="+ NAD+", id_rx="rx_ceto3"))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c*3, "D-β-Hidroxibutirato", "4C", D_BETA_HIDROXIBUTIRATO, "m_betahidroxi", text_right=True, dx=160))
    
    # Línea rosa de exportación que sale hacia abajo y luego dobla a la izquierda en X=35, evitando cruzar cualquier texto
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
    partes.append(nodo_libre(x_aa, y_aa, "L-Alanina", "3C", AMINO_ALANINA, "m_ala_integ", text_right=True, dx=110))

    # Reacción ALT / GPT (Alanina + α-KG ⇄ Piruvato + Glutamato)
    partes.append(f'''
    <g id="rx_alt_integ" data-arrastrable="1" transform="translate({x_aa}, {y_aa + 115})">
      <line x1="-3" y1="0" x2="-3" y2="75" stroke="#0d9488" stroke-width="2" marker-end="url(#arrowTeal)"/>
      <line x1="3" y1="75" x2="3" y2="0" stroke="#0d9488" stroke-width="2" marker-end="url(#arrowTeal)"/>
      <!-- Arco de recolección de nitrógeno acoplado con α-KG ➔ Glutamato -->
      <path d="M 65 10 Q 15 38 65 65" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrowBlueAmino)"/>
      <text x="70" y="8" fill="#64748b" font-size="9.5" font-family="'Inter', sans-serif">α-Cetoglutarato</text>
      <text x="70" y="72" fill="#1d4ed8" font-size="10" font-weight="800" font-family="'Inter', sans-serif">Glutamato</text>

      <g transform="translate(-15, 38)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">ALT / GPT</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 2.6.1.2 (PLP)</text>
      </g>
    </g>
    ''')

    # 3. Piruvato resultante de ALT en citosol
    partes.append(nodo_libre(x_aa, y_aa + 230, "Piruvato (de Alanina)", "3C", PIRUVATO, "m_pyr_ala_integ", text_right=True, dx=110))

    # Conexión directa hacia la Glucólisis (desciende por canal citosólico despejado en X=2135)
    partes.append(f'''
    <text x="{x_aa}" y="{y_aa + 305}" fill="#c2410c" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Pool de Piruvato (➔ MPC) ↓</text>
    <path d="M {x_aa} {y_aa + 320} C 2135 {y_aa + 345}, 2135 800, 2135 1550 C 2135 1630, 2060 1675, 1880 1675" fill="none" stroke="#ea580c" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowFlow)"/>
    ''')

    # 4. L-Glutamato (colector común de nitrógeno en citosol - centrado en X=2280 con texto superior)
    partes.append(nodo_libre(2280, y_aa + 380, "L-Glutamato", "5C", AMINO_GLUTAMATO, "m_glu_integ", text_pos="top", dy=-18))

    # 5. Rama Citosólica de Glutamina Sintetasa (Destoxificación a Glutamina)
    partes.append(nodo_libre(2280, y_aa + 630, "L-Glutamina", "5C", AMINO_GLUTAMINA, "m_gln_integ", text_pos="top", dy=-18))
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

    # Exportación de Glutamina al torrente sanguíneo superior (vía canal despejado en X=2390 hacia Y=74)
    partes.append(f'''
    <path d="M 2340 {y_aa + 640} Q 2390 {y_aa + 640} 2390 850 L 2390 74" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
    <text x="2405" y="520" fill="#0f766e" font-size="11" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 2405 520)">EXPORTACIÓN DE GLUTAMINA A SANGRE ➔</text>
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
    <path d="M 2240 {y_aa + 400} C 2200 {y_aa + 440}, 2200 950, 2200 1200 C 2200 1500, {x_agc} 1750, {x_agc} {y_agc - 18}" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
    <!-- Tránsito desde AGC hacia L-Glutamato dentro de la matriz -->
    <path d="M {x_agc} {y_agc + 22} L {x_agc} {y_gldh_start - 10}" fill="none" stroke="#0d9488" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowTeal)"/>
    ''')

    # 7. MATRIZ MITOCONDRIAL: Glutamato en la Matriz (elevado para no interferir con Krebs->CTE)
    partes.append(nodo_libre(x_agc - 40, y_gldh_start, "L-Glutamato (Matriz)", "5C", AMINO_GLUTAMATO, "m_glu_mito_integ", text_right=True, dx=145))

    # Reacción GLDH (Glutamato Deshidrogenasa)
    partes.append(f'''
    <g id="rx_gldh_integ" data-arrastrable="1" transform="translate({x_agc}, {y_gldh_start + 105})">
      <line x1="-3" y1="0" x2="-3" y2="70" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
      <line x1="3" y1="70" x2="3" y2="0" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
      
      <!-- Entrada NAD(P)+ / Salida NAD(P)H -->
      <path d="M -75 14 Q -25 14 -4 24" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-80" y="17" fill="#059669" font-size="10" font-weight="800" text-anchor="end">+ NAD(P)⁺ + H₂O</text>
      
      <path d="M -4 46 Q -25 56 -75 56" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-80" y="60" fill="#059669" font-size="10" font-weight="800" text-anchor="end">+ NAD(P)H + H⁺</text>

      <!-- Salida de Amonio libre hacia la derecha -->
      <path d="M 4 35 Q 50 35 90 60" fill="none" stroke="#2563eb" stroke-width="2.4" marker-end="url(#arrowBlueAmino)"/>
      <text x="95" y="70" fill="#1d4ed8" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">➔ + NH₄⁺</text>

      <!-- Textos y Alosterismo a la derecha bien despejados -->
      <g transform="translate(20, 10)">
        <text x="0" y="0" fill="#0f172a" font-size="12.5" font-weight="900" font-family="'Inter', sans-serif">Glutamato Deshidrogenasa (GLDH)</text>
        <text x="0" y="14" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">EC 1.4.1.3 (Mitocondrial)</text>
        <text x="0" y="27" fill="#16a34a" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">(+) Activada por ADP, GDP</text>
        <text x="0" y="39" fill="#e11d48" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">(-) Inhibida por ATP, GTP</text>
      </g>
    </g>
    ''')

    # 8. Productos de GLDH:
    # A. α-Cetoglutarato regenerado en matriz mitocondrial (hacia la izquierda, Y=2360)
    partes.append(nodo_libre(x_agc - 210, y_gldh_start + 150, "α-Cetoglutarato", "5C", AMINO_AKG, "m_akg_gldh_integ", text_right=False, dx=-25))
    # Ramificación de la flecha de GLDH hacia la estructura de α-Cetoglutarato
    partes.append(f'''
    <path d="M {x_agc - 5} {y_gldh_start + 175} Q {x_agc - 40} {y_gldh_start + 195} {x_agc - 100} {y_gldh_start + 195}" fill="none" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
    ''')
    # Conexión directa hacia el Ciclo de Krebs (bordeando limpiamente por arriba de NADH & FADH2 para no solapar el badge)
    partes.append(f'''
    <path d="M {x_agc - 210} {y_gldh_start + 205} C 1720 2520, 1500 2550, 1420 2620 C 1370 2660, 1330 2710, {x_k + 160} {y_k + paso_k * 3 - 10}" fill="none" stroke="#b45309" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowFlow)"/>
    <text x="1600" y="2520" fill="#78350f" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">➔ Reingreso directo al Ciclo de Krebs (α-KG)</text>
    ''')

    # B. Ion Amonio (NH4+) libre en matriz (hacia la derecha, Y=2360)
    partes.append(nodo_libre(x_agc + 120, y_gldh_start + 150, "Ion Amonio (NH₄⁺)", "Nitrógeno", AMINO_NH4, "m_nh4_integ", text_right=True, dx=85))
    # Conexión directa hacia el Ciclo de la Urea (CPS-1) bordeando por debajo del marco de la CTE
    partes.append(f'''
    <!-- Canal conductor de Amonio hacia la Carbamoil Fosfato Sintetasa I (CPS-1) -->
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
    # 13. CICLO DE LA UREA Y BICICLO DE KREBS (CUADRANTE DERECHO - ENTORNO REAL)
    # =========================================================================
    x_u_l = 4100  # Carril Izquierdo (Carbamoil-P, CPS-1, Aspartato, Fumarato, Biciclo)
    x_u_c = 4420  # Carril Central (Flujo principal: Citrulina, Arg-Succ, Arginina, Urea)
    x_u_r = 4700  # Carril Derecho (Lanzadera de Ornitina, ORNT1)

    partes.append(f'''
    <!-- ================================================================= -->
    <!-- RUTA 13: CICLO DE LA UREA (DESINTOXICACIÓN HEPÁTICA DE NITRÓGENO)   -->
    <!-- ================================================================= -->
    <g id="ruta_ciclo_urea">
      <!-- Rótulo de la Ruta flotando libremente en citosol superior (despejado a la izquierda de la excreción) -->
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

      <!-- Metadatos de OTC (en 2 líneas compactas para no invadir carril de Ornitina) -->
      <g transform="translate(18, 12)">
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
      <path d="M 0 -25 L 0 -130" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)" fill="none"/>

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
        x_u_c - 40, 1960,
        "L-Citrulina (Citosol)", "6C",
        UREA_CITRULINA, "m_u_citrulina_cito",
        text_right=True, dx=140,
        detalle="Recibida por SLC25A13 para condensación"
    ))

    # 6. Donador lateral de nitrógeno: L-Aspartato (en carril izquierdo)
    partes.append(nodo_libre(
        x_u_l - 20, 1810,
        "L-Aspartato", "4C",
        UREA_ASPARTATO, "m_u_aspartato",
        text_right=False, dx=-15,
        detalle="Aporta el 2º nitrógeno de la urea"
    ))

    # Reacción 3: ASS (Argininosuccinato Sintetasa)
    partes.append(f'''
    <g id="rx_u_ass" data-arrastrable="1" transform="translate({x_u_c}, 1760)">
      <!-- Flecha ascendente desde Citrulina -->
      <line x1="0" y1="130" x2="0" y2="-10" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Entrada diagonal de L-Aspartato desde carril izquierdo -->
      <path d="M -220 50 Q -90 50 -4 25" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de 1 ATP (lado derecho) -->
      <path d="M 65 65 Q 25 65 4 45" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="70" y="68" fill="#dc2626" font-size="11" font-weight="800" font-family="'Inter', sans-serif">- 1 ATP</text>

      <!-- Salida de AMP + PPi (lado derecho) -->
      <path d="M 4 15 Q 25 5 65 5" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="70" y="9" fill="#475569" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">+ AMP + PPi (➔ 2 Pi)</text>

      <!-- Metadatos de ASS (formato compacto de 2 líneas) -->
      <g transform="translate(18, -12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif">Argininosuccinato</text>
        <text x="0" y="13" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif">Sintetasa (ASS)</text>
        <text x="0" y="26" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">EC 6.3.4.5 (Citosólica)</text>
        <text x="0" y="38" fill="#15803d" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Intermedio Citrulil-AMP activado</text>
      </g>
    </g>
    ''')

    # 7. L-Argininosuccinato (10C) - Intermediario que une ambos nitrógenos
    partes.append(nodo_libre(
        x_u_c - 50, 1480,
        "L-Argininosuccinato", "10C",
        UREA_ARGININOSUCCINATO, "m_u_argininosuccinato",
        text_right=True, dx=165,
        detalle="Condensado Citrulina-Aspartato"
    ))

    # Reacción 4: ASL (Argininosuccinato Liasa)
    partes.append(f'''
    <g id="rx_u_asl" data-arrastrable="1" transform="translate({x_u_c}, 1340)">
      <!-- Flecha vertical ascendente hacia Arginina -->
      <line x1="0" y1="100" x2="0" y2="-10" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Salida lateral hacia la IZQUIERDA de FUMARATO -->
      <path d="M -4 45 Q -80 45 -180 45" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      <text x="-190" y="40" fill="#c2410c" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">⮜ + Fumarato (4C)</text>

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
        x_u_l - 20, 1340,
        "Fumarato", "4C",
        UREA_FUMARATO, "m_u_fumarato",
        text_right=False, dx=-15,
        detalle="Subproducto de escisión trans"
    ))

    # Biciclo de Krebs (Krebs Bicycle Shunt): Reconexión Fumarato ➔ Aspartato
    partes.append(f'''
    <g id="biciclo_krebs_shunt" data-arrastrable="1">
      <path d="M {x_u_l - 20} 1410 C {x_u_l - 120} 1450, {x_u_l - 120} 1750, {x_u_l - 20} 1790" fill="none" stroke="#ea580c" stroke-width="2.6" stroke-dasharray="7 4" marker-end="url(#arrowFlow)"/>
      <g transform="translate({x_u_l - 120}, 1560)">
        <text x="0" y="0" fill="#c2410c" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">BICICLO DE KREBS ↻</text>
        <text x="0" y="14" fill="#475569" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">+ H₂O (Fumarasa) ➔ L-Malato</text>
        <text x="0" y="27" fill="#475569" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">+ NAD⁺ (MDH1) ➔ OAA</text>
        <text x="0" y="40" fill="#475569" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">+ Glu (GOT1) ➔ Asp</text>
      </g>
    </g>
    ''')

    # 9. L-Arginina (6C) (carril central, X=4420, Y=1160)
    partes.append(nodo_libre(
        x_u_c - 40, 1160,
        "L-Arginina", "6C",
        UREA_ARGININA, "m_u_arginina",
        text_right=True, dx=145,
        detalle="Grupo guanidino cargado"
    ))

    # Reacción 5: Arginasa 1 (ARG1) - Bifurcación hacia Urea y Ornitina
    partes.append(f'''
    <g id="rx_u_arg1" data-arrastrable="1" transform="translate({x_u_c}, 980)">
      <!-- Entrada de Agua para la hidrólisis -->
      <path d="M -75 35 Q -25 35 -4 50" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="-80" y="38" fill="#0284c7" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">+ H₂O</text>

      <!-- Flecha vertical hacia UREA -->
      <line x1="0" y1="120" x2="0" y2="-90" stroke="#dc2626" stroke-width="2.8" marker-end="url(#arrowRed)"/>

      <!-- Flecha curva hacia la derecha hacia Ornitina citosólica (X=4700) -->
      <path d="M 0 50 Q 80 50 200 15" fill="none" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowTeal)"/>
      <text x="120" y="34" fill="#0f766e" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">➔ Retorno Ornitina</text>

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
        x_u_r - 20, 960,
        "L-Ornitina (Citosol)", "5C",
        UREA_ORNITINA, "m_u_ornitina_cito",
        text_right=True, dx=115,
        detalle="Regenerada tras hidrólisis"
    ))

    # Canal de retorno de Ornitina hacia ORNT1 (descenso por carril X=4700 con badge central)
    partes.append(f'''
    <g id="canal_retorno_ornitina" data-arrastrable="1">
      <!-- Descenso desde Ornitina citosol (Y=1060) hasta ORNT1 (Y=2140) -->
      <path d="M {x_u_r} 1060 L {x_u_r} 2140" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-dasharray="8 5" marker-end="url(#arrowBlueAmino)"/>
      <!-- Continuación desde ORNT1 (Y=2180) hasta Ornitina matriz (Y=2850) -->
      <path d="M {x_u_r} 2180 L {x_u_r} 2850" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-dasharray="8 5" marker-end="url(#arrowBlueAmino)"/>
      
      <!-- Insignia informativa en el carril -->
      <g transform="translate({x_u_r}, 1600)">
        <rect x="-85" y="-12" width="170" height="24" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.2"/>
        <text x="0" y="4" fill="#1d4ed8" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">↓ ORNT1 (SLC25A15)</text>
      </g>
    </g>
    ''')

    # 11. UREA (Carbamida) - Producto final de desecho (X=4420, Y=780)
    partes.append(nodo_libre(
        x_u_c - 30, 780,
        "UREA (Carbamida)", "1C",
        UREA_MOL, "m_u_urea",
        text_right=True, dx=110,
        detalle="Diamida neutra no tóxica (2 nitrógenos)"
    ))

    # 12. Excreción directa de Urea al torrente sanguíneo superior (Y=750 ➔ Y=74)
    partes.append(f'''
    <g id="excrecion_urea_sangre" data-arrastrable="1">
      <path d="M {x_u_c} 750 L {x_u_c} 74" fill="none" stroke="#dc2626" stroke-width="3.2" stroke-dasharray="8 4" marker-end="url(#arrowRed)"/>
      <text x="{x_u_c + 18}" y="520" fill="#b91c1c" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 {x_u_c + 18} 520)">➔ EXCRECIÓN DE UREA AL TORRENTE SANGUÍNEO HEPÁTICO (➔ RIÑÓN)</text>

      <!-- Biomarcador vascular en el capilar superior -->
      <ellipse cx="{x_u_c}" cy="38" rx="26" ry="16" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
      <text x="{x_u_c}" y="42" fill="#dc2626" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">UREA</text>
      <text x="{x_u_c}" y="60" fill="#fca5a5" font-size="7.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Excreción</text>
    </g>
    ''')

    partes.append(f'</g>')

    # 14. BLOQUE INSTITUCIONAL Y AUTORÍA DE CÓDIGO ABIERTO
    partes.append(generar_bloque_autoria(3820, 3540))

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
      <h2 style="color: #38bdf8; font-size: 1.1rem;">🌿 Entorno Biológico Real: Citosol y Gran Mitocondria</h2>
      <p style="color: #94a3b8; font-size: 0.78rem;">Glucólisis • Glucógeno • Pentosas • Lanzadera • Krebs • Cadena Respiratoria • β-Oxidación • Cetogénesis</p>
    </div>
    <div class="controls">
      <button onclick="zoomOut()">−</button>
      <span id="zoomLevel">100%</span>
      <button onclick="zoomIn()">+</button>
      <button onclick="resetView()">Reset</button>
      <button style="background: #16a34a;" onclick="fitView()">Ajustar</button>
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
    
    let scale = 1;
    let pointX = 0;
    let pointY = 0;
    let startX = 0;
    let startY = 0;
    let isPanning = false;

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
      isPanning = true;
      startX = e.clientX - pointX;
      startY = e.clientY - pointY;
      viewport.classList.add('grabbing');
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isPanning) return;
      pointX = e.clientX - startX;
      pointY = e.clientY - startY;
      updateTransform();
    }});

    window.addEventListener('mouseup', () => {{
      isPanning = false;
      viewport.classList.remove('grabbing');
    }});

    // Ajustar vista al inicio
    window.addEventListener('load', fitView);
  </script>
</body>
</html>
"""
    return html_out, svg_completo

if __name__ == "__main__":
    html_str, svg_str = construir_mapa_organico()
    
    ruta_html = os.path.join(DIR_BASE, "prueba_visual_integrada.html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html_str)

    ruta_svg = os.path.join(DIR_BASE, "prueba_visual_integrada.svg")
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_str)

    print(f"✅ Mapa Orgánico Celular generado en HTML: {ruta_html}")
    print(f"✅ Mapa Orgánico Celular generado en SVG: {ruta_svg}")
