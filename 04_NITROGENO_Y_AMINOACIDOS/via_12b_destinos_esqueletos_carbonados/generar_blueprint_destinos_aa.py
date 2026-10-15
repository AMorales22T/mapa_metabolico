#!/usr/bin/env python3
"""
GENERADOR DEL BLUEPRINT EXCALIDRAW: DESTINOS DE LOS ESQUELETOS CARBONADOS DE AMINOÁCIDOS
========================================================================================
Estructura topológica y arquitectónica previa para la convergencia de los 20 aminoácidos
en los 7 intermediarios metabólicos centrales (Piruvato, Acetil-CoA, Acetoacetil-CoA,
α-Cetoglutarato, Succinil-CoA, Fumarato y Oxalacetato).

Cumple estrictamente con las directrices de diseño acordadas:
- Cero rectángulos rígidos para metabolitos (usando nodos redondeados u orgánicos).
- Cero puntos negros para conteo de carbonos (conteo en texto [xC]).
- Información clínica y cofactores hiper-reducida en dianas directas (ej. ⚠ PKU, ⚠ MSUD).
- Bicompartimental: Citosol vs. Matriz Mitocondrial.
"""

import os
import json
import uuid

def make_id(prefix="el"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def create_blueprint():
    elements = []
    
    # -------------------------------------------------------------------------
    # 1. TÍTULO Y JERARQUÍA GENERAL
    # -------------------------------------------------------------------------
    elements.append({
        "type": "text", "id": "title_main", "x": 100, "y": 40, "width": 950, "height": 38,
        "text": "DESTINOS DE LOS ESQUELETOS CARBONADOS DE AMINOÁCIDOS",
        "originalText": "DESTINOS DE LOS ESQUELETOS CARBONADOS DE AMINOÁCIDOS",
        "fontSize": 28, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#0284c7", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    
    elements.append({
        "type": "text", "id": "subtitle_main", "x": 100, "y": 85, "width": 1100, "height": 24,
        "text": "Convergencia de los 20 AA en 7 intermediarios: Glucogénicos (Verde), Cetogénicos (Rojo/Rosa) y Mixtos (Púrpura)",
        "originalText": "Convergencia de los 20 AA en 7 intermediarios: Glucogénicos (Verde), Cetogénicos (Rojo/Rosa) y Mixtos (Púrpura)",
        "fontSize": 15, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#64748b", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # -------------------------------------------------------------------------
    # 2. SECCIONES COMPARTIMENTALES (Límites Orgánicos)
    # -------------------------------------------------------------------------
    # Zona Citosol (Superior / Periférica)
    elements.append({
        "type": "rectangle", "id": "sec_citosol", "x": 80, "y": 140, "width": 1440, "height": 450,
        "strokeColor": "#38bdf8", "backgroundColor": "#f0f9ff", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 50,
        "roundness": {"type": 3, "value": 24},
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "label_citosol", "x": 110, "y": 155, "width": 300, "height": 22,
        "text": "CITOSOL CELULAR (Fase de transaminación e hidroxilación)",
        "originalText": "CITOSOL CELULAR (Fase de transaminación e hidroxilación)",
        "fontSize": 14, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#0284c7", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # Zona Matriz Mitocondrial (Inferior / Central de Oxidación)
    elements.append({
        "type": "rectangle", "id": "sec_mitocondria", "x": 80, "y": 620, "width": 1440, "height": 780,
        "strokeColor": "#f59e0b", "backgroundColor": "#fffbeb", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 50,
        "roundness": {"type": 3, "value": 28},
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "label_mitocondria", "x": 110, "y": 635, "width": 400, "height": 22,
        "text": "MATRIZ MITOCONDRIAL (Ciclo de Krebs, BCKDH y Vía Propionato)",
        "originalText": "MATRIZ MITOCONDRIAL (Ciclo de Krebs, BCKDH y Vía Propionato)",
        "fontSize": 14, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#b45309", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # Helper para nodos orgánicos (píldoras suaves sin rectángulos rígidos)
    def add_pill(x, y, text, color_fill="#e0f2fe", color_stroke="#0284c7", text_color="#0f172a", width=140, height=48, rx=24):
        node_id = make_id()
        elements.append({
            "type": "rectangle", "id": node_id, "x": x, "y": y, "width": width, "height": height,
            "strokeColor": color_stroke, "backgroundColor": color_fill, "fillStyle": "solid",
            "strokeWidth": 1.5, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
            "roundness": {"type": 3, "value": rx},
            "groupIds": [], "isDeleted": False, "boundElements": [], "link": None, "locked": False
        })
        text_id = make_id("txt")
        elements.append({
            "type": "text", "id": text_id, "x": x + 6, "y": y + (height/2) - 10, "width": width - 12, "height": 20,
            "text": text, "originalText": text,
            "fontSize": 13, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
            "strokeColor": text_color, "backgroundColor": "transparent", "fillStyle": "solid",
            "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
            "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False,
            "containerId": node_id
        })
        elements[-2]["boundElements"].append({"id": text_id, "type": "text"})
        return node_id

    # Helper para micro-insignias clínicas o de cofactores (ancladas a diana)
    def add_badge(x, y, text, is_warning=True, width=120, height=26):
        fill = "#fee2e2" if is_warning else "#e0e7ff"
        stroke = "#dc2626" if is_warning else "#4f46e5"
        txt_col = "#991b1b" if is_warning else "#3730a3"
        badge_id = make_id("bdg")
        elements.append({
            "type": "rectangle", "id": badge_id, "x": x, "y": y, "width": width, "height": height,
            "strokeColor": stroke, "backgroundColor": fill, "fillStyle": "solid",
            "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
            "roundness": {"type": 3, "value": 13},
            "groupIds": [], "isDeleted": False, "boundElements": [], "link": None, "locked": False
        })
        t_id = make_id("txt_b")
        elements.append({
            "type": "text", "id": t_id, "x": x + 4, "y": y + 4, "width": width - 8, "height": 18,
            "text": text, "originalText": text,
            "fontSize": 11, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
            "strokeColor": txt_col, "backgroundColor": "transparent", "fillStyle": "solid",
            "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
            "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False,
            "containerId": badge_id
        })
        elements[-2]["boundElements"].append({"id": t_id, "type": "text"})
        return badge_id

    # Flechas conectoras Excalidraw
    def add_arrow(start_x, start_y, end_x, end_y, stroke_color="#0284c7", stroke_width=2, dashed=False):
        arrow_id = make_id("arr")
        elements.append({
            "type": "arrow", "id": arrow_id,
            "x": start_x, "y": start_y, "width": end_x - start_x, "height": end_y - start_y,
            "strokeColor": stroke_color, "backgroundColor": "transparent", "fillStyle": "solid",
            "strokeWidth": stroke_width,
            "strokeStyle": "dashed" if dashed else "solid",
            "roughness": 0, "opacity": 100,
            "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False,
            "points": [[0, 0], [end_x - start_x, end_y - start_y]],
            "lastCommittedPoint": None, "startBinding": None, "endBinding": None,
            "startArrowhead": None, "endArrowhead": "arrow"
        })
        return arrow_id

    # -------------------------------------------------------------------------
    # 3. CONVERGENCIA 1: AMINOÁCIDOS A PIRUVATO [3C] (Columna Izquierda Citosol ➔ Matriz)
    # -------------------------------------------------------------------------
    # Aminoácidos glucogénicos a Piruvato en Citosol
    add_pill(100, 200, "Alanina [3C]", "#dcfce7", "#16a34a", "#14532d")
    add_pill(250, 200, "Serina [3C]", "#dcfce7", "#16a34a", "#14532d")
    add_pill(100, 270, "Glicina [2C]", "#dcfce7", "#16a34a", "#14532d")
    add_pill(250, 270, "Cisteína [3C]", "#dcfce7", "#16a34a", "#14532d")
    add_pill(100, 340, "Treonina [4C]*", "#f3e8ff", "#9333ea", "#581c87") # Mixto
    add_pill(250, 340, "Triptófano [11C]*", "#f3e8ff", "#9333ea", "#581c87") # Mixto

    # Hub Central: PIRUVATO [3C] (en Matriz Mitocondrial / Cruce MPC)
    id_piruvato = add_pill(175, 680, "PIRUVATO [3C]", "#fef3c7", "#d97706", "#78350f", width=180, height=54, rx=27)
    
    # Flechas hacia Piruvato
    add_arrow(170, 400, 220, 675, stroke_color="#16a34a", stroke_width=2.5)
    add_badge(120, 480, "⚡ PLP (ALT / SDH)", is_warning=False, width=130)

    # -------------------------------------------------------------------------
    # 4. CONVERGENCIA 2 Y 3: ACETIL-CoA [2C] Y ACETOACETIL-CoA [4C]
    # -------------------------------------------------------------------------
    # Aminoácidos cetogénicos y aromáticos
    add_pill(450, 200, "Leucina [6C] (Ceto)", "#ffe4e6", "#e11d48", "#881337")
    add_pill(610, 200, "Lisina [6C] (Ceto)", "#ffe4e6", "#e11d48", "#881337")
    add_pill(450, 270, "Isoleucina [6C]*", "#f3e8ff", "#9333ea", "#581c87")
    add_pill(610, 270, "Fenilalanina [9C]*", "#f3e8ff", "#9333ea", "#581c87")
    add_pill(610, 340, "Tirosina [9C]*", "#f3e8ff", "#9333ea", "#581c87")

    # Anotaciones diagnósticas para Phe / Tyr
    add_badge(760, 270, "⚠ PKU (PAH / BH4)", is_warning=True, width=135)
    add_badge(760, 320, "⚠ Alcaptonuria (HGD)", is_warning=True, width=145)
    add_badge(760, 370, "⚠ Tirosinemia I (FAH)", is_warning=True, width=145)

    # Hubs Centrales Cetogénicos en Matriz Mitocondrial
    id_acetoacetil = add_pill(460, 680, "ACETOACETIL-CoA [4C]", "#ffe4e6", "#e11d48", "#881337", width=190, height=54, rx=27)
    id_acetil = add_pill(690, 680, "ACETIL-CoA [2C]", "#fef08a", "#ca8a04", "#713f12", width=170, height=54, rx=27)

    # Flechas cetogénicas
    add_arrow(530, 340, 530, 675, stroke_color="#e11d48", stroke_width=2.5)
    add_arrow(660, 400, 750, 675, stroke_color="#ca8a04", stroke_width=2.5)

    # -------------------------------------------------------------------------
    # 5. CONVERGENCIA 4: α-CETOGLUTARATO [5C] (Ciclo Glutamato)
    # -------------------------------------------------------------------------
    add_pill(930, 200, "Glutamina [5C]", "#dcfce7", "#16a34a", "#14532d")
    add_pill(1080, 200, "Prolina [5C]", "#dcfce7", "#16a34a", "#14532d")
    add_pill(930, 270, "Arginina [6C]", "#dcfce7", "#16a34a", "#14532d")
    add_pill(1080, 270, "Histidina [6C]", "#dcfce7", "#16a34a", "#14532d")
    add_pill(1005, 350, "Glutamato [5C]", "#dcfce7", "#16a34a", "#14532d", width=150)

    # Hub α-Cetoglutarato en Matriz Mitocondrial (Krebs)
    id_akg = add_pill(980, 780, "α-CETOGLUTARATO [5C]", "#ede9fe", "#7c3aed", "#4c1d95", width=200, height=54, rx=27)
    add_arrow(1080, 410, 1080, 775, stroke_color="#7c3aed", stroke_width=2.5)
    add_badge(1140, 520, "GDH (NAD+ -> NADH + NH4+)", is_warning=False, width=170)

    # -------------------------------------------------------------------------
    # 6. CONVERGENCIA 5: SUCCINIL-CoA [4C] (Ramificados y Ciclo Propionato)
    # -------------------------------------------------------------------------
    add_pill(930, 930, "Valina [5C]", "#dcfce7", "#16a34a", "#14532d")
    add_pill(1080, 930, "Isoleucina [6C]*", "#f3e8ff", "#9333ea", "#581c87")
    add_pill(930, 1000, "Metionina [5C]", "#dcfce7", "#16a34a", "#14532d")
    add_pill(1080, 1000, "Treonina [4C]*", "#f3e8ff", "#9333ea", "#581c87")

    add_badge(1240, 940, "⚠ MSUD (BCKDH)", is_warning=True, width=130)
    add_badge(1240, 990, "⚠ Homocistinuria (CBS)", is_warning=True, width=155)

    # Paso intermedio: Propionil-CoA -> Metilmalonil-CoA
    add_pill(1005, 1080, "Propionil-CoA [3C]", "#fef3c7", "#d97706", "#78350f", width=160, height=44)
    add_badge(1180, 1080, "⚡ Biotina / PCC", is_warning=False, width=120)

    # Hub Succinil-CoA
    id_succinil = add_pill(1000, 1190, "SUCCINIL-CoA [4C]", "#ede9fe", "#7c3aed", "#4c1d95", width=180, height=54, rx=27)
    add_arrow(1085, 1130, 1085, 1185, stroke_color="#7c3aed", stroke_width=2.5)
    add_badge(1195, 1160, "⚡ Vit B12 (Mutasa / MMA)", is_warning=True, width=165)

    # -------------------------------------------------------------------------
    # 7. CONVERGENCIA 6 Y 7: FUMARATO [4C] Y OXALACETATO [4C] (Krebs)
    # -------------------------------------------------------------------------
    add_pill(100, 930, "Asparagina [4C]", "#dcfce7", "#16a34a", "#14532d")
    add_pill(250, 930, "Aspartato [4C]", "#dcfce7", "#16a34a", "#14532d")
    add_badge(130, 990, "AST / PLP", is_warning=False, width=90)

    # Hub Fumarato y Oxalacetato en Matriz Mitocondrial
    id_fumarato = add_pill(460, 950, "FUMARATO [4C]", "#ede9fe", "#7c3aed", "#4c1d95", width=170, height=54, rx=27)
    id_oxalacetato = add_pill(180, 1060, "OXALACETATO [4C]", "#ede9fe", "#7c3aed", "#4c1d95", width=180, height=54, rx=27)

    # Conexiones orgánicas hacia Fumarato y Oxalacetato
    add_arrow(320, 975, 455, 975, stroke_color="#7c3aed", stroke_width=2.5) # Asp -> Fumarato (vía urea/purinas)
    add_arrow(250, 980, 250, 1055, stroke_color="#7c3aed", stroke_width=2.5) # Asp -> Oxalacetato (AST)
    add_arrow(660, 400, 540, 945, stroke_color="#9333ea", stroke_width=2.0, dashed=True) # Phe/Tyr -> Fumarato

    # Conexión del Ciclo de Krebs (Esqueleto circular esquemático entre los 4 intermediarios de Krebs)
    # Oxalacetato -> aKG -> Succinil-CoA -> Fumarato -> Oxalacetato
    add_arrow(365, 1085, 995, 1215, stroke_color="#cbd5e1", stroke_width=2, dashed=True)
    add_arrow(995, 820, 1070, 1185, stroke_color="#cbd5e1", stroke_width=2, dashed=True)
    add_arrow(995, 1215, 635, 980, stroke_color="#cbd5e1", stroke_width=2, dashed=True)
    add_arrow(460, 980, 365, 1085, stroke_color="#cbd5e1", stroke_width=2, dashed=True)

    # Leyenda reducida orgánica en el extremo inferior
    elements.append({
        "type": "text", "id": "legend_text", "x": 100, "y": 1330, "width": 1200, "height": 30,
        "text": "LEYENDA: [Verde]=Glucogénico puro  |  [Rojo]=Cetogénico puro (Leu, Lys)  |  [Púrpura*]=Mixto (Ile, Phe, Trp, Tyr, Thr)  |  ⚠=Patología clínica en diana  |  ⚡=Cofactor vitamínico",
        "originalText": "LEYENDA: [Verde]=Glucogénico puro  |  [Rojo]=Cetogénico puro (Leu, Lys)  |  [Púrpura*]=Mixto (Ile, Phe, Trp, Tyr, Thr)  |  ⚠=Patología clínica en diana  |  ⚡=Cofactor vitamínico",
        "fontSize": 13, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#475569", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    return {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {
            "viewBackgroundColor": "#ffffff",
            "currentItemFontFamily": 3
        },
        "files": {}
    }

def main():
    blueprint_data = create_blueprint()
    ruta_salida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blueprint_destinos_aa.excalidraw")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        json.dump(blueprint_data, f, indent=2, ensure_ascii=False)
    print(f"Blueprint generado exitosamente en: {ruta_salida}")

if __name__ == "__main__":
    main()
