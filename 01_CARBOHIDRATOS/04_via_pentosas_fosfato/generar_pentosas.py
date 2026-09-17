#!/usr/bin/env python3
"""
GENERADOR DE LA VÍA DE LAS PENTOSAS FOSFATO CON CITOSOL BIOLÓGICO REAL
=====================================================================
- Entorno de Citosol celular auténtico (textura acuosa, citoesqueleto, ribosomas y vesículas).
- Cero amontonamientos: Espaciado ampliado específicamente para moléculas lineales altas (6-Fosfogluconato y Ribulosa-5-P).
- Ramificación no oxidativa amplia y limpia (Ribosa-5-P para nucleótidos y Xilulosa-5-P).
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
  <title>Vía de las Pentosas Fosfato en Citosol</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', sans-serif;
      background: #e2e8f0;
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
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
      overflow: hidden;
    }
    svg { display: block; width: 100%; height: auto; }
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="1000" height="1520" viewBox="0 0 1000 1520" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Flecha de flujo metabólico principal (Naranja) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de poder reductor NADPH (Verde esmeralda) -->
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

        <!-- Gradiente suave de citosol celular -->
        <linearGradient id="gradCitosolPentosas" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
          <stop offset="20%" stop-color="#f0fdf4" stop-opacity="0.75" />
          <stop offset="60%" stop-color="#f8fafc" stop-opacity="0.6" />
          <stop offset="100%" stop-color="#f0fdf4" stop-opacity="0.8" />
        </linearGradient>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""


# -----------------------------------------------------------------------------
# 2. CAPA DE DIBUJO DEL CITOSOL PARA PENTOSAS
# -----------------------------------------------------------------------------
def generar_citosol_pentosas_svg(ancho=1000, alto=1520):
    """Genera el dibujo anatómico del citosol sin carteles de texto."""
    return f"""
    <!-- Fondo acuoso citosólico biológico -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#gradCitosolPentosas)" />

    <!-- Filamentos sutiles de citoesqueleto celular cruzando el citoplasma -->
    <g opacity="0.32" stroke="#94a3b8" fill="none">
      <path d="M 30 180 Q 300 120 600 190 T 970 160" stroke-width="1.5" stroke-dasharray="8 6" />
      <path d="M 50 380 Q 350 440 650 390 T 960 410" stroke-width="1.4" stroke-dasharray="6 6" />
      <path d="M 40 680 Q 280 620 580 690 T 950 660" stroke-width="1.5" stroke-dasharray="8 5" />
      <path d="M 60 980 Q 340 1040 620 990 T 970 1010" stroke-width="1.6" stroke-dasharray="7 7" />
      <path d="M 30 1260 Q 320 1200 640 1270 T 960 1230" stroke-width="1.5" stroke-dasharray="8 6" />
    </g>

    <!-- Polirribosomas celulares flotando libres -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="120" cy="140" r="2.5"/><circle cx="126" cy="142" r="2"/><circle cx="124" cy="148" r="2.3"/>
      <circle cx="860" cy="240" r="2.5"/><circle cx="867" cy="242" r="2"/><circle cx="864" cy="248" r="2.3"/>
      <circle cx="130" cy="560" r="2.5"/><circle cx="136" cy="563" r="2.2"/><circle cx="133" cy="568" r="2"/>
      <circle cx="880" cy="780" r="2.5"/><circle cx="887" cy="783" r="2"/><circle cx="883" cy="788" r="2.2"/>
      <circle cx="140" cy="1120" r="2.5"/><circle cx="146" cy="1122" r="2"/><circle cx="143" cy="1128" r="2.3"/>
    </g>

    <!-- Vesículas citosólicas translúcidas en los márgenes laterales -->
    <g opacity="0.3">
      <circle cx="130" cy="320" r="20" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="880" cy="620" r="24" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
    </g>

    <!-- Indicador de conexión lateral de entrada (proviene de Glucólisis a la izquierda) -->
    <g transform="translate(60, 115)">
      <path d="M 0 0 L 260 0" fill="none" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#arrowFlow)"/>
      <text x="10" y="-10" fill="#c2410c" font-size="11" font-weight="800">← Bifurcación lateral desde la Glucólisis</text>
    </g>
    """


# -----------------------------------------------------------------------------
# 3. FUNCIONES GENERADORAS DE ELEMENTOS METABÓLICOS
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
    """Genera la reacción enzimática de la fase oxidativa con proporciones compactas sin choques."""
    curvas = ""
    
    if genera_nadph:
        curvas += """
        <path d="M -75 8 Q -25 8 -4 18" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="-80" y="11" fill="#475569" font-size="11" font-weight="800" text-anchor="end">NADP⁺</text>
        <path d="M -4 24 Q -25 34 -75 34" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowNADPH)"/>
        <text x="-80" y="37" fill="#059669" font-size="11" font-weight="800" text-anchor="end">+ NADPH + H⁺</text>
        """

    if salida_co2:
        curvas += """
        <path d="M -4 38 Q -30 50 -75 50" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="-80" y="53" fill="#475569" font-size="11" font-weight="800" text-anchor="end">+ CO₂ ↑</text>
        """

    if entra_agua:
        curvas += """
        <path d="M -75 12 Q -25 12 -4 22" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-80" y="15" fill="#0284c7" font-size="11" font-weight="800" text-anchor="end">+ H₂O</text>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="26" fill="{color_reg}" font-size="10" font-weight="700">{regulacion}</text>'

    altura_flecha = "52" if salida_co2 else "46"

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
# 4. CONSTRUCCIÓN Y GENERACIÓN DEL ARCHIVO
# -----------------------------------------------------------------------------
def main():
    contenido_svg = []

    # =========================================================================
    # CAPA DE FONDO: CITOSOL BIOLÓGICO CELULAR
    # =========================================================================
    contenido_svg.append(generar_citosol_pentosas_svg(ancho=1000, alto=1520))

    # =========================================================================
    # FASE 1: FASE OXIDATIVA (ESPACIADO HOLGADO)
    # =========================================================================

    # 1. Glucosa-6-Fosfato (Sustrato puente que entra desde la izquierda)
    contenido_svg.append(crear_metabolito(
        x=340, y=80,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Entrada al Shunt de Pentosas",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # Reacción 1: G6PDH (Paso Limitante Clave)
    contenido_svg.append(crear_reaccion_oxidativa(
        x=385, y=190,
        enzima="Glucosa-6-P Deshidrogenasa (G6PDH)",
        ec="EC 1.1.1.49 (Paso Limitante Clave)",
        regulacion="⊣ NADPH | ⊕ NADP⁺, Insulina",
        genera_nadph=True
    ))

    # 2. 6-Fosfoglucono-δ-lactona
    contenido_svg.append(crear_metabolito(
        x=340, y=275,
        nombre="6-Fosfoglucono-δ-Lactona",
        carbonos="6 Carbonos (Lactona)",
        detalle="Éster intramolecular hidrolizable",
        svg_estructura=FOSFOGLUCONO_LACTONA_6
    ))

    # Reacción 2: Lactonasa (+ H2O)
    contenido_svg.append(crear_reaccion_oxidativa(
        x=385, y=380,
        enzima="6-Fosfogluconolactonasa",
        ec="EC 3.1.1.31 (Mg²⁺)",
        entra_agua=True
    ))

    # 3. 6-Fosfogluconato (Cadena lineal alta: 135 px de altura)
    # Se ubica en y = 460 para dejar 35 px de margen arriba
    contenido_svg.append(crear_metabolito(
        x=340, y=460,
        nombre="6-Fosfogluconato",
        carbonos="6 Carbonos (Cadena lineal)",
        detalle="Ácido descarboxilable",
        svg_estructura=FOSFOGLUCONATO_6
    ))

    # Reacción 3: 6-Fosfogluconato DH (Descarboxilación Oxidativa)
    # Colocada en y = 640 (¡dejando 45 px de aire limpio con el fosfato de arriba!)
    contenido_svg.append(crear_reaccion_oxidativa(
        x=385, y=640,
        enzima="6-Fosfogluconato Deshidrogenasa",
        ec="EC 1.1.1.44 (Descarboxilación Oxidativa)",
        genera_nadph=True,
        salida_co2=True
    ))

    # 4. D-Ribulosa-5-Fosfato (Fin de la fase oxidativa)
    # Colocada en y = 735 (45 px de aire limpio debajo de la flecha)
    contenido_svg.append(crear_metabolito(
        x=340, y=735,
        nombre="D-Ribulosa-5-Fosfato",
        carbonos="5 Carbonos (Pentosa Cetosa)",
        detalle="Cruce a la fase no oxidativa",
        svg_estructura=RIBULOSA_5_FOSFATO
    ))


    # =========================================================================
    # FASE 2: FASE NO OXIDATIVA (ESPACIO AMPLIO SIN CHOQUES)
    # =========================================================================

    # Ramificación amplia desde Ribulosa-5-P hacia los lados
    contenido_svg.append("""
    <!-- Ramificación amplia de la Ribulosa-5-P -->
    <g transform="translate(385, 895)">
      <!-- Rama Izquierda (Epimerasa -> Xilulosa-5-P) -->
      <path d="M -20 0 Q -110 30 -160 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(-160, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Fosfopentosa Epimerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 5.1.3.1 (⇄)</text>
      </g>

      <!-- Rama Derecha (Isomerasa -> Ribosa-5-P) -->
      <path d="M 20 0 Q 110 30 180 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(130, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Fosfopentosa Isomerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 5.3.1.6 (⇄)</text>
      </g>
    </g>
    """)

    # 5a. D-Xilulosa-5-Fosfato (A la izquierda, con texto a la izquierda)
    contenido_svg.append(crear_metabolito(
        x=70, y=980,
        nombre="D-Xilulosa-5-P",
        carbonos="5 Carbonos (Epímero C3)",
        detalle="Donador de 2C en Transcetolasa",
        svg_estructura=XILULOSA_5_FOSFATO,
        texto_izquierda=True
    ))

    # 5b. D-Ribosa-5-Fosfato (A la derecha)
    contenido_svg.append(crear_metabolito(
        x=560, y=980,
        nombre="D-Ribosa-5-Fosfato",
        carbonos="5 Carbonos (Pentosa Aldosa)",
        detalle="Precursora de Nucleótidos",
        svg_estructura=RIBOSA_5_FOSFATO
    ))

    # Salida destacada hacia Síntesis de Nucleótidos (ARN/ADN/ATP)
    contenido_svg.append("""
    <!-- Salida hacia Síntesis de Nucleótidos -->
    <g transform="translate(730, 1085)">
      <path d="M 0 0 L 0 45" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
      <rect x="-85" y="50" width="170" height="36" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
      <text x="0" y="66" fill="#6d28d9" font-size="11" font-weight="800" text-anchor="middle">SÍNTESIS DE NUCLEÓTIDOS</text>
      <text x="0" y="80" fill="#7c3aed" font-size="9" font-weight="600" text-anchor="middle">ATP • GTP • ARN • ADN • PRPP</text>
    </g>
    """)

    # Bloque de barajado no oxidativo (Transcetolasa / Transaldolasa)
    contenido_svg.append("""
    <!-- Interconversión No Oxidativa -->
    <g transform="translate(190, 1170)">
      <rect x="0" y="0" width="400" height="85" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.04))"/>
      <text x="200" y="22" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">Transcetolasa (TPP) + Transaldolasa</text>
      <text x="200" y="38" fill="#64748b" font-size="10" text-anchor="middle">Barajado: C5 + C5 ⇄ C3 + C7 ⇄ C6 + C4 ⇄ C6 + C3</text>
      
      <!-- Flechas de reingreso al eje glucolítico -->
      <path d="M 100 50 L 100 70" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <text x="100" y="82" fill="#c2410c" font-size="10" font-weight="800" text-anchor="middle">→ Fructosa-6-P</text>

      <path d="M 300 50 L 300 70" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <text x="300" y="82" fill="#c2410c" font-size="10" font-weight="800" text-anchor="middle">→ Gliceraldehído-3-P</text>
    </g>

    <!-- Conexión de retorno al eje glucolítico citosólico -->
    <g transform="translate(390, 1295)">
      <path d="M 0 0 Q -100 30 -250 30" fill="none" stroke="#ea580c" stroke-width="2.2" stroke-dasharray="5 4" marker-end="url(#arrowFlow)"/>
      <text x="-120" y="22" fill="#ea580c" font-size="11" font-weight="800" text-anchor="middle">↺ Retorno al eje principal de la Glucólisis</text>
    </g>
    """)

    # Unir todo el código
    html_final = CABECERA_HTML + "\n".join(contenido_svg) + PIE_HTML

    # Escribir el archivo Pentosas.html
    ruta_salida = os.path.join(os.path.dirname(__file__), "Pentosas.html")
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(html_final)

    print(f"✅ ¡Vía de las Pentosas Fosfato espaciosa y con citosol generada en: {ruta_salida}!")


if __name__ == "__main__":
    main()
