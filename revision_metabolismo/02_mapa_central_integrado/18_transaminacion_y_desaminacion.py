# =============================================================================
# MÓDULO DE REVISIÓN: Vía 13: Transaminación y Desaminación Oxidativa
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 2706 a 2866 de 4188)
# Descripción      : Embudo colector de grupos amino (ALT, AST, PLP) y desaminación por GDH.
# =============================================================================

    # =========================================================================
    # 12. METABOLISMO DEL NITRÓGENO Y AMINOÁCIDOS: TRANSAMINACIÓN Y DESAMINACIÓN
    # =========================================================================
    x_aa = 2140
    y_aa = 380
    partes.append(f'<g id="ruta_transaminacion_desaminacion">')
    partes.append(badge_via(13, x_aa - 190, 170))

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
    partes.append(nodo_libre(x_aa, y_aa, "L-Alanina", "3C", AMINO_ALANINA, "m_ala_integ", text_pos="top", dy=-20))

    # Reacción ALT / GPT (Alanina + α-KG ⇄ Piruvato + Glutamato)
    partes.append(f'''
    <g id="rx_alt_integ" data-arrastrable="1" transform="translate({x_aa}, {y_aa + 115})">
      <line x1="-3" y1="0" x2="-3" y2="75" stroke="#0d9488" stroke-width="2" marker-end="url(#arrowTeal)"/>
      <line x1="3" y1="75" x2="3" y2="0" stroke="#0d9488" stroke-width="2" marker-end="url(#arrowTeal)"/>
      <!-- Arco de recolección de nitrógeno acoplado con α-KG ➔ Glutamato -->
      <path d="M 65 10 Q 15 38 65 65" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrowBlueAmino)"/>
      <text x="70" y="-4" fill="#64748b" font-size="9.5" font-family="'Inter', sans-serif">α-Cetoglutarato</text>
      <text x="70" y="72" fill="#1d4ed8" font-size="10" font-weight="800" font-family="'Inter', sans-serif">Glutamato</text>

      <g transform="translate(-15, 38)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">ALT / GPT</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 2.6.1.2 (PLP)</text>
      </g>
    </g>
    ''')

    # 3. Piruvato resultante de ALT en citosol
    partes.append(nodo_libre(x_aa, y_aa + 230, "Piruvato (de Alanina)", "3C", PIRUVATO, "m_pyr_ala_integ", text_right=True, dx=110))

    # Conexión directa hacia la Glucólisis
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <text x="{x_aa + 30}" y="{y_aa + 305}" fill="#c2410c" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Pool de Piruvato (➔ MPC) ↓</text>
        <path d="M {x_aa} {y_aa + 320} C 1960 {y_aa + 345}, 1960 800, 1960 1550 C 1960 1630, 1920 1675, 1880 1675" fill="none" stroke="#ea580c" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowFlow)"/>
        ''')

    # 4. L-Glutamato (colector común de nitrógeno en citosol - centrado en X=2280 con texto superior)
    partes.append(nodo_libre(2280, y_aa + 380, "L-Glutamato", "5C", AMINO_GLUTAMATO, "m_glu_integ", text_pos="top", dy=-18))

    # 5. Rama Citosólica de Glutamina Sintetasa (Destoxificación a Glutamina)
    partes.append(nodo_libre(2280, y_aa + 630, "L-Glutamina", "5C", AMINO_GLUTAMINA, "m_gln_integ", text_pos="top", dx=70, dy=-38, detalle="Destino: Torrente Sanguíneo"))
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

    # Exportación de Glutamina al torrente sanguíneo
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <path d="M 2340 {y_aa + 640} Q 2420 {y_aa + 640} 2420 850 L 2420 74" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
        <text x="2435" y="520" fill="#0f766e" font-size="11" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 2435 520)">EXPORTACIÓN DE GLUTAMINA A SANGRE ➔</text>
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
    ''')
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <path d="M 2240 {y_aa + 400} C 2220 {y_aa + 440}, 2220 950, 2220 1200 C 2220 1500, {x_agc} 1750, {x_agc} {y_agc - 18}" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
        <path d="M {x_agc} {y_agc + 22} L {x_agc} {y_gldh_start - 10}" fill="none" stroke="#0d9488" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowTeal)"/>
        ''')

    # 7. MATRIZ MITOCONDRIAL: Glutamato en la Matriz (elevado para no interferir con Krebs->CTE)
    partes.append(nodo_libre(x_agc - 40, y_gldh_start, "L-Glutamato (Matriz)", "5C", AMINO_GLUTAMATO, "m_glu_mito_integ", text_right=True, dx=145))

    # Reacción GLDH (Glutamato Deshidrogenasa) - Arquitectura espaciosa y despejada
    partes.append(f'''
    <g id="rx_gldh_integ" data-arrastrable="1" transform="translate({x_agc + 10}, {y_gldh_start + 135})">
      <line x1="-3" y1="0" x2="-3" y2="70" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
      <line x1="3" y1="70" x2="3" y2="0" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
      
      <!-- Entrada NAD(P)+ / Salida NAD(P)H en arco izquierdo despejado -->
      <path d="M -90 10 Q -35 10 -4 20" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-95" y="14" fill="#059669" font-size="9.5" font-weight="800" text-anchor="end">+ NAD(P)⁺ + H₂O</text>
      
      <path d="M -4 46 Q -35 56 -90 56" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-95" y="60" fill="#059669" font-size="9.5" font-weight="800" text-anchor="end">+ NAD(P)H + H⁺</text>

      <!-- Salida de Amonio libre hacia la derecha -->
      <path d="M 4 35 Q 60 35 120 60" fill="none" stroke="#2563eb" stroke-width="2.4" marker-end="url(#arrowBlueAmino)"/>
      <text x="125" y="68" fill="#1d4ed8" font-size="11" font-weight="900" font-family="'Inter', sans-serif">➔ + NH₄⁺</text>

      <!-- Textos y Alosterismo a la derecha bien despejados -->
      <g transform="translate(45, -10)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif">Glutamato Deshidrogenasa (GLDH)</text>
        <text x="0" y="14" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">EC 1.4.1.3 (Mitocondrial)</text>
        <text x="0" y="27" fill="#16a34a" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">(+) ADP, GDP (activa)</text>
        <text x="0" y="39" fill="#e11d48" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">(-) ATP, GTP (inhibe)</text>
      </g>
    </g>
    ''')

    # 8. Productos de GLDH:
    # A. α-Cetoglutarato regenerado en matriz mitocondrial (hacia la izquierda, espaciado a X=x_agc - 260)
    partes.append(nodo_libre(x_agc - 260, y_gldh_start + 225, "α-Cetoglutarato", "5C", AMINO_AKG, "m_akg_gldh_integ", text_right=False, dx=-30))
    # Ramificación de la flecha de GLDH hacia la estructura de α-Cetoglutarato
    partes.append(f'''
    <path d="M {x_agc - 5} {y_gldh_start + 205} Q {x_agc - 80} {y_gldh_start + 245} {x_agc - 150} {y_gldh_start + 245}" fill="none" stroke="#0d9488" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
    ''')
    # Conexión directa hacia el Ciclo de Krebs
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <path d="M {x_agc - 260} {y_gldh_start + 270} C 1720 2520, 1500 2550, 1420 2620 C 1370 2660, 1330 2710, {x_k + 160} {y_k + paso_k * 3 - 10}" fill="none" stroke="#b45309" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowFlow)"/>
        <text x="1650" y="2520" fill="#78350f" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">➔ Reingreso al Ciclo de Krebs (α-KG)</text>
        ''')

    # B. Ion Amonio (NH4+) libre en matriz (hacia la derecha, espaciado a X=x_agc + 160)
    partes.append(nodo_libre(x_agc + 170, y_gldh_start + 225, "Ion Amonio (NH₄⁺)", "Nitrógeno", AMINO_NH4, "m_nh4_integ", text_right=True, dx=85))
    # Conexión directa hacia el Ciclo de la Urea
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <!-- Canal conductor de Amonio hacia CPS-1 -->
        <g id="canal_amonio_hacia_urea" data-arrastrable="1">
          <path d="M {x_agc + 190} {y_gldh_start + 185} Q {x_agc + 230} {y_gldh_start + 200} {x_agc + 230} 2520 L {x_agc + 230} 3360 Q {x_agc + 230} 3380 {x_agc + 250} 3380 L 4120 3380 Q 4140 3380 4140 3340 L 4140 3260" fill="none" stroke="#2563eb" stroke-width="3" stroke-dasharray="8 5" marker-end="url(#arrowBlueAmino)"/>
          <g transform="translate(3050, 3368)">
            <rect x="-195" y="-13" width="390" height="26" rx="8" fill="#1e293b" opacity="0.9" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="0" y="4" fill="#93c5fd" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CANAL MATRICIAL DE NH₄⁺ ➔ SÍNTESIS DE UREA (CPS-1)</text>
          </g>
        </g>
        ''')

    partes.append(f'</g>')

