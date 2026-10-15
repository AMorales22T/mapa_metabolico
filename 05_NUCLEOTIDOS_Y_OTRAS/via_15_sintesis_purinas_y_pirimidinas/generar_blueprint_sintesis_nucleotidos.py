#!/usr/bin/env python3
"""
GENERADOR DEL BLUEPRINT EXCALIDRAW - SÍNTESIS DE PURINAS Y PIRIMIDINAS (VÍA 15)
=============================================================================
Blueprint editable en formato .excalidraw estructurado según el skill excalidraw-diagram:
- Arquitectura multi-zoom: Visión general, rutas de novo, salvamento y regulación recíproca.
- Colores semánticos definidos en color-palette.md (Start, End, Enzymes, Regulators).
- Topología libre de ruido y conectividad visual entre intermediarios.
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
        "text": "ARQUITECTURA METABÓLICA: SÍNTESIS DE NUCLEÓTIDOS (PURINAS Y PIRIMIDINAS)",
        "originalText": "ARQUITECTURA METABÓLICA: SÍNTESIS DE NUCLEÓTIDOS (PURINAS Y PIRIMIDINAS)",
        "fontSize": 26, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#1e40af", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    elements.append({
        "type": "text", "id": "subtitle_main", "x": 60, "y": 82, "width": 1050, "height": 24,
        "text": "Rutas De Novo (PRPP, IMP, UMP), Vías de Salvamento (HGPRT/APRT) y Regulación Alostérica Cruzada",
        "originalText": "Rutas De Novo (PRPP, IMP, UMP), Vías de Salvamento (HGPRT/APRT) y Regulación Alostérica Cruzada",
        "fontSize": 15, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#64748b", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # -------------------------------------------------------------
    # 2. CONTENEDORES COMPARTIMENTALES / REGIONALES
    # -------------------------------------------------------------
    # Región Central: Precursor Común PRPP
    elements.append({
        "type": "rectangle", "id": "sec_precursor", "x": 60, "y": 130, "width": 420, "height": 340,
        "strokeColor": "#c2410c", "backgroundColor": "#fff7ed", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 100,
        "roundness": {"type": 3, "value": 8},
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "lbl_sec_precursor", "x": 80, "y": 145, "width": 260, "height": 20,
        "text": "ACTIVACIÓN DE LA RIBOSA (PRPP)", "originalText": "ACTIVACIÓN DE LA RIBOSA (PRPP)",
        "fontSize": 13, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#c2410c", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # Región Izquierda-Media: Purinas De Novo y Salvamento
    elements.append({
        "type": "rectangle", "id": "sec_purinas", "x": 510, "y": 130, "width": 640, "height": 720,
        "strokeColor": "#1e3a5f", "backgroundColor": "#eff6ff", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 100,
        "roundness": {"type": 3, "value": 8},
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "lbl_sec_purinas", "x": 530, "y": 145, "width": 340, "height": 20,
        "text": "SÍNTESIS DE PURINAS: IMP ➔ AMP / GMP", "originalText": "SÍNTESIS DE PURINAS: IMP ➔ AMP / GMP",
        "fontSize": 13, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#1e40af", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # Región Derecha: Pirimidinas De Novo y Timidilato
    elements.append({
        "type": "rectangle", "id": "sec_pirimidinas", "x": 1180, "y": 130, "width": 620, "height": 720,
        "strokeColor": "#7c3aed", "backgroundColor": "#faf5ff", "fillStyle": "solid",
        "strokeWidth": 2, "strokeStyle": "dashed", "roughness": 0, "opacity": 100,
        "roundness": {"type": 3, "value": 8},
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })
    elements.append({
        "type": "text", "id": "lbl_sec_pirimidinas", "x": 1200, "y": 145, "width": 360, "height": 20,
        "text": "SÍNTESIS DE PIRIMIDINAS: UMP ➔ CTP / dTMP", "originalText": "SÍNTESIS DE PIRIMIDINAS: UMP ➔ CTP / dTMP",
        "fontSize": 13, "fontFamily": 3, "textAlign": "left", "verticalAlign": "top",
        "strokeColor": "#6d28d9", "backgroundColor": "transparent", "fillStyle": "solid",
        "strokeWidth": 1, "strokeStyle": "solid", "roughness": 0, "opacity": 100,
        "groupIds": [], "isDeleted": False, "boundElements": None, "link": None, "locked": False
    })

    # -------------------------------------------------------------
    # 3. GENERADOR DE NODOS (METABOLITOS Y ENZIMAS)
    # -------------------------------------------------------------
    def add_node(x, y, text, color_fill="#3b82f6", color_stroke="#1e3a5f", text_color="#ffffff", width=190, height=55, rx=8):
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

    # --- Bloque 1: Ribosa-5-P y PRPP ---
    id_r5p = add_node(150, 190, "Ribosa-5-Fosfato\n(Vía Pentosas Fosfato)", color_fill="#fed7aa", color_stroke="#c2410c", text_color="#431407", height=65)
    id_prpps = add_node(150, 290, "PRPP Sintetasa\n(ATP ➔ AMP)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", height=60)
    id_prpp = add_node(150, 390, "PRPP\n(5-Fosforribosil-1-PP)", color_fill="#fed7aa", color_stroke="#c2410c", text_color="#431407", height=60)

    # --- Bloque 2: Rama Purinas ---
    id_prppat = add_node(540, 200, "PRPP Amidotransferasa\n(+ Gln ➔ Glu + PPi)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", height=65)
    id_imp = add_node(540, 310, "Inosina Monofosfato (IMP)\n(Punto de Bifurcación Purínica)", color_fill="#93c5fd", color_stroke="#1e3a5f", text_color="#1e3a5f", height=65)

    # Bifurcación hacia AMP
    id_adsl_sint = add_node(540, 420, "Adenilosuccinato Sintetasa\n(+ Aspartato + GTP)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", height=65)
    id_adsl_lias = add_node(540, 520, "Adenilosuccinato Liasa\n(Libera Fumarato)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", height=60)
    id_amp = add_node(540, 620, "AMP (Adenosina-5'-P)\n➔ ATP (ARN / Energía)", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b", height=60)

    # Bifurcación hacia GMP
    id_impdh = add_node(860, 420, "IMP Deshidrogenasa\n(+ NAD⁺ + H2O ➔ NADH)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", height=65)
    id_gmps = add_node(860, 520, "GMP Sintetasa\n(+ Gln + ATP)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", height=60)
    id_gmp = add_node(860, 620, "GMP (Guanosina-5'-P)\n➔ GTP (ARN / Señalización)", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b", height=60)

    # Salvamento de Purinas
    id_salvamento = add_node(700, 740, "SALVAMENTO DE PURINAS\n• HGPRT: Hipoxantina/Guanina ➔ IMP/GMP\n• APRT: Adenina ➔ AMP", color_fill="#e0e7ff", color_stroke="#4338ca", text_color="#312e81", width=340, height=80)

    # --- Bloque 3: Rama Pirimidinas ---
    id_cps2 = add_node(1220, 200, "Carbamoil-P Sintetasa II (CPS-II)\n(2 ATP + Gln + HCO3⁻ citosólico)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", width=240, height=65)
    id_dhodh = add_node(1220, 300, "DHODH (Dihidroorotato DH)\n(Anclada a MMI · Acoplada a CoQ)", color_fill="#fed7aa", color_stroke="#c2410c", text_color="#7c2d12", width=240, height=65)
    id_orotato = add_node(1220, 400, "Orotato + PRPP ➔ UMP\n(UMP Sintasa: OPRT + ODC)", color_fill="#93c5fd", color_stroke="#1e3a5f", text_color="#1e3a5f", width=240, height=65)
    id_ump = add_node(1220, 500, "UMP (Uridina Monofosfato)\n(Precursor común pirimidínico)", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b", width=240, height=60)

    # Sub-ramificación UMP ➔ CTP y dTMP
    id_ctps = add_node(1220, 600, "CTP Sintetasa\n(UTP + Gln + ATP ➔ CTP)", color_fill="#fef3c7", color_stroke="#b45309", text_color="#78350f", width=240, height=60)
    id_ts = add_node(1520, 500, "Timidilato Sintasa (TS)\n(dUMP + Metileno-THF ➔ dTMP)", color_fill="#fee2e2", color_stroke="#dc2626", text_color="#991b1b", width=240, height=65)
    id_rnr = add_node(1520, 400, "Ribonucleótido Reductasa (RNR)\n(NDP ➔ dNDP · Diana Hidroxiurea)", color_fill="#fee2e2", color_stroke="#dc2626", text_color="#991b1b", width=240, height=65)
    id_dtmp = add_node(1520, 600, "dTMP (Timina activa)\n➔ Replicación del ADN", color_fill="#a7f3d0", color_stroke="#047857", text_color="#064e3b", width=240, height=60)

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

    # Pentosas ➔ PRPP
    add_arrow(id_r5p, id_prpps, "#c2410c")
    add_arrow(id_prpps, id_prpp, "#c2410c")

    # PRPP ➔ Purinas De Novo
    add_arrow(id_prpp, id_prppat, "#1e3a5f")
    add_arrow(id_prppat, id_imp, "#1e3a5f")

    # Bifurcación IMP ➔ AMP
    add_arrow(id_imp, id_adsl_sint, "#1e3a5f")
    add_arrow(id_adsl_sint, id_adsl_lias, "#1e3a5f")
    add_arrow(id_adsl_lias, id_amp, "#047857")

    # Bifurcación IMP ➔ GMP
    add_arrow(id_imp, id_impdh, "#1e3a5f")
    add_arrow(id_impdh, id_gmps, "#1e3a5f")
    add_arrow(id_gmps, id_gmp, "#047857")

    # Salvamento de Purinas
    add_arrow(id_salvamento, id_amp, "#4338ca")
    add_arrow(id_salvamento, id_gmp, "#4338ca")

    # Pirimidinas De Novo
    add_arrow(id_cps2, id_dhodh, "#6d28d9")
    add_arrow(id_dhodh, id_orotato, "#6d28d9")
    add_arrow(id_prpp, id_orotato, "#c2410c") # PRPP entra al orotato
    add_arrow(id_orotato, id_ump, "#047857")
    add_arrow(id_ump, id_ctps, "#6d28d9")
    add_arrow(id_ump, id_rnr, "#dc2626")
    add_arrow(id_rnr, id_ts, "#dc2626")
    add_arrow(id_ts, id_dtmp, "#047857")

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
    destino = os.path.join(dir_actual, "blueprint_sintesis_nucleotidos.excalidraw")
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(blueprint, f, indent=2, ensure_ascii=False)
    print(f"✓ Blueprint Excalidraw generado con éxito: {destino}")

if __name__ == "__main__":
    create_blueprint()
