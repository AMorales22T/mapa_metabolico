#!/usr/bin/env python3
"""
PRUEBA DE ESTILO ORGÁNICO APLICADA AL CICLO DE KREBS
====================================================
ARCHIVO DE PRUEBA: no sustituye ni modifica a generar_ciclo_krebs.py.

Objetivo: adaptar el Ciclo de Krebs al lenguaje visual de
`ejemplo_estilo_visual.html` (moléculas libres sin cajas, fondo celular
orgánico con textura biológica, marca de agua de compartimento y barra de
herramientas con impresión), conservando intactos todos los archivos
originales del proyecto.

Reutiliza sin modificarlas:
  • estructuras_krebs.py ...... catálogo SVG de los metabolitos
  • entorno_mitocondrial.py ... dibujo de fondo mitocondrial

Salida: Ciclo_de_Krebs_prueba.html (convive con el Ciclo_de_Krebs.html real).

Ejecución:
    python3 02_RESPIRACION_Y_ENERGIA/02_ciclo_de_krebs/generar_ciclo_krebs_prueba.py
"""

import os
from estructuras_krebs import (
    PIRUVATO,
    ACETIL_COA,
    OXALACETATO,
    CITRATO,
    ISOCITRATO,
    ALFA_CETOGLUTARATO,
    SUCCINIL_COA,
    SUCCINATO,
    FUMARATO,
    MALATO,
    GLUTAMATO,
    DELTA_AMINOLEVULINATO,
    FOSFOENOLPIRUVATO,
    PROPIONIL_COA,
)
from entorno_mitocondrial import (
    DEFS_ENTORNO_MITOCONDRIAL,
    generar_entorno_mitocondrial_svg,
)

# -----------------------------------------------------------------------------
# 1. GEOMETRÍA DE LA PRUEBA (idéntica al mapa original, para poder compararlos)
# -----------------------------------------------------------------------------
ANCHO_CANVAS = 1150
ALTO_CANVAS = 2450

X_ESTRUCTURA = 380
X_FLECHA = 428

# Escala de las moléculas: el ejemplo de estilo las muestra grandes y libres.
ESCALA_MOLECULA = 1.12

