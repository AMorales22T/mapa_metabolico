#!/usr/bin/env python3
"""
GENERADOR DE LA RUTA GLUCOLÍTICA EN SVG/HTML
============================================
Este script ensambla el archivo Glucolisis.html usando funciones modulares en Python.
Intercala automáticamente cada metabolito con su reacción enzimática, cofactores,
flechas de flujo y curvas de acoplamiento energético (ATP/ADP y NAD+/NADH).
"""

import os
from estructuras_glucosa import (
    GLUCOSA,
    GLUCOSA_6_FOSFATO,
    FRUCTOSA_6_FOSFATO,
    FRUCTOSA_1_6_BISFOSFATO,
    DIHIDROXIACETONA_FOSFATO,
    GLICERALDEHIDO_3_FOSFATO,
    BISFOSFOGLICERATO_1_3,
    FOSFOGLICERATO_3,
    FOSFOGLICERATO_2,
    FOSFOENOLPIRUVATO,
    PIRUVATO
)

# -----------------------------------------------------------------------------
# 1. PLANTILLAS BASE DE HTML Y SVG
# -----------------------------------------------------------------------------
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
    <svg width="1000" height="1920" viewBox="0 0 1000 1920" xmlns="http://www.w3.org/2000/svg">
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
        <!-- Flecha de generación de energía / ganancia (Verde esmeralda) -->
        <marker id="arrowGreen" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#059669" />
        </marker>
        <!-- Flecha de salida de agua (Azul) -->
        <marker id="arrowBlue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#0284c7" />
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
    """Construye el bloque SVG de un metabolito libre con su estructura y textos."""
    return f"""
      <!-- Metabolito: {nombre} -->
      <g transform="translate({x}, {y})">
        <g transform="translate(0, 0)">
          {svg_estructura}
        </g>
        <g transform="translate(130, 25)">
          <text x="0" y="0" fill="#0f172a" font-size="18" font-weight="800">{nombre}</text>
          <text x="0" y="20" fill="#ea580c" font-size="12" font-weight="700">{carbonos}</text>
          <text x="0" y="36" fill="#64748b" font-size="11">{detalle}</text>
        </g>
      </g>
    """


def crear_reaccion(x, y, enzima, ec="", regulacion="", entra_energia="", sale_energia="", 
                   reversible=False, es_ganancia=False, salida_agua=False):
    """
    Genera el bloque SVG de una reacción:
    - Flecha vertical (simple o reversible)
    - Curvas acopladas (roja/gris para gasto de ATP, verde para ganancia de ATP/NADH, azul para H2O)
    - Textos de enzima, código EC y regulación alostérica
    """
    curvas_energia = ""
    
    # 1. Entrada de energía o reactivo
    if entra_energia:
        color_entrada = "#dc2626" if not es_ganancia else "#475569"
        marcador_entrada = "url(#arrowRed)" if not es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -90 15 Q -30 12 -5 32" fill="none" stroke="{color_entrada}" stroke-width="2" marker-end="{marcador_entrada}"/>
        <text x="-95" y="18" fill="{color_entrada}" font-size="12" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
        
    # 2. Salida de producto energético
    if sale_energia:
        color_salida = "#059669" if es_ganancia else "#475569"
        marcador_salida = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -5 38 Q -30 58 -90 55" fill="none" stroke="{color_salida}" stroke-width="2" marker-end="{marcador_salida}"/>
        <text x="-95" y="58" fill="{color_salida}" font-size="12" font-weight="800" text-anchor="end">{sale_energia}</text>
        """

    # 3. Salida de agua (para Enolasa)
    if salida_agua:
        curvas_energia += """
        <path d="M -5 38 Q -30 58 -80 55" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
        <text x="-85" y="58" fill="#0284c7" font-size="12" font-weight="800" text-anchor="end">- 2 H₂O</text>
        """

    # 4. Flecha principal
    if reversible:
        flecha_central = """
        <line x1="-3" y1="0" x2="-3" y2="65" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        <line x1="3" y1="65" x2="3" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        """
    else:
        flecha_central = """
        <line x1="0" y1="0" x2="0" y2="65" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="28" fill="{color_reg}" font-size="10" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha_central}
      {curvas_energia}
      <g transform="translate(18, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """


def crear_bifurcacion_aldolasa():
    """Genera las flechas ramificadas de la Aldolasa y la conexión de la Triosa Fosfato Isomerasa."""
    return """
    <!-- Bifurcación Aldolasa (F-1,6-BP -> DHAP + GAP) -->
    <g transform="translate(390, 715)">
      <!-- Flecha hacia DHAP (izquierda) -->
      <path d="M 0 0 Q -80 30 -220 70" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <!-- Flecha hacia GAP (derecha) -->
      <path d="M 0 0 Q 80 30 140 70" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      
      <!-- Datos de la Aldolasa en el centro -->
      <g transform="translate(0, 30)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800" text-anchor="middle">Aldolasa</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 4.1.2.13 (Reversible)</text>
      </g>
    </g>

    <!-- Conexión Reversible DHAP <-> GAP (Triosa Fosfato Isomerasa) -->
    <g transform="translate(300, 850)">
      <line x1="-70" y1="-3" x2="160" y2="-3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="160" y1="3" x2="-70" y2="3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <text x="45" y="-10" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">Triosa Fosfato Isomerasa (TPI)</text>
      <text x="45" y="18" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1</text>
    </g>

    <!-- Flecha de convergencia hacia la Fase 2 (GAP -> 1,3-BPG x2) -->
    <g transform="translate(490, 905)">
      <path d="M 40 0 Q 0 35 -90 60" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <text x="-15" y="40" fill="#ea580c" font-size="12" font-weight="800">× 2 moléculas</text>
    </g>
    """


# -----------------------------------------------------------------------------
# 3. CONSTRUCCIÓN Y GENERACIÓN DEL ARCHIVO
# -----------------------------------------------------------------------------

