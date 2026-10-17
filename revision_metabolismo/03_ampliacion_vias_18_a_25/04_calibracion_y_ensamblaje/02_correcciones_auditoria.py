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
        '<g id="m_der_pc_membrana" class="nodo-metabolito-libre" transform="translate(6220, 2150)">',
        '<g id="m_der_pc_membrana" class="nodo-metabolito-libre" transform="translate(6140, 2150)">'
    )
    svg = svg.replace(
        '<path d="M 40 0 C 70 40, 100 70, 100 100" fill="none" stroke="#0284c7" stroke-width="3" marker-end="url(#arrowBlue)"/>',
        '<path d="M 40 0 C 50 40, 60 70, 70 100" fill="none" stroke="#0284c7" stroke-width="3" marker-end="url(#arrowBlue)"/>'
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
      <line x1="0" y1="0" x2="0" y2="28" stroke="#ea580c" stroke-width="2.4"/>
      <!-- Rama Izquierda hacia DHAP (X=1470, Y=845) -->
      <path d="M 0 28 Q -90 35 -170 65" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <!-- Rama Derecha hacia GAP (X=1890, Y=845) -->
      <path d="M 0 28 Q 90 35 170 65" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <!-- Retorno gluconeogénico (condensación aldólica) -->
      <path d="M -160 55 Q -85 28 -5 20" fill="none" stroke="#7c3aed" stroke-width="1.8" stroke-dasharray="4 2" marker-end="url(#arrowFlow)"/>
      <path d="M 160 55 Q 85 28 5 20" fill="none" stroke="#7c3aed" stroke-width="1.8" stroke-dasharray="4 2" marker-end="url(#arrowFlow)"/>
      <!-- Rótulo y EC -->
      <text x="0" y="22" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Aldolasa</text>
      <text x="0" y="34" fill="#64748b" font-size="8" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 4.1.2.13</text>
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

    bloque_colector_nuevo = """      <!-- Colector lateral limpio por el canal izquierdo (sin cruzar sobre textos de DAG/MAG/MGL) -->
      <!-- Entrada 1 (ATGL): sale a la izquierda hacia el canal X=-650 -->
      <path d="M -586 1590 L -650 1590" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <!-- Entrada 2 (HSL): sale a la izquierda hacia el canal X=-650 -->
      <path d="M -586 1810 L -650 1810" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <!-- Entrada 3 (MGL): sale a la izquierda hacia el canal X=-650 -->
      <path d="M -586 2030 L -650 2030" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <!-- Tronco colector vertical por el margen izquierdo despejado hasta el fondo -->
      <path d="M -650 1590 L -650 2195 Q -650 2210 -635 2210 L -280 2210 Q -260 2210 -260 2190 L -260 1775" fill="none" stroke="#ea580c" stroke-width="2.4" stroke-dasharray="7 4" marker-end="url(#arrowOrange)"/>
      <text x="-655" y="1900" fill="#059669" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end" transform="rotate(-90 -655 1900)">Canal Colector de Ácidos Grasos Libres (1º, 2º y 3º AG)</text>"""

    if bloque_colector_anterior in svg:
        svg = svg.replace(bloque_colector_anterior, bloque_colector_nuevo)

    # -------------------------------------------------------------------------
    # 11. EXTENSIÓN DE FLECHAS CORTAS (FLECHAS QUE CAÍAN EN EL VACÍO)
    # -------------------------------------------------------------------------
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

    return svg
