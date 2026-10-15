#!/usr/bin/env python3
"""
BASE DE DATOS BIOQUÍMICA ESTEQUIOMÉTRICA DE REACCIONES METABÓLICAS
===================================================================
Proporciona la ecuación química balanceada, reactivos, productos principales,
coproductos (cofactores), reversibilidad/energética (ΔG°'), regulación y
relevancia clínica/fisiológica de todas las reacciones de las 25 vías metabólicas.

Utilizado para:
1. Enriquecer los visores interactivos web (01_mapa_ampliado_completo_25_vias.html, etc.).
2. Ficha flotante inteligente (tooltip enriquecido al pasar el ratón o cliquear).
3. Documentación estequiométrica rigurosa del repositorio.
"""

REACCIONES_ESTEQUIOMETRIA = {
    # =========================================================================
    # VÍA 1: GLUCÓLISIS CITOSÓLICA
    # =========================================================================
    "rx_hk": {
        "enzima": "Hexoquinasa (I–III) / Glucoquinasa (IV)",
        "ec": "EC 2.7.1.1",
        "via": "Vía 1: Glucólisis",
        "compartimento": "Citosol (Hepatocito / Miocito)",
        "ecuacion": "D-Glucosa + ATP ➔ D-Glucosa-6-Fosfato + ADP + H⁺",
        "sustratos": ["D-Glucosa", "ATP"],
        "productos": ["D-Glucosa-6-Fosfato", "ADP", "H⁺"],
        "coproductos": "ADP (Gasto de 1 enlace de alta energía)",
        "deltaG": "ΔG°' = -16.7 kJ/mol (Irreversible · Paso limitante 1)",
        "regulacion": "HK: ⊖ Glucosa-6-P | GK (hígado): secuestrada en núcleo por GKRP (⊖ F6P), inducida por insulina.",
        "relevancia": "Fosforilación de atrapamiento: impide la salida de la glucosa a través de los transportadores GLUT."
    },
    "rx_pgi": {
        "enzima": "Fosfoglucosa Isomerasa (PGI)",
        "ec": "EC 5.3.1.9",
        "via": "Vía 1: Glucólisis",
        "compartimento": "Citosol",
        "ecuacion": "D-Glucosa-6-Fosfato ⇄ D-Fructosa-6-Fosfato",
        "sustratos": ["D-Glucosa-6-Fosfato"],
        "productos": ["D-Fructosa-6-Fosfato"],
        "coproductos": "Ninguno (Isomerización aldosa ⇄ cetosa)",
        "deltaG": "ΔG°' = +1.7 kJ/mol (Reversible ⇄ cerca del equilibrio)",
        "regulacion": "Controlada por balance de masas [G6P]/[F6P].",
        "relevancia": "Prepara la molécula para la posterior fosforilación en C1 y ruptura simétrica en dos triosas."
    },
    "rx_pfk1": {
        "enzima": "Fosfofructoquinasa-1 (PFK-1)",
        "ec": "EC 2.7.1.11",
        "via": "Vía 1: Glucólisis",
        "compartimento": "Citosol",
        "ecuacion": "D-Fructosa-6-Fosfato + ATP ➔ D-Fructosa-1,6-Bisfosfato + ADP + H⁺",
        "sustratos": ["D-Fructosa-6-Fosfato", "ATP"],
        "productos": ["D-Fructosa-1,6-Bisfosfato", "ADP", "H⁺"],
        "coproductos": "ADP (Gasto de 1 enlace de alta energía)",
        "deltaG": "ΔG°' = -14.2 kJ/mol (Irreversible · Principal marcapasos glucolítico)",
        "regulacion": "⊕ F-2,6-BP (el más potente), AMP, ADP | ⊖ ATP (alostérico), Citrato, H⁺ (acidosis láctica).",
        "relevancia": "Paso de compromiso definitivo: compromete el flujo de carbonos a degradación glucolítica."
    },
    "rx_aldo": {
        "enzima": "Aldolasa A / B (Fructosa-Bisfosfato Aldolasa)",
        "ec": "EC 4.1.2.13",
        "via": "Vía 1: Glucólisis",
        "compartimento": "Citosol",
        "ecuacion": "D-Fructosa-1,6-Bisfosfato ⇄ Dihidroxiacetona-Fosfato + D-Gliceraldehído-3-Fosfato",
        "sustratos": ["D-Fructosa-1,6-Bisfosfato"],
        "productos": ["Dihidroxiacetona-Fosfato (DHAP)", "D-Gliceraldehído-3-Fosfato (GAP)"],
        "coproductos": "Ninguno (Escisión aldólica 6C ⇄ 2 × 3C)",
        "deltaG": "ΔG°' = +23.8 kJ/mol (Fisiológicamente reversible por rápido consumo de triosas)",
        "regulacion": "Aldolasa B hepática escinde también Fructosa-1-P; su déficit causa Intolerancia Hereditaria a la Fructosa.",
        "relevancia": "Ruptura del esqueleto de hexosa en dos triosas fosforiladas interconvertibles."
    },
    "rx_tpi": {
        "enzima": "Triosa Fosfato Isomerasa (TPI / TIM)",
        "ec": "EC 5.3.1.1",
        "via": "Vía 1: Glucólisis",
        "compartimento": "Citosol",
        "ecuacion": "Dihidroxiacetona-Fosfato (DHAP) ⇄ D-Gliceraldehído-3-Fosfato (GAP)",
        "sustratos": ["Dihidroxiacetona-Fosfato"],
        "productos": ["D-Gliceraldehído-3-Fosfato"],
        "coproductos": "Ninguno (Isomerización de triosas)",
        "deltaG": "ΔG°' = +7.5 kJ/mol (Reversible ⇄ · Enzima cinéticamente perfecta)",
        "regulacion": "Impulsada por ley de acción de masas al retirarse el GAP en el siguiente paso.",
        "relevancia": "Permite que los dos fragmentos derivados de la glucosa continúen por una vía oxidativa unificada."
    },
    "rx_gapdh": {
        "enzima": "Gliceraldehído-3-Fosfato Deshidrogenasa (GAPDH)",
        "ec": "EC 1.2.1.12",
        "via": "Vía 1: Glucólisis",
        "compartimento": "Citosol",
        "ecuacion": "GAP + NAD⁺ + Pᵢ ⇄ 1,3-Bisfosfoglicerato + NADH + H⁺",
        "sustratos": ["D-Gliceraldehído-3-Fosfato", "NAD⁺", "Pᵢ"],
        "productos": ["1,3-Bisfosfoglicerato (1,3-BPG)", "NADH", "H⁺"],
        "coproductos": "NADH + H⁺ (Poder reductor citosólico)",
        "deltaG": "ΔG°' = +6.3 kJ/mol (Reversible · Formación de acil-fosfato de alta energía)",
        "regulacion": "Inhibida por yodoacetato y arseniato (compite con Pᵢ desacoplando síntesis de ATP).",
        "relevancia": "Único paso oxidativo de la glucólisis; conserva la energía redox en un enlace anhídrido mixto."
    },
    "rx_pgk": {
        "enzima": "Fosfoglicerato Quinasa (PGK)",
        "ec": "EC 2.7.2.3",
        "via": "Vía 1: Glucólisis",
        "compartimento": "Citosol",
        "ecuacion": "1,3-Bisfosfoglicerato + ADP ⇄ 3-Fosfoglicerato + ATP",
        "sustratos": ["1,3-Bisfosfoglicerato", "ADP"],
        "productos": ["3-Fosfoglicerato", "ATP"],
        "coproductos": "ATP (Fosforilación a nivel de sustrato 1)",
        "deltaG": "ΔG°' = -18.5 kJ/mol (Fisiológicamente reversible acoplada a GAPDH)",
        "regulacion": "Controlada por la relación [ATP]/[ADP] celular.",
        "relevancia": "Recupera la inversión de ATP de la fase preparatoria (2 ATP por glucosa)."
    },
    "rx_pgm": {
        "enzima": "Fosfoglicerato Mutasa (PGM)",
        "ec": "EC 5.4.2.11",
        "via": "Vía 1: Glucólisis",
        "compartimento": "Citosol",
        "ecuacion": "3-Fosfoglicerato ⇄ 2-Fosfoglicerato",
        "sustratos": ["3-Fosfoglicerato"],
        "productos": ["2-Fosfoglicerato"],
        "coproductos": "Intermediario catalítico: 2,3-Bisfosfoglicerato (2,3-BPG)",
        "deltaG": "ΔG°' = +4.4 kJ/mol (Reversible ⇄)",
        "regulacion": "Requiere trazas de 2,3-BPG para mantener fosforilada la histidina del sitio activo.",
        "relevancia": "Desplaza el grupo fosforilo a C2 para permitir la subsiguiente deshidratación enolítica."
    },
    "rx_eno": {
        "enzima": "Enolasa (Fosfopiruvato Hidratasa)",
        "ec": "EC 4.2.1.11",
        "via": "Vía 1: Glucólisis",
        "compartimento": "Citosol",
        "ecuacion": "2-Fosfoglicerato ⇄ Fosfoenolpiruvato (PEP) + H₂O",
        "sustratos": ["2-Fosfoglicerato"],
        "productos": ["Fosfoenolpiruvato (PEP)", "H₂O"],
        "coproductos": "H₂O (Deshidratación interna)",
        "deltaG": "ΔG°' = +7.5 kJ/mol (Reversible ⇄)",
        "regulacion": "Requiere Mg²⁺; inhibida fuertemente por Fluoruro (empleado en tubos de recogida para glucemia).",
        "relevancia": "Concentra la energía del éster fosfato atrapando la forma enol inestable (ΔG°' hidrólisis PEP = -61.9 kJ/mol)."
    },
    "rx_pk": {
        "enzima": "Piruvato Quinasa (PK)",
        "ec": "EC 2.7.1.40",
        "via": "Vía 1: Glucólisis",
        "compartimento": "Citosol",
        "ecuacion": "Fosfoenolpiruvato (PEP) + ADP + H⁺ ➔ Piruvato + ATP",
        "sustratos": ["Fosfoenolpiruvato (PEP)", "ADP", "H⁺"],
        "productos": ["Piruvato", "ATP"],
        "coproductos": "ATP (Fosforilación a nivel de sustrato 2)",
        "deltaG": "ΔG°' = -31.4 kJ/mol (Irreversible · Paso limitante 3)",
        "regulacion": "⊕ Fructosa-1,6-BP (feed-forward) | ⊖ ATP, Alanina, Acetil-CoA; PK-L hepática: fosforilada (PKA/glucagón) = inactiva.",
        "relevancia": "Genera el rendimiento neto de 2 ATP por glucosa y finaliza la glucólisis aeróbica/anaeróbica."
    },

    # =========================================================================
    # VÍA 2: GLUCONEOGÉNESIS (ENZIMAS ESPECÍFICAS DE DESVÍO)
    # =========================================================================
    "rx_gng_ldh": {
        "enzima": "Lactato Deshidrogenasa (LDH)",
        "ec": "EC 1.1.1.27",
        "via": "Vía 2 y 17: Gluconeogénesis / Ciclo de Cori",
        "compartimento": "Citosol",
        "ecuacion": "Lactato + NAD⁺ ⇄ Piruvato + NADH + H⁺",
        "sustratos": ["Lactato", "NAD⁺"],
        "productos": ["Piruvato", "NADH", "H⁺"],
        "coproductos": "NADH + H⁺ (En hígado hacia GNG) / NAD⁺ (En músculo en anaerobiosis)",
        "deltaG": "ΔG°' = -25.1 kJ/mol (en sentido piruvato ➔ lactato en músculo)",
        "regulacion": "Isoenzimas M₄ (músculo, afinidad por piruvato) y H₄ (corazón/hígado, inhibida por exceso de piruvato).",
        "relevancia": "Conecta el lactato del eritrocito y músculo con la gluconeogénesis hepática (Ciclo de Cori)."
    },
    "rx_gng_glicerol_cinasa": {
        "enzima": "Glicerol Quinasa (GK)",
        "ec": "EC 2.7.1.30",
        "via": "Vía 2: Gluconeogénesis",
        "compartimento": "Citosol (Exclusiva del Hígado y Riñón)",
        "ecuacion": "Glicerol + ATP ➔ L-Glicerol-3-Fosfato + ADP + H⁺",
        "sustratos": ["Glicerol", "ATP"],
        "productos": ["L-Glicerol-3-Fosfato", "ADP", "H⁺"],
        "coproductos": "ADP (Gasto de 1 ATP)",
        "deltaG": "ΔG°' = -20.8 kJ/mol (Irreversible)",
        "regulacion": "Ausente en adipocitos, obligando al glicerol de la lipólisis a viajar por sangre al hígado.",
        "relevancia": "Permite canalizar el esqueleto hidrocarbonado de los triglicéridos hacia glucosa."
    },
    "rx_gng_g3pdh": {
        "enzima": "Glicerol-3-Fosfato Deshidrogenasa Citosólica (cGPDH / GPD1)",
        "ec": "EC 1.1.1.8",
        "via": "Vía 2 y 8B: Gluconeogénesis / Lanzadera G3P",
        "compartimento": "Citosol",
        "ecuacion": "L-Glicerol-3-Fosfato + NAD⁺ ⇄ Dihidroxiacetona-Fosfato + NADH + H⁺",
        "sustratos": ["L-Glicerol-3-Fosfato", "NAD⁺"],
        "productos": ["Dihidroxiacetona-Fosfato (DHAP)", "NADH", "H⁺"],
        "coproductos": "NADH + H⁺",
        "deltaG": "ΔG°' = -1.9 kJ/mol (Reversible ⇄)",
        "regulacion": "Equilibrio dependiente de la relación [NAD⁺]/[NADH] citosólica.",
        "relevancia": "Entrada directa del glicerol a la fase de triosas de la gluconeogénesis a nivel de DHAP."
    },

    # =========================================================================
    # VÍA 3: METABOLISMO DEL GLUCÓGENO
    # =========================================================================
    "rx_pgm_glucogeno": {
        "enzima": "Fosfoglucomutasa (PGM-1)",
        "ec": "EC 5.4.2.2",
        "via": "Vía 3: Glucógeno",
        "compartimento": "Citosol",
        "ecuacion": "Glucosa-6-Fosfato ⇄ Glucosa-1-Fosfato",
        "sustratos": ["Glucosa-6-Fosfato"],
        "productos": ["Glucosa-1-Fosfato"],
        "coproductos": "Intermediario catalítico: Glucosa-1,6-Bisfosfato",
        "deltaG": "ΔG°' = +7.1 kJ/mol (Reversible ⇄)",
        "regulacion": "Controlada por la demanda metabólica y concentraciones relativas de G6P y G1P.",
        "relevancia": "Puente bidireccional entre la glucólisis/gluconeogénesis y el pool de glucógeno."
    },
    "rx_udpg": {
        "enzima": "UDP-Glucosa Pirofosforilasa",
        "ec": "EC 2.7.7.9",
        "via": "Vía 3: Glucogenogénesis",
        "compartimento": "Citosol",
        "ecuacion": "Glucosa-1-Fosfato + UTP ⇄ UDP-Glucosa + PPᵢ (➔ 2 Pᵢ por pirofosfatasa)",
        "sustratos": ["Glucosa-1-Fosfato", "UTP"],
        "productos": ["UDP-Glucosa", "Pirofosfato inorgánico (PPᵢ)"],
        "coproductos": "PPᵢ rápidamente hidrolizado a 2 Pᵢ (fuerza impulsora termodinámica)",
        "deltaG": "ΔG°' global = -19.2 kJ/mol (con hidrólisis de PPᵢ)",
        "regulacion": "Impulsada irreversiblemente hacia adelante por la pirofosfatasa inorgánica.",
        "relevancia": "Activa la glucosa como nucleótido-azúcar donor para la síntesis de glucógeno y galactosa."
    },
    "rx_sintesis_degradacion_glucogeno": {
        "enzima": "Glucógeno Sintasa (GS) / Glucógeno Fosforilasa (GP)",
        "ec": "EC 2.4.1.11 / EC 2.4.1.1",
        "via": "Vía 3: Glucógeno",
        "compartimento": "Citosol",
        "ecuacion": "UDP-Glucosa + Glucógeno(n) ➔ Glucógeno(n+1) + UDP  |  Glucógeno(n) + Pᵢ ➔ Glucosa-1-P + Glucógeno(n-1)",
        "sustratos": ["UDP-Glucosa / Glucógeno(n) + Pᵢ"],
        "productos": ["Glucógeno(n+1) + UDP / Glucosa-1-Fosfato"],
        "coproductos": "UDP (Síntesis) / Pᵢ (Fosforólisis sin gasto de ATP)",
        "deltaG": "Ambas reacciones son termodinámicamente exergónicas en sus condiciones fisiológicas respectivas",
        "regulacion": "Regulación covalente recíproca coordinada por PKA, Fosforilasa Quinasa, PP1 y GSK-3 (Insulina activa GS; Glucagón/Adrenalina activan GP).",
        "relevancia": "Mantenimiento homeostático estricto de la glucemia plasmática (hígado) y reserva para el trabajo contráctil (músculo)."
    },

    # =========================================================================
    # VÍA 4: VÍA DE LAS PENTOSAS FOSFATO (SHUNT DE LAS HEXOSAS MONOFOSFATO)
    # =========================================================================
    "rx_g6pdh": {
        "enzima": "Glucosa-6-Fosfato Deshidrogenasa (G6PDH)",
        "ec": "EC 1.1.1.49",
        "via": "Vía 4: Pentosas Fosfato",
        "compartimento": "Citosol",
        "ecuacion": "D-Glucosa-6-Fosfato + NADP⁺ ➔ 6-Fosfoglucono-δ-Lactona + NADPH + H⁺",
        "sustratos": ["D-Glucosa-6-Fosfato", "NADP⁺"],
        "productos": ["6-Fosfoglucono-δ-Lactona", "NADPH", "H⁺"],
        "coproductos": "NADPH + H⁺ (1.er equivalente reductor)",
        "deltaG": "ΔG°' = -17.6 kJ/mol (Irreversible · Marcapasos de la vía)",
        "regulacion": "Control alostérico estricto por relación [NADPH]/[NADP⁺]; fuertemente inhibida por NADPH.",
        "relevancia": "Principal fuente celular de NADPH para defensas antioxidantes (glutatión reducido) y lipogénesis. Su déficit causa favismo/anemia hemolítica."
    },
    "rx_lactonasa": {
        "enzima": "6-Fosfogluconolactonasa",
        "ec": "EC 3.1.1.31",
        "via": "Vía 4: Pentosas Fosfato",
        "compartimento": "Citosol",
        "ecuacion": "6-Fosfoglucono-δ-Lactona + H₂O ➔ 6-Fosfogluconato + H⁺",
        "sustratos": ["6-Fosfoglucono-δ-Lactona", "H₂O"],
        "productos": ["6-Fosfogluconato", "H⁺"],
        "coproductos": "H₂O (Apertura hidrolítica del anillo lactona)",
        "deltaG": "ΔG°' = -21.0 kJ/mol (Irreversible)",
        "regulacion": "Actividad constitutiva rápida para prevenir acumulación espontánea de la lactona.",
        "relevancia": "Convierte la lactona cíclica en el sustrato lineal con carboxilato para la siguiente descarboxilación."
    },
    "rx_6pgdh": {
        "enzima": "6-Fosfogluconato Deshidrogenasa (6PGDH)",
        "ec": "EC 1.1.1.44",
        "via": "Vía 4: Pentosas Fosfato",
        "compartimento": "Citosol",
        "ecuacion": "6-Fosfogluconato + NADP⁺ ➔ D-Ribulosa-5-Fosfato + NADPH + CO₂",
        "sustratos": ["6-Fosfogluconato", "NADP⁺"],
        "productos": ["D-Ribulosa-5-Fosfato", "NADPH", "CO₂"],
        "coproductos": "NADPH + H⁺ + CO₂ (Descarboxilación oxidativa)",
        "deltaG": "ΔG°' = -1.9 kJ/mol (Fisiológicamente irreversible por escape de CO₂)",
        "regulacion": "Inhibida por NADPH.",
        "relevancia": "Genera el segundo NADPH y sintetiza la primera pentosa cetosa precursora de nucleótidos."
    },
    "rx_tk1_pnt": {
        "enzima": "Transcetolasa (Paso 1 · TPP dependiente)",
        "ec": "EC 2.2.1.1",
        "via": "Vía 4: Pentosas Fosfato",
        "compartimento": "Citosol",
        "ecuacion": "Xilulosa-5-P + Ribosa-5-P ⇄ Sedoheptulosa-7-P + Gliceraldehído-3-P",
        "sustratos": ["Xilulosa-5-P (5C)", "Ribosa-5-P (5C)"],
        "productos": ["Sedoheptulosa-7-P (7C)", "Gliceraldehído-3-P (3C)"],
        "coproductos": "Cofactor: Pirofosfato de Tiamina (TPP) y Mg²⁺ (Transfiere unidad de 2C)",
        "deltaG": "ΔG°' = +0.5 kJ/mol (Reversible ⇄)",
        "regulacion": "Controlada por disponibilidad de sustratos. Marcador clínico de deficiencia de tiamina (Vitamina B₁).",
        "relevancia": "Conecta el exceso de pentosas con intermediarios de la glucólisis."
    },
    "rx_ta_pnt": {
        "enzima": "Transaldolasa",
        "ec": "EC 2.2.1.2",
        "via": "Vía 4: Pentosas Fosfato",
        "compartimento": "Citosol",
        "ecuacion": "Sedoheptulosa-7-P + Gliceraldehído-3-P ⇄ Fructosa-6-P + Eritrosa-4-P",
        "sustratos": ["Sedoheptulosa-7-P (7C)", "Gliceraldehído-3-P (3C)"],
        "productos": ["Fructosa-6-P (6C)", "Eritrosa-4-P (4C)"],
        "coproductos": "Intermediario base de Schiff con lisina (Transfiere unidad de 3C dihidroxiacetona)",
        "deltaG": "ΔG°' = -1.0 kJ/mol (Reversible ⇄)",
        "regulacion": "Equilibrio dependiente del pool de intermediarios glucolíticos y eritrosa.",
        "relevancia": "Genera Eritrosa-4-P (precursora de aminoácidos aromáticos) y reinyecta Fructosa-6-P a la glucólisis."
    },

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
        "coproductos": "5 coenzimas: TPP (E1), Lipoamida (E2), CoA (E2), FAD (E3), NAD⁺ (E3)",
        "deltaG": "ΔG°' = -33.4 kJ/mol (Completamente irreversible en animales)",
        "regulacion": "Alostérica: ⊖ Acetil-CoA, NADH, ATP | ⊕ ADP, Piruvato, Ca²⁺, NAD⁺, CoA. Covalente: PDK fosforila E1 = inactiva; PDP (insulina, Ca²⁺) = activa.",
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
        "regulacion": "Dependiente de la disponibilidad de CoA en la matriz.",
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

    # =========================================================================
    # VÍA 18: DIGESTIÓN Y ABSORCIÓN DE LÍPIDOS
    # =========================================================================
    "rx_lipasa_pancreatica": {
        "enzima": "Lipasa Pancreática & Colipasa",
        "ec": "EC 3.1.1.3",
        "via": "Vía 18: Digestión de Lípidos",
        "compartimento": "Luz Intestinal (Duodeno/Yeyuno)",
        "ecuacion": "Triglicérido (TAG) + 2 H₂O ➔ 2-Monoacilglicerol (2-MAG) + 2 Ácidos Grasos Libres",
        "sustratos": ["Triglicéridos dietéticos", "Sales biliares (emulsión)"],
        "productos": ["2-Monoacilglicerol", "2 Ácidos Grasos libres"],
        "coproductos": "Micelas mixtas biliares",
        "deltaG": "Irreversible",
        "regulacion": "Activada por Colipasa (secreción pancreática); inhibida farmacológicamente por Orlistat (anti-obesidad).",
        "relevancia": "Permite la absorción entérica de las grasas hidrolizando selectivamente las posiciones sn-1 y sn-3 de los TAG."
    },

    # =========================================================================
    # VÍA 19: TEJIDO ADIPOSO (LIPÓLISIS SECUENCIAL)
    # =========================================================================
    "rx_atgl": {
        "enzima": "Adiposo Triglicérido Lipasa (ATGL / PNPLA2)",
        "ec": "EC 3.1.1.3",
        "via": "Vía 19: Lipólisis Adiposa",
        "compartimento": "Gota Lipídica / Citosol del Adipocito",
        "ecuacion": "Triglicérido (TAG) + H₂O ➔ Diacilglicerol (DAG) + 1.er Ácido Graso Libre",
        "sustratos": ["TAG de la gota lipídica", "H₂O"],
        "productos": ["Diacilglicerol (DAG)", "Ácido Graso Libre (R₁-COO⁻)"],
        "coproductos": "1.er AG libre hacia pool de transporte plasmático",
        "deltaG": "Irreversible · Paso iniciador de la lipólisis",
        "regulacion": "Activada por coactivador ABHD5 (CGI-58) liberado de la Perilipina-1 al ser fosforilada por PKA; inhibida por G0S2 e insulina.",
        "relevancia": "Iniciador fisiológico indispensable de la movilización de reservas energéticas en ayuno."
    },
    "rx_hsl": {
        "enzima": "Lipasa Sensible a Hormonas (HSL / LIPE)",
        "ec": "EC 3.1.1.79",
        "via": "Vía 19: Lipólisis Adiposa",
        "compartimento": "Citosol ➔ Gota Lipídica del Adipocito",
        "ecuacion": "Diacilglicerol (DAG) + H₂O ➔ 2-Monoacilglicerol (2-MAG) + 2.º Ácido Graso Libre",
        "sustratos": ["Diacilglicerol (DAG)", "H₂O"],
        "productos": ["2-Monoacilglicerol (2-MAG)", "Ácido Graso Libre (R₂-COO⁻)"],
        "coproductos": "2.º AG libre hacia pool de transporte",
        "deltaG": "Irreversible",
        "regulacion": "⊕ Fosforilación directa por PKA (Glucagón, Adrenalina vía AMPc) ➔ trasloca del citosol a la superficie de la gota lipídica | ⊖ Insulina (activa fosfodiesterasa PDE3B y PP1/PP2A).",
        "relevancia": "Principal enzima regulada hormonalmente en la movilización de grasas."
    },
    "rx_mgl": {
        "enzima": "Monoacilglicerol Lipasa (MGL / MGLL)",
        "ec": "EC 3.1.1.23",
        "via": "Vía 19: Lipólisis Adiposa",
        "compartimento": "Citosol del Adipocito",
        "ecuacion": "2-Monoacilglicerol (2-MAG) + H₂O ➔ Glicerol Libre + 3.er Ácido Graso Libre",
        "sustratos": ["2-Monoacilglicerol", "H₂O"],
        "productos": ["Glicerol Libre", "Ácido Graso Libre (R₃-COO⁻)"],
        "coproductos": "Glicerol (excreción vía AQP7) + 3.er AG libre (vía CD36/FATP + Albúmina)",
        "deltaG": "Irreversible",
        "regulacion": "Actividad basal constitutiva elevada (no regulada por hormonas; el flujo depende de HSL).",
        "relevancia": "Completa la degradación del triglicérido rindiendo 3 ácidos grasos y glicerol libre."
    },

    # =========================================================================
    # VÍA 22: LIPOPROTEÍNAS PLASMÁTICAS
    # =========================================================================
    "rx_lpl_lh": {
        "enzima": "Lipoproteína Lipasa (LPL) / Lipasa Hepática (LH)",
        "ec": "EC 3.1.1.34",
        "via": "Vía 22: Lipoproteínas Plasmáticas",
        "compartimento": "Endotelio Capilar Luminal (Adiposo, Músculo) / Sinusoides Hepáticos",
        "ecuacion": "TAG de Quilomicrones / VLDL + H₂O ➔ Ácidos Grasos Libres + Glicerol + Remanentes (IDL/LDL)",
        "sustratos": ["Triglicéridos de VLDL / Quilomicrón", "ApoC-II (activador)"],
        "productos": ["Ácidos Grasos para captación tisular", "Glicerol", "Remanentes / IDL"],
        "coproductos": "ApoC-II actúa como cofactor proteico obligado",
        "deltaG": "Irreversible",
        "regulacion": "LPL en adipocito inducida por insulina en estado posprandial; en músculo cardíaco tiene baja Km (alta afinidad) para actuar en ayuno.",
        "relevancia": "Descarga los triglicéridos transportados por la sangre hacia los tejidos consumidores y de reserva."
    },
    "rx_ldlr_endocitosis": {
        "enzima": "Receptor de LDL (LDLR) · Endocitosis Mediada por Receptor",
        "ec": "Proteína de Membrana",
        "via": "Vía 22: Captación de Colesterol",
        "compartimento": "Fositas recubiertas de clatrina (Hepatocito / Células periféricas)",
        "ecuacion": "LDL (ApoB-100) + LDLR ➔ Complejo Endocitado ➔ Lisosoma (Colesterol libre + Aminoácidos) + Reciclaje de LDLR",
        "sustratos": ["Partícula LDL circulante", "Receptor LDLR"],
        "productos": ["Colesterol libre intracelular", "Aminoácidos (ApoB degradada)"],
        "coproductos": "El colesterol intracelular reprime HMGCR y LDLR, y activa ACAT",
        "deltaG": "Endocitosis dependiente de energía",
        "regulacion": "Inducida por SREBP-2; degradada lisosómicamente por PCSK9 (diana de anticuerpos monoclonales como Evolocumab).",
        "relevancia": "Principal mecanismo de depuración de colesterol LDL aterogénico del plasma."
    },

    # =========================================================================
    # VÍA 23: BIOSÍNTESIS DE TAG Y FOSFOLÍPIDOS (VÍA DE KENNEDY)
    # =========================================================================
    "rx_gpat": {
        "enzima": "Glicerol-3-Fosfato Aciltransferasa (GPAT)",
        "ec": "EC 2.3.1.15",
        "via": "Vía 23: Vía de Kennedy",
        "compartimento": "Membrana Mitocondrial Externa / Retículo Endoplásmico",
        "ecuacion": "Glicerol-3-Fosfato + Acil-CoA ➔ Ácido Lisofosfatídico (LPA) + CoA-SH",
        "sustratos": ["Glicerol-3-Fosfato", "Acil-CoA (Palmitoil-CoA)"],
        "productos": ["Ácido Lisofosfatídico (1-Acil-G3P / LPA)", "CoA-SH"],
        "coproductos": "CoA-SH",
        "deltaG": "Irreversible · Paso limitante de la vía de Kennedy",
        "regulacion": "Inducida fuertemente por insulina (SREBP-1c); activada en estado posprandial.",
        "relevancia": "Incorpora el primer ácido graso en la posición sn-1 para construir lípidos neutros y estructurales."
    },
    "rx_agpat": {
        "enzima": "1-Acilglicerol-3-Fosfato Aciltransferasa (AGPAT)",
        "ec": "EC 2.3.1.51",
        "via": "Vía 23: Vía de Kennedy",
        "compartimento": "Retículo Endoplásmico",
        "ecuacion": "Ácido Lisofosfatídico (LPA) + Acil-CoA (Oleil-CoA) ➔ Ácido Fosfatídico (PA) + CoA-SH",
        "sustratos": ["LPA", "Acil-CoA insaturado"],
        "productos": ["Ácido Fosfatídico (PA)", "CoA-SH"],
        "coproductos": "CoA-SH",
        "deltaG": "Irreversible",
        "regulacion": "Prefiere ácidos grasos mono/poliinsaturados para la posición sn-2.",
        "relevancia": "Sintetiza Ácido Fosfatídico, encrucijada entre triglicéridos y fosfolípidos de membrana."
    },
    "rx_pap": {
        "enzima": "Fosfatidato Fosfatasa (PAP / Lipina-1)",
        "ec": "EC 3.1.3.4",
        "via": "Vía 23: Vía de Kennedy",
        "compartimento": "Citosol / Retículo Endoplásmico",
        "ecuacion": "Ácido Fosfatídico (PA) + H₂O ➔ 1,2-Diacilglicerol (DAG) + Pᵢ",
        "sustratos": ["Ácido Fosfatídico (PA)", "H₂O"],
        "productos": ["1,2-Diacilglicerol (DAG)", "Fosfato inorgánico (Pᵢ)"],
        "coproductos": "Pᵢ libre",
        "deltaG": "Irreversible",
        "regulacion": "La Lipina-1 actúa como enzima en RE y como coactivador transcripcional en núcleo.",
        "relevancia": "Bifurcación: el DAG generado puede ser acilado a TAG o reaccionar con CDP-colina para fosfatidilcolina."
    },

    # =========================================================================
    # VÍA 24: BIOSÍNTESIS DE AMINOÁCIDOS NO ESENCIALES
    # =========================================================================
    "rx_alt_amino": {
        "enzima": "Alanina Aminotransferasa (ALT / GPT)",
        "ec": "EC 2.6.1.2",
        "via": "Vía 24: Biosíntesis de Alanina",
        "compartimento": "Citosol",
        "ecuacion": "Piruvato + L-Glutamato ⇄ L-Alanina + α-Cetoglutarato",
        "sustratos": ["Piruvato (3C)", "L-Glutamato"],
        "productos": ["L-Alanina", "α-Cetoglutarato"],
        "coproductos": "Cofactor: Fosfato de Piridoxal (PLP / Vitamina B₆)",
        "deltaG": "ΔG°' ≈ 0 kJ/mol (Reversible ⇄)",
        "regulacion": "Marcador hepático clásico en plasma (transaminasa citosólica).",
        "relevancia": "Síntesis directa de Alanina a partir de intermediarios de la glucólisis y acoplamiento con Ciclo de Cahill."
    },
    "rx_ast_amino": {
        "enzima": "Aspartato Aminotransferasa (AST / GOT)",
        "ec": "EC 2.6.1.1",
        "via": "Vía 24: Biosíntesis de Aspartato",
        "compartimento": "Citosol / Matriz Mitocondrial",
        "ecuacion": "Oxalacetato + L-Glutamato ⇄ L-Aspartato + α-Cetoglutarato",
        "sustratos": ["Oxalacetato (4C)", "L-Glutamato"],
        "productos": ["L-Aspartato", "α-Cetoglutarato"],
        "coproductos": "Cofactor: Fosfato de Piridoxal (PLP)",
        "deltaG": "ΔG°' ≈ 0 kJ/mol (Reversible ⇄)",
        "regulacion": "Isoformas citosólica (GOT1) y mitocondrial (GOT2) clave en la lanzadera malato-aspartato.",
        "relevancia": "Sintetiza Aspartato, donador de nitrógeno para el ciclo de la urea y síntesis de nucleótidos purínicos/pirimidínicos."
    },
    "rx_gln_sintetasa": {
        "enzima": "Glutamina Sintetasa (GS)",
        "ec": "EC 6.3.1.2",
        "via": "Vía 24: Biosíntesis de Glutamina",
        "compartimento": "Citosol",
        "ecuacion": "L-Glutamato + NH₄⁺ + ATP ➔ L-Glutamina + ADP + Pᵢ",
        "sustratos": ["L-Glutamato", "Ion Amonio (NH₄⁺)", "ATP"],
        "productos": ["L-Glutamina", "ADP", "Pᵢ"],
        "coproductos": "ADP + Pᵢ (Gasto de 1 ATP)",
        "deltaG": "Irreversible",
        "regulacion": "Expresada preferentemente en astrocitos cerebrales y hepatocitos perivenosos.",
        "relevancia": "Detoxificación fundamental de amonio en cerebro y síntesis del transportador no tóxico de nitrógeno más abundante en sangre."
    },
    "rx_gdh_amino": {
        "enzima": "Glutamato Deshidrogenasa (GDH)",
        "ec": "EC 1.4.1.2 / EC 1.4.1.3",
        "via": "Vía 13 y 24: Desaminación / Síntesis de Glutamato",
        "compartimento": "Matriz Mitocondrial",
        "ecuacion": "α-Cetoglutarato + NH₄⁺ + NADPH + H⁺ ⇄ L-Glutamato + NADP⁺ + H₂O",
        "sustratos": ["α-Cetoglutarato", "NH₄⁺", "NADPH"],
        "productos": ["L-Glutamato", "NADP⁺", "H₂O"],
        "coproductos": "NADP⁺ (Síntesis con NADPH) / NADH (Desaminación con NAD⁺)",
        "deltaG": "Reversible ⇄",
        "regulacion": "⊕ ADP, Leucina | ⊖ GTP, ATP, NADH (señal de alta carga energética).",
        "relevancia": "Enlace central entre el metabolismo de los aminoácidos y el ciclo de Krebs."
    }
}
