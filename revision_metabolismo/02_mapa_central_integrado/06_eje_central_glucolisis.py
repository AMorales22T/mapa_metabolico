# =============================================================================
# MÓDULO DE REVISIÓN: Vía 1: Eje Central de la Glucólisis
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 1351 a 1432 de 4188)
# Descripción      : Los 10 pasos glucolíticos verticales en el centro del citosol.
# =============================================================================

    # =========================================================================
    # 3. EJE CENTRAL: GLUCÓLISIS VERTICAL (LIBRE EN CITOSOL)
    # =========================================================================
    x_g = 1680
    y_g = 160
    paso_y = 175

    partes.append(f'<g id="ruta_glucolisis">')
    
    # 1. Glucosa
    partes.append(nodo_libre(x_g - 40, y_g, "D-Glucosa", "6C", GLUCOSA, "m_glucosa"))
    partes.append(badge_via(1, x_g - 80, y_g + 30))
    partes.append(reaccion_libre(x_g, y_g + 105, 52, "Hexocinasa", entra="-1 ATP", sale="+1 ADP", id_rx="rx_hk"))
    partes.append(etiqueta_regulacion("hk", x_g + 95, y_g + 115, dx=0, dy=0))

    # 2. G6P
    partes.append(nodo_libre(x_g - 40, y_g + paso_y, "Glucosa-6-Fosfato", "6C", GLUCOSA_6_FOSFATO, "m_g6p"))
    partes.append(reaccion_libre(x_g, y_g + paso_y + 105, 52, "Fosfoglucosa Isomerasa", reversible=True, id_rx="rx_pgi"))

    # 3. F6P
    partes.append(nodo_libre(x_g - 40, y_g + paso_y * 2, "Fructosa-6-Fosfato", "6C", FRUCTOSA_6_FOSFATO, "m_f6p"))
    partes.append(reaccion_libre(x_g, y_g + paso_y * 2 + 105, 52, "PFK-1", entra="-1 ATP", sale="+1 ADP", id_rx="rx_pfk1"))
    partes.append(etiqueta_regulacion("pfk1", x_g + 95, y_g + paso_y * 2 + 115, dx=0, dy=0))
    partes.append("""
      <!-- Mini-recuadro regulador: Enzima Bifuncional PFK-2 / FBPasa-2 -->
      <g id="recuadro_pfk2_fbpasa2" transform="translate(1260, 485)">
        <rect x="0" y="0" width="220" height="90" rx="8" fill="#f8fafc" stroke="#7c3aed" stroke-width="1.8" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.06))"/>
        <text x="110" y="18" fill="#5b21b6" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">PFK-2 / FBPasa-2</text>
        <text x="110" y="32" fill="#6d28d9" font-size="9.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Enzima Tándem Reguladora</text>
        <line x1="12" y1="40" x2="208" y2="40" stroke="#ddd6fe" stroke-width="1"/>
        <text x="15" y="55" fill="#16a34a" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">[Hormonal] Insulina (PP2A) ➔ ↑ F-2,6-BP</text>
        <text x="15" y="69" fill="#dc2626" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">[Hormonal] Glucagón (PKA) ➔ ↓ F-2,6-BP</text>
        <text x="15" y="82" fill="#0284c7" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">F-2,6-BP: (+) PFK-1 / (-) FBPasa-1</text>
      </g>
""")

    # 4. F-1,6-BP
    partes.append(nodo_libre(x_g - 40, y_g + paso_y * 3, "Fructosa-1,6-Bisfosfato", "6C", FRUCTOSA_1_6_BISFOSFATO, "m_fbp"))
    partes.append(reaccion_libre(x_g, y_g + paso_y * 3 + 105, 52, "Aldolasa", reversible=True, id_rx="rx_aldo"))

    # 5. DHAP y GAP
    partes.append(nodo_libre(x_g - 250, y_g + paso_y * 4, "Dihidroxiacetona-P", "3C", DIHIDROXIACETONA_FOSFATO, "m_dhap", text_pos="top", dy=-32))
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 4, "Gliceraldehído-3-P", "3C", GLICERALDEHIDO_3_FOSFATO, "m_gap", text_pos="top", dy=-20))
    # Conexión TPI
    partes.append(f"""
    <g id="rx_tpi" data-arrastrable="1">
      <line x1="{x_g - 40}" y1="{y_g + paso_y * 4 + 40}" x2="{x_g + 160}" y2="{y_g + paso_y * 4 + 40}" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="{x_g + 160}" y1="{y_g + paso_y * 4 + 48}" x2="{x_g - 40}" y2="{y_g + paso_y * 4 + 48}" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <text x="{x_g + 60}" y="{y_g + paso_y * 4 + 28}" fill="#0f172a" font-size="11" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Triosa Fosfato Isomerasa</text>
    </g>
    """)

    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 4 + 115, 45, "GAPDH", entra="+ NAD⁺", sale="+ NADH + H⁺", es_ganancia=True, reversible=True, id_rx="rx_gapdh"))

    # 6. 1,3-BPG
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 5, "1,3-Bisfosfoglicerato", "3C", BISFOSFOGLICERATO_1_3, "m_bpg"))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 5 + 115, 45, "Fosfoglicerato Cinasa", entra="+ ADP", sale="+ ATP", es_ganancia=True, reversible=True, id_rx="rx_pgk"))

    # 7. 3-PG
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 6, "3-Fosfoglicerato", "3C", FOSFOGLICERATO_3, "m_3pg"))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 6 + 115, 45, "Fosfoglicerato Mutasa", reversible=True, id_rx="rx_pgm"))

    # 8. 2-PG
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 7, "2-Fosfoglicerato", "3C", FOSFOGLICERATO_2, "m_2pg"))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 7 + 105, 52, "Enolasa (-H₂O)", reversible=True, id_rx="rx_eno"))

    # 9. PEP
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 8, "Fosfoenolpiruvato", "3C", FOSFOENOLPIRUVATO, "m_pep", dx=115))
    partes.append(reaccion_libre(x_g + 220, y_g + paso_y * 8 + 105, 52, "Piruvato Cinasa", entra="+ ADP", sale="+ ATP", es_ganancia=True, id_rx="rx_pk"))
    partes.append(etiqueta_regulacion("pk", x_g + 325, y_g + paso_y * 8 + 115, dx=0, dy=0))

    # 10. Piruvato (Citosol)
    partes.append(nodo_libre(x_g + 180, y_g + paso_y * 9, "Piruvato", "3C", PIRUVATO, "m_pyr_cito"))

    # Flecha Piruvato Citosol ➔ MPC (entra directo al centro del transportador en x=1680)
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f"""
        <path d="M {x_g + 220} {y_g + paso_y * 9 + 100} Q {x_g + 120} {y_g + paso_y * 9 + 135}, 1680 {y_mito - 60}" fill="none" stroke="#ea580c" stroke-width="3" stroke-dasharray="10 6" marker-end="url(#arrowFlow)"/>
        """)
    partes.append('</g>')


