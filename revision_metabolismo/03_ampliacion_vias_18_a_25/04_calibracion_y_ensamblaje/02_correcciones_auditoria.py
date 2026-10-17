#!/usr/bin/env python3
"""
correcciones_mapa.py
====================
Módulo de posprocesamiento y calibración bioquímica de precisión para el SVG
del Mapa Metabólico Integrado Ampliado (25 vías).

Aplica las correcciones científicas y de diseño validadas en la auditoría:
 1. Marcador #inhibitionT en <defs>.
 2. Deduplicación de IDs (rx_pah, marcadores de flechas en defs).
 3. Corrección biológica de transporte: GLUT-2 en hepatocito central (en lugar de GLUT-4).
 4. Mejora de contraste de protones H⁺ en Cadena Respiratoria (ratio WCAG > 7:1).
 5. Margen de seguridad editorial en imprenta para Fosfatidilcolina (PC).
 6. Resolución de solapamientos tipográficos en Lupa PDH.
 7. Conversión de bandas de estriación muscular a líneas vectoriales limpias.
 8. Bifurcación real en 'Y' de la Aldolasa hacia DHAP y GAP.
 9. Despeje de conexiones UMP ➔ CTP y dTMP sin solapamientos.
10. Reruteo del colector lipolítico en tejido adiposo por el canal lateral izquierdo.
11. Conexión de flechas de flujo metabólico vertical directamente a los metabolitos destino.
12. Incorporación de códigos numéricos EC oficiales en reacciones troncales.
"""

import re


