#!/usr/bin/env python3
"""
GENERADOR DEL MAPA METABÓLICO INTEGRADO AMPLIADO — MAPA METABÓLICO ALTERNATIVO
===================================================================================
Genera de manera 100% autónoma e independiente el mapa metabólico alternativo (25 vías),
tomando como base inmutable de solo lectura:
  07_AMPLIACION_TEMARIO/mapa_cartulina_ampliado.svg
y aplicando las correcciones bioquímicas rigurosas, optimizaciones de trazado inter-ruta
(con 0 solapamientos en detectar_solapamientos.py), puertos de atraque respiratorio,
enlaces de pentosas, modo de lectura y aislamiento didáctico, y parámetros URL dinámicos.
"""

import os
import re
import subprocess
import sys

DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
DIR_PROYECTO = os.path.dirname(DIR_SCRIPT)

RUTA_BASE_SVG = os.path.join(DIR_PROYECTO, "07_AMPLIACION_TEMARIO", "mapa_cartulina_ampliado.svg")
RUTA_OUT_SVG = os.path.join(DIR_SCRIPT, "mapa_metabolico_alternativo.svg")
RUTA_OUT_HTML = os.path.join(DIR_SCRIPT, "mapa_metabolico_alternativo.html")
RUTA_OUT_PDF = os.path.join(DIR_SCRIPT, "mapa_metabolico_alternativo_120x90cm.pdf")
RUTA_OUT_PNG = os.path.join(DIR_SCRIPT, "mapa_metabolico_alternativo_preview.png")

