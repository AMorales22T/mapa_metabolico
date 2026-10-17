# =============================================================================
# MÓDULO DE REVISIÓN: Estequiometría de Carbohidratos (Vías 1, 2, 3 y 4)
# =============================================================================
# Archivo original : 06_REGULACION_Y_LEYENDA/reacciones_estequiometria.py (líneas 1 a 304 de 988)
# Descripción      : Ecuaciones balanceadas, números EC, ΔG°' y cofactores de Glucólisis, Gluconeogénesis, Glucógeno y Pentosas.
# =============================================================================

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

