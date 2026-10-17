# =============================================================================
# MÓDULO DE REVISIÓN: Estequiometría de Lípidos (Vías 9, 10, 11 y 12)
# =============================================================================
# Archivo original : 06_REGULACION_Y_LEYENDA/reacciones_estequiometria.py (líneas 464 a 661 de 988)
# Descripción      : Ecuaciones balanceadas de Beta-Oxidación, Lipogénesis, Cetogénesis y Biosíntesis de Colesterol.
# =============================================================================

    # =========================================================================
    # VÍA 9: β-OXIDACIÓN DE ÁCIDOS GRASOS
    # =========================================================================
    "rx_acs": {
        "enzima": "Acil-CoA Sintetasa (Tiocinasa de Ácidos Grasos)",
        "ec": "EC 6.2.1.3",
        "via": "Vía 9: Activación de Ácidos Grasos",
        "compartimento": "Membrana Mitocondrial Externa (MME) / Citosol",
        "ecuacion": "Ácido Graso (Palmitato 16C) + ATP + CoA-SH ➔ Acil-CoA (Palmitoil-CoA) + AMP + PPᵢ (➔ 2 Pᵢ)",
        "sustratos": ["Ácido Graso libre", "ATP", "CoA-SH"],
        "productos": ["Acil-CoA", "AMP", "Pirofosfato inorgánico (PPᵢ)"],
        "coproductos": "Gasto equivalente a 2 enlaces de alta energía (ATP ➔ AMP + 2 Pᵢ)",
        "deltaG": "ΔG°' global = -32.5 kJ/mol (con hidrólisis de PPᵢ)",
        "regulacion": "Impulsada por pirofosfatasa inorgánica; activación previa al transporte por carnitina.",
        "relevancia": "Activación termodinámica obligatoria de los ácidos grasos antes de su entrada a la mitocondria."
    },
    "rx_cpt1": {
        "enzima": "Carnitina Palmitoiltransferasa-1 (CPT-1 / CAT-1)",
        "ec": "EC 2.3.1.21",
        "via": "Vía 9: Lanzadera de Carnitina",
        "compartimento": "Membrana Mitocondrial Externa (MME)",
        "ecuacion": "Palmitoil-CoA + L-Carnitina ➔ Palmitoil-Carnitina + CoA-SH",
        "sustratos": ["Palmitoil-CoA", "L-Carnitina"],
        "productos": ["Palmitoil-Carnitina", "CoA-SH"],
        "coproductos": "CoA-SH libre citosólica",
        "deltaG": "ΔG°' ≈ 0 kJ/mol (Transferencia de acilo)",
        "regulacion": "Inhibidor alostérico crucial: Malonil-CoA (primer intermediario de la síntesis de ácidos grasos).",
        "relevancia": "Marcapasos y punto de control exclusivo de la β-oxidación: evita la oxidación simultánea a la síntesis (ciclo fútil)."
    },
    "rx_cpt2": {
        "enzima": "Carnitina Palmitoiltransferasa-2 (CPT-2)",
        "ec": "EC 2.3.1.21",
        "via": "Vía 9: Lanzadera de Carnitina",
        "compartimento": "Membrana Mitocondrial Interna (Cara Matriz)",
        "ecuacion": "Palmitoil-Carnitina + CoA-SH(matriz) ➔ Palmitoil-CoA + L-Carnitina",
        "sustratos": ["Palmitoil-Carnitina", "CoA-SH mitocondrial"],
        "productos": ["Palmitoil-CoA", "L-Carnitina"],
        "coproductos": "L-Carnitina liberada que retorna al EIM vía translocasa CACT",
        "deltaG": "Reversible ⇄",
        "regulacion": "Dependiente de la disponibilidad de CoA-SH en la matriz.",
        "relevancia": "Reconstituye el Acil-CoA en el interior de la matriz mitocondrial listo para la espiral de Lynen."
    },
    "rx_box1": {
        "enzima": "Acil-CoA Deshidrogenasa (VLCAD / MCAD / SCAD)",
        "ec": "EC 1.3.8.7 (MCAD)",
        "via": "Vía 9: Espiral de β-Oxidación (Paso 1)",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "Acil-CoA + FAD ➔ trans-Δ²-Enoil-CoA + FADH₂ (➔ ETF ➔ CoQ ➔ 1.5 ATP)",
        "sustratos": ["Acil-CoA", "FAD"],
        "productos": ["trans-Δ²-Enoil-CoA", "FADH₂"],
        "coproductos": "FADH₂ (Oxidado por Flavoproteína de Transferencia de Electrones ETF a CoQ)",
        "deltaG": "Irreversible",
        "regulacion": "Su deficiencia genética más común (déficit de MCAD) causa hipoglucemia hipocetósica grave en ayuno.",
        "relevancia": "Introduce un doble enlace trans entre C2 y C3, generando el primer cofactor reducido de la espiral."
    },
    "rx_box1b": {
        "enzima": "Enoil-CoA Hidratasa (Crotonasa)",
        "ec": "EC 4.2.1.17",
        "via": "Vía 9: Espiral de β-Oxidación (Paso 2)",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "trans-Δ²-Enoil-CoA + H₂O ➔ L-β-Hidroxiacil-CoA",
        "sustratos": ["trans-Δ²-Enoil-CoA", "H₂O"],
        "productos": ["L-β-Hidroxiacil-CoA"],
        "coproductos": "H₂O (Hidratación estereoespecífica del doble enlace)",
        "deltaG": "Reversible ⇄",
        "regulacion": "Controlada por flujo de sustratos.",
        "relevancia": "Adiciona una molécula de agua para crear un grupo hidroxilo en posición beta."
    },
    "rx_box2": {
        "enzima": "L-β-Hidroxiacil-CoA Deshidrogenasa",
        "ec": "EC 1.1.1.35",
        "via": "Vía 9: Espiral de β-Oxidación (Paso 3)",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "L-β-Hidroxiacil-CoA + NAD⁺ ⇄ β-Cetoacil-CoA + NADH + H⁺",
        "sustratos": ["L-β-Hidroxiacil-CoA", "NAD⁺"],
        "productos": ["β-Cetoacil-CoA", "NADH", "H⁺"],
        "coproductos": "NADH + H⁺ (➔ Complejo I de CTE ➔ 2.5 ATP)",
        "deltaG": "Reversible ⇄ (Inhibida por relación NADH/NAD⁺ alta)",
        "regulacion": "Controlada por el estado redox mitocondrial.",
        "relevancia": "Oxida el hidroxilo beta a grupo carbonilo ceto preparando el enlace para tiólisis."
    },
    "rx_box3": {
        "enzima": "β-Cetotiolasa (Acil-CoA Acetiltransferasa)",
        "ec": "EC 2.3.1.16",
        "via": "Vía 9: Espiral de β-Oxidación (Paso 4)",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "β-Cetoacil-CoA + CoA-SH ➔ Acil-CoA (acortado en 2C) + Acetil-CoA",
        "sustratos": ["β-Cetoacil-CoA", "CoA-SH"],
        "productos": ["Acil-CoA (n-2 carbonos)", "Acetil-CoA"],
        "coproductos": "Acetil-CoA (➔ Krebs o Cetogénesis)",
        "deltaG": "ΔG°' = -28.0 kJ/mol (Irreversible por escisión tiolítica exergónica)",
        "regulacion": "Inhibida por concentraciones altas de Acetil-CoA.",
        "relevancia": "Libera una unidad de Acetil-CoA y recircula el ácido graso acortado en 2C a una nueva vuelta."
    },

    # =========================================================================
    # VÍA 10: LIPOGÉNESIS (SÍNTESIS DE NOVO DE ÁCIDOS GRASOS)
    # =========================================================================
    "rx_acly": {
        "enzima": "ATP-Citrato Liasa (ACLY)",
        "ec": "EC 2.3.3.8",
        "via": "Vía 10: Lipogénesis",
        "compartimento": "Citosol",
        "ecuacion": "Citrato + ATP + CoA-SH ➔ Acetil-CoA + Oxalacetato + ADP + Pᵢ",
        "sustratos": ["Citrato", "ATP", "CoA-SH"],
        "productos": ["Acetil-CoA", "Oxalacetato", "ADP", "Pᵢ"],
        "coproductos": "ADP + Pᵢ (Gasto de 1 ATP)",
        "deltaG": "ΔG°' = -18.0 kJ/mol (Irreversible)",
        "regulacion": "Activada por fosforilación por Akt (vía insulina); inducida por dieta rica en glúcidos (SREBP-1c).",
        "relevancia": "Libera el Acetil-CoA en el citosol a partir del citrato exportado desde la mitocondria."
    },
    "rx_acc": {
        "enzima": "Acetil-CoA Carboxilasa (ACC1 / ACC2)",
        "ec": "EC 6.4.1.2",
        "via": "Vía 10: Lipogénesis",
        "compartimento": "Citosol",
        "ecuacion": "Acetil-CoA + HCO₃⁻ + ATP ➔ Malonil-CoA + ADP + Pᵢ",
        "sustratos": ["Acetil-CoA", "Bicarbonato (HCO₃⁻)", "ATP"],
        "productos": ["Malonil-CoA", "ADP", "Pᵢ"],
        "coproductos": "Cofactor: Biotina (Gasto de 1 ATP)",
        "deltaG": "ΔG°' = -19.7 kJ/mol (Irreversible · Marcapasos limitante de la síntesis de AG)",
        "regulacion": "⊕ Citrato (estimula polimerización activa), Insulina (desfosforilación por PP2A) | ⊖ Palmitoil-CoA, AMPK (fosforilación en baja energía), Glucagón.",
        "relevancia": "Sintetiza Malonil-CoA, inhibidor de CPT-1 y donador de 2 carbonos para la elongación por FAS."
    },
    "rx_fas1": {
        "enzima": "Ácido Graso Sintasa (FAS) · Ciclo de Elongación",
        "ec": "EC 2.3.1.85",
        "via": "Vía 10: Lipogénesis",
        "compartimento": "Citosol",
        "ecuacion": "Acetil-CoA + 7 Malonil-CoA + 14 NADPH + 14 H⁺ ➔ Palmitato + 7 CO₂ + 8 CoA-SH + 14 NADP⁺ + 6 H₂O",
        "sustratos": ["Acetil-CoA (cebador)", "7 Malonil-CoA", "14 NADPH", "14 H⁺"],
        "productos": ["Palmitato (16C)", "7 CO₂", "8 CoA-SH", "14 NADP⁺", "6 H₂O"],
        "coproductos": "14 NADP⁺ + 7 CO₂ (Consumo de 14 NADPH)",
        "deltaG": "Irreversible",
        "regulacion": "Control transcripcional a largo plazo inducido por insulina vía SREBP-1c.",
        "relevancia": "Complejo homodimérico multifuncional que construye el ácido palmítico de 16 carbonos."
    },

    # =========================================================================
    # VÍA 11: CETOGÉNESIS
    # =========================================================================
    "rx_ceto1": {
        "enzima": "Mitocondrial Tiolasa / HMG-CoA Sintasa Mitocondrial (HMGCS2)",
        "ec": "EC 2.3.1.9 / EC 2.3.3.10",
        "via": "Vía 11: Cetogénesis",
        "compartimento": "Matriz Mitocondrial (Hepatocito exclusivamente)",
        "ecuacion": "2 Acetil-CoA ➔ Acetoacetil-CoA + CoA-SH  ➔ + Acetil-CoA + H₂O ➔ HMG-CoA + CoA-SH",
        "sustratos": ["3 Acetil-CoA", "H₂O"],
        "productos": ["HMG-CoA (3-Hidroxi-3-Metilglutaril-CoA)", "2 CoA-SH"],
        "coproductos": "2 CoA-SH libres regeneradas para continuar la β-oxidación",
        "deltaG": "Irreversible",
        "regulacion": "HMGCS2 es el marcapasos: inducida en ayuno por glucagón/ácidos grasos (PPAR-α); inhibida por insulina.",
        "relevancia": "Canaliza el exceso de Acetil-CoA de la β-oxidación cuando el oxalacetato se desvía a gluconeogénesis."
    },
    "rx_ceto2": {
        "enzima": "HMG-CoA Liasa Mitocondrial",
        "ec": "EC 4.1.3.4",
        "via": "Vía 11: Cetogénesis",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "HMG-CoA ➔ Acetoacetato + Acetil-CoA",
        "sustratos": ["HMG-CoA"],
        "productos": ["Acetoacetato (1.er cuerpo cetónico)", "Acetil-CoA"],
        "coproductos": "Acetil-CoA regenerado",
        "deltaG": "Irreversible",
        "regulacion": "Expresión exclusiva hepática en mitocondrias.",
        "relevancia": "Escinde el HMG-CoA liberando el primer cuerpo cetónico soluble al torrente sanguíneo."
    },
    "rx_ceto3": {
        "enzima": "β-Hidroxibutirato Deshidrogenasa Mitocondrial",
        "ec": "EC 1.1.1.30",
        "via": "Vía 11: Cetogénesis",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "Acetoacetato + NADH + H⁺ ⇄ D-β-Hidroxibutirato + NAD⁺",
        "sustratos": ["Acetoacetato", "NADH", "H⁺"],
        "productos": ["D-β-Hidroxibutirato", "NAD⁺"],
        "coproductos": "NAD⁺ (Regenerado en matriz)",
        "deltaG": "Reversible ⇄ (Equilibrio determinado por la relación NADH/NAD⁺ mitocondrial)",
        "regulacion": "En ayuno prolongado predomina la forma reducida β-hidroxibutirato (relación 3:1 a 5:1).",
        "relevancia": "Principal combustible cetónico circulante para cerebro, músculo cardíaco y corteza renal."
    },

    # =========================================================================
    # VÍA 12: BIOSÍNTESIS DE COLESTEROL
    # =========================================================================
    "rx_hmgcr": {
        "enzima": "HMG-CoA Reductasa (HMGCR)",
        "ec": "EC 1.1.1.34",
        "via": "Vía 12: Síntesis de Colesterol",
        "compartimento": "Retículo Endoplásmico / Citosol",
        "ecuacion": "HMG-CoA + 2 NADPH + 2 H⁺ ➔ Mevalonato + CoA-SH + 2 NADP⁺",
        "sustratos": ["HMG-CoA citosólico", "2 NADPH", "2 H⁺"],
        "productos": ["Mevalonato", "CoA-SH", "2 NADP⁺"],
        "coproductos": "CoA-SH + 2 NADP⁺ (Consumo de 2 equivalentes de NADPH)",
        "deltaG": "ΔG°' = -37.7 kJ/mol (Irreversible · Marcapasos limitante absoluto de la síntesis de colesterol)",
        "regulacion": "⊕ Insulina (desfosforilación), SREBP-2 | ⊖ Colesterol libre (degradación por INSIG), AMPK (fosforilación), Estatinas (inhibidores competitivos reversibles).",
        "relevancia": "Diana farmacológica de las Estatinas (Atorvastatina, Simvastatina) para reducir la colesterolemia LDL."
    },

