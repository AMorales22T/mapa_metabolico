#!/usr/bin/env python3
"""
Generador del Blueprint Arquitectónico para Cartulina (Excalidraw JSON)
Mapea la distribución espacial exacta de las rutas metabólicas en una cartulina,
resolviendo la zonificación celular, los cruces de líneas y la escala de metabolitos.
"""

import json
import uuid

def gen_id():
    return str(uuid.uuid4())[:8]

elements = []

def add_rect(x, y, w, h, stroke, bg, label="", sub="", stroke_width=2, stroke_style="solid", fill_style="solid", opacity=100, text_color="#0f172a"):
    rect_id = gen_id()
    r = {
        "id": rect_id,
        "type": "rectangle",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "strokeColor": stroke,
        "backgroundColor": bg,
        "fillStyle": fill_style,
        "strokeWidth": stroke_width,
        "strokeStyle": stroke_style,
        "roughness": 0,
        "opacity": opacity,
        "angle": 0,
        "seed": 10000,
        "version": 1,
        "versionNonce": 10001,
        "isDeleted": False,
        "groupIds": [],
        "boundElements": [],
        "link": None,
        "locked": False
    }
    elements.append(r)
    
    if label:
        t_id = gen_id()
        r["boundElements"].append({"id": t_id, "type": "text"})
        display_text = f"{label}\n{sub}" if sub else label
        t = {
            "id": t_id,
            "type": "text",
            "x": x + 10,
            "y": y + (h // 2) - (20 if sub else 10),
            "width": w - 20,
            "height": 40 if sub else 20,
            "text": display_text,
            "originalText": display_text,
            "fontSize": 15 if not sub else 14,
            "fontFamily": 3,
            "textAlign": "center",
            "verticalAlign": "middle",
            "strokeColor": text_color,
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
            "angle": 0,
            "seed": 20000,
            "version": 1,
            "versionNonce": 20001,
            "isDeleted": False,
            "groupIds": [],
            "boundElements": None,
            "link": None,
            "locked": False,
            "containerId": rect_id,
            "lineHeight": 1.25
        }
        elements.append(t)
    return rect_id

def add_text(x, y, text, size=16, color="#0f172a", align="left"):
    t_id = gen_id()
    t = {
        "id": t_id,
        "type": "text",
        "x": x,
        "y": y,
        "width": len(text) * (size * 0.6),
        "height": size * 1.4,
        "text": text,
        "originalText": text,
        "fontSize": size,
        "fontFamily": 3,
        "textAlign": align,
        "verticalAlign": "top",
        "strokeColor": color,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": 30000,
        "version": 1,
        "versionNonce": 30001,
        "isDeleted": False,
        "groupIds": [],
        "boundElements": None,
        "link": None,
        "locked": False,
        "containerId": None,
        "lineHeight": 1.25
    }
    elements.append(t)
    return t_id

def add_arrow(start_x, start_y, points, stroke="#ea580c", stroke_width=2, stroke_style="solid", label=""):
    a_id = gen_id()
    a = {
        "id": a_id,
        "type": "arrow",
        "x": start_x,
        "y": start_y,
        "width": abs(points[-1][0]),
        "height": abs(points[-1][1]),
        "strokeColor": stroke,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": stroke_width,
        "strokeStyle": stroke_style,
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": 40000,
        "version": 1,
        "versionNonce": 40001,
        "isDeleted": False,
        "groupIds": [],
        "boundElements": [],
        "link": None,
        "locked": False,
        "points": points,
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": None,
        "endArrowhead": "arrow"
    }
    elements.append(a)
    if label:
        mid_x = start_x + points[-1][0] // 2
        mid_y = start_y + points[-1][1] // 2 - 16
        add_text(mid_x, mid_y, label, size=11, color=stroke, align="center")
    return a_id

# -------------------------------------------------------------
# 1. CONTORNO GENERAL DE LA CARTULINA (Escala 1px = ~0.6mm)
# -------------------------------------------------------------
# Cartulina estándar: 1600 x 1150 px
add_rect(40, 40, 1620, 1160, stroke="#0284c7", bg="#f8fafc", label="", stroke_width=4)
add_text(60, 55, "PLAN MAESTRO DE DISTRIBUCIÓN EN CARTULINA: MAPA METABÓLICO CELULAR INTEGRADO", size=20, color="#0369a1")
add_text(60, 85, "Zonificación por compartimentos (Citosol vs Matriz Mitocondrial) para evitar cruces y optimizar espacio", size=13, color="#64748b")

# MEMBRANA PLASMÁTICA Y ESPACIO EXTRACELULAR
add_rect(70, 120, 1560, 45, stroke="#0284c7", bg="#e0f2fe", label="MEMBRANA PLASMÁTICA (Transportadores GLUT-4, Canales y Receptores)", sub="Límite exterior superior de la cartulina", stroke_width=2, text_color="#0369a1")

# -------------------------------------------------------------
# 2. ZONA CITOSOL (Superior y Laterales)
# -------------------------------------------------------------
# A. GLUCÓGENO (Superior Izquierda)
add_rect(90, 190, 360, 160, stroke="#f59e0b", bg="#fffbeb", label="METABOLISMO DEL GLUCÓGENO", sub="G6P ⇄ G1P ⇄ UDP-Glucosa ⇄ Glucógeno\n[Glucógeno Sintasa / Glucógeno Fosforilasa]", stroke_width=2, text_color="#b45309")

# B. GLUCÓLISIS Y GLUCONEOGÉNESIS (Centro Superior Vertical)
add_rect(500, 190, 420, 410, stroke="#ea580c", bg="#fff7ed", label="GLUCÓLISIS Y GLUCONEOGÉNESIS", sub="Eje troncal: Glucosa ➔ G6P ➔ F6P ➔ F-1,6-BP ➔ GAP / DHAP\n➔ 1,3-BPG ➔ 3-PG ➔ 2-PG ➔ PEP ➔ Piruvato\n(Bypasses: G6Pasa, FBPasa-1, PEPCK)", stroke_width=3, text_color="#c2410c")

# C. VÍA DE LAS PENTOSAS FOSFATO (Superior Derecha)
add_rect(960, 190, 370, 180, stroke="#059669", bg="#ecfdf5", label="VÍA PENTOSAS FOSFATO", sub="Fase Oxidativa: G6P ➔ 6-P-Gluconolactona ➔ Ribulosa-5P (+2 NADPH)\nFase No Oxidativa: Xilulosa-5P + Ribosa-5P ⇄ F6P + GAP", stroke_width=2, text_color="#047857")

# D. SÍNTESIS DE NUCLEÓTIDOS (Extremo Derecho)
add_rect(1360, 190, 250, 280, stroke="#7c3aed", bg="#f5f3ff", label="SÍNTESIS NUCLEÓTIDOS", sub="Ribosa-5P ➔ PRPP\n➔ Purinas (IMP, AMP, GMP)\n➔ Pirimidinas (UMP, CTP, dTTP)\n➔ Degradación a Ácido Úrico", stroke_width=2, stroke_style="dashed", text_color="#6d28d9")

# E. LÍPIDOS CITOSÓLICOS / LIPOGÉNESIS (Lateral Izquierdo)
add_rect(90, 380, 360, 110, stroke="#16a34a", bg="#f0fdf4", label="LÍPIDOS: LIPOGÉNESIS (CITOSOL)", sub="• Citrato (CIC) ➔ Acetil-CoA (ACLY)\n• Acetil-CoA ➔ Malonil-CoA (ACC) ➔ Palmitato (FAS)\n[Requiere NADPH de Pentosas Fosfato y Enzima Málica]", stroke_width=2, text_color="#15803d")

# E2. SÍNTESIS DE COLESTEROL (Lateral Izquierdo Medio / REL)
add_rect(90, 500, 360, 115, stroke="#d97706", bg="#fffbeb", label="SÍNTESIS DE COLESTEROL (VÍA MEVALONATO)", sub="• 2 Acetil-CoA ➔ Acetoacetil-CoA ➔ HMG-CoA\n• HMGCR (REL, -2 NADPH, Diana Estatinas) ➔ Mevalonato\n• Mevalonato ➔ IPP (5C) ➔ FPP (15C) ➔ Escualeno (30C) ➔ Colesterol (27C)", stroke_width=2, text_color="#b45309")

# F. CICLO DE LA UREA: FASE CITOSÓLICA (Lateral Derecho)
add_rect(1060, 400, 270, 200, stroke="#2563eb", bg="#eff6ff", label="UREA: FASE CITOSÓLICA", sub="Citrulina (sale de mitocondria)\n➔ Argininosuccinato (ASS + Aspartato)\n➔ Fumarato + Arginina (ASL)\n➔ UREA (Excreción) + Ornitina (retorna)", stroke_width=2, stroke_style="dashed", text_color="#1d4ed8")

# -------------------------------------------------------------
# 3. ZONA MATRIZ MITOCONDRIAL (Centro e Inferior Amplio)
# -------------------------------------------------------------
add_rect(70, 630, 1560, 420, stroke="#b45309", bg="#fefce8", label="", stroke_width=3)
add_text(100, 645, "MATRIZ MITOCONDRIAL (DELIMITADA POR DOBLE MEMBRANA Y CRESTAS)", size=16, color="#92400e")
add_text(100, 668, "Espacio cerrado donde convergen piruvato, beta-oxidación y aminoácidos hacia la energía", size=12, color="#78350f")

# PUERTE ENTRADA PIRUVATO & PDH
add_rect(530, 695, 360, 95, stroke="#ea580c", bg="#ffedd5", label="COMPLEJO PIRUVATO DESHIDROGENASA (PDH)", sub="Piruvato (3C) + CoA + NAD⁺ ➔ Acetil-CoA (2C) + CO₂ + NADH\nE1 (TPP), E2 (Lipoamida), E3 (FAD)", stroke_width=2, text_color="#9a3412")

# EL GRAN CICLO DE KREBS (Corazón Central)
add_rect(480, 810, 460, 220, stroke="#b45309", bg="#fef3c7", label="CICLO DE KREBS (ÁCIDO CÍTRICO / TCA)", sub="Oxalacetato (4C) + Acetil-CoA (2C) ➔ Citrato (6C) ➔ Isocitrato\n➔ α-Cetoglutarato (5C) ➔ Succinil-CoA (4C) ➔ Succinato\n➔ Fumarato ➔ Malato ➔ Oxalacetato\nBalance: 3 NADH, 1 FADH₂, 1 GTP por vuelta", stroke_width=3, text_color="#78350f")

# CADENA DE TRANSPORTE Y ATP SINTASA (Franja Inferior Cresta)
add_rect(980, 810, 620, 220, stroke="#0284c7", bg="#f0f9ff", label="CADENA RESPIRATORIA & FOSFORILACIÓN OXIDATIVA", sub="Membrana Interna / Crestas:\nComplejo I (NADH DH) ➔ Q ➔ Complejo III ➔ Citocromo c ➔ Complejo IV (O₂ ➔ H₂O)\nComplejo II (Succinato DH de Krebs alimenta FADH₂ directo a Q)\nGradiente electroquímico de H⁺ en Espacio Intermembrana ➔ FoF1 ATP Sintasa", stroke_width=2, text_color="#0369a1")

# BETA-OXIDACIÓN Y CETOGÉNESIS (Matriz Izquierda)
add_rect(90, 710, 360, 320, stroke="#d97706", bg="#fffbeb", label="METABOLISMO LIPÍDICO MITOCONDRIAL", sub="1. Lanzadera de Carnitina (CPT-I, CPT-II)\n2. Beta-Oxidación (4 pasos recurrentes):\n   Acil-CoA ➔ Trans-Δ²-Enoil-CoA ➔ L-β-Hidroxiacil-CoA\n   ➔ β-Cetoacil-CoA ➔ Acetil-CoA + Acil-CoA(-2C)\n3. Cetogénesis (Hígado en ayuno prolongado):\n   Acetil-CoA ➔ HMG-CoA ➔ Acetoacetato / β-Hidroxibutirato", stroke_width=2, stroke_style="dashed", text_color="#92400e")

# METABOLISMO DE AMINOÁCIDOS Y UREA MITOCONDRIAL (Matriz Derecha/Centro)
add_rect(980, 695, 340, 100, stroke="#2563eb", bg="#eff6ff", label="UREA MITOCONDRIAL & TRANSAMINACIÓN", sub="NH₄⁺ + HCO₃⁻ ➔ Carbamoil-Fosfato (CPS-1)\nCarbamoil-P + Ornitina ➔ Citrulina (OTC)\nTransaminación (GOT/AST alimenta Oxalacetato y Glutamato)", stroke_width=2, stroke_style="dashed", text_color="#1d4ed8")

# -------------------------------------------------------------
# 4. CONEXIONES E INTERACCIONES CLAVE (FLECHAS ESTRATÉGICAS)
# -------------------------------------------------------------
# Glucólisis a PDH (Entrada a Mitocondria vía MPC)
add_arrow(710, 600, [[0, 95]], stroke="#ea580c", stroke_width=3, label="Piruvato (MPC)")

# PDH a Krebs
add_arrow(710, 790, [[0, 20]], stroke="#ea580c", stroke_width=3, label="Acetil-CoA")

# Beta-oxidación a Krebs (Acetil-CoA)
add_arrow(450, 850, [[30, 0]], stroke="#d97706", stroke_width=3, label="Acetil-CoA")

# Salida de Citrato de Krebs hacia Lipogénesis
add_arrow(480, 830, [[-30, 0], [-30, -310], [-60, -310]], stroke="#16a34a", stroke_width=2, stroke_style="dashed", label="Citrato (Lanzadera CIC)")

# Glucólisis G6P a Glucógeno
add_arrow(500, 260, [[-50, 0]], stroke="#f59e0b", stroke_width=2, label="G6P ⇄ G1P")

# Glucólisis G6P a Pentosas
add_arrow(920, 260, [[40, 0]], stroke="#059669", stroke_width=2, label="G6P")

# Pentosas retorno a Glucólisis
add_arrow(960, 330, [[-40, 0]], stroke="#059669", stroke_width=2, stroke_style="dashed", label="F6P + GAP")

# Pentosas a Nucleótidos
add_arrow(1330, 260, [[30, 0]], stroke="#7c3aed", stroke_width=2, label="Ribosa-5P")

# Krebs a Cadena Respiratoria (NADH y FADH2)
add_arrow(940, 910, [[40, 0]], stroke="#0284c7", stroke_width=3, label="NADH / FADH₂")

# Urea Mitocondria a Citosol
add_arrow(1150, 695, [[0, -95]], stroke="#2563eb", stroke_width=2, stroke_style="dashed", label="Citrulina")

# Urea Citosol a Mitocondria
add_arrow(1210, 600, [[0, 95]], stroke="#2563eb", stroke_width=2, stroke_style="dashed", label="Ornitina")

# -------------------------------------------------------------
# 5. GUÍA PRÁCTICA PARA AHORRAR ESPACIO EN LA CARTULINA FÍSICA
# -------------------------------------------------------------
add_rect(40, 1070, 1620, 80, stroke="#334155", bg="#1e293b", label="", stroke_width=1)
add_text(60, 1080, "REGLAS DE ORO PARA NO QUEDARTE SIN ESPACIO EN LA CARTULINA FÍSICA:", size=13, color="#38bdf8")
add_text(60, 1102, "1. Dibuja fórmulas químicas completas SÓLO en los 8 nodos maestros: Glucosa, G6P, Piruvato, Acetil-CoA, Citrato, α-Cetoglutarato, Oxalacetato y Palmitato.", size=11, color="#cbd5e1")
add_text(60, 1120, "2. Para pasos intermedios (ej. 1,3-BPG, 2-PG, Isocitrato, Succinato) usa cápsulas con el nombre y conteo de C (ej. [3C], [4C]) ahorrando 60% de área.", size=11, color="#cbd5e1")
add_text(60, 1138, "3. Traza las líneas de delimitación (Membrana externa y Mitocondria) con lápiz tenue antes de dibujar cualquier metabolito para no invadir áreas.", size=11, color="#fde047")

excalidraw_data = {
    "type": "excalidraw",
    "version": 2,
    "source": "https://excalidraw.com",
    "elements": elements,
    "appState": {
        "viewBackgroundColor": "#ffffff",
        "gridSize": None
    },
    "files": {}
}

with open("blueprint_cartulina_metabolica.excalidraw", "w", encoding="utf-8") as f:
    json.dump(excalidraw_data, f, indent=2, ensure_ascii=False)

print("✅ Blueprint Excalidraw generado con éxito: blueprint_cartulina_metabolica.excalidraw")
