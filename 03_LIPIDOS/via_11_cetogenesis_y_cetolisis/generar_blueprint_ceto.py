#!/usr/bin/env python3
"""
Genera el blueprint arquitectónico Excalidraw para Cetogénesis y Cetólisis
siguiendo las directrices del skill 'excalidraw-diagram'.
"""
import json

def create_blueprint():
    elements = []
    
    # Título y Subtítulo
    elements.append({
        "type": "text",
        "id": "title_ceto",
        "x": 80, "y": 40,
        "width": 880, "height": 38,
        "text": "ARQUITECTURA ESPACIAL: CETOGÉNESIS Y CETÓLISIS",
        "originalText": "ARQUITECTURA ESPACIAL: CETOGÉNESIS Y CETÓLISIS",
        "fontSize": 26,
        "fontFamily": 3,
        "textAlign": "left",
        "verticalAlign": "top",
        "strokeColor": "#9f1239",
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": 1001,
        "version": 1,
        "versionNonce": 1002,
        "isDeleted": False,
        "groupIds": [],
        "boundElements": None,
        "link": None,
        "locked": False,
        "containerId": None,
        "lineHeight": 1.25
    })
    
    elements.append({
        "type": "text",
        "id": "subtitle_ceto",
        "x": 80, "y": 85,
        "width": 950, "height": 24,
        "text": "Flujo intertisular: Hígado (Cetogénesis, mHS) ➔ Torrente Plasmático (MCT1) ➔ Músculo/Cerebro (Cetólisis, SCOT)",
        "originalText": "Flujo intertisular: Hígado (Cetogénesis, mHS) ➔ Torrente Plasmático (MCT1) ➔ Músculo/Cerebro (Cetólisis, SCOT)",
        "fontSize": 15,
        "fontFamily": 3,
        "textAlign": "left",
        "verticalAlign": "top",
        "strokeColor": "#64748b",
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": 1003,
        "version": 1,
        "versionNonce": 1004,
        "isDeleted": False,
        "groupIds": [],
        "boundElements": None,
        "link": None,
        "locked": False,
        "containerId": None,
        "lineHeight": 1.25
    })

    # Región 1: Hígado - Matriz Mitocondrial (Cetogénesis)
    elements.append({
        "type": "rectangle",
        "id": "sec_higado",
        "x": 80, "y": 130,
        "width": 950, "height": 280,
        "strokeColor": "#d97706",
        "backgroundColor": "#fffbeb",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "dashed",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": 2001,
        "version": 1,
        "versionNonce": 2002,
        "isDeleted": False,
        "groupIds": [],
        "boundElements": None,
        "link": None,
        "locked": False,
        "roundness": {"type": 3}
    })
    elements.append({
        "type": "text",
        "id": "lbl_sec_higado",
        "x": 100, "y": 145,
        "width": 550, "height": 22,
        "text": "1. HÍGADO (MATRIZ MITOCONDRIAL) - SÍNTESIS DE CUERPOS CETÓNICOS",
        "originalText": "1. HÍGADO (MATRIZ MITOCONDRIAL) - SÍNTESIS DE CUERPOS CETÓNICOS",
        "fontSize": 14,
        "fontFamily": 3,
        "textAlign": "left",
        "verticalAlign": "top",
        "strokeColor": "#b45309",
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": 2003,
        "version": 1,
        "versionNonce": 2004,
        "isDeleted": False,
        "groupIds": [],
        "boundElements": None,
        "link": None,
        "locked": False,
        "containerId": None,
        "lineHeight": 1.25
    })

    # Región 2: Torrente Sanguíneo (Plasma)
    elements.append({
        "type": "rectangle",
        "id": "sec_torrente",
        "x": 80, "y": 440,
        "width": 950, "height": 180,
        "strokeColor": "#e11d48",
        "backgroundColor": "#ffe4e6",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "dashed",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": 3001,
        "version": 1,
        "versionNonce": 3002,
        "isDeleted": False,
        "groupIds": [],
        "boundElements": None,
        "link": None,
        "locked": False,
        "roundness": {"type": 3}
    })
    elements.append({
        "type": "text",
        "id": "lbl_sec_torrente",
        "x": 100, "y": 455,
        "width": 600, "height": 22,
        "text": "2. CIRCULACIÓN SISTÉMICA (PLASMA) - TRANSPORTE SOLUBLE SIN ALBÚMINA",
        "originalText": "2. CIRCULACIÓN SISTÉMICA (PLASMA) - TRANSPORTE SOLUBLE SIN ALBÚMINA",
        "fontSize": 14,
        "fontFamily": 3,
        "textAlign": "left",
        "verticalAlign": "top",
        "strokeColor": "#9f1239",
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": 3003,
        "version": 1,
        "versionNonce": 3004,
        "isDeleted": False,
        "groupIds": [],
        "boundElements": None,
        "link": None,
        "locked": False,
        "containerId": None,
        "lineHeight": 1.25
    })

    # Región 3: Músculo / Cerebro / Riñón (Cetólisis)
    elements.append({
        "type": "rectangle",
        "id": "sec_extrahepatico",
        "x": 80, "y": 650,
        "width": 950, "height": 280,
        "strokeColor": "#0284c7",
        "backgroundColor": "#f0f9ff",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "dashed",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": 4001,
        "version": 1,
        "versionNonce": 4002,
        "isDeleted": False,
        "groupIds": [],
        "boundElements": None,
        "link": None,
        "locked": False,
        "roundness": {"type": 3}
    })
    elements.append({
        "type": "text",
        "id": "lbl_sec_extrahepatico",
        "x": 100, "y": 665,
        "width": 650, "height": 22,
        "text": "3. MATRIZ MITOCONDRIAL EXTRAHEPÁTICA - ACTIVACIÓN ENERGÉTICA (TIOFORASA)",
        "originalText": "3. MATRIZ MITOCONDRIAL EXTRAHEPÁTICA - ACTIVACIÓN ENERGÉTICA (TIOFORASA)",
        "fontSize": 14,
        "fontFamily": 3,
        "textAlign": "left",
        "verticalAlign": "top",
        "strokeColor": "#0369a1",
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "angle": 0,
        "seed": 4003,
        "version": 1,
        "versionNonce": 4004,
        "isDeleted": False,
        "groupIds": [],
        "boundElements": None,
        "link": None,
        "locked": False,
        "containerId": None,
        "lineHeight": 1.25
    })

    blueprint = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elements,
        "appState": {
            "viewBackgroundColor": "#ffffff",
            "gridSize": 20
        },
        "files": {}
    }
    
    import os
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blueprint_cetogenesis.excalidraw")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(blueprint, f, indent=2, ensure_ascii=False)
    print(f"Blueprint Excalidraw generado con éxito en: {out_path}")

if __name__ == "__main__":
    create_blueprint()
