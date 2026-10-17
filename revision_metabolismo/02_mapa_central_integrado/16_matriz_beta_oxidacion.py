# =============================================================================
# MÓDULO DE REVISIÓN: Vía 9: Beta-Oxidación Mitocondrial
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 2580 a 2662 de 4188)
# Descripción      : Lanzadera de carnitina (CPT-I/CAT/CPT-II) y los 4 pasos recurrentes de la espiral de Lynen.
# =============================================================================

    # =========================================================================
    # 10. LÍPIDOS: BETA-OXIDACIÓN (MATRIZ MITOCONDRIAL)
    # =========================================================================
    x_box = 180
    y_box = y_mito + 100
    paso_b = 160
    partes.append(f'<g id="ruta_beta_ox">')
    partes.append(badge_via(9, x_box - 20, y_box - 1220))
    

    # Sangre -> Citosol -> Mitocondria
    # Palmitato en sangre (unido a Albúmina dentro del torrente vascular superior)
    x_palm_sangre = 510
    partes.append(nodo_libre(x_palm_sangre, 24, "Palmitato (Sanguíneo / Albúmina)", "16C", PALMITATO_LIBRE, "m_palmitato_sangre", text_right=True, dx=265))
    
    # Cruce de la membrana plasmática hacia citosol por transportador CD36 / FAT
    partes.append(f'''
    <path d="M 500 98 L {x_box + 20} {y_box - 1220}" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <g transform="translate(460, 68)">
      <rect x="0" y="0" width="80" height="26" rx="6" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <text x="40" y="17" fill="#ffffff" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CD36/FAT</text>
    </g>
    <text x="550" y="110" fill="#0284c7" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">Captación celular ➔</text>
    ''')
    
    # 1. Palmitato Citosólico
    partes.append(nodo_libre(x_box, y_box - 1200, "Palmitato (Citosólico)", "16C", PALMITATO_LIBRE, "m_palmitato_cito", text_right=True, dx=265))
    partes.append(reaccion_libre(x_box + 60, y_box - 1200 + 80, 50, "Acil-CoA Sintetasa (ACS)", entra="+ ATP + CoA", sale="+ AMP + PPi", id_rx="rx_acs"))
    
    # 2. Palmitoil-CoA Citosólico (Nombre encima de la estructura)
    partes.append(nodo_libre(x_box, y_box - 800, "Palmitoil-CoA (Citosólico)", "16C", PALMITOIL_COA, "m_palmitoil_cito", text_pos="top", dx=110, dy=-22))
    partes.append(reaccion_libre(x_box + 60, y_box - 800 + 80, 50, "CPT-1 (Lanzadera de Carnitina)", entra="+ Carnitina", sale="- CoA", id_rx="rx_cpt1"))
    partes.append(etiqueta_regulacion("cpt1", x_box + 260, y_box - 800 + 90, dx=0, dy=0))
    
    # 3. Palmitoil-Carnitina (Espacio Citosol / EIM exterior)
    partes.append(nodo_libre(x_box, y_box - 280, "Palmitoil-Carnitina", "16C", PALMITOIL_CARNITINA, "m_palm_carnitina", text_right=True, dx=145))
    
    # Cruce del Espacio Intermembrana (EIM) e inserción de CACT directamente incrustado en la Membrana Mitocondrial Interna (MMI)
    x_cact = 240
    y_cact = 2305
    partes.append(f'''
    <!-- Lanzadera de Carnitina: Transportador CACT en la MMI -->
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
    partes.append(nodo_libre(x_box, y_m_palm + 35, "Palmitoil-CoA (Matriz)", "16C", PALMITOIL_COA, "m_palmitoil", text_pos="top", dx=110, dy=-20))
    partes.append(reaccion_libre(x_box + 60, y_m_palm + 105, 42, "Acil-CoA DH", entra="+ FAD", sale="+ FADH2", es_ganancia=True, id_rx="rx_box1"))
    
    # 5. trans-Δ²-Enoil-CoA (Paso añadido)
    y_m_enoil = y_m_palm + 140
    partes.append(nodo_libre(x_box, y_m_enoil, "trans-Δ²-Enoil-CoA", "16C", TRANS_DELTA2_ENOIL_COA, "m_trans_enoil", text_right=True, dx=265))
    partes.append(reaccion_libre(x_box + 60, y_m_enoil + 70, 42, "Enoil-CoA Hidratasa", entra="+ H₂O", id_rx="rx_box1b"))

    # 6. L-β-Hidroxiacil-CoA
    y_m_hidro = y_m_enoil + 140
    partes.append(nodo_libre(x_box, y_m_hidro, "L-β-Hidroxiacil-CoA", "16C", L_BETA_HIDROXIACIL_COA, "m_hidroxi_coa", text_right=True, dx=210))
    partes.append(reaccion_libre(x_box + 60, y_m_hidro + 70, 42, "β-Hidroxiacil-CoA DH", entra="+ NAD+", sale="+ NADH + H+", es_ganancia=True, id_rx="rx_box2"))
    
    # 7. β-Cetoacil-CoA
    y_m_ceto = y_m_hidro + 140
    partes.append(nodo_libre(x_box, y_m_ceto, "β-Cetoacil-CoA", "16C", BETA_CETOACIL_COA, "m_cetoacil_coa", text_right=True, dx=265))
    partes.append(reaccion_libre(x_box + 60, y_m_ceto + 70, 42, "Tiolasa", entra="+ CoA", id_rx="rx_box3"))
    
    # 8. Clivaje tiolítico: Acetil-CoA y Miristoil-CoA
    y_m_split = y_m_ceto + 160
    partes.append(nodo_libre(85, y_m_split, "Acetil-CoA", "2C", ACETIL_COA_BETA, "m_acetil_coa_beta", text_pos="top", dx=50, dy=65))
    partes.append(nodo_libre(230, y_m_split, "Miristoil-CoA", "14C", MIRISTOIL_COA, "m_miristoil_coa", text_pos="top", dx=95, dy=-16))
    
    partes.append(f"""
    <path d="M {x_box+60} {y_m_ceto + 115} L 135 {y_m_split - 22}" stroke="#ea580c" stroke-width="2.6" fill="none" marker-end="url(#arrowFlow)"/>
    <path d="M {x_box+60} {y_m_ceto + 115} L 270 {y_m_split - 22}" stroke="#ea580c" stroke-width="2.6" fill="none" marker-end="url(#arrowFlow)"/>
    """)
    partes.append(f'</g>')

