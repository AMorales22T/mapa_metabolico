#!/usr/bin/env python3
"""
GENERADOR DEL BLUEPRINT EXCALIDRAW - DEGRADACIÓN DE NUCLEÓTIDOS Y ÁCIDO ÚRICO (VÍA 16)
=====================================================================================
Blueprint editable en formato .excalidraw estructurado según el skill excalidraw-diagram:
- Arquitectura multi-zoom: Catabolismo convergente de purinas a urato y catabolismo soluble de pirimidinas.
- Colores semánticos de color-palette.md (Start, Intermediate, End, Enzymes, Clinical highlights).
"""

import json
import uuid
import os

def make_id(prefix="el"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def create_blueprint():
    elements = []

    # -------------------------------------------------------------
    # 1. TÍTULO Y JERARQUÍA GENERAL
    # -------------------------------------------------------------
    elements.append({
        "type": "text", "id": "title_main", "x": 60, "y": 40, "width": 1050, "height": 38,
        "text": "ARQUITECTURA METABÓLICA: CATABOLISMO DE NUCLEÓTIDOS Y ÁCIDO ÚRICO",
        "originalText": "ARQUITECTURA METABÓLICA: CATABOLISMO DE NUCLEÓTIDOS Y ÁCIDO ÚRICO",
        "fontSize": 26, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#1e40af", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    elements.append({
        "type": "text", "id": "subtitle_main", "x": 60, "y": 82, "width": 1100, "height": 24,
        "text": "Convergencia de Purinas a Ácido Úrico (XOD / Gota) y Degradación Soluble de Pirimidinas (DPD / β-Alanina)",
        "originalText": "Convergencia de Purinas a Ácido Úrico (XOD / Gota) y Degradación Soluble de Pirimidinas (DPD / β-Alanina)",
        "fontSize": 15, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#64748b", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # -------------------------------------------------------------
    # 2. SECCIONES COMPARTIMENTALES / FUNCIONALES
    # -------------------------------------------------------------
    # Sección Izquierda: Catabolismo de Purinas
    elements.append({
        "type": "rectangle", "id": "sec_purinas_cat", "x": 60, "y": 130, "width": 840, "height": 720,
        "strokeColor": "#c2410c", "backgroundColor": "#fff7ed", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 100,
        "roundness": {"type": 3, "value": 8},
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "lbl_sec_purinas_cat", "x": 80, "y": 145, "width": 460, "height": 20,
        "text": "RAMA DE PURINAS: CONVERGENCIA EN ÁCIDO ÚRICO (XOD)", "originalText": "RAMA DE PURINAS: CONVERGENCIA EN ÁCIDO ÚRICO (XOD)",
        "fontSize": 13, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#c2410c", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # Sección Derecha: Catabolismo de Pirimidinas
    elements.append({
        "type": "rectangle", "id": "sec_pirimidinas_cat", "x": 930, "y": 130, "width": 840, "height": 720,
        "strokeColor": "#047857", "backgroundColor": "#f0fdf4", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 100,
        "roundness": {"type": 3, "value": 8},
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "lbl_sec_pirimidinas_cat", "x": 950, "y": 145, "width": 480, "height": 20,
        "text": "RAMA DE PIRIMIDINAS: APERTURA EN CADENA Y EXCRECIÓN SOLUBLE", "originalText": "RAMA DE PIRIMIDINAS: APERTURA EN CADENA Y EXCRECIÓN SOLUBLE",
        "fontSize": 13, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#047857", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # -------------------------------------------------------------
    # 3. GENERADOR DE NODOS (METABOLITOS Y ENZIMAS)
    # -------------------------------------------------------------
    def add_node(x, y, text, color_fill="#3b82f6", color_stroke="#1e3a5f", text_color="#ffffff", width=200, height=55, rx=8):
        node_id = make_id("node")
        elements.append({
            "type": "rectangle", "id": node_id, "x": x, "y": y, "width": width, "height": height,
            "strokeColor": color_stroke, "backgroundColor": color_fill, "fillStyle": "solid",
            "strokeWidth": 2, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
            "roundness": {"type": 3, "value": rx},
            "groupIds": [], "isDeleted": False, "boundElements": [], "link": None, "locked": False
        })
        text_id = make_id("txt")
        elements.append({
            "type": "text", "id": text_id, "x": x + 10, "y": y + height/2 - 12, "width": width - 20, "height": 24,
            "text": text, "originalText": text,
            "fontSize": 14, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
            "strokeColor": text_color, "backgroundColor": "transparent", "fillStyle": "solid",
            "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
            "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False,
            "containerId": node_id
        })
        elements[-2]["boundElements"].append({"id": text_id, "type": "text"})
        return node_id

    # --- Purinas: Eje Adenina / AMP ---
    id_amp = add_node(100, 200, "AMP (Adenosina Monofosfato)", color_fill="#fed7aa", color_stroke="#c2410c", text_color="#7c2d12")
    id_ada = add_node(100, 300, "ADA (Adenosina Desaminasa)\n(Déficit: Inmunodeficiencia SCID)", color_fill="#fee2e2", color_stroke="#dc2626", text_color="#991b1b", height=65)
    id_inosina = add_node(100, 410, "Inosina\n(Hipoxantina-Ribosa)", color_fill="#93c5fd", color_stroke="#1e3a5f", text_color="#1e3a5f", height=60)
    id_hipoxantina = add_node(100, 510, "Hipoxantina\n(Base purínica libre)", color_fill="#fed7aa", color_stroke="#c2410c", text_color="#7c2d12", height=60)

    # --- Purinas: Eje Guanina / GMP ---
    id_gmp = add_node(380, 200, "GMP (Guanosina Monofosfato)", color_fill="#fed7aa", color_stroke="#c2410c", text_color="#7c2d12")
    id_guanina = add_node(380, 350, "Guanina\n(Vía PNP desfosforilante)", color_fill="#93c5fd", color_stroke="#1e3a5f", text_color="#1e3a5f", height=60)
    id_guanasa = add_node(380, 450, "Guanasa\n(+ H2O ➔ NH3)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f")

    # --- Convergencia en Xantina y Ácido Úrico ---
    id_xod1 = add_node(240, 590, "Xantina Oxidasa (XOD - Paso 1)\n(Hipoxantina ➔ Xantina)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", width=220, height=65)
    id_xantina = add_node(240, 680, "Xantina\n(2,6-Dioxipurina)", color_fill="#fed7aa", color_stroke="#c2410c", text_color="#7c2d12", width=220, height=55)
    id_xod2 = add_node(540, 680, "Xantina Oxidasa (XOD - Paso 2)\n(Diana: Alopurinol / Febuxostat)", color_fill="#fee2e2", color_stroke="#dc2626", text_color="#991b1b", width=240, height=65)
    id_urato = add_node(540, 770, "ÁCIDO ÚRICO (URATO)\n➔ Excreción renal (URAT1) / Gota", color_fill="#fecaca", color_stroke="#b91c1c", text_color="#7f1d1d", width=240, height=65)

    # --- Pirimidinas: Eje Uracilo (Citosina ➔ Uracilo) ---
    id_uracilo = add_node(980, 200, "Uracilo / Citosina\n(Bases pirimidínicas)", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b", height=60)
    id_dpd1 = add_node(980, 310, "DPD (Dihidropirimidina DH)\n(+ NADPH · Diana toxicidad 5-FU)", color_fill="#fee2e2", color_stroke="#dc2626", text_color="#991b1b", width=230, height=65)
    id_dihidroura = add_node(980, 420, "Dihidrouracilo\n(Anillo saturado sin C=C)", color_fill="#dbeafe", color_stroke="#1e40af", text_color="#1e3a5f", width=230, height=60)
    id_ureidoprop = add_node(980, 530, "β-Ureidopropionato\n(Cadena abierta acíclica por DHPasa)", color_fill="#dbeafe", color_stroke="#1e40af", text_color="#1e3a5f", width=230, height=65)
    id_beta_alanina = add_node(980, 650, "β-ALANINA SOLUBLE\n(+ NH4⁺ + CO2 ➔ Excreción inocua)", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b", width=230, height=65)

    # --- Pirimidinas: Eje Timina (dTMP) ---
    id_timina = add_node(1360, 200, "Timina (5-Metiluracilo)\n(Del ADN catabolizado)", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b", height=60)
    id_dpd2 = add_node(1360, 310, "DPD (Paso reductor con NADPH)\n(Saturación del C5-C6)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", width=230, height=65)
    id_dihidrotim = add_node(1360, 420, "Dihidrotimina\n(Anillo saturado metilado)", color_fill="#dbeafe", color_stroke="#1e40af", text_color="#1e3a5f", width=230, height=60)
    id_ureidoisobut = add_node(1360, 530, "β-Ureidoisobutirato\n(Cadena abierta metilada por DHPasa)", color_fill="#dbeafe", color_stroke="#1e40af", text_color="#1e3a5f", width=230, height=65)
    id_aminoisobut = add_node(1360, 650, "β-AMINOISOBUTIRATO\n➔ Metabolismo soluble en orina", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b", width=230, height=65)

    # -------------------------------------------------------------
    # 4. FLECHAS Y CONEXIONES (ARROWS)
    # -------------------------------------------------------------
    def add_arrow(start_id, end_id, color="#1e3a5f"):
        arrow_id = make_id("arr")
        elements.append({
            "type": "arrow", "id": arrow_id, "x": 0, "y": 0, "width": 10, "height": 10,
            "strokeColor": color, "backgroundColor": "transparent", "fillStyle": "solid",
            "strokeWidth": 2, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
            "startBinding": {"elementId": start_id, "focus": 0, "gap": 6},
            "endBinding": {"elementId": end_id, "focus": 0, "gap": 6},
            "startArrowhead": None, "endArrowhead": "arrow",
            "points": [[0, 0], [10, 10]],
            "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
        })

    # Purinas Adenina
    add_arrow(id_amp, id_ada, "#c2410c")
    add_arrow(id_ada, id_inosina, "#c2410c")
    add_arrow(id_inosina, id_hipoxantina, "#c2410c")
    add_arrow(id_hipoxantina, id_xod1, "#c2410c")
    add_arrow(id_xod1, id_xantina, "#b45309")

    # Purinas Guanina
    add_arrow(id_gmp, id_guanina, "#1e3a5f")
    add_arrow(id_guanina, id_guanasa, "#1e3a5f")
    add_arrow(id_guanasa, id_xantina, "#b45309")

    # Paso final XOD
    add_arrow(id_xantina, id_xod2, "#b45309")
    add_arrow(id_xod2, id_urato, "#b91c1c")

    # Pirimidinas Uracilo
    add_arrow(id_uracilo, id_dpd1, "#047857")
    add_arrow(id_dpd1, id_dihidroura, "#047857")
    add_arrow(id_dihidroura, id_ureidoprop, "#1e40af")
    add_arrow(id_ureidoprop, id_beta_alanina, "#047857")

    # Pirimidinas Timina
    add_arrow(id_timina, id_dpd2, "#047857")
    add_arrow(id_dpd2, id_dihidrotim, "#047857")
    add_arrow(id_dihidrotim, id_ureidoisobut, "#1e40af")
    add_arrow(id_ureidoisobut, id_aminoisobut, "#047857")

    blueprint = {
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

    dir_actual = os.path.dirname(os.path.abspath(__file__))
    destino = os.path.join(dir_actual, "blueprint_degradacion_nucleotidos.excalidraw")
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(blueprint, f, indent=2, ensure_ascii=False)
    print(f"✓ Blueprint Excalidraw generado con éxito: {destino}")

if __name__ == "__main__":
    create_blueprint()
