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

# Estructuras químicas
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

ANCHO_CANVAS = 3800
ALTO_CANVAS = 3500

def nodo_libre(x, y, nombre, carbonos, svg_mol, id_nodo="", text_right=True, dx=135):
    """Metabolito 100% libre sin tarjetas ni globos."""
    tx = dx if text_right else -20
    align = "" if text_right else 'text-anchor="end"'
    return f"""
    <!-- Metabolito Libre: {nombre} -->
    <g id="{id_nodo}" data-arrastrable="1" transform="translate({x}, {y})">
      <g>{svg_mol}</g>
      <text x="{tx}" y="24" fill="#0f172a" font-size="15" font-weight="800" font-family="'Inter', sans-serif" {align}>{nombre}</text>
      <text x="{tx}" y="41" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace" {align}>[{carbonos}]</text>
    </g>
    """

def reaccion_libre(x, y, h, enzima, entra="", sale="", es_ganancia=False, reversible=False, id_rx=""):
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

    return f"""
    <!-- Reacción: {enzima} -->
    <g id="{id_rx}" data-arrastrable="1" transform="translate({x}, {y})">
      {lineas}
      {curvas}
      <text x="14" y="{h//2 + 4}" fill="#0f172a" font-size="12" font-weight="700" font-family="'Inter', sans-serif">{enzima}</text>
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
      <text x="0" y="0" fill="#166534" font-size="20" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="3">CITOSOL</text>
      <path d="M 0 10 Q 100 20 200 10" fill="none" stroke="#4ade80" stroke-width="2"/>
    </g>

    <!-- Microfilamentos del citoesqueleto atravesando el citoplasma -->
    <g fill="none" stroke="#86efac" opacity="0.25">
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
    <!-- MEMBRANA PLASMÁTICA CONTINUA Y CANAL GLUT-4 (ARRIBA)              -->
    <!-- ================================================================= -->
    <!-- Espacio Extracelular -->
    <path d="M 0 0 L {ANCHO_CANVAS} 0 L {ANCHO_CANVAS} 65 Q {ANCHO_CANVAS*0.5} 90 0 65 Z" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.2"/>
    <text x="50" y="36" font-family="'Inter', sans-serif" font-size="14" font-weight="800" fill="#64748b" letter-spacing="2">
      ESPACIO EXTRACELULAR (SANGRE / LÍQUIDO INTERSTICIAL)
    </text>

    <!-- Doble Bicapa Fosfolipídica Ondulada -->
    <path d="M 0 65 Q {ANCHO_CANVAS*0.25} 92 {ANCHO_CANVAS*0.5} 65 T {ANCHO_CANVAS} 65" fill="none" stroke="#0284c7" stroke-width="9" stroke-linecap="round"/>
    <path d="M 0 74 Q {ANCHO_CANVAS*0.25} 101 {ANCHO_CANVAS*0.5} 74 T {ANCHO_CANVAS} 74" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>

    <!-- Cabezas polares fosfolipídicas -->
    <g fill="#0284c7" opacity="0.6">
      <circle cx="150" cy="69" r="3.2"/><circle cx="168" cy="71" r="3.2"/><circle cx="186" cy="73" r="3.2"/>
      <circle cx="950" cy="78" r="3.2"/><circle cx="968" cy="77" r="3.2"/><circle cx="986" cy="75" r="3.2"/>
      <circle cx="2800" cy="75" r="3.2"/><circle cx="2818" cy="73" r="3.2"/><circle cx="2836" cy="71" r="3.2"/>
    </g>

    <!-- Canal Transportador GLUT-4 (alineado con la Glucólisis en X=1680) -->
    <g transform="translate(1640, 78)">
      <path d="M 0 6 C 10 -14, 28 -14, 34 6 C 38 20, 34 38, 25 44 C 12 47, 2 37, 0 24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
      <path d="M 80 6 C 70 -14, 52 -14, 46 6 C 42 20, 46 38, 55 44 C 68 47, 78 37, 80 24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
      <ellipse cx="40" cy="22" rx="12" ry="20" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
      <!-- Glucosa entrando -->
      <polygon points="40,15 46,18 46,25 40,28 34,25 34,18" fill="#ffffff" stroke="#ea580c" stroke-width="1.8"/>
      <circle cx="34" cy="18" r="2.2" fill="#dc2626"/>
      <text x="40" y="52" fill="#0369a1" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-4</text>
    </g>

    <!-- Flujo desde la sangre hacia la primera reacción -->
    <line x1="1680" y1="50" x2="1680" y2="78" stroke="#ea580c" stroke-width="2.6"/>
    <line x1="1680" y1="120" x2="1680" y2="155" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

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
      <path d="M 120 {y_mito + 180} 
               C 280 {y_mito - 30}, 850 {y_mito - 90}, 1520 {y_mito - 40}
               C 1950 {y_mito - 110}, 2650 {y_mito - 80}, 3250 {y_mito - 30}
               C 3620 {y_mito + 30}, 3720 {y_mito + 220}, 3680 {y_mito + 600}
               C 3620 {y_mito + 1150}, 2750 {y_mito + 1280}, 1900 {y_mito + 1260}
               C 1100 {y_mito + 1280}, 320 {y_mito + 1200}, 160 {y_mito + 800}
               C 70 {y_mito + 500}, 60 {y_mito + 300}, 120 {y_mito + 180} Z"
            fill="url(#gradMitocondria)" stroke="#92400e" stroke-width="6"/>

      <!-- Espacio Intermembrana (EIM) -->
      <path d="M 170 {y_mito + 195} 
               C 320 {y_mito}, 870 {y_mito - 55}, 1520 {y_mito - 10}
               C 1940 {y_mito - 75}, 2640 {y_mito - 45}, 3220 {y_mito}
               C 3560 {y_mito + 55}, 3650 {y_mito + 235}, 3615 {y_mito + 590}
               C 3560 {y_mito + 1110}, 2730 {y_mito + 1230}, 1900 {y_mito + 1215}
               C 1120 {y_mito + 1230}, 370 {y_mito + 1155}, 220 {y_mito + 775}
               C 140 {y_mito + 490}, 130 {y_mito + 305}, 170 {y_mito + 195} Z"
            fill="#fffbeb" fill-opacity="0.6" stroke="#b45309" stroke-width="3" stroke-dasharray="12 7"/>

      <!-- Matriz Mitocondrial (MMI Contorno interno) -->
      <path d="M 230 {y_mito + 220} 
               C 380 {y_mito + 45}, 900 {y_mito}, 1520 {y_mito + 35}
               C 1920 {y_mito - 25}, 2620 {y_mito}, 3180 {y_mito + 45}
               C 3490 {y_mito + 95}, 3570 {y_mito + 260}, 3540 {y_mito + 570}
               C 3490 {y_mito + 1060}, 2700 {y_mito + 1175}, 1900 {y_mito + 1160}
               C 1150 {y_mito + 1175}, 440 {y_mito + 1105}, 300 {y_mito + 745}
               C 220 {y_mito + 480}, 200 {y_mito + 325}, 230 {y_mito + 220} Z"
            fill="#fef3c7" fill-opacity="0.4" stroke="#d97706" stroke-width="3.5"/>

      <!-- Crestas Mitocondriales Profundas (Pliegues de MMI) -->
      <g fill="none" stroke="#b45309" stroke-width="5" stroke-linecap="round" opacity="0.65">
        <path d="M 450 {y_mito + 780} C 580 {y_mito + 620}, 720 {y_mito + 850}, 860 {y_mito + 710}"/>
        <path d="M 960 {y_mito + 840} C 1090 {y_mito + 660}, 1240 {y_mito + 880}, 1380 {y_mito + 730}"/>
        <path d="M 1520 {y_mito + 820} C 1650 {y_mito + 650}, 1800 {y_mito + 870}, 1940 {y_mito + 720}"/>
        <path d="M 2100 {y_mito + 850} C 2240 {y_mito + 670}, 2390 {y_mito + 890}, 2530 {y_mito + 740}"/>
        <path d="M 2700 {y_mito + 810} C 2850 {y_mito + 630}, 3000 {y_mito + 860}, 3150 {y_mito + 710}"/>
      </g>

      <!-- Rótulo de la Matriz integrado orgánicamente -->
      <g transform="translate(1900, {y_mito + 90})" opacity="0.85">
        <text x="0" y="0" fill="#78350f" font-size="24" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="4">MATRIZ MITOCONDRIAL</text>
        <text x="0" y="24" fill="#92400e" font-size="12.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Oxidación celular • Descarboxilación • Respiración</text>
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
    partes.append(reaccion_libre(x_g, y_g + 95, 70, "Hexocinasa", entra="-1 ATP", sale="+1 ADP", id_rx="rx_hk"))

    # 2. G6P
    partes.append(nodo_libre(x_g - 40, y_g + paso_y, "Glucosa-6-Fosfato", "6C", GLUCOSA_6_FOSFATO, "m_g6p"))
    partes.append(reaccion_libre(x_g, y_g + paso_y + 95, 65, "Fosfoglucosa Isomerasa", reversible=True, id_rx="rx_pgi"))

    # 3. F6P
    partes.append(nodo_libre(x_g - 40, y_g + paso_y * 2, "Fructosa-6-Fosfato", "6C", FRUCTOSA_6_FOSFATO, "m_f6p"))
    partes.append(reaccion_libre(x_g, y_g + paso_y * 2 + 95, 70, "PFK-1", entra="-1 ATP", sale="+1 ADP", id_rx="rx_pfk1"))

    # 4. F-1,6-BP
    partes.append(nodo_libre(x_g - 40, y_g + paso_y * 3, "Fructosa-1,6-Bisfosfato", "6C", FRUCTOSA_1_6_BISFOSFATO, "m_fbp"))
    partes.append(reaccion_libre(x_g, y_g + paso_y * 3 + 95, 65, "Aldolasa", reversible=True, id_rx="rx_aldo"))

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

    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 4 + 95, 70, "GAPDH", entra="+ NAD⁺", sale="+ NADH + H⁺", es_ganancia=True, reversible=True, id_rx="rx_gapdh"))

    # 6. 1,3-BPG
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 5, "1,3-Bisfosfoglicerato", "3C", BISFOSFOGLICERATO_1_3, "m_bpg"))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 5 + 95, 70, "Fosfoglicerato Cinasa", entra="+ ADP", sale="+ ATP", es_ganancia=True, reversible=True, id_rx="rx_pgk"))

    # 7. 3-PG
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 6, "3-Fosfoglicerato", "3C", FOSFOGLICERATO_3, "m_3pg"))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 6 + 95, 65, "Fosfoglicerato Mutasa", reversible=True, id_rx="rx_pgm"))

    # 8. 2-PG
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 7, "2-Fosfoglicerato", "3C", FOSFOGLICERATO_2, "m_2pg"))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 7 + 95, 65, "Enolasa (-H₂O)", reversible=True, id_rx="rx_eno"))

    # 9. PEP
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 8, "Fosfoenolpiruvato", "3C", FOSFOENOLPIRUVATO, "m_pep"))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 8 + 95, 70, "Piruvato Cinasa", entra="+ ADP", sale="+ ATP", es_ganancia=True, id_rx="rx_pk"))

    # 10. Piruvato (Citosol)
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 9, "Piruvato", "3C", PIRUVATO, "m_pyr_cito"))

    # Flecha Piruvato Citosol ➔ MPC
    partes.append(f"""
    <path d="M {x_g + 220} {y_g + paso_y * 9 + 85} L {x_g} {y_mito - 60}" fill="none" stroke="#ea580c" stroke-width="3" stroke-dasharray="10 6" marker-end="url(#arrowFlow)"/>
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
      <path d="M {x_g - 40} {y_g + paso_y + 35} L {x_glc + 590} {y_glc + 35}" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <text x="{(x_g - 40 + x_glc + 590)//2}" y="{y_glc + 20}" fill="#b45309" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Fosfoglucomutasa ⇄</text>
    </g>
    """)

    # UDP-Glucosa
    partes.append(nodo_libre(x_glc + 150, y_glc, "UDP-Glucosa", "6C", UDP_GLUCOSA, "m_udpg"))
    partes.append(f"""
    <g id="rx_udpg" data-arrastrable="1">
      <line x1="{x_glc + 440}" y1="{y_glc + 35}" x2="{x_glc + 290}" y2="{y_glc + 35}" stroke="#f59e0b" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <text x="{x_glc + 365}" y="{y_glc + 22}" fill="#d97706" font-size="11" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">UDP-Glucosa Pirofosforilasa (+UTP)</text>
    </g>
    """)

    # Cadena de Glucógeno
    partes.append(nodo_libre(x_glc - 80, y_glc + 220, "Glucógeno (n+1)", "Polímero", CADENA_GLUCOGENO, "m_glucogeno_cadena"))
    partes.append(f"""
    <g id="rx_sintesis_degradacion_glucogeno" data-arrastrable="1">
      <!-- Síntesis -->
      <path d="M {x_glc + 150} {y_glc + 60} Q {x_glc + 70} {y_glc + 160} {x_glc + 10} {y_glc + 215}" fill="none" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="{x_glc + 120}" y="{y_glc + 150}" fill="#b45309" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">Glucógeno Sintasa</text>

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
    partes.append(nodo_libre(x_p, y_p, "6-P-Gluconolactona", "6C", FOSFOGLUCONO_LACTONA_6, "m_lactona"))
    partes.append(reaccion_libre(x_p + 60, y_p + 75, 45, "Lactonasa (+ H₂O)", id_rx="rx_lactonasa"))

    # 2. 6-Fosfogluconato
    partes.append(nodo_libre(x_p, y_p + 130, "6-Fosfogluconato", "6C", FOSFOGLUCONATO_6, "m_6pg"))
    partes.append(reaccion_libre(x_p + 60, y_p + 205, 50, "6-Fosfogluconato DH (+ NADP⁺ ➔ + NADPH + CO₂)", es_ganancia=True, id_rx="rx_6pgdh"))

    # 3. Ribulosa-5-P
    partes.append(nodo_libre(x_p, y_p + 270, "Ribulosa-5-Fosfato", "5C", RIBULOSA_5_FOSFATO, "m_ru5p"))

    # Ramas: Xilulosa-5P y Ribosa-5P
    partes.append(nodo_libre(x_p - 100, y_p + 420, "Xilulosa-5-P", "5C", XILULOSA_5_FOSFATO, "m_xu5p", text_right=False))
    partes.append(nodo_libre(x_p + 280, y_p + 420, "Ribosa-5-P", "5C", RIBOSA_5_FOSFATO, "m_r5p"))
    partes.append(f"""
    <path d="M {x_p + 20} {y_p + 340} L {x_p - 50} {y_p + 415}" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="{x_p - 50}" y="{y_p + 375}" fill="#047857" font-size="10.5" font-family="'Inter', sans-serif" text-anchor="end">Fosfopentosa Epimerasa</text>

    <path d="M {x_p + 80} {y_p + 340} L {x_p + 270} {y_p + 415}" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="{x_p + 200}" y="{y_p + 375}" fill="#047857" font-size="10.5" font-family="'Inter', sans-serif">Fosfopentosa Isomerasa</text>
    """)

    # Sedoheptulosa-7P y Eritrosa-4P
    partes.append(nodo_libre(x_p - 100, y_p + 580, "Sedoheptulosa-7-P", "7C", SEDOHEPTULOSA_7_FOSFATO, "m_s7p", text_right=False))
    partes.append(nodo_libre(x_p + 280, y_p + 580, "Eritrosa-4-P", "4C", ERITROSA_4_FOSFATO, "m_e4p"))
    partes.append(f"""
    <text x="{x_p + 90}" y="{y_p + 520}" fill="#047857" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Transcetolasa 1 (TK1) ⇄</text>
    <text x="{x_p + 90}" y="{y_p + 680}" fill="#047857" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Transaldolasa ⇄ Retorno a F6P y GAP</text>

    <!-- Retornos elegantes sin cajas -->
    <path d="M {x_p - 110} {y_p + 695} C {x_p - 350} {y_p + 695} {x_g + 400} {y_g + paso_y * 2 + 35} {x_g + 160} {y_g + paso_y * 2 + 35}" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <text x="{(x_p + x_g)//2 + 100}" y="{y_g + paso_y * 2 + 22}" fill="#059669" font-size="12" font-weight="800" font-family="'Inter', sans-serif">Retorno: Fructosa-6-P</text>

    <path d="M {x_p - 110} {y_p + 735} C {x_p - 350} {y_p + 735} {x_g + 450} {y_g + paso_y * 4 + 35} {x_g + 300} {y_g + paso_y * 4 + 35}" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <text x="{(x_p + x_g)//2 + 150}" y="{y_g + paso_y * 4 + 22}" fill="#059669" font-size="12" font-weight="800" font-family="'Inter', sans-serif">Retorno: GAP</text>
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
        <!-- ZONA 1: CITOPLASMA (ARRIBA) - SÍNTESIS DE MALATO            -->
        <!-- =========================================================== -->
        <g transform="translate({cx_lupa}, {cy_lupa - 260})">
          <rect x="-190" y="-14" width="380" height="26" rx="13" fill="#dcfce7" stroke="#16a34a" stroke-width="1.8"/>
          <text x="0" y="4" fill="#166534" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
            🌿 CITOPLASMA: OXALACETATO CAPTA NADH
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

        <!-- FLECHA CLARA: Malato baja desde el citoplasma y cruza la membrana -->
        <path d="M {cx_lupa + 95} {cy_lupa - 70} L {cx_lupa + 95} {cy_lupa + 65}" stroke="#0284c7" stroke-width="3.2" marker-end="url(#arrowBlue)"/>
        <text x="{cx_lupa + 140}" y="{cy_lupa - 35}" fill="#0284c7" font-size="9.5" font-weight="800">Malato²⁻ cruza hacia matriz ➔</text>

        <!-- =========================================================== -->
        <!-- ZONA 2: MATRIZ MITOCONDRIAL (ABAJO) - REOXIDACIÓN A NADH   -->
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

        <!-- Retorno de Aspartato hacia el citoplasma -->
        <path d="M {cx_lupa - 90} {cy_lupa + 70} L {cx_lupa - 90} {cy_lupa - 65}" stroke="#db2777" stroke-width="2.8" marker-end="url(#arrowRed)"/>
        <text x="{cx_lupa - 95}" y="{cy_lupa - 40}" fill="#db2777" font-size="9" font-weight="800" text-anchor="end">Aspartato retorna al citosol ➔</text>

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
    # 7. MATRIZ MITOCONDRIAL: PDH Y CICLO DE KREBS (COMPACTO Y DENTRO DEL LÍMITE)
    # =========================================================================
    x_k = 1140
    y_k = y_mito + 80
    paso_k = 100  # Paso vertical compacto para no tocar el borde inferior

    partes.append(f'<g id="ruta_krebs">')

    # Complejo PDH (Transición MPC ➔ Acetil-CoA)
    partes.append(f"""
    <!-- Reacción PDH -->
    <path d="M 1680 {y_mito - 10} C 1680 {y_k - 20}, {x_k + 400} {y_k - 20}, {x_k + 370} {y_k + 10}" fill="none" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    <text x="{x_k + 500}" y="{y_k - 5}" fill="#c2410c" font-size="13" font-weight="900" font-family="'Inter', sans-serif">Complejo PDH (E1, E2, E3)</text>
    <text x="{x_k + 500}" y="{y_k + 14}" fill="#64748b" font-size="11" font-family="'Inter', sans-serif">+ CoA-SH + NAD⁺ ➔ CO₂ + NADH</text>
    """)

    # Acetil-CoA
    partes.append(nodo_libre(x_k + 220, y_k + 15, "Acetil-CoA", "2C", ACETIL_COA, "m_accoa"))

    # Oxalacetato (inicio del ciclo de Krebs)
    partes.append(nodo_libre(x_k - 160, y_k + 15, "Oxalacetato", "4C", KREBS_OXALACETATO, "m_oaa"))
    partes.append(f"""
    <!-- Condensación Citrato Sintasa -->
    <path d="M {x_k - 20} {y_k + 55} L {x_k + 210} {y_k + 55}" stroke="#b45309" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
    <path d="M {x_k + 90} {y_k + 55} L {x_k + 90} {y_k + 95}" stroke="#b45309" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    <text x="{x_k + 105}" y="{y_k + 75}" fill="#78350f" font-size="12" font-weight="800" font-family="'Inter', sans-serif">Citrato Sintasa</text>
    """)

    # Citrato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k, "Citrato", "6C", CITRATO, "m_citrato"))
    partes.append(reaccion_libre(x_k + 90, y_k + paso_k + 65, 45, "Aconitasa ⇄", reversible=True, id_rx="rx_acon"))

    # Isocitrato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 2, "Isocitrato", "6C", ISOCITRATO, "m_isocitrato"))
    partes.append(reaccion_libre(x_k + 90, y_k + paso_k * 2 + 65, 48, "Isocitrato DH", entra="+ NAD⁺", sale="+ NADH + CO₂", es_ganancia=True, id_rx="rx_icdh"))

    # Alfa-Cetoglutarato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 3, "α-Cetoglutarato", "5C", KREBS_ALFA_CETOGLUTARATO, "m_akg"))
    partes.append(reaccion_libre(x_k + 90, y_k + paso_k * 3 + 65, 48, "α-KG Deshidrogenasa", entra="+ CoA + NAD⁺", sale="+ NADH + CO₂", es_ganancia=True, id_rx="rx_akgdh"))

    # Succinil-CoA
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 4, "Succinil-CoA", "4C", SUCCINIL_COA, "m_succoa"))
    partes.append(reaccion_libre(x_k + 90, y_k + paso_k * 4 + 65, 48, "Succinil-CoA Sintetasa", entra="+ GDP + Pi", sale="+ GTP (+CoA)", es_ganancia=True, id_rx="rx_scas"))

    # Succinato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 5, "Succinato", "4C", SUCCINATO, "m_succinato"))
    partes.append(reaccion_libre(x_k + 90, y_k + paso_k * 5 + 65, 48, "Succinato DH (Complejo II)", entra="+ FAD", sale="+ FADH₂", es_ganancia=True, id_rx="rx_sdh"))

    # Fumarato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 6, "Fumarato", "4C", FUMARATO, "m_fumarato"))
    partes.append(reaccion_libre(x_k + 90, y_k + paso_k * 6 + 65, 45, "Fumarasa (+ H₂O)", reversible=True, id_rx="rx_fum"))

    # L-Malato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 7, "L-Malato", "4C", KREBS_MALATO, "m_malato"))

    # Cierre del Ciclo: Retorno de Malato a Oxalacetato (100% dentro de la matriz mitocondrial)
    partes.append(f"""
    <g id="rx_mdh_retorno" data-arrastrable="1">
      <path d="M {x_k} {y_k + paso_k * 7 + 45} C {x_k - 240} {y_k + paso_k * 7 + 45}, {x_k - 240} {y_k + 55}, {x_k - 160} {y_k + 55}" fill="none" stroke="#b45309" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <text x="{x_k - 250}" y="{y_k + paso_k * 4}" fill="#78350f" font-size="12" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 {x_k - 250} {y_k + paso_k * 4})">
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

          <!-- Figuritas moleculares vectoriales añadidas sobre el diseño del usuario -->
          <!-- 1. Estructura real de NADH entrando a Complejo I -->
          <g transform="translate(185, 615) scale(0.55)">
            {CTE_NADH}
          </g>

          <!-- 2. Estructura real de FADH2 entrando a Complejo II -->
          <g transform="translate(385, 615) scale(0.55)">
            {CTE_FADH2}
          </g>

          <!-- 3. Estructura real de Ubiquinona en la bicapa -->
          <g transform="translate(355, 425) scale(0.55)">
            {UBIQUINONA}
          </g>

          <!-- 4. Estructura real de Citocromo c en el EIM -->
          <g transform="translate(565, 425) scale(0.48)">
            {CITOCROMO_C}
          </g>

          <!-- 5. Estructuras de Oxígeno y Agua en Complejo IV -->
          <g transform="translate(670, 535) scale(0.55)">
            {OXIGENO}
          </g>
          <g transform="translate(730, 535) scale(0.55)">
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

    # Defs y Marcadores
    defs_svg = """
    <defs>
      <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
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
        <stop offset="5%" stop-color="#f0fdf4" stop-opacity="0.8" />
        <stop offset="50%" stop-color="#f8fafc" stop-opacity="0.5" />
        <stop offset="90%" stop-color="#f0fdf4" stop-opacity="0.7" />
        <stop offset="100%" stop-color="#f8fafc" stop-opacity="1" />
      </linearGradient>

      <radialGradient id="haloCitosolUnificado" cx="50%" cy="48%" r="72%">
        <stop offset="0%" stop-color="#bbf7d0" stop-opacity="0.14" />
        <stop offset="55%" stop-color="#dcfce7" stop-opacity="0.07" />
        <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
      </radialGradient>

      <radialGradient id="gradMitocondria" cx="50%" cy="100%" r="90%">
        <stop offset="0%" stop-color="#fef3c7" stop-opacity="1" />
        <stop offset="45%" stop-color="#fffbeb" stop-opacity="0.95" />
        <stop offset="75%" stop-color="#fed7aa" stop-opacity="0.9" />
        <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.8" />
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
      align-items: center;
      padding: 20px;
    }}
    .header-bar {{
      width: 100%;
      max-width: {ANCHO_CANVAS}px;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1e293b;
      padding: 12px 24px;
      border-radius: 8px;
      border: 1px solid #334155;
    }}
    .lienzo {{
      width: 100%;
      max-width: {ANCHO_CANVAS}px;
      background: #ffffff;
      border-radius: 8px;
      box-shadow: 0 25px 60px rgba(0,0,0,0.6);
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
  </style>
</head>
<body>
  <div class="header-bar">
    <div>
      <h2 style="color: #38bdf8; font-size: 1.15rem;">🌿 Entorno Biológico Real: Citosol y Gran Mitocondria (Sin Globos ni Tarjetas)</h2>
      <p style="color: #94a3b8; font-size: 0.8rem;">Glucólisis • Glucógeno • Pentosas • Lanzadera • Krebs • Cadena Respiratoria</p>
    </div>
    <span style="background: #0284c7; color: white; padding: 4px 12px; border-radius: 9999px; font-size: 0.75rem; font-weight: bold;">
      Compatible con editor_arrastrable.html
    </span>
  </div>
  <div class="lienzo">
    {svg_completo}
  </div>
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
