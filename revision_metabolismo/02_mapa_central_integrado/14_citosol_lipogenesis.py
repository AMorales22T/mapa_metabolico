# =============================================================================
# MÓDULO DE REVISIÓN: Vía 10: Lipogénesis Citosólica
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 2468 a 2518 de 4188)
# Descripción      : Lanzadera de citrato, ACLY, ACC (malonil-CoA) y complejo ácido graso sintasa (FAS) hasta palmitato.
# =============================================================================

    # =========================================================================
    # 9. LÍPIDOS: LIPOGÉNESIS (CITOSOL)
    # =========================================================================
    x_lipo = 3080
    y_lipo = 1000
    paso_l = 175
    paso_fas = 152
    partes.append(f'<g id="ruta_lipogenesis">')
    partes.append(badge_via(10, x_lipo - 30, y_lipo - paso_l*2 - 20))

    partes.append(nodo_libre(x_lipo, y_lipo - paso_l*2 - 60, "Citrato (Citosólico)", "6C", CITRATO, "m_citrato_cito", text_right=True, dx=220))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo - paso_l*2 + 65, 52, "ATP Citrato Liasa", entra="+ ATP + CoA-SH", sale="+ OAA", id_rx="rx_acly"))
    partes.append(f'''
    <g id="retorno_malico_lanzadera_citrato" transform="translate({x_lipo + 74}, {y_lipo - paso_l*2 + 104})">
      <text x="0" y="0" fill="#047857" font-size="8" font-weight="800" font-family="'Inter', sans-serif">↳ OAA ➔ Malato (MDH1)</text>
      <text x="0" y="10" fill="#059669" font-size="8" font-weight="800" font-family="'Inter', sans-serif">➔ Piruvato + NADPH (ME1)</text>
    </g>
    ''')
    partes.append(etiqueta_regulacion("acly", x_lipo + 255, y_lipo - paso_l*2 + 52, dx=0, dy=0))
    
    partes.append(nodo_libre(x_lipo, y_lipo - paso_l, "Acetil-CoA (Citosólico)", "2C", ACETIL_COA, "m_acetil_coa_cito", text_pos="top", dx=60, dy=-22))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo - paso_l + 75, 48, "ACC (Acetil-CoA Carboxilasa)", entra="+ ATP + HCO₃⁻", sale="+ ADP + Pi", id_rx="rx_acc"))
    partes.append(etiqueta_regulacion("acc", x_lipo + 260, y_lipo - paso_l + 85, dx=0, dy=0))
    
    partes.append(f'''
    <!-- Transportador CIC en MMI (Lanzadera de Citrato) -->
    <g id="transportador_cic" data-arrastrable="1" transform="translate(1915, 2115)">
      <rect x="0" y="0" width="60" height="28" rx="7" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <text x="30" y="18" fill="#ffffff" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CIC</text>
    </g>
    ''')

    partes.append(nodo_libre(x_lipo, y_lipo, "Malonil-CoA", "3C", MALONIL_COA, "m_malonil", text_right=True, dx=185))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + 68, 42, "FAS: Condensación (KS)", entra="+ Acetil-ACP", sale="- CO₂", id_rx="rx_fas1"))
    partes.append(etiqueta_regulacion("fas", x_lipo + 245, y_lipo + 74, dx=0, dy=0))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_fas, "Acetoacetil-ACP", "4C", ACETOACETIL_ACP, "m_acetoac_acp", text_right=True, dx=190))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_fas + 68, 42, "FAS: 1ª Reducción (KR)", entra="+ NADPH", sale="+ NADP⁺", id_rx="rx_fas2"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_fas*2, "D-β-Hidroxiacil-ACP", "4C", D_BETA_HIDROXIACIL_ACP, "m_hidroxi_acp", text_right=True, dx=190))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_fas*2 + 68, 42, "FAS: Deshidratación (DH)", entra="", sale="- H₂O", id_rx="rx_fas3"))

    partes.append(nodo_libre(x_lipo, y_lipo + paso_fas*3, "trans-Δ²-Enoil-ACP", "4C", TRANS_DELTA2_ENOIL_ACP, "m_enoil_acp", text_right=True, dx=190, detalle="Crotonil-ACP (α,β-insaturado)"))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_fas*3 + 68, 42, "FAS: 2ª Reducción (ER)", entra="+ NADPH", sale="+ NADP⁺", id_rx="rx_fas3b"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_fas*4, "Butiril-ACP", "4C", BUTIRIL_ACP, "m_butiril_acp", text_right=True, dx=190, detalle="Acilo saturado (1ᵉʳ ciclo)"))
    partes.append(reaccion_libre(x_lipo + 60, y_lipo + paso_fas*4 + 68, 42, "FAS (x6 Ciclos + Tioesterasa)", entra="+ 6 Malonil", sale="+ H₂O (-ACP)", id_rx="rx_fas4"))
    
    partes.append(nodo_libre(x_lipo, y_lipo + paso_fas*5, "Palmitato", "16C", PALMITATO_LIBRE, "m_palmitato_libre", text_right=True, dx=255))
    partes.append(f'</g>')

