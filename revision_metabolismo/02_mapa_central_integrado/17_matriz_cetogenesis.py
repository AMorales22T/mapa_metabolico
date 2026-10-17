# =============================================================================
# MÓDULO DE REVISIÓN: Vía 11: Cetogénesis Mitocondrial
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 2663 a 2705 de 4188)
# Descripción      : Síntesis hepática de acetoacetato, D-beta-hidroxibutirato y acetona.
# =============================================================================

    # =========================================================================
    # 11. CETOGÉNESIS (MATRIZ MITOCONDRIAL)
    # =========================================================================
    x_ceto = 570
    y_ceto = y_mito + 700
    paso_c = 140
    partes.append(f'<g id="ruta_ceto">')
    partes.append(badge_via(11, x_ceto - 40, y_ceto - 20))
    partes.append(f'''
    <text x="{x_ceto + 10}" y="{y_ceto - 8}" fill="#9d174d" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">Paso 1: Tiolasa (ACAT1) • 2 Acetil-CoA ⇄</text>
    ''')
    
    partes.append(nodo_libre(x_ceto, y_ceto, "Acetoacetil-CoA", "4C", ACETOACETIL_COA, "m_acetoac_coa", text_right=True, dx=200))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + 70, 40, "HMG-CoA Sintasa 2 (HMGCS2)", entra="+ Acetil-CoA", id_rx="rx_ceto1"))
    partes.append(etiqueta_regulacion("hmgcs2", x_ceto + 74, y_ceto + 108, dx=0, dy=0))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c, "HMG-CoA", "6C", HMG_COA, "m_hmg_coa", text_right=True, dx=200))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + paso_c + 70, 40, "HMG-CoA Liasa", sale="+ Acetil-CoA", id_rx="rx_ceto2"))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c*2, "Acetoacetato", "4C", ACETOACETATO, "m_acetoacetato", text_right=True, dx=200))
    partes.append(reaccion_libre(x_ceto + 60, y_ceto + paso_c*2 + 70, 40, "β-Hidroxibutirato DH", entra="+ NADH", sale="+ NAD+", id_rx="rx_ceto3"))

    # Rama lateral de descarboxilación espontánea: Acetoacetato ➔ Acetona [3C] + CO₂ ↑
    partes.append(f'''
    <g id="rx_ceto_acetona" data-arrastrable="1">
      <path d="M {x_ceto - 5} {y_ceto + paso_c*2 + 25} L 465 {y_ceto + paso_c*2 + 25}" fill="none" stroke="#db2777" stroke-width="2.2" stroke-dasharray="5 3" marker-end="url(#arrowRed)"/>
      <text x="512" y="{y_ceto + paso_c*2 + 15}" fill="#be185d" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Espontánea (- CO₂ ↑)</text>
    </g>
    ''')
    partes.append(nodo_libre(335, y_ceto + paso_c*2 + 2, "Acetona", "3C", ACETONA, "m_acetona_ceto", text_pos="bottom", dx=58, dy=52, detalle="Volátil • Exhalación pulmonar"))
    
    partes.append(nodo_libre(x_ceto, y_ceto + paso_c*3, "D-β-Hidroxibutirato", "4C", D_BETA_HIDROXIBUTIRATO, "m_betahidroxi", text_right=True, dx=220))
    
    # Línea rosa de exportación hacia sangre
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        y_ceto_bottom = y_ceto + paso_c*3 + 70
        partes.append(f'''
        <path d="M {x_ceto + 40} {y_ceto + paso_c*3 + 45} L {x_ceto + 40} {y_ceto_bottom} L 55 {y_ceto_bottom} L 55 40" fill="none" stroke="#ec4899" stroke-width="3.2" stroke-dasharray="10 5" marker-end="url(#arrowFlow)"/>
        <text x="42" y="1600" fill="#db2777" font-size="13" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 42 1600)" stroke="none">EXPORTACIÓN DE CUERPOS CETÓNICOS A SANGRE (PARA CEREBRO/MÚSCULO) ➔</text>
        ''')
    
    partes.append(f'</g>')

