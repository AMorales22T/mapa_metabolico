#!/usr/bin/env python3
"""
GENERADOR DE LA VÍA DE LAS PENTOSAS FOSFATO COMPLETA (SVG/HTML)
===============================================================
Correcciones visuales aplicadas:
1. Entrada lateral rediseñada con holgura: ya no toca el grupo fosfato de la G6P.
2. Enzima Fosfopentosa Epimerasa recolocada para no montarse sobre la flecha curva.
3. Caja morada de Síntesis de Nucleótidos reubicada lateralmente a la derecha de la Ribosa-5-P
   (despejando totalmente la Transcetolasa 1).
"""

import os
from estructuras_pentosas import (
    GLUCOSA_6_FOSFATO,
    FOSFOGLUCONO_LACTONA_6,
    FOSFOGLUCONATO_6,
    RIBULOSA_5_FOSFATO,
    RIBOSA_5_FOSFATO,
    XILULOSA_5_FOSFATO,
    SEDOHEPTULOSA_7_FOSFATO,
    ERITROSA_4_FOSFATO,
    GLICERALDEHIDO_3_FOSFATO,
    FRUCTOSA_6_FOSFATO
)

# -----------------------------------------------------------------------------
# 1. PLANTILLAS BASE DE HTML Y SVG
# -----------------------------------------------------------------------------
CABECERA_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vía de las Pentosas Fosfato - Ruta Completa en Citosol</title>
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
    <svg width="1000" height="2150" viewBox="0 0 1000 2150" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Marcadores de flechas -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <marker id="arrowNADPH" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#059669" />
        </marker>
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>
        <marker id="arrowPurple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
        </marker>

        <!-- Fondo del Citosol Celular -->
        <linearGradient id="gradCitosolPentosas" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
          <stop offset="15%" stop-color="#f0fdf4" stop-opacity="0.7" />
          <stop offset="60%" stop-color="#f8fafc" stop-opacity="0.5" />
          <stop offset="100%" stop-color="#f0fdf4" stop-opacity="0.7" />
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
# 2. CAPA DE ENTORNO CITOSÓLICO BIOLÓGICO
# -----------------------------------------------------------------------------
def generar_citosol_pentosas_svg(ancho=1000, alto=2150):
    """Genera el dibujo anatómico del citosol celular orgánico."""
    return f"""
    <!-- Fondo acuoso citoplasmático -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#gradCitosolPentosas)" />

    <!-- Citoesqueleto: filamentos sutiles atravesando el espacio celular -->
    <g opacity="0.3" stroke="#94a3b8" fill="none">
      <path d="M 30 180 Q 300 120 600 190 T 970 160" stroke-width="1.5" stroke-dasharray="8 6" />
      <path d="M 50 380 Q 350 440 650 390 T 960 410" stroke-width="1.4" stroke-dasharray="6 6" />
      <path d="M 40 680 Q 280 620 580 690 T 950 660" stroke-width="1.5" stroke-dasharray="8 5" />
      <path d="M 60 1050 Q 340 1110 620 1060 T 970 1080" stroke-width="1.6" stroke-dasharray="7 7" />
      <path d="M 40 1420 Q 320 1360 640 1430 T 960 1390" stroke-width="1.5" stroke-dasharray="8 6" />
      <path d="M 50 1780 Q 350 1840 680 1790 T 970 1810" stroke-width="1.4" stroke-dasharray="6 6" />
    </g>

    <!-- Polirribosomas celulares flotantes -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="120" cy="140" r="2.5"/><circle cx="126" cy="142" r="2"/><circle cx="124" cy="148" r="2.3"/>
      <circle cx="860" cy="240" r="2.5"/><circle cx="867" cy="242" r="2"/><circle cx="864" cy="248" r="2.3"/>
      <circle cx="130" cy="560" r="2.5"/><circle cx="136" cy="563" r="2.2"/><circle cx="133" cy="568" r="2"/>
      <circle cx="880" cy="920" r="2.5"/><circle cx="887" cy="923" r="2"/><circle cx="883" cy="928" r="2.2"/>
      <circle cx="130" cy="1320" r="2.5"/><circle cx="136" cy="1323" r="2.2"/><circle cx="133" cy="1328" r="2"/>
      <circle cx="870" cy="1680" r="2.5"/><circle cx="877" cy="1683" r="2"/><circle cx="873" cy="1688" r="2.2"/>
    </g>

    <!-- Vesículas citosólicas translúcidas -->
    <g opacity="0.3">
      <circle cx="130" cy="320" r="20" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="880" cy="620" r="24" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="120" cy="1580" r="22" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
    </g>

    <!-- Entrada lateral rediseñada: termina con 60 px de aire antes de la G6P -->
    <g transform="translate(60, 60)">
      <path d="M 0 0 L 190 0 Q 230 0 250 25" fill="none" stroke="#ea580c" stroke-width="2.2" stroke-dasharray="5 4" marker-end="url(#arrowFlow)"/>
      <text x="5" y="-10" fill="#c2410c" font-size="11" font-weight="800">← Entrada lateral desde Glucosa-6-P (Glucólisis)</text>
    </g>
    """


