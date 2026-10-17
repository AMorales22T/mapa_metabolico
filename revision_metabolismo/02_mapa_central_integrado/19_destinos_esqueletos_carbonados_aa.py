# =============================================================================
# MÓDULO DE REVISIÓN: Vía 12B: Destinos de los Esqueletos Carbonados de los 20 AA
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 2867 a 3095 de 4188)
# Descripción      : Clasificación glucogénica/cetogénica y ruta del propionil-CoA -> D/L-metilmalonil-CoA -> succinil-CoA.
# =============================================================================

    # =========================================================================
    # 12B. DESTINOS DE LOS ESQUELETOS CARBONADOS DE AMINOÁCIDOS (VÍA 12B)
    # =========================================================================
    partes.append(f'<g id="ruta_destinos_aa">')

    # 1. Rótulo principal de la Vía 12B en corredor citosólico central
    partes.append(badge_via("12B", 2480, 1195))
    partes.append(f'''
    <g id="banner_destinos_aa" data-arrastrable="1" transform="translate(2660, 1195)">
      <rect x="-165" y="-14" width="330" height="28" rx="14" fill="#fdf4ff" stroke="#a855f7" stroke-width="1.8"/>
      <text x="0" y="4" fill="#7e22ce" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
        DESTINOS DE ESQUELETOS CARBONADOS (20 AA)
      </text>
    </g>
    ''')

    # -------------------------------------------------------------------------
    # A. CASCADA AROMÁTICA CITOSÓLICA (Phe ➔ Tyr ➔ Fumarato + Acetoacetato)
    # (Zona despejada: X ≈ 2480 - 2680, Y ≈ 1240 - 1840)
    # -------------------------------------------------------------------------
    # L-Fenilalanina
    partes.append(nodo_libre(2480, 1250, "L-Fenilalanina", "9C", AA_FENILALANINA, "m_phe_aa", text_right=True, dx=115, detalle="Esencial • Mixto"))

    # Reacción PAH (Fenilalanina Hidroxilasa)
    partes.append(f'''
    <g id="rx_pah" data-arrastrable="1" transform="translate(2520, 1410)">
      <line x1="0" y1="0" x2="0" y2="55" stroke="#9333ea" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <path d="M 12 12 Q 35 12 40 28" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="45" y="24" fill="#0284c7" font-size="8.5" font-weight="800">+ O₂ + BH₄ ➔ H₂O + BH₂</text>
      <g transform="translate(-15, 28)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Fenilalanina Hidroxilasa (PAH)</text>
        <text x="0" y="13" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 1.14.16.1 (BH₄)</text>
      </g>
    </g>
    ''')
    partes.append(badge_clinico(2530, 1455, "[Clínica] PKU • Déficit PAH / BH₄", es_alerta=True))

    # L-Tirosina
    partes.append(nodo_libre(2480, 1500, "L-Tirosina", "9C", AA_TIROSINA, "m_tyr_aa", text_right=True, dx=115, detalle="Condicionalmente esencial"))

    # Cascada catabólica: HGD y FAH
    partes.append(f'''
    <g id="rx_tirosina_catabolismo" data-arrastrable="1" transform="translate(2520, 1690)">
      <line x1="0" y1="0" x2="0" y2="65" stroke="#9333ea" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="-15" y="20" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Homogentisato 1,2-Dioxigenasa (HGD)</text>
      <text x="-15" y="32" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 1.13.11.5</text>
      <text x="-15" y="50" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Fumarilacetoacetasa (FAH)</text>
      <text x="-15" y="62" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 3.7.1.2</text>
    </g>
    ''')
    partes.append(badge_clinico(2530, 1705, "[Clínica] Alcaptonuria • Déficit HGD", es_alerta=True))
    partes.append(badge_clinico(2530, 1745, "[Clínica] Tirosinemia I • Déficit FAH", es_alerta=True))

    # Bifurcación Fumarato (➔ Krebs) y Acetoacetato (➔ Cetogénesis)
    partes.append(f'''
    <!-- Conectores continuos de convergencia de esqueletos carbonados -->
    <g id="conectores_catabolismo_phe_tyr">
      <!-- Rama Glucogénica: Fumarato hacia Ciclo de Krebs (m_fumarato) -->
      <path d="M 2520 1765 Q 2480 1775 2480 1810 L 2480 2025 Q 2480 2040 2465 2040 L 1575 2040 Q 1560 2040 1560 2055 L 1560 3265 Q 1560 3280 1545 3280 L 1260 3280" fill="none" stroke="#16a34a" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
      <text x="2470" y="1805" fill="#15803d" font-size="9.5" font-weight="800" text-anchor="end">Fumarato</text>

      <!-- Rama Cetogénica: Acetoacetato hacia Cetogénesis (m_acetoacetato) -->
      <path d="M 2520 1765 Q 2560 1775 2560 1810 L 2560 2040 Q 2560 2055 2545 2055 L 1015 2055 Q 1000 2055 1000 2070 L 1000 3055 Q 1000 3070 985 3070 L 765 3070 Q 750 3070 750 3085 L 750 3135" fill="none" stroke="#dc2626" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowRed)"/>
      <text x="2570" y="1805" fill="#b91c1c" font-size="9.5" font-weight="800" text-anchor="start">Acetoacetato</text>
    </g>
    ''')

    # -------------------------------------------------------------------------
    # B. VÍA DE METIONINA, HOMOCISTEÍNA Y TRANSULFURACIÓN (CITOSOL)
    # (Zona despejada: X ≈ 2740 - 2940, Y ≈ 1240 - 1700)
    # -------------------------------------------------------------------------
    partes.append(nodo_aa(2740, 1250, "L-Metionina", "5C", clasificacion="glu", detalle="Esencial • Inicia SAM"))
    partes.append(f'''
    <g id="rx_transmetilacion" data-arrastrable="1" transform="translate(2760, 1300)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#16a34a" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <text x="12" y="22" fill="#64748b" font-size="8.5" font-family="'Inter', sans-serif">SAM ➔ SAH</text>
    </g>
    ''')
    partes.append(nodo_libre(2730, 1350, "L-Homocisteína", "4C", AA_HOMOCISTEINA, "m_hcy_aa", text_right=True, dx=85, detalle="Tiol reactivo"))

    # Reacción CBS (Cistationina β-Sintetasa)
    partes.append(f'''
    <g id="rx_cbs" data-arrastrable="1" transform="translate(2760, 1510)">
      <line x1="0" y1="0" x2="0" y2="50" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <path d="M -8 15 Q -25 15 -30 28" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-35" y="22" fill="#15803d" font-size="8.5" font-weight="800" text-anchor="end">+ Serina</text>
      <g transform="translate(15, 24)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Cistationina β-Sintetasa (CBS)</text>
        <text x="0" y="13" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">EC 4.2.1.22 (PLP / Vit B₆)</text>
      </g>
    </g>
    ''')
    partes.append(badge_clinico(2680, 1580, "[Clínica] Homocistinuria • CBS / B₆", es_alerta=True))

    # Tránsito hacia L-Cistationina y bifurcación a Propionil-CoA y L-Cisteína
    partes.append(f'''
    <!-- Conector CBS -> L-Cistationina -->
    <path d="M 2760 1610 L 2780 1610 Q 2795 1610 2795 1625 L 2795 1630" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    ''')
    partes.append(nodo_aa(2795, 1640, "L-Cistationina", "7C", clasificacion="glu", detalle="Condensado Hcy + Ser", id_nodo="m_cistat_aa"))

    partes.append(f'''
    <!-- Reacción CTH (Cistationina γ-Liasa) -->
    <g id="rx_cth" data-arrastrable="1" transform="translate(2810, 1680)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(-15, 18)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Cistationina γ-Liasa (CTH)</text>
        <text x="0" y="12" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 4.4.1.1 (PLP / Vit B₆)</text>
      </g>
    </g>
    ''')

    partes.append(f'''
    <!-- Conectores continuos de convergencia de Cistationina -->
    <g id="conectores_transsulfuracion">
      <!-- Rótulos de salida de bifurcación -->
      <text x="2770" y="1735" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Propionil-CoA</text>
      <text x="2825" y="1735" fill="#0f766e" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="start">L-Cisteína</text>
    ''' + (f'''
      <!-- Rama hacia Propionil-CoA (m_prop_aa_matriz en Matriz) -->
      <path id="conn_transsulf_prop" d="M 2810 1715 L 2800 1715 Q 2780 1715 2780 1730 L 2780 2035 Q 2780 2050 2765 2050 L 1035 2050 Q 1020 2050 1020 2065 L 1020 2585 Q 1020 2600 1005 2600 L 795 2600" fill="none" stroke="#16a34a" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>

      <!-- Rama hacia L-Cisteína (nodo citosólico en afluentes a Piruvato) -->
      <path id="conn_transsulf_cys" d="M 2810 1715 L 2945 1715 Q 2960 1715 2960 1700 L 2960 1195 Q 2960 1180 2945 1180 L 2415 1180 Q 2400 1180 2400 1165 L 2400 580 Q 2400 565 2385 565 L 2345 565" fill="none" stroke="#0d9488" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
    ''' if MOSTRAR_CONEXIONES_INTER_RUTA else '') + f'''
    </g>
    ''')

    # -------------------------------------------------------------------------
    # C. MATRIZ MITOCONDRIAL: BCAA Y PROPIONIL-CoA ➔ METILMALONIL-CoA ➔ SUCCINIL-CoA
    # (Zona 100% despejada: X ≈ 590 - 750, Y ≈ 2360 - 2850)
    # -------------------------------------------------------------------------
    # Nodos AA BCAA (Val, Ile) con colector hacia BCKDH
    partes.append(nodo_aa(610, 2360, "L-Valina", "5C", clasificacion="glu", detalle="BCAA Glucogénico"))
    partes.append(nodo_aa(610, 2398, "L-Isoleucina", "6C", clasificacion="mixto", detalle="BCAA Mixto"))
    partes.append('''
    <path d="M 600 2368 L 590 2368 L 590 2432 L 640 2432 M 600 2406 L 590 2406" fill="none" stroke="#ea580c" stroke-width="1.8"/>
    ''')

    # Complejo BCKDH
    partes.append(f'''
    <g id="rx_bckdh" data-arrastrable="1" transform="translate(640, 2436)">
      <line x1="0" y1="0" x2="0" y2="28" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <g transform="translate(15, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Complejo BCKDH</text>
        <text x="0" y="12" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">Cofactores: TPP, Lipoamida, FAD</text>
      </g>
    </g>
    ''')
    partes.append(badge_clinico(580, 2472, "[Clínica] MSUD • Jarabe de Arce (BCKDH)", es_alerta=True))

    # Propionil-CoA [3C]
    partes.append(nodo_libre(610, 2525, "Propionil-CoA", "3C", AA_PROPIONIL_COA, "m_prop_aa_matriz", text_pos="top", dx=55, dy=-18))

    # Reacción PCC (Propionil-CoA Carboxilasa)
    partes.append(f'''
    <g id="rx_pcc" data-arrastrable="1" transform="translate(640, 2572)">
      <line x1="0" y1="0" x2="0" y2="24" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <path d="M -8 8 Q -25 8 -30 18" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-35" y="14" fill="#dc2626" font-size="8" font-weight="800" text-anchor="end">+ ATP + HCO₃⁻</text>
      <g transform="translate(15, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Propionil-CoA Carboxilasa (PCC)</text>
        <text x="0" y="12" fill="#0284c7" font-size="8.5" font-weight="800">EC 6.4.1.3 (Biotina)</text>
      </g>
    </g>
    ''')

    # Intermediario D/L-Metilmalonil-CoA [4C]
    partes.append(nodo_libre(610, 2652, "D/L-Metilmalonil-CoA", "4C", AA_METILMALONIL_COA, "m_metilmalonil_aa", text_pos="top", dx=65, dy=-22))

    # Reacción MCM (Metilmalonil-CoA Mutasa)
    partes.append(f'''
    <g id="rx_mcm" data-arrastrable="1" transform="translate(640, 2700)">
      <line x1="0" y1="0" x2="0" y2="28" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <g transform="translate(15, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Metilmalonil-CoA Mutasa (MCM)</text>
        <text x="0" y="12" fill="#0284c7" font-size="8.5" font-weight="800">EC 5.4.99.2 (Vitamina B₁₂)</text>
      </g>
    </g>
    ''')
    partes.append(badge_clinico(590, 2740, "[Clínica] Acidemia Metilmalónica • MCM / B₁₂", es_alerta=True))

    # Conexión directa anaplerótica a Succinil-CoA de Krebs
    partes.append(f'''
    <path d="M 640 2778 L 640 2830 L 780 2830" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="650" y="2824" fill="#c2410c" font-size="9.5" font-weight="800">➔ Succinil-CoA [4C] (Krebs)</text>
    ''')

    # Aminoácidos Cetogénicos Puros (Leu, Lys) en Matriz con línea colectora hacia Acetoacetil-CoA
    partes.append(nodo_aa(455, 2875, "L-Leucina", "6C", clasificacion="ceto"))
    partes.append(nodo_aa(455, 2912, "L-Lisina", "6C", clasificacion="ceto"))
    partes.append(f'''
    <path d="M 535 2882 L 548 2882 L 548 2919 L 535 2919 M 548 2895 L 566 2885" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
    <text x="435" y="2900" fill="#881337" font-size="8.5" font-weight="800" text-anchor="end">Leu, Lys ➔ Acetoacetil-CoA</text>
    ''')

    # -------------------------------------------------------------------------
    # D. AFLUENTES A PIRUVATO, GLUTAMATO Y OXALACETATO
    # -------------------------------------------------------------------------
    # Afluentes Ser, Gly, Cys, Thr ➔ Piruvato (Zona despejada: X ≈ 2295, Y ≈ 465-580)
    partes.append('''<text x="2295" y="465" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif">Ser, Gly, Cys ➔ Piruvato</text>''')
    partes.append(nodo_aa(2295, 485, "L-Serina", "3C", clasificacion="glu", detalle="Serina deshidratasa (PLP)"))
    partes.append(nodo_aa(2295, 525, "Glicina", "2C", clasificacion="glu", detalle="Sistema escisión (GCS)"))
    partes.append(nodo_aa(2295, 565, "L-Cisteína", "3C", clasificacion="glu", detalle="Desulfuración"))
    partes.append(f'''
    <path d="M 2285 492 L 2275 492 L 2275 572 L 2285 572 M 2285 532 L 2275 532" fill="none" stroke="#16a34a" stroke-width="1.8"/>
    <path d="M 2275 572 L 2275 602 L 2205 602" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
    ''')

    # Afluentes Pro, His, Arg ➔ Glutamato (Zona despejada: X ≈ 2040, Y ≈ 760-880)
    partes.append('''<text x="2040" y="760" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif">Pro, His, Arg ➔ Glutamato ➔</text>''')
    partes.append(nodo_aa(2040, 780, "L-Prolina", "5C", clasificacion="glu", detalle="Oxidación a Glutamato"))
    partes.append(nodo_aa(2040, 820, "L-Histidina", "6C", clasificacion="glu", detalle="Histidasa ➔ FIGLU ➔ Glu"))
    partes.append(nodo_aa(2040, 860, "L-Arginina", "6C", clasificacion="glu", detalle="Urea ➔ Ornitina ➔ Glu"))
    partes.append(f'''
    <path d="M 2182 788 L 2198 788 L 2198 868 L 2182 868 M 2182 828 L 2198 828" fill="none" stroke="#16a34a" stroke-width="1.8"/>
    <path d="M 2198 788 L 2265 788" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowTeal)"/>
    ''')

    # Afluentes Asn, Asp ➔ Oxalacetato (Zona despejada: X ≈ 500, Y ≈ 2215-2260)
    partes.append('''<text x="500" y="2195" fill="#15803d" font-size="9" font-weight="800" font-family="'Inter', sans-serif">Asn, Asp ➔ Oxalacetato ➔</text>''')
    partes.append(nodo_aa(500, 2215, "L-Asparagina", "4C", clasificacion="glu", detalle="Asparaginasa ➔ Aspartato"))
    partes.append(nodo_aa(500, 2255, "L-Aspartato", "4C", clasificacion="glu", detalle="AST / GOT ➔ Oxalacetato"))
    partes.append(f'''
    <path d="M 640 2235 L 735 2235 Q 750 2235 750 2222 L 885 2222 Q 895 2222 895 2235" fill="none" stroke="#16a34a" stroke-width="2.3" stroke-dasharray="6 4" marker-end="url(#arrowGreen)"/>
    ''')

    partes.append(f'</g>')