def main():
    contenido_svg = []

    # ================= FASE 1: INVERSIÓN DE ENERGÍA =================

    # 1. D-Glucosa
    contenido_svg.append(crear_metabolito(
        x=350, y=80,
        nombre="D-Glucosa",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Sustrato inicial de la glucólisis",
        svg_estructura=GLUCOSA
    ))

    # Reacción 1: Hexoquinasa
    contenido_svg.append(crear_reaccion(
        x=395, y=180,
        enzima="Hexoquinasa",
        ec="EC 2.7.1.1 (Mg²⁺)",
        regulacion="⊣ Inhibida por G-6-P",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 2. Glucosa-6-Fosfato
    contenido_svg.append(crear_metabolito(
        x=350, y=270,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Fosforilada)",
        detalle="Encrucijada metabólica (Vía Pentosas / Glucógeno)",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # Reacción 2: Fosfohexosa Isomerasa
    contenido_svg.append(crear_reaccion(
        x=395, y=360,
        enzima="Fosfohexosa Isomerasa",
        ec="EC 5.3.1.9 (Mg²⁺)",
        reversible=True
    ))

    # 3. Fructosa-6-Fosfato
    contenido_svg.append(crear_metabolito(
        x=350, y=440,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Furanosa)",
        detalle="Isomerización aldosa → cetosa",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # Reacción 3: Fosfofructoquinasa-1 (Paso Limitante Clave)
    contenido_svg.append(crear_reaccion(
        x=395, y=535,
        enzima="Fosfofructoquinasa-1 (PFK-1)",
        ec="EC 2.7.1.11 (Mg²⁺)",
        regulacion="⊕ AMP, F-2,6-BP | ⊣ ATP, Citrato",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 4. Fructosa-1,6-Bisfosfato
    contenido_svg.append(crear_metabolito(
        x=350, y=625,
        nombre="Fructosa-1,6-Bisfosfato",
        carbonos="6 Carbonos (Doble fosfato)",
        detalle="Molécula comprometida a la lisis",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO
    ))

    # Reacción 4 & 5: Aldolasa + Triosa Fosfato Isomerasa (Bifurcación)
    contenido_svg.append(crear_bifurcacion_aldolasa())

    # 5a. Dihidroxiacetona Fosfato (DHAP)
    contenido_svg.append(crear_metabolito(
        x=100, y=800,
        nombre="Dihidroxiacetona-P",
        carbonos="3 Carbonos (Cetosa)",
        detalle="Interconvertible hacia GAP",
        svg_estructura=DIHIDROXIACETONA_FOSFATO
    ))

    # 5b. Gliceraldehído-3-Fosfato (GAP)
    contenido_svg.append(crear_metabolito(
        x=490, y=800,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Aldosa)",
        detalle="Sustrato activo que continúa la vía",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))


    # ================= FASE 2: RENDIMIENTO ENERGÉTICO (x2) =================

    # 6. 1,3-Bisfosfoglicerato
    contenido_svg.append(crear_metabolito(
        x=350, y=980,
        nombre="1,3-Bisfosfoglicerato",
        carbonos="3 Carbonos (× 2)",
        detalle="Acil-fosfato de muy alta energía",
        svg_estructura=BISFOSFOGLICERATO_1_3
    ))

    # Reacción 6: Gliceraldehído-3-Fosfato DH (GAPDH) - Se produce NADH
    contenido_svg.append(crear_reaccion(
        x=395, y=1070,
        enzima="GAPDH (Gliceraldehído-3-P DH)",
        ec="EC 1.2.1.12",
        entra_energia="2 NAD⁺ + 2 Pi",
        sale_energia="+ 2 NADH + 2 H⁺",
        es_ganancia=True,
        reversible=True
    ))

    # 7. 3-Fosfoglicerato
    contenido_svg.append(crear_metabolito(
        x=350, y=1160,
        nombre="3-Fosfoglicerato",
        carbonos="3 Carbonos (× 2)",
        detalle="Fosforilación a nivel de sustrato",
        svg_estructura=FOSFOGLICERATO_3
    ))

    # Reacción 7: Fosfoglicerato Quinasa - Ganancia neta de ATP
    contenido_svg.append(crear_reaccion(
        x=395, y=1250,
        enzima="Fosfoglicerato Quinasa",
        ec="EC 2.7.2.3 (Mg²⁺)",
        entra_energia="2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True,
        reversible=True
    ))

    # 8. 2-Fosfoglicerato
    contenido_svg.append(crear_metabolito(
        x=350, y=1340,
        nombre="2-Fosfoglicerato",
        carbonos="3 Carbonos (× 2)",
        detalle="Reordenamiento interno de éster fosfato",
        svg_estructura=FOSFOGLICERATO_2
    ))

    # Reacción 8: Fosfoglicerato Mutasa
    contenido_svg.append(crear_reaccion(
        x=395, y=1430,
        enzima="Fosfoglicerato Mutasa",
        ec="EC 5.4.2.11 (Mg²⁺)",
        reversible=True
    ))

    # 9. Fosfoenolpiruvato (PEP)
    contenido_svg.append(crear_metabolito(
        x=350, y=1520,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 Carbonos (× 2)",
        detalle="Enol-fosfato de altísima energía de hidrólisis",
        svg_estructura=FOSFOENOLPIRUVATO
    ))

    # Reacción 9: Enolasa (Deshidratación)
    contenido_svg.append(crear_reaccion(
        x=395, y=1610,
        enzima="Enolasa",
        ec="EC 4.2.1.11 (Mg²⁺)",
        salida_agua=True,
        reversible=True
    ))

    # 10. Piruvato (Fin de la vía)
    contenido_svg.append(crear_metabolito(
        x=350, y=1700,
        nombre="Piruvato",
        carbonos="3 Carbonos (× 2)",
        detalle="Producto final en citosol (destino mitocondrial)",
        svg_estructura=PIRUVATO
    ))

    # Reacción 10: Piruvato Quinasa (Segunda fosforilación a nivel de sustrato)
    contenido_svg.append(crear_reaccion(
        x=395, y=1790,
        enzima="Piruvato Quinasa",
        ec="EC 2.7.1.40 (K⁺, Mg²⁺)",
        regulacion="⊕ F-1,6-BP | ⊣ ATP, Alanina",
        entra_energia="2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True
    ))

    # Unir todo el código
    html_final = CABECERA_HTML + "\n".join(contenido_svg) + PIE_HTML

    # Escribir el archivo Glucolisis.html
    ruta_salida = os.path.join(os.path.dirname(__file__), "Glucolisis.html")
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(html_final)

    print(f"✅ ¡Ruta Glucolítica completa generada en: {ruta_salida}!")


if __name__ == "__main__":
    main()
