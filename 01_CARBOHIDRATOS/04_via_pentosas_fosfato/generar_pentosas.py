#!/usr/bin/env python3
"""
GENERADOR DE LA VÍA DE LAS PENTOSAS FOSFATO (SVG/HTML)
======================================================
Esta ruta citoplasmática se conecta a la derecha de la Glucosa-6-P en la Glucólisis.
Tiene dos fases:
1. Fase Oxidativa (Irreversible): Genera 2 NADPH + CO2 y convierte hexosas (6C) en pentosas (5C).
2. Fase No Oxidativa (Reversible): Produce Ribosa-5-P para nucleótidos (ADN/ARN) y reconecta con F6P y GAP.
"""

import os
from estructuras_pentosas import (
    GLUCOSA_6_FOSFATO,
    FOSFOGLUCONO_LACTONA_6,
    FOSFOGLUCONATO_6,
    RIBULOSA_5_FOSFATO,
    RIBOSA_5_FOSFATO,
    XILULOSA_5_FOSFATO,
    SEDOHEPTULOSA_7_FOSFATO
)

# -----------------------------------------------------------------------------
# 1. PLANTILLAS BASE DE HTML Y SVG
# -----------------------------------------------------------------------------
CABECERA_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vía de las Pentosas Fosfato - Mapa Metabólico</title>
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
    <svg width="1000" height="1500" viewBox="0 0 1000 1500" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Flecha de flujo metabólico principal (Naranja) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de poder reductor NADPH (Verde esmeralda / azulado) -->
        <marker id="arrowNADPH" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#059669" />
        </marker>
        <!-- Flecha de salida de reactivo o subproducto (Gris pizarra) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <!-- Flecha de agua (Azul) -->
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>
        <!-- Flecha violeta para precursores de nucleótidos -->
        <marker id="arrowPurple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
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
    """Construye el bloque SVG de un metabolito libre."""
    if texto_izquierda:
        pos_estructura = "translate(150, 0)"
        pos_texto = "translate(130, 25)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = "translate(135, 25)"
        alineacion = ''

    return f"""
      <!-- Metabolito: {nombre} -->
      <g transform="translate({x}, {y})">
        <g transform="{pos_estructura}">
          {svg_estructura}
        </g>
        <g transform="{pos_texto}">
          <text x="0" y="0" fill="#0f172a" font-size="17" font-weight="800" {alineacion}>{nombre}</text>
          <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700" {alineacion}>{carbonos}</text>
          <text x="0" y="34" fill="#64748b" font-size="11" {alineacion}>{detalle}</text>
        </g>
      </g>
    """


def crear_reaccion_oxidativa(x, y, enzima, ec="", regulacion="", genera_nadph=False, salida_co2=False, entra_agua=False):
    """Genera la reacción enzimática de la fase oxidativa con sus curvas de NADPH, CO2 y H2O."""
    curvas = ""
    
    # Si produce NADPH
    if genera_nadph:
        curvas += """
        <!-- Entrada de NADP+ -->
        <path d="M -75 8 Q -25 8 -4 18" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="-80" y="11" fill="#475569" font-size="11" font-weight="800" text-anchor="end">NADP⁺</text>
        <!-- Salida de NADPH + H+ -->
        <path d="M -4 24 Q -25 34 -75 34" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowNADPH)"/>
        <text x="-80" y="37" fill="#059669" font-size="11" font-weight="800" text-anchor="end">+ NADPH + H⁺</text>
        """

    # Si libera CO2
    if salida_co2:
        curvas += """
        <!-- Desprendimiento de CO2 -->
        <path d="M -4 38 Q -30 52 -75 52" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="-80" y="55" fill="#475569" font-size="11" font-weight="800" text-anchor="end">+ CO₂ ↑</text>
        """

    # Si entra agua (Lactonasa)
    if entra_agua:
        curvas += """
        <!-- Entrada de H2O -->
        <path d="M -75 14 Q -25 14 -4 24" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-80" y="17" fill="#0284c7" font-size="11" font-weight="800" text-anchor="end">+ H₂O</text>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="26" fill="{color_reg}" font-size="10" font-weight="700">{regulacion}</text>'

    altura_flecha = "58" if salida_co2 else "48"

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="0" y1="0" x2="0" y2="{altura_flecha}" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      {curvas}
      <g transform="translate(18, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">{enzima}</text>
        <text x="0" y="13" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """


