# =============================================================================
# MÓDULO DE REVISIÓN: Vía 24: Biosíntesis de Aminoácidos No Esenciales
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/generar_ampliacion.py (líneas 567 a 613 de 925)
# Descripción      : Síntesis de Ala, Asp, Asn, Glu, Gln, Pro, Ser, Gly, Cys y Tyr a partir de piruvato, OAA, alfa-KG, 3-PG y fenilalanina.
# =============================================================================

    # -------------------------------------------------------------------------
    # VÍA 24: BIOSÍNTESIS DE AMINOÁCIDOS NO ESENCIALES
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_biosintesis_aminoacidos" class="ruta-metabolica">')
    p.append(encabezado_via(5850, 2350, 24, "BIOSÍNTESIS DE AMINOÁCIDOS NO ESENCIALES", "Esqueletos centrales de Glucólisis y Krebs ➔ Transaminación (PLP)", color="#059669"))

    # Piruvato a Alanina
    p.append(nodo_libre(5880, 2430, "Piruvato (Glucólisis)", "3C", eaa.PIRUVATO_AMINO, "m_aa_pyr", dx=140, dy=20, detalle="Esqueleto cetoácido"))
    p.append(reaccion_flecha(6020, 2525, 55, "ALT (Alanina Aminotransferasa)", entra="+ Glutamato", sale="+ α-KG", ec="EC 2.6.1.2 (PLP)", color="#059669", reversible=True, id_rx="rx_alt_amino"))
    p.append(nodo_libre(5880, 2600, "L-Alanina", "3C", eaa.ALANINA, "m_aa_ala", dx=140, dy=20, detalle="Transaminación directa"))

    # Oxalacetato a Aspartato y Asparagina
    p.append(nodo_libre(6220, 2430, "Oxalacetato (Krebs)", "4C", eaa.OXALACETATO_AMINO, "m_aa_oaa", dx=140, dy=20, detalle="Cetoácido dicarboxílico"))
    p.append(reaccion_flecha(6360, 2565, 55, "AST (Aspartato Aminotransferasa)", entra="+ Glu", sale="+ α-KG", ec="EC 2.6.1.1 (PLP)", color="#059669", reversible=True, curvas_side="right", text_dx=-14, text_anchor="end", id_rx="rx_ast_amino"))
    p.append(nodo_libre(6220, 2640, "L-Aspartato", "4C", eaa.ASPARTATO_AMINO, "m_aa_asp", dx=140, dy=20, detalle="Donador de N en Urea"))
    p.append(reaccion_flecha(6360, 2775, 55, "Asparagina Sintetasa", entra="+ Gln + ATP", sale="+ Glu + AMP + PPi", ec="EC 6.3.5.4", color="#059669", curvas_side="right", text_dx=-14, text_anchor="end", id_rx="rx_asn_sintetasa"))
    p.append(nodo_libre(6220, 2850, "L-Asparagina", "4C", ea.L_ASPARAGINA, "m_aa_asn", dx=140, dy=20, detalle="Amida neutra"))

    # α-Cetoglutarato a Glutamato, Glutamina y Prolina
    p.append(nodo_libre(5880, 2715, "α-Cetoglutarato (Krebs)", "5C", eaa.ALFA_CETOGLUTARATO, "m_aa_akg", dx=140, dy=20, detalle="Colector común de nitrógeno"))
    p.append(reaccion_flecha(6020, 2870, 55, "GDH (Glutamato DH)", entra="+ NH₄⁺ + NADPH", sale="+ NADP⁺", ec="EC 1.4.1.3", color="#059669", reversible=True, id_rx="rx_gdh_amino"))
    p.append(nodo_libre(5880, 2945, "L-Glutamato", "5C", eaa.GLUTAMATO, "m_aa_glu", dx=140, dy=20, detalle="Aminoácido central del metabolismo"))
    
    p.append("""
    <g id="rx_gln_sintetasa" transform="translate(6020, 3080)">
      <path d="M 0 0 L 0 50" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>
      <text x="14" y="26" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a">Glutamina Sintetasa (+ NH₄⁺, ATP)</text>
    </g>
    """)
    p.append(nodo_libre(5880, 3150, "L-Glutamina", "5C", eaa.GLUTAMINA, "m_aa_gln", dx=140, dy=20, detalle="Transporte no tóxico de amonio"))
    p.append(nodo_libre(6220, 3150, "L-Prolina", "5C", ea.L_PROLINA, "m_aa_pro", dx=140, dy=20, detalle="Iminoácido cíclico"))

    # 3-Fosfoglicerato a Serina, Glicina y Cisteína
    p.append(nodo_libre(5880, 3300, "3-Fosfoglicerato (Glucólisis)", "3C-P", ea.GLICEROL_ESTRUCTURA, "m_aa_3pg", dx=140, dy=20, detalle="Vía de biosíntesis de serina"))
    p.append(reaccion_flecha(6020, 3410, 55, "Vía de Fosfoserina (3 pasos)", entra="+ NAD⁺ + Glu", sale="+ NADH + α-KG + Pi", ec="PHGDH / PSAT / PSP", color="#059669", id_rx="rx_via_serina"))
    p.append(nodo_libre(5880, 3485, "L-Serina", "3C", ea.L_SERINA, "m_aa_ser", dx=140, dy=20, detalle="Precursor de Gly, Cys y Esfingolípidos"))

    p.append(reaccion_flecha(6020, 3610, 55, "SHMT (Serina Hidroximetiltransferasa)", entra="+ THF", sale="+ N⁵,N¹⁰-CH₂-THF", ec="EC 2.1.2.1 (PLP)", color="#059669", reversible=True, id_rx="rx_shmt"))
    p.append(nodo_libre(5880, 3685, "Glicina", "2C", ea.L_GLICINA, "m_aa_gly", dx=140, dy=20, detalle="Hemo • Purinas • Glutatión"))
    p.append(nodo_libre(6220, 3685, "L-Cisteína", "3C", ea.L_CISTEINA, "m_aa_cys", dx=140, dy=20, detalle="Azufre derivado de Metionina"))

    # Fenilalanina a Tirosina
    p.append(nodo_libre(5880, 3840, "L-Fenilalanina (Esencial)", "9C", eda.FENILALANINA, "m_aa_phe", dx=140, dy=20, detalle="Aminoácido aromático dietario"))
    p.append(reaccion_flecha(6020, 4005, 55, "PAH (Fenilalanina Hidroxilasa)", entra="+ O₂ + BH₄", sale="+ BH₂ + H₂O", ec="EC 1.14.16.1", color="#059669", id_rx="rx_pah"))
    p.append(nodo_libre(5880, 4080, "L-Tirosina", "9C", eda.TIROSINA, "m_aa_tyr", dx=140, dy=20, detalle="Precursor de Catecolaminas y Melanina"))
    p.append('</g>')