# -----------------------------------------------------------------------------
# 2. PLANTILLA HTML: BARRA DE HERRAMIENTAS + REGLAS DE IMPRESIÓN
# -----------------------------------------------------------------------------
CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ciclo de Krebs (TCA) • Prueba de Estilo Orgánico</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #e2e8f0;
      color: #0f172a;
      padding: 30px 15px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .barra-herramientas {{
      width: {ANCHO_CANVAS}px;
      max-width: 100%;
      background: #ffffff;
      padding: 14px 22px;
      border-radius: 10px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 18px;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.06);
    }}
    .barra-herramientas h1 {{ font-size: 16px; font-weight: 900; }}
    .barra-herramientas p {{ font-size: 12px; color: #64748b; margin-top: 3px; }}
    .barra-herramientas button {{
      background: #0f172a; color: #ffffff; border: none;
      padding: 9px 18px; border-radius: 6px; white-space: nowrap;
      font-family: 'Inter', sans-serif; font-weight: 700; font-size: 12px; cursor: pointer;
    }}
    .lienzo-svg {{
      width: {ANCHO_CANVAS}px;
      max-width: 100%;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 12px;
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.14);
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
    @media print {{
      body {{ background: #ffffff; padding: 0; }}
      .barra-herramientas {{ display: none; }}
      .lienzo-svg {{ border: none; border-radius: 0; box-shadow: none; width: 100%; }}
    }}
  </style>
</head>
<body>
  <div class="barra-herramientas">
    <div>
      <h1>Ciclo de Krebs (TCA) • Matriz Mitocondrial Real</h1>
      <p>Prueba de estilo orgánico: moléculas libres, textura biológica y marca de agua de compartimento.</p>
    </div>
    <button onclick="window.print()">🖨️ Probar impresión</button>
  </div>
  <div class="lienzo-svg">
    <svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Flecha de flujo metabólico principal (Naranja) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de reactivo / gasto (Roja) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de salida de subproducto (Gris pizarra) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <!-- Flecha de ganancia / poder reductor (Verde esmeralda) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de agua (Azul) -->
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>
        <!-- Flecha de Coenzima A (Púrpura) -->
        <marker id="arrowPurple" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#7c3aed" />
        </marker>

        <!-- Textura orgánica del estroma: mitorribosomas (55S) dispersos -->
        <pattern id="pruebaRibosomas" width="92" height="92" patternUnits="userSpaceOnUse">
          <circle cx="18" cy="16" r="2.1" fill="#b45309" opacity="0.30"/>
          <circle cx="22" cy="19" r="1.4" fill="#b45309" opacity="0.30"/>
          <circle cx="70" cy="58" r="2.1" fill="#b45309" opacity="0.28"/>
          <circle cx="74" cy="61" r="1.4" fill="#b45309" opacity="0.28"/>
          <circle cx="46" cy="80" r="1.8" fill="#b45309" opacity="0.24"/>
          <circle cx="84" cy="12" r="1.8" fill="#b45309" opacity="0.24"/>
        </pattern>

        {DEFS_ENTORNO_MITOCONDRIAL}
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""


# -----------------------------------------------------------------------------
# 3. CAPAS DE ESTILO ORGÁNICO (TEXTURA + MARCA DE AGUA)
# -----------------------------------------------------------------------------
def capa_textura_organica():
    """
    Añade la textura biológica del estroma y la marca de agua del compartimento,
    imitando el fondo libre de cajas del ejemplo_estilo_visual.html.
    """
    return f"""
    <!-- ================================================================= -->
    <!-- CAPA ORGÁNICA: TEXTURA DEL ESTROMA Y MARCA DE AGUA                -->
    <!-- ================================================================= -->
    <rect x="0" y="170" width="{ANCHO_CANVAS}" height="{ALTO_CANVAS - 170}"
          fill="url(#pruebaRibosomas)" pointer-events="none"/>

    <text x="{X_ESTRUCTURA}" y="1250" font-family="'Inter', sans-serif" font-size="46"
          font-weight="900" fill="#b45309" opacity="0.07" letter-spacing="7"
          text-anchor="middle" pointer-events="none">MATRIZ MITOCONDRIAL</text>
    """


# -----------------------------------------------------------------------------
# 4. METABOLITO LIBRE: ESTRUCTURA GRANDE + RÓTULO FLOTANTE
# -----------------------------------------------------------------------------
def crear_metabolito(x, y, nombre, carbonos, detalle="", detalle2="",
                     svg_estructura="", offset_texto=150, escala=ESCALA_MOLECULA):
    """Metabolito sin caja: estructura grande y rótulo flotante a su derecha."""
    txt2 = (f'<text x="0" y="50" fill="#64748b" font-size="11.5">{detalle2}</text>'
            if detalle2 else "")
    return f"""
      <!-- Metabolito: {nombre} -->
      <g transform="translate({x}, {y})">
        <g transform="scale({escala})">
          {svg_estructura}
        </g>
        <g transform="translate({offset_texto}, 26)">
          <text x="0" y="0" fill="#0f172a" font-size="19" font-weight="800">{nombre}</text>
          <text x="0" y="20" fill="#ea580c" font-size="13" font-weight="700">{carbonos}</text>
          <text x="0" y="37" fill="#64748b" font-size="11.5">{detalle}</text>
          {txt2}
        </g>
      </g>
    """


# -----------------------------------------------------------------------------
# 5. REACCIÓN: FLECHA + CURVAS DE ENERGÍA + NOMBRE ENZIMÁTICO
# -----------------------------------------------------------------------------
def crear_reaccion(x, y, enzima, ec="", regulacion="", entra_reactivo="", sale_producto="",
                   sale_co2=False, entra_h2o=False, sale_h2o=False, entra_coa=False,
                   sale_coa=False, sustrato_lateral="", reversible=False,
                   es_ganancia=False, detalle_extra=""):
    """Bloque SVG de una reacción con curvas Bézier de energía."""
    curvas_energia = ""

    if sustrato_lateral:
        curvas_energia += f"""
        <path d="M -150 14 Q -50 14 -5 20" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        <text x="-155" y="18" fill="#c2410c" font-size="11.5" font-weight="900" text-anchor="end">{sustrato_lateral}</text>
        """

    if entra_reactivo:
        color_in = "#7c3aed" if entra_coa else "#475569"
        marker_in = "url(#arrowPurple)" if entra_coa else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -80 8 Q -30 8 -5 18" fill="none" stroke="{color_in}" stroke-width="1.8" marker-end="{marker_in}"/>
        <text x="-85" y="11" fill="{color_in}" font-size="11.5" font-weight="800" text-anchor="end">{entra_reactivo}</text>
        """

    if entra_h2o:
        curvas_energia += """
        <path d="M -70 -6 Q -30 -6 -5 12" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-75" y="-3" fill="#0284c7" font-size="11.5" font-weight="800" text-anchor="end">+ H₂O</text>
        """

    if sale_producto:
        color_out = "#059669" if es_ganancia else "#475569"
        marker_out = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -5 26 Q -30 36 -80 36" fill="none" stroke="{color_out}" stroke-width="1.8" marker-end="{marker_out}"/>
        <text x="-85" y="40" fill="{color_out}" font-size="12" font-weight="900" text-anchor="end">{sale_producto}</text>
        """

    if sale_co2:
        curvas_energia += """
        <path d="M -5 36 Q -30 52 -75 52" fill="none" stroke="#64748b" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="-80" y="55" fill="#64748b" font-size="11.5" font-weight="800" text-anchor="end">+ CO₂ ↑</text>
        """

    if sale_coa:
        curvas_energia += """
        <path d="M -5 32 Q -30 46 -75 46" fill="none" stroke="#7c3aed" stroke-width="1.8" marker-end="url(#arrowPurple)"/>
        <text x="-80" y="50" fill="#7c3aed" font-size="11" font-weight="800" text-anchor="end">+ CoA-SH</text>
        """

    if sale_h2o:
        curvas_energia += """
        <path d="M -5 24 Q -30 34 -70 34" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-75" y="37" fill="#0284c7" font-size="11" font-weight="800" text-anchor="end">- H₂O / + H₂O</text>
        """

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
        regulacion_svg = (f'<text x="0" y="27" fill="{color_reg}" font-size="10.5" '
                          f'font-weight="700">{regulacion}</text>')

    extra_svg = ""
    if detalle_extra:
        extra_svg = (f'<text x="0" y="40" fill="#c2410c" font-size="10" '
                     f'font-weight="800">{detalle_extra}</text>')

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha_central}
      {curvas_energia}
      <g transform="translate(20, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
        {extra_svg}
      </g>
    </g>
    """


# -----------------------------------------------------------------------------
# 6. PANELES DIDÁCTICOS LATERALES (se conservan como en el mapa original)
# -----------------------------------------------------------------------------
def crear_paneles_flotantes():
    return f"""
    <!-- ================================================================= -->
    <!-- LATERAL DERECHO: TARJETAS EDUCATIVAS UNIVERSITARIAS               -->
    <!-- ================================================================= -->

    <!-- TARJETA 1: RENDIMIENTO ENERGÉTICO Y BALANCE DE ATP -->
    <g transform="translate(760, 780)">
      <rect x="0" y="0" width="360" height="295" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" filter="drop-shadow(0 10px 20px rgba(0,0,0,0.07))"/>
      <rect x="0" y="0" width="360" height="34" rx="10" fill="#fff7ed" stroke="#ea580c" stroke-width="1.8"/>
      <text x="180" y="22" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#9a3412" text-anchor="middle" letter-spacing="0.5">BALANCE ENERGÉTICO POR ACETIL-CoA</text>

      <g transform="translate(20, 52)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a">PRODUCTOS NETOS (1 VUELTA):</text>

        <g transform="translate(0, 12)">
          <rect x="0" y="0" width="70" height="24" rx="12" fill="#dcfce7" stroke="#059669" stroke-width="1.5"/>
          <text x="35" y="16" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#065f46" text-anchor="middle">3 NADH</text>

          <rect x="80" y="0" width="75" height="24" rx="12" fill="#dcfce7" stroke="#059669" stroke-width="1.5"/>
          <text x="117" y="16" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#065f46" text-anchor="middle">1 FADH₂</text>

          <rect x="165" y="0" width="65" height="24" rx="12" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
          <text x="197" y="16" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#854d0e" text-anchor="middle">1 GTP</text>

          <rect x="240" y="0" width="70" height="24" rx="12" fill="#f1f5f9" stroke="#64748b" stroke-width="1.3"/>
          <text x="275" y="16" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#334155" text-anchor="middle">2 CO₂</text>
        </g>
      </g>

      <g transform="translate(20, 124)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a">FOSFORILACIÓN OXIDATIVA (CADENA RESP.):</text>
        <text x="10" y="20" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#047857">• 3 NADH × 2.5 ATP = 7.5 ATP</text>
        <text x="10" y="38" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#047857">• 1 FADH₂ × 1.5 ATP = 1.5 ATP</text>
        <text x="10" y="56" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#b45309">• 1 GTP (Fosf. a nivel sustrato) = 1.0 ATP</text>
      </g>

      <g transform="translate(180, 222)">
        <rect x="-140" y="-14" width="280" height="30" rx="15" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
        <text x="0" y="6" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#c2410c" text-anchor="middle">TOTAL = 10 ATP / Acetil-CoA</text>
      </g>
      <text x="180" y="254" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#475569" text-anchor="middle">★ Rendimiento total = 20 ATP por Glucosa</text>
      <text x="180" y="270" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">(+ 2 NADH de PDH = 25 ATP totales mitocondriales)</text>
    </g>


    <!-- MÓDULO 1: ENCRUCIJADA α-CETOGLUTARATO ⇄ L-GLUTAMATO -->
    <g transform="translate(760, 1100)">
      <rect x="0" y="0" width="360" height="260" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" filter="drop-shadow(0 10px 20px rgba(0,0,0,0.07))"/>
      <rect x="0" y="0" width="360" height="32" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.4"/>
      <text x="180" y="21" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#1e40af" text-anchor="middle">ENCRUCIJADA α-KG ⇄ L-GLUTAMATO</text>

      <g transform="translate(18, 50)">
        {GLUTAMATO}
      </g>

      <g transform="translate(115, 52)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a">L-Glutamato</text>
        <text x="0" y="16" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#2563eb">5 Carbonos (Aminoácido α)</text>

        <g transform="translate(0, 32)">
          <rect x="0" y="0" width="225" height="42" rx="5" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/>
          <text x="8" y="14" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#15803d">ANAPLEROSIS (Relleno de α-KG):</text>
          <text x="8" y="26" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="700" fill="#166534">Glutamato DH / AST / ALT (PLP)</text>
          <text x="8" y="36" font-family="'Inter', sans-serif" font-size="7.5" fill="#166534">Gln, Pro, His, Arg ➔ Glu ➔ α-KG</text>
        </g>

        <g transform="translate(0, 84)">
          <rect x="0" y="0" width="225" height="42" rx="5" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/>
          <text x="8" y="14" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#9d174d">CATAPLEROSIS (Biosíntesis):</text>
          <text x="8" y="26" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="700" fill="#be185d">Síntesis de Glutamina y Prolina</text>
          <text x="8" y="36" font-family="'Inter', sans-serif" font-size="7.5" fill="#be185d">Precursor clave de Purinas / Pirimidinas</text>
        </g>
      </g>
    </g>


    <!-- MÓDULO 2: ENCRUCIJADA SUCCINIL-CoA (HEMO Y PROPIONIL-CoA) -->
    <g transform="translate(760, 1380)">
      <rect x="0" y="0" width="360" height="305" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" filter="drop-shadow(0 10px 20px rgba(0,0,0,0.07))"/>
      <rect x="0" y="0" width="360" height="32" rx="10" fill="#fdf2f8" stroke="#db2777" stroke-width="1.4"/>
      <text x="180" y="21" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#9d174d" text-anchor="middle">SUCCINIL-CoA: HEMO Y AMINOÁCIDOS</text>

      <g transform="translate(18, 48)">
        {DELTA_AMINOLEVULINATO}
      </g>
      <g transform="translate(115, 50)">
        <text x="0" y="12" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a">δ-Aminolevulinato (ALA)</text>
        <text x="0" y="26" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#dc2626">5 Carbonos (Precursor de Hemo)</text>

        <g transform="translate(0, 34)">
          <rect x="0" y="0" width="225" height="42" rx="5" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/>
          <text x="8" y="14" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#9d174d">CATAPLEROSIS (ALA Sintasa):</text>
          <text x="8" y="26" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="700" fill="#be185d">Succinil-CoA + Gly ➔ ALA + CO₂</text>
          <text x="8" y="36" font-family="'Inter', sans-serif" font-size="7.5" fill="#be185d">➔ Porfirinas, Mioglobina y Hemoglobina</text>
        </g>
      </g>

      <line x1="20" y1="190" x2="340" y2="190" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3"/>

      <g transform="translate(18, 200)">
        {PROPIONIL_COA}
      </g>
      <g transform="translate(185, 204)">
        <text x="0" y="12" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a">Propionil-CoA</text>
        <text x="0" y="26" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#7c3aed">3 Carbonos + CoA (Tioéster)</text>

        <g transform="translate(0, 32)">
          <rect x="0" y="0" width="155" height="48" rx="5" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/>
          <text x="6" y="13" font-family="'Inter', sans-serif" font-size="8" font-weight="900" fill="#15803d">ANAPLEROSIS (Val/Ile/Met):</text>
          <text x="6" y="24" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="700" fill="#166534">Propionil-CoA Carboxilasa</text>
          <text x="6" y="34" font-family="'Inter', sans-serif" font-size="7" fill="#166534">Biotina + ATP ➔ Metilmalonil-CoA</text>
          <text x="6" y="44" font-family="'Inter', sans-serif" font-size="7" font-weight="700" fill="#15803d">➔ Succinil-CoA (Mutasa / B₁₂)</text>
        </g>
      </g>
    </g>


    <!-- MÓDULO 3: ENCRUCIJADA OXALACETATO (GLUCONEOGÉNESIS Y PIRUVATO CARBOXILASA) -->
    <g transform="translate(760, 1705)">
      <rect x="0" y="0" width="360" height="275" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" filter="drop-shadow(0 10px 20px rgba(0,0,0,0.07))"/>
      <rect x="0" y="0" width="360" height="32" rx="10" fill="#fff7ed" stroke="#ea580c" stroke-width="1.4"/>
      <text x="180" y="21" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" text-anchor="middle">OXALACETATO: GLUCONEOGÉNESIS</text>

      <g transform="translate(18, 48)">
        {FOSFOENOLPIRUVATO}
      </g>
      <g transform="translate(150, 48)">
        <text x="0" y="12" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a">Fosfoenolpiruvato (PEP)</text>
        <text x="0" y="26" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#ea580c">3 Carbonos (Fosforilado)</text>

        <g transform="translate(0, 32)">
          <rect x="0" y="0" width="190" height="42" rx="5" fill="#fdf2f8" stroke="#db2777" stroke-width="1.2"/>
          <text x="8" y="14" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#9d174d">CATAPLEROSIS (PEPCK):</text>
          <text x="8" y="26" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="700" fill="#be185d">Oxalacetato + GTP ➔ PEP + CO₂</text>
          <text x="8" y="36" font-family="'Inter', sans-serif" font-size="7.5" fill="#be185d">Ruta central de la Gluconeogénesis</text>
        </g>
      </g>

      <line x1="20" y1="165" x2="340" y2="165" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3"/>

      <g transform="translate(20, 180)">
        <rect x="0" y="0" width="320" height="80" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.3"/>
        <text x="12" y="18" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#15803d">ANAPLEROSIS MAESTRA: PIRUVATO CARBOXILASA (PC)</text>
        <text x="12" y="34" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="800" fill="#166534">Piruvato + CO₂ + ATP + H₂O ➔ Oxalacetato + ADP + Pi</text>
        <text x="12" y="50" font-family="'Inter', sans-serif" font-size="8" fill="#166534">• Enzima mitocondrial alostérica (Cofactor: Biotina dependiente de ATP y Mg²⁺).</text>
        <text x="12" y="64" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#047857">• ⊕ Activador alostérico obligado: Acetil-CoA (señal de exceso de combustible).</text>
      </g>
    </g>
    """


# -----------------------------------------------------------------------------
# 7. CONSTRUCCIÓN DEL EJE METABÓLICO VERTICAL
# -----------------------------------------------------------------------------
def construir_eje():
    piezas = []

    # 0. PIRUVATO (llega desde el citosol cruzando VDAC y MPC)
    piezas.append(crear_metabolito(
        X_ESTRUCTURA, 25,
        "Piruvato", "3 Carbonos (× 2)",
        "Generado en la Glucólisis citosólica",
        PIRUVATO, offset_texto=130,
    ))
    piezas.append(crear_reaccion(
        X_FLECHA, 175,
        enzima="Complejo Piruvato DH (PDH)",
        ec="EC 1.2.4.1 (E1 + E2 + E3)",
        regulacion="⊣ Acetil-CoA, NADH, ATP | ⊕ ADP, Ca²⁺",
        entra_reactivo="NAD⁺ + CoA-SH",
        sale_producto="+ NADH + H⁺",
        sale_co2=True,
        es_ganancia=True,
        detalle_extra="TPP • Lipoato • FAD • Cruce MPC",
    ))

    # 1. ACETIL-CoA
    piezas.append(crear_metabolito(
        X_ESTRUCTURA - 30, 280,
        "Acetil-CoA", "2 Carbonos (Activados)",
        "Tioéster de alta energía que inicia el ciclo",
        ACETIL_COA, offset_texto=200,
    ))
    piezas.append(crear_reaccion(
        X_FLECHA, 385,
        enzima="Citrato Sintasa",
        ec="EC 2.3.3.1 (ΔG°' = -31.5 kJ/mol)",
        regulacion="⊣ ATP, NADH, Citrato, Succinil-CoA | ⊕ ADP",
        sustrato_lateral="+ Oxalacetato (4C)",
        entra_h2o=True,
        sale_coa=True,
        detalle_extra="Ajuste inducido obligado • Retorno ↻",
    ))

    # 2. CITRATO
    piezas.append(crear_metabolito(
        X_ESTRUCTURA, 490,
        "Citrato", "6 Carbonos (Tricarboxilato)",
        "Alcohol terciario simétrico no oxidable",
        CITRATO,
    ))
    piezas.append(crear_reaccion(
        X_FLECHA, 650,
        enzima="Aconitasa (Aconitato Hidratasa)",
        ec="EC 4.2.1.3 (Centro [4Fe-4S])",
        regulacion="⊣ Fluoroacetato (Fluorocitrato)",
        sale_h2o=True,
        reversible=True,
        detalle_extra="Intermedio transitorio: cis-Aconitato",
    ))

    # 3. D-ISOCITRATO
    piezas.append(crear_metabolito(
        X_ESTRUCTURA, 745,
        "D-Isocitrato", "6 Carbonos (Tricarboxilato)",
        "Alcohol secundario en C2 apto para oxidación",
        ISOCITRATO,
    ))
    piezas.append(crear_reaccion(
        X_FLECHA, 905,
        enzima="Isocitrato Deshidrogenasa (IDH)",
        ec="EC 1.1.1.41 (Mg²⁺ / Mn²⁺)",
        regulacion="⊕ ADP, Ca²⁺ | ⊣ ATP, NADH",
        entra_reactivo="NAD⁺",
        sale_producto="+ NADH + H⁺",
        sale_co2=True,
        es_ganancia=True,
        detalle_extra="★ PASO LIMITANTE ALOSTÉRICO CLAVE",
    ))

    # 4. α-CETOGLUTARATO
    piezas.append(crear_metabolito(
        X_ESTRUCTURA, 1000,
        "α-Cetoglutarato", "5 Carbonos (α-Cetoácido)",
        "Encrucijada de transaminación",
        ALFA_CETOGLUTARATO, detalle2="Interconversión reversible con L-Glutamato",
    ))
    piezas.append(crear_reaccion(
        X_FLECHA, 1160,
        enzima="Complejo α-Cetoglutarato DH",
        ec="EC 1.2.4.2 (TPP, Lipoamida, FAD)",
        regulacion="⊕ Ca²⁺ | ⊣ Succinil-CoA, NADH, ATP",
        entra_reactivo="NAD⁺ + CoA-SH",
        sale_producto="+ NADH + H⁺",
        sale_co2=True,
        es_ganancia=True,
        detalle_extra="Complejo análogo a PDH (E1+E2+E3)",
    ))

    # 5. SUCCINIL-CoA
    piezas.append(crear_metabolito(
        X_ESTRUCTURA - 10, 1255,
        "Succinil-CoA", "4 Carbonos + CoA (Tioéster)",
        "Enlace tioéster de alta energía",
        SUCCINIL_COA, offset_texto=165,
        detalle2="ΔG°' ≈ -33.5 kJ/mol (Rico en energía)",
    ))
    piezas.append(crear_reaccion(
        X_FLECHA, 1405,
        enzima="Succinil-CoA Sintetasa (Tioquinasa)",
        ec="EC 6.2.1.4 / EC 6.2.1.5 (Mg²⁺)",
        entra_reactivo="GDP + Pi (o ADP)",
        sale_producto="+ 1 GTP / ATP",
        sale_coa=True,
        reversible=True,
        es_ganancia=True,
        detalle_extra="⚡ FOSFORILACIÓN A NIVEL DE SUSTRATO",
    ))

    # 6. SUCCINATO
    piezas.append(crear_metabolito(
        X_ESTRUCTURA, 1495,
        "Succinato", "4 Carbonos (Dicarboxilato)",
        "Sustrato simétrico",
        SUCCINATO, detalle2="Oxidado directamente en la MMI por SDH",
    ))
    piezas.append(crear_reaccion(
        X_FLECHA, 1635,
        enzima="Succinato DH (Complejo II)",
        ec="EC 1.3.5.1 (FAD, Fe-S)",
        regulacion="⊣ Malonato (Inhibidor competitivo)",
        entra_reactivo="FAD (covalente)",
        sale_producto="+ 1 FADH₂ (➔ CoQ)",
        es_ganancia=True,
        detalle_extra="INTEGRADA EN MMI • Cede e⁻ a Cadena Resp.",
    ))

    # 7. FUMARATO
    piezas.append(crear_metabolito(
        X_ESTRUCTURA, 1730,
        "Fumarato", "4 Carbonos (trans-Alqueno)",
        "Dicarboxilato insaturado",
        FUMARATO, detalle2="Configuración trans estereoespecífica",
    ))
    piezas.append(crear_reaccion(
        X_FLECHA, 1865,
        enzima="Fumarasa (Fumarato Hidratasa)",
        ec="EC 4.2.1.2 (Hidratasa)",
        entra_h2o=True,
        reversible=True,
        detalle_extra="Adición trans estereoespecífica",
    ))

    # 8. L-MALATO
    piezas.append(crear_metabolito(
        X_ESTRUCTURA, 1955,
        "L-Malato", "4 Carbonos (Hidroxiácido)",
        "Intermediario transportable",
        MALATO, detalle2="Lanzadera Malato-Aspartato",
    ))
    piezas.append(crear_reaccion(
        X_FLECHA, 2090,
        enzima="Malato Deshidrogenasa (MDH)",
        ec="EC 1.1.1.37 (Reversible ⇄)",
        entra_reactivo="NAD⁺",
        sale_producto="+ 1 NADH + H⁺",
        reversible=True,
        es_ganancia=True,
        detalle_extra="ΔG°' = +29.7 kJ/mol (Traccionada por CS)",
    ))

    # 9. OXALACETATO
    piezas.append(crear_metabolito(
        X_ESTRUCTURA, 2180,
        "Oxalacetato", "4 Carbonos (Dicarboxilato Regenerado)",
        "Aceptor regenerado al final del ciclo",
        OXALACETATO, detalle2="Listo para reiniciar la vía en Citrato Sintasa",
    ))

    # CIERRE DEL CICLO
    piezas.append(f"""
    <!-- ================================================================= -->
    <!-- NODO DE CIERRE: REGENERACIÓN DE OXALACETATO Y RETORNO             -->
    <!-- ================================================================= -->
    <path d="M {X_FLECHA} 2310 L {X_FLECHA} 2345" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

    <g transform="translate({X_FLECHA}, 2370)">
      <rect x="-185" y="-15" width="370" height="30" rx="15" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
      <text x="0" y="6" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#c2410c" text-anchor="middle">↻ REGENERA OXALACETATO (REINGRESA ARRIBA)</text>
    </g>

    <g transform="translate({X_FLECHA}, 2408)">
      <text x="0" y="0" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">Cierra el ciclo catalítico uniéndose a una nueva molécula de Acetil-CoA en la Citrato Sintasa</text>
    </g>
    """)

    return "\n".join(piezas)


# -----------------------------------------------------------------------------
# 8. ENSAMBLADO Y ESCRITURA
# -----------------------------------------------------------------------------
def main():
    contenido = [
        generar_entorno_mitocondrial_svg(ancho=ANCHO_CANVAS, alto=ALTO_CANVAS),
        capa_textura_organica(),
        crear_paneles_flotantes(),
        construir_eje(),
    ]

    html_final = CABECERA_HTML + "\n".join(contenido) + PIE_HTML

    ruta_salida = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "Ciclo_de_Krebs_prueba.html")
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(html_final)

    print(f"✅ Prueba de estilo generada en: {ruta_salida}")
    print("   (Los originales generar_ciclo_krebs.py y Ciclo_de_Krebs.html no se han tocado)")


if __name__ == "__main__":
    main()
