# =============================================================================
# MÓDULO DE REVISIÓN: Vía 3: Glucogenogénesis y Glucogenólisis
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 1669 a 1723 de 4188)
# Descripción      : Rama izquierda citosólica: G1P, UDP-glucosa, glucogenina y gránulo de glucógeno.
# =============================================================================

    # =========================================================================
    # 4. IZQUIERDA: METABOLISMO DEL GLUCÓGENO (LIBRE EN CITOSOL)
    # =========================================================================
    x_glc = 520
    y_glc = 340
    partes.append(f'<g id="ruta_glucogeno">')
    partes.append(badge_via(3, 440, 310))
    
    # G1P
    partes.append(nodo_libre(x_glc + 450, y_glc, "Glucosa-1-Fosfato", "6C", GLUCOSA_1_FOSFATO, "m_g1p", text_pos="top", dx=60, dy=-20))

    # Conexión G6P ⇄ G1P
    partes.append(f"""
    <g id="rx_pgm_glucogeno" data-arrastrable="1">
      <path d="M {x_g - 75} {y_g + paso_y + 35} L {x_glc + 600} {y_glc + 35}" stroke="#f59e0b" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <text x="{(x_g - 75 + x_glc + 630)//2}" y="{y_glc + 20}" fill="#b45309" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Fosfoglucomutasa ⇄</text>
    </g>
    """)

    # UDP-Glucosa (nombre arriba, estructura centrada y flecha de pirofosforilasa arqueada por encima)
    y_udpg = y_glc - 70
    partes.append(nodo_libre(x_glc + 120, y_udpg, "UDP-Glucosa", "6C", UDP_GLUCOSA, "m_udpg", text_pos="top", dx=65, dy=-20))
    partes.append(f"""
    <g id="rx_udpg" data-arrastrable="1">
      <path d="M {x_glc + 450} {y_glc + 20} C {x_glc + 420} {y_glc + 20}, {x_glc + 395} {y_udpg + 35}, {x_glc + 380} {y_udpg + 35}" fill="none" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="{x_glc + 365}" y="{y_udpg - 55}" fill="#d97706" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">UDP-Glucosa Pirofosforilasa (+UTP)</text>
    </g>
    """)

    # Cadena de Glucógeno
    partes.append(nodo_libre(x_glc - 80, y_glc + 260, "Glucógeno (n+1)", "Polímero", CADENA_GLUCOGENO, "m_glucogeno_cadena", text_pos="top", dx=30, dy=-60))
    partes.append(f"""
    <g id="rx_sintesis_degradacion_glucogeno" data-arrastrable="1">
      <!-- Síntesis -->
      <path d="M {x_glc + 120} {y_udpg + 65} Q {x_glc + 45} {y_glc + 140} {x_glc + 45} {y_glc + 232}" fill="none" stroke="#f59e0b" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="{x_glc + 140}" y="{y_glc + 145}" fill="#b45309" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">Glucógeno Sintasa</text>
      <g transform="translate({x_glc + 140}, {y_glc + 160})">
        <text x="0" y="0" fill="#16a34a" font-size="9" font-weight="800">(+) G6P</text>
        <text x="0" y="12" fill="#ca8a04" font-size="9" font-weight="800">(P) Inactiva (GSK-3/PKA)</text>
        <text x="0" y="24" fill="#0284c7" font-size="9" font-weight="800">[Hormonal] Insulina ↑ · Glucagón ↓</text>
      </g>

      <!-- Glucogenólisis (degradación) -->
      """ + (f"""<path d="M {x_glc + 80} {y_glc + 310} Q {x_glc + 320} {y_glc + 360} {x_glc + 500} {y_glc + 85}" fill="none" stroke="#ea580c" stroke-width="2.2" stroke-dasharray="7 5" marker-end="url(#arrowFlow)"/>""" if MOSTRAR_CONEXIONES_INTER_RUTA else "") + f"""
      <text x="{x_glc + 330}" y="{y_glc + 345}" fill="#c2410c" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">Glucógeno Fosforilasa (+Pi ➔ G1P)</text>
      <g transform="translate({x_glc + 330}, {y_glc + 360})">
        <text x="0" y="0" fill="#16a34a" font-size="9" font-weight="800">(+) AMP, Ca²⁺</text>
        <text x="0" y="12" fill="#dc2626" font-size="9" font-weight="800">(-) ATP, G6P, Glucosa</text>
        <text x="0" y="24" fill="#ca8a04" font-size="9" font-weight="800">(P) Activa (Fosforilasa quinasa)</text>
        <text x="0" y="36" fill="#0284c7" font-size="9" font-weight="800">[Hormonal] Glucagón/Adrenalina ↑</text>
      </g>
    </g>
    """)
    partes.append('</g>')