# -----------------------------------------------------------------------------
# 3. CONSTRUCCIÓN Y GENERACIÓN DEL ARCHIVO
# -----------------------------------------------------------------------------

def main():
    contenido_svg = []

    # =========================================================================
    # CABECERA VISUAL: TÍTULO Y CONEXIÓN CON GLUCÓLISIS
    # =========================================================================
    contenido_svg.append("""
    <!-- Banner de Encabezado -->
    <g transform="translate(385, 40)">
      <rect x="-180" y="-14" width="360" height="28" rx="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
      <text x="0" y="4" fill="#c2410c" font-size="12" font-weight="800" text-anchor="middle">VÍA DE LAS PENTOSAS FOSFATO (SHUNT HMP)</text>
    </g>
    """)

    # =========================================================================
    # FASE 1: FASE OXIDATIVA (IRREVERSIBLE - GENERADORA DE NADPH)
    # =========================================================================

    # 1. Glucosa-6-Fosfato (Sustrato inicial de la vía)
    contenido_svg.append(crear_metabolito(
        x=340, y=90,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Bifurcación lateral desde la Glucólisis",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # Reacción 1: Glucosa-6-Fosfato Deshidrogenasa (G6PDH) - PASO LIMITANTE
    contenido_svg.append(crear_reaccion_oxidativa(
        x=385, y=200,
        enzima="Glucosa-6-P Deshidrogenasa (G6PDH)",
        ec="EC 1.1.1.49 (Paso Limitante Clave)",
        regulacion="⊣ NADPH | ⊕ NADP⁺, Insulina",
        genera_nadph=True
    ))

    # 2. 6-Fosfoglucono-δ-lactona
    contenido_svg.append(crear_metabolito(
        x=340, y=285,
        nombre="6-Fosfoglucono-δ-Lactona",
        carbonos="6 Carbonos (Lactona cíclica)",
        detalle="Éster intramolecular inestable",
        svg_estructura=FOSFOGLUCONO_LACTONA_6
    ))

    # Reacción 2: 6-Fosfogluconolactonasa
    contenido_svg.append(crear_reaccion_oxidativa(
        x=385, y=390,
        enzima="6-Fosfogluconolactonasa",
        ec="EC 3.1.1.31 (Mg²⁺)",
        entra_agua=True
    ))

    # 3. 6-Fosfogluconato
    contenido_svg.append(crear_metabolito(
        x=340, y=475,
        nombre="6-Fosfogluconato",
        carbonos="6 Carbonos (Cadena lineal)",
        detalle="Ácido carboxílico fosforilado",
        svg_estructura=FOSFOGLUCONATO_6
    ))

    # Reacción 3: 6-Fosfogluconato Deshidrogenasa (Descarboxilación oxidativa)
    contenido_svg.append(crear_reaccion_oxidativa(
        x=385, y=585,
        enzima="6-Fosfogluconato Deshidrogenasa",
        ec="EC 1.1.1.44 (Descarboxilación Oxidativa)",
        genera_nadph=True,
        salida_co2=True
    ))

    # 4. D-Ribulosa-5-Fosfato (Fin de la fase oxidativa)
    contenido_svg.append(crear_metabolito(
        x=340, y=695,
        nombre="D-Ribulosa-5-Fosfato",
        carbonos="5 Carbonos (Pentosa Cetosa)",
        detalle="Punto de ramificación de la fase no oxidativa",
        svg_estructura=RIBULOSA_5_FOSFATO
    ))


    # =========================================================================
    # FASE 2: FASE NO OXIDATIVA (BIFURCACIÓN HACIA RIBOSA-5-P Y XILULOSA-5-P)
    # =========================================================================

    # Ramificación desde Ribulosa-5-P
    contenido_svg.append("""
    <!-- Ramificación dual de la Ribulosa-5-P -->
    <g transform="translate(385, 805)">
      <!-- Rama Izquierda (Epimerasa -> Xilulosa-5-P) -->
      <path d="M -15 0 Q -100 25 -160 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(-150, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Fosfopentosa Epimerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 5.1.3.1 (⇄)</text>
      </g>

      <!-- Rama Derecha (Isomerasa -> Ribosa-5-P) -->
      <path d="M 15 0 Q 100 25 180 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(130, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Fosfopentosa Isomerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 5.3.1.6 (⇄)</text>
      </g>
    </g>
    """)

    # 5a. D-Xilulosa-5-Fosfato (A la izquierda)
    contenido_svg.append(crear_metabolito(
        x=70, y=885,
        nombre="D-Xilulosa-5-P",
        carbonos="5 Carbonos (Epímero C3)",
        detalle="Donador de 2C en Transcetolasa",
        svg_estructura=XILULOSA_5_FOSFATO,
        texto_izquierda=True
    ))

    # 5b. D-Ribosa-5-Fosfato (A la derecha)
    contenido_svg.append(crear_metabolito(
        x=560, y=885,
        nombre="D-Ribosa-5-Fosfato",
        carbonos="5 Carbonos (Pentosa Aldosa)",
        detalle="Precursora de Nucleótidos",
        svg_estructura=RIBOSA_5_FOSFATO
    ))

    # Conexión destacada: Salida hacia Síntesis de Nucleótidos (ADN/ARN/ATP)
    contenido_svg.append("""
    <!-- Salida hacia Síntesis de Nucleótidos -->
    <g transform="translate(730, 990)">
      <path d="M 0 0 L 0 50" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
      <rect x="-80" y="55" width="160" height="34" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
      <text x="0" y="70" fill="#6d28d9" font-size="11" font-weight="800" text-anchor="middle">SÍNTESIS DE NUCLEÓTIDOS</text>
      <text x="0" y="83" fill="#7c3aed" font-size="9" font-weight="600" text-anchor="middle">ATP • GTP • ARN • ADN • PRPP</text>
    </g>
    """)

    # Barajado de carbonos: Transcetolasa y reconexión a Glucólisis
    contenido_svg.append("""
    <!-- Interconversión No Oxidativa (Transcetolasa y Transaldolasa) -->
    <g transform="translate(230, 1020)">
      <rect x="-10" y="0" width="360" height="90" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="170" y="24" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">Transcetolasa (TPP) + Transaldolasa</text>
      <text x="170" y="42" fill="#64748b" font-size="10" text-anchor="middle">Barajado de C5 + C5 ⇄ C3 + C7 ⇄ C6 + C4</text>
      
      <!-- Flechas de retorno a Glucólisis -->
      <path d="M 90 55 L 90 75" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <text x="90" y="88" fill="#c2410c" font-size="10" font-weight="800" text-anchor="middle">→ Fructosa-6-P</text>

      <path d="M 250 55 L 250 75" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <text x="250" y="88" fill="#c2410c" font-size="10" font-weight="800" text-anchor="middle">→ Gliceraldehído-3-P</text>
    </g>

    <!-- Conexión de retorno a la Glucólisis -->
    <g transform="translate(410, 1150)">
      <text x="0" y="0" fill="#ea580c" font-size="12" font-weight="800" text-anchor="middle">↺ Reingreso al eje glucolítico en citosol</text>
    </g>
    """)

    # Unir todo el código
    html_final = CABECERA_HTML + "\n".join(contenido_svg) + PIE_HTML

    # Escribir el archivo Pentosas.html
    ruta_salida = os.path.join(os.path.dirname(__file__), "Pentosas.html")
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(html_final)

    print(f"✅ ¡Vía de las Pentosas Fosfato generada en: {ruta_salida}!")


if __name__ == "__main__":
    main()
