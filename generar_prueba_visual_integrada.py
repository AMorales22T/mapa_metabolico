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

ANCHO_CANVAS = 4000
ALTO_CANVAS = 4200

def nodo_libre(x, y, nombre, carbonos, svg_mol, id_nodo="", text_right=True, dx=135, dy=24, text_pos="side"):
    """Metabolito 100% libre sin tarjetas ni globos."""
    if text_pos == "top":
        align = 'text-anchor="middle"'
        tx = dx if dx != 135 else 70
        ty = dy if dy != 24 else -22
        return f"""
        <!-- Metabolito Libre: {nombre} -->
        <g id="{id_nodo}" data-arrastrable="1" transform="translate({x}, {y})">
          <g>{svg_mol}</g>
          <text x="{tx}" y="{ty}" fill="#0f172a" font-size="14.5" font-weight="800" font-family="'Inter', sans-serif" {align}>{nombre}</text>
          <text x="{tx}" y="{ty + 16}" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace" {align}>[{carbonos}]</text>
        </g>
        """
    if text_right:
        tx = dx
    else:
        tx = dx if dx != 135 else -20
    align = "" if text_right else 'text-anchor="end"'
    return f"""
    <!-- Metabolito Libre: {nombre} -->
    <g id="{id_nodo}" data-arrastrable="1" transform="translate({x}, {y})">
      <g>{svg_mol}</g>
      <text x="{tx}" y="{dy}" fill="#0f172a" font-size="15" font-weight="800" font-family="'Inter', sans-serif" {align}>{nombre}</text>
      <text x="{tx}" y="{dy + 17}" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace" {align}>[{carbonos}]</text>
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
    </g>

    <!-- Albúmina sérica y Lipoproteínas en el plasma -->
    <g opacity="0.6">
      <ellipse cx="480" cy="24" rx="16" ry="11" fill="#fef08a" stroke="#ca8a04" stroke-width="1.2"/>
      <text x="480" y="27" fill="#854d0e" font-size="7.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">ALBÚMINA</text>
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
               C 3750 {y_mito + 30}, 3920 {y_mito + 220}, 3880 {y_mito + 700}
               C 3820 {y_mito + 1750}, 2850 {y_mito + 1950}, 1900 {y_mito + 1930}
               C 1100 {y_mito + 1950}, 300 {y_mito + 1850}, 140 {y_mito + 1300}
               C 60 {y_mito + 800}, 50 {y_mito + 400}, 100 {y_mito + 180} Z"
            fill="url(#gradMitocondria)" stroke="#92400e" stroke-width="6"/>

      <!-- Espacio Intermembrana (EIM) -->
      <path d="M 150 {y_mito + 195} 
               C 300 {y_mito}, 870 {y_mito - 55}, 1520 {y_mito - 10}
               C 1940 {y_mito - 75}, 2640 {y_mito - 45}, 3320 {y_mito}
               C 3680 {y_mito + 55}, 3850 {y_mito + 235}, 3815 {y_mito + 690}
               C 3760 {y_mito + 1710}, 2830 {y_mito + 1900}, 1900 {y_mito + 1885}
               C 1120 {y_mito + 1900}, 350 {y_mito + 1805}, 190 {y_mito + 1275}
               C 110 {y_mito + 790}, 100 {y_mito + 405}, 150 {y_mito + 195} Z"
            fill="#fffbeb" fill-opacity="0.6" stroke="#b45309" stroke-width="3" stroke-dasharray="12 7"/>

      <!-- Matriz Mitocondrial (MMI Contorno interno) -->
      <path d="M 210 {y_mito + 220} 
               C 360 {y_mito + 45}, 900 {y_mito}, 1520 {y_mito + 35}
               C 1920 {y_mito - 25}, 2620 {y_mito}, 3280 {y_mito + 45}
               C 3610 {y_mito + 95}, 3770 {y_mito + 260}, 3740 {y_mito + 670}
               C 3690 {y_mito + 1660}, 2800 {y_mito + 1845}, 1900 {y_mito + 1830}
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
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 8, "Fosfoenolpiruvato", "3C", FOSFOENOLPIRUVATO, "m_pep"))
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

    # Ramas: Xilulosa-5P y Ribosa-5P (texto de Xilulosa estrictamente a la izquierda de la estructura)
    partes.append(nodo_libre(x_p - 110, y_p + 500, "Xilulosa-5-P", "5C", XILULOSA_5_FOSFATO, "m_xu5p", text_right=False, dx=-30))
    partes.append(nodo_libre(x_p + 280, y_p + 500, "Ribosa-5-P", "5C", RIBOSA_5_FOSFATO, "m_r5p"))
    partes.append(f"""
    <path d="M {x_p + 20} {y_p + 430} L {x_p - 50} {y_p + 495}" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="{x_p - 50}" y="{y_p + 460}" fill="#047857" font-size="10.5" font-family="'Inter', sans-serif" text-anchor="end">Fosfopentosa Epimerasa</text>

    <path d="M {x_p + 80} {y_p + 430} L {x_p + 270} {y_p + 495}" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="{x_p + 200}" y="{y_p + 460}" fill="#047857" font-size="10.5" font-family="'Inter', sans-serif">Fosfopentosa Isomerasa</text>
    """)

    # Sedoheptulosa-7P y Eritrosa-4P
    partes.append(nodo_libre(x_p - 110, y_p + 660, "Sedoheptulosa-7-P", "7C", SEDOHEPTULOSA_7_FOSFATO, "m_s7p", text_right=False, dx=-30))
    partes.append(nodo_libre(x_p + 280, y_p + 660, "Eritrosa-4-P", "4C", ERITROSA_4_FOSFATO, "m_e4p"))
    partes.append(f"""
    <text x="{x_p + 90}" y="{y_p + 600}" fill="#047857" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Transcetolasa 1 (TK1) ⇄</text>
    <text x="{x_p + 90}" y="{y_p + 760}" fill="#047857" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Transaldolasa ⇄ Retorno a F6P y GAP</text>

    <!-- Retornos de Transaldolasa: Canal citosólico fluido (Y=1200-1350) que rodea el bloque de aminoácidos -->
    <path d="M {x_p - 110} {y_p + 775} C {x_p - 350} {y_p + 775}, 2100 1200, {x_g + 200} {y_g + paso_y * 2 + 35}" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <text x="2100" y="1190" fill="#059669" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Retorno a Glucólisis: Fructosa-6-P</text>

    <path d="M {x_p - 110} {y_p + 815} C {x_p - 350} {y_p + 815}, 2100 1320, {x_g + 280} {y_g + paso_y * 4 + 35}" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <text x="2100" y="1310" fill="#059669" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Retorno a Glucólisis: GAP</text>
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
        <g transform="translate({cx_lupa - 225}, {cy_lupa - 220})">
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
        <g transform="translate({cx_lupa - 150}, {cy_lupa - 85})">
          <path d="M 60 15 C 30 -5, -15 -10, -35 -40" fill="none" stroke="#db2777" stroke-width="2.6" marker-end="url(#arrowRed)"/>
          <text x="10" y="-3" fill="#be123c" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">GOT1 (cAST)</text>
          <text x="10" y="10" fill="#64748b" font-size="8.5" font-family="'Inter', sans-serif" text-anchor="middle">+ α-KG ➔ + Glu</text>
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
          <text x="-65" y="44" fill="#059669" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">+ NADH + H⁺</text>
          <text x="-65" y="58" fill="#047857" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">➔ alimenta Complejo I (2.5 ATP)</text>
        </g>

        <!-- Estructura Matricial 2: Oxalacetato en la Matriz -->
        <g transform="translate({cx_lupa - 225}, {cy_lupa + 75})">
          {LANZ_OAA}
          <text x="40" y="145" fill="#0f172a" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Oxalacetato (Matriz)</text>
        </g>

        <!-- Transaminación Matricial GOT2 (Oxalacetato ➔ Aspartato) -->
        <g transform="translate({cx_lupa - 150}, {cy_lupa + 50})">
          <path d="M -35 25 C -15 0, 30 -5, 60 15" fill="none" stroke="#db2777" stroke-width="2.6" marker-end="url(#arrowRed)"/>
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
    
    partes.append(nodo_libre(x_lipo, y_lipo - paso_l, "Acetil-CoA (Citosólico)", "2C", ACETIL_COA, "m_acetil_coa_cito", text_right=True, dx=180))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo - paso_l + 75, 48, "ACC (Acetil-CoA Carboxilasa)", entra="+ ATP + CO2", sale="+ ADP", id_rx="rx_acc"))
    
    partes.append(f'''
    <path d="M 1250 2380 Q 2200 2200, {x_lipo - 30} 690" fill="none" stroke="#0ea5e9" stroke-width="2.5" stroke-dasharray="10 5" marker-end="url(#arrowBlue)"/>
    <text x="2200" y="2180" fill="#0284c7" font-size="12" font-weight="900" font-family="'Inter', sans-serif">Transportador de Tricarboxilatos (CIC) ➔</text>
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
    <path d="M {x_lipo + 190} {y_lipo - paso_l + 30} Q {x_col - 80} {y_lipo - paso_l + 30}, {x_col} {y_col}" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <text x="{x_lipo + 210}" y="{y_lipo - paso_l + 18}" fill="#9a3412" font-size="12" font-weight="900" font-family="'Inter', sans-serif">➔ Vía del Mevalonato</text>
    ''')

    # Mevalonato (producto irreversible del marcapasos HMGCR)
    partes.append(nodo_libre(x_col, y_col, "Mevalonato", "6C", MEVALONATO, "m_mevalonato_integ", text_right=True, dx=205))
    partes.append(reaccion_libre(x_col + 60, y_col + 75, 45, "Mevalonato Quinasa / Descarboxilasa", entra="- 3 ATP", sale="+ CO2 + Pi", id_rx="rx_col1"))
    
    # Isopentenil Pirofosfato (IPP)
    partes.append(nodo_libre(x_col, y_col + paso_col, "Isopentenil-PP (IPP)", "5C", ISOPENTENIL_PP, "m_ipp_integ", text_right=True, dx=205))
    partes.append(reaccion_libre(x_col + 60, y_col + paso_col + 75, 45, "Preniltransferasas", entra="+ 2 IPP", sale="+ 2 PPi", id_rx="rx_col2"))
    
    # Farnesil Pirofosfato (FPP)
    partes.append(nodo_libre(x_col, y_col + paso_col*2, "Farnesil-PP (FPP)", "15C", FARNESIL_PP, "m_fpp_integ", text_right=True, dx=200))
    partes.append(reaccion_libre(x_col + 60, y_col + paso_col*2 + 75, 45, "Escualeno Sintasa", entra="- NADPH", sale="+ 2 PPi", es_ganancia=False, id_rx="rx_col3"))
    
    # Escualeno
    partes.append(nodo_libre(x_col, y_col + paso_col*3, "Escualeno", "30C", ESCUALENO, "m_escualeno_integ", text_right=True, dx=210))
    partes.append(reaccion_libre(x_col + 60, y_col + paso_col*3 + 75, 45, "Oxidoscualeno Ciclasa", entra="- NADPH + O2", sale="+ H2O", id_rx="rx_col4"))
    
    # Lanosterol
    partes.append(nodo_libre(x_col, y_col + paso_col*4, "Lanosterol", "30C", LANOSTEROL, "m_lanosterol_integ", text_right=True, dx=200))
    partes.append(reaccion_libre(x_col + 60, y_col + paso_col*4 + 75, 45, "Vías de Bloch &amp; Kandutsch (19 pasos)", entra="- NADPH + O2", sale="+ 3 CO2", id_rx="rx_col5"))
    
    # Colesterol Final
    partes.append(nodo_libre(x_col, y_col + paso_col*5, "COLESTEROL", "27C", COLESTEROL, "m_colesterol_integ", text_right=True, dx=285))
    
    # Conexiones funcionales de destino del Colesterol
    partes.append(f'''
    <path d="M {x_col + 280} {y_col + paso_col*5 + 35} Q 3920 {y_col + paso_col*5 + 35}, 3920 200" fill="none" stroke="#0284c7" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowBlue)"/>
    <text x="3905" y="500" fill="#0369a1" font-size="12" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 3905 500)">➔ Destino a Membrana Plasmática (Balsas Lipídicas)</text>
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
    x_palm_sangre = 480
    partes.append(nodo_libre(x_palm_sangre, 24, "Palmitato (Sanguíneo / Albúmina)", "16C", PALMITATO_LIBRE, "m_palmitato_sangre", text_right=True, dx=140))
    
    # Cruce de la membrana plasmática hacia citosol por transportador CD36 / FAT
    partes.append(f'''
    <path d="M {x_palm_sangre - 40} 60 L {x_palm_sangre - 40} 78 L {x_box + 20} {y_box - 1220}" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <g transform="translate({x_palm_sangre - 80}, 68)">
      <rect x="0" y="0" width="80" height="26" rx="6" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <text x="40" y="17" fill="#ffffff" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CD36/FAT</text>
    </g>
    <text x="{x_palm_sangre + 10}" y="85" fill="#0284c7" font-size="10" font-weight="800" font-family="'Inter', sans-serif">Captación celular ➔</text>
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
    x_aa = 2160
    y_aa = 380
    partes.append(f'<g id="ruta_transaminacion_desaminacion">')

    # Rótulo de la vía en el citosol
    partes.append(f'''
    <g id="banner_aminoacidos" data-arrastrable="1" transform="translate({x_aa + 110}, {y_aa - 70})">
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
    partes.append(nodo_libre(x_aa - 80, y_aa, "L-Alanina", "3C", AMINO_ALANINA, "m_ala_integ", text_right=True, dx=140))

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
    partes.append(nodo_libre(x_aa - 80, y_aa + 230, "Piruvato (de Alanina)", "3C", PIRUVATO, "m_pyr_ala_integ", text_right=True, dx=140))

    # Conexión directa hacia la Glucólisis (hacia x_g = 1680)
    partes.append(f'''
    <path d="M {x_aa - 80} {y_aa + 270} C {x_aa - 200} {y_aa + 270}, 1950 1700, 1900 1735" fill="none" stroke="#ea580c" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowFlow)"/>
    <text x="{x_aa - 180}" y="{y_aa + 320}" fill="#c2410c" font-size="11" font-weight="800" font-family="'Inter', sans-serif">➔ Conexión con Piruvato Citosólico</text>
    ''')

    # 4. L-Glutamato (colector común de nitrógeno en citosol)
    partes.append(nodo_libre(x_aa + 180, y_aa + 380, "L-Glutamato", "5C", AMINO_GLUTAMATO, "m_glu_integ", text_right=True, dx=140))

    # 5. Rama Citosólica de Glutamina Sintetasa (Destoxificación a Glutamina)
    partes.append(nodo_libre(x_aa + 180, y_aa + 620, "L-Glutamina", "5C", AMINO_GLUTAMINA, "m_gln_integ", text_right=True, dx=140))
    partes.append(f'''
    <g id="rx_glns_integ" data-arrastrable="1" transform="translate({x_aa + 220}, {y_aa + 510})">
      <line x1="0" y1="0" x2="0" y2="70" stroke="#0d9488" stroke-width="2.4" marker-end="url(#arrowTeal)"/>
      <path d="M -50 15 Q -15 15 -3 30" fill="none" stroke="#2563eb" stroke-width="1.8" marker-end="url(#arrowBlueAmino)"/>
      <text x="-55" y="18" fill="#1d4ed8" font-size="9.5" font-weight="800" text-anchor="end">+ NH₄⁺</text>
      <path d="M -50 35 Q -20 35 -3 45" fill="none" stroke="#dc2626" stroke-width="1.6" marker-end="url(#arrowRed)"/>
      <text x="-55" y="38" fill="#dc2626" font-size="9.5" font-weight="800" text-anchor="end">- 1 ATP</text>
      <g transform="translate(15, 38)">
        <text x="0" y="0" fill="#0f172a" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">Glutamina Sintetasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 6.3.1.2</text>
      </g>
    </g>
    ''')

    # Exportación de Glutamina al torrente sanguíneo superior
    partes.append(f'''
    <path d="M {x_aa + 335} {y_aa + 710} Q {x_aa + 420} {y_aa + 710} {x_aa + 420} 500 L {x_aa + 420} 70" fill="none" stroke="#0d9488" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
    <text x="{x_aa + 435}" y="300" fill="#0f766e" font-size="11" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(90 {x_aa + 435} 300)">EXPORTACIÓN DE GLUTAMINA A SANGRE ➔</text>
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
    <path d="M {x_aa + 180} {y_aa + 440} C {x_aa + 120} {y_aa + 600}, {x_agc} {y_mito - 120}, {x_agc} {y_agc - 18}" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
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
    # Conexión directa hacia el Ciclo de Krebs (nodo de alfa-cetoglutarato en x_k=1140, y_k + paso_k*3 = 2765)
    partes.append(f'''
    <path d="M {x_agc - 230} {y_gldh_start + 230} C {x_agc - 400} {y_gldh_start + 230}, 1450 {y_k + paso_k * 3 - 30}, {x_k + 160} {y_k + paso_k * 3 + 10}" fill="none" stroke="#b45309" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowFlow)"/>
    <text x="{x_agc - 340}" y="{y_gldh_start + 250}" fill="#78350f" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">➔ Reingreso directo al Ciclo de Krebs (α-KG)</text>
    ''')

    # B. Ion Amonio (NH4+) libre en matriz (hacia la derecha, Y=2360)
    partes.append(nodo_libre(x_agc + 120, y_gldh_start + 150, "Ion Amonio (NH₄⁺)", "Nitrógeno", AMINO_NH4, "m_nh4_integ", text_right=True, dx=85))
    # Conexión hacia el Ciclo de la Urea (CPS-1)
    partes.append(f'''
    <path d="M {x_agc + 190} {y_gldh_start + 185} Q {x_agc + 260} {y_gldh_start + 200} {x_agc + 270} {y_gldh_start + 260}" fill="none" stroke="#2563eb" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowBlueAmino)"/>
    <text x="{x_agc + 280}" y="{y_gldh_start + 255}" fill="#1d4ed8" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">➔ ENTRADA AL CICLO DE LA UREA</text>
    <text x="{x_agc + 280}" y="{y_gldh_start + 272}" fill="#64748b" font-size="10" font-family="'Inter', sans-serif">Carbamoil Fosfato Sintetasa I (CPS-1)</text>
    ''')

    partes.append(f'</g>')

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
      <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
        <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
      </marker>
      <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
        <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
      </marker>
      <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
        <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
      </marker>

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
