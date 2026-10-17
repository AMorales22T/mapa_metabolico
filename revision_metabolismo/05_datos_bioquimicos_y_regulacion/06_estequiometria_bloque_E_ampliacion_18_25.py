# =============================================================================
# MÓDULO DE REVISIÓN: Estequiometría de la Ampliación (Vías 18 a 24)
# =============================================================================
# Archivo original : 06_REGULACION_Y_LEYENDA/reacciones_estequiometria.py (líneas 800 a 988 de 988)
# Descripción      : Ecuaciones de Digestión Lipídica, Lipólisis Adiposa (ATGL/HSL/MGL), Lipoproteínas, Vía de Kennedy y Síntesis de AA.
# =============================================================================

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