def aplicar_correcciones_mapa(svg: str) -> str:
    """Aplica el lote completo de correcciones al código fuente SVG."""
    # -------------------------------------------------------------------------
    # 1. MARCADOR INHIBITION-T EN <defs>
    # -------------------------------------------------------------------------
    marcador_inhibition = """
      <marker id="inhibitionT" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
        <line x1="4" y1="0" x2="4" y2="8" stroke="#dc2626" stroke-width="2.4"/>
      </marker>
    """
    if 'id="inhibitionT"' not in svg:
        svg = svg.replace("</defs>", marcador_inhibition + "\n    </defs>", 1)

    # -------------------------------------------------------------------------
    # 2. DESDUPLICAR IDS
    # -------------------------------------------------------------------------
    patron_rx_pah_2 = r'(<g id="rx_pah" class="reaccion-paso" transform="translate\(6020, 4005\)">)'
    svg = re.sub(patron_rx_pah_2, r'<g id="rx_pah_biosintesis_tyr" class="reaccion-paso" transform="translate(6020, 4005)">', svg)

    def deduplicar_marker(svg_str, marker_name):
        ocurrencias = [m.start() for m in re.finditer(f'id="{marker_name}"', svg_str)]
        if len(ocurrencias) > 1:
            segunda = ocurrencias[1]
            svg_str = svg_str[:segunda] + f'id="{marker_name}_secundario"' + svg_str[segunda + len(f'id="{marker_name}"'):]
        return svg_str

    svg = deduplicar_marker(svg, "arrowTeal")
    svg = deduplicar_marker(svg, "arrowSlate")
    svg = deduplicar_marker(svg, "arrowAmber")

    # -------------------------------------------------------------------------
    # 3. CORRECCIÓN BIOLÓGICA: GLUT-2 EN HEPATOCITO
    # -------------------------------------------------------------------------
    svg = svg.replace(
        '<!-- Canal Transportador GLUT-4 (alineado con la Glucólisis en X=1680) -->\n    <g transform="translate(1640, 80)">',
        '<!-- Canal Transportador GLUT-2 (alineado con la Glucólisis en X=1680) -->\n    <g transform="translate(1640, 80)">'
    )
    svg = svg.replace(
        '<text x="40" y="52" fill="#0369a1" font-size="11" font-weight="900" font-family="\'JetBrains Mono\', monospace" text-anchor="middle">GLUT-4</text>',
        '<text x="40" y="52" fill="#0369a1" font-size="11" font-weight="900" font-family="\'JetBrains Mono\', monospace" text-anchor="middle">GLUT-2</text>'
    )
    svg = svg.replace(
        '<line x1="1680" y1="135" x2="1680" y2="152" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>',
        '<line x1="1680" y1="135" x2="1680" y2="178" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>'
    )

    # -------------------------------------------------------------------------
    # 4. CONTRASTE DE PROTONES H+ EN LUPA CADENA RESPIRATORIA
    # -------------------------------------------------------------------------
    def oscurecer_protones(match):
        texto = match.group(0)
        return texto.replace('fill="#ea580c"', 'fill="#9a3412"')

    patron_protones = r'<text x="[^"]+" y="(?:170|225|280)" font-family="\'Inter\', sans-serif" font-size="10" font-weight="900" fill="#ea580c">H⁺</text>'
    svg, _ = re.subn(patron_protones, oscurecer_protones, svg)

    # -------------------------------------------------------------------------
    # 5. MARGEN DE SEGURIDAD EN IMPRENTA: FOSFATIDILCOLINA (PC)
    # -------------------------------------------------------------------------
    svg = svg.replace(
        '<g id="m_der_pc_membrana" class="nodo-metabolito-libre" transform="translate(6220, 2120)">',
        '<g id="m_der_pc_membrana" class="nodo-metabolito-libre" transform="translate(6160, 2120)">'
    )
    svg = svg.replace(
        '<path d="M 40 0 C 70 40, 100 70, 100 100" fill="none" stroke="#0284c7" stroke-width="3" marker-end="url(#arrowBlue)"/>',
        '<path d="M 40 0 C 60 35, 75 65, 75 100" fill="none" stroke="#0284c7" stroke-width="3" marker-end="url(#arrowBlue)"/>'
    )

    # -------------------------------------------------------------------------
    # 6. SOLAPAMIENTOS DE TEXTO EN LUPA PDH
    # -------------------------------------------------------------------------
    svg = svg.replace(
        '<text x="0" y="13" fill="#334155" font-size="8.5" font-family="\'Inter\', sans-serif">• Carencia B₁ ➔ Agota TPP ➔ <tspan font-weight="700">Beriberi</tspan> y <tspan font-weight="700">Wernicke-Korsakoff</tspan></text>',
        '<text x="0" y="13" fill="#334155" font-size="8.5" font-family="\'Inter\', sans-serif">• Carencia B₁ ➔ Agota TPP ➔ Beriberi y Wernicke-Korsakoff</text>'
    )
    svg = svg.replace(
        '<text x="85" y="10" fill="#334155" font-size="9.5" font-family="\'Inter\', sans-serif">Inhibida por <tspan font-weight="800" fill="#b91c1c">Acetil-CoA</tspan> (competitivo)</text>',
        '<text x="85" y="10" fill="#334155" font-size="9.5" font-family="\'Inter\', sans-serif">Inhibida por Acetil-CoA (competitivo)</text>'
    )
    svg = svg.replace(
        '<text x="85" y="10" fill="#334155" font-size="9.5" font-family="\'Inter\', sans-serif">Inhibida por cociente elevado <tspan font-weight="800" fill="#b91c1c">NADH/NAD⁺</tspan></text>',
        '<text x="85" y="10" fill="#334155" font-size="9.5" font-family="\'Inter\', sans-serif">Inhibida por cociente elevado NADH/NAD⁺</text>'
    )
    svg = svg.replace(
        '<text x="184" y="349" fill="#059669" font-size="9.5" font-weight="900" font-family="\'Inter\', sans-serif">+ NADH + H⁺ <tspan fill="#64748b" font-size="8.5">(vía FAD ➔ FADH₂)</tspan></text>',
        '<text x="184" y="349" fill="#059669" font-size="9.5" font-weight="900" font-family="\'Inter\', sans-serif">+ NADH + H⁺ (vía FAD ➔ FADH₂)</text>'
    )

    # -------------------------------------------------------------------------
    # 7. ESTRIACIONES DEL MÚSCULO ESQUELÉTICO (EVITAR FALSOS DESBORDES)
    # -------------------------------------------------------------------------
    def rect_a_linea_estriacion(match):
        x = float(match.group(1))
        y = float(match.group(2))
        w = float(match.group(3))
        h = float(match.group(4))
        xc = x + w / 2
        return f'<line x1="{xc:.1f}" y1="{y:.1f}" x2="{xc:.1f}" y2="{y+h:.1f}" stroke="#be123c" stroke-width="{w:.1f}" stroke-linecap="round" opacity="0.055"/>'

    patron_estriacion = r'<rect x="(\d+)" y="(\d+)" width="(\d+)" height="(\d+)" rx="3" fill="#be123c" opacity="0\.055"/>'
    svg, _ = re.subn(patron_estriacion, rect_a_linea_estriacion, svg)

    # -------------------------------------------------------------------------
    # 8. BIFURCACIÓN REAL DE LA ALDOLASA (GLUCÓLISIS)
    # -------------------------------------------------------------------------
    bloque_aldolasa_anterior = """    <!-- Reacción: Aldolasa -->
    <g id="rx_aldo" data-arrastrable="1" transform="translate(1680, 790)">
      
        <line x1="-3" y1="0" x2="-3" y2="52" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        <line x1="3" y1="52" x2="3" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        
      
      <text x="14" y="30" fill="#0f172a" font-size="12" font-weight="700" font-family="'Inter', sans-serif" >Aldolasa</text>
    </g>"""

    bloque_aldolasa_nuevo = """    <!-- Reacción: Aldolasa con Bifurcación en Y hacia DHAP y GAP -->
    <g id="rx_aldo" data-arrastrable="1" transform="translate(1680, 790)">
      <!-- Tronco vertical desde F-1,6-BP -->
      <line x1="0" y1="0" x2="0" y2="18" stroke="#ea580c" stroke-width="2.4"/>
      <!-- Rama Izquierda hacia DHAP (termina arriba del título Dihidroxiacetona-P) -->
      <path d="M 0 18 Q -65 20 -130 25" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <!-- Rama Derecha hacia GAP -->
      <path d="M 0 18 Q 75 22 145 42" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <!-- Retorno gluconeogénico (condensación aldólica) -->
      <path d="M -125 19 Q -60 13 -6 10" fill="none" stroke="#7c3aed" stroke-width="1.8" stroke-dasharray="4 2" marker-end="url(#arrowFlow)"/>
      <path d="M 140 34 Q 70 16 6 10" fill="none" stroke="#7c3aed" stroke-width="1.8" stroke-dasharray="4 2" marker-end="url(#arrowFlow)"/>
      <!-- Rótulo y EC debajo de la horquilla (sin tocar las ramas) -->
      <text x="0" y="48" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Aldolasa</text>
      <text x="0" y="60" fill="#64748b" font-size="8" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 4.1.2.13</text>
    </g>"""

    if bloque_aldolasa_anterior in svg:
        svg = svg.replace(bloque_aldolasa_anterior, bloque_aldolasa_nuevo)

    # -------------------------------------------------------------------------
    # 9. DESPEJE DE UMP: CONEXIONES A CTP Y dTMP SIN CORTAR ESTRUCTURAS
    # -------------------------------------------------------------------------
    svg = svg.replace(
        '<path d="M 5083 1548 Q 5069 1562 5060 1575" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>',
        '<path d="M 5055 1555 Q 5035 1568 5015 1582" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>'
    )
    svg = svg.replace(
        '<text x="5050" y="1552" fill="#0f172a" font-size="10" font-weight="700" font-family="\'Inter\', sans-serif" text-anchor="end">CTP Sintetasa (+Gln, -ATP)</text>',
        '<text x="5030" y="1558" fill="#0f172a" font-size="9" font-weight="800" font-family="\'Inter\', sans-serif" text-anchor="end">CTP Sintetasa (EC 6.3.4.2)</text>'
    )

    # -------------------------------------------------------------------------
    # 10. CASCADA LIPOLÍTICA EN ADIPOCITO: REUBICAR COLECTOR DE 3 AG
    # -------------------------------------------------------------------------
    bloque_colector_anterior = """      <!-- Convergencia de los 3 cortes enzimáticos (ATGL, HSL, MGL) hacia el Pool con flechas punteadas -->
      <path d="M -580 1590 C -450 1590, -360 1700, -280 1700" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>
      <path d="M -580 1810 C -450 1810, -360 1726, -280 1726" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>
      <path d="M -580 2030 C -450 2030, -360 1750, -280 1750" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>"""

    bloque_colector_nuevo = """      <!-- Colector lateral limpio por el canal izquierdo y cruce horizontal en Y=1638 (0 solapamientos) -->
      <!-- Entrada 1 (ATGL): nace a la izquierda de «+ 1º AG libre» (X=-666) hacia el canal X=-680 -->
      <path d="M -666 1590 L -680 1590" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <!-- Entrada 2 (HSL): nace a la izquierda de «+ 2º AG libre» (X=-666) hacia el canal X=-680 -->
      <path d="M -666 1810 L -680 1810" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <!-- Entrada 3 (MGL): nace a la izquierda de «+ 3º AG libre» (X=-666) hacia el canal X=-680 -->
      <path d="M -666 2030 L -680 2030" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <!-- Tronco colector vertical por X=-680 (de MGL a ATGL) y cruce libre en Y=1638 hacia el borde superior del Pool -->
      <path d="M -680 2030 L -680 1590 M -680 1638 L -199 1638 Q -185 1638 -185 1652 L -185 1680" fill="none" stroke="#ea580c" stroke-width="2.4" stroke-dasharray="7 4" marker-end="url(#arrowOrange)"/>
      <text x="-692" y="1820" fill="#059669" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle" transform="rotate(-90 -692 1820)">Canal Colector de Ácidos Grasos Libres (1º, 2º y 3º AG)</text>"""

    if bloque_colector_anterior in svg:
        svg = svg.replace(bloque_colector_anterior, bloque_colector_nuevo)

    # -------------------------------------------------------------------------
    # 11. EXTENSIÓN DE FLECHAS CORTAS (FLECHAS QUE CAÍAN EN EL VACÍO)
    # -------------------------------------------------------------------------
    # Acil-CoA Sintetasa (rx_acs): extender la flecha hasta Palmitoil-CoA (Citosólico)
    svg = svg.replace(
        '<g id="rx_acs" data-arrastrable="1" transform="translate(240, 1140)">\n      <line x1="0" y1="0" x2="0" y2="50"',
        '<g id="rx_acs" data-arrastrable="1" transform="translate(240, 1140)">\n      <line x1="0" y1="0" x2="0" y2="280"'
    )
    svg = svg.replace(
        '<g id="rx_hk" data-arrastrable="1" transform="translate(1680, 265)">\n      <line x1="0" y1="0" x2="0" y2="52"',
        '<g id="rx_hk" data-arrastrable="1" transform="translate(1680, 265)">\n      <line x1="0" y1="0" x2="0" y2="70"'
    )
    svg = svg.replace(
        '<g id="rx_pfk1" data-arrastrable="1" transform="translate(1680, 615)">\n      <line x1="0" y1="0" x2="0" y2="52"',
        '<g id="rx_pfk1" data-arrastrable="1" transform="translate(1680, 615)">\n      <line x1="0" y1="0" x2="0" y2="70"'
    )
    svg = svg.replace(
        '<g id="rx_pk" data-arrastrable="1" transform="translate(1900, 1665)">\n      <line x1="0" y1="0" x2="0" y2="52"',
        '<g id="rx_pk" data-arrastrable="1" transform="translate(1900, 1665)">\n      <line x1="0" y1="0" x2="0" y2="70"'
    )
    svg = svg.replace(
        '<g id="rx_gpat" class="reaccion-paso" transform="translate(6020, 1350)">\n      <line x1="0" y1="0" x2="0" y2="70"',
        '<g id="rx_gpat" class="reaccion-paso" transform="translate(6020, 1350)">\n      <line x1="0" y1="0" x2="0" y2="95"'
    )
    svg = svg.replace(
        '<g id="rx_agpat" class="reaccion-paso" transform="translate(6020, 1570)">\n      <line x1="0" y1="0" x2="0" y2="70"',
        '<g id="rx_agpat" class="reaccion-paso" transform="translate(6020, 1570)">\n      <line x1="0" y1="0" x2="0" y2="95"'
    )
    svg = svg.replace(
        '<g id="rx_pap" class="reaccion-paso" transform="translate(6020, 1790)">\n      <line x1="0" y1="0" x2="0" y2="70"',
        '<g id="rx_pap" class="reaccion-paso" transform="translate(6020, 1790)">\n      <line x1="0" y1="0" x2="0" y2="95"'
    )
    svg = re.sub(
        r'(<g id="rx_col\d" class="reaccion-paso"[^>]*>\s*<line x1="0" y1="0" x2="0" y2=")70(")',
        r'\g<1>95\2',
        svg
    )
    svg = re.sub(
        r'(<g id="rx_fas\w*" class="reaccion-paso"[^>]*>\s*<line x1="0" y1="0" x2="0" y2=")70(")',
        r'\g<1>95\2',
        svg
    )

    # -------------------------------------------------------------------------
    # 12. CÓDIGOS EC EN GLUCÓLISIS Y KREBS
    # -------------------------------------------------------------------------
    svg = svg.replace(
        '<text x="14" y="30" fill="#0f172a" font-size="12" font-weight="700" font-family="\'Inter\', sans-serif" >Hexocinasa</text>',
        '<text x="14" y="24" fill="#0f172a" font-size="11.5" font-weight="800" font-family="\'Inter\', sans-serif">Hexocinasa</text>\n      <text x="14" y="36" fill="#64748b" font-size="8.5" font-family="\'JetBrains Mono\', monospace">EC 2.7.1.1</text>'
    )
    svg = svg.replace(
        '<text x="14" y="30" fill="#0f172a" font-size="12" font-weight="700" font-family="\'Inter\', sans-serif" >Fosfoglucosa Isomerasa</text>',
        '<text x="14" y="24" fill="#0f172a" font-size="11.5" font-weight="800" font-family="\'Inter\', sans-serif">Fosfoglucosa Isomerasa</text>\n      <text x="14" y="36" fill="#64748b" font-size="8.5" font-family="\'JetBrains Mono\', monospace">EC 5.3.1.9</text>'
    )
    svg = svg.replace(
        '<text x="14" y="30" fill="#0f172a" font-size="12" font-weight="700" font-family="\'Inter\', sans-serif" >Fosfofructocinasa-1</text>',
        '<text x="14" y="24" fill="#0f172a" font-size="11.5" font-weight="800" font-family="\'Inter\', sans-serif">PFK-1</text>\n      <text x="14" y="36" fill="#64748b" font-size="8.5" font-family="\'JetBrains Mono\', monospace">EC 2.7.1.11</text>'
    )
    svg = svg.replace(
        '<text x="14" y="26" fill="#0f172a" font-size="12" font-weight="700" font-family="\'Inter\', sans-serif" >GAPDH</text>',
        '<text x="14" y="22" fill="#0f172a" font-size="11.5" font-weight="800" font-family="\'Inter\', sans-serif">GAPDH</text>\n      <text x="14" y="34" fill="#64748b" font-size="8.5" font-family="\'JetBrains Mono\', monospace">EC 1.2.1.12</text>'
    )
    svg = svg.replace(
        '<text x="14" y="30" fill="#0f172a" font-size="12" font-weight="700" font-family="\'Inter\', sans-serif" >Piruvato Cinasa</text>',
        '<text x="14" y="24" fill="#0f172a" font-size="11.5" font-weight="800" font-family="\'Inter\', sans-serif">Piruvato Cinasa</text>\n      <text x="14" y="36" fill="#64748b" font-size="8.5" font-family="\'JetBrains Mono\', monospace">EC 2.7.1.40</text>'
    )
    svg = svg.replace(
        '<text x="14" y="30" fill="#0f172a" font-size="12" font-weight="700" font-family="\'Inter\', sans-serif" >Citrato Sintasa</text>',
        '<text x="14" y="24" fill="#0f172a" font-size="11.5" font-weight="800" font-family="\'Inter\', sans-serif">Citrato Sintasa</text>\n      <text x="14" y="36" fill="#64748b" font-size="8.5" font-family="\'JetBrains Mono\', monospace">EC 2.3.3.1</text>'
    )

    # -------------------------------------------------------------------------
    # 13. UNIFICACIÓN BIOQUÍMICA DE COENZIMA A LIBRE (CoA-SH) EN REACCIONES
    # -------------------------------------------------------------------------
    # Complejo α-Cetoglutarato Deshidrogenasa (rx_akgdh)
    svg = svg.replace(">+ CoA + NAD⁺</text>", ">+ CoA-SH + NAD⁺</text>")
    # Succinil-CoA Sintetasa (rx_scas)
    svg = svg.replace(">+ GTP (+CoA)</text>", ">+ GTP (+CoA-SH)</text>")
    # ATP Citrato Liasa (rx_acly) y Acil-CoA Sintetasa (rx_acs)
    svg = svg.replace(">+ ATP + CoA</text>", ">+ ATP + CoA-SH</text>")
    # HMG-CoA Reductasa (rx_hmgcr), CPT-2 (rx_cpt2) y Tiolasa β-oxidación (rx_box3)
    svg = svg.replace(">+ CoA</text>", ">+ CoA-SH</text>")
    # CPT-1 Lanzadera de Carnitina (rx_cpt1)
    svg = svg.replace(">- CoA</text>", ">- CoA-SH</text>")
    # GPAT y AGPAT en Biosíntesis de TAG (Vía 23)
    svg = svg.replace(">+ CoASH</text>", ">+ CoA-SH</text>")
    # Complejo BCKDH (rx_bckdh)
    svg = svg.replace(
        ">Cofactores: TPP, Lipoamida, FAD</text>",
        ">Cofactores: TPP, Lipoamida, CoA-SH, FAD, NAD⁺</text>"
    )
    # HMG-CoA Sintasa Citosólica (rx_hmgs_cito): añadir salida de - CoA-SH
    bloque_hmgs_cito_ant = """    <g id="rx_hmgs_cito" data-arrastrable="1" transform="translate(3620, 585)">
      <line x1="0" y1="0" x2="0" y2="45" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
        <path d="M -65 6 Q -20 6 -4 16" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
        <text x="-70" y="9" fill="#dc2626" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ Acetil-CoA</text>
        
      <text x="14" y="26" fill="#0f172a" font-size="12" font-weight="700" font-family="'Inter', sans-serif" >HMG-CoA Sintasa (Citosólica)</text>
    </g>"""
    bloque_hmgs_cito_nvo = """    <g id="rx_hmgs_cito" data-arrastrable="1" transform="translate(3620, 585)">
      <line x1="0" y1="0" x2="0" y2="45" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
        <path d="M -65 6 Q -20 6 -4 16" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
        <text x="-70" y="9" fill="#dc2626" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ Acetil-CoA</text>
        
        <path d="M -4 22 Q -20 32 -65 32" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
        <text x="-70" y="36" fill="#475569" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">- CoA-SH</text>
        
      <text x="14" y="26" fill="#0f172a" font-size="12" font-weight="700" font-family="'Inter', sans-serif" >HMG-CoA Sintasa (Citosólica)</text>
    </g>"""
    svg = svg.replace(bloque_hmgs_cito_ant, bloque_hmgs_cito_nvo)

    # HMG-CoA Sintasa 2 Mitocondrial (rx_ceto1): añadir salida de - CoA-SH
    bloque_ceto1_ant = """    <g id="rx_ceto1" data-arrastrable="1" transform="translate(630, 2930)">
      <line x1="0" y1="0" x2="0" y2="40" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
        <path d="M -65 6 Q -20 6 -4 16" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
        <text x="-70" y="9" fill="#dc2626" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ Acetil-CoA</text>
        
      <text x="14" y="24" fill="#0f172a" font-size="12" font-weight="700" font-family="'Inter', sans-serif" >HMG-CoA Sintasa 2 (HMGCS2)</text>
    </g>"""
    bloque_ceto1_nvo = """    <g id="rx_ceto1" data-arrastrable="1" transform="translate(630, 2930)">
      <line x1="0" y1="0" x2="0" y2="40" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
        <path d="M -65 6 Q -20 6 -4 16" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
        <text x="-70" y="9" fill="#dc2626" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ Acetil-CoA</text>
        
        <path d="M -4 22 Q -20 32 -65 32" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
        <text x="-70" y="36" fill="#475569" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">- CoA-SH</text>
        
      <text x="14" y="24" fill="#0f172a" font-size="12" font-weight="700" font-family="'Inter', sans-serif" >HMG-CoA Sintasa 2 (HMGCS2)</text>
    </g>"""
    svg = svg.replace(bloque_ceto1_ant, bloque_ceto1_nvo)

    # -------------------------------------------------------------------------
    # 14. ANCLAJE EXACTO DE FLECHAS PUNTEADAS DE L-MALATO (LUPA LANZADERA ➔ KREBS)
    # -------------------------------------------------------------------------
    # 14a. Origen de cx_lanz_malato_krebs: nace directamente bajo L-Malato (Matriz) dentro de la lupa (1256, 2065)
    #      y baja por X=654 hasta Y=2726 para pasar limpiamente por debajo de la Lupa de Carnitina
    tramo_ini_malato_ant = (
        "M 774.0 2532.5 L 774.0 2541.5 Q 774.0 2550.0 768.0 2556.0 L 768.0 2556.0 "
        "Q 762.0 2562.0 753.5 2562.0 L 694.0 2562.0 Q 678.0 2562.0 666.7 2550.7 "
        "L 665.3 2549.3 Q 654.0 2538.0 654.0 2522.0 L 654.0 2474.5 Q 654.0 2466.0 "
        "648.0 2460.0 L 648.0 2460.0 Q 642.0 2454.0 633.5 2454.0 L 250.0 2454.0 "
        "Q 234.0 2454.0 222.7 2465.3 L 53.3 2634.7 Q 42.0 2646.0 42.0 2662.0"
    )
    tramo_ini_malato_nvo = (
        "M 1256.0 2065.0 L 1256.0 2214.0 Q 1256.0 2228.0 1242.0 2228.0 "
        "L 668.0 2228.0 Q 654.0 2228.0 654.0 2242.0 L 654.0 2648.0 "
        "Q 654.0 2662.0 640.0 2662.0 L 526.0 2662.0 Q 512.0 2662.0 512.0 2676.0 "
        "L 512.0 2696.0 Q 512.0 2710.0 498.0 2710.0 L 56.0 2710.0 Q 42.0 2710.0 42.0 2724.0"
    )
    svg = svg.replace(tramo_ini_malato_ant, tramo_ini_malato_nvo)

    # 14b. Destino de cx_lanz_malato_krebs: apunta directamente a la molécula de L-Malato en Krebs (1218, 3886)
    tramo_fin_malato_ant = (
        "L 1305.5 3990.0 Q 1314.0 3990.0 1320.0 3984.0 L 1320.0 3984.0 "
        "Q 1326.0 3978.0 1326.0 3969.5 L 1326.0 3932.6"
    )
    tramo_fin_malato_nvo = (
        "L 1290.0 3990.0 Q 1304.0 3990.0 1304.0 3976.0 L 1304.0 3900.0 "
        "Q 1304.0 3886.0 1290.0 3886.0 L 1218.0 3886.0"
    )
    svg = svg.replace(tramo_fin_malato_ant, tramo_fin_malato_nvo)

    # 14c. Origen de cx_lanz_malato_cte_comp1: nace justo bajo el transportador OGC en la MMI (Y=2492)
    svg = svg.replace("M 1278.0 2532.5 L 1278.0 2553.5", "M 1278.0 2492.0 L 1278.0 2553.5")

    # 14d. Origen de cx_krebs_mdh_cte: nace justo debajo de L-Malato [4C] (Y=3864) en vez de flotar en Y=3929.6
    svg = svg.replace("M 1350.0 3929.6 L 1350.0 4430.0", "M 1350.0 3864.0 L 1350.0 4430.0")

    # -------------------------------------------------------------------------
    # 15. LUPA DE LANZADERA DE CARNITINA (3 BANDAS: MME · INTERMEMBRANA · MMI)
    #     + CORRECCIÓN DE TEXTO PALMITOIL-CARNITINA Y DESPEJE DE FLECHAS A*
    # -------------------------------------------------------------------------
    bloque_carnitina_ant = """    <!-- Reacción: CPT-1 (Lanzadera de Carnitina) -->
    <g id="rx_cpt1" data-arrastrable="1" transform="translate(240, 1540)">
      <line x1="0" y1="0" x2="0" y2="50" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
        <path d="M -65 6 Q -20 6 -4 16" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
        <text x="-70" y="9" fill="#dc2626" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ Carnitina</text>
        
        <path d="M -4 22 Q -20 32 -65 32" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
        <text x="-70" y="36" fill="#475569" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">- CoA-SH</text>
        
      <text x="14" y="29" fill="#0f172a" font-size="12" font-weight="700" font-family="'Inter', sans-serif" >CPT-1 (Lanzadera de Carnitina)</text>
    </g>
    
    <g class="etiqueta-regulacion" transform="translate(440, 1550)">
      <text x="0" y="0" fill="#dc2626" font-size="9" font-weight="800" font-family="'Inter', sans-serif" >(-) Malonil-CoA</text><text x="0" y="12" fill="#0284c7" font-size="9" font-weight="800" font-family="'Inter', sans-serif" >[Hormonal] Paso limitante · Glucagón ↑ (indirecto)</text>
    </g>
    
    <!-- Metabolito Libre: Palmitoil-Carnitina -->
    <g id="m_palm_carnitina" data-arrastrable="1" transform="translate(180, 1980)">
      <g>
<g class="mol-palmitoil-carnitina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Amonio cuaternario -->
  <text x="32" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0284c7" stroke="none" text-anchor="end">(CH₃)₃N⁺</text>
  <line x1="36" y1="20" x2="46" y2="20" />
  <text x="55" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- C3 con enlace éster a palmitato explícito -->
  <line x1="64" y1="24" x2="70" y2="30" />
  <text x="76" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="76" y1="41" x2="76" y2="49" stroke="#dc2626" stroke-width="2"/>
  <text x="76" y="59" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  
  <!-- Enlace éster hacia acilo -->
  <line x1="76" y1="62" x2="76" y2="70" />
  <text x="76" y="80" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="69" y1="74" x2="58" y2="74" stroke="#dc2626" stroke-width="1.8"/>
  <line x1="69" y1="78" x2="58" y2="78" stroke="#dc2626" stroke-width="1.8"/>
  <text x="54" y="80" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <line x1="83" y1="78" x2="92" y2="83" />
  <text x="95" y="87" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#64748b" stroke="none">(CH₂)₁₄CH₃</text>

  <!-- C2 metileno y C1 carboxilato -->
  <line x1="84" y1="30" x2="90" y2="24" />
  <text x="100" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="110" y1="20" x2="118" y2="20" />
  <text x="122" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
</g>
      <text x="145" y="24" fill="#0f172a" font-size="15" font-weight="800" font-family="'Inter', sans-serif" >Palmitoil-Carnitina</text>
      <text x="145" y="41" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace" >[16C]</text>
      
    </g>
    
    <!-- Lanzadera de Carnitina: Transportador CACT en la MMI -->
    <g id="transportador_cact" data-arrastrable="1" transform="translate(192, 2285)">
      <rect x="0" y="0" width="96" height="40" rx="10" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
      <text x="48" y="18" fill="#ffffff" font-size="12.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" stroke="none">CACT</text>
      <text x="48" y="32" fill="#e0f2fe" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle" stroke="none">Antipuerto MMI</text>
    </g>
    
    <!-- Reacción: CPT-2 (Cara Interna MMI) -->
    <g id="rx_cpt2" data-arrastrable="1" transform="translate(240, 2330)">
      <line x1="0" y1="0" x2="0" y2="40" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
        <path d="M -65 6 Q -20 6 -4 16" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
        <text x="-70" y="9" fill="#dc2626" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ CoA-SH</text>
        
        <path d="M -4 22 Q -20 32 -65 32" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
        <text x="-70" y="36" fill="#475569" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">- Carnitina</text>
        
      <text x="14" y="24" fill="#0f172a" font-size="12" font-weight="700" font-family="'Inter', sans-serif" >CPT-2 (Cara Interna MMI)</text>
    </g>"""

    bloque_carnitina_nvo = """    <!-- LUPA TÉCNICA: LANZADERA DE CARNITINA (CPT-1 · CACT · CPT-2) -->
    <g id="lupa_lanzadera_carnitina" data-arrastrable="1">
      <defs>
        <clipPath id="clipLupaCarnitina">
          <rect x="108" y="1556" width="364" height="784" rx="18"/>
        </clipPath>
      </defs>

      <!-- Cuerpo y Bisel del Panel Técnico -->
      <rect x="108" y="1556" width="364" height="784" rx="18" fill="#ffffff" stroke="#0284c7" stroke-width="2.5"/>

      <g clip-path="url(#clipLupaCarnitina)">
        <!-- 1. Banda Superior: Citosol y Bicapa Externa (MME) -->
        <rect x="104" y="1556" width="372" height="90" fill="#f0fdf4"/>
        <!-- Encabezado de la Lupa -->
        <rect x="104" y="1556" width="372" height="34" fill="#0f172a"/>
        <text x="290" y="1577" fill="#ffffff" font-size="10" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="0.5">LANZADERA DE CARNITINA (CPT-1 · CACT · CPT-2)</text>
        <text x="460" y="1608" fill="#15803d" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="end">CITOSOL</text>

        <!-- Bicapa MME -->
        <rect x="104" y="1646" width="372" height="40" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.2"/>
        <text x="118" y="1670" fill="#0369a1" font-size="8.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="start">MME (EXTERNA)</text>
        <g fill="#0284c7" opacity="0.55">
          <circle cx="202" cy="1652" r="2.5"/><circle cx="214" cy="1652" r="2.5"/>
          <circle cx="202" cy="1680" r="2.5"/><circle cx="214" cy="1680" r="2.5"/>
          <circle cx="442" cy="1652" r="2.5"/><circle cx="454" cy="1652" r="2.5"/>
          <circle cx="442" cy="1680" r="2.5"/><circle cx="454" cy="1680" r="2.5"/>
        </g>

        <!-- Complejo CPT-1 en la MME -->
        <g id="rx_cpt1" transform="translate(278, 1642)">
          <rect x="-52" y="0" width="104" height="48" rx="10" fill="#ea580c" stroke="#c2410c" stroke-width="2.2"/>
          <text x="0" y="19" fill="#ffffff" font-size="12" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CPT-1</text>
          <text x="0" y="34" fill="#ffedd5" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">EC 2.3.1.21 · MME</text>
          <!-- Salida de - SH-CoA hacia el citosol -->
          <path d="M 34 -2 Q 56 -18 86 -18" fill="none" stroke="#475569" stroke-width="1.9" marker-end="url(#arrowGreen)"/>
          <text x="92" y="-14" fill="#475569" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="start">- SH-CoA</text>
        </g>

        <!-- Regulación Alostérica y Hormonal sobre CPT-1 -->
        <g class="etiqueta-regulacion" transform="translate(338, 1705)">
          <line x1="-6" y1="-22" x2="0" y2="-28" stroke="#dc2626" stroke-width="2.2"/>
          <text x="0" y="0" fill="#dc2626" font-size="9" font-weight="900" font-family="'Inter', sans-serif">(-) Malonil-CoA</text>
          <text x="0" y="12" fill="#0284c7" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">[Hormonal] Paso limitante</text>
          <text x="0" y="24" fill="#0369a1" font-size="8" font-weight="700" font-family="'Inter', sans-serif">Glucagón ↑ (↓ Malonil-CoA)</text>
        </g>

        <!-- 2. Banda Media: Espacio Intermembrana (Ciclo Antipuerto) -->
        <rect x="104" y="1686" width="372" height="394" fill="#f8fafc" opacity="0.45"/>
        <text x="118" y="1706" fill="#475569" font-size="8.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="start">ESPACIO INTERMEMBRANA</text>

        <!-- Flecha de bajada CPT-1 ➔ Palmitoil-Carnitina -->
        <line x1="278" y1="1690" x2="278" y2="1772" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

        <!-- Metabolito Intermembrana ( Vía Derecha Descendente ): Palmitoil-Carnitina [16C] -->
        <g id="m_palm_carnitina" transform="translate(184, 1782)">
          <g class="mol-palmitoil-carnitina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <text x="32" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0284c7" stroke="none" text-anchor="end">(CH₃)₃N⁺</text>
            <line x1="36" y1="20" x2="46" y2="20" />
            <text x="55" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
            <line x1="64" y1="24" x2="70" y2="30" />
            <text x="76" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
            <line x1="76" y1="41" x2="76" y2="49" stroke="#dc2626" stroke-width="2"/>
            <text x="76" y="59" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
            <line x1="76" y1="62" x2="76" y2="70" />
            <text x="76" y="80" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
            <line x1="69" y1="74" x2="58" y2="74" stroke="#dc2626" stroke-width="1.8"/>
            <line x1="69" y1="78" x2="58" y2="78" stroke="#dc2626" stroke-width="1.8"/>
            <text x="54" y="80" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
            <line x1="83" y1="78" x2="92" y2="83" />
            <text x="95" y="87" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#64748b" stroke="none">(CH₂)₁₄CH₃</text>
            <line x1="84" y1="30" x2="90" y2="24" />
            <text x="100" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
            <line x1="110" y1="20" x2="118" y2="20" />
            <text x="122" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
          </g>
          <!-- Texto desplazado a x=162 para no chocar con COO⁻ (x=122..154) -->
          <text x="162" y="24" fill="#0f172a" font-size="12.5" font-weight="800" font-family="'Inter', sans-serif">Palmitoil-Carnitina</text>
          <text x="162" y="40" fill="#ea580c" font-size="10.5" font-weight="700" font-family="'JetBrains Mono', monospace">[16C] Acil-carnitina</text>
        </g>

        <!-- Flecha de bajada Palmitoil-Carnitina ➔ CACT -->
        <line x1="278" y1="1878" x2="278" y2="2070" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
        <text x="290" y="2050" fill="#c2410c" font-size="9" font-weight="800" font-family="'Inter', sans-serif">Acil-Carnitina ↓</text>

        <!-- Metabolito Intermembrana ( Vía Izquierda Ascendente ): L-Carnitina libre -->
        <g id="m_carnitina_libre" transform="translate(128, 1932) scale(0.90)">
          <g class="mol-carnitina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <text x="32" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0284c7" stroke="none" text-anchor="end">(CH₃)₃N⁺</text>
            <line x1="36" y1="20" x2="46" y2="20" />
            <text x="55" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
            <line x1="64" y1="24" x2="70" y2="30" />
            <text x="76" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
            <line x1="76" y1="41" x2="76" y2="51" stroke="#0284c7" stroke-width="2.1"/>
            <text x="76" y="63" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">OH</text>
            <line x1="84" y1="30" x2="90" y2="24" />
            <text x="100" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
            <line x1="110" y1="20" x2="118" y2="20" />
            <text x="122" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
          </g>
          <text x="76" y="-8" fill="#0369a1" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Carnitina libre</text>
          <text x="76" y="80" fill="#0284c7" font-size="9.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[Retorno a CPT-1]</text>
        </g>

        <!-- Flechas de retorno de L-Carnitina: CACT (182, 2076) ➔ L-Carnitina ➔ CPT-1 (226, 1666) -->
        <path d="M 182 2074 L 182 2012" fill="none" stroke="#0284c7" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowBlue)"/>
        <path d="M 182 1910 L 182 1735 Q 182 1718 196 1718 L 208 1718 Q 220 1718 220 1702 L 220 1676 Q 220 1666 226 1666" fill="none" stroke="#0284c7" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowBlue)"/>
        <text x="172" y="1820" fill="#0284c7" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ L-Carnitina ↑</text>

        <!-- 3. Banda Inferior: Bicapa Interna (MMI con CACT) y Matriz Mitocondrial (CPT-2) -->
        <rect x="104" y="2120" width="372" height="220" fill="#fffbeb"/>
        <rect x="104" y="2080" width="372" height="40" fill="#fed7aa" stroke="#d97706" stroke-width="2.5"/>
        <text x="460" y="2104" fill="#92400e" font-size="8.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="end">MMI (INTERNA)</text>
        <g fill="#d97706" opacity="0.6">
          <circle cx="122" cy="2086" r="2.5"/><circle cx="134" cy="2086" r="2.5"/>
          <circle cx="122" cy="2114" r="2.5"/><circle cx="134" cy="2114" r="2.5"/>
          <circle cx="332" cy="2086" r="2.5"/><circle cx="344" cy="2086" r="2.5"/>
          <circle cx="332" cy="2114" r="2.5"/><circle cx="344" cy="2114" r="2.5"/>
        </g>

        <!-- Transportador CACT en la MMI -->
        <g id="transportador_cact" transform="translate(232, 2076)">
          <rect x="-68" y="0" width="136" height="48" rx="10" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
          <text x="0" y="19" fill="#ffffff" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CACT (SLC25A20)</text>
          <text x="0" y="34" fill="#e0f2fe" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Antipuerto Acil-Carn ⇄ Carn</text>
        </g>

        <text x="460" y="2142" fill="#b45309" font-size="8.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="end">MATRIZ MITOCONDRIAL</text>

        <!-- Flecha CACT ➔ CPT-2 -->
        <line x1="278" y1="2124" x2="278" y2="2184" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

        <!-- Complejo CPT-2 en la Cara Matricial de la MMI -->
        <g id="rx_cpt2" transform="translate(278, 2188)">
          <rect x="-52" y="0" width="104" height="46" rx="10" fill="#ea580c" stroke="#c2410c" stroke-width="2.2"/>
          <text x="0" y="18" fill="#ffffff" font-size="12" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CPT-2</text>
          <text x="0" y="33" fill="#ffedd5" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">EC 2.3.1.21 · Matriz</text>

          <!-- Entrada de + SH-CoA matricial -->
          <path d="M 88 10 Q 66 10 54 18" fill="none" stroke="#dc2626" stroke-width="1.9" marker-end="url(#arrowRed)"/>
          <text x="94" y="14" fill="#dc2626" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="start">+ SH-CoA</text>

          <!-- Liberación de - L-Carnitina hacia CACT (182, 2124) -->
          <path d="M -52 23 L -82 23 Q -96 23 -96 9 L -96 -60" fill="none" stroke="#0284c7" stroke-width="2.2" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
          <text x="-58" y="42" fill="#0369a1" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">- L-Carnitina</text>
        </g>

        <!-- Barra resumen inferior de la Lupa -->
        <rect x="120" y="2302" width="340" height="24" rx="12" fill="#0f172a"/>
        <text x="290" y="2318" fill="#f8fafc" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Translocación neta: Palmitoil-CoA (Citosol) ➔ Palmitoil-CoA (Matriz)</text>
      </g>

      <!-- Flecha de entrada desde Palmitoil-CoA (Citosólico) hacia CPT-1 (dibujada encima del encabezado) -->
      <path d="M 240 1524 L 240 1538 Q 240 1548 252 1548 L 266 1548 Q 278 1548 278 1560 L 278 1638" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

      <!-- Flecha de salida desde CPT-2 hacia Palmitoil-CoA (Matriz) -->
      <path d="M 278 2234 L 278 2270 Q 278 2284 264 2284 L 254 2284 Q 240 2284 240 2298 L 240 2404" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    </g>"""
    svg = svg.replace(bloque_carnitina_ant, bloque_carnitina_nvo)

    # 15b. Despejar las rutas A* laterales y eliminar volteretas en Cuerpos Cetónicos ➔ Sangre
    # - cx_dhap_lanzadera_g3p: mantiene su vertical en X=90 y pasa por encima de la Leyenda (Y=4565)
    tramo_dhap_ant = (
        "L 90.0 1905.5 Q 90.0 1914.0 96.0 1920.0 L 96.0 1920.0 Q 102.0 1926.0 102.0 1934.5 "
        "L 102.0 1938.0 Q 102.0 1950.0 114.0 1950.0 L 122.0 1950.0 Q 138.0 1950.0 149.3 1961.3 "
        "L 150.7 1962.7 Q 162.0 1974.0 162.0 1990.0 L 162.0 2126.0 Q 162.0 2142.0 173.3 2153.3 "
        "L 234.7 2214.7 Q 246.0 2226.0 246.0 2242.0 L 246.0 2294.0 Q 246.0 2310.0 230.0 2310.0 "
        "L 142.0 2310.0 Q 126.0 2310.0 114.7 2321.3 L 89.3 2346.7 Q 78.0 2358.0 78.0 2374.0 "
        "L 78.0 2565.5 Q 78.0 2574.0 84.0 2580.0 L 85.8 2581.8 Q 90.0 2586.0 90.0 2592.0 "
        "L 90.0 2592.0 Q 90.0 2598.0 94.2 2602.2 L 96.0 2604.0 Q 102.0 2610.0 102.0 2618.5 "
        "L 102.0 2673.5 Q 102.0 2682.0 96.0 2688.0 L 96.0 2688.0 Q 90.0 2694.0 90.0 2702.5"
    )
    svg = svg.replace(tramo_dhap_ant, "L 90.0 2702.5")

    tramo_dhap_leyenda_ant = (
        "L 30.0 5006.0 Q 30.0 5022.0 41.3 5033.3 L 78.7 5070.7 Q 90.0 5082.0 106.0 5082.0 "
        "L 3753.5 5082.0 Q 3762.0 5082.0 3768.0 5076.0 L 3768.0 5076.0 Q 3774.0 5070.0 3774.0 5061.5 "
        "L 3774.0 4558.0 Q 3774.0 4542.0 3785.3 4530.7 L 3834.7 4481.3 Q 3846.0 4470.0 3862.0 4470.0"
    )
    tramo_dhap_leyenda_nvo = (
        "L 30.0 4549.0 Q 30.0 4565.0 46.0 4565.0 L 3758.0 4565.0 "
        "Q 3774.0 4565.0 3774.0 4549.0 L 3774.0 4486.0 Q 3774.0 4470.0 3790.0 4470.0 L 3862.0 4470.0"
    )
    svg = svg.replace(tramo_dhap_leyenda_ant, tramo_dhap_leyenda_nvo)

    # - cx_cetonicos_sangre: trayectoria en L directa desde D-β-Hidroxibutirato (586, 3630) ➔ X=54 ➔ Sangre (447)
    tramo_ceto_sangre_ant = (
        "M 586.0 3630.0 L 370.0 3630.0 Q 354.0 3630.0 342.7 3618.7 L 326.5 3602.5 "
        "Q 318.0 3594.0 306.0 3594.0 L 306.0 3594.0 Q 294.0 3594.0 294.0 3582.0 "
        "L 294.0 3582.0 Q 294.0 3570.0 285.5 3561.5 L 233.3 3509.3 Q 222.0 3498.0 "
        "206.0 3498.0 L 98.5 3498.0 Q 90.0 3498.0 84.0 3492.0 L 84.0 3492.0 "
        "Q 78.0 3486.0 78.0 3477.5 L 78.0 3410.5 Q 78.0 3402.0 72.0 3396.0 "
        "L 72.0 3396.0 Q 66.0 3390.0 66.0 3381.5 L 66.0 2798.5 Q 66.0 2790.0 "
        "72.0 2784.0 L 72.0 2784.0 Q 78.0 2778.0 78.0 2769.5 L 78.0 2654.5 "
        "Q 78.0 2646.0 72.0 2640.0 L 70.2 2638.2 Q 66.0 2634.0 66.0 2628.0 "
        "L 66.0 2628.0 Q 66.0 2622.0 61.8 2617.8 L 60.0 2616.0 Q 54.0 2610.0 "
        "54.0 2601.5 L 54.0 447.0"
    )
    tramo_ceto_sangre_nvo = (
        "M 566.0 3630.0 L 70.0 3630.0 Q 54.0 3630.0 54.0 3614.0 L 54.0 447.0"
    )
    svg = svg.replace(tramo_ceto_sangre_ant, tramo_ceto_sangre_nvo)

    # - cx_acetoacetato_sangre: trayectoria en L paralela desde Acetoacetato (880, 3486) ➔ Y=3652 ➔ X=74 ➔ Sangre (447)
    tramo_aceto_full_ant = (
        "M 880.0 3486.0 L 887.0 3486.0 Q 894.0 3486.0 898.9 3481.1 L 906.7 3473.3 "
        "Q 918.0 3462.0 918.0 3446.0 L 918.0 3146.5 Q 918.0 3138.0 924.0 3132.0 "
        "L 924.0 3132.0 Q 930.0 3126.0 930.0 3117.5 L 930.0 3086.5 Q 930.0 3078.0 "
        "924.0 3072.0 L 924.0 3072.0 Q 918.0 3066.0 918.0 3057.5 L 918.0 2830.0 "
        "Q 918.0 2814.0 906.7 2802.7 L 773.3 2669.3 Q 762.0 2658.0 746.0 2658.0 "
        "L 482.5 2658.0 Q 474.0 2658.0 468.0 2652.0 L 468.0 2652.0 Q 462.0 2646.0 "
        "462.0 2637.5 L 462.0 2446.0 Q 462.0 2430.0 473.3 2418.7 L 510.7 2381.3 "
        "Q 522.0 2370.0 522.0 2354.0 L 522.0 2326.0 Q 522.0 2310.0 510.7 2298.7 "
        "L 497.3 2285.3 Q 486.0 2274.0 470.0 2274.0 L 266.5 2274.0 Q 258.0 2274.0 "
        "252.0 2268.0 L 252.0 2268.0 Q 246.0 2262.0 237.5 2262.0 L 98.5 2262.0 "
        "Q 90.0 2262.0 84.0 2256.0 L 84.0 2256.0 Q 78.0 2250.0 78.0 2241.5 L 78.0 447.0"
    )
    tramo_aceto_full_nvo = (
        "M 880.0 3486.0 L 954.0 3486.0 Q 968.0 3486.0 968.0 3500.0 L 968.0 3728.0 "
        "Q 968.0 3742.0 954.0 3742.0 L 90.0 3742.0 Q 74.0 3742.0 74.0 3726.0 L 74.0 447.0"
    )
    svg = svg.replace(tramo_aceto_full_ant, tramo_aceto_full_nvo)

    # Mover los 2 rótulos de cetonas ➔ sangre a x=82 (con font-size=9.5 para no tocar la flecha X=240 de ACS)
    svg = svg.replace(
        '<text x="62.0" y="2288.9" text-anchor="start" fill="#9d1c55" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">Cuerpos cetónicos ➔ Sangre</text>',
        '<text x="82.0" y="1635.0" text-anchor="start" fill="#9d1c55" font-size="9.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">Cuerpos cetónicos ➔ Sangre</text>',
    )
    svg = svg.replace(
        '<text x="324.1" y="2289.5" text-anchor="middle" fill="#9d1c55" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">Acetoacetato ➔ Sangre</text>',
        '<text x="82.0" y="1662.0" text-anchor="start" fill="#9d1c55" font-size="9.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">Acetoacetato ➔ Sangre</text>',
    )

    # - cx_ctp_uracilo: nacer justo debajo del grupo OH de CTP (Y=2060 en lugar de Y=2037)
    svg = svg.replace("M 5034.0 2037.0 L 5034.0 2486.0", "M 5034.0 2060.0 L 5034.0 2486.0")

    # - cx_cistat_propionil: baja por X=30 hasta Y=2862 (debajo de Palmitoil-CoA Matriz) antes de girar a la derecha
    tramo_cistat_ant = (
        "L 30.0 2606.0 Q 30.0 2622.0 46.0 2622.0 L 134.0 2622.0 Q 150.0 2622.0 161.3 2610.7 "
        "L 165.5 2606.5 Q 174.0 2598.0 186.0 2598.0 L 189.5 2598.0 Q 198.0 2598.0 204.0 2604.0 "
        "L 204.0 2604.0 Q 210.0 2610.0 218.5 2610.0 L 302.0 2610.0 Q 318.0 2610.0 329.3 2621.3 "
        "L 366.7 2658.7 Q 378.0 2670.0 394.0 2670.0 L 422.0 2670.0 Q 438.0 2670.0 449.3 2681.3 "
        "L 534.7 2766.7 Q 546.0 2778.0 546.0 2794.0 L 546.0 2841.5 Q 546.0 2850.0 552.0 2856.0 "
        "L 552.0 2856.0 Q 558.0 2862.0 566.5 2862.0"
    )
    tramo_cistat_nvo = "L 30.0 2846.0 Q 30.0 2862.0 46.0 2862.0 L 566.5 2862.0"
    svg = svg.replace(tramo_cistat_ant, tramo_cistat_nvo)

    # -------------------------------------------------------------------------
    # 16. CONEXIÓN DIRECTA DE L-ASPARTATO EN LA LUPA LANZADERA MALATO-ASPARTATO
    #     (OAA Krebs ➔ GOT2 ➔ L-Aspartato Matriz ➔ Aralar ➔ L-Aspartato Citosol ➔ Urea)
    # -------------------------------------------------------------------------
    # 16a. cx_oaa_got2_asp: conecta Oxalacetato en Krebs (830, 2612) directamente con L-Aspartato [4C] Matriz en la lupa (805, 2065)
    tramo_oaa_asp_ant = (
        "M 986.8 2622.0 L 1000.4 2622.0 Q 1014.0 2622.0 1023.6 2612.4 L 1026.7 2609.3 "
        "Q 1038.0 2598.0 1054.0 2598.0 L 1298.0 2598.0 Q 1314.0 2598.0 1325.3 2586.7 "
        "L 1338.7 2573.3 Q 1350.0 2562.0 1366.0 2562.0 L 1533.5 2562.0 Q 1542.0 2562.0 "
        "1548.0 2556.0 L 1548.0 2556.0 Q 1554.0 2550.0 1562.5 2550.0 L 1641.5 2550.0 "
        "Q 1650.0 2550.0 1656.0 2556.0 L 1656.0 2556.0 Q 1662.0 2562.0 1670.5 2562.0 "
        "L 2378.0 2562.0 Q 2394.0 2562.0 2405.3 2550.7 L 2418.7 2537.3 Q 2430.0 2526.0 "
        "2430.0 2510.0 L 2430.0 2486.5 Q 2430.0 2478.0 2436.0 2472.0 L 2436.0 2472.0 "
        "Q 2442.0 2466.0 2450.5 2466.0 L 2565.5 2466.0 Q 2574.0 2466.0 2580.0 2460.0 "
        "L 2580.0 2460.0 Q 2586.0 2454.0 2586.0 2445.5 L 2586.0 2422.0 Q 2586.0 2406.0 "
        "2597.3 2394.7 L 2706.7 2285.3 Q 2718.0 2274.0 2718.0 2258.0 L 2718.0 2242.0 "
        "Q 2718.0 2226.0 2729.3 2214.7 L 2742.7 2201.3 Q 2754.0 2190.0 2770.0 2190.0 "
        "L 3806.0 2190.0 Q 3822.0 2190.0 3833.3 2178.7 L 3888.3 2123.7 Q 3894.0 2118.0 "
        "3894.0 2109.9 L 3894.0 2101.8"
    )
    tramo_oaa_asp_nvo = (
        "M 830.0 2612.0 L 830.0 2250.0 Q 830.0 2236.0 817.5 2236.0 "
        "Q 805.0 2236.0 805.0 2222.0 L 805.0 2065.0"
    )
    svg = svg.replace(tramo_oaa_asp_ant, tramo_oaa_asp_nvo)
    svg = svg.replace(
        '<text x="2255.7" y="2555.0" text-anchor="middle" fill="#096a61" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">GOT2: OAA ➔ Aspartato</text>',
        '<text x="842.0" y="2385.0" text-anchor="start" fill="#096a61" font-size="10.5" font-weight="800" font-family="\'Inter\', sans-serif" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round" paint-order="stroke">GOT2: OAA ➔ L-Aspartato (Matriz)</text>',
    )

    # 16b. cx_lanz_asp_urea: nace directamente de L-Aspartato [4C] Citosol dentro de la lupa (792, 1642) y sale hacia ASS1 en Urea
    svg = svg.replace(
        "M 1348.0 2214.0 L 1509.5 2214.0",
        "M 792.0 1642.0 L 792.0 1607.0 Q 792.0 1595.0 804.0 1595.0 "
        "L 1314.0 1595.0 Q 1326.0 1595.0 1326.0 1607.0 L 1326.0 2202.0 "
        "Q 1326.0 2214.0 1338.0 2214.0 L 1509.5 2214.0",
    )

    return svg
