# =============================================================================
# MÓDULO DE REVISIÓN: Vía 15: Biosíntesis de Novo de Purinas y Pirimidinas
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 3444 a 3542 de 4188)
# Descripción      : PRPP, 5-PRA, anillo de purina hasta IMP/AMP/GMP, y vía del orotato (CAD, DHODH, UMPS) hasta UMP/CTP/dTMP.
# =============================================================================

    # =========================================================================
    # 15. RUTA 15: BIOSÍNTESIS DE NUCLEÓTIDOS (PURINAS Y PIRIMIDINAS)
    # =========================================================================
    partes.append(f'<g id="ruta_sintesis_nucleotidos">')
    
    x_nuc = 5120
    partes.append(badge_via(15, x_nuc - 40, 185))
    partes.append(f'''
    <g transform="translate({x_nuc}, 185)" data-arrastrable="1">
      <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="900" font-family="'Inter', sans-serif">BIOSÍNTESIS DE NUCLEÓTIDOS (DE NOVO Y SALVAMENTO)</text>
      <text x="0" y="16" fill="#0284c7" font-size="11" font-weight="800" font-family="'Inter', sans-serif">Rutas convergentes sobre PRPP • Purinas (IMP) y Pirimidinas (UMP)</text>
    </g>
    ''')

    # Enlace hacia Pentosas y nodo precursor Ribosa-5-P antes de PRPP Sintetasa
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="conexion_pentosas_prpp" data-arrastrable="1">
          <path d="M 2560 880 C 3600 700, 4600 245, 5080 245" fill="none" stroke="#059669" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
        </g>
        ''')
    partes.append(f'''
    <g id="m_nuc_r5p_in" data-arrastrable="1" transform="translate({x_nuc + 45}, 228)">
      <rect x="0" y="0" width="250" height="24" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
      <text x="125" y="16" fill="#047857" font-size="10" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">Ribosa-5-Fosfato [5C] (de Vía Pentosas)</text>
    </g>
    ''')

    # Paso 0: PRPP Sintetasa (Ribosa-5-P + ATP ➔ PRPP + AMP)
    partes.append(reaccion_libre(x_nuc + 130, 260, 38, "PRPP Sintetasa (PRS1)", entra="- 1 ATP", sale="+ 1 AMP", id_rx="rx_prpps"))
    partes.append(etiqueta_regulacion("prpp_s", x_nuc + 295, 266, dx=0, dy=0))

    # 1. PRPP (5-Fosforribosil-1-Pirofosfato)
    partes.append(nodo_libre(x_nuc + 80, 315, "PRPP", "5C", PRPP, "m_nuc_prpp", dx=165, detalle="5-Fosforribosil-1-Pirofosfato"))

    # Paso 1 comprometido de Purinas: PRPP Amidotransferasa (GPAT)
    partes.append(reaccion_libre(x_nuc + 130, 430, 38, "PRPP Amidotransferasa (GPAT)", entra="+ Gln + H₂O", sale="+ Glu + PPi", id_rx="rx_prppat"))
    partes.append(etiqueta_regulacion("prpp_at", x_nuc + 335, 436, dx=0, dy=0))

    # 1B. Intermediario comprometido: 5-Fosforribosilamina (5-PRA)
    partes.append(nodo_libre(x_nuc + 80, 485, "5-Fosforribosilamina (5-PRA)", "5C", NUC_5_PRA, "m_nuc_5pra", dx=140, detalle="1ᵉʳ intermediario purínico (N9)"))

    # Ensamblaje de los 9 pasos hacia IMP (GAR ➔ FGAR ➔ AIR ➔ AICAR ➔ FAICAR ➔ IMP)
    partes.append(reaccion_libre(x_nuc + 130, 590, 38, "Ensamblaje Purínico (9 pasos: GAR ➔ FAICAR)", entra="+ Gly, +2 Formil-THF", sale="+ Gln, +Asp, +CO₂", id_rx="rx_pur_9pasos"))

    # 2. IMP (Inosina Monofosfato - Bifurcación purínica)
    partes.append(nodo_libre(x_nuc + 80, 645, "Inosina Monofosfato (IMP)", "Base Hipoxantina", IMP, "m_nuc_imp", dx=120, detalle="Punto de ramificación purínica"))

    # 3. Bifurcación hacia AMP (izquierda) y GMP (derecha)
    partes.append(f'''
    <path d="M {x_nuc + 90} 770 Q {x_nuc} 795 {x_nuc - 20} 820" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc - 25}" y="795" fill="#0f172a" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">AdSS (+Asp, +GTP) ➔ AdSL</text>
    ''')
    partes.append(nodo_libre(x_nuc - 110, 825, "AMP (Adenosina-5'-P)", "Adenina", NUC_AMP, "m_nuc_amp", text_right=False, dx=-55, detalle="➔ ATP (Energía / ARN)"))

    partes.append(f'''
    <path d="M {x_nuc + 170} 770 Q {x_nuc + 260} 795 {x_nuc + 280} 820" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc + 285}" y="795" fill="#0f172a" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">IMPDH (+NAD⁺) ➔ GMPS (+Gln, +ATP)</text>
    ''')
    partes.append(nodo_libre(x_nuc + 220, 825, "GMP (Guanosina-5'-P)", "Guanina", NUC_GMP, "m_nuc_gmp", text_right=True, dx=115, detalle="➔ GTP (Señalización / ARN)"))

    # 4. Rama Pirimidinas (Síntesis de novo del anillo antes de unir PRPP)
    y_pir = 980
    partes.append(f'''
    <g id="m_nuc_pir_sustratos" data-arrastrable="1" transform="translate({x_nuc - 50}, {y_pir - 38})">
      <rect x="0" y="0" width="235" height="24" rx="8" fill="#eff6ff" stroke="#0284c7" stroke-width="1.5"/>
      <text x="117" y="16" fill="#0369a1" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">HCO₃⁻ + L-Glutamina + 2 ATP (Citosol)</text>
    </g>
    ''')
    partes.append(reaccion_libre(x_nuc + 50, y_pir - 6, 38, "CPS-II Citosólica (CAD)", entra="2 ATP + Gln", sale="2 ADP + Glu", id_rx="rx_cps2"))
    partes.append(etiqueta_regulacion("cps2", x_nuc + 275, y_pir, dx=0, dy=0))
    partes.append(nodo_libre(x_nuc - 50, y_pir + 45, "Carbamoil-Fosfato", "1C • Citosol", NUC_CARBAMOIL_P, "m_nuc_cp", dx=115, detalle="Precursor pirimidínico citosólico"))

    partes.append(reaccion_libre(x_nuc + 50, y_pir + 115, 38, "ATCasa + Dihidroorotasa", entra="+ L-Aspartato", sale="- Pi - H₂O", id_rx="rx_atcasa"))
    partes.append(etiqueta_regulacion("atcasa", x_nuc + 275, y_pir + 121, dx=0, dy=0))
    partes.append(nodo_libre(x_nuc - 50, y_pir + 168, "L-Dihidroorotato (DHO)", "4C • Vía Carbamoil-Asp", NUC_DHO, "m_nuc_dho", dx=115, detalle="Sustrato de DHODH mitocondrial"))

    partes.append(reaccion_libre(x_nuc + 50, y_pir + 260, 38, "Dihidroorotato DH (DHODH • MMI)", entra="+ CoQ (MMI)", sale="+ CoQH₂ (➔ CTE)", es_ganancia=True, id_rx="rx_dhodh"))
    partes.append(nodo_libre(x_nuc - 50, y_pir + 312, "Ácido Orotato", "Anillo Pirimidina", NUC_OROTATO, "m_nuc_orotato", dx=115, detalle="Acoplado a CoQ en cara externa MMI"))

    partes.append(reaccion_libre(x_nuc + 50, y_pir + 402, 38, "UMP Sintasa (OPRT + ODC)", entra="+ PRPP", sale="- PPi - CO₂", id_rx="rx_umps"))
    partes.append(nodo_libre(x_nuc - 50, y_pir + 455, "UMP (Uridina Monofosfato)", "Uracilo", NUC_UMP, "m_nuc_ump", dx=115, detalle="Precursor común pirimidinas"))

    # Bifurcación UMP ➔ CTP y dTMP
    partes.append(f'''
    <path d="M {x_nuc - 37} {y_pir + 568} Q {x_nuc - 51} {y_pir + 582} {x_nuc - 60} {y_pir + 595}" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc - 70}" y="{y_pir + 572}" fill="#0f172a" font-size="10" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">CTP Sintetasa (+Gln, -ATP)</text>
    ''')
    partes.append(nodo_libre(x_nuc - 140, y_pir + 605, "CTP (Citidina-5'-P)", "Citosina", NUC_CTP, "m_nuc_ctp", text_right=False, dx=-55, detalle="Precursor de ARN / Lípidos"))

    partes.append(f'''
    <path d="M {x_nuc + 120} {y_pir + 545} Q {x_nuc + 160} {y_pir + 572} {x_nuc + 180} {y_pir + 595}" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <text x="{x_nuc + 190}" y="{y_pir + 572}" fill="#0f172a" font-size="10" font-weight="700" font-family="'Inter', sans-serif">RNR ➔ Timidilato Sintasa (N⁵,N¹⁰-CH₂-THF)</text>
    ''')
    partes.append(nodo_libre(x_nuc + 130, y_pir + 605, "dTMP (Timidilato)", "Timina [ADN]", NUC_DTMP, "m_nuc_dtmp", text_right=True, dx=145, detalle="Diana 5-FU y Metotrexato"))
    partes.append(etiqueta_regulacion("ts", x_nuc + 280, y_pir + 675, dx=0, dy=0))

    partes.append(f'</g>')

