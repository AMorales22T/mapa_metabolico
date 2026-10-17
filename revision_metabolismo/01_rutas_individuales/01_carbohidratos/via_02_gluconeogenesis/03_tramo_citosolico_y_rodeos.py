# =============================================================================
# MÓDULO DE REVISIÓN: Tramo Citosólico, Rodeos 2 y 3 (FBPasa-1 y G6Pasa)
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/via_02_gluconeogenesis/generar_gluconeogenesis.py (líneas 521 a 1090 de 1263)
# Descripción      : Subida gluconeogénica en el citosol, entrada de glicerol y lactato.
# =============================================================================

      <g transform="translate(24, 8)">
        <text x="0" y="-10" fill="#6d28d9" font-size="11" font-weight="900" font-family="'Inter', sans-serif">BYPASS 2</text>
        <text x="0" y="2" fill="#b91c1c" font-size="10" font-weight="800" font-family="'Inter', sans-serif">Sustituye a: Fosfofructocinasa-1 (PFK-1)</text>
        
        <text x="0" y="16" fill="#0f172a" font-size="13" font-weight="900">Fructosa-1,6-Bisfosfatasa-1 (FBPasa-1)</text>
        <text x="0" y="29" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">EC 3.1.3.11 (Hidrólisis simple de fosfato)</text>
        
        <text x="0" y="43" fill="#16a34a" font-size="10" font-weight="800">(+) Citrato (Abundancia energética)</text>
        <text x="0" y="56" fill="#dc2626" font-size="10" font-weight="800">(-) AMP, Fructosa-2,6-bisfosfato (F-2,6-BP)</text>

        <!-- Rótulo directo de la flecha glucolítica PFK-1 -->
        <text x="0" y="70" fill="#ea580c" font-size="10" font-weight="800">
          [Glucólisis: PFK-1 (EC 2.7.1.11) invierte 1 ATP]
        </text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # MÓDULO EXPLÍCITO: ENZIMA BIFUNCIONAL PFK-2 / FBPasa-2, FRUCTOSA-2,6-BISFOSFATO (F-2,6-BP)
    # Y CASCADA HORMONAL HEPÁTICA (GLUCAGÓN / PKA vs INSULINA / PP1)
    # Ubicado en X = 1360 a 1880 con total holgura espacial
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- MÓDULO REGULATORIO PFK-2 / FBPasa-2 Y F-2,6-BP -->
    <g transform="translate(1360, 560)">
      <!-- Rótulo del Sistema -->
      <text x="0" y="0" fill="#6d28d9" font-size="12.5" font-weight="900" letter-spacing="0.5">
        ENZIMA BIFUNCIONAL HEPÁTICA: PFK-2 / FBPasa-2
      </text>
      <text x="0" y="14" fill="#475569" font-size="9.5" font-weight="700">
        Control maestro del conmutador alostérico Glucólisis ⇄ Gluconeogénesis
      </text>

      <!-- 1. Enzima Bifuncional Hepática PFK-2/FBPasa-2 (Diagrama de Dominios) -->
      <g transform="translate(0, 26)">
        <rect x="0" y="0" width="160" height="26" rx="5" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>
        <text x="80" y="17" fill="#b91c1c" font-size="10" font-weight="900" text-anchor="middle">Dominio PFK-2 (Quinasa)</text>

        <!-- Enlace peptídico central con residuo regulatorio Ser-32 -->
        <line x1="160" y1="13" x2="200" y2="13" stroke="#0f172a" stroke-width="2"/>
        <circle cx="180" cy="13" r="9" fill="#fef9c3" stroke="#b45309" stroke-width="1.6"/>
        <text x="180" y="16" fill="#78350f" font-size="8" font-weight="900" text-anchor="middle">Ser-32</text>

        <rect x="200" y="0" width="170" height="26" rx="5" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
        <text x="285" y="17" fill="#6d28d9" font-size="10" font-weight="900" text-anchor="middle">Dominio FBPasa-2 (Fosfatasa)</text>

        <text x="380" y="17" fill="#64748b" font-size="9" font-weight="700">(Misma proteína dímera)</text>
      </g>

      <!-- 2. Cascada Hormonal Hepática: Glucagón vs Insulina -->
      <g transform="translate(0, 68)">
        <!-- Vía Glucagón (Ayuno) -->
        <g transform="translate(0, 0)">
          <path d="M 0 8 L 30 8" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
          <text x="36" y="11" fill="#ea580c" font-size="10" font-weight="900">Glucagón (Ayuno)</text>
          <text x="135" y="11" fill="#b45309" font-size="9.5" font-weight="800">➔ cAMP ↑ ➔ PKA ➔ Fosforila Ser-32 ➔</text>
          <text x="330" y="11" fill="#7c3aed" font-size="10" font-weight="900">ACTIVA FBPasa-2</text>
        </g>

        <!-- Vía Insulina (Posprandial) -->
        <g transform="translate(0, 20)">
          <path d="M 0 8 L 30 8" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
          <text x="36" y="11" fill="#0284c7" font-size="10" font-weight="900">Insulina (Saciedad)</text>
          <text x="135" y="11" fill="#0369a1" font-size="9.5" font-weight="800">➔ PP1 (Fosfatasa) ➔ Desfosforila Ser-32 ➔</text>
          <text x="330" y="11" fill="#b91c1c" font-size="10" font-weight="900">ACTIVA PFK-2</text>
        </g>
      </g>

      <!-- 3. Ciclo Local de Interconversión F-6-P ⇄ F-2,6-BP con Estructura Molecular -->
      <g transform="translate(30, 115)">
        <!-- Conector superior desde el pool de F-6-P -->
        <text x="150" y="0" fill="#0f172a" font-size="11" font-weight="900" text-anchor="middle">
          Fructosa-6-Fosfato (F-6-P) [Pool Citosólico]
        </text>

        <!-- Flecha hacia abajo: Actividad PFK-2 (Insulina) -->
        <line x1="70" y1="12" x2="70" y2="52" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
        <g transform="translate(62, 34)">
          <text x="-10" y="-3" fill="#dc2626" font-size="9.5" font-weight="900" text-anchor="end">PFK-2 (- 1 ATP)</text>
          <text x="-10" y="9" fill="#991b1b" font-size="8.5" font-weight="700" text-anchor="end">[Insulina activa]</text>
        </g>

        <!-- Flecha hacia arriba: Actividad FBPasa-2 (Glucagón) -->
        <line x1="230" y1="52" x2="230" y2="12" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arrowPurple)"/>
        <g transform="translate(238, 34)">
          <text x="10" y="-3" fill="#7c3aed" font-size="9.5" font-weight="900">FBPasa-2 (+ H₂O ➔ + Pi)</text>
          <text x="10" y="9" fill="#5b21b6" font-size="8.5" font-weight="700">[Glucagón/PKA activa]</text>
        </g>

        <!-- Estructura molecular de F-2,6-BP centrada -->
        <g transform="translate(100, 60)">
          {FRUCTOSA_2_6_BISFOSFATO}
          
          <g transform="translate(125, 24)">
            <g transform="translate(0, -18)">
              <rect x="0" y="0" width="42" height="18" rx="4" fill="#7c3aed" opacity="0.14"/>
              <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#7c3aed" stroke-width="1.4"/>
              <text x="21" y="13" fill="#7c3aed" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">6 C</text>
            </g>
            <text x="0" y="14" fill="#0f172a" font-size="13" font-weight="900">Fructosa-2,6-Bisfosfato (F-2,6-BP)</text>
            <text x="0" y="27" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">Señal alostérica potente</text>
          </g>
        </g>

        <!-- Consecuencia fisiológica explicada directamente -->
        <g transform="translate(0, 185)">
          <text x="0" y="0" fill="#047857" font-size="10.5" font-weight="900">
            EFECTO DEL AYUNO (GLUCAGÓN / ADRENALINA):
          </text>
          <text x="0" y="14" fill="#15803d" font-size="9.5" font-weight="700">
            FBPasa-2 degrada F-2,6-BP ➔ Caída de F-2,6-BP ➔ DESINHIBICIÓN DE FBPasa-1 ➔ VÍA GLUCONEOGÉNICA ACTIVA
          </text>
        </g>
      </g>
    </g>

    <!-- 4. LÍNEAS DE REGULACIÓN ALOSTÉRICA DIRECTAS: Conectan desde F-2,6-BP al borde derecho de FBPasa-1 y PFK-1 (terminando en X=1000 sin cruzar textos) -->
    <!-- Conexión 1: F-2,6-BP INHIBE ALOSTÉRICAMENTE FBPasa-1 -->
    <path d="M 1450 780 Q 1200 730 1005 730" fill="none" stroke="#dc2626" stroke-width="2.6" stroke-dasharray="6 4" marker-end="url(#markerInhibeRojo)"/>
    <text x="1220" y="722" fill="#dc2626" font-size="10" font-weight="900" text-anchor="middle">
      (-) Inhibe alostéricamente FBPasa-1 (Gluconeogénesis ↓)
    </text>

    <!-- Conexión 2: F-2,6-BP ACTIVA ALOSTÉRICAMENTE PFK-1 -->
    <path d="M 1450 795 Q 1200 785 1005 785" fill="none" stroke="#16a34a" stroke-width="2.6" stroke-dasharray="6 4" marker-end="url(#markerActivaVerde)"/>
    <text x="1220" y="780" fill="#16a34a" font-size="10" font-weight="900" text-anchor="middle">
      (+) Activa alostéricamente PFK-1 (Glucólisis ↑)
    </text>
    """)

    # -------------------------------------------------------------------------
    # 4. Fructosa-1,6-Bisfosfato (F-1,6-BP)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=860,
        nombre="Fructosa-1,6-Bisfosfato (F-1,6-BP)",
        carbonos="6 C",
        formula="C₆H₁₀O₁₂P₂⁴⁻ (Hexosa bisfosforilada)",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO,
        dx_texto=135,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 10: Aldolasa - Condensación Aldólica Reversible (3C + 3C -> 6C)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=980,
        enzima="Aldolasa A / B (Condensación Aldólica)",
        ec="EC 4.1.2.13 (Condensación reversible: 3 C + 3 C -> 6 C)",
        altura=45,
        reversible=True,
        num_paso=10,
        es_bypass=False,
        etiqueta_paso="PASO 10"
    ))

    # -------------------------------------------------------------------------
    # PRECURSOR 3: GLICEROL [3 C] - REORGANIZACIÓN COMPLETA
    # Incorporación directa a nivel de Triosas Fosfato (DHAP) con Glicerol-3-P
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- PRECURSOR 3: GLICEROL Y SU INCORPORACIÓN DIRECTA A DHAP VIA GLICEROL-3-FOSFATO -->
    <g transform="translate(60, 1050)">
      <!-- Encabezado del Precursor -->
      <g transform="translate(0, -18)">
        <rect x="0" y="0" width="42" height="18" rx="4" fill="#0284c7" opacity="0.14"/>
        <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#0284c7" stroke-width="1.4"/>
        <text x="21" y="13" fill="#0284c7" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
      </g>
      <text x="48" y="-4" fill="#0284c7" font-size="12" font-weight="900">PRECURSOR: GLICEROL</text>
      <text x="0" y="14" fill="#64748b" font-size="9.5">Origen: Lipólisis de Triglicéridos en Tejido Adiposo</text>

      <!-- 1. Molécula: Glicerol [3 C] -->
      <g transform="translate(0, 24)">
        {GLICEROL}
      </g>
      <g transform="translate(100, 48)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">Glicerol [3 C]</text>
        <text x="0" y="14" fill="#64748b" font-size="9.5">Lipólisis adiposa libera glicerol a sangre</text>
      </g>

      <!-- 2. Reacción: Glicerol Cinasa (GK) con gasto de 1 ATP -->
      <g transform="translate(50, 140)">
        <line x1="0" y1="0" x2="0" y2="40" stroke="#dc2626" stroke-width="2.4" marker-end="url(#arrowRed)"/>
        
        <!-- Curvas de ATP -> ADP -->
        <path d="M -60 10 Q -25 10 -4 18" fill="none" stroke="#dc2626" stroke-width="1.6" marker-end="url(#arrowRed)"/>
        <text x="-65" y="14" fill="#dc2626" font-size="10" font-weight="800" text-anchor="end">- 1 ATP</text>
        
        <path d="M -4 24 Q -25 32 -60 32" fill="none" stroke="#475569" stroke-width="1.6" marker-end="url(#arrowSlate)"/>
        <text x="-65" y="36" fill="#475569" font-size="10" font-weight="800" text-anchor="end">+ ADP</text>

        <g transform="translate(15, 16)">
          <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Glicerol Cinasa (GK)</text>
          <text x="0" y="12" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 2.7.1.30 (Hepática)</text>
        </g>
      </g>

      <!-- 3. Molécula: Glicerol-3-Fosfato [3 C] -->
      <g transform="translate(0, 200)">
        {GLICEROL_3_FOSFATO}
        <g transform="translate(100, 50)">
          <g transform="translate(0, -18)">
            <rect x="0" y="0" width="42" height="18" rx="4" fill="#0284c7" opacity="0.14"/>
            <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#0284c7" stroke-width="1.4"/>
            <text x="21" y="13" fill="#0284c7" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
          </g>
          <text x="0" y="14" fill="#0f172a" font-size="13" font-weight="800">Glicerol-3-Fosfato (G-3-P)</text>
          <text x="0" y="28" fill="#64748b" font-size="9.5">Intermediario fosforilado</text>
        </g>
      </g>

      <!-- 4. Reacción Redox: G3PDH (+ NAD+ -> + NADH + H+) y Conexión DIRECTA a DHAP -->
      <path d="M 60 330 Q 180 340 320 230 Q 360 190 390 120" fill="none" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>
      <g transform="translate(150, 310)">
        <text x="0" y="0" fill="#059669" font-size="11" font-weight="900">G3PDH Citosólica (EC 1.1.1.8)</text>
        <text x="0" y="14" fill="#047857" font-size="10.5" font-weight="800">+ NAD⁺ ➔ + NADH + H⁺</text>
        <text x="0" y="28" fill="#0284c7" font-size="9.5" font-weight="800">➔ ENTRADA DIRECTA A NIVEL DE TRIOSAS (DHAP)</text>
        <text x="0" y="40" fill="#64748b" font-size="9">Se incorpora a la ruta SIN pasar por Piruvato ni Mitocondria</text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # 5. Triosas Fosfato: DHAP y Gliceraldehído-3-P (Equilibrio por TPI)
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- TRIOSAS FOSFATO: DHAP Y GAP -->
    <g transform="translate(450, 1070)">
      {DIHIDROXIACETONA_FOSFATO}
      <g transform="translate(20, 120)">
        <rect x="0" y="-12" width="40" height="17" rx="4" fill="#ea580c" opacity="0.14"/>
        <rect x="0" y="-12" width="40" height="17" rx="4" fill="none" stroke="#ea580c" stroke-width="1.3"/>
        <text x="20" y="1" fill="#ea580c" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
      </g>
      <text x="40" y="140" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">DHAP</text>
      <text x="40" y="153" fill="#64748b" font-size="9" text-anchor="middle">Cetotriosa Fosfato</text>
    </g>

    <g transform="translate(750, 1070)">
      {GLICERALDEHIDO_3_FOSFATO}
      <g transform="translate(20, 120)">
        <rect x="0" y="-12" width="40" height="17" rx="4" fill="#ea580c" opacity="0.14"/>
        <rect x="0" y="-12" width="40" height="17" rx="4" fill="none" stroke="#ea580c" stroke-width="1.3"/>
        <text x="20" y="1" fill="#ea580c" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
      </g>
      <text x="40" y="140" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">Gliceraldehído-3-P</text>
      <text x="40" y="153" fill="#64748b" font-size="9" text-anchor="middle">Aldotriosa Fosfato</text>
    </g>

    <!-- Conexión y equilibrio TPI entre triosas -->
    <g transform="translate(575, 1105)">
      <line x1="0" y1="-3" x2="80" y2="-3" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <line x1="80" y1="3" x2="0" y2="3" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="40" y="-8" fill="#059669" font-size="10" font-weight="900" text-anchor="middle">TPI (Isomerasa)</text>
      <text x="40" y="18" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1 (Reversible)</text>
    </g>

    <!-- Flechas ascendentes convergiendo a Aldolasa -->
    <path d="M 500 1060 Q 590 1010 700 1025" fill="none" stroke="#059669" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
    <path d="M 780 1060 Q 750 1010 720 1025" fill="none" stroke="#059669" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
    """)

    # -------------------------------------------------------------------------
    # PASO 9: GAPDH - Reducción Reversa (Consume NADH citosólico)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 60, y=1260,
        enzima="GAPDH (Reducción Reversa)",
        ec="EC 1.2.1.12",
        altura=55,
        entra_energia="+ 2 NADH + 2 H⁺",
        sale_energia="+ 2 NAD⁺ + 2 Pi",
        nota_adicional="[Consume el NADH citosólico generado por la lanzadera de Malato (cMDH) / LDH / G3PDH]",
        reversible=True,
        num_paso=9,
        es_bypass=False,
        etiqueta_paso="PASO 9"
    ))

    # -------------------------------------------------------------------------
    # 6. 1,3-Bisfosfoglicerato (1,3-BPG)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE + 60, y=1345,
        nombre="1,3-Bisfosfoglicerato (1,3-BPG)",
        carbonos="3 C",
        formula="C₃H₄O₁₀P₂⁴⁻ (Acil-fosfato de alta energía)",
        svg_estructura=BISFOSFOGLICERATO_1_3,
        dx_texto=135,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 8: Fosfoglicerato Cinasa (PGK) - Reversible (Gasto de 2 ATP)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 60, y=1460,
        enzima="Fosfoglicerato Cinasa (PGK)",
        ec="EC 2.7.2.3",
        altura=50,
        entra_energia="- 2 ATP",
        sale_energia="+ 2 ADP",
        nota_adicional="[Invierte 2 ATP por cada molécula de glucosa generada]",
        reversible=True,
        num_paso=8,
        es_bypass=False,
        etiqueta_paso="PASO 8"
    ))

    # -------------------------------------------------------------------------
    # 7. 3-Fosfoglicerato (3-PG)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE + 60, y=1545,
        nombre="3-Fosfoglicerato (3-PG)",
        carbonos="3 C",
        formula="C₃H₄O₇P³⁻",
        svg_estructura=FOSFOGLICERATO_3,
        dx_texto=135,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 7: Fosfoglicerato Mutasa (PGM) - Reversible
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 60, y=1660,
        enzima="Fosfoglicerato Mutasa (PGM)",
        ec="EC 5.4.2.1",
        altura=50,
        reversible=True,
        num_paso=7,
        es_bypass=False,
        etiqueta_paso="PASO 7"
    ))

    # -------------------------------------------------------------------------
    # 8. 2-Fosfoglicerato (2-PG)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE + 60, y=1745,
        nombre="2-Fosfoglicerato (2-PG)",
        carbonos="3 C",
        formula="C₃H₄O₇P³⁻",
        svg_estructura=FOSFOGLICERATO_2,
        dx_texto=135,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 6: Enolasa - Hidratación Reversa
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 60, y=1860,
        enzima="Enolasa (Hidratación Reversa)",
        ec="EC 4.2.1.11",
        altura=50,
        entra_energia="+ H₂O",
        reversible=True,
        num_paso=6,
        es_bypass=False,
        etiqueta_paso="PASO 6"
    ))

    # -------------------------------------------------------------------------
    # 9. Fosfoenolpiruvato (PEP)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE + 60, y=1945,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 C",
        formula="C₃H₂O₆P³⁻ (Enol-fosfato de altísima energía)",
        svg_estructura=FOSFOENOLPIRUVATO,
        dx_texto=135,
        badge_color="#7c3aed"
    ))

    # -------------------------------------------------------------------------
    # PASO 5: BYPASS 1B - PEPCK Citosólica (PCK1)
    # Sustituye a la Piruvato Quinasa (PK) de la Glucólisis
    # Descarboxilación: - CO2 (4C - 1C -> 3C)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 60, y=2070,
        enzima="PEPCK Citosólica (PCK1)",
        ec="EC 4.1.1.32 (Fosforilación y descarboxilación concertada)",
        altura=60,
        entra_energia="- 1 GTP",
        sale_energia="+ GDP",
        delta_co2="- CO₂ (Descarboxilación: 4 C - 1 C -> 3 C)",
        inhibidores=["ADP (Baja carga energética desvía OAA a Krebs)"],
        nota_adicional="[Inducción génica: Glucagón y Cortisol (CREB/FOXO1) inducen síntesis de PEPCK]",
        reversible=False,
        num_paso=5,
        es_bypass=True,
        titulo_bypass="BYPASS 1B",
        sustituye_glucolisis="Piruvato Quinasa (PK) de la glucólisis"
    ))

    # -------------------------------------------------------------------------
    # RÓTULO DIRECTO DEL BALANCE DE CARBONOS DEL BYPASS 1
    # -------------------------------------------------------------------------
    svg_parts.append("""
    <g transform="translate(340, 2030)">
      <text x="0" y="0" fill="#047857" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace">
        BALANCE DE CARBONOS BYPASS 1:
      </text>
      <text x="0" y="15" fill="#047857" font-size="10" font-family="'JetBrains Mono', monospace">
        3 C (Piruvato) + CO₂ (PC) -> 4 C (OAA) - CO₂ (PEPCK) -> 3 C (PEP)
      </text>
      <text x="0" y="28" fill="#15803d" font-size="9.5" font-weight="700">
        El esqueleto de 3 carbonos del precursor se conserva intacto en el balance neto
      </text>
    </g>
    """)

    # -------------------------------------------------------------------------
    # 10. Oxalacetato Citosólico (OAA Citosólico) [4 C]
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE + 60, y=2175,
        nombre="Oxalacetato (OAA Citosólico)",
        carbonos="4 C",
        formula="C₄H₂O₅²⁻ (Dicarboxilato de 4 C)",
        svg_estructura=OXALACETATO,
        dx_texto=105,
        badge_color="#7c3aed"
    ))

    # -------------------------------------------------------------------------
    # 11. L-Malato Citosólico [4 C]
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=220, y=2175,
        nombre="L-Malato (Citosólico)",
        carbonos="4 C",
        formula="C₄H₄O₅²⁻",
        svg_estructura=MALATO,
        texto_izquierda=True,
        badge_color="#047857"
    ))

    # -------------------------------------------------------------------------
    # PASO 4: cMDH (Malato Deshidrogenasa Citosólica)
    # Regenera NADH citosólico imprescindible para GAPDH
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- PASO 4: MDH CITOSÓLICA (cMDH) -->
    <g transform="translate(340, 2235)">
      <line x1="0" y1="0" x2="370" y2="0" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>
      {badge_paso(4, 25, 0, es_bypass=False, etiqueta="")}

      <g transform="translate(185, -12)">
        <text x="0" y="-12" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#6d28d9" text-anchor="middle">cMDH (MDH Citosólica)</text>
        <text x="0" y="2" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#0284c7" text-anchor="middle">Exportación de equivalentes reductores: regenera NADH para GAPDH</text>
        <text x="0" y="22" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#059669" text-anchor="middle">+ NAD⁺ -> + NADH + H⁺</text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # PASO 3: Transporte Transmembrana de Malato vía Carrier OGC (SLC25A11)
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- PASO 3: SALIDA POR CARRIER OGC (TRANSPORTE FÍSICO) -->
    <path d="M 220 3180 L 220 2680 Q 220 2660 220 2480 L 220 2270" fill="none" stroke="#047857" stroke-width="3" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>
    {badge_paso(3, 220, 2620, es_bypass=False, etiqueta="")}
    <g transform="translate(245, 2585)">
      <text x="0" y="0" fill="#047857" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Transporte Físico OGC (Antiporte Malato²⁻ / α-KG²⁻)</text>
      <text x="0" y="13" fill="#15803d" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">SLC25A11: exporta esqueleto de 4C y equivalente reductor (NADH) al citosol</text>
      <text x="0" y="26" fill="#64748b" font-size="9" font-family="'Inter', sans-serif">La MMI es completamente impermeable al Oxaloacetato</text>
    </g>
    """)

    # -------------------------------------------------------------------------
    # PRECURSORES CITOSÓLICOS: L-LACTATO (CICLO DE CORI) Y L-ALANINA (CICLO DE CAHILL)
    # Reorganizados con conexión funcional a músculo e hígado, convergencia en Piruvato
    # -------------------------------------------------------------------------

    # PRECURSOR 1: L-Lactato [3 C] (Ciclo de Cori Músculo-Hígado)
    svg_parts.append(f"""
    <!-- PRECURSOR 1: L-LACTATO Y CICLO DE CORI -->
    <g transform="translate(1060, 2150)">
      <!-- Encabezado con Carbonos -->
      <g transform="translate(0, -18)">
        <rect x="0" y="0" width="42" height="18" rx="4" fill="#7c3aed" opacity="0.14"/>
        <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#7c3aed" stroke-width="1.4"/>
        <text x="21" y="13" fill="#7c3aed" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
      </g>
      <text x="48" y="-4" fill="#7c3aed" font-size="12" font-weight="900">PRECURSOR: L-LACTATO</text>
      <text x="0" y="14" fill="#0284c7" font-size="10" font-weight="800">Ciclo de Cori (Intercambio Funcional Músculo ⇄ Hígado)</text>
      <text x="0" y="26" fill="#64748b" font-size="9">Glucólisis anaerobia en eritrocito/músculo genera lactato ➔ sangre ➔ hígado</text>

      <!-- Molécula de Lactato con estructura completa -->
      <g transform="translate(0, 36)">
        {LACTATO}
      </g>

      <!-- Reacción de la Lactato Deshidrogenasa (LDH) -->
      <g transform="translate(115, 56)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">L-Lactato [3 C]</text>
        <text x="0" y="16" fill="#7c3aed" font-size="11" font-weight="800">LDH (Lactato Deshidrogenasa / EC 1.1.1.27)</text>
        <text x="0" y="30" fill="#059669" font-size="11" font-weight="900">+ NAD⁺ ➔ + NADH + H⁺</text>
        <text x="0" y="44" fill="#047857" font-size="9.5" font-weight="700">Genera NADH citosólico imprescindible para GAPDH</text>
      </g>

      <!-- Flecha diagonal convergente hacia Piruvato citosólico -->
      <path d="M 60 145 Q 120 190 160 225" fill="none" stroke="#7c3aed" stroke-width="2.4" marker-end="url(#arrowPurple)"/>
      <text x="120" y="180" fill="#7c3aed" font-size="10" font-weight="800">LDH ➔ Piruvato</text>
    </g>
    """)

    # PRECURSOR 2: L-Alanina [3 C] (Ciclo Glucosa-Alanina / Cahill)
    svg_parts.append(f"""
    <!-- PRECURSOR 2: L-ALANINA Y CICLO DE CAHILL -->
    <g transform="translate(1500, 2150)">
      <!-- Encabezado con Carbonos -->
      <g transform="translate(0, -18)">
        <rect x="0" y="0" width="42" height="18" rx="4" fill="#ea580c" opacity="0.14"/>
        <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#ea580c" stroke-width="1.4"/>
        <text x="21" y="13" fill="#ea580c" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
      </g>
      <text x="48" y="-4" fill="#ea580c" font-size="12" font-weight="900">PRECURSOR: L-ALANINA</text>
      <text x="0" y="14" fill="#b45309" font-size="10" font-weight="800">Ciclo Glucosa-Alanina / Cahill (Proteólisis Muscular)</text>
      <text x="0" y="26" fill="#64748b" font-size="9">Exporta nitrógeno al Ciclo de la Urea y esqueleto carbonado a Glucosa</text>

      <!-- Molécula de Alanina con estructura completa -->
      <g transform="translate(0, 36)">
        {AMINO_ALANINA}
      </g>

      <!-- Reacción de la Alanina Aminotransferasa (ALT) -->
      <g transform="translate(115, 56)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">L-Alanina [3 C]</text>
        <text x="0" y="16" fill="#ea580c" font-size="11" font-weight="800">ALT (Alanina Aminotransferasa / EC 2.6.1.2)</text>
        <text x="0" y="30" fill="#0284c7" font-size="10.5" font-weight="900">+ α-Cetoglutarato ➔ + L-Glutamato</text>
        <text x="0" y="44" fill="#4338ca" font-size="9.5" font-weight="700">Transferencia del grupo amino (⁺NH₃) hacia la Urea</text>
      </g>

      <!-- Flecha diagonal convergente hacia Piruvato citosólico -->
      <path d="M 20 145 Q -70 190 -170 225" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="-95" y="180" fill="#ea580c" font-size="10" font-weight="800">ALT ➔ Piruvato</text>
    </g>
    """)

    # -------------------------------------------------------------------------
    # CONVERGENCIA EN CITOSOL: Piruvato Citosólico [3 C] alineado en X=1280
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- METABOLITO: PIRUVATO CITOSÓLICO [3 C] (PUNTO DE CONVERGENCIA) -->
    <g transform="translate(1255, 2380)">
      {PIRUVATO}
      <g transform="translate(100, 24)">
        <g transform="translate(0, -18)">
          <rect x="0" y="0" width="42" height="18" rx="4" fill="#ea580c" opacity="0.14"/>
          <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#ea580c" stroke-width="1.4"/>
          <text x="21" y="13" fill="#ea580c" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
        </g>
        <text x="0" y="14" fill="#0f172a" font-size="14" font-weight="900">Piruvato (Citosólico) [3 C]</text>
        <text x="0" y="28" fill="#0369a1" font-size="10" font-weight="800">Convergencia de Precursores (Lactato y Alanina)</text>
      </g>
    </g>

    <!-- Flecha descendente directa que cruza el transportador MPC en X=1280 -->
    <line x1="1280" y1="2470" x2="1280" y2="2735" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    """)

