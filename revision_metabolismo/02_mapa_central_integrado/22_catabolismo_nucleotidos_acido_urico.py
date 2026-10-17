# =============================================================================
# MÓDULO DE REVISIÓN: Vía 16: Degradación de Nucleótidos y Ácido Úrico
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 3543 a 3601 de 4188)
# Descripción      : Catabolismo de purinas vía xantina oxidasa a urato y de pirimidinas a beta-alanina.
# =============================================================================

    # =========================================================================
    # 16. RUTA 16: CATABOLISMO DE NUCLEÓTIDOS Y ÁCIDO ÚRICO
    # =========================================================================
    partes.append(f'<g id="ruta_degradacion_nucleotidos">')
    
    y_deg = 1765
    partes.append(badge_via(16, x_nuc - 40, y_deg))
    partes.append(f'''
    <g transform="translate({x_nuc}, {y_deg})" data-arrastrable="1">
      <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="900" font-family="'Inter', sans-serif">CATABOLISMO DE NUCLEÓTIDOS Y ÁCIDO ÚRICO</text>
      <text x="0" y="16" fill="#dc2626" font-size="11" font-weight="800" font-family="'Inter', sans-serif">Convergencia en XOD ➔ Ácido Úrico (Gota) y Apertura Soluble (β-Alanina)</text>
    </g>
    ''')

    # Degradación de Purinas: Hipoxantina ➔ Xantina ➔ Ácido Úrico
    partes.append(nodo_libre(x_nuc + 30, y_deg + 55, "Hipoxantina (de AMP)", "Purina", HIPOXANTINA, "m_deg_hipo", dx=115, detalle="Vía ADA (diana SCID) y PNP"))
    partes.append(etiqueta_regulacion("ada", x_nuc + 160, y_deg + 120, dx=0, dy=0))

    partes.append(reaccion_libre(x_nuc + 80, y_deg + 145, 42, "XOD (Paso 1)", entra="+ O₂ + H₂O", sale="+ H₂O₂", id_rx="rx_xod1"))
    partes.append(nodo_libre(x_nuc + 30, y_deg + 202, "Xantina", "Dioxipurina", XANTINA, "m_deg_xantina", dx=115, detalle="Convergencia de Adenina y Guanina (Guanasa)"))

    partes.append(reaccion_libre(x_nuc + 80, y_deg + 288, 42, "XOD (Paso 2 · Alopurinol)", entra="+ O₂ + H₂O", sale="+ H₂O₂", id_rx="rx_xod2"))
    partes.append(etiqueta_regulacion("xod", x_nuc + 270, y_deg + 296, dx=0, dy=0))
    partes.append(nodo_libre(x_nuc + 30, y_deg + 350, "ÁCIDO ÚRICO (URATO)", "Trioxipurina", ACIDO_URICO, "m_deg_urato", dx=115, detalle="Poco soluble · Precipita en gota"))

    # Trazo de excreción renal de Urato hacia el torrente vascular capilar superior
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="excrecion_urato_sangre" data-arrastrable="1">
          <path d="M {x_nuc + 120} {y_deg + 350} C {x_nuc + 380} {y_deg + 180}, {x_nuc + 480} 500, {x_nuc + 480} 74" fill="none" stroke="#dc2626" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowRed)"/>
        </g>
        ''')
    partes.append(f'''
    <g id="indicador_urato_excrecion" transform="translate({x_nuc + 160}, {y_deg + 350})">
      <path d="M 0 0 Q 70 -30 110 -30" fill="none" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
      <text x="120" y="-26" fill="#dc2626" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">➔ Excreción renal de Urato (URAT1) / Hiperuricemia</text>
    </g>
    <!-- Biomarcador vascular de Urato en torrente capilar superior -->
    <g transform="translate(5550, 38)">
      <ellipse cx="0" cy="0" rx="28" ry="16" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
      <text x="0" y="4" fill="#dc2626" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">URATO</text>
      <text x="0" y="19" fill="#fca5a5" font-size="7" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Filtro Renal</text>
    </g>
    ''')

    # Degradación de Pirimidinas (con intermediario Dihidrouracilo y apertura soluble)
    y_deg_pir = y_deg + 495
    partes.append(nodo_libre(x_nuc + 30, y_deg_pir, "Uracilo / Citosina", "Pirimidina libre", DEG_URACILO, "m_deg_uracilo", dx=115, detalle="Sustrato de DPD (NADPH)"))
    partes.append(reaccion_libre(x_nuc + 80, y_deg_pir + 68, 38, "Dihidropirimidina DH (DPD)", entra="+ NADPH", sale="+ NADP⁺", id_rx="rx_dpd"))

    partes.append(nodo_libre(x_nuc + 30, y_deg_pir + 128, "Dihidrouracilo (DHU)", "4C • Anillo saturado", DEG_DIHIDROURACILO, "m_deg_dhu", dx=115, detalle="Reducción C5=C6 completada"))
    partes.append(reaccion_libre(x_nuc + 80, y_deg_pir + 198, 38, "DHPasa (Apertura hidrolítica)", entra="+ H₂O", id_rx="rx_dhpasa"))

    partes.append(nodo_libre(x_nuc + 30, y_deg_pir + 250, "β-Ureidopropionato", "Cadena abierta acíclica", BETA_UREIDOPROPIONATO, "m_deg_ureido", dx=175, detalle="Apertura hidrolítica del anillo"))
    partes.append(reaccion_libre(x_nuc + 80, y_deg_pir + 318, 38, "β-Ureidopropionasa", entra="+ H₂O", sale="+ NH₄⁺ + CO₂", id_rx="rx_ureidopropionasa"))
    partes.append(nodo_libre(x_nuc + 30, y_deg_pir + 370, "β-Alanina Soluble", "Producto soluble", BETA_ALANINA, "m_deg_beta_ala", dx=120, detalle="Excreción inocua en orina"))

    partes.append(f'</g>')

