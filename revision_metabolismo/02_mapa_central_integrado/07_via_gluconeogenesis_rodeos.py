# =============================================================================
# MÓDULO DE REVISIÓN: Vía 2: Gluconeogénesis y sus 3 Rodeos Metabólicos
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 1433 a 1668 de 4188)
# Descripción      : Subida anabólica desde piruvato/lactato/glicerol hasta glucosa libre.
# =============================================================================

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

