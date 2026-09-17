#!/usr/bin/env python3
"""
GENERADOR DE LA RUTA GLUCOLÍTICA EN SVG/HTML
============================================
Este script ensambla el archivo Glucolisis.html usando funciones modulares en Python.
Cada función se encarga de fabricar un bloque visual específico (un metabolito, una flecha, etc.).
"""

import os
from estructuras_glucosa import GLUCOSA, GLUCOSA_6_FOSFATO
# -----------------------------------------------------------------------------
# 1. PLANTILLAS BASE DE HTML Y SVG
# -----------------------------------------------------------------------------
# Estas cadenas contienen el "marco" de la página web y las definiciones gráficas
# globales (como las puntas de flecha que reutilizaremos en todo el mapa).

CABECERA_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vía Glucolítica - Mapa Metabólico</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', sans-serif;
      background: #f1f5f9;
      color: #0f172a;
      padding: 30px 15px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .lienzo-svg {
      width: 1000px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.07);
      overflow: hidden;
    }
    svg { display: block; width: 100%; height: auto; }
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="1000" height="900" viewBox="0 0 1000 900" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Flecha de flujo metabólico principal (Naranja) -->
        <marker id="arrowFlow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
          <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de gasto de energía (Roja) -->
        <marker id="arrowRed" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de salida de producto energético (Gris pizarra) -->
        <marker id="arrowSlate" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#475569" />
        </marker>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""


# -----------------------------------------------------------------------------
# 2. FUNCIONES GENERADORAS DE ELEMENTOS
# -----------------------------------------------------------------------------

def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura=""):
    """
    Construye el bloque SVG de un metabolito libre (sin recuadro).
    
    Parámetros:
      - x, y: Posición donde se anclará este bloque en el lienzo general.
      - nombre: Nombre del compuesto (ej: 'D-Glucosa').
      - carbonos: Texto con el número de carbonos (ej: '6 Carbonos'). 
      - detalle: Texto secundario opcional (ej: 'Sustrato inicial').
      - svg_estructura: Código SVG de la molécula química (anillo, enlaces, etc.).
    """
    bloque = f"""
      <!-- Bloque Metabolito: {nombre} -->
      <g transform="translate({x}, {y})">
        <!-- 1. Estructura química dibujada a la izquierda -->
        <g transform="translate(0, 0)">
          {svg_estructura}
        </g>

        <!-- 2. Bloque de texto descriptivo a la derecha de la molécula -->
        <g transform="translate(130, 25)">
          <text x="0" y="0" fill="#0f172a" font-size="18" font-weight="800">{nombre}</text>
          <text x="0" y="20" fill="#ea580c" font-size="12" font-weight="700">{carbonos}</text>
          <text x="0" y="36" fill="#64748b" font-size="11">{detalle}</text>
        </g>
      </g>
    """
    return bloque


# -----------------------------------------------------------------------------
# 3. CONSTRUCCIÓN Y GENERACIÓN DEL ARCHIVO
# -----------------------------------------------------------------------------

def main():
    contenido_svg = []

    # Estructura básica de prueba (círculo guía temporal mientras aprendemos a dibujar el anillo)
    estructura_temporal = """
      <circle cx="45" cy="45" r="35" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4 3" />
      <text x="45" y="49" fill="#94a3b8" font-size="11" text-anchor="middle" font-weight="600">Estructura</text>
    """

    # Paso 1: Generar D-Glucosa
    glucosa = crear_metabolito(
        x=350,
        y=80,
        nombre="D-Glucosa",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Sustrato inicial de la glucólisis",
        svg_estructura=GLUCOSA
    )
    contenido_svg.append(glucosa)
    g6p = crear_metabolito(
        x=350,
        y=270,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (fosforilacion)",
        detalle="Encrucijada metabolica",
        svg_estructura=GLUCOSA_6_FOSFATO
    )
    contenido_svg.append(g6p)
    # Unir todo el código
    html_final = CABECERA_HTML + "\n".join(contenido_svg) + PIE_HTML

    # Escribir el archivo Glucolisis.html en la misma carpeta
    ruta_salida = os.path.join(os.path.dirname(__file__), "Glucolisis.html")
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(html_final)

    print(f"✅ ¡Archivo generado exitosamente en: {ruta_salida}!")


if __name__ == "__main__":
    main()
