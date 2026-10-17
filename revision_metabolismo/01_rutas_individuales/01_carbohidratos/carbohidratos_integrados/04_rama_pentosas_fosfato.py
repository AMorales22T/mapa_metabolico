# =============================================================================
# MÓDULO DE REVISIÓN: Rama Derecha: Vía de las Pentosas Fosfato
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/carbohidratos_unidos/generar_carbohidratos_unidos.py (líneas 775 a 1031 de 1241)
# Descripción      : Shunt oxidativo, interconversiones no oxidativas y retorno a F6P/GAP.
# =============================================================================

    # =========================================================================
    # CONEXIÓN HORIZONTAL SEGMENTADA: G-6-P ➔ G6PDH ➔ LACTONA (SHUNT PENTOSAS)
    # =========================================================================
    # Segmento 1: desde G-6-P (x=1680) hasta G6PDH (x=2000)
    # Enzima: G6PDH en x=2070 con flecha y cofactores limpios sin líneas atravesándola
    # Segmento 2: desde G6PDH (x=2140) hasta Lactona (x=2430)
    svg_parts.append("""
    <!-- Conexión horizontal hacia Shunt de Pentosas (Segmento 1) -->
    <line x1="1680" y1="410" x2="2010" y2="410" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>

    <!-- Reacción G6PDH (Totalmente despejada) -->
    <g transform="translate(2080, 410)">
      <line x1="-35" y1="0" x2="35" y2="0" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>
      <path d="M -35 -12 Q -12 -24 15 -12" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-30" y="-26" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#475569">+ NADP⁺</text>
      
      <path d="M -35 12 Q -12 24 15 12" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-30" y="30" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#059669">+ NADPH + H⁺</text>
      
      <g transform="translate(0, -2)">
        <text x="0" y="-12" font-family="'Inter', sans-serif" font-size="14.5" font-weight="800" fill="#0f172a" text-anchor="middle">G6PDH</text>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748b" text-anchor="middle">EC 1.1.1.49</text>
      </g>
    </g>

    <!-- Conexión horizontal hacia Lactona (Segmento 2) -->
    <line x1="2150" y1="410" x2="2430" y2="410" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>
    """)

    # =========================================================================
    # RUTA LATERAL DERECHA: VÍA DE LAS PENTOSAS FOSFATO (X ≈ 2450 a 3150)
    # =========================================================================
    # 1. 6-Fosfoglucono-δ-Lactona
    svg_parts.append(crear_metabolito(
        x=2440, y=375,
        nombre="6-Fosfoglucono-δ-Lactona",
        carbonos="6 Carbonos (Lactona intramolecular)",
        detalle="Primer intermediario oxidativo",
        svg_estructura=FOSFOGLUCONO_LACTONA_6,
        dx_texto=140
    ))

    # Reacción 2: Lactonasa
    svg_parts.append("""
    <g transform="translate(2760, 420)">
      <line x1="0" y1="0" x2="65" y2="0" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M 12 -14 Q 32 -26 52 -14" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="32" y="-28" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0284c7" text-anchor="middle">+ H₂O</text>
      <text x="32" y="18" font-family="'Inter', sans-serif" font-size="13.5" font-weight="800" fill="#0f172a" text-anchor="middle">Lactonasa</text>
      <text x="32" y="32" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#64748b" text-anchor="middle">EC 3.1.1.31</text>
    </g>
    """)

    # 2. 6-Fosfogluconato
    svg_parts.append(crear_metabolito(
        x=2860, y=375,
        nombre="6-Fosfogluconato",
        carbonos="6 Carbonos (Ácido aldónico Ⓟ)",
        detalle="Substrato de descarboxilación oxidativa",
        svg_estructura=FOSFOGLUCONATO_6,
        dx_texto=140
    ))

    # Reacción 3: 6-Fosfogluconato Deshidrogenasa (Vertical descendente)
    svg_parts.append("""
    <g transform="translate(2800, 510)">
      <line x1="0" y1="0" x2="0" y2="52" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M -85 10 Q -30 10 -4 20" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-92" y="14" fill="#475569" font-size="12" font-weight="800" text-anchor="end">+ NADP⁺</text>
      
      <path d="M -4 28 Q -30 38 -85 38" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-92" y="42" fill="#059669" font-size="12" font-weight="800" text-anchor="end">+ NADPH + H⁺</text>
      
      <path d="M 4 28 Q 30 38 85 38" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="92" y="42" fill="#475569" font-size="12" font-weight="800">+ CO₂</text>
      
      <g transform="translate(22, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">6-Fosfogluconato Deshidrogenasa</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 1.1.1.44 (Genera 2.º NADPH)</text>
      </g>
    </g>
    """)

    # 3. D-Ribulosa-5-Fosfato
    svg_parts.append(crear_metabolito(
        x=2720, y=610,
        nombre="D-Ribulosa-5-Fosfato",
        carbonos="5 Carbonos (Cetopentosa Ⓟ)",
        detalle="Encrucijada entre isomerización y epimerización",
        svg_estructura=RIBULOSA_5_FOSFATO,
        dx_texto=140
    ))

    # Bifurcación Isomerasa / Epimerasa
    svg_parts.append("""
    <g transform="translate(2800, 750)">
      <!-- Rama Izquierda a Xilulosa-5-P -->
      <path d="M -15 0 Q -100 25 -150 65" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(-140, 20)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Fosfopentosa Epimerasa</text>
        <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#64748b" text-anchor="middle">EC 5.1.3.1 (Inversión en C3)</text>
      </g>
      <!-- Rama Derecha a Ribosa-5-P -->
      <path d="M 15 0 Q 100 25 160 65" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(140, 20)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Fosfopentosa Isomerasa</text>
        <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#64748b" text-anchor="middle">EC 5.3.1.6 (Cetosa ⇄ Aldosa)</text>
      </g>
    </g>
    """)

    # 4a. Xilulosa-5-P (a la izquierda)
    svg_parts.append(crear_metabolito(
        x=2480, y=835,
        nombre="D-Xilulosa-5-P",
        carbonos="5 Carbonos (Epímero C3)",
        detalle="Donador de 2C a la Transcetolasa",
        svg_estructura=XILULOSA_5_FOSFATO,
        texto_izquierda=True
    ))

    # 4b. Ribosa-5-P (a la derecha)
    svg_parts.append(crear_metabolito(
        x=2960, y=835,
        nombre="D-Ribosa-5-P",
        carbonos="5 Carbonos (Pentosa Aldosa)",
        detalle="Precursora de Nucleótidos y Ácidos Nucleicos",
        svg_estructura=RIBOSA_5_FOSFATO,
        dx_texto=140
    ))

    # Salida hacia Síntesis de Nucleótidos desde Ribosa-5-P (y = 960)
    svg_parts.append("""
    <g transform="translate(3030, 955)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>
      <g transform="translate(0, 42)">
        <rect x="-105" y="0" width="210" height="40" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="2"/>
        <text x="0" y="16" fill="#6d28d9" font-size="12" font-weight="900" text-anchor="middle">SÍNTESIS DE NUCLEÓTIDOS</text>
        <text x="0" y="30" fill="#7c3aed" font-size="10" font-weight="700" text-anchor="middle">PRPP ➔ ARN, ADN, ATP, GTP</text>
      </g>
    </g>
    """)

    # Fase No Oxidativa: TK1 (DESPEJADA >100 px debajo de la caja morada, en y = 1110)
    svg_parts.append(crear_paso_no_oxidativo(
        x=2780, y=1110,
        enzima="Transcetolasa (TK1)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Ribosa-5-P (5C)",
        productos_txt="GAP (3C) + Sedoheptulosa-7-P (7C)"
    ))

    # Sedoheptulosa-7-P (Izquierda)
    svg_parts.append(crear_metabolito(
        x=2480, y=1210,
        nombre="Sedoheptulosa-7-P",
        carbonos="7 Carbonos (Heptosa Ⓟ)",
        detalle="Intermediario transitorio de 7C",
        svg_estructura=SEDOHEPTULOSA_7_FOSFATO,
        texto_izquierda=True
    ))

    # GAP (Derecha)
    svg_parts.append(crear_metabolito(
        x=2960, y=1210,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="Aceptor intermedio",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO,
        dx_texto=140
    ))

    # Transaldolasa (TA)
    svg_parts.append(crear_paso_no_oxidativo(
        x=2780, y=1340,
        enzima="Transaldolasa (TA)",
        ec="EC 2.2.1.2 (Base de Schiff con Lys)",
        sustratos_txt="Sedoheptulosa-7-P (7C) + GAP (3C)",
        productos_txt="Eritrosa-4-P (4C) + Fructosa-6-P (6C)"
    ))

    # Eritrosa-4-P (Izquierda)
    svg_parts.append(crear_metabolito(
        x=2480, y=1440,
        nombre="D-Eritrosa-4-P",
        carbonos="4 Carbonos (Tetrosa)",
        detalle="Precursor de Aminoácidos Aromáticos",
        svg_estructura=ERITROSA_4_FOSFATO,
        texto_izquierda=True
    ))

    # F6P (1er reingreso - Derecha)
    svg_parts.append(crear_metabolito(
        x=2960, y=1440,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡1.er Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        dx_texto=140
    ))

    # TK2
    svg_parts.append(crear_paso_no_oxidativo(
        x=2780, y=1570,
        enzima="Transcetolasa (TK2)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Eritrosa-4-P (4C)",
        productos_txt="Fructosa-6-P (6C) + GAP (3C)"
    ))

    # F6P (2º reingreso)
    svg_parts.append(crear_metabolito(
        x=2480, y=1670,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡2.º Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        texto_izquierda=True
    ))

    # GAP (3er reingreso)
    svg_parts.append(crear_metabolito(
        x=2960, y=1670,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="¡3.er Reingreso a la Glucólisis!",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO,
        dx_texto=140
    ))

    # BANNER DE BALANCE FINAL DE PENTOSAS
    svg_parts.append("""
    <g transform="translate(2780, 1830)">
      <rect x="-260" y="-14" width="520" height="74" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="2.2" filter="drop-shadow(0 4px 8px rgba(0,0,0,0.06))"/>
      <text x="0" y="14" fill="#6d28d9" font-size="14" font-weight="900" text-anchor="middle">BALANCE TOTAL DE LA FASE NO OXIDATIVA</text>
      <text x="0" y="34" fill="#0f172a" font-size="12.5" font-weight="800" text-anchor="middle">3 Pentosas (5C) ⇄ 2 Fructosa-6-P (6C) + 1 Gliceraldehído-3-P (3C)</text>
      <text x="0" y="50" fill="#047857" font-size="11.5" font-weight="700" text-anchor="middle">Todos los carbonos se reciclan de vuelta hacia el eje de la Glucólisis citosólica</text>
    </g>
    """)

    # =========================================================================
    # FLECHAS DE RETORNO/RECICLAJE HACIA LA GLUCÓLISIS CENTRAL
    # =========================================================================
    svg_parts.append("""
    <!-- RETORNO 1: Fructosa-6-P hacia F6P Central -->
    <path d="M 2960 1485 C 2400 1400 1950 900 1690 635" fill="none" stroke="#059669" stroke-width="2.8" stroke-dasharray="9 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(2100, 890)">
      <text x="0" y="0" fill="#047857" font-size="11" font-weight="800" text-anchor="middle">RETORNO: F-6-P A GLUCÓLISIS</text>
    </g>

    <!-- RETORNO 2: GAP hacia GAP Central -->
    <path d="M 2960 1715 C 2480 1640 2000 1350 1810 1140" fill="none" stroke="#059669" stroke-width="2.8" stroke-dasharray="9 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(2280, 1370)">
      <text x="0" y="0" fill="#047857" font-size="11" font-weight="800" text-anchor="middle">RETORNO: GAP A GLUCÓLISIS</text>
    </g>
    """)

