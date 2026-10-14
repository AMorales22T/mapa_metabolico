#!/usr/bin/env python3
"""
FUENTE ÚNICA DE DATOS: REGULACIÓN ENZIMÁTICA Y LEYENDA DE VÍAS
================================================================
Este archivo lo leen:
  - generar_prueba_visual_integrada.py  -> dibuja las etiquetas ⊕ / ⊖ / P en el mapa.
  - generar_documentos.py               -> escribe REGULACION_ENZIMATICA.md y LEYENDA_VIAS.md.

Así el mapa y los documentos nunca se contradicen: si cambias algo aquí,
regenera ambos.

Campos de cada enzima:
  id          identificador interno (lo usa el generador para colocar la etiqueta)
  via         número de vía (ver VIAS)
  enzima      nombre
  ec          número EC
  activadores lista de efectores alostéricos positivos (⊕)
  inhibidores lista de efectores alostéricos negativos (⊖)
  covalente   texto corto de modificación covalente (fosforilación) o "" si no tiene
  hormonal    control hormonal / transcripcional resumido ("" si no aplica)
  mapa_cov    versión muy corta de 'covalente' para el mapa (cabe en una línea)
  mapa_hor    versión muy corta de 'hormonal' para el mapa (cabe en una línea)
"""

# ---------------------------------------------------------------------------
# VÍAS METABÓLICAS INCLUIDAS EN EL TRABAJO (leyenda numerada)
# ---------------------------------------------------------------------------
VIAS = [
    {"n": 1,  "nombre": "Glucólisis",                              "lugar": "Citosol",              "resumen": "Glucosa → 2 Piruvato (+2 ATP, +2 NADH)"},
    {"n": 2,  "nombre": "Gluconeogénesis",                         "lugar": "Matriz + citosol + RE", "resumen": "Piruvato → Glucosa (4 enzimas específicas) · hepática"},
    {"n": 3,  "nombre": "Glucogenogénesis y glucogenólisis",       "lugar": "Citosol",              "resumen": "Síntesis y degradación del glucógeno"},
    {"n": 4,  "nombre": "Vía de las pentosas fosfato",             "lugar": "Citosol",              "resumen": "G6P → NADPH + Ribosa-5-P (fase oxidativa y no oxidativa)"},
    {"n": 5,  "nombre": "Complejo piruvato deshidrogenasa (PDH)",  "lugar": "Matriz",               "resumen": "Piruvato → Acetil-CoA + CO₂ + NADH"},
    {"n": 6,  "nombre": "Ciclo de Krebs",                          "lugar": "Matriz",               "resumen": "Acetil-CoA → 2 CO₂ + 3 NADH + FADH₂ + GTP"},
    {"n": 7,  "nombre": "Cadena de transporte de electrones y ATP sintasa", "lugar": "Membrana mitocondrial interna", "resumen": "Fosforilación oxidativa (acoplamiento quimiosmótico)"},
    {"n": 8,  "nombre": "Lanzaderas (malato-aspartato, glicerol-P)", "lugar": "MME / EIM / MMI",     "resumen": "Transporte de equivalentes redox (NADH citosólico) y Acetil-CoA"},
    {"n": 9,  "nombre": "β-oxidación (y lanzadera de carnitina)",  "lugar": "Citosol → Matriz",     "resumen": "Palmitoil-CoA → 8 Acetil-CoA + FADH₂ + NADH"},
    {"n": 10, "nombre": "Lipogénesis (síntesis de ácidos grasos)", "lugar": "Citosol",              "resumen": "Acetil-CoA → Malonil-CoA → Palmitato (FAS)"},
    {"n": 11, "nombre": "Cetogénesis",                             "lugar": "Matriz · hepática",    "resumen": "Acetil-CoA → Acetoacetato / β-Hidroxibutirato"},
    {"n": 12, "nombre": "Síntesis de colesterol",                  "lugar": "Citosol + RE",         "resumen": "Acetil-CoA → HMG-CoA → Mevalonato → Colesterol"},
    {"n": "12B", "nombre": "Destinos esqueletos carbonados AA",    "lugar": "Citosol + Matriz",     "resumen": "Convergencia de los 20 AA en Krebs, Piruvato y Cuerpos Cetónicos"},
    {"n": 13, "nombre": "Transaminación y desaminación oxidativa", "lugar": "Citosol + Matriz",     "resumen": "Recogida del grupo amino en Glutamato → NH₄⁺"},
    {"n": 14, "nombre": "Ciclo de la urea",                        "lugar": "Matriz + citosol · hepático", "resumen": "NH₄⁺ + HCO₃⁻ + Aspartato → Urea"},
    {"n": 15, "nombre": "Biosíntesis de nucleótidos (purinas y pirimidinas)", "lugar": "Citosol + MMI", "resumen": "Rutas de novo convergentes sobre PRPP y vías de salvamento (HGPRT/APRT)"},
    {"n": 16, "nombre": "Catabolismo de nucleótidos y ácido úrico", "lugar": "Citosol + túbulo renal", "resumen": "Degradación de purinas a Ácido Úrico (XOD/Alopurinol) y pirimidinas a β-Alanina"},
    {"n": 17, "nombre": "Ciclo de Cori (acoplamiento músculo-hígado)", "lugar": "Músculo ⇄ Sangre ⇄ Hígado", "resumen": "Lactato muscular anaeróbico → Sangre → Glucosa hepática (GNG) → Músculo (-4 ATP neto)"},
]