# -----------------------------------------------------------------------------
# 3. FUNCIONES GENERADORAS DE ELEMENTOS
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
    """Genera la reacción enzimática de la fase oxidativa con proporciones compactas."""
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


def crear_paso_no_oxidativo(x, y, enzima, ec, sustratos_txt, productos_txt):
    """Genera un nodo de reacción de transferencia (Transcetolasa / Transaldolasa)."""
    return f"""
    <!-- Reacción de Transferencia: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="-3" y1="0" x2="-3" y2="45" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="45" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>

      <g transform="translate(18, 10)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        <text x="0" y="28" fill="#c2410c" font-size="10" font-weight="700">{sustratos_txt} ⇄ {productos_txt}</text>
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
    contenido_svg.append(generar_citosol_pentosas_svg(ancho=1000, alto=2150))

    # =========================================================================
    # FASE 1: FASE OXIDATIVA
    # =========================================================================

    # 1. Glucosa-6-Fosfato (Despejada de la flecha de entrada)
    contenido_svg.append(crear_metabolito(
        x=340, y=90,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Entrada al Shunt de Pentosas",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # Reacción 1: G6PDH
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
        carbonos="6 Carbonos (Lactona)",
        detalle="Éster intramolecular hidrolizable",
        svg_estructura=FOSFOGLUCONO_LACTONA_6
    ))

    # Reacción 2: Lactonasa (+ H2O)
    contenido_svg.append(crear_reaccion_oxidativa(
        x=385, y=390,
        enzima="6-Fosfogluconolactonasa",
        ec="EC 3.1.1.31 (Mg²⁺)",
        entra_agua=True
    ))

    # 3. 6-Fosfogluconato (Cadena lineal de 135 px de altura)
    contenido_svg.append(crear_metabolito(
        x=340, y=470,
        nombre="6-Fosfogluconato",
        carbonos="6 Carbonos (Cadena lineal)",
        detalle="Ácido descarboxilable",
        svg_estructura=FOSFOGLUCONATO_6
    ))

    # Reacción 3: 6-Fosfogluconato DH (Descarboxilación Oxidativa)
    # Ubicada en y = 650 (50 px de aire libre con el fosfato de arriba)
    contenido_svg.append(crear_reaccion_oxidativa(
        x=385, y=650,
        enzima="6-Fosfogluconato Deshidrogenasa",
        ec="EC 1.1.1.44 (Descarboxilación)",
        genera_nadph=True,
        salida_co2=True
    ))

    # 4. D-Ribulosa-5-Fosfato (Fin de la fase oxidativa)
    contenido_svg.append(crear_metabolito(
        x=340, y=745,
        nombre="D-Ribulosa-5-Fosfato",
        carbonos="5 Carbonos (Pentosa Cetosa)",
        detalle="Cruce a la fase no oxidativa",
        svg_estructura=RIBULOSA_5_FOSFATO
    ))


    # =========================================================================
    # FASE 2: FASE NO OXIDATIVA
    # =========================================================================

    # Ramificación amplia desde Ribulosa-5-P con textos despejados
    contenido_svg.append("""
    <!-- Ramificación amplia de la Ribulosa-5-P (sin solapamiento de textos) -->
    <g transform="translate(385, 905)">
      <!-- Rama Izquierda (Epimerasa -> Xilulosa-5-P) -->
      <path d="M -20 0 Q -110 30 -160 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <!-- Texto de Epimerasa a la izquierda con text-anchor='end' para no pisar la curva -->
      <g transform="translate(-175, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800" text-anchor="end">Fosfopentosa Epimerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 5.1.3.1 (⇄)</text>
      </g>

      <!-- Rama Derecha (Isomerasa -> Ribosa-5-P) -->
      <path d="M 20 0 Q 110 30 180 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <!-- Texto de Isomerasa a la derecha sin pisar la curva -->
      <g transform="translate(175, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Fosfopentosa Isomerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 5.3.1.6 (⇄)</text>
      </g>
    </g>
    """)

    # 5a. D-Xilulosa-5-Fosfato (A la izquierda)
    contenido_svg.append(crear_metabolito(
        x=70, y=990,
        nombre="D-Xilulosa-5-P",
        carbonos="5 Carbonos (Epímero C3)",
        detalle="Donador de 2C (TPP)",
        svg_estructura=XILULOSA_5_FOSFATO,
        texto_izquierda=True
    ))

    # 5b. D-Ribosa-5-Fosfato (A la derecha)
    contenido_svg.append(crear_metabolito(
        x=560, y=990,
        nombre="D-Ribosa-5-P",
        carbonos="5 Carbonos (Pentosa Aldosa)",
        detalle="Precursora de Nucleótidos",
        svg_estructura=RIBOSA_5_FOSFATO
    ))

    # SALIDA LATERAL DERECHA: SÍNTESIS DE NUCLEÓTIDOS (Completamente a la derecha, despejando la Transcetolasa)
    contenido_svg.append("""
    <!-- Salida Lateral hacia Síntesis de Nucleótidos (a la derecha de Ribosa-5-P) -->
    <g transform="translate(710, 1015)">
      <path d="M 0 0 L 45 0" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
      <g transform="translate(55, -18)">
        <rect x="0" y="0" width="180" height="38" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
        <text x="90" y="16" fill="#6d28d9" font-size="10" font-weight="800" text-anchor="middle">SÍNTESIS DE NUCLEÓTIDOS</text>
        <text x="90" y="29" fill="#7c3aed" font-size="9" font-weight="600" text-anchor="middle">ATP • GTP • ARN • ADN • PRPP</text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # PASO 1 NO OXIDATIVO: TRANSCETOLASA 1 (X5P + R5P ⇄ S7P + GAP)
    # Totalmente libre y sin colisiones en Y = 1140
    # -------------------------------------------------------------------------
    contenido_svg.append(crear_paso_no_oxidativo(
        x=385, y=1140,
        enzima="Transcetolasa (TK1)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Ribosa-5-P (5C)",
        productos_txt="GAP (3C) + Sedoheptulosa-7-P (7C)"
    ))

    # Productos del Paso 1:
    # Sedoheptulosa-7-P (7C) a la izquierda
    contenido_svg.append(crear_metabolito(
        x=70, y=1220,
        nombre="Sedoheptulosa-7-P",
        carbonos="7 Carbonos (Cetosa)",
        detalle="Intermediario de 7C",
        svg_estructura=SEDOHEPTULOSA_7_FOSFATO,
        texto_izquierda=True
    ))

    # Gliceraldehído-3-P (3C) a la derecha
    contenido_svg.append(crear_metabolito(
        x=560, y=1220,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="Intermediario transferible",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))

    # -------------------------------------------------------------------------
    # PASO 2 NO OXIDATIVO: TRANSALDOLASA (S7P + GAP ⇄ F6P + E4P)
    # -------------------------------------------------------------------------
    contenido_svg.append(crear_paso_no_oxidativo(
        x=385, y=1380,
        enzima="Transaldolasa (TA)",
        ec="EC 2.2.1.2 (Base de Schiff con Lisina)",
        sustratos_txt="Sedoheptulosa-7-P (7C) + GAP (3C)",
        productos_txt="Fructosa-6-P (6C) + Eritrosa-4-P (4C)"
    ))

    # Productos del Paso 2:
    # Eritrosa-4-P (4C) a la izquierda
    contenido_svg.append(crear_metabolito(
        x=70, y=1460,
        nombre="D-Eritrosa-4-P",
        carbonos="4 Carbonos (Tetrosa)",
        detalle="Aceptor para segunda transcetolasa",
        svg_estructura=ERITROSA_4_FOSFATO,
        texto_izquierda=True
    ))

    # Fructosa-6-P (6C) a la derecha (¡Primer reingreso a Glucólisis!)
    contenido_svg.append(crear_metabolito(
        x=560, y=1460,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Furanosa)",
        detalle="→ Reingreso al eje glucolítico",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # -------------------------------------------------------------------------
    # PASO 3 NO OXIDATIVO: TRANSCETOLASA 2 (X5P + E4P ⇄ F6P + GAP)
    # -------------------------------------------------------------------------
    contenido_svg.append(crear_paso_no_oxidativo(
        x=385, y=1620,
        enzima="Transcetolasa (TK2)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="2ª Xilulosa-5-P (5C) + Eritrosa-4-P (4C)",
        productos_txt="Fructosa-6-P (6C) + GAP (3C)"
    ))

    # Productos finales del Paso 3 (Reingreso total a Glucólisis):
    # Segunda Fructosa-6-P a la izquierda
    contenido_svg.append(crear_metabolito(
        x=70, y=1700,
        nombre="Fructosa-6-Fosfato (2ª)",
        carbonos="6 Carbonos (Furanosa)",
        detalle="→ Reingreso al eje glucolítico",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        texto_izquierda=True
    ))

    # Gliceraldehído-3-P (3C) a la derecha
    contenido_svg.append(crear_metabolito(
        x=560, y=1700,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="→ Reingreso al eje glucolítico",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))

    # -------------------------------------------------------------------------
    # BANNER DE BALANCE ESTEQUIOMÉTRICO FINAL Y REINGRESO A GLUCÓLISIS
    # -------------------------------------------------------------------------
    contenido_svg.append("""
    <!-- Banner de Balance y Cierre -->
    <g transform="translate(385, 1890)">
      <rect x="-240" y="0" width="480" height="75" rx="10" fill="#ffffff" stroke="#ea580c" stroke-width="2" filter="drop-shadow(0 4px 8px rgba(0,0,0,0.06))"/>
      <text x="0" y="24" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">BALANCE TOTAL DE LA FASE NO OXIDATIVA</text>
      <text x="0" y="42" fill="#ea580c" font-size="11" font-weight="900" text-anchor="middle">3 Pentosas (5C) ⇄ 2 Fructosa-6-P (6C) + 1 Gliceraldehído-3-P (3C)</text>
      <text x="0" y="58" fill="#64748b" font-size="10" text-anchor="middle">Todos los carbonos se reciclan de vuelta hacia la Glucólisis en citosol</text>
    </g>

    <!-- Flecha de reingreso hacia la izquierda -->
    <g transform="translate(145, 1925)">
      <path d="M 0 0 L -80 0" fill="none" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#arrowFlow)"/>
      <text x="-90" y="-10" fill="#c2410c" font-size="10" font-weight="800" text-anchor="end">← Reingreso directo a Glucólisis</text>
    </g>
    """)

    # Unir todo el código
    html_final = CABECERA_HTML + "\n".join(contenido_svg) + PIE_HTML

    # Escribir el archivo Pentosas.html
    ruta_salida = os.path.join(os.path.dirname(__file__), "Pentosas.html")
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(html_final)

    print(f"✅ ¡Vía de las Pentosas Fosfato con colisiones corregidas en: {ruta_salida}!")


if __name__ == "__main__":
    main()
