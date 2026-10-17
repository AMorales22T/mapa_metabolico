# =============================================================================
# MÓDULO DE REVISIÓN: Vía 6: Ciclo de Krebs en Matriz Mitocondrial
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 2028 a 2135 de 4188)
# Descripción      : Anillo tricarboxílico de 8 reacciones con estructuras químicas e isómeros.
# =============================================================================

    # =========================================================================
    # 7. MATRIZ MITOCONDRIAL: PDH Y CICLO DE KREBS (ESPACIOSO Y NÍTIDO)
    # =========================================================================
    x_k = 1140
    y_k = y_mito + 80
    paso_k = 175  # Paso vertical holgado para que cada intermediario de Krebs respire plenamente

    partes.append(f'<g id="ruta_krebs">')
    partes.append(badge_via(5, 1695, 2185))
    partes.append(badge_via(6, x_k - 40, y_k + paso_k * 4 + 40))

    # 0. Piruvato (Matriz) recién ingresado por el transportador MPC (X=1680)
    partes.append(f"""
    <g id="m_pyr_mito" transform="translate(1632, 2132)">
      <rect x="0" y="0" width="116" height="28" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1.8"/>
      <text x="58" y="13" fill="#9a3412" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">Piruvato (Matriz)</text>
      <text x="58" y="24" fill="#c2410c" font-size="8" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">[3C] CH₃–CO–COO⁻</text>
    </g>

    <!-- Reacción única y clara del Complejo PDH: Piruvato (Matriz) ➔ Acetil-CoA -->
    <path d="M 1680 2162 L 1680 2253 Q 1680 2265 1668 2265 L 1490 2265" fill="none" stroke="#ea580c" stroke-width="3.0" marker-end="url(#arrowFlow)"/>
    <path d="M 1640 2235 Q 1620 2235 1610 2261" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
    <text x="1605" y="2229" fill="#475569" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">+ CoA-SH + NAD⁺</text>
    <path d="M 1625 2269 Q 1615 2292 1595 2292" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
    <text x="1580" y="2308" fill="#059669" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="start">+ CO₂ ↑ + NADH + H⁺</text>

    <!-- Flecha punteada guía visual hacia el panel de detalle PDH -->
    <path d="M 1530 2272 L 1530 3435" fill="none" stroke="#0284c7" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowBlue)"/>

    <g id="ancla_pdh_molecular" transform="translate({x_k + 580}, {y_k - 10})">
      <text x="0" y="5" fill="#c2410c" font-size="13" font-weight="900" font-family="'Inter', sans-serif">Complejo PDH (E1, E2, E3)</text>
      <text x="0" y="24" fill="#64748b" font-size="11" font-family="'Inter', sans-serif">Descarboxilación oxidativa (Piruvato ➔ Acetil-CoA)</text>
      <g transform="translate(0, 40)">
        <text x="0" y="0" fill="#16a34a" font-size="9" font-weight="800">(+) Piruvato, ADP, NAD⁺, Ca²⁺</text>
        <text x="0" y="12" fill="#dc2626" font-size="9" font-weight="800">(-) Acetil-CoA, NADH, ATP</text>
        <text x="0" y="24" fill="#ca8a04" font-size="9" font-weight="800">(P) Inactiva por PDK · Activa por PDP (Ca²⁺/Insulina)</text>
      </g>
    </g>
    """)

    # Acetil-CoA (2C, derecha del inicio del ciclo, título arriba para despejar la convergencia en Y)
    partes.append(nodo_libre(x_k + 220, y_k + 15, "Acetil-CoA", "2C", ACETIL_COA, "m_accoa", text_pos="top", dx=55, dy=-16))

    # Oxalacetato (4C, izquierda del inicio del ciclo)
    partes.append(nodo_libre(x_k - 240, y_k + 15, "Oxalacetato", "4C", KREBS_OXALACETATO, "m_oaa", text_right=False))
    partes.append(f"""
    <!-- Condensación en Y de Citrato Sintasa: Oxalacetato (4C) + Acetil-CoA (2C) ➔ Citrato (6C) -->
    <g id="rx_citrato_sintasa">
      <path d="M 1015 {y_k + 48} L {x_k + 35} {y_k + 48} Q {x_k + 55} {y_k + 48} {x_k + 55} {y_k + 68}" fill="none" stroke="#b45309" stroke-width="2.6"/>
      <path d="M 1348 {y_k + 48} L {x_k + 75} {y_k + 48} Q {x_k + 55} {y_k + 48} {x_k + 55} {y_k + 68}" fill="none" stroke="#ea580c" stroke-width="2.6"/>
      <path d="M {x_k + 55} {y_k + 60} L {x_k + 55} {y_k + 160}" fill="none" stroke="#b45309" stroke-width="3.0" marker-end="url(#arrowFlow)"/>
      <!-- Entrada de + H2O y salida de - CoA-SH -->
      <path d="M {x_k + 5} {y_k + 80} Q {x_k + 35} {y_k + 80} {x_k + 51} {y_k + 96}" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="{x_k}" y="{y_k + 84}" fill="#0284c7" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ H₂O</text>
      <path d="M {x_k + 51} {y_k + 118} Q {x_k + 35} {y_k + 134} {x_k + 5} {y_k + 134}" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="{x_k}" y="{y_k + 138}" fill="#dc2626" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">- CoA-SH</text>
      <!-- Nombre enzimático, mecanismo y regulación alostérica -->
      <text x="{x_k + 72}" y="{y_k + 85}" fill="#78350f" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">Citrato Sintasa</text>
      <text x="{x_k + 72}" y="{y_k + 98}" fill="#64748b" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace">Condensación: OAA (4C) + Ac-CoA (2C)</text>
      <text x="{x_k + 72}" y="{y_k + 111}" fill="#16a34a" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">⊕ ADP (carga energética baja)</text>
      <text x="{x_k + 72}" y="{y_k + 123}" fill="#dc2626" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">⊖ ATP, NADH, Succinil-CoA, Citrato</text>
    </g>
    """)

    # Citrato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k, "Citrato", "6C", CITRATO, "m_citrato", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k + 130, 38, "Aconitasa ⇄", reversible=True, id_rx="rx_acon", text_dx=-16, text_anchor="end"))

    # Isocitrato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 2, "Isocitrato", "6C", ISOCITRATO, "m_isocitrato", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 2 + 130, 38, "Isocitrato DH", entra="+ NAD⁺", sale="+ NADH + CO₂", es_ganancia=True, id_rx="rx_icdh", text_dx=-16, text_anchor="end"))
    partes.append(etiqueta_regulacion("icdh", x_k + 69, y_k + paso_k * 2 + 135, dx=0, dy=0, anchor="start"))

    # Alfa-Cetoglutarato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 3, "α-Cetoglutarato", "5C", KREBS_ALFA_CETOGLUTARATO, "m_akg", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 3 + 130, 38, "α-KG Deshidrogenasa", entra="+ CoA-SH + NAD⁺", sale="+ NADH + CO₂", es_ganancia=True, id_rx="rx_akgdh", text_dx=-16, text_anchor="end"))
    partes.append(etiqueta_regulacion("akgdh", x_k + 69, y_k + paso_k * 3 + 138, dx=0, dy=0, anchor="start"))

    # Succinil-CoA
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 4, "Succinil-CoA", "4C", SUCCINIL_COA, "m_succoa", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 4 + 130, 38, "Succinil-CoA Sintetasa", entra="+ GDP + Pi", sale="+ GTP (+CoA-SH)", es_ganancia=True, id_rx="rx_scas", text_dx=-16, text_anchor="end"))

    # Succinato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 5, "Succinato", "4C", SUCCINATO, "m_succinato", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 5 + 130, 38, "Succinato DH (Complejo II)", entra="+ FAD", sale="+ FADH₂", es_ganancia=True, id_rx="rx_sdh", text_dx=-16, text_anchor="end"))

    # Fumarato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 6, "Fumarato", "4C", FUMARATO, "m_fumarato", text_right=True, dx=140))
    partes.append(reaccion_libre(x_k + 55, y_k + paso_k * 6 + 130, 38, "Fumarasa (+ H₂O)", reversible=True, id_rx="rx_fum", text_dx=-16, text_anchor="end"))

    # L-Malato
    partes.append(nodo_libre(x_k + 10, y_k + paso_k * 7, "L-Malato", "4C", KREBS_MALATO, "m_malato", text_right=True, dx=140))

    # Cierre del Ciclo: Retorno completo de L-Malato hasta tocar Oxalacetato con sus cofactores
    partes.append(f"""
    <g id="rx_mdh_retorno" data-arrastrable="1">
      <path d="M {x_k} {y_k + paso_k * 7 + 60} C 945 {y_k + paso_k * 7 + 60}, 945 3300, 945 2750 L 945 2378" fill="none" stroke="#b45309" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M 905 2620 Q 930 2620 941 2595" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="900" y="2624" fill="#475569" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ NAD⁺</text>
      <path d="M 941 2545 Q 930 2520 905 2520" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="900" y="2524" fill="#059669" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">+ NADH + H⁺</text>
      <text x="968" y="2570" fill="#78350f" font-size="11" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 968 2570)" text-anchor="middle">
        Malato DH (mMDH: L-Malato ➔ Oxalacetato)
      </text>
    </g>
    """)
    partes.append('</g>')

