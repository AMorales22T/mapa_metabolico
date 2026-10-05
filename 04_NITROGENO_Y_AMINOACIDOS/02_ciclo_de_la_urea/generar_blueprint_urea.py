#!/usr/bin/env python3
import json
import uuid

def make_id(prefix="el"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def create_blueprint():
    elements = []
    
    # -------------------------------------------------------------
    # 1. TÍTULO Y JERARQUÍA GENERAL
    # -------------------------------------------------------------
    elements.append({
        "type": "text", "id": "title_main", "x": 80, "y": 40, "width": 800, "height": 38,
        "text": "ARQUITECTURA ESPACIAL: CICLO DE LA UREA",
        "originalText": "ARQUITECTURA ESPACIAL: CICLO DE LA UREA",
        "fontSize": 28, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#1e40af", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    
    elements.append({
        "type": "text", "id": "subtitle_main", "x": 80, "y": 85, "width": 850, "height": 24,
        "text": "Topología subcelular: Mitocondria (CPS1, OTC) ➔ Citosol (ASS, ASL, ARG1)",
        "originalText": "Topología subcelular: Mitocondria (CPS1, OTC) ➔ Citosol (ASS, ASL, ARG1)",
        "fontSize": 16, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#64748b", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # -------------------------------------------------------------
    # 2. SECCIONES COMPARTIMENTALES (Section Boundaries)
    # -------------------------------------------------------------
    # Contenedor Mitocondria
    elements.append({
        "type": "rectangle", "id": "sec_mitocondria", "x": 80, "y": 140, "width": 500, "height": 800,
        "strokeColor": "#b45309", "backgroundColor": "#fef3c7", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "label_mito", "x": 90, "y": 150, "width": 150, "height": 20,
        "text": "MATRIZ MITOCONDRIAL", "originalText": "MATRIZ MITOCONDRIAL",
        "fontSize": 14, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#b45309", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # Contenedor Citosol
    elements.append({
        "type": "rectangle", "id": "sec_citosol", "x": 620, "y": 140, "width": 600, "height": 800,
        "strokeColor": "#3b82f6", "backgroundColor": "#eff6ff", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "label_cito", "x": 630, "y": 150, "width": 150, "height": 20,
        "text": "CITOSOL", "originalText": "CITOSOL",
        "fontSize": 14, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#1e40af", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # -------------------------------------------------------------
    # 3. NODOS Y METABOLITOS (Shapes)
    # -------------------------------------------------------------
    def add_node(x, y, text, color_fill="#3b82f6", color_stroke="#1e3a5f", text_color="#ffffff", width=180, height=60, type="rectangle", rx=10):
        node_id = make_id()
        elements.append({
            "type": type, "id": node_id, "x": x, "y": y, "width": width, "height": height,
            "strokeColor": color_stroke, "backgroundColor": color_fill, "fillStyle": "solid",
            "strokeWidth": 2, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
            "roundness": {"type": 3, "value": rx} if type == "rectangle" else None,
            "groupIds": [], "isDeleted": False, "boundElements": [], "link": None, "locked": False
        })
        text_id = make_id("txt")
        elements.append({
            "type": "text", "id": text_id, "x": x + 10, "y": y + height/2 - 12, "width": width - 20, "height": 24,
            "text": text, "originalText": text,
            "fontSize": 16, "fontFamily": 3, "textAlign": "center", "verticalAlign": "middle",
            "strokeColor": text_color, "backgroundColor": "transparent", "fillStyle": "solid",
            "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
            "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False,
            "containerId": node_id
        })
        elements[-2]["boundElements"].append({"id": text_id, "type": "text"})
        return node_id

    # Mitocondria Nodes
    id_nh4 = add_node(200, 200, "NH4+ + HCO3-", color_fill="#fed7aa", color_stroke="#c2410c", text_color="#374151")
    id_cps1 = add_node(200, 300, "CPS1\n(2 ATP -> 2 ADP + Pi)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#374151", height=70)
    id_carbamoyl = add_node(200, 420, "Carbamoil Fosfato", color_fill="#93c5fd", color_stroke="#1e3a5f", text_color="#1e40af")
    id_ornithine_mito = add_node(350, 520, "Ornitina (Mitocondria)", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b")
    id_otc = add_node(200, 520, "OTC", color_fill="#fef3c7", color_stroke="#b45309", text_color="#374151")
    id_citrulline_mito = add_node(200, 650, "Citrulina", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b")

    # Citosol Nodes
    id_citrulline_cyto = add_node(700, 650, "Citrulina (Citosol)", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b")
    id_aspartate = add_node(950, 550, "Aspartato (del Krebs)", color_fill="#fed7aa", color_stroke="#c2410c", text_color="#374151")
    id_ass = add_node(700, 550, "ASS\n(ATP -> AMP + PPi)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#374151", height=70)
    id_argininosuccinate = add_node(700, 420, "Argininosuccinato", color_fill="#93c5fd", color_stroke="#1e3a5f", text_color="#1e40af")
    id_asl = add_node(700, 320, "ASL", color_fill="#fef3c7", color_stroke="#b45309", text_color="#374151")
    id_fumarate = add_node(950, 320, "Fumarato (hacia Krebs)", color_fill="#fee2e2", color_stroke="#dc2626", text_color="#7f1d1d")
    id_arginine = add_node(700, 200, "Arginina", color_fill="#93c5fd", color_stroke="#1e3a5f", text_color="#1e40af")
    id_arg1 = add_node(450, 200, "ARG1\n(+ H2O)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#374151", height=70)
    id_urea = add_node(450, 100, "Urea (Excreción)", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b")
    id_ornithine_cyto = add_node(700, 100, "Ornitina (Citosol)", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b")

    # -------------------------------------------------------------
    # 4. ENLACES / FLECHAS (Arrows)
    # -------------------------------------------------------------
    def add_arrow(start_id, end_id, color="#1e3a5f", type="arrow"):
        arrow_id = make_id("arr")
        elements.append({
            "type": type, "id": arrow_id, "x": 0, "y": 0, "width": 10, "height": 10,
            "strokeColor": color, "backgroundColor": "transparent", "fillStyle": "solid",
            "strokeWidth": 2, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
            "startBinding": {"elementId": start_id, "focus": 0, "gap": 5},
            "endBinding": {"elementId": end_id, "focus": 0, "gap": 5},
            "startArrowhead": None, "endArrowhead": "arrow",
            "points": [[0, 0], [10, 10]],
            "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
        })

    add_arrow(id_nh4, id_cps1)
    add_arrow(id_cps1, id_carbamoyl)
    add_arrow(id_carbamoyl, id_otc)
    add_arrow(id_ornithine_mito, id_otc)
    add_arrow(id_otc, id_citrulline_mito)
    add_arrow(id_citrulline_mito, id_citrulline_cyto, color="#059669") # Transporte
    add_arrow(id_citrulline_cyto, id_ass)
    add_arrow(id_aspartate, id_ass)
    add_arrow(id_ass, id_argininosuccinate)
    add_arrow(id_argininosuccinate, id_asl)
    add_arrow(id_asl, id_fumarate)
    add_arrow(id_asl, id_arginine)
    add_arrow(id_arginine, id_arg1)
    add_arrow(id_arg1, id_urea)
    add_arrow(id_arg1, id_ornithine_cyto)
    add_arrow(id_ornithine_cyto, id_ornithine_mito, color="#059669") # Transporte

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
    
    with open("blueprint_ciclo_urea.excalidraw", "w", encoding="utf-8") as f:
        json.dump(blueprint, f, indent=2, ensure_ascii=False)
    print("Blueprint Excalidraw del Ciclo de la Urea generado con éxito.")

if __name__ == "__main__":
    create_blueprint()
