# =============================================================================
# MÓDULO DE REVISIÓN: Eje Inicial de Glucólisis y Rama de Glucógeno
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/carbohidratos_unidos/generar_carbohidratos_unidos.py (líneas 533 a 774 de 1241)
# Descripción      : Conexión G6P <-> G1P, glucógeno y lupa molecular de glucogenina.
# =============================================================================

def generar_mapa_carbohidratos():
    """Compila las tres rutas conectadas biológicamente en el citosol unificado."""
    validar_contrato_layout()
    svg_parts = []

    # 1. Capa de entorno celular continuo (Membrana arriba y citoesqueleto)
    svg_parts.append(generar_entorno_celular_continuo(ANCHO_CANVAS, ALTO_CANVAS))

    # 2. Mitocondria Biológica amplia en la base
    svg_parts.append(generar_mitocondria_biologica(
        x_inicio=1020,
        ancho_mito=2350,
        y_base=BANDAS["matriz_mitocondrial"][0]
    ))

    # =========================================================================
    # RUTA CENTRAL: LA GLUCÓLISIS (EJE X = 1520 a 1580)
    # =========================================================================
    X_GLU = punto_nodo("glucosa_6_fosfato")[0]
    X_FLECHA = 1580
    Y_G6P = punto_nodo("glucosa_6_fosfato")[1]
    X_PIRUVATO, Y_PIRUVATO = punto_nodo("piruvato")

    # 1. D-Glucosa
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=170,
        nombre="D-Glucosa",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Entrada directa desde el GLUT-4",
        svg_estructura=GLUCOSA,
        dx_texto=140
    ))

    # Reacción 1: Hexoquinasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=275,
        enzima="Hexoquinasa",
        ec="EC 2.7.1.1 (Mg²⁺)",
        regulacion="⊣ G-6-P | ⊕ Insulina",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 2. Glucosa-6-Fosfato (EL NODO CENTRAL DISTRIBUIDOR - LIMPIO, SIN GLOBO)
    svg_parts.append(f"""
    <!-- Nodo Central: Glucosa-6-Fosfato -->
    <g transform="translate({X_GLU}, {Y_G6P})">
      {GLUCOSA_6_FOSFATO}
    </g>
    <g transform="translate({X_FLECHA}, 465)">
      <text x="0" y="0" fill="#0f172a" font-size="17" font-weight="800" text-anchor="middle">Glucosa-6-Fosfato (G-6-P)</text>
      <text x="0" y="18" fill="#ea580c" font-size="12.5" font-weight="700" text-anchor="middle">6 Carbonos (Hexosa Ⓟ)</text>
    </g>
    """)

    # =========================================================================
    # CONEXIÓN HORIZONTAL SEGMENTADA: G-6-P ⇄ FOSFOGLUCOMUTASA ⇄ G-1-P
    # =========================================================================
    # Segmento 1: desde G-6-P (x=1470) hasta Fosfoglucomutasa (x=1070)
    # Enzima: Fosfoglucomutasa en x=1000 con sus flechas ⇄ sin ser atravesada por líneas
    # Segmento 2: desde Fosfoglucomutasa (x=930) hasta Haworth de G1P (x=675)
    svg_parts.append("""
    <!-- Conexión horizontal hacia la Glucogénesis (Segmento 1) -->
    <line x1="1470" y1="410" x2="1080" y2="410" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

    <!-- Reacción Fosfoglucomutasa (Totalmente despejada) -->
    <g transform="translate(1000, 410)">
      <line x1="-35" y1="-3" x2="35" y2="-3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="35" y1="3" x2="-35" y2="3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(0, -12)">
        <text x="0" y="-12" font-family="'Inter', sans-serif" font-size="14.5" font-weight="800" fill="#0f172a" text-anchor="middle">Fosfoglucomutasa</text>
        <text x="0" y="2" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748b" text-anchor="middle">EC 5.4.2.2 (⇄)</text>
        <text x="0" y="-25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#d97706" text-anchor="middle">Interm. Glucosa-1,6-BP</text>
      </g>
    </g>

    <!-- Conexión horizontal hacia G-1-P (Segmento 2) -->
    <line x1="920" y1="410" x2="680" y2="410" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
    """)

    # =========================================================================
    # RUTA LATERAL IZQUIERDA: GLUCOGÉNESIS
    # =========================================================================
    # 2. α-D-Glucosa-1-Fosfato (G-1-P)
    # Estructura en x=530, texto a la izquierda sin globos
    svg_parts.append(crear_metabolito(
        x=530, y=375,
        nombre="α-D-Glucosa-1-Fosfato",
        carbonos="6 Carbonos (Fosfato en C1-α)",
        detalle="Sustrato de activación por UTP",
        svg_estructura=GLUCOSA_1_FOSFATO,
        texto_izquierda=True
    ))

    # Reacción 2: UDP-Glucosa Pirofosforilasa
    svg_parts.append("""
    <g transform="translate(520, 505)">
      <line x1="0" y1="0" x2="0" y2="52" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M -90 10 Q -35 10 -4 22" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-98" y="14" fill="#475569" font-size="12" font-weight="800" text-anchor="end">+ UTP</text>
      <path d="M -4 30 Q -35 42 -90 42" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-98" y="46" fill="#059669" font-size="12" font-weight="800" text-anchor="end">+ PPi ➔ 2 Pi (Pirofosfatasa)</text>
      <g transform="translate(22, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">UDP-Glucosa Pirofosforilasa</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 2.7.7.9 (Impulso por PPi)</text>
        <text x="0" y="32" fill="#059669" font-size="11" font-weight="700">ΔG'° ≈ -19.2 kJ/mol (Irreversible)</text>
      </g>
    </g>
    """)

    # 3. UDP-Glucosa (Uridina Difosfato Glucosa)
    svg_parts.append(crear_metabolito(
        x=280, y=605,
        nombre="UDP-Glucosa",
        carbonos="Nucleótido-Azúcar activado",
        detalle="Donador de glucosa de alta energía",
        svg_estructura=UDP_GLUCOSA,
        dx_texto=290
    ))

    # =========================================================================
    # 4. CEBADOR MOLECULAR DE GLUCOGENINA + LUPA MOLECULAR (DISEÑO ORIGINAL)
    # =========================================================================
    Y_CEBADOR = 770
    svg_parts.append(f"""
    <!-- CEBADOR MOLECULAR DE GLUCOGENINA (LIBRE, SIN GLOBO) -->
    <g transform="translate(140, {Y_CEBADOR})">
      {CEBADOR_GLUCOGENINA}
      
      <!-- Textos del cebador a la derecha -->
      <g transform="translate(370, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="900">Cebador: Glucogenina-(Glc)₈</text>
        <text x="0" y="18" fill="#b45309" font-size="11.5" font-weight="700">Dímero autoglucosilante (EC 2.4.1.186)</text>
        <text x="0" y="34" fill="#64748b" font-size="10.5">• Anclaje covalente en residuo Tyr-194</text>
        <text x="0" y="48" fill="#dc2626" font-size="10.5" font-weight="800">• Extremo 4-OH libre: Sustrato aceptor</text>
        <text x="0" y="63" fill="#64748b" font-size="10">Requerido: Glucógeno Sintasa no inicia de novo</text>
      </g>
    </g>

    <!-- LÍNEAS DE PROYECCIÓN CÓNICA HACIA LA LUPA DE ZOOM MOLECULAR -->
    <g stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4 3" opacity="0.65">
      <line x1="435" y1="{Y_CEBADOR + 35}" x2="255" y2="{Y_CEBADOR + 180}"/>
      <line x1="435" y1="{Y_CEBADOR + 15}" x2="160" y2="{Y_CEBADOR + 140}"/>
    </g>

    <!-- LUPA DE ZOOM MOLECULAR: ACOPLAMIENTO CATALÍTICO CEBADOR + SINTASA -->
    <g transform="translate(180, {Y_CEBADOR + 210})">
      {LUPA_MECANISMO_CEBADOR}
    </g>

    <!-- EXPLICACIÓN BIOQUÍMICA A LA DERECHA DE LA LUPA -->
    <g transform="translate(340, {Y_CEBADOR + 175})">
      <rect x="0" y="0" width="460" height="95" rx="8" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="16" y="22" fill="#1d4ed8" font-size="12" font-weight="900">MECANISMO DE ACOPLAMIENTO Y ELONGACIÓN</text>
      <text x="16" y="40" fill="#0f172a" font-size="10.5" font-weight="600">
        1. La <tspan font-weight="800" fill="#2563eb">Glucógeno Sintasa</tspan> abraza el extremo <tspan font-weight="800" fill="#dc2626">4-OH</tspan> de la cadena cebadora.
      </text>
      <text x="16" y="58" fill="#0f172a" font-size="10.5" font-weight="600">
        2. El oxígeno ataca al <tspan font-weight="800" fill="#ea580c">C1</tspan> de la <tspan font-weight="800">UDP-Glucosa</tspan>, expulsando al grupo UDP.
      </text>
      <text x="16" y="76" fill="#059669" font-size="10.5" font-weight="800">
        3. Se forma el nuevo enlace α(1→4) y la cadena se alarga un residuo a la vez.
      </text>
    </g>
    """)

    # Reacción 3: Glucógeno Sintasa (debajo de la lupa)
    Y_RX_SINTASA = Y_CEBADOR + 325
    svg_parts.append(f"""
    <!-- Reacción: Glucógeno Sintasa -->
    <g transform="translate(520, {Y_RX_SINTASA})">
      <line x1="0" y1="0" x2="0" y2="55" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M -4 30 Q -35 42 -90 42" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="-98" y="46" fill="#0284c7" font-size="12" font-weight="800" text-anchor="end">+ UDP libre</text>
      <g transform="translate(22, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">Glucógeno Sintasa</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 2.4.1.11 (Paso Limitante Clave)</text>
        <text x="0" y="32" fill="#16a34a" font-size="11" font-weight="700">⊕ Insulina (PP1), G-6-P</text>
        <text x="0" y="46" fill="#e11d48" font-size="11" font-weight="700">⊣ Glucagón, Adrenalina (PKA / GSK-3)</text>
      </g>
    </g>
    """)

    # Reacción 4: Enzima Ramificante
    Y_RX_RAMIF = Y_RX_SINTASA + 95
    svg_parts.append(f"""
    <!-- Reacción: Enzima Ramificadora -->
    <g transform="translate(520, {Y_RX_RAMIF})">
      <line x1="0" y1="0" x2="0" y2="50" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(22, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">Enzima Ramificadora del Glucógeno</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 2.4.1.18 (Amilo α-1,4 ➔ α-1,6)</text>
        <text x="0" y="32" fill="#c2410c" font-size="11" font-weight="700">Transfiere bloque de ~7 glucosas; ramifica cada 8-12 residuos</text>
      </g>
    </g>
    """)

    # 5. CADENA DE GLUCÓGENO RAMIFICADA (SIN GLOBO)
    Y_GLUC = Y_RX_RAMIF + 80
    svg_parts.append(f"""
    <!-- Polímero de Glucógeno Completo -->
    <g transform="translate(180, {Y_GLUC})">
      <g transform="translate(0, 30)">
        {CADENA_GLUCOGENO}
      </g>
      <g transform="translate(420, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="17" font-weight="900">Glucógeno (n + 1)</text>
        <text x="0" y="18" fill="#d97706" font-size="12.5" font-weight="800">Polisacárido de Reserva Energética</text>
        <text x="0" y="34" fill="#64748b" font-size="11">• Enlaces principales α(1→4) y ramas α(1→6)</text>
        <text x="0" y="48" fill="#b45309" font-size="11" font-weight="700">• Múltiples extremos no reductores para rápida lisis</text>
        <text x="0" y="63" fill="#64748b" font-size="10.5">Hasta 55,000 unidades de glucosa por partícula</text>
      </g>
    </g>
    """)

    # 6. GRÁNULO CITOSÓLICO DE INCLUSIÓN
    Y_GRANULO = Y_GLUC + 200
    svg_parts.append(f"""
    <!-- SECCIÓN ANATÓMICA: EL GRÁNULO DE GLUCÓGENO EN EL CITOSOL -->
    <g transform="translate(140, {Y_GRANULO})">
      <rect x="0" y="0" width="760" height="165" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="1.8"/>
      <g transform="translate(15, 15)">
        {GRANULO_CITOSOLICO_INCLUSION}
      </g>
      <g transform="translate(180, 24)">
        <text x="0" y="0" fill="#92400e" font-size="14" font-weight="900">¿POR QUÉ FLOTA EN EL CITOSOL Y CÓMO SALE DE LA CÉLULA?</text>
        <text x="0" y="20" fill="#0f172a" font-size="11" font-weight="700">
          • Inclusión no membranosa: Permite almacenar miles de glucosas sin alterar la presión osmótica celular.
        </text>
        <text x="0" y="38" fill="#dc2626" font-size="11" font-weight="700">
          • Nunca sale como polímero: No puede cruzar la membrana plasmática.
        </text>
        <text x="0" y="56" fill="#047857" font-size="11" font-weight="700">
          • En hígado: Glucógeno ➔ G-1-P ➔ G-6-P ➔ Glucosa libre (Glucosa-6-Fosfatasa en RE) ➔ GLUT-2 a sangre.
        </text>
        <text x="0" y="74" fill="#475569" font-size="10.5">
          • En músculo: Carece de Glucosa-6-Fosfatasa; el glucógeno se destina exclusivamente a ATP por Glucólisis.
        </text>
      </g>
    </g>
    """)