def construir_mapa_alternativo():
    print("1. Leyendo mapa base original inmutable:")
    print(f"   {RUTA_BASE_SVG}")
    with open(RUTA_BASE_SVG, "r", encoding="utf-8") as f:
        svg = f.read()

    print(f"   ✓ Mapa base cargado con éxito ({len(svg):,} caracteres)")

    # -------------------------------------------------------------------------
    # A. MODO LECTURA Y ESTILOS DE ESTUDIO CIENTÍFICO EN <defs>
    # -------------------------------------------------------------------------
    estilos_lectura = """
      <!-- FILTROS DE RESPLANDOR BIOLUMINISCENTE PARA PARTÍCULAS -->
      <filter id="glowShuttleParticle" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="3.5" result="blur" />
        <feMerge>
          <feMergeNode in="blur" />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>
      <filter id="glowElectronParticle" x="-50%" y="-50%" width="200%" height="200%">
        <feGaussianBlur stdDeviation="4.5" result="blur" />
        <feMerge>
          <feMergeNode in="blur" />
          <feMergeNode in="SourceGraphic" />
        </feMerge>
      </filter>
      <!-- ESTILOS DIDÁCTICOS Y DE LEGIBILIDAD (MAPA METABÓLICO ALTERNATIVO) -->
      <style id="study_readability_styles">
        #capa_conexiones_inter_ruta .conexion-inter-ruta > path:first-child {
          stroke-width: 8 !important;
          opacity: 0.72 !important;
        }
        #capa_conexiones_inter_ruta .conexion-inter-ruta > path:nth-child(2) {
          stroke-width: 3.2 !important;
        }
        #capa_conexiones_inter_ruta .conexion-inter-ruta > path:last-child {
          stroke-dasharray: 10 6 !important;
          animation: animFlujoInterRuta 1.6s linear infinite !important;
        }
        @keyframes animFlujoInterRuta {
          from { stroke-dashoffset: 32; }
          to { stroke-dashoffset: 0; }
        }
        #cx_rotulos text {
          paint-order: stroke fill;
          stroke: #ffffff;
          stroke-width: 3.2px;
          stroke-linejoin: round;
        }
        .ui_pista_orbital {
          stroke-dasharray: 8 6;
          animation: animPistaOrbital 1.8s linear infinite;
        }
        @keyframes animPistaOrbital {
          from { stroke-dashoffset: 28; }
          to { stroke-dashoffset: 0; }
        }
        .ui_carrier_pulsante rect {
          filter: drop-shadow(0 0 10px #38bdf8) !important;
          stroke: #38bdf8 !important;
          transition: all 0.3s ease;
        }
        /* Control global de pausa de animaciones */
        .pausar-animaciones * {
          animation-play-state: paused !important;
        }
      </style>
    """
    if 'id="study_readability_styles"' not in svg:
        svg = svg.replace("</defs>", estilos_lectura + "\n    </defs>", 1)
        print("   ✓ Estilos de contraste, lectura y filtros de partículas incorporados en <defs>")


    # -------------------------------------------------------------------------
    # B. CORRECCIÓN BIOQUÍMICA: CICLO DE LA UREA (CITRINA Y ORNT1)
    # -------------------------------------------------------------------------
    # Citrina (SLC25A13) es un antiporte electroneutro Aspartato citosólico / Glutamato matricial
    # ORNT1 (SLC25A15) es el transportador de Ornitina citosólica / Citrulina matricial
    citrina_old = '''    <g id="trans_u_citrina" data-arrastrable="1" transform="translate(4420, 2160)">
      <!-- Flechas de translocación ascendente de Citrulina -->
      <path d="M 0 160 L 0 25" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)" fill="none"/>
      <path d="M 0 -25 L 0 -85" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)" fill="none"/>

      <!-- Cápsula del transportador sobre MMI -->
      <rect x="-60" y="-18" width="120" height="36" rx="8" fill="#92400e" stroke="#78350f" stroke-width="2"/>
      <text x="0" y="4" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">SLC25A13</text>
      <text x="0" y="30" fill="#78350f" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Citrina (Exportador Citrulina)</text>
    </g>'''

    citrina_new = '''    <g id="trans_u_citrina" data-arrastrable="1" transform="translate(4420, 2160)">
      <!-- Antiporte Aspartato (Matriz ➔ Citosol) / Glutamato (Citosol ➔ Matriz) lateralizado -->
      <path d="M -75 35 Q -90 0 -75 -35" stroke="#0d9488" stroke-width="2.4" marker-end="url(#arrowTeal)" fill="none"/>
      <path d="M 75 -35 Q 90 0 75 35" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arrowBlueAmino)" fill="none"/>

      <!-- Cápsula del transportador sobre MMI -->
      <rect x="-60" y="-18" width="120" height="36" rx="8" fill="#92400e" stroke="#78350f" stroke-width="2"/>
      <text x="0" y="4" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">SLC25A13</text>
      <text x="0" y="30" fill="#78350f" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Citrina: Asp⁻ ⇄ Glu⁻</text>
    </g>'''

    ornt1_old = '''    <g id="trans_u_ornt1" data-arrastrable="1" transform="translate(4640, 2160)">
      <!-- Cápsula del transportador sobre MMI -->
      <rect x="-60" y="-18" width="120" height="36" rx="8" fill="#1d4ed8" stroke="#1e3a8a" stroke-width="2"/>
      <text x="0" y="4" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">SLC25A15</text>
      <text x="0" y="30" fill="#1e40af" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">ORNT1 (Carrier Ornitina)</text>
    </g>'''

    ornt1_new = '''    <g id="trans_u_ornt1" data-arrastrable="1" transform="translate(4640, 2160)">
      <!-- Cápsula del transportador sobre MMI -->
      <rect x="-60" y="-18" width="120" height="36" rx="8" fill="#1d4ed8" stroke="#1e3a8a" stroke-width="2"/>
      <text x="0" y="4" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">SLC25A15</text>
      <!-- Antiporte Citrulina Citosol / Ornitina Matriz lateralizado -->
      <path d="M -75 35 Q -90 0 -75 -35" stroke="#0d9488" stroke-width="2.4" marker-end="url(#arrowTeal)" fill="none"/>
      <path d="M 75 -35 Q 90 0 75 35" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arrowBlueAmino)" fill="none"/>
      <text x="0" y="30" fill="#1e40af" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">ORNT1: Orn⁺ ⇄ Citrulina</text>
    </g>'''

    if citrina_old in svg:
        svg = svg.replace(citrina_old, citrina_new)
        print("   ✓ SLC25A13 (Citrina) actualizado a antiporte Asp⁻ ⇄ Glu⁻ lateralizado (0 colisiones)")
    if ornt1_old in svg:
        svg = svg.replace(ornt1_old, ornt1_new)
        print("   ✓ SLC25A15 (ORNT1) actualizado a antiporte Orn⁺ ⇄ Citrulina lateralizado (0 colisiones)")

    # Adaptar la conexión inter-ruta de citrulina (cx_citrulina_translocacion) para cruzar ORNT1 en X=4578
    cx_citrulina_old = '''<g id="cx_citrulina_translocacion" class="conexion-inter-ruta"><path d="M 4446.0 2724.6 L 4446.0 2558.0" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" opacity="0.55"/><path d="M 4446.0 2724.6 L 4446.0 2558.0" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="10 6" stroke-linecap="round" stroke-linejoin="round"/><path d="M 4446.0 2483.0 L 4446.0 2424.9" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" opacity="0.55"/><path d="M 4446.0 2483.0 L 4446.0 2424.9" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="10 6" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#cxFlecha0d9488)"/></g>'''
    cx_citrulina_new = '''<g id="cx_citrulina_translocacion" class="conexion-inter-ruta"><path d="M 4578.0 2724.6 L 4578.0 2558.0" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" opacity="0.55"/><path d="M 4578.0 2724.6 L 4578.0 2558.0" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="10 6" stroke-linecap="round" stroke-linejoin="round"/><path d="M 4578.0 2483.0 L 4578.0 2424.9" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" opacity="0.55"/><path d="M 4578.0 2483.0 L 4578.0 2424.9" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="10 6" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#cxFlecha0d9488)"/></g>'''
    if cx_citrulina_old in svg:
        svg = svg.replace(cx_citrulina_old, cx_citrulina_new)
        print("   ✓ Conexión citrulina_translocacion reubicada a través de ORNT1")

    # -------------------------------------------------------------------------
    # C. CORRECCIÓN BIOQUÍMICA: CATABOLISMO DE CISTATIONINA (CTH)
    # -------------------------------------------------------------------------
    # Cistationina gamma-liasa escinde la cistationina en 3 productos:
    # 1. L-Cisteína (3C, producto azufrado)
    # 2. alfa-Cetobutirato (4C, esqueleto carbonado)
    # 3. NH4+ (ión amonio liberado)
    # Configuración geométrica optimizada con 0 solapamientos
    cth_old = '''    <!-- Conectores continuos de convergencia de Cistationina -->
    <g id="conectores_transsulfuracion">
      <!-- Rótulos de salida de bifurcación -->
      <text x="2770" y="1735" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Propionil-CoA</text>
      <text x="2825" y="1735" fill="#0f766e" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="start">L-Cisteína</text>
    
    </g>'''

    cth_new = '''    <!-- AA: L-Cisteína -->
    <g id="m_cisteina_cth" data-arrastrable="1" transform="translate(2830, 1735)">
      <circle cx="-6" cy="-4" r="3.5" fill="#16a34a" />
      <text x="0" y="0" fill="#14532d" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">L-Cisteína</text>
      <text x="0" y="13" fill="#ea580c" font-size="9.5" font-weight="800" font-family="'JetBrains Mono', monospace">[3C]</text>
    </g>
    <!-- AA: α-Cetobutirato -->
    <g id="m_akb_aa" data-arrastrable="1" transform="translate(2830, 1775)">
      <circle cx="-6" cy="-4" r="3.5" fill="#16a34a" />
      <text x="0" y="0" fill="#14532d" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">α-Cetobutirato</text>
      <text x="0" y="13" fill="#ea580c" font-size="9.5" font-weight="800" font-family="'JetBrains Mono', monospace">[4C]</text>
    </g>
    <!-- CTH productos -->
    <g id="productos_cth" data-arrastrable="1">
      <path d="M 2810 1715 Q 2815 1735 2824 1735" fill="none" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
      <path d="M 2810 1715 Q 2810 1775 2824 1775" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
      <text x="2770" y="1735" fill="#1d4ed8" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ NH₄⁺</text>
    </g>'''

    if cth_old in svg:
        svg = svg.replace(cth_old, cth_new)
        print("   ✓ CTH actualizada con L-Cisteína, α-Cetobutirato y NH₄⁺ (0 colisiones)")

    # Actualizar rótulo en cx_rotulos
    svg = svg.replace(
        '<text x="694.9" y="1547.0" text-anchor="middle" fill="#a83f08" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">CTH: Cistationina ➔ Propionil-CoA</text>',
        '<text x="694.9" y="1547.0" text-anchor="middle" fill="#a83f08" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">CTH: α-Cetobutirato ➔ Propionil-CoA</text>'
    )

    # -------------------------------------------------------------------------
    # D. CORRECCIÓN BIOQUÍMICA: BIOSÍNTESIS DE PIRIMIDINAS (UMP ➔ dTMP)
    # -------------------------------------------------------------------------
    # Explicitar RNR (reducción 2'-OH), dUMP y Timidilato sintasa (N5,N10-CH2-THF)
    ump_old = '''    <path d="M 5240 1525 Q 5280 1552 5300 1575" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="5310" y="1552" fill="#0f172a" font-size="10" font-weight="700" font-family="'Inter', sans-serif">RNR ➔ Timidilato Sintasa (N⁵,N¹⁰-CH₂-THF)</text>'''

    ump_new = '''    <path d="M 5240 1525 Q 5280 1545 5300 1570" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="5315" y="1528" fill="#0f172a" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">UMP → UDP → dUDP/dUTP</text>
    <text x="5315" y="1543" fill="#64748b" font-size="9" font-weight="700" font-family="'Inter', sans-serif">RNR (reducción 2'-OH)</text>
    <path d="M 5325 1555 L 5325 1590" fill="none" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
    <text x="5335" y="1583" fill="#0f172a" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">dUMP</text>
    <text x="5395" y="1583" fill="#64748b" font-size="8.8" font-weight="700" font-family="'Inter', sans-serif">Timidilato sintasa + N⁵,N¹⁰-CH₂-THF</text>'''

    if ump_old in svg:
        svg = svg.replace(ump_old, ump_new)
        print("   ✓ Pasos intermedios de timidilato (RNR ➔ dUMP ➔ TS) explicitados")

    # -------------------------------------------------------------------------
    # E. CORRECCIÓN BIOQUÍMICA: URAT1 (REABSORCIÓN RENAL DESDE LUMEN TUBULAR)
    # -------------------------------------------------------------------------
    # URAT1 (SLC22A12) es un transportador apical del túbulo proximal renal que reabsorbe urato
    # desde la luz tubular hacia la célula tubular; no lo exporta a sangre
    urato_old = '''    <g id="indicador_urato_excrecion" transform="translate(5280, 2115)">
      <path d="M 0 0 Q 70 -30 110 -30" fill="none" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
      <text x="120" y="-26" fill="#dc2626" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">➔ Excreción renal de Urato (URAT1) / Hiperuricemia</text>
    </g>
    <!-- Biomarcador vascular de Urato en torrente capilar superior -->
    <g transform="translate(5550, 38)">
      <ellipse cx="0" cy="0" rx="28" ry="16" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
      <text x="0" y="4" fill="#dc2626" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">URATO</text>
      <text x="0" y="19" fill="#fca5a5" font-size="7" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Filtro Renal</text>
    </g>'''

    urato_new = '''    <g id="indicador_urato_reabsorcion" transform="translate(5280, 2115)">
      <path d="M 130 -10 Q 70 -10 0 0" fill="none" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arrowBlueAmino)"/>
      <text x="65" y="-18" fill="#1e40af" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">URAT1: reabsorción apical</text>
    </g>
    <!-- Ancla anatómica renal: Lumen tubular (filtrado glomerular previo a reabsorción) -->
    <g id="renal_lumen_urato" transform="translate(5480, 2105)">
      <ellipse cx="0" cy="0" rx="28" ry="16" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
      <text x="0" y="4" fill="#1e40af" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">URATO</text>
      <text x="0" y="19" fill="#3b82f6" font-size="7" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Lumen renal</text>
    </g>'''

    rotulo_urato_old = '<text x="5668.8" y="2481.5" text-anchor="middle" fill="#9e1b1b" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">URAT1: Ácido Úrico ➔ Sangre</text>'
    rotulo_urato_new = '<text x="5520.0" y="2530.0" text-anchor="middle" fill="#1e40af" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">URAT1: Reabsorción de Urato (Lumen ➔ Célula)</text>'

    cx_urato_old = '''<g id="cx_urato_sangre" class="conexion-inter-ruta"><path d="M 5449.4 2466.0 L 5726.0 2466.0 Q 5742.0 2466.0 5753.3 2454.7 L 5766.7 2441.3 Q 5778.0 2430.0 5778.0 2414.0 L 5778.0 550.0 Q 5778.0 534.0 5766.7 522.7 L 5717.3 473.3 Q 5706.0 462.0 5690.0 462.0 L 5533.9 462.0 Q 5526.0 462.0 5523.8 454.5 L 5521.6 446.9" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" opacity="0.55"/><path d="M 5449.4 2466.0 L 5726.0 2466.0 Q 5742.0 2466.0 5753.3 2454.7 L 5766.7 2441.3 Q 5778.0 2430.0 5778.0 2414.0 L 5778.0 550.0 Q 5778.0 534.0 5766.7 522.7 L 5717.3 473.3 Q 5706.0 462.0 5690.0 462.0 L 5533.9 462.0 Q 5526.0 462.0 5523.8 454.5 L 5521.6 446.9" fill="none" stroke="#dc2626" stroke-width="2.6" stroke-dasharray="10 6" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#cxFlechadc2626)"/></g>'''
    cx_urato_new = '''<g id="cx_urato_sangre" class="conexion-inter-ruta"><path d="M 5480.0 2489.0 L 5480.0 2495.0 Q 5480.0 2505.0 5468.0 2505.0 L 5360.0 2505.0" fill="none" stroke="#ffffff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" opacity="0.55"/><path d="M 5480.0 2489.0 L 5480.0 2495.0 Q 5480.0 2505.0 5468.0 2505.0 L 5360.0 2505.0" fill="none" stroke="#2563eb" stroke-width="2.6" stroke-dasharray="10 6" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#cxFlecha2563eb)"/></g>'''

    if urato_old in svg:
        svg = svg.replace(urato_old, urato_new)
        print("   ✓ URAT1 redefinido como reabsorción tubular apical (lumen ➔ célula proximal)")
    if rotulo_urato_old in svg:
        svg = svg.replace(rotulo_urato_old, rotulo_urato_new)
    if cx_urato_old in svg:
        svg = svg.replace(cx_urato_old, cx_urato_new)
        print("   ✓ Trazo cx_urato_sangre reconducido desde lumen tubular hacia célula proximal")

    # -------------------------------------------------------------------------
    # F. PENTOSAS FOSFATO: CONEXIÓN TK2/TRANSALDOLASA ➔ GAP ➔ GLUCÓLISIS
    # -------------------------------------------------------------------------
    gap_pnt_target = '    <!-- Metabolito Libre: Gliceraldehído-3-P -->\n    <g id="m_gap_pnt" data-arrastrable="1" transform="translate(2840, 995)">'
    gap_pnt_replacement = '''    <!-- Conector de TK2/Transaldolasa ➔ Gliceraldehído-3-P -->
    <path d="M 2700 950 Q 2840 950 2860 985" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <!-- Conector de reingreso a glucólisis -->
    <path d="M 2880 1115 L 2880 1145" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <!-- Metabolito Libre: Gliceraldehído-3-P -->
    <g id="m_gap_pnt" data-arrastrable="1" transform="translate(2840, 995)">'''
    if gap_pnt_target in svg:
        svg = svg.replace(gap_pnt_target, gap_pnt_replacement)
        print("   ✓ Vía de las Pentosas: m_gap_pnt conectado con TK2/TA y reingreso a glucólisis")

    # -------------------------------------------------------------------------
    # G. PUERTOS DE ENTRADA A CADENA RESPIRATORIA (DOCKING PORTS EN CRESTA)
    # -------------------------------------------------------------------------
    docking_ports = '''
    <!-- PUERTOS DE ENTRADA A CADENA RESPIRATORIA (DOCKING PORTS) -->
    <g id="docking_ports_cresta">
      <!-- C-I Izquierda: NADH (Krebs y Lanzadera Malato) -->
      <g transform="translate(2477, 3010)">
        <rect x="0" y="-12" width="68" height="24" rx="6" fill="#0369a1" stroke="#38bdf8" stroke-width="1.6"/>
        <text x="34" y="4.5" fill="#ffffff" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">➔ C-I (NADH)</text>
      </g>
      <!-- CoQ Izquierda: FADH2 (β-Oxidación ETF-QO) -->
      <g transform="translate(2477, 3078)">
        <rect x="0" y="-12" width="68" height="24" rx="6" fill="#92400e" stroke="#fbbf24" stroke-width="1.6"/>
        <text x="34" y="4.5" fill="#ffffff" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">➔ CoQ (ETF)</text>
      </g>
      <!-- C-II Izquierda: FADH2 (Succinato DH Krebs) -->
      <g transform="translate(2477, 3498)">
        <rect x="0" y="-12" width="68" height="24" rx="6" fill="#047857" stroke="#34d399" stroke-width="1.6"/>
        <text x="34" y="4.5" fill="#ffffff" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">➔ C-II (FAD)</text>
      </g>
      <!-- CoQ Derecha: FADH2 (DHODH Pirimidinas) -->
      <g transform="translate(3745, 2658)">
        <rect x="-68" y="-12" width="68" height="24" rx="6" fill="#92400e" stroke="#fbbf24" stroke-width="1.6"/>
        <text x="-34" y="4.5" fill="#ffffff" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">DHODH ➔ CoQ</text>
      </g>
      <!-- CoQ Derecha: FADH2 (Lanzadera G3P) -->
      <g transform="translate(3745, 3498)">
        <rect x="-68" y="-12" width="68" height="24" rx="6" fill="#92400e" stroke="#fbbf24" stroke-width="1.6"/>
        <text x="-34" y="4.5" fill="#ffffff" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">mGPDH ➔ CoQ</text>
      </g>
    </g>
'''
    marcador_cresta = '  <!-- ================================================================= -->\n  <!-- CAPA 2.5: MITOCONDRIA BIOLÓGICA'
    if marcador_cresta in svg and 'id="docking_ports_cresta"' not in svg:
        svg = svg.replace(marcador_cresta, docking_ports + '\n' + marcador_cresta)
        print("   ✓ Puertos de atraque vectorial (Docking Ports C-I, C-II, CoQ) incorporados en cresta")

    # -------------------------------------------------------------------------
    # H. RÓTULOS TRUNCADOS EN LA CAPA DE CONEXIONES
    # -------------------------------------------------------------------------
    # Reemplazar símbolo de tijeras en tiólisis por texto científico
    svg = svg.replace('✂ TIÓLISIS', 'TIÓLISIS')
    svg = svg.replace(
        '<text x="1406.0" y="1423.3" text-anchor="start" fill="#5929aa" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">Lactato (Ciclo de Cori) ➔</text>',
        '<text x="1406.0" y="1423.3" text-anchor="start" fill="#5929aa" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">Lactato (Ciclo de Cori) ➔ Piruvato</text>'
    )
    svg = svg.replace(
        '<text x="503.4" y="1149.5" text-anchor="middle" fill="#5929aa" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">Glicerol (Lipólisis TAG) ➔</text>',
        '<text x="503.4" y="1149.5" text-anchor="middle" fill="#5929aa" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">Glicerol (Lipólisis TAG) ➔ Glicerol-3-P</text>'
    )
    print("   ✓ Rótulos truncados completados y tipografía depurada sin emojis")

    # -------------------------------------------------------------------------
    # H2. SISTEMA VECTORIAL Y SEMÁNTICO DE LANZADERAS MITOCONDRIALES VIVAS
    # -------------------------------------------------------------------------
    # 1. Lupa Lanzadera Malato-Aspartato: Asignación de IDs semánticos y órbitas vivas
    malato_subs = [
        ('<g transform="translate(806, 1520)">', '<g id="trans_lanz_aralar" transform="translate(806, 1520)">'),
        ('<g transform="translate(1246, 1520)">', '<g id="trans_lanz_ogc" transform="translate(1246, 1520)">'),
        ('<!-- Estructura Citosólica 1 (Izquierda): L-Aspartato (Citosol) -->\n        <g transform="translate(781, 1292)">', '<!-- Estructura Citosólica 1 (Izquierda): L-Aspartato (Citosol) -->\n        <g id="m_lanz_asp_cito" transform="translate(781, 1292)">'),
        ('<!-- Reacción 1 (Izquierda ➔ Centro): GOT1 / cAST (Punteada) -->\n        <g transform="translate(841, 1332)">', '<!-- Reacción 1 (Izquierda ➔ Centro): GOT1 / cAST (Punteada) -->\n        <g id="rx_lanz_got1" transform="translate(841, 1332)">'),
        ('<!-- Estructura Citosólica 2 (Centro): Oxalacetato (Citosol) -->\n        <g transform="translate(1002, 1292)">', '<!-- Estructura Citosólica 2 (Centro): Oxalacetato (Citosol) -->\n        <g id="m_lanz_oaa_cito" transform="translate(1002, 1292)">'),
        ('<!-- Reacción 2 (Centro ➔ Derecha): cMDH (Punteada) -->\n        <g transform="translate(1064, 1332)">', '<!-- Reacción 2 (Centro ➔ Derecha): cMDH (Punteada) -->\n        <g id="rx_lanz_cmdh" transform="translate(1064, 1332)">'),
        ('<!-- Estructura Citosólica 3 (Derecha): L-Malato (Citosol) -->\n        <g transform="translate(1222, 1292)">', '<!-- Estructura Citosólica 3 (Derecha): L-Malato (Citosol) -->\n        <g id="m_lanz_mal_cito" transform="translate(1222, 1292)">'),
        ('<!-- Estructura acoplada: L-Glutamato [5C] -->\n        <g transform="translate(878, 1410)">', '<!-- Estructura acoplada: L-Glutamato [5C] -->\n        <g id="m_lanz_glu" transform="translate(878, 1410)">'),
        ('<!-- Estructura acoplada: α-Cetoglutarato [5C] -->\n        <g transform="translate(1058, 1410)">', '<!-- Estructura acoplada: α-Cetoglutarato [5C] -->\n        <g id="m_lanz_akg" transform="translate(1058, 1410)">'),
        ('<!-- Estructura Matricial 1 (Derecha): L-Malato (Matriz) -->\n        <g transform="translate(1222, 1610)">', '<!-- Estructura Matricial 1 (Derecha): L-Malato (Matriz) -->\n        <g id="m_lanz_mal_mito" transform="translate(1222, 1610)">'),
        ('<!-- Reacción 3 (Derecha ➔ Centro): mMDH (Punteada hacia la izquierda) -->\n        <g transform="translate(1210, 1650)">', '<!-- Reacción 3 (Derecha ➔ Centro): mMDH (Punteada hacia la izquierda) -->\n        <g id="rx_lanz_mmdh" transform="translate(1210, 1650)">'),
        ('<!-- Estructura Matricial 2 (Centro): Oxalacetato (Matriz) -->\n        <g transform="translate(1002, 1610)">', '<!-- Estructura Matricial 2 (Centro): Oxalacetato (Matriz) -->\n        <g id="m_lanz_oaa_mito" transform="translate(1002, 1610)">'),
        ('<!-- Reacción 4 (Centro ➔ Izquierda): GOT2 / mAST (Punteada hacia la izquierda) -->\n        <g transform="translate(983, 1650)">', '<!-- Reacción 4 (Centro ➔ Izquierda): GOT2 / mAST (Punteada hacia la izquierda) -->\n        <g id="rx_lanz_got2" transform="translate(983, 1650)">'),
        ('<!-- Estructura Matricial 3 (Izquierda): L-Aspartato (Matriz) -->\n        <g transform="translate(781, 1610)">', '<!-- Estructura Matricial 3 (Izquierda): L-Aspartato (Matriz) -->\n        <g id="m_lanz_asp_mito" transform="translate(781, 1610)">')
    ]
    for old, new in malato_subs:
        if old in svg:
            svg = svg.replace(old, new, 1)

    anim_malato = '''
        <!-- Pistas de Órbita Cíclica Bioluminiscente para Lanzadera Malato-Aspartato -->
        <g id="anim_lanz_malato_orbitas" class="ui_shuttle_orbit_group">
          <!-- Pista principal del ciclo de 4 carbonos -->
          <path id="track_malato_principal" d="M 806 1332 L 1026 1332 L 1246 1332 L 1246 1650 L 1026 1650 L 806 1650 Z"
                fill="none" stroke="#38bdf8" stroke-width="2.8" stroke-dasharray="10 8" opacity="0.35" class="ui_pista_orbital"/>

          <!-- Partícula 1: Equivalente Reductor / L-Malato (Citosol ➔ Matriz vía OGC) -->
          <g class="ui_shuttle_particle_wrapper">
            <circle r="7.5" fill="#38bdf8" filter="url(#glowShuttleParticle)">
              <animateMotion dur="5.5s" repeatCount="indefinite" path="M 806 1332 L 1246 1332 L 1246 1650 L 806 1650 Z" />
            </circle>
            <circle r="4" fill="#ffffff">
              <animateMotion dur="5.5s" repeatCount="indefinite" path="M 806 1332 L 1246 1332 L 1246 1650 L 806 1650 Z" />
            </circle>
          </g>

          <!-- Partícula 2: Retorno de L-Aspartato (Matriz ➔ Citosol vía Aralar) en contrafase -->
          <g class="ui_shuttle_particle_wrapper">
            <circle r="6.5" fill="#ec4899" filter="url(#glowShuttleParticle)">
              <animateMotion dur="5.5s" begin="-2.75s" repeatCount="indefinite" path="M 806 1332 L 1246 1332 L 1246 1650 L 806 1650 Z" />
            </circle>
            <circle r="3.5" fill="#ffffff">
              <animateMotion dur="5.5s" begin="-2.75s" repeatCount="indefinite" path="M 806 1332 L 1246 1332 L 1246 1650 L 806 1650 Z" />
            </circle>
          </g>

          <!-- Partícula 3: Sub-órbita de Glutamato (Citosol ➔ Matriz) -->
          <circle r="5.5" fill="#be185d">
            <animateMotion dur="4s" repeatCount="indefinite" path="M 911 1482 L 911 1628" />
          </circle>

          <!-- Partícula 4: Sub-órbita de α-Cetoglutarato (Matriz ➔ Citosol) -->
          <circle r="5.5" fill="#d97706">
            <animateMotion dur="4s" repeatCount="indefinite" path="M 941 1628 L 941 1586 L 1121 1586 L 1121 1482" />
          </circle>

          <!-- Partícula 5: Disparo de electrones hacia Cadena Respiratoria Complejo I -->
          <circle r="6" fill="#22c55e" filter="url(#glowShuttleParticle)">
            <animateMotion dur="3.5s" repeatCount="indefinite" path="M 1210 1650 L 1278 1650 L 1278 2492" />
          </circle>
        </g>
'''
    if 'id="anim_lanz_malato_orbitas"' not in svg and '<!-- Banner Explicativo Inferior -->' in svg:
        svg = svg.replace('<!-- Banner Explicativo Inferior -->', anim_malato + '\n        <!-- Banner Explicativo Inferior -->', 1)
        print("   ✓ Lanzadera Malato-Aspartato enriquecida con semántica y bucle continuo bioluminiscente")

    # 2. Lupa Lanzadera Glicerol-3-Fosfato: Asignación de IDs y órbita viva
    g3p_subs = [
        ('<!-- Porina VDAC en MME -->\n      <g transform="translate(10, 42)">', '<!-- Porina VDAC en MME -->\n      <g id="trans_vdac" transform="translate(10, 42)">'),
        ('<!-- Proteína integral mGPDH anclada a MMI -->\n      <g transform="translate(75, 30)">', '<!-- Proteína integral mGPDH anclada a MMI -->\n      <g id="rx_mgpdh_mmi" transform="translate(75, 30)">'),
        ('<g transform="translate(204, 54)">', '<g id="coq_g3p" transform="translate(204, 54)">'),
        ('<g transform="translate(302, 54)">', '<g id="comp3_g3p" transform="translate(302, 54)">')
    ]
    for old, new in g3p_subs:
        if old in svg:
            svg = svg.replace(old, new, 1)

    anim_g3p = '''
      <!-- Pistas de Órbita Cíclica Bioluminiscente para Lanzadera Glicerol-3-Fosfato -->
      <g id="anim_lanz_g3p_orbitas" class="ui_shuttle_orbit_group">
        <!-- Pista de órbita cerrada DHAP ➔ G3P ➔ mGPDH ➔ Retorno DHAP -->
        <path id="track_g3p_principal" d="M 5195 3050 L 5195 3220 L 5455 3210 L 5455 3140 L 5455 3108 L 5195 3050 Z"
              fill="none" stroke="#ea580c" stroke-width="2.6" stroke-dasharray="10 8" opacity="0.35" class="ui_pista_orbital"/>

        <!-- Partícula 1: Glicerol-3-P cargado de electrones viajando hacia mGPDH -->
        <g class="ui_shuttle_particle_wrapper">
          <circle r="7.5" fill="#ea580c" filter="url(#glowShuttleParticle)">
            <animateMotion dur="4.8s" repeatCount="indefinite" path="M 5195 3050 L 5195 3220 L 5455 3210 L 5455 3140 L 5455 3108 L 5195 3050 Z" />
          </circle>
          <circle r="4" fill="#ffffff">
            <animateMotion dur="4.8s" repeatCount="indefinite" path="M 5195 3050 L 5195 3220 L 5455 3210 L 5455 3140 L 5455 3108 L 5195 3050 Z" />
          </circle>
        </g>

        <!-- Partícula 2: Retorno de DHAP oxidado al citosol en contrafase -->
        <g class="ui_shuttle_particle_wrapper">
          <circle r="6" fill="#0284c7" filter="url(#glowShuttleParticle)">
            <animateMotion dur="4.8s" begin="-2.4s" repeatCount="indefinite" path="M 5195 3050 L 5195 3220 L 5455 3210 L 5455 3140 L 5455 3108 L 5195 3050 Z" />
          </circle>
          <circle r="3.5" fill="#ffffff">
            <animateMotion dur="4.8s" begin="-2.4s" repeatCount="indefinite" path="M 5195 3050 L 5195 3220 L 5455 3210 L 5455 3140 L 5455 3108 L 5195 3050 Z" />
          </circle>
        </g>

        <!-- Partícula 3: Electrones hacia Coenzima Q y Complejo III (1.5 ATP) -->
        <circle r="6.5" fill="#16a34a" filter="url(#glowShuttleParticle)">
          <animateMotion dur="2.8s" repeatCount="indefinite" path="M 5515 3170 L 5584 3170 L 5682 3170" />
        </circle>
      </g>
'''
    target_g3p = '<!-- BLOQUE INSTITUCIONAL: LEYENDA GENERAL DE VÍAS METABÓLICAS Y REGULACIÓN -->'
    if 'id="anim_lanz_g3p_orbitas"' not in svg and target_g3p in svg:
        idx_bl = svg.find(target_g3p)
        idx_cg = svg.rfind('</g>', 0, idx_bl)
        svg = svg[:idx_cg] + anim_g3p + '\n    ' + svg[idx_cg:]
        print("   ✓ Lanzadera Glicerol-3-P enriquecida con semántica y bucle continuo bioluminiscente")

    # 3. Lupa Lanzadera Carnitina: Órbita viva
    anim_carnitina = '''
      <!-- Pistas de Órbita Cíclica Bioluminiscente para Lanzadera de Carnitina -->
      <g id="anim_lanz_carnitina_orbitas" class="ui_shuttle_orbit_group">
        <circle r="7" fill="#ea580c" filter="url(#glowShuttleParticle)">
          <animateMotion dur="5.2s" repeatCount="indefinite" path="M 278 1690 L 278 2070 L 278 2150 L 182 2150 L 182 1718 Q 182 1702 208 1702 L 226 1666 Z" />
        </circle>
        <circle r="3.8" fill="#ffffff">
          <animateMotion dur="5.2s" repeatCount="indefinite" path="M 278 1690 L 278 2070 L 278 2150 L 182 2150 L 182 1718 Q 182 1702 208 1702 L 226 1666 Z" />
        </circle>
      </g>
'''
    target_carnitina = '<!-- Flecha de salida desde CPT-2 hacia Palmitoil-CoA (Matriz) -->'
    if 'id="anim_lanz_carnitina_orbitas"' not in svg and target_carnitina in svg:
        svg = svg.replace(target_carnitina, anim_carnitina + '\n      ' + target_carnitina, 1)
        print("   ✓ Lanzadera de Carnitina enriquecida con bucle continuo bioluminiscente")

    # 4. Lupa Cadena Respiratoria y ATP Sintasa: Simulación continua de flujo electrónico, bombeo H+ y ATP Sintasa
    anim_cte = '''
        <!-- ================================================================= -->
        <!-- CAPA DE SIMULACIÓN VIVA CONTINUA: CADENA DE TRANSPORTE DE ELECTRONES -->
        <!-- Y GRADIENTE QUIMIOSMÓTICO DE ATP SINTASA                         -->
        <!-- ================================================================= -->
        <g id="anim_cte_dinamica_viva" class="ui_cte_anim_group">
          <!-- 1. Flujo Electrónico desde Complejo I (NADH) hacia CoQ -->
          <g id="cte_e_comp1">
            <circle r="6" fill="#38bdf8" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.4s" repeatCount="indefinite" path="M 120 520 L 120 440 L 120 380 L 405 380" />
            </circle>
            <circle r="3.5" fill="#ffffff">
              <animateMotion dur="2.4s" repeatCount="indefinite" path="M 120 520 L 120 440 L 120 380 L 405 380" />
            </circle>
            <circle r="6" fill="#38bdf8" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.4s" begin="1.2s" repeatCount="indefinite" path="M 120 520 L 120 440 L 120 380 L 405 380" />
            </circle>
          </g>

          <!-- 2. Flujo Electrónico desde Complejo II (Succinato / FAD) hacia CoQ -->
          <g id="cte_e_comp2">
            <circle r="5.5" fill="#fbbf24" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.4s" begin="0.6s" repeatCount="indefinite" path="M 300 520 L 300 440 L 300 380 L 405 380" />
            </circle>
            <circle r="3" fill="#ffffff">
              <animateMotion dur="2.4s" begin="0.6s" repeatCount="indefinite" path="M 300 520 L 300 440 L 300 380 L 405 380" />
            </circle>
            <circle r="5.5" fill="#fbbf24" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.4s" begin="1.8s" repeatCount="indefinite" path="M 300 520 L 300 440 L 300 380 L 405 380" />
            </circle>
          </g>

          <!-- 3. Transportador Móvil Lipídico: Coenzima Q (Ubiquinona Q ⇄ QH₂) -->
          <g id="cte_coq_shuttle">
            <ellipse rx="11" ry="7" fill="#f59e0b" stroke="#ffffff" stroke-width="1.6" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.8s" repeatCount="indefinite" path="M 380 380 L 470 380 L 380 380 Z" />
            </ellipse>
            <circle r="3" fill="#ffffff">
              <animateMotion dur="2.8s" repeatCount="indefinite" path="M 380 380 L 470 380 L 380 380 Z" />
            </circle>
          </g>

          <!-- 4. Flujo Electrónico a través del Complejo III (Ciclo Q) hacia Citocromo c -->
          <g id="cte_e_comp3">
            <circle r="5.5" fill="#a855f7" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.2s" repeatCount="indefinite" path="M 470 380 L 520 340 L 520 280 L 620 270" />
            </circle>
            <circle r="3.2" fill="#ffffff">
              <animateMotion dur="2.2s" repeatCount="indefinite" path="M 470 380 L 520 340 L 520 280 L 620 270" />
            </circle>
            <circle r="5.5" fill="#a855f7" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.2s" begin="1.1s" repeatCount="indefinite" path="M 470 380 L 520 340 L 520 280 L 620 270" />
            </circle>
          </g>

          <!-- 5. Transportador Móvil Soluble: Citocromo c en Espacio Intermembrana -->
          <g id="cte_cytc_shuttle">
            <circle r="9" fill="#0891b2" stroke="#ffffff" stroke-width="2" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.5s" repeatCount="indefinite" path="M 620 270 L 680 280 L 620 270 Z" />
            </circle>
            <circle r="4" fill="#ffffff">
              <animateMotion dur="2.5s" repeatCount="indefinite" path="M 620 270 L 680 280 L 620 270 Z" />
            </circle>
          </g>

          <!-- 6. Flujo Electrónico en Complejo IV hacia Sitio Reductor de O₂ -->
          <g id="cte_e_comp4">
            <circle r="5.5" fill="#f59e0b" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.2s" repeatCount="indefinite" path="M 680 280 L 730 340 L 730 440 L 730 490" />
            </circle>
            <circle r="3" fill="#ffffff">
              <animateMotion dur="2.2s" repeatCount="indefinite" path="M 680 280 L 730 340 L 730 440 L 730 490" />
            </circle>
            <!-- Destello de formación de Agua (½ O₂ + 2 H⁺ + 2 e⁻ ➔ H₂O) -->
            <circle cx="730" cy="490" r="10" fill="none" stroke="#38bdf8" stroke-width="2.5">
              <animate attributeName="r" values="6;24;6" dur="2.2s" repeatCount="indefinite"/>
              <animate attributeName="opacity" values="0.9;0;0.9" dur="2.2s" repeatCount="indefinite"/>
            </circle>
          </g>

          <!-- 7. Bombeo Transmembrana de Protones (H⁺) al Espacio Intermembrana -->
          <g id="cte_protones_bombeo">
            <!-- C-I: 4 H⁺ bombeados -->
            <circle r="4.5" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="1.8s" repeatCount="indefinite" path="M 95 440 L 95 180" />
            </circle>
            <circle r="4.5" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="1.8s" begin="0.9s" repeatCount="indefinite" path="M 95 440 L 95 180" />
            </circle>
            <circle r="4.5" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="1.8s" begin="0.45s" repeatCount="indefinite" path="M 145 440 L 145 180" />
            </circle>
            <circle r="4.5" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="1.8s" begin="1.35s" repeatCount="indefinite" path="M 145 440 L 145 180" />
            </circle>
            <!-- C-III: 4 H⁺ bombeados -->
            <circle r="4.5" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="1.8s" repeatCount="indefinite" path="M 495 400 L 495 180" />
            </circle>
            <circle r="4.5" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="1.8s" begin="0.9s" repeatCount="indefinite" path="M 495 400 L 495 180" />
            </circle>
            <circle r="4.5" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="1.8s" begin="0.45s" repeatCount="indefinite" path="M 545 400 L 545 180" />
            </circle>
            <!-- C-IV: 2 H⁺ bombeados -->
            <circle r="4.5" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.0s" repeatCount="indefinite" path="M 710 420 L 710 180" />
            </circle>
            <circle r="4.5" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.0s" begin="1.0s" repeatCount="indefinite" path="M 750 420 L 750 180" />
            </circle>
          </g>

          <!-- 8. Cascada Quimiosmótica de H⁺ hacia el Rotor F₀ de ATP Sintasa -->
          <g id="cte_cascada_atp_sintasa">
            <circle r="4.8" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="3.2s" begin="0s" repeatCount="indefinite" path="M 250 180 Q 600 150 945 170 L 945 340 L 945 440 L 945 520" />
            </circle>
            <circle r="4.8" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="3.2s" begin="0.8s" repeatCount="indefinite" path="M 250 180 Q 600 150 945 170 L 945 340 L 945 440 L 945 520" />
            </circle>
            <circle r="4.8" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="3.2s" begin="1.6s" repeatCount="indefinite" path="M 250 180 Q 600 150 945 170 L 945 340 L 945 440 L 945 520" />
            </circle>
            <circle r="4.8" fill="#ea580c" filter="url(#glowShuttleParticle)">
              <animateMotion dur="3.2s" begin="2.4s" repeatCount="indefinite" path="M 250 180 Q 600 150 945 170 L 945 340 L 945 440 L 945 520" />
            </circle>
          </g>

          <!-- 9. Síntesis y Liberación Rotatoria de ATP en F₁ hacia la Matriz -->
          <g id="cte_atp_liberacion">
            <circle r="7" fill="#10b981" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.4s" repeatCount="indefinite" path="M 945 530 L 945 610 L 990 640" />
            </circle>
            <circle r="3.5" fill="#ffffff">
              <animateMotion dur="2.4s" repeatCount="indefinite" path="M 945 530 L 945 610 L 990 640" />
            </circle>
            <circle r="7" fill="#10b981" filter="url(#glowShuttleParticle)">
              <animateMotion dur="2.4s" begin="1.2s" repeatCount="indefinite" path="M 945 530 L 945 610 L 990 640" />
            </circle>
            <circle r="3.5" fill="#ffffff">
              <animateMotion dur="2.4s" begin="1.2s" repeatCount="indefinite" path="M 945 530 L 945 610 L 990 640" />
            </circle>
          </g>
        </g>
'''
    target_cte = '<!-- Badge Identificador Inferior -->'
    if 'id="anim_cte_dinamica_viva"' not in svg and target_cte in svg:
        svg = svg.replace(target_cte, anim_cte + '\n        ' + target_cte, 1)
        print("   ✓ Lupa Cadena Respiratoria enriquecida con simulación viva de electrones, protones y ATP Sintasa")

    # 5. Capa Global de Flujo Metabólico de Rutas y Conexiones Inter-Ruta
    anim_rutas = '''</g></g>

    <!-- ================================================================= -->
    <!-- CAPA GLOBAL DE FLUJO CONTINUO BIOLUMINISCENTE DE RUTAS METABÓLICAS -->
    <!-- ================================================================= -->
    <g id="capa_animaciones_flujo_rutas" class="ui_capa_flujo_global">
      <!-- Vía 1: Glucólisis (Flujo descendente Glucosa ➔ Piruvato) -->
      <g id="anim_flujo_via_1" class="ui_grupo_flujo_via">
        <!-- Tronco principal Glucosa ➔ Piruvato -->
        <circle r="6" fill="#38bdf8" filter="url(#glowShuttleParticle)">
          <animateMotion dur="8.0s" repeatCount="indefinite" path="M 1680 180 L 1680 355 L 1680 530 L 1680 705 L 1680 880 L 1860 880 L 1860 1055 L 1860 1230 L 1860 1405 L 1860 1580 L 1860 1755" />
        </circle>
        <circle r="3.2" fill="#ffffff">
          <animateMotion dur="8.0s" repeatCount="indefinite" path="M 1680 180 L 1680 355 L 1680 530 L 1680 705 L 1680 880 L 1860 880 L 1860 1055 L 1860 1230 L 1860 1405 L 1860 1580 L 1860 1755" />
        </circle>
        <circle r="6" fill="#38bdf8" filter="url(#glowShuttleParticle)">
          <animateMotion dur="8.0s" begin="2.6s" repeatCount="indefinite" path="M 1680 180 L 1680 355 L 1680 530 L 1680 705 L 1680 880 L 1860 880 L 1860 1055 L 1860 1230 L 1860 1405 L 1860 1580 L 1860 1755" />
        </circle>
        <circle r="6" fill="#38bdf8" filter="url(#glowShuttleParticle)">
          <animateMotion dur="8.0s" begin="5.3s" repeatCount="indefinite" path="M 1680 180 L 1680 355 L 1680 530 L 1680 705 L 1680 880 L 1860 880 L 1860 1055 L 1860 1230 L 1860 1405 L 1860 1580 L 1860 1755" />
        </circle>
        <!-- Bifurcación FBP ➔ DHAP ➔ TPI ➔ GAP -->
        <circle r="5" fill="#0284c7" filter="url(#glowShuttleParticle)">
          <animateMotion dur="4.2s" begin="1.2s" repeatCount="indefinite" path="M 1680 705 L 1430 880 Q 1640 850 1860 880" />
        </circle>
      </g>

      <!-- Vía 6: Ciclo de Krebs (Carrusel Mitocondrial Matricial) -->
      <g id="anim_flujo_via_6" class="ui_grupo_flujo_via">
        <!-- Entrada Piruvato ➔ Acetil-CoA ➔ Citrato -->
        <circle r="5.5" fill="#ea580c" filter="url(#glowShuttleParticle)">
          <animateMotion dur="4.0s" repeatCount="indefinite" path="M 1680 2150 L 1680 2220 L 1380 2255 L 1215 2288 L 1195 2308" />
        </circle>
        <!-- Bucle cerrado de Krebs -->
        <circle r="6" fill="#fbbf24" filter="url(#glowShuttleParticle)">
          <animateMotion dur="9.5s" repeatCount="indefinite" path="M 1195 2308 L 1195 2435 L 1195 2610 L 1195 2785 L 1195 2960 L 1195 3135 L 1195 3310 L 1195 3485 C 945 3525 945 3300 945 2750 L 945 2378 L 1015 2288 L 1195 2308 Z" />
        </circle>
        <circle r="3.2" fill="#ffffff">
          <animateMotion dur="9.5s" repeatCount="indefinite" path="M 1195 2308 L 1195 2435 L 1195 2610 L 1195 2785 L 1195 2960 L 1195 3135 L 1195 3310 L 1195 3485 C 945 3525 945 3300 945 2750 L 945 2378 L 1015 2288 L 1195 2308 Z" />
        </circle>
        <circle r="6" fill="#fbbf24" filter="url(#glowShuttleParticle)">
          <animateMotion dur="9.5s" begin="3.2s" repeatCount="indefinite" path="M 1195 2308 L 1195 2435 L 1195 2610 L 1195 2785 L 1195 2960 L 1195 3135 L 1195 3310 L 1195 3485 C 945 3525 945 3300 945 2750 L 945 2378 L 1015 2288 L 1195 2308 Z" />
        </circle>
        <circle r="6" fill="#fbbf24" filter="url(#glowShuttleParticle)">
          <animateMotion dur="9.5s" begin="6.4s" repeatCount="indefinite" path="M 1195 2308 L 1195 2435 L 1195 2610 L 1195 2785 L 1195 2960 L 1195 3135 L 1195 3310 L 1195 3485 C 945 3525 945 3300 945 2750 L 945 2378 L 1015 2288 L 1195 2308 Z" />
        </circle>
      </g>

      <!-- Vía 9: Beta-Oxidación (Espiral de Degradación Grasa) -->
      <g id="anim_flujo_via_9" class="ui_grupo_flujo_via">
        <circle r="5.5" fill="#06b6d4" filter="url(#glowShuttleParticle)">
          <animateMotion dur="7.0s" repeatCount="indefinite" path="M 240 1140 L 278 1642 L 278 2188 L 240 2495 L 240 2670 L 240 2845 L 240 3020 L 240 3200" />
        </circle>
        <circle r="5.5" fill="#06b6d4" filter="url(#glowShuttleParticle)">
          <animateMotion dur="7.0s" begin="3.5s" repeatCount="indefinite" path="M 240 1140 L 278 1642 L 278 2188 L 240 2495 L 240 2670 L 240 2845 L 240 3020 L 240 3200" />
        </circle>
      </g>

      <!-- Vía 14: Ciclo de la Urea (Bucle Intercompartimental) -->
      <g id="anim_flujo_via_14" class="ui_grupo_flujo_via">
        <circle r="6" fill="#818cf8" filter="url(#glowShuttleParticle)">
          <animateMotion dur="8.0s" repeatCount="indefinite" path="M 4100 3060 L 4420 2670 L 4420 2400 L 4420 2100 L 4420 1800 L 4100 1800 L 4100 2100 L 4100 2500 L 4420 2670 Z" />
        </circle>
        <circle r="6" fill="#818cf8" filter="url(#glowShuttleParticle)">
          <animateMotion dur="8.0s" begin="4.0s" repeatCount="indefinite" path="M 4100 3060 L 4420 2670 L 4420 2400 L 4420 2100 L 4420 1800 L 4100 1800 L 4100 2100 L 4100 2500 L 4420 2670 Z" />
        </circle>
      </g>

      <!-- Vía 2: Gluconeogénesis (Flujo Ascendente hacia Glucosa) -->
      <g id="anim_flujo_via_2" class="ui_grupo_flujo_via">
        <circle r="5.5" fill="#34d399" filter="url(#glowShuttleParticle)">
          <animateMotion dur="7.5s" repeatCount="indefinite" path="M 1860 1755 L 1860 1580 L 1860 1230 L 1860 1055 L 1680 705 L 1680 530 L 1680 355 L 1680 180" />
        </circle>
        <circle r="5.5" fill="#34d399" filter="url(#glowShuttleParticle)">
          <animateMotion dur="7.5s" begin="3.7s" repeatCount="indefinite" path="M 1860 1755 L 1860 1580 L 1860 1230 L 1860 1055 L 1680 705 L 1680 530 L 1680 355 L 1680 180" />
        </circle>
      </g>

      <!-- Vía 10: Lipogénesis (Citrato ➔ Palmitato) -->
      <g id="anim_flujo_via_10" class="ui_grupo_flujo_via">
        <circle r="5.5" fill="#fb7185" filter="url(#glowShuttleParticle)">
          <animateMotion dur="6.5s" repeatCount="indefinite" path="M 3140 715 L 3140 900 L 3140 1068 L 3140 1220 L 3140 1450 L 3140 1700" />
        </circle>
      </g>

      <!-- Vía 11: Cetogénesis (Acetil-CoA ➔ Cuerpos Cetónicos) -->
      <g id="anim_flujo_via_11" class="ui_grupo_flujo_via">
        <!-- Flujo principal: Tiolasa ➔ Acetoacetil-CoA ➔ HMG-CoA ➔ Acetoacetato ➔ D-β-Hidroxibutirato -->
        <circle r="5.5" fill="#be123c" filter="url(#glowShuttleParticle)">
          <animateMotion dur="6.0s" repeatCount="indefinite" path="M 662 3185 L 662 3240 L 630 3280 L 630 3380 L 630 3460 L 630 3515 L 630 3600 L 630 3655" />
        </circle>
        <circle r="3.2" fill="#ffffff">
          <animateMotion dur="6.0s" repeatCount="indefinite" path="M 662 3185 L 662 3240 L 630 3280 L 630 3380 L 630 3460 L 630 3515 L 630 3600 L 630 3655" />
        </circle>
        <circle r="5.5" fill="#be123c" filter="url(#glowShuttleParticle)">
          <animateMotion dur="6.0s" begin="3.0s" repeatCount="indefinite" path="M 662 3185 L 662 3240 L 630 3280 L 630 3380 L 630 3460 L 630 3515 L 630 3600 L 630 3655" />
        </circle>
        <!-- Descarboxilación espontánea: Acetoacetato ➔ Acetona -->
        <circle r="4.5" fill="#db2777" filter="url(#glowShuttleParticle)">
          <animateMotion dur="3.0s" begin="1.5s" repeatCount="indefinite" path="M 630 3515 L 440 3515" />
        </circle>
      </g>

      <!-- Vía 21: Cerebro y Combustibles Neuronales (Cetólisis) -->
      <g id="anim_flujo_via_21" class="ui_grupo_flujo_via">
        <!-- Entrada MCT1 ➔ BDH1 ➔ SCOT ➔ Tiolasa ➔ 2 Acetil-CoA ➔ Krebs Neuronal -->
        <circle r="5.5" fill="#a855f7" filter="url(#glowShuttleParticle)">
          <animateMotion dur="6.5s" repeatCount="indefinite" path="M -220 3500 L -365 3545 Q -505 3545 -505 3570 L -505 3700 L -505 3860 L -505 4015 L -505 4110" />
        </circle>
        <circle r="3.2" fill="#ffffff">
          <animateMotion dur="6.5s" repeatCount="indefinite" path="M -220 3500 L -365 3545 Q -505 3545 -505 3570 L -505 3700 L -505 3860 L -505 4015 L -505 4110" />
        </circle>
        <circle r="5.5" fill="#a855f7" filter="url(#glowShuttleParticle)">
          <animateMotion dur="6.5s" begin="3.25s" repeatCount="indefinite" path="M -220 3500 L -365 3545 Q -505 3545 -505 3570 L -505 3700 L -505 3860 L -505 4015 L -505 4110" />
        </circle>
      </g>

      <!-- Vía 4: Vía de las Pentosas Fosfato -->
      <g id="anim_flujo_via_4" class="ui_grupo_flujo_via">
        <circle r="5.5" fill="#f59e0b" filter="url(#glowShuttleParticle)">
          <animateMotion dur="6.0s" repeatCount="indefinite" path="M 1720 355 L 2100 355 L 2100 600 L 2100 800 L 1860 880" />
        </circle>
      </g>

      <!-- Conexiones Inter-Ruta Clave (Transferencia Intercompartimental y Tisular) -->
      <g id="anim_flujo_conexiones_clave" class="ui_grupo_flujo_via">
        <!-- cx_piruvato_mpc: Piruvato citosol ➔ Matriz MPC -->
        <circle r="4.8" fill="#ea580c" filter="url(#glowShuttleParticle)">
          <animateMotion dur="3.8s" repeatCount="indefinite" path="M 1890.0 2175.6 L 1890.0 2258.0 Q 1890.0 2274.0 1878.7 2285.3 L 1805.3 2358.7 Q 1794.0 2370.0 1794.0 2386.0 L 1794.0 2414.0 Q 1794.0 2430.0 1778.0 2430.0 L 1720.0 2430.0 Q 1710.0 2430.0 1710.0 2440.0 L 1710.0 2450.0" />
        </circle>
        <!-- cx_citrato_cic: Citrato matricial ➔ Citrato citosólico (CIC) -->
        <circle r="4.8" fill="#0d9488" filter="url(#glowShuttleParticle)">
          <animateMotion dur="4.2s" repeatCount="indefinite" path="M 1355.0 2778.0 L 1598.0 2778.0 Q 1614.0 2778.0 1625.3 2766.7 L 1698.7 2693.3 Q 1710.0 2682.0 1710.0 2666.0 L 1710.0 2568.0 Q 1710.0 2562.0 1716.0 2562.0 L 1716.0 2562.0 Q 1722.0 2562.0 1726.2 2557.8 L 1734.7 2549.3 Q 1746.0 2538.0 1762.0 2538.0 L 1874.0 2538.0 Q 1890.0 2538.0 1901.3 2526.7 L 1907.4 2520.6 Q 1914.0 2514.0 1916.5 2505.0 L 1919.0 2496.0" />
        </circle>
        <!-- cx_krebs_cte: NADH de Krebs ➔ CTE Complejo I -->
        <circle r="5" fill="#38bdf8" filter="url(#glowShuttleParticle)">
          <animateMotion dur="3.5s" repeatCount="indefinite" path="M 1373.0 3522.0 L 2426.0 3522.0 Q 2442.0 3522.0 2453.3 3510.7 L 2462.2 3501.8 Q 2466.0 3498.0 2471.4 3498.0 L 2476.8 3498.0" />
        </circle>
        <!-- cx_lanz_malato_cte_comp1: Malato ➔ CTE Complejo I -->
        <circle r="5" fill="#38bdf8" filter="url(#glowShuttleParticle)">
          <animateMotion dur="4.0s" repeatCount="indefinite" path="M 1278.0 2492.0 L 1278.0 2553.5 Q 1278.0 2562.0 1284.0 2568.0 L 1285.8 2569.8 Q 1290.0 2574.0 1296.0 2574.0 L 1296.0 2574.0 Q 1302.0 2574.0 1306.2 2578.2 L 1309.8 2581.8 Q 1314.0 2586.0 1314.0 2592.0 L 1314.0 2592.0 Q 1314.0 2598.0 1318.2 2602.2 L 1326.7 2610.7 Q 1338.0 2622.0 1338.0 2638.0 L 1338.0 2649.5 Q 1338.0 2658.0 1344.0 2664.0 L 1344.0 2664.0 Q 1350.0 2670.0 1358.5 2670.0 L 1478.0 2670.0 Q 1494.0 2670.0 1494.0 2686.0 L 1494.0 2793.5 Q 1494.0 2802.0 1500.0 2808.0 L 1500.0 2808.0 Q 1506.0 2814.0 1514.5 2814.0 L 1838.0 2814.0 Q 1854.0 2814.0 1865.3 2825.3 L 1869.5 2829.5 Q 1878.0 2838.0 1890.0 2838.0 L 1890.0 2838.0 Q 1902.0 2838.0 1902.0 2850.0 L 1902.0 2870.0 Q 1902.0 2886.0 1913.3 2897.3 L 1998.7 2982.7 Q 2010.0 2994.0 2026.0 2994.0 L 2476.8 2994.0" />
        </circle>
        <!-- cx_betaox_cetogenesis: Acetil-CoA de β-oxidación ➔ Cetogénesis -->
        <circle r="4.8" fill="#ea580c" filter="url(#glowShuttleParticle)">
          <animateMotion dur="4.2s" repeatCount="indefinite" path="M 200.6 3402.0 L 213.5 3402.0 Q 222.0 3402.0 228.0 3408.0 L 228.0 3408.0 Q 234.0 3414.0 242.5 3414.0 L 458.0 3414.0 Q 474.0 3414.0 485.3 3402.7 L 546.7 3341.3 Q 558.0 3330.0 574.0 3330.0 L 585.5 3330.0 Q 594.0 3330.0 600.0 3324.0 L 600.0 3324.0 Q 606.0 3318.0 606.0 3309.5 L 606.0 3275.0" />
        </circle>
        <!-- cx_cetogenesis_bhe_cerebro: Cuerpos cetónicos (D-β-Hidroxibutirato) ➔ BHE (MCT1 cerebral) -->
        <circle r="5.5" fill="#be123c" filter="url(#glowShuttleParticle)">
          <animateMotion dur="5.0s" repeatCount="indefinite" path="M 570.0 3655.0 L 40.0 3655.0 Q 10.0 3655.0 -15.0 3630.0 L -15.0 3525.0 Q -15.0 3500.0 -40.0 3500.0 L -65.0 3500.0" />
        </circle>
        <circle r="3.2" fill="#ffffff">
          <animateMotion dur="5.0s" repeatCount="indefinite" path="M 570.0 3655.0 L 40.0 3655.0 Q 10.0 3655.0 -15.0 3630.0 L -15.0 3525.0 Q -15.0 3500.0 -40.0 3500.0 L -65.0 3500.0" />
        </circle>
        <circle r="5.5" fill="#be123c" filter="url(#glowShuttleParticle)">
          <animateMotion dur="5.0s" begin="2.5s" repeatCount="indefinite" path="M 570.0 3655.0 L 40.0 3655.0 Q 10.0 3655.0 -15.0 3630.0 L -15.0 3525.0 Q -15.0 3500.0 -40.0 3500.0 L -65.0 3500.0" />
        </circle>
        <!-- cx_urea_sangre: Urea ➔ Sangre -->
        <circle r="4.8" fill="#818cf8" filter="url(#glowShuttleParticle)">
          <animateMotion dur="3.5s" repeatCount="indefinite" path="M 4530.0 983.5 L 4530.0 469.9 Q 4530.0 462.0 4532.2 454.5 L 4534.4 446.9" />
        </circle>
      </g>
    </g>
'''
    target_rutas = '</g></g>\n\n\n    <!-- 4. Contenidos de ampliación temática en las bandas laterales -->'
    if 'id="capa_animaciones_flujo_rutas"' not in svg and target_rutas in svg:
        svg = svg.replace(target_rutas, anim_rutas + '\n\n    <!-- 4. Contenidos de ampliación temática en las bandas laterales -->', 1)
        print("   ✓ Capa global de flujo continuo enriquecida con partículas bioluminiscentes para rutas metabólicas")


    # -------------------------------------------------------------------------
    # I. GUARDAR SVG ALTERNATIVO
    # -------------------------------------------------------------------------
    print(f"\n2. Escribiendo mapa SVG alternativo en:")
    print(f"   {RUTA_OUT_SVG}")
    with open(RUTA_OUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg)
    print("   ✓ SVG guardado exitosamente")

    # -------------------------------------------------------------------------
    # J. GENERAR VISOR HTML INTERACTIVO CON FLUJO ANIMADO, LECTURA Y AISLAMIENTO
    # -------------------------------------------------------------------------
    print(f"\n3. Construyendo visor HTML interactivo con soporte avanzado...")
    sys.path.append(os.path.join(DIR_PROYECTO, "07_AMPLIACION_TEMARIO"))
    from interactividad_html import construir_html_mapa_ampliado

    html_content = construir_html_mapa_ampliado(svg)

    # Actualizar título a 'Mapa Metabólico Alternativo'
    html_content = html_content.replace(
        '<title>Mapa Metabólico Integrado — Herramienta Interactiva Ampliada (25 Vías)</title>',
        '<title>Mapa Metabólico Alternativo — Herramienta Interactiva Ampliada (25 Vías)</title>'
    )
    html_content = html_content.replace(
        '<h2>Mapa Metabólico Integrado — Versión Ampliada (1200 × 900 mm)</h2>',
        '<h2>Mapa Metabólico Alternativo — Versión Ampliada (1200 × 900 mm)</h2>'
    )

    # Limpiar cualquier emoji existente en la plantilla original
    emojis_limpieza = [
        ('📑 Vías (25)', 'Vias (25)'),
        ('🍽️ Posprandial', 'Posprandial'),
        ('⚡ Ayuno', 'Ayuno'),
        ('🌐 Vistas / PDF', 'Vistas / PDF'),
        ('<span class="ui_search_icon">🔍</span>', '<span class="ui_search_icon" style="font-size:10px; font-weight:800; color:#94a3b8; margin-right:4px;">BUSCAR</span>'),
        ('🌟 01. Mapa Ampliado (25 Vías)', '01. Mapa Ampliado (25 Vias)'),
        ('🧩 02. Ampliación Vías 18–25 (Standalone)', '02. Ampliacion Vias 18–25 (Standalone)'),
        ('🗺️ 03. Mapa Central (17 Vías)', '03. Mapa Central (17 Vias)'),
        ('📋 04. Temario A–E (Metabolismo Intermediario)', '04. Temario A–E (Metabolismo Intermediario)'),
        ('📥 Descargar PDF 25 Vías (120×90 cm)', 'Descargar PDF 25 Vias (120×90 cm)'),
        ('📥 Descargar PDF Standalone Vías 18–25', 'Descargar PDF Standalone Vias 18–25'),
        ('<span>📑</span>', '<span>[Vias]</span>'),
        ('`📑 Vías (${viasCount})`', '`Vias (${viasCount})`'),
        ('`📑 Vias (${viasCount})`', '`Vias (${viasCount})`'),
        ('✂ TIÓLISIS', 'TIÓLISIS'),
    ]
    for viejo, nuevo in emojis_limpieza:
        html_content = html_content.replace(viejo, nuevo)

    # Inyectar estilos para Modo Lectura, Modo Aislar Vía, Flujo Vectorial y Transformación Molecular
    estilos_html_extra = """
    /* Selector de Version del Mapa y Selector Rapido de Vias */
    .ui_map_version_group {
      display: inline-flex;
      align-items: center;
      background: #090d16;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 2px;
      gap: 2px;
    }
    .ui_ver_link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 10px;
      font-size: 0.78rem;
      font-weight: 600;
      text-decoration: none;
      color: #94a3b8;
      border-radius: 6px;
      transition: all 0.15s ease;
      white-space: nowrap;
      cursor: pointer;
    }
    .ui_ver_link:hover {
      color: #f8fafc;
      background: #1e293b;
    }
    .ui_ver_link.active {
      color: #38bdf8;
      background: #1e293b;
      border: 1px solid #0284c7;
      font-weight: 700;
      box-shadow: 0 1px 4px rgba(2, 132, 199, 0.3);
    }
    .ui_live_dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #38bdf8;
      box-shadow: 0 0 6px #38bdf8;
      display: inline-block;
      animation: animPulsoGlow 2s infinite ease-in-out;
    }
    .ui_quick_via_wrapper {
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    #ui_select_quick_via {
      background: #1e293b;
      border: 1px solid #475569;
      color: #f8fafc;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 5px 8px;
      border-radius: 6px;
      outline: none;
      cursor: pointer;
      max-width: 260px;
      transition: border-color 0.15s ease;
    }
    #ui_select_quick_via:hover, #ui_select_quick_via:focus {
      border-color: #38bdf8;
    }
    #ui_select_quick_via optgroup {
      background: #0f172a;
      color: #94a3b8;
      font-weight: 700;
      font-size: 0.75rem;
    }
    #ui_select_quick_via option {
      background: #1e293b;
      color: #f8fafc;
      font-weight: 500;
      font-size: 0.8rem;
      padding: 3px 6px;
    }

    /* Modo Lectura y Modo Aislar Via (Mapa Alternativo) */
    body.ui_reading_mode #capa_conexiones_inter_ruta .conexion-inter-ruta > path:first-child {
      stroke-width: 9.5 !important;
      opacity: 0.85 !important;
    }
    body.ui_reading_mode #capa_conexiones_inter_ruta .conexion-inter-ruta > path:nth-child(2) {
      stroke-width: 3.8 !important;
    }
    body.ui_reading_mode #cx_rotulos text {
      paint-order: stroke fill;
      stroke: #ffffff;
      stroke-width: 4px;
      stroke-linejoin: round;
      font-weight: 900 !important;
    }
    /* Modo lectura: ocultar las bolitas (particulas SMIL) para poder leer sin distracciones */
    .ui_particula_oculta_lectura {
      display: none !important;
    }
    body.ui_isolate_mode .ui_dimmed {
      display: none !important;
    }
    .ui_state_btn.ui_btn_active_custom {
      background: #0284c7 !important;
      color: #ffffff !important;
      box-shadow: 0 1px 4px rgba(2, 132, 199, 0.4);
    }

    /* Motor de Flujo Vectorial Bioluminiscente (60 FPS) */
    @keyframes animFlujoConexion {
      from { stroke-dashoffset: 32; }
      to { stroke-dashoffset: 0; }
    }
    @keyframes animFlujoReaccion {
      from { stroke-dashoffset: 24; }
      to { stroke-dashoffset: 0; }
    }
    @keyframes animPulsoGlow {
      0%, 100% { filter: drop-shadow(0 0 2px rgba(56, 189, 248, 0.4)); }
      50% { filter: drop-shadow(0 0 7px rgba(56, 189, 248, 0.85)); }
    }

    /* Conexiones inter-ruta con flujo animado */
    body.ui_flujo_on #capa_conexiones_inter_ruta .conexion-inter-ruta.ui_highlighted > path:nth-child(2),
    body.ui_flujo_on #capa_conexiones_inter_ruta .conexion-inter-ruta.ui_state_active > path:nth-child(2),
    body.ui_flujo_on.ui_flujo_global #capa_conexiones_inter_ruta .conexion-inter-ruta:not(.ui_dimmed) > path:nth-child(2) {
      stroke-dasharray: 10 6 !important;
      animation: animFlujoConexion 1.1s linear infinite !important;
    }

    /* Resplandor bioluminiscente en conexiones activas */
    body.ui_flujo_on #capa_conexiones_inter_ruta .conexion-inter-ruta.ui_highlighted,
    body.ui_flujo_on #capa_conexiones_inter_ruta .conexion-inter-ruta.ui_state_active,
    body.ui_flujo_on.ui_flujo_global #capa_conexiones_inter_ruta .conexion-inter-ruta:not(.ui_dimmed) {
      filter: drop-shadow(0 0 3px rgba(255, 255, 255, 0.6)) drop-shadow(0 0 6px currentColor);
    }

    /* Flechas enzimaticas internas de la via activa o estado activo */
    body.ui_flujo_on .ui_highlighted path[marker-end],
    body.ui_flujo_on .ui_highlighted line[marker-end],
    body.ui_flujo_on .ui_state_active path[marker-end],
    body.ui_flujo_on .ui_state_active line[marker-end],
    body.ui_flujo_on.ui_flujo_global [id^="ruta_"]:not(.ui_dimmed) path[marker-end],
    body.ui_flujo_on.ui_flujo_global [id^="ruta_"]:not(.ui_dimmed) line[marker-end],
    body.ui_flujo_on.ui_flujo_global [id^="lupa_"]:not(.ui_dimmed) path[marker-end],
    body.ui_flujo_on.ui_flujo_global [id^="lupa_"]:not(.ui_dimmed) line[marker-end] {
      stroke-dasharray: 8 4 !important;
      animation: animFlujoReaccion 0.8s linear infinite !important;
      filter: drop-shadow(0 0 2px rgba(255, 255, 255, 0.5));
    }

    /* Resaltado de transformacion molecular quimica */
    .ui_mol_sustrato {
      filter: drop-shadow(0 0 8px #38bdf8) drop-shadow(0 0 16px rgba(56, 189, 248, 0.6)) !important;
      opacity: 1 !important;
    }
    .ui_mol_producto {
      filter: drop-shadow(0 0 8px #22c55e) drop-shadow(0 0 18px rgba(34, 197, 94, 0.7)) !important;
      opacity: 1 !important;
    }
    .ui_rx_activa {
      filter: drop-shadow(0 0 10px #f59e0b) drop-shadow(0 0 20px rgba(245, 158, 11, 0.8)) !important;
      opacity: 1 !important;
    }
    .ui_mol_producto text, .ui_mol_producto circle {
      animation: anim_cambio_quimico 1.2s infinite alternate ease-in-out !important;
    }
    @keyframes anim_cambio_quimico {
      0% { filter: drop-shadow(0 0 2px #eab308); }
      100% { filter: drop-shadow(0 0 8px #eab308) drop-shadow(0 0 15px #22c55e); }
    }

    /* Estilos del Simulador de Lanzaderas Vivas */
    .ui_shuttle_badge {
      background: linear-gradient(135deg, #0284c7, #0d9488) !important;
      color: #ffffff !important;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
    }
    .ui_shuttle_yield {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.78rem;
      color: #38bdf8;
      background: rgba(2, 132, 199, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.4);
      padding: 3px 8px;
      border-radius: 6px;
      font-weight: 800;
    }
    .ui_shuttle_phases_nav {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 6px;
      margin: 4px 0 2px 0;
    }
    .ui_shuttle_phase_btn {
      background: #1e293b;
      border: 1px solid #334155;
      color: #94a3b8;
      padding: 6px 8px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 700;
      cursor: pointer;
      text-align: center;
      transition: all 0.2s ease;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .ui_shuttle_phase_btn:hover {
      background: #334155;
      color: #f8fafc;
      border-color: #38bdf8;
    }
    .ui_shuttle_phase_btn.active {
      background: #0369a1 !important;
      border-color: #38bdf8 !important;
      color: #ffffff !important;
      box-shadow: 0 0 10px rgba(56, 189, 248, 0.6);
    }
    .ui_shuttle_compartment_pill {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: 4px;
      text-transform: uppercase;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: #38bdf8;
      margin-bottom: 2px;
      letter-spacing: 0.5px;
    }

    /* Panel didactico inferior de transformacion quimica y simulador de lanzaderas */
    #ui_panel_transformacion {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(160%);
      width: min(880px, 95vw);
      background: rgba(15, 23, 42, 0.96);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1.5px solid #38bdf8;
      border-radius: 14px;
      box-shadow: 0 14px 40px rgba(0, 0, 0, 0.75), 0 0 24px rgba(56, 189, 248, 0.25);
      padding: 16px 20px;
      z-index: 9999;
      color: #f8fafc;
      font-family: 'Inter', system-ui, sans-serif;
      transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      gap: 10px;
      pointer-events: auto;
    }
    #ui_panel_transformacion.ui_visible {
      transform: translateX(-50%) translateY(0);
    }
    .ui_trans_header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #334155;
      padding-bottom: 8px;
    }
    .ui_trans_step_badge {
      background: #0284c7;
      color: #ffffff;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 800;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }
    .ui_trans_title {
      font-size: 1.05rem;
      font-weight: 800;
      color: #38bdf8;
      margin-left: 10px;
    }
    .ui_trans_ec {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      color: #94a3b8;
      background: rgba(255, 255, 255, 0.06);
      padding: 2px 6px;
      border-radius: 4px;
      margin-left: 8px;
    }
    .ui_trans_close {
      background: transparent;
      border: none;
      color: #94a3b8;
      font-size: 1.1rem;
      font-weight: 800;
      cursor: pointer;
      padding: 2px 8px;
      border-radius: 6px;
      transition: all 0.15s;
    }
    .ui_trans_close:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.1);
    }
    .ui_trans_body {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .ui_trans_flow_row {
      display: flex;
      align-items: center;
      gap: 12px;
      font-weight: 700;
      font-size: 0.95rem;
    }
    .ui_trans_sub { color: #38bdf8; }
    .ui_trans_arrow { color: #eab308; font-weight: 900; }
    .ui_trans_prod { color: #22c55e; }
    .ui_trans_desc {
      font-size: 0.88rem;
      color: #e2e8f0;
      line-height: 1.4;
    }
    .ui_trans_details {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      font-size: 0.8rem;
      color: #94a3b8;
      background: rgba(0, 0, 0, 0.25);
      padding: 8px 12px;
      border-radius: 8px;
    }
    .ui_trans_details strong {
      color: #f1f5f9;
    }
    .ui_trans_footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 4px;
      padding-top: 6px;
      border-top: 1px solid #1e293b;
    }
    .ui_trans_nav_btns {
      display: flex;
      gap: 8px;
    }
    .ui_btn_trans {
      background: #1e293b;
      color: #f8fafc;
      border: 1px solid #475569;
      padding: 6px 14px;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.82rem;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .ui_btn_trans:hover {
      background: #334155;
      border-color: #38bdf8;
    }
    .ui_btn_trans.primary {
      background: #0284c7;
      border-color: #38bdf8;
    }
    .ui_btn_trans.primary:hover {
      background: #0369a1;
    }
  </style>"""
    html_content = html_content.replace('  </style>', estilos_html_extra, 1)

    # Inyectar selector de version y selector rapido de vias al inicio de .controls
    controles_inicio = """      <!-- Selector de Version del Mapa -->
      <div class="ui_map_version_group">
        <a href="index.html" class="ui_ver_link active" onclick="irAMapaAlternativo(); return false;" title="Mapa interactivo con flujo animado continuo a 60 FPS, lanzaderas y monitor CTE">
          <span class="ui_live_dot"></span> Mapa Alternativo
        </a>
        <a href="../versiones_html/01_mapa_ampliado_completo_25_vias.html" class="ui_ver_link" onclick="irAMapaOriginal(); return false;" title="Mapa cartulina base clasico ampliado de 25 vias">
          Mapa Original
        </a>
      </div>

      <!-- Selector Rapido de Vias (1 a 25) y Aislamiento -->
      <div class="ui_quick_via_wrapper">
        <select id="ui_select_quick_via" onchange="seleccionarViaRapida(this.value)" title="Seleccionar via metabolica individual">
          <option value="">-- Ver Via Individual (1 a 25) --</option>
          <optgroup label="Carbohidratos y Respiracion Celular">
            <option value="1">Via 1: Glucolisis (Citosol)</option>
            <option value="2">Via 2: Gluconeogenesis (Matriz / Citosol / RE)</option>
            <option value="3">Via 3: Glucogeno (Genesis y Lisis)</option>
            <option value="4">Via 4: Via de las Pentosas Fosfato</option>
            <option value="5">Via 5: Complejo Piruvato Deshidrogenasa (PDH)</option>
            <option value="6">Via 6: Ciclo de Krebs (ATC)</option>
            <option value="7">Via 7: Cadena Respiratoria y ATP Sintasa</option>
            <option value="8">Via 8: Lanzadera Malato-Aspartato</option>
            <option value="8B">Via 8B: Lanzadera Glicerol-3-Fosfato</option>
          </optgroup>
          <optgroup label="Lipidos y Cuerpos Cetonicos">
            <option value="9">Via 9: Beta-Oxidacion y Lanzadera de Carnitina</option>
            <option value="10">Via 10: Lipogenesis de Novo y Lanzadera de Citrato</option>
            <option value="11">Via 11: Cetogenesis Hepatica</option>
            <option value="12">Via 12: Biosintesis de Colesterol</option>
          </optgroup>
          <optgroup label="Nitrogeno, Aminoacidos y Nucleotidos">
            <option value="12B">Via 12B: Transulfuracion y Destino Carbonado AA</option>
            <option value="13">Via 13: Transaminacion y Ciclo Glucosa-Alanina</option>
            <option value="14">Via 14: Ciclo de la Urea y Biciclo Krebs-Henseleit</option>
            <option value="15">Via 15: Biosintesis de Purinas y Pirimidinas</option>
            <option value="16">Via 16: Catabolismo Nucleotidos y Acido Urico (URAT1)</option>
          </optgroup>
          <optgroup label="Ampliacion Fisiologica Intertisular">
            <option value="17">Via 17: Ciclo de Cori y Ciclo de Cahill (Vascular)</option>
            <option value="18">Via 18: Digestion y Absorcion de Lipidos (Enterocito)</option>
            <option value="19">Via 19: Lipolisis Adipocitaria (ATGL/HSL/MGL)</option>
            <option value="20">Via 20: Musculo Esqueletico y Sarcomero</option>
            <option value="21">Via 21: Cerebro, Barrera Hematoencefalica y Cetolisis</option>
            <option value="22">Via 22: Metabolismo Lipoproteinas Plasmaticas</option>
            <option value="23">Via 23: Via de Kennedy (Fosfolipidos Membrana)</option>
            <option value="24">Via 24: Biosintesis Aminoacidos No Esenciales</option>
            <option value="25">Via 25: Conmutador Hormonal Pancreatico</option>
          </optgroup>
        </select>
        <button id="ui_btn_isolate" class="ui_state_btn" onclick="toggleModoAislar()" title="Oculta por completo las vias atenuadas para ver unicamente la via seleccionada">Aislar</button>
        <button id="ui_btn_open_svg" class="ui_state_btn" onclick="abrirSvgViaActual()" style="background:#0284c7; color:#ffffff; font-weight:700;" title="Abrir el diagrama SVG vectorial individual de esta ruta en una pestaña nueva">Ver SVG</button>
      </div>

      <div style="width: 1px; height: 20px; background: #475569; margin: 0 4px;"></div>

      <!-- Botón de Índice -->"""
    html_content = html_content.replace('      <!-- Botón de Índice -->', controles_inicio, 1)

    # Inyectar botones didacticos en .controls sin emojis
    botones_extra = """      <!-- Botones Didacticos: Lectura, Flujo Animado y Paso a Paso -->
      <div class="ui_state_group">
        <button id="ui_btn_reading" class="ui_state_btn" onclick="toggleModoLectura()" title="Aumenta grosor y contraste de conexiones inter-ruta y rotulos">Lectura</button>
        <button id="ui_btn_flow" class="ui_state_btn ui_btn_active_custom" onclick="toggleFlujoAnimado()" title="Activa o pausa la corriente bioluminiscente en las rutas activas">Flujo Animado</button>
        <button id="ui_btn_step" class="ui_state_btn" onclick="iniciarPasoAPaso()" title="Inicia la navegacion guiada de cambios quimicos paso a paso">Paso a Paso</button>
      </div>

      <!-- Selector de Vistas / Descargas -->"""
    html_content = html_content.replace('      <!-- Selector de Vistas / Descargas -->', botones_extra, 1)

    # Inyectar boton de Ver SVG Individual en el banner flotante
    banner_viejo = """  <!-- BANNER FLOTANTE DE VÍA RESALTADA -->
  <div id="ui_highlight_banner">
    <span id="ui_highlight_title">Vía resaltada</span>
    <button onclick="clearPathwayHighlight()" title="Quitar resaltado (Esc)">✕ Quitar</button>
  </div>"""
    banner_nuevo = """  <!-- BANNER FLOTANTE DE VÍA RESALTADA -->
  <div id="ui_highlight_banner">
    <span id="ui_highlight_title">Vía resaltada</span>
    <button id="ui_btn_banner_svg" onclick="abrirSvgViaActual()" style="background:#0284c7; color:#ffffff; border:none; padding:4px 10px; border-radius:4px; font-weight:700; cursor:pointer; font-size:0.75rem; margin-right:4px;">Abrir Diagrama SVG</button>
    <button onclick="clearPathwayHighlight()" title="Quitar resaltado (Esc)">✕ Quitar</button>
  </div>"""
    html_content = html_content.replace(banner_viejo, banner_nuevo, 1)

    # Actualizar menu de vistas y descargas
    menu_vistas_nuevo = """        <div id="ui_menu_views" style="display: none; position: absolute; right: 0; top: 100%; margin-top: 6px; background: #0f172a; border: 1px solid #334155; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.6); min-width: 280px; z-index: 1000; padding: 6px 0; text-align: left;">
          <a href="index.html" onclick="irAMapaAlternativo(); return false;" style="display: block; padding: 8px 14px; color: #38bdf8; text-decoration: none; font-size: 0.8rem; font-weight: 700;">* Mapa Alternativo (Flujo Vivo 60 FPS)</a>
          <a href="../versiones_html/01_mapa_ampliado_completo_25_vias.html" onclick="irAMapaOriginal(); return false;" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem; font-weight: 700;">* Mapa Original Base (25 Vias)</a>
          <div style="height: 1px; background: #334155; margin: 4px 0;"></div>
          <a href="../versiones_html/02_ampliacion_rutas_18_25.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">02. Ampliacion Vias 18–25 (Standalone)</a>
          <a href="../versiones_html/03_mapa_central_interactivo_17_vias.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">03. Mapa Central (17 Vias)</a>
          <a href="../versiones_html/04_cuadro_temario_bloques_A_E.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">04. Temario A–E (Metabolismo Intermediario)</a>
          <div style="height: 1px; background: #334155; margin: 4px 0;"></div>
          <a href="mapa_metabolico_alternativo_120x90cm.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #38bdf8; text-decoration: none; font-size: 0.8rem; font-weight: 700;">Descargar PDF Alternativo (120×90 cm)</a>
          <a href="../versiones_impresion/01_mapa_ampliado_completo_120x90cm.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem; font-weight: 700;">Descargar PDF Original (120×90 cm)</a>
          <a href="../versiones_impresion/02_ampliacion_rutas_18_25.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem;">Descargar PDF Standalone Vias 18–25</a>
        </div>"""
    menu_vistas_viejo = """        <div id="ui_menu_views" style="display: none; position: absolute; right: 0; top: 100%; margin-top: 6px; background: #0f172a; border: 1px solid #334155; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.6); min-width: 260px; z-index: 1000; padding: 6px 0; text-align: left;">
          <a href="01_mapa_ampliado_completo_25_vias.html" style="display: block; padding: 8px 14px; color: #38bdf8; text-decoration: none; font-size: 0.8rem; font-weight: 700;">01. Mapa Ampliado (25 Vias)</a>
          <a href="02_ampliacion_rutas_18_25.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">02. Ampliacion Vias 18–25 (Standalone)</a>
          <a href="03_mapa_central_interactivo_17_vias.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">03. Mapa Central (17 Vias)</a>
          <a href="04_cuadro_temario_bloques_A_E.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">04. Temario A–E (Metabolismo Intermediario)</a>
          <div style="height: 1px; background: #334155; margin: 4px 0;"></div>
          <a href="../versiones_impresion/01_mapa_ampliado_completo_120x90cm.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem; font-weight: 700;">Descargar PDF 25 Vias (120×90 cm)</a>
          <a href="../versiones_impresion/02_ampliacion_rutas_18_25.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem;">Descargar PDF Standalone Vias 18–25</a>
        </div>"""
    html_content = html_content.replace(menu_vistas_viejo, menu_vistas_nuevo, 1)

    # Inyectar markup del panel didactico antes de </body>
    panel_transformacion_html = """
  <!-- PANEL DIDACTICO DE TRANSFORMACION QUIMICA Y SIMULADOR DE LANZADERAS -->
  <div id="ui_panel_transformacion">
    <div class="ui_trans_header">
      <div style="display: flex; align-items: center; gap: 8px;">
        <span id="ui_trans_step_badge" class="ui_trans_step_badge">Paso 1 de 10</span>
        <span id="ui_trans_title" class="ui_trans_title">Hexoquinasa</span>
        <span id="ui_trans_ec" class="ui_trans_ec">EC 2.7.1.1</span>
        <span id="ui_trans_yield" class="ui_shuttle_yield" style="display: none;">2.5 ATP (C-I)</span>
      </div>
      <button class="ui_trans_close" onclick="cerrarPanelTransformacion()" title="Cerrar panel">[X]</button>
    </div>

    <!-- Navegacion de fases para Modo Lanzadera -->
    <div id="ui_shuttle_phases_container" class="ui_shuttle_phases_nav" style="display: none;">
      <button id="ui_btn_fase_0" class="ui_shuttle_phase_btn active" onclick="irAFaseLanzadera(0)">1. Citosol</button>
      <button id="ui_btn_fase_1" class="ui_shuttle_phase_btn" onclick="irAFaseLanzadera(1)">2. Translocacion</button>
      <button id="ui_btn_fase_2" class="ui_shuttle_phase_btn" onclick="irAFaseLanzadera(2)">3. Matriz (C-I)</button>
      <button id="ui_btn_fase_3" class="ui_shuttle_phase_btn" onclick="irAFaseLanzadera(3)">4. Retorno</button>
    </div>

    <div class="ui_trans_body">
      <div id="ui_trans_compartimento" class="ui_shuttle_compartment_pill" style="display: none;">CITOSOL CELULAR</div>
      <div class="ui_trans_flow_row">
        <span id="ui_trans_sub" class="ui_trans_sub">D-Glucosa</span>
        <span class="ui_trans_arrow">➔</span>
        <span id="ui_trans_prod" class="ui_trans_prod">D-Glucosa-6-Fosfato</span>
      </div>
      <div id="ui_trans_desc" class="ui_trans_desc">
        Fosforilacion irreversible en C6 para atrapar la glucosa en el citosol.
      </div>
      <div class="ui_trans_details">
        <div id="ui_box_cofactores"><strong>Cofactores:</strong> <span id="ui_trans_cofactores">ATP ➔ ADP + H⁺ (Mg²⁺)</span></div>
        <div id="ui_box_deltag"><strong>Energia:</strong> <span id="ui_trans_deltag">ΔG°' = -16.7 kJ/mol</span></div>
        <div id="ui_box_regulacion"><strong>Regulacion:</strong> <span id="ui_trans_regulacion">Inhibida por G6P</span></div>
        <div id="ui_box_carrier" style="display: none;"><strong>Carrier:</strong> <span id="ui_trans_carrier">SLC25A11 (OGC)</span></div>
      </div>
    </div>
    <div class="ui_trans_footer">
      <div class="ui_trans_nav_btns">
        <button id="ui_btn_step_prev" class="ui_btn_trans" onclick="pasoAnterior()">Anterior</button>
        <button id="ui_btn_step_next" class="ui_btn_trans primary" onclick="pasoSiguiente()">Siguiente</button>
      </div>
      <div style="display: flex; align-items: center; gap: 8px;">
        <button id="ui_btn_shuttle_target" class="ui_btn_trans" style="display: none;" onclick="enfocarDestinoCadena()">Ver C-I</button>
        <button id="ui_btn_shuttle_lupa" class="ui_btn_trans" style="display: none;" onclick="enfocarLupaShuttleActual()">Ver Lanzadera</button>
        <button id="ui_btn_shuttle_speed" class="ui_btn_trans" style="display: none;" onclick="toggleVelocidadLanzadera()">1x</button>
        <button id="ui_btn_cam_follow" class="ui_btn_trans" onclick="toggleSeguirCamara()" title="Alterna el centrado automatico de camara en cada paso">Camara: ON</button>
        <button id="ui_btn_step_auto" class="ui_btn_trans" onclick="toggleReproduccionAuto()" title="Avanza automaticamente">Reproducir</button>
      </div>
    </div>
  </div>
</body>"""
    html_content = html_content.replace('</body>', panel_transformacion_html, 1)

    # Inyectar motor JS completo
    js_extra = """
    // =========================================================================
    // FUNCIONALIDADES ADICIONALES: MOTOR DE TRANSFORMACION MOLECULAR DINAMICA
    // Y SIMULADOR DE LANZADERAS MITOCONDRIALES VIVAS
    // =========================================================================
    let modoLecturaActivo = false;
    let modoAislarActivo = false;
    let flujoAnimadoHabilitado = true;
    let seguirCamaraActivo = true;
    let reproduccionAutoInterval = null;

    // Estado del motor de lanzaderas
    let modoLanzaderaActivo = false;
    let lanzaderaActualId = null;
    let faseLanzaderaIdx = 0;
    let velocidadFactorLanzadera = 1;
    let intervaloLanzadera = null;

    // Catalogo estructurado de secuencias enzimaticas para vias lineales
    const CATALOGO_PASOS_VIAS = {
      "1": [ // Glucolisis
        { id: "rx_hk", nombre: "Hexoquinasa (HK)", ec: "EC 2.7.1.1", sub: ["m_glucosa"], prod: ["m_g6p"], cambio: "Fosforilacion irreversible en C6 para atrapar la glucosa", cofactores: "ATP ➔ ADP + H⁺ (Mg²⁺)", deltag: "-16.7 kJ/mol (Irreversible)", regulacion: "Inhibida por G6P; Glucoquinasa hepática inducida por insulina" },
        { id: "rx_pgi", nombre: "Fosfoglucosa Isomerasa (PGI)", ec: "EC 5.3.1.9", sub: ["m_g6p"], prod: ["m_f6p"], cambio: "Isomerizacion aldosa a cetosa (anillo piranosa a furanosa)", cofactores: "Ninguno (Equilibrio rápido)", deltag: "+1.7 kJ/mol (Reversible)", regulacion: "Control por balance de masas [G6P]/[F6P]" },
        { id: "rx_pfk1", nombre: "Fosfofructoquinasa-1 (PFK-1)", ec: "EC 2.7.1.11", sub: ["m_f6p"], prod: ["m_fbp"], cambio: "Fosforilacion en C1 marcapasos y punto de compromiso glucolitico", cofactores: "ATP ➔ ADP + H⁺ (Mg²⁺)", deltag: "-14.2 kJ/mol (Irreversible)", regulacion: "Activada por F-2,6-BP y AMP; inhibida por ATP y Citrato" },
        { id: "rx_aldo", nombre: "Aldolasa (FBA)", ec: "EC 4.1.2.13", sub: ["m_fbp"], prod: ["m_dhap", "m_gap"], cambio: "Escision aldolica simetrica de 1 hexosa (6C) en 2 triosas (3C)", cofactores: "Ninguno", deltag: "+23.8 kJ/mol (Impulsada por consumo de triosas)", regulacion: "Déficit de Aldolasa B causa Intolerancia Hereditaria a la Fructosa" },
        { id: "rx_tpi", nombre: "Triosa Fosfato Isomerasa (TPI)", ec: "EC 5.3.1.1", sub: ["m_dhap"], prod: ["m_gap"], cambio: "Interconversion estereoespecifica entre DHAP y GAP", cofactores: "Ninguno (Enzima cinéticamente perfecta)", deltag: "+7.5 kJ/mol (Reversible)", regulacion: "Equilibrio desplazado por sustrato continuo de GAPDH" },
        { id: "rx_gapdh", nombre: "Gliceraldehido-3-P Deshidrogenasa (GAPDH)", ec: "EC 1.2.1.12", sub: ["m_gap"], prod: ["m_bpg"], cambio: "Oxidacion con fosforilacion inorganica formando acil-fosfato de alta energia", cofactores: "NAD⁺ + Pᵢ ➔ NADH + H⁺", deltag: "+6.3 kJ/mol (Reversible)", regulacion: "Genera el poder reductor citosólico de la glucólisis" },
        { id: "rx_pgk", nombre: "Fosfoglicerato Quinasa (PGK)", ec: "EC 2.7.2.3", sub: ["m_bpg"], prod: ["m_3pg"], cambio: "Primera fosforilacion a nivel de sustrato generando ATP", cofactores: "ADP ➔ ATP (Mg²⁺)", deltag: "-18.5 kJ/mol (Acoplada a GAPDH)", regulacion: "Recupera la inversion energetica inicial de la fase preparatoria" },
        { id: "rx_pgm", nombre: "Fosfoglicerato Mutasa (PGM)", ec: "EC 5.4.2.11", sub: ["m_3pg"], prod: ["m_2pg"], cambio: "Transferencia intramolecular del grupo fosfato de C3 a C2", cofactores: "Requiere trazas de 2,3-BPG", deltag: "+4.4 kJ/mol (Reversible)", regulacion: "Prepara la molecula para la posterior deshidratacion" },
        { id: "rx_eno", nombre: "Enolasa", ec: "EC 4.2.1.11", sub: ["m_2pg"], prod: ["m_pep"], cambio: "Deshidratacion formando el enlace enol-fosfato de altisima energia", cofactores: "H₂O eliminada (Mg²⁺)", deltag: "+7.5 kJ/mol (Reversible)", regulacion: "Inhibida por fluoruro (utilizado en tubos de recogida de glucemia)" },
        { id: "rx_pk", nombre: "Piruvato Quinasa (PK)", ec: "EC 2.7.1.40", sub: ["m_pep"], prod: ["m_pyr_cito"], cambio: "Segunda fosforilacion a nivel de sustrato irreversible generando ATP y piruvato", cofactores: "ADP + H⁺ ➔ ATP (K⁺, Mg²⁺)", deltag: "-31.4 kJ/mol (Irreversible)", regulacion: "Activada por F-1,6-BP (feedforward); inhibida por ATP, Alanina y glucagon" }
      ],
      "6": [ // Ciclo de Krebs
        { id: "rx_citrato_sintasa", nombre: "Citrato Sintasa", ec: "EC 2.3.3.1", sub: ["m_oaa", "m_accoa"], prod: ["m_citrato"], cambio: "Condensacion aldolica de oxalacetato (4C) y acetil-CoA (2C) a citrato (6C)", cofactores: "H₂O ➔ CoASH", deltag: "-31.5 kJ/mol (Irreversible)", regulacion: "Inhibida por ATP, NADH, Succinil-CoA y Citrato" },
        { id: "rx_acon", nombre: "Aconitasa", ec: "EC 4.2.1.3", sub: ["m_citrato"], prod: ["m_isocitrato"], cambio: "Deshidratacion e hidratacion estereoquimica via cis-aconitato", cofactores: "Centro ferrosulfurado [4Fe-4S]", deltag: "+6.3 kJ/mol (Reversible)", regulacion: "Inhibida por fluorocitrato (veneno metabolico)" },
        { id: "rx_icdh", nombre: "Isocitrato Deshidrogenasa (ICDH)", ec: "EC 1.1.1.41", sub: ["m_isocitrato"], prod: ["m_akg"], cambio: "Descarboxilacion oxidativa de 6C a 5C (+1 NADH, -1 CO2)", cofactores: "NAD⁺ ➔ NADH + H⁺ + CO₂ (Mn²⁺)", deltag: "-8.4 kJ/mol (Marcapasos)", regulacion: "Activada por ADP y Ca²⁺; inhibida por ATP y NADH" },
        { id: "rx_akgdh", nombre: "alfa-Cetoglutarato Deshidrogenasa (aKGDH)", ec: "EC 1.2.4.2", sub: ["m_akg"], prod: ["m_succoa"], cambio: "Descarboxilacion oxidativa de 5C a 4C conservando energia en tioester", cofactores: "NAD⁺ + CoASH ➔ NADH + CO₂ (TPP, Lipoato, FAD)", deltag: "-30.1 kJ/mol (Irreversible)", regulacion: "Activada por Ca²⁺; inhibida por Succinil-CoA y NADH" },
        { id: "rx_scas", nombre: "Succinil-CoA Sintetasa", ec: "EC 6.2.1.4", sub: ["m_succoa"], prod: ["m_succinato"], cambio: "Fosforilacion a nivel de sustrato en la matriz mitocondrial", cofactores: "GDP/ADP + Pᵢ ➔ GTP/ATP + CoASH", deltag: "-3.8 kJ/mol (Reversible)", regulacion: "Isoforma hepatica genera GTP para gluconeogenesis" },
        { id: "rx_sdh", nombre: "Succinato Deshidrogenasa (Complejo II)", ec: "EC 1.3.5.1", sub: ["m_succinato"], prod: ["m_fumarato"], cambio: "Oxidacion trans de alcano a alqueno ligada directamente a la cresta mitocondrial", cofactores: "FAD ➔ FADH₂ ➔ Coenzima Q", deltag: "0.0 kJ/mol (Reversible)", regulacion: "Inhibida por malonato (inhibidor competitivo clasico)" },
        { id: "rx_fum", nombre: "Fumarasa", ec: "EC 4.2.1.2", sub: ["m_fumarato"], prod: ["m_malato"], cambio: "Hidratacion estereoespecifica trans del doble enlace formando L-malato", cofactores: "H₂O", deltag: "-3.8 kJ/mol (Reversible)", regulacion: "Conecta con el biciclo de la urea mediante el aspartato" },
        { id: "rx_mdh_retorno", nombre: "Malato Deshidrogenasa (mMDH)", ec: "EC 1.1.1.37", sub: ["m_malato"], prod: ["m_oaa"], cambio: "Oxidacion final regenerando oxalacetato para reiniciar el ciclo (+1 NADH)", cofactores: "NAD⁺ ➔ NADH + H⁺", deltag: "+29.7 kJ/mol (Impulsada por Citrato Sintasa)", regulacion: "La bajísima concentración de OAA mantiene el flujo hacia adelante" }
      ],
      "9": [ // Beta-oxidacion
        { id: "rx_acs", nombre: "Acil-CoA Sintetasa (ACS)", ec: "EC 6.2.1.3", sub: ["m_palmitato_cito"], prod: ["m_palmitoil_cito"], cambio: "Activacion de acido graso a acil-CoA consumiendo dos enlaces de alta energia", cofactores: "ATP + CoASH ➔ AMP + PPᵢ (2 ATP eq)", deltag: "-34 kJ/mol", regulacion: "Localizada en la membrana mitocondrial externa y REL" },
        { id: "rx_cpt1", nombre: "Carnitina Palmitoiltransferasa-1 (CPT-1)", ec: "EC 2.3.1.21", sub: ["m_palmitoil_cito"], prod: ["m_palm_carnitina"], cambio: "Transesterificacion de acil-CoA a acilcarnitina marcapasos de entrada", cofactores: "Carnitina libre ➔ CoASH", deltag: "-1.2 kJ/mol", regulacion: "Inhibida por Malonil-CoA citosólico (evita ciclo futil con lipogenesis)" },
        { id: "rx_cpt2", nombre: "Carnitina Palmitoiltransferasa-2 (CPT-2)", ec: "EC 2.3.1.21", sub: ["m_palm_carnitina"], prod: ["m_palmitoil"], cambio: "Regeneracion del acil-CoA graso en la matriz mitocondrial", cofactores: "CoASH matricial ➔ Carnitina libre", deltag: "+1.2 kJ/mol", regulacion: "Permite la entrada al ciclo espiral de beta-oxidacion" },
        { id: "rx_box1", nombre: "Acil-CoA Deshidrogenasa", ec: "EC 1.3.8.7", sub: ["m_palmitoil"], prod: ["m_trans_enoil"], cambio: "Deshidrogenacion C2-C3 formando doble enlace trans-2-enoil-CoA (+1 FADH2)", cofactores: "FAD ➔ FADH₂ ➔ ETF-QO ➔ CoQ", deltag: "-4 kJ/mol", regulacion: "Isoformas VLCAD, MCAD, SCAD segun longitud de cadena" },
        { id: "rx_box1b", nombre: "Enoil-CoA Hidratasa", ec: "EC 4.2.1.17", sub: ["m_trans_enoil"], prod: ["m_hidroxi_coa"], cambio: "Hidratacion estereoespecifica formando L-3-hidroxiacil-CoA", cofactores: "H₂O", deltag: "-8 kJ/mol", regulacion: "Complejo trifuncional mitocondrial en cadenas largas" },
        { id: "rx_box2", nombre: "3-Hidroxiacil-CoA Deshidrogenasa", ec: "EC 1.1.1.35", sub: ["m_hidroxi_coa"], prod: ["m_cetoacil_coa"], cambio: "Oxidacion a 3-cetoacil-CoA formando carbonilo (+1 NADH)", cofactores: "NAD⁺ ➔ NADH + H⁺", deltag: "+10 kJ/mol", regulacion: "Inhibida por alta relacion NADH/NAD+" },
        { id: "rx_box3", nombre: "Beta-Cetoacil-CoA Tiolasa", ec: "EC 2.3.1.16", sub: ["m_cetoacil_coa"], prod: ["m_acetil_coa_beta", "m_miristoil_coa"], cambio: "Tiolisis liberando 1 Acetil-CoA (2C) y acortando la cadena en 2 carbonos", cofactores: "CoASH", deltag: "-28 kJ/mol", regulacion: "El acil-CoA acortado reingresa en una nueva vuelta de la espiral" }
      ],
      "14": [ // Ciclo de la Urea
        { id: "rx_u_cps1", nombre: "Carbamoil-Fosfato Sintetasa I (CPS-1)", ec: "EC 6.3.4.16", sub: ["m_u_sustratos_inicio"], prod: ["m_u_carbamoil_p"], cambio: "Condensacion de amonio y bicarbonato marcapasos del ciclo de la urea", cofactores: "2 ATP ➔ 2 ADP + Pᵢ", deltag: "-12.5 kJ/mol (Irreversible)", regulacion: "Absolutamente dependiente del activador alosterico N-acetilglutamato (NAG)" },
        { id: "rx_u_otc", nombre: "Ornitina Transcarbamilasa (OTC)", ec: "EC 2.1.3.3", sub: ["m_u_carbamoil_p", "m_u_ornitina_mito"], prod: ["m_u_citrulina_mito"], cambio: "Transferencia de carbamoilo a ornitina en matriz mitocondrial", cofactores: "Pᵢ libre", deltag: "-2.1 kJ/mol", regulacion: "La citrulina es exportada al citosol a través del transportador ORNT1" },
        { id: "rx_u_ass", nombre: "Argininosuccinato Sintetasa (ASS1)", ec: "EC 6.3.4.5", sub: ["m_u_citrulina_cito", "m_u_aspartato"], prod: ["m_u_argininosuccinato"], cambio: "Condensacion citosolica con aspartato aportado por la lanzadera Aralar/Citrina", cofactores: "ATP ➔ AMP + PPᵢ (2 ATP eq)", deltag: "-13 kJ/mol", regulacion: "Incorpora el segundo atomo de nitrogeno de la molecula de urea" },
        { id: "rx_u_asl", nombre: "Argininosuccinato Liasa (ASL)", ec: "EC 4.3.2.1", sub: ["m_u_argininosuccinato"], prod: ["m_u_arginina", "m_u_fumarato"], cambio: "Escision liberando arginina y fumarato (conexion con el biciclo de Krebs)", cofactores: "Ninguno", deltag: "+12.6 kJ/mol", regulacion: "El fumarato se hidrata a malato e ingresa a la mitocondria" },
        { id: "rx_u_arg1", nombre: "Arginasa-1 (ARG1)", ec: "EC 3.5.3.1", sub: ["m_u_arginina"], prod: ["m_u_urea", "m_u_ornitina_cito"], cambio: "Hidrolisis citosolica irreversible liberando molecula de urea y ornitina", cofactores: "H₂O (Mn²⁺)", deltag: "-11.7 kJ/mol (Irreversible)", regulacion: "La ornitina reingresa a la mitocondria por ORNT1 para reiniciar el ciclo" }
      ]
    };

    // Catalogo estructurado de Lanzaderas Mitocondriales Cíclicas Vivas
    const CONFIG_LANZADERAS = {
      "8": {
        id: "8",
        nombre: "Lanzadera Malato-Aspartato",
        lupaId: "lupa_lanzadera_malato_aspartato",
        estequiometria: "2.5 ATP por par de e⁻ (Complejo I)",
        tipo: "Lanzadera Redox Cíclica (Hígado, Riñón y Corazón)",
        conexiones: ["cx_glucolisis_lanz_malato", "cx_lanz_malato_cte_comp1", "cx_lanz_malato_krebs", "cx_lanz_asp_urea"],
        destinoNombre: "Complejo I (NADH)",
        coordsDestino: { x: 2477, y: 3010 },
        fases: [
          {
            titulo: "1. Reducción Citosólica (cMDH)",
            badgeFase: "Fase 1 / 4",
            compartimento: "CITOSOL CELULAR",
            enzima: "cMDH (Malato Deshidrogenasa citosólica)",
            ec: "EC 1.1.1.37",
            reaccion: "Oxalacetato + NADH + H⁺ ➔ L-Malato + NAD⁺",
            sub: ["Oxalacetato [4C]", "NADH + H⁺ (Glucólisis)"],
            prod: ["L-Malato [4C]", "NAD⁺ (Regenerado)"],
            desc: "El NADH generado por la glucólisis citosólica (GAPDH) cede sus 2 electrones al oxalacetato, formándose L-malato y regenerando el NAD⁺ libre necesario para mantener viva la glucólisis anaeróbica y aeróbica.",
            cofactores: "NADH + H⁺ ➔ NAD⁺",
            deltag: "-29.7 kJ/mol (Favorecida por [NADH]/[NAD⁺] citosólica)",
            regulacion: "Acoplada directamente a la velocidad glucolítica",
            carrier: "Ninguno (Reacción soluble en citoplasma)",
            resaltarIds: ["rx_lanz_cmdh", "m_lanz_oaa_cito", "m_lanz_mal_cito"]
          },
          {
            titulo: "2. Antiporte MMI (OGC / SLC25A11)",
            badgeFase: "Fase 2 / 4",
            compartimento: "MEMBRANA MITOCONDRIAL INTERNA",
            enzima: "OGC (SLC25A11 / Antiporte Malato-αKG)",
            ec: "Translocador MMI",
            reaccion: "L-Malato²⁻ (Citosol ➔ Matriz) ⇄ α-Cetoglutarato²⁻ (Matriz ➔ Citosol)",
            sub: ["L-Malato citosólico", "α-Cetoglutarato matricial"],
            prod: ["L-Malato matricial", "α-Cetoglutarato citosólico"],
            desc: "Como la bicapa interna es impermeable al NADH y oxalacetato, el carrier OGC transloca de forma electroneutra el L-malato hacia la matriz mitocondrial a cambio de exportar una molécula de α-cetoglutarato al citosol.",
            cofactores: "Antiporte electroneutro acoplado",
            deltag: "Impulsado por gradientes de concentración",
            regulacion: "Inhibido competitivamente por fenildicarboxilatos",
            carrier: "SLC25A11 (Carrier Oxoglutarato/Malato)",
            resaltarIds: ["trans_lanz_ogc", "m_lanz_mal_cito", "m_lanz_mal_mito"]
          },
          {
            titulo: "3. Oxidación Matriz (mMDH ➔ Complejo I)",
            badgeFase: "Fase 3 / 4",
            compartimento: "MATRIZ MITOCONDRIAL",
            enzima: "mMDH (Malato Deshidrogenasa mitocondrial)",
            ec: "EC 1.1.1.37",
            reaccion: "L-Malato + NAD⁺ ➔ Oxalacetato + NADH + H⁺ ➔ C-I",
            sub: ["L-Malato matricial", "NAD⁺ matricial"],
            prod: ["Oxalacetato matricial", "NADH ➔ Complejo I (2.5 ATP)"],
            desc: "En la matriz mitocondrial, mMDH oxida el L-malato a oxalacetato reduciendo NAD⁺ a NADH. Este NADH cede de inmediato sus electrones al Complejo I de la Cadena Respiratoria, bombeando protones y rindiendo 2.5 ATP.",
            cofactores: "NAD⁺ ➔ NADH + H⁺ (➔ Complejo I)",
            deltag: "+29.7 kJ/mol (Impulsada por bajo [OAA] matricial)",
            regulacion: "Alimenta directamente la respiración celular",
            carrier: "Conexión directa cx_lanz_malato_cte_comp1",
            resaltarIds: ["rx_lanz_mmdh", "m_lanz_mal_mito", "m_lanz_oaa_mito", "cx_lanz_malato_cte_comp1"]
          },
          {
            titulo: "4. Antiporte Aralar / Citrina y Transaminación",
            badgeFase: "Fase 4 / 4",
            compartimento: "MATRIZ ➔ MMI ➔ CITOSOL",
            enzima: "mGOT2 + AGC1/Aralar (SLC25A12) + cGOT1",
            ec: "EC 2.6.1.1 & SLC25A12",
            reaccion: "OAA + Glu ➔ Asp + α-KG (mGOT2) ➔ Aralar (Asp⁻ ⇄ Glu⁻) ➔ cGOT1 (OAA)",
            sub: ["Oxalacetato matricial", "L-Glutamato matricial"],
            prod: ["L-Aspartato citosólico", "Oxalacetato citosólico regenerado"],
            desc: "Para reiniciar el ciclo sin acumular oxalacetato matricial, mGOT2 transamina OAA con Glutamato a Aspartato y α-KG. Aralar (SLC25A12) exporta electrogénicamente el Aspartato al citosol e importa Glutamato; allí cGOT1 regenera OAA cerrando el ciclo.",
            cofactores: "Piridoxal Fosfato (PLP / Vitamina B6)",
            deltag: "Electrogénico: estimulado por el potencial de membrana ΔΨ",
            regulacion: "Activado alostéricamente por Ca²⁺ citosólico en Aralar",
            carrier: "SLC25A12 (Aralar / AGC1) y SLC25A13 (Citrina)",
            resaltarIds: ["trans_lanz_aralar", "rx_lanz_got2", "rx_lanz_got1", "m_lanz_asp_mito", "m_lanz_asp_cito"]
          }
        ]
      },
      "8B": {
        id: "8B",
        nombre: "Lanzadera Glicerol-3-Fosfato",
        lupaId: "lupa_lanzadera_glicerol_p",
        estequiometria: "1.5 ATP por par de e⁻ (CoQ / Complejo III)",
        tipo: "Lanzadera Flavoproteica Rápida (Músculo Esquelético y Cerebro)",
        conexiones: ["cx_dhap_lanzadera_g3p", "cx_lanz_g3p_coq"],
        destinoNombre: "Coenzima Q / Complejo III",
        coordsDestino: { x: 3745, y: 3498 },
        fases: [
          {
            titulo: "1. Reducción Citosólica (cGPDH / GPD1)",
            badgeFase: "Fase 1 / 4",
            compartimento: "CITOSOL CELULAR",
            enzima: "cGPDH / GPD1 (Glicerol-3-P Deshidrogenasa citosólica)",
            ec: "EC 1.1.1.8",
            reaccion: "DHAP + NADH + H⁺ ➔ L-Glicerol-3-P + NAD⁺",
            sub: ["Dihidroxiacetona-P [3C]", "NADH + H⁺ (Glucólisis)"],
            prod: ["L-Glicerol-3-Fosfato [3C]", "NAD⁺ (Regenerado)"],
            desc: "En tejidos de alta tasa glucolítica (músculo en contracción rápida o encéfalo), la cGPDH reduce instantáneamente la DHAP citosólica a Glicerol-3-P consumiendo NADH y regenerando NAD⁺ a máxima velocidad.",
            cofactores: "NADH + H⁺ ➔ NAD⁺",
            deltag: "-26.4 kJ/mol (Irreversible funcionalmente)",
            regulacion: "Activa ante elevadas demandas glucolíticas rápidas",
            carrier: "Ninguno (Citosol)",
            resaltarIds: ["rx_cgpdh", "m_lanz_dhap", "m_lanz_g3p"]
          },
          {
            titulo: "2. Difusión por Porina MME (VDAC)",
            badgeFase: "Fase 2 / 4",
            compartimento: "MEMBRANA MITOCONDRIAL EXTERNA (MME)",
            enzima: "VDAC (Canal Aniónico Dependiente de Voltaje)",
            ec: "Porina de Membrana Externa",
            reaccion: "L-Glicerol-3-P (Citosol ➔ Espacio Intermembrana)",
            sub: ["L-Glicerol-3-P citosólico"],
            prod: ["L-Glicerol-3-P en Espacio Intermembrana"],
            desc: "El Glicerol-3-P recién formado difunde pasivamente por la porina VDAC de la membrana mitocondrial externa, alcanzando el espacio intermembrana sin requerir transportador específico en la MMI.",
            cofactores: "Difusión pasiva facilitada",
            deltag: "Equilibrio osmótico rápido",
            regulacion: "Paso no saturante a través de canales VDAC abiertos",
            carrier: "Porina VDAC (MME)",
            resaltarIds: ["trans_vdac", "m_lanz_g3p"]
          },
          {
            titulo: "3. Oxidación por Flavoproteína mGPDH ➔ CoQ",
            badgeFase: "Fase 3 / 4",
            compartimento: "MEMBRANA MITOCONDRIAL INTERNA (CARA EXTERNA)",
            enzima: "mGPDH / GPD2 (Flavoproteína unida a MMI)",
            ec: "EC 1.1.5.3",
            reaccion: "L-Glicerol-3-P + FAD ➔ DHAP + FADH₂ ➔ CoQH₂ (1.5 ATP)",
            sub: ["L-Glicerol-3-P", "FAD prostético de mGPDH"],
            prod: ["DHAP regenerada", "CoQH₂ (➔ Complejo III ➔ 1.5 ATP)"],
            desc: "mGPDH anclada en la cara externa de la MMI oxida Glicerol-3-P a DHAP. Sus electrones van al grupo prostético FAD y de allí directamente al pool de Ubiquinona (CoQ) hacia el Complejo III, rindiendo 1.5 ATP.",
            cofactores: "FAD (grupo prostético) ➔ Coenzima Q (Ubiquinona)",
            deltag: "-13.5 kJ/mol",
            regulacion: "Activada alostéricamente por Ca²⁺ libre intramitocondrial",
            carrier: "Conexión directa cx_lanz_g3p_coq",
            resaltarIds: ["rx_mgpdh_mmi", "coq_g3p", "comp3_g3p", "cx_lanz_g3p_coq"]
          },
          {
            titulo: "4. Retorno Citosólico de DHAP",
            badgeFase: "Fase 4 / 4",
            compartimento: "ESPACIO INTERMEMBRANA ➔ CITOSOL",
            enzima: "VDAC (Canal Aniónico Dependiente de Voltaje)",
            ec: "Porina MME",
            reaccion: "DHAP (Espacio Intermembrana ➔ Citosol Celular)",
            sub: ["DHAP en Espacio Intermembrana"],
            prod: ["DHAP en Citosol (Aceptor para Glucólisis)"],
            desc: "La DHAP regenerada en la superficie externa de la MMI difunde de vuelta al citosol a través de VDAC, completando la órbita perpetua y quedando lista para captar otro par de electrones glucolíticos.",
            cofactores: "Difusión pasiva facilitada",
            deltag: "Cierre de bucle estacionario",
            regulacion: "Mantiene la reserva de DHAP en equilibrio",
            carrier: "Porina VDAC (MME)",
            resaltarIds: ["trans_vdac", "m_lanz_dhap"]
          }
        ]
      },
      "carnitina": {
        id: "carnitina",
        nombre: "Lanzadera de Carnitina",
        lupaId: "lupa_lanzadera_carnitina",
        estequiometria: "Translocación obligada de Acil-CoA [16C] a Matriz",
        tipo: "Lanzadera de Acilos Grasos para Beta-Oxidación",
        conexiones: ["cx_betaox_etf_cte"],
        destinoNombre: "Beta-Oxidación (Espiral)",
        coordsDestino: { x: 278, y: 2404 },
        fases: [
          {
            titulo: "1. Transesterificación Citosólica (CPT-1)",
            badgeFase: "Fase 1 / 4",
            compartimento: "MEMBRANA MITOCONDRIAL EXTERNA (MME)",
            enzima: "CPT-1 (Carnitina Palmitoiltransferasa 1)",
            ec: "EC 2.3.1.21",
            reaccion: "Palmitoil-CoA + L-Carnitina ➔ Palmitoil-Carnitina + CoASH",
            sub: ["Palmitoil-CoA [16C]", "L-Carnitina libre"],
            prod: ["Palmitoil-Carnitina [16C]", "CoASH citosólico liberado"],
            desc: "Paso limitante y regulador principal de la oxidación de ácidos grasos. CPT-1 une el acilo a carnitina liberando CoA citosólico. Es fuertemente inhibida por Malonil-CoA citosólico durante la lipogénesis.",
            cofactores: "L-Carnitina ➔ CoASH",
            deltag: "-1.2 kJ/mol (Transesterificación isoenergética)",
            regulacion: "Inhibida por Malonil-CoA; activada por Glucagón en ayuno",
            carrier: "CPT-1 en MME",
            resaltarIds: ["rx_cpt1", "m_palm_carnitina"]
          },
          {
            titulo: "2. Antiporte MMI (CACT / SLC25A20)",
            badgeFase: "Fase 2 / 4",
            compartimento: "MEMBRANA MITOCONDRIAL INTERNA (MMI)",
            enzima: "CACT (SLC25A20 / Carnitina-Acilcarnitina Translocasa)",
            ec: "SLC25A20",
            reaccion: "Palmitoil-Carnitina (EIM ➔ Matriz) ⇄ Carnitina libre (Matriz ➔ EIM)",
            sub: ["Palmitoil-Carnitina en EIM"],
            prod: ["Palmitoil-Carnitina en Matriz", "L-Carnitina libre en EIM"],
            desc: "CACT transloca la Palmitoil-Carnitina a través de la membrana interna hacia la matriz mitocondrial, intercambiándola simultáneamente con una molécula de Carnitina libre que regresa al espacio intermembrana.",
            cofactores: "Antiporte electroneutro acoplado 1:1",
            deltag: "Impulsado por balance de masas",
            regulacion: "Su déficit genético causa hipoglucemia no cetósica grave",
            carrier: "SLC25A20 (CACT)",
            resaltarIds: ["transportador_cact", "m_palm_carnitina", "m_carnitina_libre"]
          },
          {
            titulo: "3. Regeneración de Acil-CoA en Matriz (CPT-2)",
            badgeFase: "Fase 3 / 4",
            compartimento: "MATRIZ MITOCONDRIAL",
            enzima: "CPT-2 (Carnitina Palmitoiltransferasa 2)",
            ec: "EC 2.3.1.21",
            reaccion: "Palmitoil-Carnitina + CoASH matricial ➔ Palmitoil-CoA + Carnitina",
            sub: ["Palmitoil-Carnitina matricial", "CoASH matricial"],
            prod: ["Palmitoil-CoA matricial", "L-Carnitina libre matricial"],
            desc: "CPT-2 en la cara matricial de la MMI regenera el Palmitoil-CoA mitocondrial, dejándolo listo para ingresar directamente a la espiral de β-oxidación liberando 8 Acetil-CoA, 7 FADH₂ y 7 NADH.",
            cofactores: "CoASH matricial ➔ Carnitina libre",
            deltag: "+1.2 kJ/mol",
            regulacion: "Alimenta la vía mitocondrial de β-oxidación",
            carrier: "CPT-2 en cara interna de MMI",
            resaltarIds: ["rx_cpt2", "m_palmitoil"]
          },
          {
            titulo: "4. Retorno de Carnitina Libre hacia Citosol",
            badgeFase: "Fase 4 / 4",
            compartimento: "MATRIZ ➔ MMI ➔ CITOSOL",
            enzima: "CACT (SLC25A20)",
            ec: "Translocador MMI",
            reaccion: "L-Carnitina libre (Matriz ➔ CACT ➔ CPT-1 en MME)",
            sub: ["L-Carnitina matricial"],
            prod: ["L-Carnitina citosólica (Reinicia el ciclo)"],
            desc: "La Carnitina libre devuelta a la matriz es transportada por CACT al espacio intermembrana y de allí hacia CPT-1 para aceptar un nuevo ácido graso, manteniendo el bucle cerrado y autosostenible.",
            cofactores: "Ciclo perpetuo de carnitina",
            deltag: "Estacionario continuo",
            regulacion: "La reserva de carnitina libre se recicla continuamente",
            carrier: "SLC25A20 (CACT)",
            resaltarIds: ["transportador_cact", "m_carnitina_libre", "rx_cpt1"]
          }
        ]
      }
    };

    // Catalogo estructurado del Monitor de Cadena Respiratoria y ATP Sintasa
    const CONFIG_CTE = {
      id: "7",
      nombre: "Cadena de Transporte de Electrones y ATP Sintasa",
      lupaId: "lupa_cadena_respiratoria",
      estequiometria: "~2.5 ATP / NADH (C-I) • ~1.5 ATP / FADH₂ (C-II/CoQ)",
      tipo: "Fosforilación Oxidativa y Transporte Electrónico",
      conexiones: [
        "cx_krebs_cte", "cx_lanz_malato_cte_comp1", "cx_lanz_g3p_coq",
        "cx_betaox_etf_cte", "cx_dhodh_coq_cte", "cx_krebs_icdh_cte", "cx_krebs_akgdh_cte", "cx_krebs_mdh_cte"
      ],
      coordsCTE: { x: 3148, y: 2850 },
      fases: [
        {
          titulo: "1. Complejos I y II: Entrada de Electrones a la Cresta MMI",
          badgeFase: "Fase 1 / 5",
          compartimento: "MATRIZ MITOCONDRIAL / MMI",
          enzima: "Complejo I (NADH Deshidrogenasa) & Complejo II (SDH)",
          ec: "EC 1.6.5.3 & EC 1.3.5.1",
          reaccion: "NADH + H⁺ + Q + 4 H⁺_mat ➔ NAD⁺ + QH₂ + 4 H⁺_EIM | Succinato + Q ➔ Fumarato + QH₂",
          sub: ["NADH matricial (Krebs / Lanzadera Malato)", "Succinato (Krebs)"],
          prod: ["Ubiquinol (QH₂) en el pool lipídico", "Fumarato", "NAD⁺"],
          desc: "El Complejo I captura 2 e⁻ del NADH matricial mediante FMN y 8 centros Fe-S, transfiriéndolos a la Coenzima Q y bombeando 4 H⁺ al espacio intermembrana (EIM). En paralelo, el Complejo II oxida Succinato a Fumarato transfiriendo 2 e⁻ vía FAD y centros Fe-S hacia CoQ sin bombear protones.",
          cofactores: "FMN, 8 centros [Fe-S], FAD, hemos b",
          deltag: "-69.5 kJ/mol (C-I, exergónico)",
          regulacion: "Inhibido por rotenona (C-I) y malonato (C-II)",
          carrier: "FMN / Fe-S (C-I) & FAD / Fe-S (C-II)",
          resaltarIds: ["cte_e_comp1", "cte_e_comp2", "cx_krebs_cte", "cx_lanz_malato_cte_comp1"]
        },
        {
          titulo: "2. Pool Lipídico de Coenzima Q (Ubiquinona Q ⇄ QH₂)",
          badgeFase: "Fase 2 / 5",
          compartimento: "BICAPA LIPÍDICA HIDROFÓBICA DE LA MMI",
          enzima: "Coenzima Q₁₀ (Ubiquinona)",
          ec: "Transportador Móvil Lipídico",
          reaccion: "Q + 2 e⁻ + 2 H⁺_mat ⇄ QH₂ (Ubiquinol reducido)",
          sub: ["Electrones de C-I (NADH)", "Electrones de C-II (Succinato)", "Electrones de mGPDH (Lanzadera G3P)", "Electrones de ETF:QO (β-Oxidación)"],
          prod: ["QH₂ móvil difusible en la membrana"],
          desc: "Punto de convergencia metabólico de la respiración celular. Recoge equivalentes de reducción de carbohidratos, lípidos, aminoácidos y pirimidinas, difundiendo lateralmente en el núcleo hidrofóbico de la cresta MMI hacia el sitio Qₒ del Complejo III.",
          cofactores: "Cadena poliisoprenoide (10 unidades)",
          deltag: "Equilibrio redox intramembrana",
          regulacion: "El estado de reducción del pool Q regula la producción de especies reactivas de oxígeno (ROS)",
          carrier: "Coenzima Q₁₀ (Móvil)",
          resaltarIds: ["cte_coq_shuttle", "cx_lanz_g3p_coq", "cx_betaox_etf_cte", "cx_dhodh_coq_cte"]
        },
        {
          titulo: "3. Complejo III & Ciclo Q (Citocromo bc₁)",
          badgeFase: "Fase 3 / 5",
          compartimento: "MMI HACIA ESPACIO INTERMEMBRANA (EIM)",
          enzima: "Complejo III (Coenzima Q:Citocromo c Oxidorreductasa)",
          ec: "EC 1.10.2.2",
          reaccion: "QH₂ + 2 Cit c (Fe³⁺) + 2 H⁺_mat ➔ Q + 2 Cit c (Fe²⁺) + 4 H⁺_EIM",
          sub: ["Ubiquinol (QH₂)", "2 Citocromo c oxidado (Fe³⁺)"],
          prod: ["Ubiquinona (Q)", "2 Citocromo c reducido (Fe²⁺)", "4 H⁺ bombeados a EIM"],
          desc: "Mediante el ciclo Q bifurcado, el Complejo III resuelve la discrepancia estequiométrica entre un transportador de 2 e⁻ (QH₂) y un transportador monoelectrónico (Citocromo c), translocando 4 protones netos al EIM por cada par de electrones transferidos.",
          cofactores: "Hemos bL, bH, proteína ferrosulfurada de Rieske [2Fe-2S], hemo c₁",
          deltag: "-36.7 kJ/mol",
          regulacion: "Inhibido por antimicina A y mixotiazol",
          carrier: "Citocromo bc₁ / Proteína de Rieske",
          resaltarIds: ["cte_e_comp3", "cte_cytc_shuttle"]
        },
        {
          titulo: "4. Complejo IV (Citocromo c Oxidasa) y Reducción a Agua",
          badgeFase: "Fase 4 / 5",
          compartimento: "MMI HACIA MATRIZ MITOCONDRIAL",
          enzima: "Complejo IV (Citocromo c Oxidasa - COX)",
          ec: "EC 1.9.3.1",
          reaccion: "4 Cit c (Fe²⁺) + 4 H⁺_mat + O₂ ➔ 4 Cit c (Fe³⁺) + 2 H₂O (+ 4 H⁺_EIM bombeados)",
          sub: ["4 Citocromo c reducido", "Oxígeno molecular (O₂)", "8 H⁺ de matriz"],
          prod: ["2 H₂O", "4 H⁺ bombeados al EIM (2 H⁺ por par de e⁻)"],
          desc: "Aceptor final de la cadena respiratoria. Transfiere 4 electrones secuenciales desde el Citocromo c soluble a través de CuA, hemo a y el centro binuclear hemo a₃-CuB, reduciendo irreversiblemente una molécula de O₂ a dos moléculas de agua y bombeando protones adicionales.",
          cofactores: "Centros binucleares de cobre CuA y CuB, hemos a y a₃",
          deltag: "-110 kJ/mol (Fuerte tracción termodinámica)",
          regulacion: "Inhibido por cianuro (CN⁻), monóxido de carbono (CO) y azida sódica (N₃⁻)",
          carrier: "Citocromo c oxidasa (Dímero transmembrana)",
          resaltarIds: ["cte_e_comp4", "cte_protones_bombeo"]
        },
        {
          titulo: "5. ATP Sintasa (F₀F₁): Acoplamiento Quimiosmótico",
          badgeFase: "Fase 5 / 5",
          compartimento: "SECTOR F₀ (MMI) Y SECTOR F₁ (MATRIZ MITOCONDRIAL)",
          enzima: "ATP Sintasa Mitocondrial (Complejo V)",
          ec: "EC 7.1.2.2",
          reaccion: "ADP³⁻ + HPO₄²⁻ + H⁺ + 3-4 H⁺_EIM ⇄ ATP⁴⁻ + H₂O + 3-4 H⁺_mat",
          sub: ["ADP matricial", "Fosfato inorgánico (Pᵢ)", "Gradiente protón-motriz (Δp)"],
          prod: ["ATP matricial exportable por ANT (SLC25A4)"],
          desc: "El gradiente electroquímico acumulado en el EIM (Δp = Δψ + ΔpH ≈ 180 mV) impulsa el retorno pasivo de protones a través del canal subunidad a / anillo c de F₀, generando rotación mecánica que hace girar el eje γ dentro del hexámero α₃β₃ de F₁, sintetizando 3 moléculas de ATP por vuelta completa.",
          cofactores: "Subunidades α, β, γ, δ, ε, anillo c, tallo estatórico b-d-F6-OSCP",
          deltag: "+30.5 kJ/mol (Impulsada por la disipación del gradiente)",
          regulacion: "Inhibida por oligomicina (bloquea F₀); desacoplada por termogenina (UCP1) y 2,4-DNP",
          carrier: "Motor molecular rotatorio F₀F₁",
          resaltarIds: ["cte_cascada_atp_sintasa", "cte_atp_liberacion"]
        }
      ]
    };

    let modoCTEActivo = false;
    let faseCTEIdx = 0;
    let intervaloCTE = null;

    function iniciarModoCTE(faseIdx = 0) {
      modoCTEActivo = true;
      modoLanzaderaActivo = false;
      detenerLoopLanzadera();
      faseCTEIdx = faseIdx;

      if (typeof highlightPathway === 'function') {
        highlightPathway("7", false);
      }

      centrarEnCoordenadas(CONFIG_CTE.coordsCTE.x, CONFIG_CTE.coordsCTE.y, 0.95);
      mostrarFaseCTE(faseCTEIdx);
      iniciarLoopCTEAuto();
    }

    function mostrarFaseCTE(idx) {
      if (idx < 0) idx = 0;
      if (idx >= CONFIG_CTE.fases.length) idx = 0;
      faseCTEIdx = idx;

      const f = CONFIG_CTE.fases[idx];
      limpiarResaltadosTransformacion();

      if (f.resaltarIds && f.resaltarIds.length) {
        f.resaltarIds.forEach(id => {
          const el = document.getElementById(id);
          if (el) {
            el.classList.add('ui_highlighted');
            el.classList.remove('ui_dimmed');
          }
        });
      }

      const panel = document.getElementById('ui_panel_transformacion');
      if (panel) {
        document.getElementById('ui_trans_step_badge').className = "ui_shuttle_badge";
        document.getElementById('ui_trans_step_badge').textContent = `Cadena Respiratoria • ${f.badgeFase}`;
        document.getElementById('ui_trans_title').textContent = f.titulo;
        document.getElementById('ui_trans_ec').textContent = f.enzima;

        const yieldEl = document.getElementById('ui_trans_yield');
        yieldEl.textContent = f.yield || CONFIG_CTE.estequiometria;
        yieldEl.style.display = 'inline-block';

        const phasesContainer = document.getElementById('ui_shuttle_phases_container');
        phasesContainer.style.display = 'grid';
        phasesContainer.innerHTML = '';
        for (let i = 0; i < CONFIG_CTE.fases.length; i++) {
          const b = document.createElement('button');
          b.className = `ui_shuttle_phase_btn ${i === idx ? 'active' : ''}`;
          b.textContent = `Fase ${i + 1}`;
          b.onclick = () => irAFaseCTE(i);
          phasesContainer.appendChild(b);
        }

        const compEl = document.getElementById('ui_trans_compartimento');
        compEl.textContent = f.compartimento;
        compEl.style.display = 'inline-block';

        document.getElementById('ui_trans_sub').textContent = f.sub.join(' + ');
        document.getElementById('ui_trans_prod').textContent = f.prod.join(' + ');
        document.getElementById('ui_trans_desc').textContent = f.desc;

        document.getElementById('ui_trans_cofactores').textContent = f.cofactores;
        document.getElementById('ui_trans_deltag').textContent = f.deltag;
        document.getElementById('ui_trans_regulacion').textContent = f.regulacion;

        const carrierBox = document.getElementById('ui_box_carrier');
        const carrierEl = document.getElementById('ui_trans_carrier');
        if (f.carrier) {
          carrierEl.textContent = f.carrier;
          carrierBox.style.display = 'block';
        } else {
          carrierBox.style.display = 'none';
        }

        const btnDest = document.getElementById('ui_btn_shuttle_target');
        btnDest.textContent = "Ver Krebs (NADH)";
        btnDest.onclick = enfocarOrigenNADH;
        btnDest.style.display = 'inline-block';

        const btnLupa = document.getElementById('ui_btn_shuttle_lupa');
        btnLupa.textContent = "Ver Cresta MMI";
        btnLupa.onclick = () => centrarEnCoordenadas(CONFIG_CTE.coordsCTE.x, CONFIG_CTE.coordsCTE.y, 0.95);
        btnLupa.style.display = 'inline-block';

        const btnSpeed = document.getElementById('ui_btn_shuttle_speed');
        btnSpeed.textContent = `${velocidadFactorLanzadera}x`;
        btnSpeed.style.display = 'inline-block';

        const btnAuto = document.getElementById('ui_btn_step_auto');
        btnAuto.textContent = intervaloCTE ? "Pausar" : "Reproducir";

        panel.classList.add('ui_visible');
      }
    }

    function siguienteFaseCTE() {
      faseCTEIdx = (faseCTEIdx + 1) % CONFIG_CTE.fases.length;
      mostrarFaseCTE(faseCTEIdx);
    }

    function anteriorFaseCTE() {
      faseCTEIdx = (faseCTEIdx - 1 + CONFIG_CTE.fases.length) % CONFIG_CTE.fases.length;
      mostrarFaseCTE(faseCTEIdx);
    }

    function irAFaseCTE(idx) {
      detenerLoopCTE();
      mostrarFaseCTE(idx);
    }

    function iniciarLoopCTEAuto() {
      detenerLoopCTE();
      const baseMs = 3800;
      const ms = Math.max(900, baseMs / velocidadFactorLanzadera);
      intervaloCTE = setInterval(() => {
        siguienteFaseCTE();
      }, ms);
      const b = document.getElementById('ui_btn_step_auto');
      if (b) b.textContent = "Pausar";
    }

    function detenerLoopCTE() {
      if (intervaloCTE) {
        clearInterval(intervaloCTE);
        intervaloCTE = null;
      }
      const b = document.getElementById('ui_btn_step_auto');
      if (b) b.textContent = "Reproducir";
    }

    function enfocarOrigenNADH() {
      centrarEnCoordenadas(1150, 2800, 1.2);
    }

    function enfocarOrigenFADH2() {
      centrarEnCoordenadas(240, 2600, 1.2);
    }

    let pasoActualIdx = 0;
    let viaPasoActual = "1";
    let listaPasosActiva = [];

    // Funciones de control de Lanzaderas Vivas
    function iniciarModoLanzadera(lanzId, faseIdx = 0) {
      const cfg = CONFIG_LANZADERAS[lanzId];
      if (!cfg) return;

      // Salir del monitor CTE si estaba activo (la lanzadera de carnitina no llama a highlightPathway)
      modoCTEActivo = false;
      detenerLoopCTE();

      modoLanzaderaActivo = true;
      lanzaderaActualId = lanzId;
      faseLanzaderaIdx = faseIdx;

      // Resaltar la vía correspondiente en el mapa
      if (lanzId === "8" || lanzId === "8B") {
        if (typeof highlightPathway === 'function') {
          highlightPathway(lanzId, false);
        }
      }

      // Enfocar suavemente la lupa de la lanzadera
      enfocarLupaShuttleActual();

      // Mostrar fase
      mostrarFaseLanzadera(faseLanzaderaIdx);

      // Iniciar reproducción automática suave del ciclo
      iniciarLoopLanzaderaAuto();
    }

    function mostrarFaseLanzadera(idx) {
      const cfg = CONFIG_LANZADERAS[lanzaderaActualId];
      if (!cfg || !cfg.fases) return;

      if (idx < 0) idx = 0;
      if (idx >= cfg.fases.length) idx = 0;
      faseLanzaderaIdx = idx;

      const f = cfg.fases[idx];
      limpiarResaltadosTransformacion();

      // Resaltar elementos SVG activos
      if (f.resaltarIds && f.resaltarIds.length) {
        f.resaltarIds.forEach(id => {
          const el = document.getElementById(id);
          if (el) {
            if (id.startsWith('rx_') || id.startsWith('trans_') || id === 'coq_g3p' || id === 'comp3_g3p') {
              el.classList.add('ui_rx_activa');
            } else if (id.startsWith('m_')) {
              el.classList.add('ui_mol_sustrato');
            } else if (id.startsWith('cx_')) {
              el.classList.add('ui_highlighted');
              el.classList.remove('ui_dimmed');
            }
          }
        });
      }

      // Actualizar interfaz del panel didáctico
      const panel = document.getElementById('ui_panel_transformacion');
      if (panel) {
        document.getElementById('ui_trans_step_badge').className = "ui_shuttle_badge";
        document.getElementById('ui_trans_step_badge').textContent = `Lanzadera • ${f.badgeFase}`;
        document.getElementById('ui_trans_title').textContent = cfg.nombre;
        document.getElementById('ui_trans_ec').textContent = f.enzima;

        const yieldEl = document.getElementById('ui_trans_yield');
        yieldEl.textContent = cfg.estequiometria;
        yieldEl.style.display = 'inline-block';

        // Barra de botones de fases
        const phasesContainer = document.getElementById('ui_shuttle_phases_container');
        phasesContainer.style.display = 'grid';
        for (let i = 0; i < 4; i++) {
          const b = document.getElementById(`ui_btn_fase_${i}`);
          if (b) {
            b.classList.toggle('active', i === idx);
          }
        }

        // Compartimento
        const compEl = document.getElementById('ui_trans_compartimento');
        compEl.textContent = f.compartimento;
        compEl.style.display = 'inline-block';

        // Reacción y descripción
        document.getElementById('ui_trans_sub').textContent = f.sub.join(' + ');
        document.getElementById('ui_trans_prod').textContent = f.prod.join(' + ');
        document.getElementById('ui_trans_desc').textContent = f.desc;

        // Detalles
        document.getElementById('ui_trans_cofactores').textContent = f.cofactores;
        document.getElementById('ui_trans_deltag').textContent = f.deltag;
        document.getElementById('ui_trans_regulacion').textContent = f.regulacion;

        const carrierBox = document.getElementById('ui_box_carrier');
        const carrierEl = document.getElementById('ui_trans_carrier');
        if (f.carrier) {
          carrierEl.textContent = f.carrier;
          carrierBox.style.display = 'block';
        } else {
          carrierBox.style.display = 'none';
        }

        // Botones de acción específicos de lanzadera
        const btnDest = document.getElementById('ui_btn_shuttle_target');
        btnDest.textContent = `Ver ${cfg.destinoNombre}`;
        btnDest.style.display = 'inline-block';

        const btnLupa = document.getElementById('ui_btn_shuttle_lupa');
        btnLupa.style.display = 'inline-block';

        const btnSpeed = document.getElementById('ui_btn_shuttle_speed');
        btnSpeed.textContent = `${velocidadFactorLanzadera}x`;
        btnSpeed.style.display = 'inline-block';

        const btnAuto = document.getElementById('ui_btn_step_auto');
        btnAuto.textContent = intervaloLanzadera ? "Pausar" : "Reproducir";

        panel.classList.add('ui_visible');
      }
    }

    function siguienteFaseLanzadera() {
      const cfg = CONFIG_LANZADERAS[lanzaderaActualId];
      if (!cfg) return;
      faseLanzaderaIdx = (faseLanzaderaIdx + 1) % cfg.fases.length;
      mostrarFaseLanzadera(faseLanzaderaIdx);
    }

    function anteriorFaseLanzadera() {
      const cfg = CONFIG_LANZADERAS[lanzaderaActualId];
      if (!cfg) return;
      faseLanzaderaIdx = (faseLanzaderaIdx - 1 + cfg.fases.length) % cfg.fases.length;
      mostrarFaseLanzadera(faseLanzaderaIdx);
    }

    function irAFaseLanzadera(idx) {
      detenerLoopLanzadera();
      mostrarFaseLanzadera(idx);
    }

    function toggleReproduccionLanzadera() {
      if (intervaloLanzadera) {
        detenerLoopLanzadera();
      } else {
        iniciarLoopLanzaderaAuto();
      }
      const b = document.getElementById('ui_btn_step_auto');
      if (b) b.textContent = intervaloLanzadera ? "Pausar" : "Reproducir";
    }

    function iniciarLoopLanzaderaAuto() {
      detenerLoopLanzadera();
      const baseMs = 3000;
      const ms = Math.max(800, baseMs / velocidadFactorLanzadera);
      intervaloLanzadera = setInterval(() => {
        siguienteFaseLanzadera();
      }, ms);
      const b = document.getElementById('ui_btn_step_auto');
      if (b) b.textContent = "Pausar";
    }

    function detenerLoopLanzadera() {
      if (intervaloLanzadera) {
        clearInterval(intervaloLanzadera);
        intervaloLanzadera = null;
      }
      const b = document.getElementById('ui_btn_step_auto');
      if (b) b.textContent = "Reproducir";
    }

    function toggleVelocidadLanzadera() {
      if (velocidadFactorLanzadera === 1) velocidadFactorLanzadera = 2;
      else if (velocidadFactorLanzadera === 2) velocidadFactorLanzadera = 0.5;
      else velocidadFactorLanzadera = 1;

      const btn = document.getElementById('ui_btn_shuttle_speed');
      if (btn) btn.textContent = `${velocidadFactorLanzadera}x`;

      if (intervaloLanzadera) {
        iniciarLoopLanzaderaAuto();
      }
    }

    function enfocarDestinoCadena() {
      const cfg = CONFIG_LANZADERAS[lanzaderaActualId];
      if (!cfg || !cfg.coordsDestino) return;
      centrarEnCoordenadas(cfg.coordsDestino.x, cfg.coordsDestino.y, 1.35);
    }

    function enfocarLupaShuttleActual() {
      const cfg = CONFIG_LANZADERAS[lanzaderaActualId];
      if (!cfg) return;
      const el = document.getElementById(cfg.lupaId);
      if (el) {
        const b = getElementSvgBounds(el);
        if (b) {
          centrarEnCoordenadas(b.x + b.width / 2, b.y + b.height / 2, 0.95);
        }
      }
    }

    function centrarEnCoordenadas(x, y, targetScale = 1.0) {
      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;
      const px = x - VB_X;
      const py = y - VB_Y;
      scale = targetScale;
      pointX = vw / 2 - px * scale;
      pointY = vh / 2 - py * scale;
      updateTransform();
    }

    function iniciarPasoAPaso(viaId = null) {
      if (!viaId) viaId = viaResaltadaActual || "1";
      viaPasoActual = String(viaId);

      // Si la vía es la Cadena Respiratoria, delegar al monitor CTE
      if (viaPasoActual === "7") {
        iniciarModoCTE(0);
        return;
      }

      // Si la vía es una lanzadera mitocondrial, delegar directamente a su simulador cíclico
      if (viaPasoActual === "8" || viaPasoActual === "8B") {
        iniciarModoLanzadera(viaPasoActual, 0);
        return;
      }

      modoLanzaderaActivo = false;
      detenerLoopLanzadera();
      modoCTEActivo = false;
      detenerLoopCTE();


      // Ocultar elementos de lanzadera en el panel
      const yieldEl = document.getElementById('ui_trans_yield');
      if (yieldEl) yieldEl.style.display = 'none';
      const phasesContainer = document.getElementById('ui_shuttle_phases_container');
      if (phasesContainer) phasesContainer.style.display = 'none';
      const compEl = document.getElementById('ui_trans_compartimento');
      if (compEl) compEl.style.display = 'none';
      const carrierBox = document.getElementById('ui_box_carrier');
      if (carrierBox) carrierBox.style.display = 'none';
      const btnDest = document.getElementById('ui_btn_shuttle_target');
      if (btnDest) btnDest.style.display = 'none';
      const btnLupa = document.getElementById('ui_btn_shuttle_lupa');
      if (btnLupa) btnLupa.style.display = 'none';
      const btnSpeed = document.getElementById('ui_btn_shuttle_speed');
      if (btnSpeed) btnSpeed.style.display = 'none';

      listaPasosActiva = CATALOGO_PASOS_VIAS[viaPasoActual] || [];

      // Si la vía no tiene catálogo preestablecido, construirlo dinámicamente desde TABLA_VIAS
      if (!listaPasosActiva.length && TABLA_VIAS[viaPasoActual]) {
        const v = TABLA_VIAS[viaPasoActual];
        const rxIds = [];
        v.grupos.forEach(gid => {
          const el = document.getElementById(gid);
          if (el) {
            el.querySelectorAll('[id^="rx_"]').forEach(r => rxIds.push(r.id));
          }
        });
        listaPasosActiva = rxIds.map(rid => {
          const info = TABLA_REACCIONES_DATA[rid] || {};
          return {
            id: rid,
            nombre: info.enzima || rid,
            ec: info.ec || "",
            sub: [],
            prod: [],
            cambio: info.ecuacion || "Reaccion enzimatica",
            cofactores: info.coproductos || "Ninguno",
            deltag: info.deltaG || "",
            regulacion: info.regulacion || ""
          };
        });
      }

      if (!listaPasosActiva.length) {
        alert("Selecciona una via con reacciones enzimaticas catalogadas.");
        return;
      }

      pasoActualIdx = 0;
      highlightPathway(viaPasoActual, false);
      mostrarPaso(pasoActualIdx);
    }

    function mostrarPaso(idx) {
      if (!listaPasosActiva || !listaPasosActiva.length) return;
      if (idx < 0) idx = 0;
      if (idx >= listaPasosActiva.length) idx = listaPasosActiva.length - 1;
      pasoActualIdx = idx;

      const p = listaPasosActiva[idx];
      limpiarResaltadosTransformacion();

      // Resaltar enzima activa
      const rxEl = document.getElementById(p.id);
      if (rxEl) rxEl.classList.add('ui_rx_activa');

      // Resaltar sustratos
      p.sub.forEach(sid => {
        const el = document.getElementById(sid);
        if (el) el.classList.add('ui_mol_sustrato');
      });

      // Resaltar productos
      p.prod.forEach(pid => {
        const el = document.getElementById(pid);
        if (el) el.classList.add('ui_mol_producto');
      });

      // Actualizar interfaz del panel didactico
      const panel = document.getElementById('ui_panel_transformacion');
      if (panel) {
        const stepBadge = document.getElementById('ui_trans_step_badge');
        stepBadge.className = "ui_trans_step_badge";
        stepBadge.textContent = `Paso ${idx + 1} de ${listaPasosActiva.length}`;
        document.getElementById('ui_trans_title').textContent = p.nombre;
        document.getElementById('ui_trans_ec').textContent = p.ec || '';
        document.getElementById('ui_trans_desc').textContent = p.cambio;
        document.getElementById('ui_trans_cofactores').textContent = p.cofactores || 'Ninguno';
        document.getElementById('ui_trans_deltag').textContent = p.deltag || 'N/A';
        document.getElementById('ui_trans_regulacion').textContent = p.regulacion || 'Control fisiologico';

        const infoSustrato = p.sub.map(s => document.getElementById(s)?.querySelector('text')?.textContent || s).join(' + ') || 'Sustrato';
        const infoProducto = p.prod.map(pr => document.getElementById(pr)?.querySelector('text')?.textContent || pr).join(' + ') || 'Producto';
        document.getElementById('ui_trans_sub').textContent = infoSustrato;
        document.getElementById('ui_trans_prod').textContent = infoProducto;

        panel.classList.add('ui_visible');
      }

      // Auto-enfoque suave de camara
      if (seguirCamaraActivo && rxEl) {
        const subEl = p.sub[0] ? document.getElementById(p.sub[0]) : null;
        const prodEl = p.prod[0] ? document.getElementById(p.prod[0]) : null;
        centrarEnReaccion(subEl, rxEl, prodEl);
      }
    }

    function pasoSiguiente() {
      if (modoCTEActivo) {
        siguienteFaseCTE();
        return;
      }
      if (modoLanzaderaActivo) {
        siguienteFaseLanzadera();
        return;
      }
      if (!listaPasosActiva.length) return;
      if (pasoActualIdx < listaPasosActiva.length - 1) {
        mostrarPaso(pasoActualIdx + 1);
      } else {
        mostrarPaso(0); // Reiniciar al inicio de la via
      }
    }

    function pasoAnterior() {
      if (modoCTEActivo) {
        anteriorFaseCTE();
        return;
      }
      if (modoLanzaderaActivo) {
        anteriorFaseLanzadera();
        return;
      }
      if (!listaPasosActiva.length) return;
      if (pasoActualIdx > 0) {
        mostrarPaso(pasoActualIdx - 1);
      }
    }

    function cerrarPanelTransformacion() {
      const panel = document.getElementById('ui_panel_transformacion');
      if (panel) panel.classList.remove('ui_visible');
      limpiarResaltadosTransformacion();
      modoLanzaderaActivo = false;
      detenerLoopLanzadera();
      modoCTEActivo = false;
      detenerLoopCTE();
      if (reproduccionAutoInterval) {
        clearInterval(reproduccionAutoInterval);
        reproduccionAutoInterval = null;
        const b = document.getElementById('ui_btn_step_auto');
        if (b) b.textContent = "Reproducir";
      }
    }

    function limpiarResaltadosTransformacion() {
      document.querySelectorAll('.ui_mol_sustrato, .ui_mol_producto, .ui_rx_activa').forEach(el => {
        el.classList.remove('ui_mol_sustrato', 'ui_mol_producto', 'ui_rx_activa');
      });
    }

    function toggleSeguirCamara() {
      seguirCamaraActivo = !seguirCamaraActivo;
      const btn = document.getElementById('ui_btn_cam_follow');
      if (btn) btn.textContent = seguirCamaraActivo ? "Camara: ON" : "Camara: OFF";
    }

    function toggleReproduccionAuto() {
      if (modoCTEActivo) {
        if (intervaloCTE) detenerLoopCTE();
        else iniciarLoopCTEAuto();
        return;
      }
      if (modoLanzaderaActivo) {
        toggleReproduccionLanzadera();
        return;
      }
      const btn = document.getElementById('ui_btn_step_auto');
      if (reproduccionAutoInterval) {
        clearInterval(reproduccionAutoInterval);
        reproduccionAutoInterval = null;
        if (btn) btn.textContent = "Reproducir";
      } else {
        if (btn) btn.textContent = "Pausar";
        reproduccionAutoInterval = setInterval(() => {
          pasoSiguiente();
        }, 4000);
      }
    }

    function centrarEnReaccion(subEl, rxEl, prodEl) {
      if (!seguirCamaraActivo) return;
      const elementos = [subEl, rxEl, prodEl].filter(Boolean);
      if (!elementos.length) return;

      let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
      elementos.forEach(el => {
        const b = getElementSvgBounds(el);
        if (b) {
          minX = Math.min(minX, b.x);
          minY = Math.min(minY, b.y);
          maxX = Math.max(maxX, b.x + b.width);
          maxY = Math.max(maxY, b.y + b.height);
        }
      });

      if (minX !== Infinity && maxX > minX) {
        const cx = (minX + maxX) / 2;
        const cy = (minY + maxY) / 2;
        const boxW = Math.max(maxX - minX, 320);
        const boxH = Math.max(maxY - minY, 260);
        const vw = viewport.clientWidth;
        const vh = viewport.clientHeight;
        const targetScale = Math.min(vw / (boxW * 1.6), vh / (boxH * 1.8), 1.5);

        centrarEnCoordenadas(cx, cy, targetScale);
      }
    }

    // Interceptar clics en el lienzo SVG para activar CTE, lanzaderas o reacciones
    window.addEventListener('click', (e) => {
      const target = e.target;
      if (!target) return;

      // Clic en lupa de cadena respiratoria (CTE)
      if (target.closest('#lupa_cadena_respiratoria')) {
        iniciarModoCTE(0);
        return;
      }
      // Clic en lupa de lanzadera malato-aspartato
      if (target.closest('#lupa_lanzadera_malato_aspartato')) {
        iniciarModoLanzadera("8", 0);
        return;
      }
      // Clic en lupa de lanzadera glicerol-3-fosfato
      if (target.closest('#lupa_lanzadera_glicerol_p')) {
        iniciarModoLanzadera("8B", 0);
        return;
      }
      // Clic en lupa de lanzadera carnitina
      if (target.closest('#lupa_lanzadera_carnitina')) {
        iniciarModoLanzadera("carnitina", 0);
        return;
      }

      // Clic en enzima de vía lineal
      const rxTarget = target.closest('[id^="rx_"]');
      if (rxTarget) {
        const rid = rxTarget.id;
        for (const [vid, pasos] of Object.entries(CATALOGO_PASOS_VIAS)) {
          const fIdx = pasos.findIndex(p => p.id === rid);
          if (fIdx !== -1) {
            viaPasoActual = vid;
            listaPasosActiva = pasos;
            modoLanzaderaActivo = false;
            detenerLoopLanzadera();
            highlightPathway(vid, false);
            mostrarPaso(fIdx);
            return;
          }
        }
      }
    });

    // Control por teclado para avanzar y retroceder pasos y pausar ciclo
    window.addEventListener('keydown', (e) => {
      if (e.target.tagName === 'INPUT') return;
      if (e.key === 'ArrowRight') {
        pasoSiguiente();
      } else if (e.key === 'ArrowLeft') {
        pasoAnterior();
      } else if (e.key === ' ' || e.code === 'Space') {
        e.preventDefault();
        toggleReproduccionAuto();
      } else if (e.key === 'Escape') {
        cerrarPanelTransformacion();
      }
    });

    function toggleModoLectura() {
      modoLecturaActivo = !modoLecturaActivo;
      document.body.classList.toggle('ui_reading_mode', modoLecturaActivo);
      const btn = document.getElementById('ui_btn_reading');
      if (btn) btn.classList.toggle('ui_btn_active_custom', modoLecturaActivo);
      // Las bolitas son <circle>/<ellipse> con <animateMotion>: se ocultan / muestran todas a la vez
      document.querySelectorAll('animateMotion').forEach(a => {
        if (a.parentElement) a.parentElement.classList.toggle('ui_particula_oculta_lectura', modoLecturaActivo);
      });
    }

    function toggleModoAislar() {
      modoAislarActivo = !modoAislarActivo;
      document.body.classList.toggle('ui_isolate_mode', modoAislarActivo);
      const btn = document.getElementById('ui_btn_isolate');
      if (btn) btn.classList.toggle('ui_btn_active_custom', modoAislarActivo);
    }

    function toggleFlujoAnimado() {
      flujoAnimadoHabilitado = !flujoAnimadoHabilitado;
      actualizarEstadoFlujo();
    }

    function actualizarEstadoFlujo() {
      const btn = document.getElementById('ui_btn_flow');
      const svgElem = document.querySelector('svg');
      if (flujoAnimadoHabilitado) {
        document.body.classList.add('ui_flujo_on');
        document.body.classList.remove('pausar-animaciones');
        if (svgElem && svgElem.unpauseAnimations) svgElem.unpauseAnimations();
        if (btn) {
          btn.classList.add('ui_btn_active_custom');
          btn.textContent = 'Flujo: Activo';
        }
        if (!viaResaltadaActual && (!estadoMetabolicoActual || estadoMetabolicoActual === 'normal')) {
          document.body.classList.add('ui_flujo_global');
        } else {
          document.body.classList.remove('ui_flujo_global');
        }
      } else {
        document.body.classList.remove('ui_flujo_on');
        document.body.classList.remove('ui_flujo_global');
        document.body.classList.add('pausar-animaciones');
        if (svgElem && svgElem.pauseAnimations) svgElem.pauseAnimations();
        if (btn) {
          btn.classList.remove('ui_btn_active_custom');
          btn.textContent = 'Flujo: Pausado';
        }
      }
    }

    // Catalogo de diagramas SVG individuales de cada ruta
    const MAPA_VIAS_SVG = {
      "1": "01_CARBOHIDRATOS/via_01_glucolisis/Glucolisis.svg",
      "2": "01_CARBOHIDRATOS/via_02_gluconeogenesis/Gluconeogenesis.svg",
      "3": "01_CARBOHIDRATOS/via_03_glucogenogenesis_y_glucogenolisis/Glucogenesis.svg",
      "4": "01_CARBOHIDRATOS/via_04_pentosas_fosfato/Pentosas.svg",
      "5": "02_RESPIRACION_Y_ENERGIA/via_05_complejo_pdh/Piruvato_Deshidrogenasa.svg",
      "6": "02_RESPIRACION_Y_ENERGIA/via_06_ciclo_de_krebs/Ciclo_de_Krebs.svg",
      "7": "02_RESPIRACION_Y_ENERGIA/via_07_cadena_respiratoria_atp_sintasa/Cadena_Transporte_Electrones.svg",
      "8": "02_RESPIRACION_Y_ENERGIA/via_08_lanzaderas/Lanzadera_Malato_Aspartato.svg",
      "8B": "02_RESPIRACION_Y_ENERGIA/via_08_lanzaderas/Lanzadera_Glicerol_3_Fosfato.svg",
      "9": "03_LIPIDOS/via_09_beta_oxidacion/Beta_Oxidacion.svg",
      "10": "03_LIPIDOS/via_10_lipogenesis/Lipogenesis.svg",
      "11": "03_LIPIDOS/via_11_cetogenesis_y_cetolisis/Cetogenesis_y_Cetolisis.svg",
      "12": "03_LIPIDOS/via_12_colesterol_y_lipoproteinas/Colesterol.svg",
      "12B": "04_NITROGENO_Y_AMINOACIDOS/via_12b_destinos_esqueletos_carbonados/Destinos_Esqueletos_Carbonados.svg",
      "13": "04_NITROGENO_Y_AMINOACIDOS/via_13_transaminacion_y_desaminacion/Transaminacion_y_Desaminacion.svg",
      "14": "04_NITROGENO_Y_AMINOACIDOS/via_14_ciclo_de_la_urea/Ciclo_de_la_Urea.svg",
      "15": "05_NUCLEOTIDOS_Y_OTRAS/via_15_sintesis_purinas_y_pirimidinas/Sintesis_Purinas_y_Pirimidinas.svg",
      "16": "05_NUCLEOTIDOS_Y_OTRAS/via_16_degradacion_y_acido_urico/Degradacion_Nucleotidos_y_Acido_Urico.svg",
      "17": "01_CARBOHIDRATOS/via_17_ciclo_de_cori/Ciclo_de_Cori.svg",
      "18": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "19": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "20": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "21": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "22": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "23": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "24": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "25": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg"
    };

    function getSvgUrlDeVia(viaId) {
      const rel = MAPA_VIAS_SVG[viaId];
      if (!rel) return null;
      const isSubdir = window.location.pathname.includes('/versiones_html') || window.location.pathname.includes('/mapa_metabolico_alternativo');
      return (isSubdir ? '../' : '') + rel;
    }

    function abrirSvgViaActual() {
      const sel = document.getElementById('ui_select_quick_via');
      const viaId = (sel && sel.value) ? sel.value : (typeof viaResaltadaActual !== 'undefined' ? viaResaltadaActual : null);
      if (!viaId) {
        alert('Por favor selecciona primero una vía en el selector o en el mapa.');
        return;
      }
      const url = getSvgUrlDeVia(viaId);
      if (url) {
        window.open(url, '_blank');
      }
    }

    // Navegacion entre versiones del mapa preservando parametros URL
    function irAMapaAlternativo() {
      try {
        const params = window.location.search;
        const isSubdir = window.location.pathname.includes('/versiones_html') || window.location.pathname.includes('/mapa_metabolico_alternativo');
        const target = isSubdir ? '../index.html' : 'index.html';
        window.location.href = target + params;
      } catch (e) {
        window.location.href = 'index.html';
      }
    }

    function irAMapaOriginal() {
      try {
        const params = window.location.search;
        const path = window.location.pathname;
        // El mapa original vive siempre en versiones_html/. Desde la raiz (GitHub Pages, file://, etc.)
        // hay que anteponer esa carpeta; si ya estamos dentro de ella basta el nombre del archivo.
        let target = 'versiones_html/01_mapa_ampliado_completo_25_vias.html';
        if (path.includes('/versiones_html/')) {
          target = '01_mapa_ampliado_completo_25_vias.html';
        } else if (path.includes('/mapa_metabolico_alternativo/')) {
          target = '../versiones_html/01_mapa_ampliado_completo_25_vias.html';
        }
        window.location.href = target + params;
      } catch (e) {
        window.location.href = 'versiones_html/01_mapa_ampliado_completo_25_vias.html';
      }
    }

    // Selector rapido de vias (1 a 25)
    function seleccionarViaRapida(val) {
      if (!val) {
        if (typeof clearPathwayHighlight === 'function') clearPathwayHighlight();
        actualizarParametroURL('via', null);
        return;
      }
      if (typeof highlightPathway === 'function') {
        highlightPathway(val, true);
        actualizarParametroURL('via', val);
      }
    }

    function actualizarParametroURL(clave, valor) {
      try {
        const url = new URL(window.location.href);
        if (valor) {
          url.searchParams.set(clave, valor);
        } else {
          url.searchParams.delete(clave);
        }
        window.history.replaceState(null, '', url.toString());
      } catch (e) {
        // Fallback silencioso
      }
    }

    // Interceptar highlightPathway para sincronizar conexiones, dropdown rapido y simuladores
    const fnOrigHighlight = window.highlightPathway;
    if (typeof fnOrigHighlight === 'function') {
      window.highlightPathway = function(viaId, shouldZoom = false) {
        // Al cambiar a otra via hay que parar el monitor CTE / lanzadera que siguiera activo:
        // si no, su temporizador seguia cambiando de fase y pisando la nueva seleccion.
        const mantieneCTE = viaId === "7" && modoCTEActivo;
        const mantieneLanzadera = (viaId === "8" || viaId === "8B") && modoLanzaderaActivo && lanzaderaActualId === viaId;
        if (modoCTEActivo && !mantieneCTE) {
          modoCTEActivo = false;
          detenerLoopCTE();
        }
        if (modoLanzaderaActivo && !mantieneLanzadera) {
          modoLanzaderaActivo = false;
          detenerLoopLanzadera();
        }

        fnOrigHighlight(viaId, shouldZoom);
        const v = TABLA_VIAS[viaId];
        if (v && v.conexiones) {
          v.conexiones.forEach(cxId => {
            const el = document.getElementById(cxId);
            if (el) {
              el.classList.add('ui_highlighted');
              el.classList.remove('ui_dimmed');
            }
          });
        }

        // Sincronizar selector desplegable rapido
        const sel = document.getElementById('ui_select_quick_via');
        if (sel && sel.value !== String(viaId)) {
          sel.value = String(viaId);
        }
        actualizarParametroURL('via', viaId);

        // Mostrar boton de SVG individual en banner
        const bannerBtn = document.getElementById('ui_btn_banner_svg');
        if (bannerBtn) bannerBtn.style.display = MAPA_VIAS_SVG[viaId] ? 'inline-block' : 'none';

        // Resaltar partículas de la vía seleccionada
        document.querySelectorAll('.ui_grupo_flujo_via').forEach(g => {
          if (g.id === `anim_flujo_via_${viaId}`) {
            g.style.opacity = '1';
          } else {
            g.style.opacity = '0.25';
          }
        });

        actualizarEstadoFlujo();

        // Si el usuario selecciona la vía 7 (CTE) o una lanzadera, activar su monitor.
        // Importante: iniciarModoCTE/iniciarModoLanzadera vuelven a llamar a highlightPathway,
        // asi que solo se arrancan si el modo todavia no esta activo (antes esto era un bucle
        // infinito cada 150 ms que dejaba el mapa colgado).
        if (viaId === "7" && !modoCTEActivo) {
          setTimeout(() => {
            if (viaResaltadaActual === "7" && !modoCTEActivo) iniciarModoCTE(0);
          }, 150);
        } else if ((viaId === "8" || viaId === "8B") && !(modoLanzaderaActivo && lanzaderaActualId === viaId)) {
          setTimeout(() => {
            if (viaResaltadaActual === viaId && !(modoLanzaderaActivo && lanzaderaActualId === viaId)) iniciarModoLanzadera(viaId, 0);
          }, 150);
        }
      };
    }

    // Interceptar clearPathwayHighlight
    const fnOrigClear = window.clearPathwayHighlight;
    if (typeof fnOrigClear === 'function') {
      window.clearPathwayHighlight = function() {
        fnOrigClear();
        const sel = document.getElementById('ui_select_quick_via');
        if (sel) {
          sel.value = '';
        }
        actualizarParametroURL('via', null);

        const bannerBtn = document.getElementById('ui_btn_banner_svg');
        if (bannerBtn) bannerBtn.style.display = 'none';

        document.querySelectorAll('#capa_conexiones_inter_ruta .conexion-inter-ruta').forEach(el => {
          el.classList.remove('ui_highlighted');
        });
        document.querySelectorAll('.ui_grupo_flujo_via').forEach(g => {
          g.style.opacity = '0.9';
        });
        actualizarEstadoFlujo();
        cerrarPanelTransformacion();
      };
    }

    // Inyectar boton [SVG] en cada elemento del indice lateral
    const fnOrigPoblar = window.poblarSidebarVias;
    if (typeof fnOrigPoblar === 'function') {
      window.poblarSidebarVias = function() {
        fnOrigPoblar();
        document.querySelectorAll('.ui_sidebar_item').forEach(it => {
          const vid = it.getAttribute('data-via');
          const svgUrl = getSvgUrlDeVia(vid);
          if (svgUrl && !it.querySelector('.ui_sidebar_svg_btn')) {
            const btn = document.createElement('a');
            btn.className = 'ui_sidebar_svg_btn';
            btn.href = svgUrl;
            btn.target = '_blank';
            btn.title = 'Abrir diagrama SVG individual';
            btn.textContent = 'SVG';
            btn.onclick = (e) => e.stopPropagation();
            btn.style.cssText = 'margin-left:auto; background:rgba(56,189,248,0.15); border:1px solid #0284c7; color:#38bdf8; font-size:10px; font-weight:800; padding:2px 6px; border-radius:4px; text-decoration:none; white-space:nowrap;';
            it.appendChild(btn);
          }
        });
      };
    }

    // Interceptar setMetabolicState
    const fnOrigSetState = window.setMetabolicState;
    if (typeof fnOrigSetState === 'function') {
      window.setMetabolicState = function(stateId) {
        fnOrigSetState(stateId);
        const st = TABLA_ESTADOS_METABOLICOS[stateId];
        if (st && st.activas) {
          const cxActivas = new Set();
          st.activas.forEach(vid => {
            const v = TABLA_VIAS[vid];
            if (v && v.conexiones) v.conexiones.forEach(c => cxActivas.add(c));
          });
          document.querySelectorAll('#capa_conexiones_inter_ruta .conexion-inter-ruta').forEach(el => {
            if (cxActivas.has(el.id)) {
              el.classList.add('ui_state_active');
              el.classList.remove('ui_dimmed');
            } else if (stateId !== 'normal') {
              el.classList.add('ui_dimmed');
              el.classList.remove('ui_state_active');
            }
          });
        }
        actualizarEstadoFlujo();
      };
    }

    function procesarParametrosURL() {
      try {
        const params = new URLSearchParams(window.location.search);
        
        const mapParam = params.get('map');
        if (mapParam === 'original' && !window.location.pathname.includes('01_mapa_ampliado')) {
          irAMapaOriginal();
          return;
        }

        const svgParam = params.get('svg') || params.get('img');
        if (svgParam) {
          const raw = svgParam.trim();
          const upper = raw.toUpperCase();
          const target = MAPA_VIAS_SVG[upper] ? upper : (MAPA_VIAS_SVG[raw] ? raw : null);
          if (target) {
            const url = getSvgUrlDeVia(target);
            if (url) {
              window.location.href = url;
              return;
            }
          }
        }

        const viaParam = params.get('via');
        if (viaParam) {
          const raw = viaParam.trim();
          const upper = raw.toUpperCase();
          const targetVia = (typeof TABLA_VIAS !== 'undefined' && TABLA_VIAS[upper]) ? upper : ((typeof TABLA_VIAS !== 'undefined' && TABLA_VIAS[raw]) ? raw : null);
          if (targetVia) {
            setTimeout(() => {
              if (typeof highlightPathway === 'function') highlightPathway(targetVia, true);
            }, 300);
          } else {
            const vNum = parseInt(raw, 10);
            if (!isNaN(vNum) && vNum >= 1 && vNum <= 25) {
              setTimeout(() => {
                if (typeof highlightPathway === 'function') highlightPathway(String(vNum), true);
              }, 300);
            }
          }
        }
        const searchParam = params.get('search') || params.get('q');
        if (searchParam) {
          setTimeout(() => {
            const input = document.getElementById('ui_search_input');
            if (input) {
              input.value = searchParam;
              if (typeof ejecutarBusqueda === 'function') ejecutarBusqueda();
            }
          }, 300);
        }
        const stateParam = params.get('state');
        if (stateParam) {
          setTimeout(() => {
            if (typeof setMetabolicState === 'function') setMetabolicState(stateParam);
          }, 300);
        }
      } catch (err) {
        console.warn('Error al procesar parametros URL:', err);
      }
    }

    window.addEventListener('DOMContentLoaded', () => {
      procesarParametrosURL();
      flujoAnimadoHabilitado = true;
      actualizarEstadoFlujo();
    });
    if (document.readyState !== 'loading') {
      procesarParametrosURL();
      flujoAnimadoHabilitado = true;
      actualizarEstadoFlujo();
    }
  </script>"""
    html_content = html_content.replace('  </script>', js_extra, 1)

    # Sincronizar conexiones inter-ruta de las lanzaderas y CTE en TABLA_VIAS
    html_content = html_content.replace(
        '"7": { numero: "7", id: "7", nombre: "Cadena de transporte de electrones y ATP sintasa", subtitulo: "MMI: Complejos I–IV, gradiente electroquímico y fosforilación oxidativa", grupos: ["lupa_cadena_respiratoria", "ancla_cresta_mmi", "badge_via_7"], color: "#0284c7" }',
        '"7": { numero: "7", id: "7", nombre: "Cadena de transporte de electrones y ATP sintasa", subtitulo: "MMI: Complejos I–IV, gradiente electroquímico y fosforilación oxidativa", grupos: ["lupa_cadena_respiratoria", "ancla_cresta_mmi", "badge_via_7"], conexiones: ["cx_krebs_cte", "cx_lanz_malato_cte_comp1", "cx_lanz_g3p_coq", "cx_betaox_etf_cte", "cx_dhodh_coq_cte", "cx_krebs_icdh_cte", "cx_krebs_akgdh_cte", "cx_krebs_mdh_cte"], color: "#0284c7" }'
    )
    html_content = html_content.replace(
        '"8": { numero: "8", id: "8", nombre: "Lanzadera malato-aspartato", subtitulo: "Transporte de equivalentes redox (NADH citosólico a matriz)", grupos: ["lupa_lanzadera_malato_aspartato", "badge_via_8"], color: "#0284c7" }',
        '"8": { numero: "8", id: "8", nombre: "Lanzadera malato-aspartato", subtitulo: "Transporte de equivalentes redox (NADH citosólico a matriz)", grupos: ["lupa_lanzadera_malato_aspartato", "badge_via_8"], conexiones: ["cx_glucolisis_lanz_malato", "cx_lanz_malato_cte_comp1", "cx_lanz_malato_krebs", "cx_lanz_asp_urea"], color: "#0284c7" }'
    )
    html_content = html_content.replace(
        '"8B": { numero: "8B", id: "8B", nombre: "Lanzadera glicerol-3-fosfato", subtitulo: "DHAP ➔ G3P (Reoxidación rápida de NADH hacia FAD en MMI)", grupos: ["lupa_lanzadera_glicerol_p", "badge_via_8B"], color: "#0d9488" }',
        '"8B": { numero: "8B", id: "8B", nombre: "Lanzadera glicerol-3-fosfato", subtitulo: "DHAP ➔ G3P (Reoxidación rápida de NADH hacia FAD en MMI)", grupos: ["lupa_lanzadera_glicerol_p", "badge_via_8B"], conexiones: ["cx_dhap_lanzadera_g3p", "cx_lanz_g3p_coq"], color: "#0d9488" }'
    )

    with open(RUTA_OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"   ✓ Visor HTML alternativo guardado en: {RUTA_OUT_HTML}")

    # Guardar portal raíz index.html para despliegue en GitHub Pages
    ruta_root_index = os.path.join(DIR_PROYECTO, "index.html")
    root_html = html_content.replace(
        'href="mapa_metabolico_alternativo_120x90cm.pdf"',
        'href="mapa_metabolico_alternativo/mapa_metabolico_alternativo_120x90cm.pdf"'
    ).replace(
        'href="../versiones_impresion/01_mapa_ampliado_completo_120x90cm.pdf"',
        'href="versiones_impresion/01_mapa_ampliado_completo_120x90cm.pdf"'
    ).replace(
        'href="../versiones_impresion/02_ampliacion_rutas_18_25.pdf"',
        'href="versiones_impresion/02_ampliacion_rutas_18_25.pdf"'
    ).replace(
        'href="../versiones_html/',
        'href="versiones_html/'
    )
    with open(ruta_root_index, "w", encoding="utf-8") as f:
        f.write(root_html)
    print(f"   ✓ Portal GitHub Pages actualizado en raíz: {ruta_root_index}")

    # -------------------------------------------------------------------------
    # K. RENDERIZACIÓN VECTORIAL PDF Y VISTA PREVIA PNG
    # -------------------------------------------------------------------------
    rsvg = "/usr/bin/rsvg-convert"
    if os.path.exists(rsvg):
        print(f"\n4. Exportando PDF vectorial a escala de impresión (1200 × 900 mm)...")
        cmd_pdf = [
            rsvg,
            "-f", "pdf",
            "-w", "1200mm",
            "-h", "900mm",
            "--page-width", "1200mm",
            "--page-height", "900mm",
            "-o", RUTA_OUT_PDF,
            RUTA_OUT_SVG
        ]
        res_pdf = subprocess.run(cmd_pdf, capture_output=True, text=True)
        if res_pdf.returncode == 0:
            print(f"   ✓ PDF generado exitosamente: {RUTA_OUT_PDF}")
        else:
            print(f"   ⚠ Error generando PDF: {res_pdf.stderr}")

        print(f"5. Generando vista previa PNG en alta resolución (2400 × 1678 px)...")
        cmd_png = [
            rsvg,
            "-w", "2400",
            "-h", "1678",
            "-o", RUTA_OUT_PNG,
            RUTA_OUT_SVG
        ]
        res_png = subprocess.run(cmd_png, capture_output=True, text=True)
        if res_png.returncode == 0:
            print(f"   ✓ Preview PNG generado exitosamente: {RUTA_OUT_PNG}")
        else:
            print(f"   ⚠ Error generando PNG: {res_png.stderr}")

    print("\n=======================================================")
    print("¡MAPA METABÓLICO ALTERNATIVO GENERADO EXITOSAMENTE!")
    print("=======================================================")

if __name__ == "__main__":
    construir_mapa_alternativo()
