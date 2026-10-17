# =============================================================================
# MÓDULO DE REVISIÓN: Vía 12: Biosíntesis de Colesterol (Vía del Mevalonato)
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 2519 a 2579 de 4188)
# Descripción      : HMG-CoA sintasa, HMG-CoA reductasa (diana de estatinas), IPP, escualeno y colesterol.
# =============================================================================

    # =========================================================================
    # 9B. LÍPIDOS: SÍNTESIS DE COLESTEROL (CITOSOL Y MEMBRANA DEL REL)
    # =========================================================================
    # Se ramifica directamente desde el pool citosólico de Acetil-CoA
    x_col = 3560
    y_col = 920
    paso_col = 165
    partes.append(f'<g id="ruta_colesterol">')
    partes.append(badge_via(12, x_col - 40, y_col - 260))

    # Inserción de Acetoacetil-CoA y HMG-CoA citosólicos + HMG-CoA Reductasa
    # Espaciado holgado: Acetoacetil-CoA (Y=520), HMG-CoA (Y=680), Mevalonato (Y=860)
    y_acetoac_col = 520
    y_hmg_col = 680
    y_mev = 890
    
    # Conexión fluida desde Acetil-CoA citosólico (X=3080, Y=825) hacia Acetoacetil-CoA citosólico (X=3560, Y=520)
    # Bordeando suavemente hacia arriba para no atravesar ningún texto
    partes.append(f'''
    <path d="M 3245 855 L 3290 855 Q 3300 855 3300 845 L 3300 470 Q 3300 460 3310 460 L 3495 460 Q 3505 460 3505 470 L 3505 525 Q 3505 535 3515 535 L 3550 535" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    <text x="3400" y="450" fill="#9a3412" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">➔ Vía del Mevalonato (2 Acetil-CoA)</text>
    ''')

    partes.append(nodo_libre(x_col, y_acetoac_col, "Acetoacetil-CoA (Citosol)", "4C", ACETOACETIL_COA_COLEST, "m_acetoac_col", text_pos="top", dx=70, dy=-22))
    partes.append(reaccion_libre(x_col + 60, y_acetoac_col + 65, 45, "HMG-CoA Sintasa (Citosólica)", entra="+ Acetil-CoA", id_rx="rx_hmgs_cito"))

    partes.append(nodo_libre(x_col, y_hmg_col, "HMG-CoA (Citosol)", "6C", HMG_COA_CITOSOL, "m_hmg_col", text_pos="top", dx=70, dy=-22))
    partes.append(reaccion_libre(x_col + 60, y_hmg_col + 65, 48, "HMG-CoA Reductasa (HMGCR)", entra="- 2 NADPH", sale="+ CoA", id_rx="rx_hmgcr"))
    partes.append(etiqueta_regulacion("hmgcr", x_col + 250, y_hmg_col + 70, dx=0, dy=0))

    # Mevalonato (producto irreversible del marcapasos HMGCR)
    partes.append(nodo_libre(x_col, y_mev, "Mevalonato", "6C", MEVALONATO, "m_mevalonato_integ", text_pos="top", dx=70, dy=-22))
    partes.append(reaccion_libre(x_col + 60, y_mev + 75, 45, "Mevalonato Quinasa / Descarboxilasa", entra="- 3 ATP", sale="+ CO2 + Pi", id_rx="rx_col1"))
    
    # Isopentenil Pirofosfato (IPP)
    partes.append(nodo_libre(x_col, y_mev + paso_col, "Isopentenil-PP (IPP)", "5C", ISOPENTENIL_PP, "m_ipp_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_mev + paso_col + 75, 45, "Preniltransferasas", entra="+ 2 IPP", sale="+ 2 PPi", id_rx="rx_col2"))
    
    # Farnesil Pirofosfato (FPP)
    partes.append(nodo_libre(x_col, y_mev + paso_col*2, "Farnesil-PP (FPP)", "15C", FARNESIL_PP, "m_fpp_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_mev + paso_col*2 + 75, 45, "Escualeno Sintasa", entra="- NADPH", sale="+ 2 PPi", es_ganancia=False, id_rx="rx_col3"))
    
    # Escualeno
    partes.append(nodo_libre(x_col, y_mev + paso_col*3, "Escualeno", "30C", ESCUALENO, "m_escualeno_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_mev + paso_col*3 + 75, 45, "Oxidoscualeno Ciclasa", entra="- NADPH + O2", sale="+ H2O", id_rx="rx_col4"))
    
    # Lanosterol
    partes.append(nodo_libre(x_col, y_mev + paso_col*4, "Lanosterol", "30C", LANOSTEROL, "m_lanosterol_integ", text_pos="top", dy=-18))
    partes.append(reaccion_libre(x_col + 60, y_mev + paso_col*4 + 75, 45, "Vías de Bloch &amp; Kandutsch (19 pasos)", entra="- NADPH + O2", sale="+ 3 CO2", id_rx="rx_col5"))
    
    # Colesterol Final
    partes.append(nodo_libre(x_col, y_mev + paso_col*5, "COLESTEROL", "27C", COLESTEROL, "m_colesterol_integ", text_pos="top", dy=-18))
    
    # Conexiones funcionales de destino del Colesterol
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <path d="M {x_col + 240} {y_mev + paso_col*5 + 35} Q 3860 {y_mev + paso_col*5 + 35}, 3860 74" fill="none" stroke="#0284c7" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowBlue)"/>
        <text x="3875" y="500" fill="#0369a1" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 3875 500)">➔ DESTINO A MEMBRANA PLASMÁTICA (BALSAS LIPÍDICAS)</text>
        ''')
    partes.append(f'</g>')

