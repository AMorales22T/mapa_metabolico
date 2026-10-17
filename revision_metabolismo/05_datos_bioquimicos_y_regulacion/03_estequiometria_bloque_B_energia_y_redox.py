# =============================================================================
# MÓDULO DE REVISIÓN: Estequiometría de Respiración Celular (Vías 5, 6, 7 y 8)
# =============================================================================
# Archivo original : 06_REGULACION_Y_LEYENDA/reacciones_estequiometria.py (líneas 305 a 463 de 988)
# Descripción      : Ecuaciones balanceadas de Complejo PDH, Ciclo de Krebs, Cadena Respiratoria y Lanzaderas.
# =============================================================================

    # =========================================================================
    # VÍA 5: COMPLEJO PIRUVATO DESHIDROGENASA (PDH)
    # =========================================================================
    "rx_pdh": {
        "enzima": "Complejo Piruvato Deshidrogenasa (E1 + E2 + E3)",
        "ec": "EC 1.2.4.1 / EC 2.3.1.12 / EC 1.8.1.4",
        "via": "Vía 5: Complejo PDH",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "Piruvato + CoA-SH + NAD⁺ ➔ Acetil-CoA + NADH + H⁺ + CO₂",
        "sustratos": ["Piruvato", "Coenzima A (CoA-SH)", "NAD⁺"],
        "productos": ["Acetil-CoA", "NADH", "H⁺", "CO₂"],
        "coproductos": "5 coenzimas: TPP (E1), Lipoamida (E2), CoA-SH (E2), FAD (E3), NAD⁺ (E3)",
        "deltaG": "ΔG°' = -33.4 kJ/mol (Completamente irreversible en animales)",
        "regulacion": "Alostérica: ⊖ Acetil-CoA, NADH, ATP | ⊕ ADP, Piruvato, Ca²⁺, NAD⁺, CoA-SH. Covalente: PDK fosforila E1 = inactiva; PDP (insulina, Ca²⁺) = activa.",
        "relevancia": "Encrucijada irreversible clave entre la glucólisis y el ciclo de Krebs / lipogénesis. Impide convertir grasas en glucosa."
    },

    # =========================================================================
    # VÍA 6: CICLO DE KREBS (CICLO DEL ÁCIDO CÍTRICO / TCA)
    # =========================================================================
    "rx_cs": {
        "enzima": "Citrato Sintasa",
        "ec": "EC 2.3.3.1",
        "via": "Vía 6: Ciclo de Krebs",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "Acetil-CoA + Oxalacetato + H₂O ➔ Citrato + CoA-SH + H⁺",
        "sustratos": ["Acetil-CoA", "Oxalacetato", "H₂O"],
        "productos": ["Citrato", "CoA-SH", "H⁺"],
        "coproductos": "CoA-SH liberada por hidrólisis del tioéster intermedio citril-CoA",
        "deltaG": "ΔG°' = -31.5 kJ/mol (Irreversible · Entrada al ciclo)",
        "regulacion": "⊕ ADP, sustratos | ⊖ ATP, NADH, Succinil-CoA, Citrato (retroinhibición).",
        "relevancia": "Condensación de entrada que fusiona el acetilo (2C) con el oxalacetato (4C) para iniciar la degradación aerobia."
    },
    "rx_acon": {
        "enzima": "Aconitasa (Aconitato Hidratasa)",
        "ec": "EC 4.2.1.3",
        "via": "Vía 6: Ciclo de Krebs",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "Citrato ⇄ [cis-Aconitato] + H₂O ⇄ D-Isocitrato",
        "sustratos": ["Citrato"],
        "productos": ["D-Isocitrato"],
        "coproductos": "Centro de hierro-azufre [4Fe-4S] catalítico",
        "deltaG": "ΔG°' = +6.3 kJ/mol (Reversible ⇄ · Favorable hacia citrato en equilibrio)",
        "regulacion": "Inhibida por fluoroacetato (se convierte en fluorocitrato, veneno mitocondrial).",
        "relevancia": "Isomeriza el alcohol terciario del citrato en un alcohol secundario oxidable (isocitrato)."
    },
    "rx_icdh": {
        "enzima": "Isocitrato Deshidrogenasa Mitocondrial (NAD⁺ dependiente)",
        "ec": "EC 1.1.1.41",
        "via": "Vía 6: Ciclo de Krebs",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "D-Isocitrato + NAD⁺ ➔ α-Cetoglutarato + NADH + H⁺ + CO₂",
        "sustratos": ["D-Isocitrato", "NAD⁺"],
        "productos": ["α-Cetoglutarato (2-Oxoglutarato)", "NADH", "H⁺", "CO₂"],
        "coproductos": "NADH + H⁺ + CO₂ (1.ª descarboxilación oxidativa del ciclo)",
        "deltaG": "ΔG°' = -8.4 kJ/mol (Irreversible · Marcapasos clave del ciclo de Krebs)",
        "regulacion": "⊕ ADP (alostérico positivo potente), Ca²⁺ | ⊖ ATP, NADH.",
        "relevancia": "Paso marcapasos del ciclo de Krebs: acelera el ciclo ante bajo estado energético celular."
    },
    "rx_akgdh": {
        "enzima": "α-Cetoglutarato Deshidrogenasa (Complejo multienzimático)",
        "ec": "EC 1.2.4.2 / EC 2.3.1.61 / EC 1.8.1.4",
        "via": "Vía 6: Ciclo de Krebs",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "α-Cetoglutarato + CoA-SH + NAD⁺ ➔ Succinil-CoA + NADH + H⁺ + CO₂",
        "sustratos": ["α-Cetoglutarato", "CoA-SH", "NAD⁺"],
        "productos": ["Succinil-CoA", "NADH", "H⁺", "CO₂"],
        "coproductos": "NADH + H⁺ + CO₂ (2.ª descarboxilación oxidativa)",
        "deltaG": "ΔG°' = -30.1 kJ/mol (Completamente irreversible)",
        "regulacion": "⊕ Ca²⁺, AMP | ⊖ Succinil-CoA, NADH, ATP, GTP.",
        "relevancia": "Homólogo al complejo PDH; completa la pérdida de los dos carbonos introducidos como Acetil-CoA."
    },
    "rx_scas": {
        "enzima": "Succinil-CoA Sintetasa (Succinato Tioquinasa)",
        "ec": "EC 6.2.1.4 (GTP) / EC 6.2.1.5 (ATP)",
        "via": "Vía 6: Ciclo de Krebs",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "Succinil-CoA + GDP + Pᵢ ⇄ Succinato + GTP + CoA-SH",
        "sustratos": ["Succinil-CoA", "GDP", "Pᵢ"],
        "productos": ["Succinato", "GTP", "CoA-SH"],
        "coproductos": "GTP (hígado/riñón) / ATP (músculo/cerebro) + CoA-SH",
        "deltaG": "ΔG°' = -3.4 kJ/mol (Reversible ⇄ · Fosforilación a nivel de sustrato mitocondrial)",
        "regulacion": "Regulada por balance de sustratos y nucleótidos de guanina/adenina.",
        "relevancia": "Única fosforilación a nivel de sustrato en la matriz mitocondrial."
    },
    "rx_sdh": {
        "enzima": "Succinato Deshidrogenasa (Complejo II de la CTE)",
        "ec": "EC 1.3.5.1",
        "via": "Vía 6 y 7: Ciclo de Krebs / Cadena Respiratoria",
        "compartimento": "Membrana Mitocondrial Interna (MMI)",
        "ecuacion": "Succinato + FAD ⇄ Fumarato + FADH₂ (electrones transferidos a CoQ ➔ CoQH₂)",
        "sustratos": ["Succinato", "FAD (unido covalentemente a histidina)"],
        "productos": ["Fumarato", "FADH₂ (➔ Ubiquinol CoQH₂)"],
        "coproductos": "FADH₂ que cede electrones a los centros Fe-S y a la Coenzima Q",
        "deltaG": "ΔG°' = 0 kJ/mol (Reversible ⇄)",
        "regulacion": "Inhibida competitivamente por Malonato (análogo estructural con 3C).",
        "relevancia": "Enzima dual: cataliza la oxidación de succinato a fumarato mientras alimenta directamente la cadena respiratoria."
    },
    "rx_fum": {
        "enzima": "Fumarasa (Fumarato Hidratasa)",
        "ec": "EC 4.2.1.2",
        "via": "Vía 6: Ciclo de Krebs",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "Fumarato + H₂O ⇄ L-Malato",
        "sustratos": ["Fumarato", "H₂O"],
        "productos": ["L-Malato"],
        "coproductos": "H₂O (Hidratación estereoespecífica trans)",
        "deltaG": "ΔG°' = -3.8 kJ/mol (Reversible ⇄)",
        "regulacion": "Equilibrio dependiente de sustratos.",
        "relevancia": "Punto de convergencia metabólica: recibe fumarato del ciclo de la urea, degradación de Tyr/Phe y purinas."
    },
    "rx_mdh_retorno": {
        "enzima": "Malato Deshidrogenasa Mitocondrial (MDH2)",
        "ec": "EC 1.1.1.37",
        "via": "Vía 6: Ciclo de Krebs",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "L-Malato + NAD⁺ ⇄ Oxalacetato + NADH + H⁺",
        "sustratos": ["L-Malato", "NAD⁺"],
        "productos": ["Oxalacetato", "NADH", "H⁺"],
        "coproductos": "NADH + H⁺ (Tercer NADH generado en el ciclo)",
        "deltaG": "ΔG°' = +29.7 kJ/mol (Desfavorable in vitro, impulsada in vivo por rápido consumo de OAA en Citrato Sintasa)",
        "regulacion": "Inhibida por concentración elevada de NADH.",
        "relevancia": "Regenera el oxalacetato para permitir una nueva vuelta del ciclo de Krebs."
    },

    # =========================================================================
    # VÍA 7: CADENA DE TRANSPORTE DE ELECTRONES Y ATP SINTASA
    # =========================================================================
    "rx_atpsint": {
        "enzima": "ATP Sintasa (Complejo V / F₀F₁)",
        "ec": "EC 7.1.2.2",
        "via": "Vía 7: Cadena Respiratoria & Fosforilación Oxidativa",
        "compartimento": "Membrana Mitocondrial Interna (MMI)",
        "ecuacion": "ADP + Pᵢ + 4 H⁺(intermembrana) ➔ ATP + H₂O + 4 H⁺(matriz)",
        "sustratos": ["ADP", "Pᵢ", "Gradiente de Protones (ΔμH⁺)"],
        "productos": ["ATP", "H₂O"],
        "coproductos": "Retorno de ~4 H⁺ por ATP sintetizado y translocado",
        "deltaG": "ΔG°' = +30.5 kJ/mol (Impulsada por la fuerza protón-motriz)",
        "regulacion": "Control respiratorio estricto por disponibilidad de ADP; inhibida por Oligomicina; desacoplada por UCP1/termogenina.",
        "relevancia": "Generador del 90% del ATP corporal total mediante catálisis rotacional quimiosmótica."
    },

    # =========================================================================
    # VÍA 8: LANZADERAS METABÓLICAS
    # =========================================================================
    "rx_cgpdh": {
        "enzima": "Glicerol-3-Fosfato Deshidrogenasa Citosólica (GPD1) y Mitocondrial (GPD2)",
        "ec": "EC 1.1.1.8 / EC 1.1.5.3",
        "via": "Vía 8B: Lanzadera de Glicerol-Fosfato",
        "compartimento": "Citosol / Membrana Mitocondrial Interna (Cara Externa)",
        "ecuacion": "NADH(cito) + H⁺ + DHAP ➔ NAD⁺ + G3P  ➔  G3P + FAD(mGPDH) ➔ DHAP + FADH₂ (➔ CoQ ➔ 1.5 ATP)",
        "sustratos": ["NADH citosólico", "DHAP"],
        "productos": ["NAD⁺ regenerado citosólico", "CoQH₂ en MMI (1.5 ATP)"],
        "coproductos": "FADH₂ intermedio que transfiere electrones al pool de Ubiquinona",
        "deltaG": "Irreversible hacia la mitocondria",
        "regulacion": "Predomina en músculo esquelético y cerebro para regeneración ultra-rápida de NAD⁺ glucolítico.",
        "relevancia": "Transporta electrones de NADH citosólico a la CTE eludiendo los transportadores mitocondriales lentos."
    },

