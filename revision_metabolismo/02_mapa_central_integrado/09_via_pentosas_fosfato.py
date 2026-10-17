# =============================================================================
# MÓDULO DE REVISIÓN: Vía 4: Vía de las Pentosas Fosfato
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 1724 a 1828 de 4188)
# Descripción      : Fase oxidativa productora de NADPH y fase no oxidativa de interconversión de azúcares.
# =============================================================================

    # =========================================================================
    # 5. DERECHA: VÍA DE LAS PENTOSAS FOSFATO (LIBRE EN CITOSOL)
    # =========================================================================
    x_p_center = 2680
    x_p_left = 2520
    x_p_right = 2840
    partes.append(f'<g id="ruta_pentosas">')

    # Badges de la vía y fase oxidativa
    partes.append(badge_via(4, 2520, 144))
    partes.append(f'''
    <g transform="translate({x_p_center - 110}, 144)">
      <rect x="0" y="0" width="220" height="20" rx="10" fill="#d1fae5" stroke="#059669" stroke-width="1.5"/>
      <text x="110" y="14" fill="#047857" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">FASE OXIDATIVA (IRREVERSIBLE)</text>
    </g>
    ''')

    # Entrada G6PDH desde G6P citosólica con cofactores (NADP⁺ ➔ NADPH + H⁺)
    partes.append(f"""
    <g id="rx_g6pdh" data-arrastrable="1">
      <path d="M {x_g + 265} {y_g + paso_y + 35} Q 2200 170 {x_p_center - 35} 200" fill="none" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>
      <text x="2220" y="156" fill="#0f172a" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Glucosa-6-P Deshidrogenasa (G6PDH)</text>
      <!-- Curva entrada NADP⁺ -->
      <path d="M 2150 195 Q 2175 195 2190 230" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="2140" y="199" fill="#475569" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ NADP⁺</text>
      <!-- Curva salida NADPH + H⁺ -->
      <path d="M 2260 225 Q 2280 260 2310 260" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="2320" y="264" fill="#059669" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="start">+ NADPH + H⁺</text>
    </g>
    """)

    # 1. 6-P-Gluconolactona
    partes.append(etiqueta_regulacion("g6pdh", x_p_center - 110, 240, dx=0, dy=0, anchor="end"))
    partes.append(nodo_libre(x_p_center, 195, "6-P-Gluconolactona", "6C", FOSFOGLUCONO_LACTONA_6, "m_lactona", text_right=True, dx=115))
    partes.append(reaccion_libre(x_p_center + 45, 285, 36, "6-Fosfogluconolactonasa", entra="+ H₂O", id_rx="rx_lactonasa"))

    # 2. 6-Fosfogluconato
    partes.append(nodo_libre(x_p_center, 330, "6-Fosfogluconato", "6C", FOSFOGLUCONATO_6, "m_6pg", text_right=True, dx=115))
    partes.append(reaccion_libre(x_p_center + 45, 468, 38, "6-Fosfogluconato DH", entra="+ NADP⁺", sale="+ NADPH + CO₂", es_ganancia=True, id_rx="rx_6pgdh"))

    # 3. Ribulosa-5-P (Punto de confluencia y ramificación)
    partes.append(nodo_libre(x_p_center, 510, "Ribulosa-5-P", "5C", RIBULOSA_5_FOSFATO, "m_ru5p", text_right=True, dx=115))

    # Badge Rama Ribosa (Morada)
    partes.append(f'''
    <g transform="translate({x_p_right - 40}, 625)">
      <rect x="0" y="0" width="190" height="18" rx="9" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.4"/>
      <text x="95" y="13" fill="#6d28d9" font-size="8" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">PRECURSOR DE NUCLEÓTIDOS (PRPP)</text>
    </g>
    ''')

    # Ramas: Xilulosa-5P (izquierda) y Ribosa-5P (derecha)
    partes.append(f"""
    <path d="M {x_p_center - 20} 635 L {x_p_left + 45} 670" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
    <text x="{x_p_left + 15}" y="650" fill="#047857" font-size="9" font-family="'Inter', sans-serif" text-anchor="middle">Epimerasa</text>

    <path d="M {x_p_center + 20} 635 L {x_p_right + 45} 670" stroke="#7c3aed" stroke-width="2.4" marker-end="url(#arrowPurple)"/>
    <text x="{x_p_right + 85}" y="650" fill="#6d28d9" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Isomerasa</text>
    """)

    # -------------------------------------------------------------------------
    # FASE NO OXIDATIVA: REORDENAMIENTO ESTEQUIOMÉTRICO (3 NIVELES DESPEJADOS)
    # -------------------------------------------------------------------------
    # Nivel 0: Xilulosa-5-P (izquierda) y Ribosa-5-P (derecha)
    partes.append(nodo_libre(x_p_left, 675, "Xilulosa-5-P", "5C", XILULOSA_5_FOSFATO, "m_xu5p", text_right=False, dx=-15, dy=25, detalle="[Regulador] ChREBP"))
    partes.append(nodo_libre(x_p_right, 675, "Ribosa-5-P", "5C", RIBOSA_5_FOSFATO, "m_r5p", text_right=True, dx=115, dy=25, detalle="Precursora PRPP / ADN"))

    # Paso 1: Transcetolasa 1 (TK1) con flechas de convergencia/divergencia de 2C
    partes.append(f"""
    <g id="rx_tk1_pnt" data-arrastrable="1" transform="translate({x_p_center - 60}, 740)">
      <path d="M -22 -2 L -4 12 M 22 -2 L 4 12 M -4 28 L -22 42 M 4 28 L 22 42" fill="none" stroke="#ea580c" stroke-width="1.6"/>
      <line x1="-3" y1="0" x2="-3" y2="40" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="40" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(24, 10)">
        <text x="0" y="0" fill="#0f172a" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">Transcetolasa 1 (TK1, 2C)</text>
        <text x="0" y="13" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">EC 2.2.1.1 (TPP) • +GAP [3C]</text>
        <text x="0" y="25" fill="#c2410c" font-size="8.5" font-weight="700">X5P + R5P ⇄ S7P + GAP</text>
      </g>
    </g>
    """)

    # Nivel 1: Sedoheptulosa-7-P (7C, izq) y Eritrosa-4-P (4C, der)
    partes.append(nodo_libre(x_p_left, 835, "Sedoheptulosa-7-P", "7C", SEDOHEPTULOSA_7_FOSFATO, "m_s7p", text_right=False, dx=-15, dy=25, detalle="Intermediario 7C (de TK1)"))
    partes.append(nodo_libre(x_p_right, 835, "Eritrosa-4-P", "4C", ERITROSA_4_FOSFATO, "m_e4p", text_right=True, dx=115, dy=25, detalle="De TA (S7P+GAP) • Precursor AA"))

    # Paso 2 y 3: Transaldolasa (TA) y Transcetolasa 2 (TK2) con flechas de convergencia/divergencia
    partes.append(f"""
    <g id="rx_ta_pnt" data-arrastrable="1" transform="translate({x_p_center - 60}, 900)">
      <path d="M -22 -2 L -4 12 M 22 -2 L 4 12 M -4 28 L -22 42 M 4 28 L 22 42" fill="none" stroke="#ea580c" stroke-width="1.6"/>
      <line x1="-3" y1="0" x2="-3" y2="40" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="40" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(24, 10)">
        <text x="0" y="0" fill="#0f172a" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">Transaldolasa (3C) + TK2 (2C)</text>
        <text x="0" y="13" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">EC 2.2.1.2 / EC 2.2.1.1 (TPP)</text>
        <text x="0" y="25" fill="#c2410c" font-size="8.5" font-weight="700">S7P+GAP+X5P ⇄ 2 F6P + GAP</text>
      </g>
    </g>
    """)

    # Nivel 2: Productos finales de reingreso al eje glucolítico
    partes.append(nodo_libre(x_p_left, 995, "Fructosa-6-P (x2)", "6C", PENTOSAS_F6P, "m_f6p_pnt", text_right=False, dx=-36, dy=25, detalle="➔ Glucólisis"))
    partes.append(nodo_libre(x_p_right, 995, "Gliceraldehído-3-P", "3C", PENTOSAS_GAP, "m_gap_pnt", text_right=False, dx=-15, dy=25, detalle="➔ Reingreso a Glucólisis"))

    partes.append('</g>')

