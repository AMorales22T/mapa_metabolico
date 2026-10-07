#!/usr/bin/env python3
"""
GENERADOR DEL BLUEPRINT EXCALIDRAW - COMPLEJO PIRUVATO DESHIDROGENASA (PDH)
===========================================================================
Genera el archivo .excalidraw editable para diagramación y presentación.
"""

import json
import uuid
import time
import os

def crear_elemento(tipo, x, y, width, height, text="", strokeColor="#1e293b", backgroundColor="transparent", fillStyle="hachure"):
    el_id = str(uuid.uuid4())[:8]
    elem = {
        "id": el_id,
        "type": tipo,
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "angle": 0,
        "strokeColor": strokeColor,
        "backgroundColor": backgroundColor,
        "fillStyle": fillStyle,
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "strokeSharpness": "round",
        "seed": int(time.time() * 1000) % 100000,
        "version": 1,
        "versionNonce": 1,
        "isDeleted": False,
        "boundElements": None,
        "updated": int(time.time() * 1000),
        "link": None,
        "locked": False
    }
    if tipo == "text":
        elem["text"] = text
        elem["fontSize"] = 16
        elem["fontFamily"] = 1
        elem["textAlign"] = "left"
        elem["verticalAlign"] = "top"
        elem["baseline"] = 14
    return elem

def main():
    elementos = []
    
    # 1. Título General
    elementos.append(crear_elemento("text", 100, 50, 600, 40, "COMPLEJO PIRUVATO DESHIDROGENASA (PDH) - BLUEPRINT", strokeColor="#ea580c"))
    
    # 2. Entrada: Piruvato Citosol -> MPC
    elementos.append(crear_elemento("rectangle", 100, 120, 220, 60, strokeColor="#475569", backgroundColor="#f1f5f9", fillStyle="solid"))
    elementos.append(crear_elemento("text", 120, 138, 180, 24, "Piruvato (Citosol 3C)"))
    
    elementos.append(crear_elemento("rectangle", 100, 220, 220, 50, strokeColor="#9a3412", backgroundColor="#ffedd5", fillStyle="solid"))
    elementos.append(crear_elemento("text", 130, 235, 160, 24, "Transportador MPC1/2", strokeColor="#9a3412"))

    # 3. Subunidad E1
    elementos.append(crear_elemento("rectangle", 380, 120, 320, 150, strokeColor="#ea580c", backgroundColor="#fff7ed", fillStyle="solid"))
    elementos.append(crear_elemento("text", 400, 135, 280, 24, "E1: Piruvato Deshidrogenasa", strokeColor="#c2410c"))
    elementos.append(crear_elemento("text", 400, 170, 280, 20, "• Cofactor: TPP\n• Descarboxilación (CO2 ↑)\n• Forma Hidroxietil-TPP"))

    # 4. Subunidad E2
    elementos.append(crear_elemento("rectangle", 740, 120, 340, 180, strokeColor="#ca8a04", backgroundColor="#fefce8", fillStyle="solid"))
    elementos.append(crear_elemento("text", 760, 135, 300, 24, "E2: Dihidrolipoil Transacetilasa", strokeColor="#854d0e"))
    elementos.append(crear_elemento("text", 760, 170, 300, 20, "• Cofactor: Lipoamida (brazo oscilante)\n• + CoA-SH ➔ Acetil-CoA (2C)\n• Queda Dihidrolipoamida reducida"))

    # 5. Subunidad E3
    elementos.append(crear_elemento("rectangle", 1120, 120, 320, 160, strokeColor="#16a34a", backgroundColor="#f0fdf4", fillStyle="solid"))
    elementos.append(crear_elemento("text", 1140, 135, 280, 24, "E3: Dihidrolipoil Deshidrogenasa", strokeColor="#15803d"))
    elementos.append(crear_elemento("text", 1140, 170, 280, 20, "• Cofactores: FAD y NAD⁺\n• Reoxida lipoamida (S-S)\n• Produce: NADH + H⁺"))

    # 6. Módulo Regulación
    elementos.append(crear_elemento("rectangle", 380, 340, 500, 180, strokeColor="#0284c7", backgroundColor="#f0f9ff", fillStyle="solid"))
    elementos.append(crear_elemento("text", 400, 355, 460, 24, "REGULACIÓN COVALENTE Y ALOSTÉRICA", strokeColor="#0369a1"))
    elementos.append(crear_elemento("text", 400, 390, 460, 20, "• PDK (Cinasa): Inactiva E1 por fosforilación (+ATP)\n• PDP (Fosfatasa): Activa E1 (⊕ Ca²⁺, Insulina)\n• Inhibidores: Acetil-CoA, NADH, ATP\n• Activadores: Piruvato, ADP, NAD⁺, Ca²⁺"))

    # 7. Salida a Destinos
    elementos.append(crear_elemento("rectangle", 920, 340, 520, 180, strokeColor="#7c3aed", backgroundColor="#faf5ff", fillStyle="solid"))
    elementos.append(crear_elemento("text", 940, 355, 480, 24, "DESTINOS DE ACETIL-COA FORMADO", strokeColor="#6d28d9"))
    elementos.append(crear_elemento("text", 940, 390, 480, 20, "1. Ciclo de Krebs (Citrato Sintasa ➔ TCA)\n2. Lipogénesis (ACLY ➔ ACC ➔ Ácidos Grasos)\n3. Cetogénesis (HMG-CoA mitocondrial ➔ Cuerpos Cetónicos)\n4. Colesterol (HMG-CoA citosólico ➔ Mevalonato)"))

    blueprint = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elementos,
        "appState": {
            "gridSize": None,
            "viewBackgroundColor": "#ffffff"
        },
        "files": {}
    }

    destino = os.path.join(os.path.dirname(os.path.abspath(__file__)), "blueprint_pdh.excalidraw")
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(blueprint, f, indent=2, ensure_ascii=False)
    print(f" Blueprint Excalidraw generado en: {destino}")

if __name__ == "__main__":
    main()
