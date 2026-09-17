#!/usr/bin/env python3
"""
GENERADOR DE LA RUTA GLUCOLÍTICA EN SVG/HTML - VERSIÓN PERFECCIONADA
====================================================================
Correcciones visuales aplicadas:
- Orden bioquímico estricto en la Fase 2: Enzima (GAPDH) ANTES del producto (1,3-BPG).
- Zona de Triosas (DHAP / GAP / TPI) con carril exclusivo y sin colisiones de texto.
- Eliminada la flecha suelta; integrado un badge elegante "FASE 2: RENDIMIENTO (× 2)".
- Flechas y metabolitos bajados con espaciado equilibrado y respiración visual.
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
    <svg width="1000" height="2150" viewBox="0 0 1000 2150" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Flecha de flujo metabólico principal (Naranja) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de gasto de energía (Roja) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de salida de producto energético (Gris pizarra) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <!-- Flecha de generación de energía / ganancia (Verde esmeralda) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de salida de agua (Azul) -->
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
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

def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False):
    """
    Construye el bloque SVG de un metabolito libre.
    Si texto_izquierda=True, coloca el bloque de texto a la izquierda de la estructura
    (ideal para DHAP, despejando el carril central).
    """
    if texto_izquierda:
        pos_estructura = "translate(150, 0)"
        pos_texto = "translate(130, 25)"
        alineacion = 'text-anchor="end"'
        x_texto = "0"
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = "translate(135, 25)"
        alineacion = ''
        x_texto = "0"

    return f"""
      <!-- Metabolito: {nombre} -->
      <g transform="translate({x}, {y})">
        <g transform="{pos_estructura}">
          {svg_estructura}
        </g>
        <g transform="{pos_texto}">
          <text x="{x_texto}" y="0" fill="#0f172a" font-size="17" font-weight="800" {alineacion}>{nombre}</text>
          <text x="{x_texto}" y="18" fill="#ea580c" font-size="12" font-weight="700" {alineacion}>{carbonos}</text>
          <text x="{x_texto}" y="34" fill="#64748b" font-size="11" {alineacion}>{detalle}</text>
        </g>
      </g>
    """


def crear_reaccion(x, y, enzima, ec="", regulacion="", entra_energia="", sale_energia="", 
                   reversible=False, es_ganancia=False, salida_agua=False):
    """Genera el bloque SVG de una reacción con proporciones compactas y sin choques."""
    curvas_energia = ""
    
    # 1. Entrada de energía o reactivo (a la izquierda)
    if entra_energia:
        color_entrada = "#dc2626" if not es_ganancia else "#475569"
        marcador_entrada = "url(#arrowRed)" if not es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -75 8 Q -25 8 -4 18" fill="none" stroke="{color_entrada}" stroke-width="1.8" marker-end="{marcador_entrada}"/>
        <text x="-80" y="11" fill="{color_entrada}" font-size="11" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
        
    # 2. Salida de producto energético (a la izquierda)
    if sale_energia:
        color_salida = "#059669" if es_ganancia else "#475569"
        marcador_salida = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -4 24 Q -25 34 -75 34" fill="none" stroke="{color_salida}" stroke-width="1.8" marker-end="{marcador_salida}"/>
        <text x="-80" y="37" fill="{color_salida}" font-size="11" font-weight="800" text-anchor="end">{sale_energia}</text>
        """

    # 3. Salida de agua (para Enolasa)
    if salida_agua:
        curvas_energia += """
        <path d="M -4 24 Q -25 34 -70 34" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="{marcador_blue}"/>
        <text x="-75" y="37" fill="#0284c7" font-size="11" font-weight="800" text-anchor="end">- 2 H₂O</text>
        """

    # 4. Flecha principal (48 px de largo)
    if reversible:
        flecha_central = """
        <line x1="-3" y1="0" x2="-3" y2="48" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        <line x1="3" y1="48" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        """
    else:
        flecha_central = """
        <line x1="0" y1="0" x2="0" y2="48" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="26" fill="{color_reg}" font-size="10" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha_central}
      {curvas_energia}
      <g transform="translate(18, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">{enzima}</text>
        <text x="0" y="13" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """


