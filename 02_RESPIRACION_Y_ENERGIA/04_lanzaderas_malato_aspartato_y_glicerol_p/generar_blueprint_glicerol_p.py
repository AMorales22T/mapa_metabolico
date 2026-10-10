#!/usr/bin/env python3
"""
GENERADOR DEL BLUEPRINT EXCALIDRAW - LANZADERA DE GLICEROL-3-FOSFATO (VÍA 8B)
=============================================================================
Blueprint editable en formato .excalidraw estructurado según el skill excalidraw-diagram:
- Arquitectura multi-zoom con compartimentación subcelular (Citosol, MME/VDAC, MMI/mGPDH).
- Colores semánticos definidos en color-palette.md (Start, Intermediate, End, Enzymes).
- Conexión funcional con la Cadena Respiratoria (CoQ y Complejo III).
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
        "type": "text", "id": "title_main", "x": 60, "y": 40, "width": 950, "height": 38,
        "text": "ARQUITECTURA METABÓLICA: LANZADERA DE GLICEROL-3-FOSFATO",
        "originalText": "ARQUITECTURA METABÓLICA: LANZADERA DE GLICEROL-3-FOSFATO",
        "fontSize": 26, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#1e40af", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    elements.append({
        "type": "text", "id": "subtitle_main", "x": 60, "y": 82, "width": 1050, "height": 24,
        "text": "Reoxidación Rápida de NADH Citosólico vía Flavoproteína MMI (FAD ➔ CoQ ➔ Complejo III) · Rendimiento: 1.5 ATP",
        "originalText": "Reoxidación Rápida de NADH Citosólico vía Flavoproteína MMI (FAD ➔ CoQ ➔ Complejo III) · Rendimiento: 1.5 ATP",
        "fontSize": 15, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#64748b", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # -------------------------------------------------------------
    # 2. CONTENEDORES COMPARTIMENTALES
    # -------------------------------------------------------------
    # Citosol
    elements.append({
        "type": "rectangle", "id": "sec_citosol", "x": 60, "y": 130, "width": 460, "height": 680,
        "strokeColor": "#3b82f6", "backgroundColor": "#eff6ff", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 100,
        "roundness": {"type": 3, "value": 8},
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "lbl_sec_citosol", "x": 80, "y": 145, "width": 300, "height": 20,
        "text": "CITOSOL CELULAR (REDUCCIÓN cGPDH)", "originalText": "CITOSOL CELULAR (REDUCCIÓN cGPDH)",
        "fontSize": 13, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#1e40af", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # Membrana Externa / Porina VDAC
    elements.append({
        "type": "rectangle", "id": "sec_mme", "x": 550, "y": 130, "width": 180, "height": 680,
        "strokeColor": "#64748b", "backgroundColor": "#f8fafc", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 100,
        "roundness": {"type": 3, "value": 8},
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "lbl_sec_mme", "x": 565, "y": 145, "width": 150, "height": 20,
        "text": "MME / VDAC", "originalText": "MME / VDAC",
        "fontSize": 13, "fontFamily": 3, "textAlign": "center", "verticalAlign": "top",
        "strokeColor": "#475569", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # Membrana Interna / Cadena Respiratoria
    elements.append({
        "type": "rectangle", "id": "sec_mmi", "x": 760, "y": 130, "width": 640, "height": 680,
        "strokeColor": "#c2410c", "backgroundColor": "#fff7ed", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 100,
        "roundness": {"type": 3, "value": 8},
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "lbl_sec_mmi", "x": 780, "y": 145, "width": 480, "height": 20,
        "text": "CARA EXTERNA MMI Y CADENA RESPIRATORIA (mGPDH ➔ CoQ)", "originalText": "CARA EXTERNA MMI Y CADENA RESPIRATORIA (mGPDH ➔ CoQ)",
        "fontSize": 13, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#c2410c", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # -------------------------------------------------------------
    # 3. GENERADOR DE NODOS
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

    # --- Citosol Nodes ---
    id_dhap_cyto = add_node(180, 200, "Dihidroxiacetona-P (DHAP)\n(Intermediario glucolítico [3C])", color_fill="#fed7aa", color_stroke="#c2410c", text_color="#7c2d12", width=220, height=65)
    id_cgpdh = add_node(180, 320, "cGPDH (GPD1 Citosólica)\n(- NADH + H⁺ ➔ + NAD⁺)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", width=220, height=65)
    id_g3p_cyto = add_node(180, 440, "L-Glicerol-3-Fosfato\n(Portador reductor citosólico [3C])", color_fill="#93c5fd", color_stroke="#1e3a5f", text_color="#1e3a5f", width=220, height=65)
    id_balance_cyto = add_node(100, 580, "REGENERACIÓN NAD⁺\n• Permite continuar glucólisis activa\n• Predomina en músculo y cerebro", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b", width=380, height=75)

    # --- MME / VDAC ---
    id_vdac_in = add_node(570, 440, "VDAC Porina\n(Difusión facilitada G3P)", color_fill="#f1f5f9", color_stroke="#475569", text_color="#1e293b", width=140, height=65)
    id_vdac_out = add_node(570, 200, "VDAC Porina\n(Retorno de DHAP)", color_fill="#f1f5f9", color_stroke="#475569", text_color="#1e293b", width=140, height=65)

    # --- MMI / Cadena Respiratoria ---
    id_mgpdh = add_node(820, 320, "mGPDH (GPD2 Mitocondrial)\nFlavoproteína periférica MMI\n(G3P + FAD ➔ DHAP + FADH₂)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", width=240, height=80)
    id_coq = add_node(1130, 320, "Coenzima Q (Ubiquinona)\nCoQ ➔ CoQH₂ (Lipídica en MMI)", color_fill="#e0f2fe", color_stroke="#0284c7", text_color="#0369a1", width=220, height=65)
    id_c3 = add_node(1130, 450, "COMPLEJO III\n(Citocromo bc₁ · Bombea 4 H⁺)", color_fill="#f0fdf4", color_stroke="#16a34a", text_color="#15803d", width=220, height=65)
    id_c4 = add_node(1130, 570, "COMPLEJO IV ➔ O₂\n(H₂O + Gradiente protónico)", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b", width=220, height=65)

    id_bioenergetica = add_node(820, 580, "BALANCE BIOENERGÉTICO: 1.5 ATP\n• Saltea Complejo I (pierde 4 H⁺ de bombeo)\n• Reacción rápida, exergónica e irreversible", color_fill="#fed7aa", color_stroke="#c2410c", text_color="#7c2d12", width=260, height=75)

    # -------------------------------------------------------------
    # 4. FLECHAS (ARROWS)
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

    # Citosol
    add_arrow(id_dhap_cyto, id_cgpdh, "#c2410c")
    add_arrow(id_cgpdh, id_g3p_cyto, "#1e3a5f")
    add_arrow(id_cgpdh, id_balance_cyto, "#047857")

    # Difusión por VDAC
    add_arrow(id_g3p_cyto, id_vdac_in, "#1e3a5f")
    add_arrow(id_vdac_in, id_mgpdh, "#1e3a5f")

    # Oxidación mGPDH y retorno de DHAP
    add_arrow(id_mgpdh, id_vdac_out, "#c2410c")
    add_arrow(id_vdac_out, id_dhap_cyto, "#c2410c")

    # Flujo de electrones a CTE
    add_arrow(id_mgpdh, id_coq, "#0284c7")
    add_arrow(id_coq, id_c3, "#16a34a")
    add_arrow(id_c3, id_c4, "#047857")
    add_arrow(id_mgpdh, id_bioenergetica, "#c2410c")

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
    destino = os.path.join(dir_actual, "blueprint_glicerol_p.excalidraw")
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(blueprint, f, indent=2, ensure_ascii=False)
    print(f"✓ Blueprint Excalidraw generado con éxito: {destino}")

if __name__ == "__main__":
    create_blueprint()
