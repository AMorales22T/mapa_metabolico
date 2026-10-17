# =============================================================================
# MÓDULO DE REVISIÓN: Estequiometría de Nitrógeno y Nucleótidos (Vías 13, 14, 15 y 16)
# =============================================================================
# Archivo original : 06_REGULACION_Y_LEYENDA/reacciones_estequiometria.py (líneas 662 a 799 de 988)
# Descripción      : Ecuaciones balanceadas del Ciclo de la Urea, Síntesis de Purinas/Pirimidinas y Degradación a Ácido Úrico.
# =============================================================================

    # =========================================================================
    # VÍA 14: CICLO DE LA UREA
    # =========================================================================
    "rx_u_cps1": {
        "enzima": "Carbamoil-Fosfato Sintetasa-I (CPS-I)",
        "ec": "EC 6.3.4.16",
        "via": "Vía 14: Ciclo de la Urea",
        "compartimento": "Matriz Mitocondrial (Hepatocito)",
        "ecuacion": "NH₄⁺ + HCO₃⁻ + 2 ATP ➔ Carbamoil-Fosfato + 2 ADP + Pᵢ",
        "sustratos": ["Ion Amonio (NH₄⁺)", "Bicarbonato (HCO₃⁻)", "2 ATP"],
        "productos": ["Carbamoil-Fosfato", "2 ADP", "Pᵢ"],
        "coproductos": "2 ADP + Pᵢ (Gasto de 2 enlaces de alta energía)",
        "deltaG": "ΔG°' = -12.3 kJ/mol (Irreversible · Marcapasos limitante del ciclo de la urea)",
        "regulacion": "Activador alostérico obligado absoluto: N-Acetilglutamato (NAG), sintetizado por NAGS en respuesta a Arginina.",
        "relevancia": "Fija el amonio tóxico libre mitocondrial procedente de la desaminación oxidativa."
    },
    "rx_u_otc": {
        "enzima": "Ornitina Transcarbamilasa (OTC)",
        "ec": "EC 2.1.3.3",
        "via": "Vía 14: Ciclo de la Urea",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "Carbamoil-Fosfato + L-Ornitina ➔ L-Citrulina + Pᵢ",
        "sustratos": ["Carbamoil-Fosfato", "L-Ornitina"],
        "productos": ["L-Citrulina", "Pᵢ"],
        "coproductos": "Fosfato inorgánico (Pᵢ)",
        "deltaG": "ΔG°' = -32.6 kJ/mol (Irreversible)",
        "regulacion": "Deficiencia genética ligada al cromosoma X más frecuente del ciclo de la urea (hiperamonemia grave).",
        "relevancia": "Transfiere el grupo carbamilo a la ornitina; la citrulina resultante sale al citosol vía transportador ORNT1."
    },
    "rx_u_ass": {
        "enzima": "Argininosuccinato Sintetasa (ASS1)",
        "ec": "EC 6.3.4.5",
        "via": "Vía 14: Ciclo de la Urea",
        "compartimento": "Citosol",
        "ecuacion": "L-Citrulina + L-Aspartato + ATP ➔ Argininosuccinato + AMP + PPᵢ (➔ 2 Pᵢ)",
        "sustratos": ["L-Citrulina", "L-Aspartato", "ATP"],
        "productos": ["Argininosuccinato", "AMP", "Pirofosfato (PPᵢ)"],
        "coproductos": "AMP + 2 Pᵢ (Consumo equivalente a 2 ATP)",
        "deltaG": "ΔG°' global = -36.0 kJ/mol (con hidrólisis de PPᵢ)",
        "regulacion": "Controlada por suministro de Aspartato (procedente de la transaminación en mitocondria por GOT2).",
        "relevancia": "Incorpora el segundo átomo de nitrógeno de la urea procedente del aminoácido aspartato."
    },
    "rx_u_asl": {
        "enzima": "Argininosuccinato Liasa (ASL)",
        "ec": "EC 4.3.2.1",
        "via": "Vía 14: Ciclo de la Urea",
        "compartimento": "Citosol",
        "ecuacion": "Argininosuccinato ⇄ L-Arginina + Fumarato",
        "sustratos": ["Argininosuccinato"],
        "productos": ["L-Arginina", "Fumarato"],
        "coproductos": "Fumarato (Biciclo de Krebs: reingresa a mitocondria vía malato)",
        "deltaG": "Reversible ⇄",
        "regulacion": "Conecta el ciclo de la urea con el ciclo de Krebs (Krebs Bicycle).",
        "relevancia": "Libera arginina y genera fumarato, el cual amortigua el coste energético del ciclo mediante síntesis de NADH en Krebs."
    },
    "rx_u_arg1": {
        "enzima": "Arginasa-1 (ARG1)",
        "ec": "EC 3.5.3.1",
        "via": "Vía 14: Ciclo de la Urea",
        "compartimento": "Citosol (Exclusiva hepática)",
        "ecuacion": "L-Arginina + H₂O ➔ Urea + L-Ornitina",
        "sustratos": ["L-Arginina", "H₂O"],
        "productos": ["Urea (H₂N-CO-NH₂)", "L-Ornitina"],
        "coproductos": "Urea (producto de excreción soluble que viaja por sangre al riñón)",
        "deltaG": "ΔG°' = -12.1 kJ/mol (Irreversible)",
        "regulacion": "Inhibida competitivamente por ornitina y lisina.",
        "relevancia": "Cierra el ciclo regenerando la ornitina para un nuevo transporte mitocondrial y secreta urea no tóxica."
    },

    # =========================================================================
    # VÍA 15 Y 16: METABOLISMO DE NUCLEÓTIDOS Y ÁCIDO ÚRICO
    # =========================================================================
    "rx_prpps": {
        "enzima": "PRPP Sintetasa (Ribosa-Fosfato Pirofosfoquinasa)",
        "ec": "EC 2.7.6.1",
        "via": "Vía 15: Biosíntesis de Nucleótidos",
        "compartimento": "Citosol",
        "ecuacion": "Ribosa-5-Fosfato + ATP ➔ 5-Fosforribosil-1-Pirofosfato (PRPP) + AMP",
        "sustratos": ["Ribosa-5-Fosfato", "ATP"],
        "productos": ["PRPP", "AMP"],
        "coproductos": "AMP (Transferencia de pirofosfato directo)",
        "deltaG": "Irreversible",
        "regulacion": "⊕ Fosfato inorgánico (Pᵢ) | ⊖ Purinas (AMP, ADP, GMP, GDP por retroinhibición alostérica).",
        "relevancia": "Sustrato donador de ribosa-fosfato para síntesis de purinas, pirimidinas y NAD⁺."
    },
    "rx_prppat": {
        "enzima": "PRPP Amidotransferasa (Glutamina-PRPP Amidotransferasa)",
        "ec": "EC 2.4.2.14",
        "via": "Vía 15: Biosíntesis de Purinas de Novo",
        "compartimento": "Citosol",
        "ecuacion": "PRPP + L-Glutamina + H₂O ➔ 5-Fosforribosilamina + Glutamato + PPᵢ",
        "sustratos": ["PRPP", "L-Glutamina", "H₂O"],
        "productos": ["5-Fosforribosilamina", "L-Glutamato", "PPᵢ"],
        "coproductos": "PPᵢ (hidrolizado a 2 Pᵢ) + Glutamato",
        "deltaG": "ΔG°' = -30.0 kJ/mol (Irreversible · Marcapasos exclusivo purinas)",
        "regulacion": "⊕ PRPP (activación por avance) | ⊖ AMP, GMP, IMP (retroinhibición coordinada en sitios alostéricos separados).",
        "relevancia": "Paso de compromiso definitivo exclusivo hacia el anillo de purina (IMP)."
    },
    "rx_cps2": {
        "enzima": "Carbamoil-Fosfato Sintetasa-II (CPS-II / CAD)",
        "ec": "EC 6.3.5.5",
        "via": "Vía 15: Biosíntesis de Pirimidinas de Novo",
        "compartimento": "Citosol",
        "ecuacion": "2 ATP + L-Glutamina + HCO₃⁻ + H₂O ➔ Carbamoil-Fosfato + 2 ADP + Pᵢ + Glutamato",
        "sustratos": ["2 ATP", "L-Glutamina", "Bicarbonato (HCO₃⁻)"],
        "productos": ["Carbamoil-Fosfato citosólico", "2 ADP", "Pᵢ", "L-Glutamato"],
        "coproductos": "2 ADP + Pᵢ + Glutamato (Gasto de 2 ATP)",
        "deltaG": "Irreversible · Marcapasos de pirimidinas",
        "regulacion": "⊕ PRPP, ATP | ⊖ UTP (retroinhibición alostérica).",
        "relevancia": "A diferencia de CPS-I (mitocondrial, usa NH₄⁺), CPS-II es citosólica y utiliza el nitrógeno amida de la glutamina."
    },
    "rx_xod1": {
        "enzima": "Xantina Oxidasa (XOD / XO) · Paso 1",
        "ec": "EC 1.17.3.2",
        "via": "Vía 16: Catabolismo de Purinas",
        "compartimento": "Citosol (Hígado / Intestino)",
        "ecuacion": "Hipoxantina + H₂O + O₂ ➔ Xantina + H₂O₂",
        "sustratos": ["Hipoxantina", "H₂O", "O₂"],
        "productos": ["Xantina", "Peróxido de Hidrógeno (H₂O₂)"],
        "coproductos": "H₂O₂ (Detoxificado por Catalasa)",
        "deltaG": "Irreversible",
        "regulacion": "Diana farmacológica del Alopurinol y Febuxostat para tratamiento de la hiperuricemia y la gota.",
        "relevancia": "Primera hidroxilación oxidativa sobre el anillo de purina procedente de la adenina."
    },
    "rx_xod2": {
        "enzima": "Xantina Oxidasa (XOD / XO) · Paso 2",
        "ec": "EC 1.17.3.2",
        "via": "Vía 16: Catabolismo de Purinas",
        "compartimento": "Citosol (Hígado / Intestino)",
        "ecuacion": "Xantina + H₂O + O₂ ➔ Ácido Úrico (Urato) + H₂O₂",
        "sustratos": ["Xantina", "H₂O", "O₂"],
        "productos": ["Ácido Úrico (Urato)", "Peróxido de Hidrógeno (H₂O₂)"],
        "coproductos": "H₂O₂ (Detoxificado por Catalasa)",
        "deltaG": "Irreversible",
        "regulacion": "Inhibida competitivamente por Alopurinol (que es convertido a oxipurinol, inhibidor suicida).",
        "relevancia": "Producto final insoluble del catabolismo de purinas en humanos (carentes de uricasa). Precipita como urato monosódico en la gota."
    },