def crear_zona_triosas():
    """Genera la bifurcación limpia de la Aldolasa, la conexión TPI despejada y la transición a la Fase 2."""
    return """
    <!-- 1. Bifurcación Aldolasa (desde F-1,6-BP hacia DHAP y GAP) -->
    <g transform="translate(385, 765)">
      <!-- Flecha suave hacia DHAP (izquierda) -->
      <path d="M -15 0 Q -120 30 -160 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <!-- Flecha suave hacia GAP (derecha) -->
      <path d="M 15 0 Q 120 30 180 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      
      <!-- Nombre de la Aldolasa en el centro despejado -->
      <g transform="translate(0, 26)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800" text-anchor="middle">Aldolasa</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 4.1.2.13 (Reversible)</text>
      </g>
    </g>

    <!-- 2. Triosa Fosfato Isomerasa (TPI): Conexión horizontal libre entre DHAP y GAP -->
    <g transform="translate(420, 895)">
      <line x1="-120" y1="-3" x2="110" y2="-3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="110" y1="3" x2="-120" y2="3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <text x="-5" y="-12" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">Triosa Fosfato Isomerasa (TPI)</text>
      <text x="-5" y="18" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1 (⇄)</text>
    </g>

    <!-- 3. Entrada fluida a la Fase 2 (Curva desde GAP hacia el eje central) -->
    <path d="M 600 965 Q 600 1000 385 1020" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    
    <!-- Badge elegante que anuncia la Fase 2 (sin elementos volando) -->
    <g transform="translate(285, 1005)">
      <rect x="-95" y="-12" width="190" height="24" rx="12" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
      <text x="0" y="4" fill="#c2410c" font-size="11" font-weight="800" text-anchor="middle">FASE 2: RENDIMIENTO (× 2)</text>
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
        x=340, y=70,
        nombre="D-Glucosa",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Sustrato inicial de la glucólisis",
        svg_estructura=GLUCOSA
    ))

    # Reacción 1: Hexoquinasa
    contenido_svg.append(crear_reaccion(
        x=385, y=185,
        enzima="Hexoquinasa",
        ec="EC 2.7.1.1 (Mg²⁺)",
        regulacion="⊣ Inhibida por G-6-P",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 2. Glucosa-6-Fosfato
    contenido_svg.append(crear_metabolito(
        x=340, y=270,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Fosforilada)",
        detalle="Encrucijada: Vía Pentosas / Glucógeno",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # Reacción 2: Fosfohexosa Isomerasa
    contenido_svg.append(crear_reaccion(
        x=385, y=375,
        enzima="Fosfohexosa Isomerasa",
        ec="EC 5.3.1.9 (Mg²⁺)",
        reversible=True
    ))

    # 3. Fructosa-6-Fosfato
    contenido_svg.append(crear_metabolito(
        x=340, y=460,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Furanosa)",
        detalle="Isomerización aldosa → cetosa",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # Reacción 3: Fosfofructoquinasa-1 (Paso Limitante Clave)
    contenido_svg.append(crear_reaccion(
        x=385, y=565,
        enzima="Fosfofructoquinasa-1 (PFK-1)",
        ec="EC 2.7.1.11 (Mg²⁺)",
        regulacion="⊕ AMP, F-2,6-BP | ⊣ ATP, Citrato",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 4. Fructosa-1,6-Bisfosfato
    contenido_svg.append(crear_metabolito(
        x=340, y=655,
        nombre="Fructosa-1,6-Bisfosfato",
        carbonos="6 Carbonos (Doble fosfato)",
        detalle="Molécula comprometida a la lisis",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO
    ))

    # Zona de Triosas: Aldolasa + TPI + Badge Fase 2
    contenido_svg.append(crear_zona_triosas())

    # 5a. Dihidroxiacetona Fosfato (DHAP) - Con texto a la izquierda para dejar libre el centro
    contenido_svg.append(crear_metabolito(
        x=70, y=845,
        nombre="Dihidroxiacetona-P",
        carbonos="3 Carbonos (Cetosa)",
        detalle="Interconvertible hacia GAP",
        svg_estructura=DIHIDROXIACETONA_FOSFATO,
        texto_izquierda=True
    ))

    # 5b. Gliceraldehído-3-Fosfato (GAP) - A la derecha
    contenido_svg.append(crear_metabolito(
        x=560, y=845,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Aldosa)",
        detalle="Sustrato activo que continúa",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))


    # ================= FASE 2: RENDIMIENTO ENERGÉTICO (x2) =================

    # Reacción 6: Gliceraldehído-3-P DH (GAPDH) - Se produce NADH ANTES del 1,3-BPG
    contenido_svg.append(crear_reaccion(
        x=385, y=1045,
        enzima="GAPDH (Gliceraldehído-3-P DH)",
        ec="EC 1.2.1.12",
        entra_energia="2 NAD⁺ + 2 Pi",
        sale_energia="+ 2 NADH + 2 H⁺",
        es_ganancia=True,
        reversible=True
    ))

    # 6. 1,3-Bisfosfoglicerato (Producto de GAPDH)
    contenido_svg.append(crear_metabolito(
        x=340, y=1140,
        nombre="1,3-Bisfosfoglicerato",
        carbonos="3 Carbonos (× 2)",
        detalle="Acil-fosfato de muy alta energía",
        svg_estructura=BISFOSFOGLICERATO_1_3
    ))

    # Reacción 7: Fosfoglicerato Quinasa - Ganancia neta de ATP
    contenido_svg.append(crear_reaccion(
        x=385, y=1255,
        enzima="Fosfoglicerato Quinasa",
        ec="EC 2.7.2.3 (Mg²⁺)",
        entra_energia="2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True,
        reversible=True
    ))

    # 7. 3-Fosfoglicerato
    contenido_svg.append(crear_metabolito(
        x=340, y=1345,
        nombre="3-Fosfoglicerato",
        carbonos="3 Carbonos (× 2)",
        detalle="Fosforilación a nivel de sustrato",
        svg_estructura=FOSFOGLICERATO_3
    ))

    # Reacción 8: Fosfoglicerato Mutasa
    contenido_svg.append(crear_reaccion(
        x=385, y=1455,
        enzima="Fosfoglicerato Mutasa",
        ec="EC 5.4.2.11 (Mg²⁺)",
        reversible=True
    ))

    # 8. 2-Fosfoglicerato
    contenido_svg.append(crear_metabolito(
        x=340, y=1545,
        nombre="2-Fosfoglicerato",
        carbonos="3 Carbonos (× 2)",
        detalle="Reordenamiento interno de fosfato",
        svg_estructura=FOSFOGLICERATO_2
    ))

    # Reacción 9: Enolasa (Deshidratación)
    contenido_svg.append(crear_reaccion(
        x=385, y=1655,
        enzima="Enolasa",
        ec="EC 4.2.1.11 (Mg²⁺)",
        salida_agua=True,
        reversible=True
    ))

    # 9. Fosfoenolpiruvato (PEP)
    contenido_svg.append(crear_metabolito(
        x=340, y=1745,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 Carbonos (× 2)",
        detalle="Enol-fosfato de altísima energía",
        svg_estructura=FOSFOENOLPIRUVATO
    ))

    # Reacción 10: Piruvato Quinasa (Segunda fosforilación a nivel de sustrato)
    contenido_svg.append(crear_reaccion(
        x=385, y=1855,
        enzima="Piruvato Quinasa",
        ec="EC 2.7.1.40 (K⁺, Mg²⁺)",
        regulacion="⊕ F-1,6-BP | ⊣ ATP, Alanina",
        entra_energia="2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True
    ))

    # 10. Piruvato (Fin de la vía)
    contenido_svg.append(crear_metabolito(
        x=340, y=1945,
        nombre="Piruvato",
        carbonos="3 Carbonos (× 2)",
        detalle="Producto final citosólico → Mitocondria",
        svg_estructura=PIRUVATO
    ))

    # Unir todo el código
    html_final = CABECERA_HTML + "\n".join(contenido_svg) + PIE_HTML

    # Escribir el archivo Glucolisis.html
    ruta_salida = os.path.join(os.path.dirname(__file__), "Glucolisis.html")
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(html_final)

    print(f"✅ ¡Ruta Glucolítica ordenada y generada en: {ruta_salida}!")


if __name__ == "__main__":
    main()