# ---------------------------------------------------------------------------
# CLAVE DE SÍMBOLOS (leyenda)
# ---------------------------------------------------------------------------
SIMBOLOS = [
    ("(+)", "Activador alostérico (efector positivo)"),
    ("(-)", "Inhibidor alostérico (efector negativo / retroinhibición)"),
    ("(P)", "Modificación covalente por fosforilación (forma activa)"),
    ("⇄", "Reacción reversible (doble flecha)"),
    ("→", "Reacción irreversible (flecha simple, punto de control)"),
    ("- - →", "Conexión entre vías / transporte entre compartimentos"),
    ("▭", "Transportador de membrana (GLUT, MPC, CACT, AGC…)"),
    ("[nC]", "Número de átomos de carbono del metabolito"),
]

# ---------------------------------------------------------------------------
# ENZIMAS REGULADAS
# ---------------------------------------------------------------------------
ENZIMAS = [
    # ---------------- 1. GLUCÓLISIS ----------------
    {"id": "hk", "via": 1, "enzima": "Hexoquinasa (I–III)", "ec": "2.7.1.1",
     "activadores": [], "inhibidores": ["Glucosa-6-P"],
     "covalente": "",
     "hormonal": "En hígado actúa la Glucoquinasa (HK IV): no inhibida por G6P; secuestrada en el núcleo por GKRP (⊖ F6P); inducida por insulina",
     "mapa_cov": "", "mapa_hor": "Hígado: Glucoquinasa (GKRP)"},
    {"id": "pfk1", "via": 1, "enzima": "Fosfofructoquinasa-1 (PFK-1)", "ec": "2.7.1.11",
     "activadores": ["AMP", "ADP", "Fructosa-2,6-BP"], "inhibidores": ["ATP", "Citrato", "H⁺"],
     "covalente": "",
     "hormonal": "Indirecto vía Fructosa-2,6-BP (PFK-2): insulina ↑, glucagón ↓",
     "mapa_cov": "", "mapa_hor": "Principal punto de control"},
    {"id": "pk", "via": 1, "enzima": "Piruvato quinasa", "ec": "2.7.1.40",
     "activadores": ["Fructosa-1,6-BP"], "inhibidores": ["ATP", "Alanina", "Acetil-CoA"],
     "covalente": "Isoforma L (hígado): fosforilada por PKA = INACTIVA; desfosforilada = activa",
     "hormonal": "Glucagón la inactiva (PKA); insulina la activa (fosfatasa)",
     "mapa_cov": "P = inactiva (PKA, hígado)", "mapa_hor": "Glucagón ↓ · Insulina ↑"},

    # ---------------- 2. GLUCONEOGÉNESIS ----------------
    {"id": "pc", "via": 2, "enzima": "Piruvato carboxilasa", "ec": "6.4.1.1",
     "activadores": ["Acetil-CoA (obligado)"], "inhibidores": ["ADP"],
     "covalente": "",
     "hormonal": "Glucagón y cortisol inducen su síntesis",
     "mapa_cov": "", "mapa_hor": "Biotina · mitocondrial"},
    {"id": "pepck", "via": 2, "enzima": "PEP carboxiquinasa (PEPCK)", "ec": "4.1.1.32",
     "activadores": [], "inhibidores": [],
     "covalente": "",
     "hormonal": "Control transcripcional: glucagón (AMPc) y cortisol inducen; insulina reprime",
     "mapa_cov": "", "mapa_hor": "Glucagón/cortisol ↑ · Insulina ↓ (gen)"},
    {"id": "fbpasa1", "via": 2, "enzima": "Fructosa-1,6-bisfosfatasa (FBPasa-1)", "ec": "3.1.3.11",
     "activadores": ["Citrato"], "inhibidores": ["AMP", "Fructosa-2,6-BP"],
     "covalente": "",
     "hormonal": "Indirecto vía Fructosa-2,6-BP: glucagón ↑ actividad, insulina ↓",
     "mapa_cov": "", "mapa_hor": "Recíproca a PFK-1"},
    {"id": "g6pasa", "via": 2, "enzima": "Glucosa-6-fosfatasa", "ec": "3.1.3.9",
     "activadores": [], "inhibidores": [],
     "covalente": "",
     "hormonal": "Control transcripcional: glucagón y glucocorticoides inducen; insulina reprime. Luz del RE (hígado y riñón)",
     "mapa_cov": "", "mapa_hor": "Glucagón ↑ · Insulina ↓ (gen) · RE"},
    {"id": "pfk2", "via": 2, "enzima": "PFK-2 / FBPasa-2 (bifuncional)", "ec": "2.7.1.105 / 3.1.3.46",
     "activadores": ["Fructosa-6-P (⊕ PFK-2)"], "inhibidores": ["Citrato (⊖ PFK-2)"],
     "covalente": "Hígado: fosforilada por PKA → FBPasa-2 activa / PFK-2 inactiva (↓ F-2,6-BP). Desfosforilada (PP2A) → PFK-2 activa (↑ F-2,6-BP)",
     "hormonal": "Glucagón → PKA → ↓ F-2,6-BP → gluconeogénesis. Insulina → fosfatasa → ↑ F-2,6-BP → glucólisis",
     "mapa_cov": "P (PKA) = FBPasa-2 activa", "mapa_hor": "Glucagón ↓F-2,6-BP · Insulina ↑"},

    # ---------------- 3. GLUCÓGENO ----------------
    {"id": "gs", "via": 3, "enzima": "Glucógeno sintasa", "ec": "2.4.1.11",
     "activadores": ["Glucosa-6-P"], "inhibidores": [],
     "covalente": "Fosforilada (GSK-3, PKA) = INACTIVA (forma b); desfosforilada por PP1 = activa (forma a)",
     "hormonal": "Insulina la activa (inhibe GSK-3, activa PP1); glucagón y adrenalina la inactivan (PKA)",
     "mapa_cov": "P = inactiva (GSK-3/PKA)", "mapa_hor": "Insulina ↑ · Glucagón/Adrenalina ↓"},
    {"id": "gp", "via": 3, "enzima": "Glucógeno fosforilasa", "ec": "2.4.1.1",
     "activadores": ["AMP (músculo)", "Ca²⁺ (músculo)"], "inhibidores": ["ATP", "Glucosa-6-P", "Glucosa (hígado)"],
     "covalente": "Fosforilada por fosforilasa quinasa = ACTIVA (forma a); desfosforilada por PP1 = inactiva (forma b)",
     "hormonal": "Glucagón (hígado) y adrenalina (músculo) la activan vía AMPc–PKA; insulina la inactiva",
     "mapa_cov": "P = activa (fosforilasa quinasa)", "mapa_hor": "Glucagón/Adrenalina ↑ · Insulina ↓"},

    # ---------------- 4. PENTOSAS FOSFATO ----------------
    {"id": "g6pdh", "via": 4, "enzima": "Glucosa-6-P deshidrogenasa (G6PDH)", "ec": "1.1.1.49",
     "activadores": ["NADP⁺"], "inhibidores": ["NADPH"],
     "covalente": "",
     "hormonal": "Inducida por insulina y dieta rica en hidratos de carbono",
     "mapa_cov": "", "mapa_hor": "Insulina ↑ (gen)"},

    # ---------------- 5. PDH ----------------
    {"id": "pdh", "via": 5, "enzima": "Complejo piruvato deshidrogenasa (PDH)", "ec": "1.2.4.1 (E1)",
     "activadores": ["Piruvato", "ADP", "NAD⁺", "CoA", "Ca²⁺"], "inhibidores": ["Acetil-CoA", "NADH", "ATP"],
     "covalente": "PDH quinasa (PDK) fosforila E1 = INACTIVA; PDH fosfatasa (PDP, ⊕ Ca²⁺) = activa",
     "hormonal": "Insulina activa la PDP (hígado/adiposo); en ayuno aumenta la PDK",
     "mapa_cov": "P (PDK) = inactiva · PDP activa", "mapa_hor": "Insulina ↑"},

    # ---------------- 6. KREBS ----------------
    {"id": "cs", "via": 6, "enzima": "Citrato sintasa", "ec": "2.3.3.1",
     "activadores": ["ADP"], "inhibidores": ["ATP", "NADH", "Succinil-CoA", "Citrato"],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": ""},
    {"id": "icdh", "via": 6, "enzima": "Isocitrato deshidrogenasa", "ec": "1.1.1.41",
     "activadores": ["ADP", "Ca²⁺", "NAD⁺"], "inhibidores": ["ATP", "NADH"],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": "Paso limitante del ciclo"},
    {"id": "akgdh", "via": 6, "enzima": "α-Cetoglutarato deshidrogenasa", "ec": "1.2.4.2",
     "activadores": ["Ca²⁺", "AMP"], "inhibidores": ["Succinil-CoA", "NADH", "ATP"],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": ""},

    # ---------------- 7. CTE / ATP SINTASA ----------------
    {"id": "atpsint", "via": 7, "enzima": "ATP sintasa (Complejo V)", "ec": "7.1.2.2",
     "activadores": ["ADP + Pi (control respiratorio)"], "inhibidores": ["ATP/ADP alto", "IF1", "Oligomicina"],
     "covalente": "",
     "hormonal": "Hormona tiroidea aumenta la actividad mitocondrial; desacopladores (UCP1/termogenina) disipan el gradiente",
     "mapa_cov": "", "mapa_hor": "Control respiratorio por ADP"},

    # ---------------- 10. LIPOGÉNESIS ----------------
    {"id": "acly", "via": 10, "enzima": "ATP-citrato liasa", "ec": "2.3.3.8",
     "activadores": [], "inhibidores": [],
     "covalente": "Fosforilada por Akt (vía insulina) = más activa",
     "hormonal": "Insulina la activa e induce su síntesis (SREBP-1c)",
     "mapa_cov": "P (Akt) = activa", "mapa_hor": "Insulina ↑"},
    {"id": "acc", "via": 10, "enzima": "Acetil-CoA carboxilasa (ACC)", "ec": "6.4.1.2",
     "activadores": ["Citrato"], "inhibidores": ["Palmitoil-CoA"],
     "covalente": "Fosforilada por AMPK y PKA = INACTIVA; desfosforilada por PP2A = activa",
     "hormonal": "Insulina la activa; glucagón y adrenalina la inactivan. Paso limitante de la lipogénesis",
     "mapa_cov": "P = inactiva (AMPK/PKA)", "mapa_hor": "Insulina ↑ · Glucagón ↓"},
    {"id": "fas", "via": 10, "enzima": "Ácido graso sintasa (FAS)", "ec": "2.3.1.85",
     "activadores": [], "inhibidores": ["Palmitoil-CoA"],
     "covalente": "",
     "hormonal": "Control transcripcional: insulina la induce (SREBP-1c); ayuno y AG poliinsaturados la reprimen",
     "mapa_cov": "", "mapa_hor": "Insulina ↑ (gen) · Ayuno ↓"},

    # ---------------- 9. β-OXIDACIÓN ----------------
    {"id": "cpt1", "via": 9, "enzima": "Carnitina palmitoiltransferasa-1 (CPT-1)", "ec": "2.3.1.21",
     "activadores": [], "inhibidores": ["Malonil-CoA"],
     "covalente": "",
     "hormonal": "Glucagón la favorece indirectamente (inactiva la ACC → ↓ malonil-CoA). Paso limitante de la β-oxidación",
     "mapa_cov": "", "mapa_hor": "Paso limitante · Glucagón ↑ (indirecto)"},

    # ---------------- 11. CETOGÉNESIS ----------------
    {"id": "hmgcs2", "via": 11, "enzima": "HMG-CoA sintasa mitocondrial (HMGCS2)", "ec": "2.3.3.10",
     "activadores": [], "inhibidores": ["Succinil-CoA"],
     "covalente": "",
     "hormonal": "Inducida por glucagón y ayuno (PPARα); reprimida por insulina. Paso limitante de la cetogénesis",
     "mapa_cov": "", "mapa_hor": "Glucagón/ayuno ↑ · Insulina ↓"},

    # ---------------- 12. COLESTEROL ----------------
    {"id": "hmgcr", "via": 12, "enzima": "HMG-CoA reductasa", "ec": "1.1.1.34",
     "activadores": [], "inhibidores": ["Colesterol", "Mevalonato", "Oxisteroles", "Estatinas (fármaco)"],
     "covalente": "Fosforilada por AMPK = INACTIVA; desfosforilada (fosfatasa, insulina) = activa",
     "hormonal": "Insulina la activa; glucagón la inactiva. El colesterol reprime su gen (SREBP-2) y acelera su degradación (INSIG)",
     "mapa_cov": "P = inactiva (AMPK)", "mapa_hor": "Insulina ↑ · Glucagón ↓"},

    # ---------------- 13. NITRÓGENO ----------------
    {"id": "gldh", "via": 13, "enzima": "Glutamato deshidrogenasa (GLDH)", "ec": "1.4.1.3",
     "activadores": ["ADP", "GDP"], "inhibidores": ["ATP", "GTP"],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": ""},

    # ---------------- 14. UREA ----------------
    {"id": "cps1", "via": 14, "enzima": "Carbamoil fosfato sintetasa I (CPS-I)", "ec": "6.3.4.16",
     "activadores": ["N-Acetilglutamato (obligado)"], "inhibidores": [],
     "covalente": "",
     "hormonal": "La NAG sintasa se activa por arginina; dieta rica en proteínas y glucagón inducen las enzimas del ciclo",
     "mapa_cov": "", "mapa_hor": "Paso limitante del ciclo"},

    # ---------------- 15. NUCLEÓTIDOS (SÍNTESIS) ----------------
    {"id": "prpp_s", "via": 15, "enzima": "PRPP Sintetasa", "ec": "2.7.6.1",
     "activadores": ["Pi"], "inhibidores": ["AMP", "GMP", "IMP"],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": "Inhibición por producto purínico"},
    {"id": "prpp_at", "via": 15, "enzima": "Glutamina-PRPP amidotransferasa", "ec": "2.4.2.14",
     "activadores": ["PRPP"], "inhibidores": ["IMP", "AMP", "GMP"],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": "Paso comprometido purinas de novo"},
    {"id": "cps2", "via": 15, "enzima": "Carbamoil fosfato sintetasa II (CPS-II)", "ec": "6.3.5.5",
     "activadores": ["PRPP", "ATP"], "inhibidores": ["UTP"],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": "Paso limitante pirimidinas citosólica"},
    {"id": "atcasa", "via": 15, "enzima": "Aspartato transcarbamoilasa (ATCasa)", "ec": "2.1.3.2",
     "activadores": ["ATP"], "inhibidores": ["CTP"],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": "Regulación por retroinhibición de CTP"},
    {"id": "rnr", "via": 15, "enzima": "Ribonucleótido reductasa (RNR)", "ec": "1.17.4.1",
     "activadores": ["ATP"], "inhibidores": ["dATP", "Hidroxiurea (fármaco)"],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": "Control alostérico global de dNTPs"},
    {"id": "ts", "via": 15, "enzima": "Timidilato sintasa", "ec": "2.1.1.45",
     "activadores": [], "inhibidores": ["5-Fluorouracilo (FdUMP, suicida)"],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": "Diana antitumoral de 5-FU"},

    # ---------------- 16. NUCLEÓTIDOS (CATABOLISMO) ----------------
    {"id": "ada", "via": 16, "enzima": "Adenosina desaminasa (ADA)", "ec": "3.5.4.4",
     "activadores": [], "inhibidores": [],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": "Déficit: Inmunodeficiencia severa (SCID)"},
    {"id": "xod", "via": 16, "enzima": "Xantina oxidasa (XOD)", "ec": "1.17.3.2",
     "activadores": [], "inhibidores": ["Alopurinol (suicida)", "Febuxostat"],
     "covalente": "", "hormonal": "",
     "mapa_cov": "", "mapa_hor": "Diana farmacológica de la gota"},
]

ENZIMAS_POR_ID = {e["id"]: e for e in ENZIMAS}
VIAS_POR_N = {v["n"]: v for v in VIAS}
