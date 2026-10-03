#!/usr/bin/env python3
"""
MAPA INDIVIDUAL DE LA GLUCONEOGÉNESIS (VÍA ANABÓLICA DE LA GLUCOSA)
===================================================================
Visualización Bioquímica Universitaria de Alta Precisión y Claridad Editorial.
- Membrana plasmática superior idéntica a la lámina individual de Glucólisis
  (fluido extracelular, bicapa ondulada continua con cabezas polares y canal GLUT-2).
- Matriz mitocondrial amplia, orgánica y holgada a juego con la de Glucólisis
  (gradiente cálido ámbar, doble membrana lisa y crestas profundas de la MMI).
- Lupa de Zoom Molecular para la Lanzadera de Malato (OGC / SLC25A11):
  corte transversal de la MMI con el antiporter de dicarboxilatos (Malato / α-KG)
  y transferencia del poder reductor.
- Flujo ascendente sin globos artificiales en metabolitos.
"""

import os
import sys

DIR_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(DIR_BASE, "01_glucolisis"))
sys.path.append(os.path.dirname(__file__))

from estructuras_glucosa import (
    GLUCOSA, GLUCOSA_6_FOSFATO, FRUCTOSA_6_FOSFATO, FRUCTOSA_1_6_BISFOSFATO,
    DIHIDROXIACETONA_FOSFATO, GLICERALDEHIDO_3_FOSFATO, BISFOSFOGLICERATO_1_3,
    FOSFOGLICERATO_3, FOSFOGLICERATO_2, FOSFOENOLPIRUVATO, PIRUVATO
)

from estructuras_gluconeogenesis import (
    OXALACETATO, MALATO, LACTATO, RE_GLUCOSA_6_FOSFATASA
)

ANCHO_CANVAS = 1350
ALTO_CANVAS = 2950

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gluconeogénesis - Mapa Bioquímico Compartimentado</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background-color: #0f172a;
      color: #334155;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 20px;
      min-height: 100vh;
    }}
    .lienzo-svg {{
      background-color: #ffffff;
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.5);
      border-radius: 12px;
      max-width: 100%;
      height: auto;
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Marcadores estándar -->
        <marker id="arrowFlow" markerWidth="7" markerHeight="7" refX="5.5" refY="3.5" orient="auto">
          <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#ea580c" />
        </marker>
        <marker id="arrowRed" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#dc2626" />
        </marker>
        <marker id="arrowGreen" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#059669" />
        </marker>
        <marker id="arrowBlue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#0284c7" />
        </marker>
        <marker id="arrowSlate" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#475569" />
        </marker>

        <!-- Gradientes celulares orgánicos a juego con Glucólisis -->
        <linearGradient id="gradCitosol" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
          <stop offset="5%" stop-color="#f0fdf4" stop-opacity="0.8" />
          <stop offset="50%" stop-color="#f8fafc" stop-opacity="0.5" />
          <stop offset="90%" stop-color="#f0fdf4" stop-opacity="0.7" />
          <stop offset="100%" stop-color="#f8fafc" stop-opacity="1" />
        </linearGradient>

        <linearGradient id="gradExtracelular" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#e2e8f0" stop-opacity="0.7" />
          <stop offset="100%" stop-color="#f1f5f9" stop-opacity="0.9" />
        </linearGradient>

        <radialGradient id="gradMitocondria" cx="50%" cy="100%" r="90%">
          <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.95" />
          <stop offset="60%" stop-color="#fffbeb" stop-opacity="0.9" />
          <stop offset="100%" stop-color="#fef9c3" stop-opacity="0.85" />
        </radialGradient>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def generar_entorno_gluconeogenesis(ancho, alto, y_mito=2220):
    """
    Genera el entorno celular con:
    1. Membrana plasmática superior ondulada real a juego con Glucólisis.
    2. Citoesqueleto y vesículas.
    3. Mitocondria biológica en la base amplia y espaciosa con transportador MPC y lanzadera.
    """
    return f"""
    <!-- Fondo Citoplasmático Acuoso -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#gradCitosol)" />

    <!-- ================================================================= -->
    <!-- CAPA: CITOESQUELETO Y ESTRUCTURAS CITOPLASMÁTICAS                 -->
    <!-- ================================================================= -->
    <g opacity="0.32" stroke="#94a3b8" fill="none">
      <path d="M 50 240 Q 350 180 700 260 T {ancho-50} 230" stroke-width="1.6" stroke-dasharray="8 6" />
      <path d="M 60 480 Q 400 550 780 490 T {ancho-60} 520" stroke-width="1.4" stroke-dasharray="6 6" />
      <path d="M 40 850 Q 420 790 820 860 T {ancho-40} 820" stroke-width="1.5" stroke-dasharray="8 5" />
      <path d="M 50 1250 Q 380 1310 740 1260 T {ancho-50} 1290" stroke-width="1.6" stroke-dasharray="7 7" />
      <path d="M 40 1680 Q 450 1630 880 1690 T {ancho-40} 1650" stroke-width="1.5" stroke-dasharray="8 6" />
      <path d="M 60 2050 Q 480 2110 850 2060 T {ancho-60} 2090" stroke-width="1.4" stroke-dasharray="6 6" />
    </g>

    <!-- Polirribosomas celulares -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="120" cy="180" r="2.5"/><circle cx="126" cy="182" r="2"/><circle cx="124" cy="188" r="2.3"/>
      <circle cx="1180" cy="340" r="2.5"/><circle cx="1187" cy="342" r="2"/><circle cx="1184" cy="348" r="2.3"/>
      <circle cx="140" cy="720" r="2.5"/><circle cx="146" cy="723" r="2.2"/><circle cx="143" cy="728" r="2"/>
      <circle cx="1160" cy="1150" r="2.5"/><circle cx="1167" cy="1153" r="2"/><circle cx="1163" cy="1158" r="2.2"/>
    </g>

    <!-- Vesículas citosólicas translúcidas -->
    <g opacity="0.3">
      <circle cx="160" cy="420" r="22" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="160" cy="420" r="16" fill="none" stroke="#7dd3fc" stroke-width="1"/>
      <circle cx="1170" cy="980" r="26" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="1170" cy="980" r="19" fill="none" stroke="#7dd3fc" stroke-width="1"/>
    </g>


    <!-- ================================================================= -->
    <!-- MEMBRANA PLASMÁTICA SUPERIOR REAL (DISEÑO IDÉNTICO A GLUCÓLISIS)  -->
    <!-- ================================================================= -->
    <!-- Medio Extracelular (Fluido intersticial / Sangre) -->
    <path d="M 0 0 L {ancho} 0 L {ancho} 60 Q {ancho*0.5} 85 0 60 Z" fill="url(#gradExtracelular)" stroke="#cbd5e1" stroke-width="1"/>
    <text x="35" y="24" fill="#64748b" font-size="10.5" font-weight="800" letter-spacing="1">ESPACIO EXTRACELULAR (SANGRE / LÍQUIDO INTERSTICIAL)</text>
    <text x="35" y="42" fill="#0284c7" font-size="9.5" font-weight="700">[GLUCEMIA AYUNO] ≈ 70-100 mg/dL</text>

    <!-- Bicapa Fosfolipídica Ondulada Celular (Azul de Glucólisis) -->
    <path d="M 0 60 Q {ancho*0.5} 85 {ancho} 60" fill="none" stroke="#0284c7" stroke-width="8" stroke-linecap="round"/>
    <path d="M 0 68 Q {ancho*0.5} 93 {ancho} 68" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>

    <!-- Cabezas de fosfolípidos decorativas -->
    <g fill="#0284c7" opacity="0.6">
      <circle cx="80" cy="58" r="3"/><circle cx="95" cy="59" r="3"/><circle cx="110" cy="60" r="3"/>
      <circle cx="240" cy="67" r="3"/><circle cx="255" cy="68" r="3"/><circle cx="270" cy="69" r="3"/>
      <circle cx="950" cy="69" r="3"/><circle cx="965" cy="68" r="3"/><circle cx="980" cy="67" r="3"/>
      <circle cx="1200" cy="60" r="3"/><circle cx="1215" cy="59" r="3"/><circle cx="1230" cy="58" r="3"/>
    </g>

    <!-- Transportador GLUT-2 en la membrana (Exporta Glucosa libre) -->
    <g transform="translate(635, 45)">
      <!-- Lóbulo proteico izquierdo -->
      <path d="M 0 5 C 10 -12, 28 -12, 34 5 C 38 18, 34 36, 25 42 C 12 45, 2 35, 0 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <!-- Lóbulo proteico derecho -->
      <path d="M 80 5 C 70 -12, 52 -12, 46 5 C 42 18, 46 36, 55 42 C 68 45, 78 35, 80 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      
      <!-- Poro o canal central acuoso -->
      <ellipse cx="40" cy="20" rx="10" ry="18" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8"/>
      
      <!-- Molécula de glucosa saliendo hacia la sangre -->
      <polygon points="40,14 45,17 45,23 40,26 35,23 35,17" fill="#ffffff" stroke="#ea580c" stroke-width="1.6"/>
      <circle cx="35" cy="17" r="2" fill="#dc2626"/>

      <!-- Rótulo en la proteína -->
      <text x="40" y="49" fill="#0369a1" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-2</text>
    </g>

    <!-- Flecha de salida hacia el torrente sanguíneo -->
    <line x1="675" y1="120" x2="675" y2="88" stroke="#ea580c" stroke-width="2.5"/>
    <line x1="675" y1="45" x2="675" y2="20" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
    <text x="735" y="85" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#c2410c">
      Exportación Hepática (Km ≈ 15-20 mM)
    </text>


    <!-- ================================================================= -->
    <!-- LA MITOCONDRIA BIOLÓGICA REAL (ABAJO, AMPLIA Y HOLGADA)           -->
    <!-- ================================================================= -->
    <g id="mitocondria-biologica-gng" transform="translate(0, {y_mito})">
      <!-- Membrana Mitocondrial Externa Lisa (Ámbar Cálido) -->
      <path d="M 0 50 Q 300 15 650 35 T {ancho} 25 L {ancho} 730 L 0 730 Z" 
            fill="url(#gradMitocondria)" stroke="#b45309" stroke-width="3.5"/>
      
      <!-- Espacio Intermembrana (Separación visible) -->
      <path d="M 0 65 Q 300 30 650 50 T {ancho} 40" 
            fill="none" stroke="#78350f" stroke-width="2" stroke-dasharray="6 3"/>

      <!-- Crestas Mitocondriales Reales de la MMI (Invaginaciones profundas) -->
      <!-- Cresta izquierda -->
      <path d="M 80 150 C 150 90, 190 180, 290 120 C 350 180, 300 230, 160 210 Z" 
            fill="#fef3c7" stroke="#b45309" stroke-width="2.5" opacity="0.85"/>
      <!-- Cresta derecha -->
      <path d="M 980 140 C 1070 80, 1140 170, 1240 110 C 1320 170, 1270 230, 1100 210 Z" 
            fill="#fef3c7" stroke="#b45309" stroke-width="2.5" opacity="0.85"/>
      <!-- Cresta inferior amplia -->
      <path d="M 380 480 C 470 430, 600 430, 700 480" 
            fill="none" stroke="#b45309" stroke-width="2.5" stroke-linecap="round"/>

      <!-- Transportador MPC (Complejo Carrier de Piruvato) incrustado en la membrana -->
      <g transform="translate(645, 22)">
        <rect x="0" y="0" width="60" height="26" rx="6" fill="#b45309" stroke="#78350f" stroke-width="1.8"/>
        <text x="30" y="18" fill="#ffffff" font-size="11" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">MPC</text>
      </g>
      <!-- Flecha del Piruvato cruzando el MPC hacia la Matriz Mitocondrial -->
      <line x1="675" y1="-8" x2="675" y2="55" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Rótulo de la Matriz Mitocondrial -->
      <g transform="translate(60, 85)">
        <text x="0" y="0" fill="#78350f" font-size="16" font-weight="900" letter-spacing="1">MATRIZ MITOCONDRIAL</text>
        <text x="0" y="18" fill="#92400e" font-size="11.5" font-weight="700">Compartimento de inicio: Bypass 1A (Piruvato Carboxilasa)</text>
      </g>

      <!-- Transportador OGC (Lanzadera Malato / α-KG) en la membrana interna -->
      <g transform="translate(370, 22)">
        <rect x="0" y="0" width="70" height="26" rx="6" fill="#047857" stroke="#064e3b" stroke-width="1.8"/>
        <text x="35" y="17" fill="#ffffff" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">OGC</text>
      </g>
      <text x="405" y="12" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#047857" text-anchor="middle">
        Antiporte Malato / α-KG
      </text>
    </g>
    """

def generar_lupa_malato(x=170, y=2320):
    """
    Genera la Lupa Molecular para la Lanzadera de Malato (OGC / SLC25A11),
    mostrando el corte transversal de la membrana mitocondrial interna,
    el transportador antiporter y la exportación de poder reductor.
    """
    return f"""
    <!-- ============================================================= -->
    <!-- ZOOM MOLECULAR / LUPA DE LA LANZADERA DE MALATO (OGC)         -->
    <!-- ============================================================= -->
    <!-- Líneas de proyección cónica desde el transportador OGC hacia la lupa -->
    <g stroke="#047857" stroke-width="1.3" stroke-dasharray="4 3" opacity="0.65">
      <line x1="370" y1="2242" x2="{x + 65}" y2="{y - 45}" />
      <line x1="370" y1="2255" x2="{x + 40}" y2="{y + 60}" />
    </g>

    <!-- Ventana Circular de Zoom (Lupa Molecular) -->
    <g transform="translate({x}, {y})">
      <!-- Fondo y bordes de la lupa -->
      <circle cx="0" cy="0" r="75" fill="#ffffff" stroke="#047857" stroke-width="3.5" />
      <circle cx="0" cy="0" r="71" fill="#f0fdf4" stroke="#dcfce7" stroke-width="1.2" />

      <!-- Bicapa lipídica de la Membrana Mitocondrial Interna (MMI) -->
      <g opacity="0.85">
        <!-- Capa citosólica de fosfolípidos (arriba) -->
        <g fill="#047857">
          <circle cx="-55" cy="-9" r="5"/><circle cx="-40" cy="-9" r="5"/><circle cx="-25" cy="-9" r="5"/>
          <circle cx="25" cy="-9" r="5"/><circle cx="40" cy="-9" r="5"/><circle cx="55" cy="-9" r="5"/>
        </g>
        <!-- Colas de ácidos grasos (onduladas) -->
        <g stroke="#94a3b8" stroke-width="1.4" fill="none">
          <path d="M -55 -4 Q -57 2 -53 8"/><path d="M -40 -4 Q -42 2 -38 8"/><path d="M -25 -4 Q -27 2 -23 8"/>
          <path d="M 25 -4 Q 23 2 27 8"/><path d="M 40 -4 Q 38 2 42 8"/><path d="M 55 -4 Q 53 2 57 8"/>
          <path d="M -55 19 Q -57 13 -53 8"/><path d="M -40 19 Q -42 13 -38 8"/><path d="M -25 19 Q -27 13 -23 8"/>
          <path d="M 25 19 Q 23 13 27 8"/><path d="M 40 19 Q 38 13 42 8"/><path d="M 55 19 Q 53 13 57 8"/>
        </g>
        <!-- Capa matricial de fosfolípidos (abajo) -->
        <g fill="#047857">
          <circle cx="-55" cy="24" r="5"/><circle cx="-40" cy="24" r="5"/><circle cx="-25" cy="24" r="5"/>
          <circle cx="25" cy="24" r="5"/><circle cx="40" cy="24" r="5"/><circle cx="55" cy="24" r="5"/>
        </g>
      </g>

      <!-- Proteína Transportadora OGC (Carrier SLC25A11) -->
      <path d="M -18 -24 C -9 -28, -5 -16, -5 0 C -5 16, -9 28, -18 24 C -26 20, -24 -20, -18 -24 Z" fill="#047857" stroke="#064e3b" stroke-width="2"/>
      <path d="M 18 -24 C 9 -28, 5 -16, 5 0 C 5 16, 9 28, 18 24 C 26 20, 24 -20, 18 -24 Z" fill="#047857" stroke="#064e3b" stroke-width="2"/>
      <ellipse cx="0" cy="0" rx="7" ry="20" fill="#a7f3d0" opacity="0.6"/>

      <!-- Flechas de antiporte -->
      <!-- Malato saliendo hacia arriba (citosol) -->
      <path d="M -7 20 L -7 -20" stroke="#059669" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
      <text x="-12" y="2" fill="#059669" font-size="8" font-weight="900" text-anchor="end">Malato²⁻ ↑</text>

      <!-- α-Ketoglutarato entrando hacia abajo (matriz) -->
      <path d="M 7 -20 L 7 20" stroke="#475569" stroke-width="2.2" marker-end="url(#arrowSlate)"/>
      <text x="12" y="2" fill="#475569" font-size="8" font-weight="900">↓ α-KG²⁻</text>

      <!-- Etiqueta inferior de la lupa -->
      <rect x="-65" y="48" width="130" height="17" rx="5" fill="#0f172a" opacity="0.9"/>
      <text x="0" y="60" fill="#ffffff" font-size="8" font-weight="800" text-anchor="middle" letter-spacing="0.5">
        ANTIPORTE OGC (SLC25A11)
      </text>
    </g>

    <!-- Caja explicativa al lado de la lupa -->
    <g transform="translate({x + 85}, {y - 40})">
      <rect x="0" y="0" width="330" height="85" rx="8" fill="#ffffff" stroke="#047857" stroke-width="1.8" filter="drop-shadow(0 2px 5px rgba(0,0,0,0.06))"/>
      <text x="14" y="20" fill="#047857" font-size="12" font-weight="900">MECANISMO DE LANZADERA DE MALATO</text>
      <text x="14" y="38" fill="#0f172a" font-size="10.5" font-weight="700">
        1. La MMI es totalmente impermeable a Oxalacetato (OAA).
      </text>
      <text x="14" y="54" fill="#0f172a" font-size="10.5">
        2. Se reduce a L-Malato consumiendo NADH mitocondrial.
      </text>
      <text x="14" y="70" fill="#047857" font-size="10.5" font-weight="800">
        3. El OGC exporta Malato al citosol y reoxida a OAA, transfiriendo NADH.
      </text>
    </g>
    """

def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False, dx_texto=140):
    """Metabolito limpio sin globos ni cajas."""
    if texto_izquierda:
        pos_estructura = "translate(0, 0)"
        pos_texto = f"translate(-25, 28)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = f"translate({dx_texto}, 28)"
        alineacion = ''

    return f"""
    <!-- Metabolito: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="{pos_estructura}">
        {svg_estructura}
      </g>
      <g transform="{pos_texto}">
        <text x="0" y="0" fill="#0f172a" font-size="17" font-weight="800" {alineacion}>{nombre}</text>
        <text x="0" y="20" fill="#ea580c" font-size="13" font-weight="700" {alineacion}>{carbonos}</text>
        <text x="0" y="37" fill="#475569" font-size="12" font-weight="600" {alineacion}>{detalle}</text>
      </g>
    </g>
    """

def crear_reaccion_ascendente(x, y, enzima, ec="", regulacion="", entra_energia="", sale_energia="", 
                              reversible=False, salida_agua=False, altura=52):
    """Generador de reacción gluconeogénica ascendente."""
    curvas_energia = ""
    if entra_energia:
        curvas_energia += f"""
        <path d="M -85 38 Q -30 38 -4 26" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
        <text x="-92" y="42" fill="#dc2626" font-size="12" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
    if sale_energia:
        curvas_energia += f"""
        <path d="M -4 20 Q -30 9 -85 9" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
        <text x="-92" y="13" fill="#475569" font-size="12" font-weight="800" text-anchor="end">{sale_energia}</text>
        """
    if salida_agua:
        curvas_energia += """
        <path d="M -85 38 Q -30 38 -4 26" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
        <text x="-92" y="42" fill="#0284c7" font-size="12" font-weight="800" text-anchor="end">+ H₂O</text>
        """

    if reversible:
        flecha = f"""
        <line x1="-3.5" y1="{altura}" x2="-3.5" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        <line x1="3.5" y1="0" x2="3.5" y2="{altura}" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        """
    else:
        flecha = f"""
        <line x1="0" y1="{altura}" x2="0" y2="0" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="30" fill="{color_reg}" font-size="11" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción Ascendente: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha}
      {curvas_energia}
      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="14.5" font-weight="800">{enzima}</text>
        <text x="0" y="15" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """

def generar_mapa_gluconeogenesis():
    """Compila el mapa individual de Gluconeogénesis."""
    svg_parts = []

    # 1. Capa de entorno celular biológico (ancho=1350, alto=2950, y_mito=2220)
    svg_parts.append(generar_entorno_gluconeogenesis(ANCHO_CANVAS, ALTO_CANVAS, y_mito=2220))

    # 2. Lupa Molecular de la Lanzadera de Malato (en la matriz izquierda)
    svg_parts.append(generar_lupa_malato(x=150, y=2460))

    X_EJE = 620
    X_FLECHA = 675

    # =========================================================================
    # FASE 1: BASE MITOCONDRIAL (AMPLIA, HOLGADA Y ORGÁNICA)
    # =========================================================================
    # Entrada de Lactato (Ciclo de Cori) a un nivel superior limpio y despejado
    svg_parts.append(f"""
    <!-- Vía del Lactato (Ciclo de Cori) -->
    <g transform="translate(1000, 2310)">
      {LACTATO}
      <g transform="translate(100, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="800">L-Lactato</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700">Ciclo de Cori (Músculo/Eritrocitos)</text>
      </g>
    </g>
    <!-- Flecha Lactato ➔ Piruvato con LDH horizontal despejada -->
    <g transform="translate(860, 2335)">
      <line x1="70" y1="0" x2="-80" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M 50 -12 Q 0 -22 -50 -12" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="0" y="-26" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">+ NAD⁺</text>
      <path d="M 50 12 Q 0 22 -50 12" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="0" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">+ NADH + H⁺</text>
      <text x="0" y="-5" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Lactato DH (LDH)</text>
    </g>
    """)

    # Piruvato Mitocondrial (Bajado a y=2420)
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=2420,
        nombre="Piruvato (Mitocondrial)",
        carbonos="3 Carbonos (α-Cetoácido)",
        detalle="Ingreso por MPC • Sustrato inicial de la Gluconeogénesis",
        svg_estructura=PIRUVATO,
        dx_texto=130
    ))

    # Reacción: Piruvato Carboxilasa (Bypass 1A)
    svg_parts.append("""
    <!-- Reacción: Piruvato Carboxilasa (PC) -->
    <g transform="translate(675, 2530)">
      <line x1="0" y1="0" x2="0" y2="52" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M -85 10 Q -30 10 -4 22" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
      <text x="-92" y="14" fill="#dc2626" font-size="12" font-weight="800" text-anchor="end">- 1 ATP + HCO₃⁻ (CO₂)</text>
      <path d="M -4 30 Q -30 42 -85 42" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-92" y="46" fill="#475569" font-size="12" font-weight="800" text-anchor="end">+ ADP + Pi</text>
      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="900">Piruvato Carboxilasa (PC)</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 6.4.1.1 (Cofactor: Biotina - Vit. B₇)</text>
        <text x="0" y="32" fill="#16a34a" font-size="11.5" font-weight="800">⊕ Activador Alostérico Obligatorio: Acetil-CoA</text>
      </g>
    </g>
    """)

    # Oxalacetato mitocondrial
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=2620,
        nombre="Oxalacetato (OAA Mitocondrial)",
        carbonos="4 Carbonos (Dicarboxilato α-Cetoácido)",
        detalle="La MMI carece de transportador directo para OAA",
        svg_estructura=OXALACETATO,
        dx_texto=140
    ))

    # Reacción: MDH Mitocondrial (mMDH hacia la izquierda)
    svg_parts.append("""
    <!-- Reacción Malato Deshidrogenasa Mitocondrial (mMDH) -->
    <g transform="translate(580, 2670)">
      <line x1="0" y1="0" x2="-140" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M -25 -14 Q -70 -26 -115 -14" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-70" y="-28" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">+ NADH + H⁺ ➔ + NAD⁺</text>
      <g transform="translate(-70, 18)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">MDH Mitocondrial</text>
        <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#64748b" text-anchor="middle">EC 1.1.1.37 (Consumo de NADH)</text>
      </g>
    </g>
    """)

    # L-Malato mitocondrial (x = 350, y = 2620)
    svg_parts.append(crear_metabolito(
        x=350, y=2620,
        nombre="L-Malato (Mitocondrial)",
        carbonos="4 Carbonos (Hidroxiácido)",
        detalle="Forma transportable a través del carrier OGC",
        svg_estructura=MALATO,
        texto_izquierda=True
    ))

    # Trayectoria de salida de Malato cruzando la MMI hacia el citosol
    svg_parts.append("""
    <!-- Malato sube cruzando la membrana mitocondrial -->
    <path d="M 405 2620 L 405 2200" fill="none" stroke="#047857" stroke-width="3" stroke-dasharray="8 4" marker-end="url(#arrowFlow)"/>
    """)

    # =========================================================================
    # FASE 2: CITOSOL Y BYPASS 1B (PEPCK)
    # =========================================================================
    # L-Malato Citosólico (x = 350, y = 2070)
    svg_parts.append(crear_metabolito(
        x=350, y=2070,
        nombre="L-Malato (Citosólico)",
        carbonos="4 Carbonos",
        detalle="Reoxidado para exportar NADH al citosol",
        svg_estructura=MALATO,
        texto_izquierda=True
    ))

    # Reacción: MDH Citosólica (cMDH)
    svg_parts.append("""
    <!-- Reacción MDH Citosólica (cMDH) -->
    <g transform="translate(460, 2120)">
      <line x1="0" y1="0" x2="130" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M 25 -14 Q 65 -26 105 -14" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="65" y="-28" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">+ NAD⁺ ➔ + NADH + H⁺</text>
      <g transform="translate(65, 18)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">MDH Citosólica</text>
        <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#64748b" text-anchor="middle">EC 1.1.1.37 (Regenera NADH para GAPDH)</text>
      </g>
    </g>
    """)

    # Oxalacetato citosólico en (X_EJE, 2070)
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=2070,
        nombre="Oxalacetato (OAA Citosólico)",
        carbonos="4 Carbonos",
        detalle="Substrato de descarboxilación por PEPCK",
        svg_estructura=OXALACETATO,
        dx_texto=140
    ))

    # Reacción: PEPCK (Bypass 1B)
    svg_parts.append("""
    <!-- Reacción PEPCK Citosólica -->
    <g transform="translate(675, 1975)">
      <line x1="0" y1="52" x2="0" y2="0" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M -85 38 Q -30 38 -4 26" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
      <text x="-92" y="42" fill="#dc2626" font-size="12" font-weight="800" text-anchor="end">- 1 GTP</text>
      <path d="M -4 20 Q -30 9 -85 9" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-92" y="13" fill="#475569" font-size="12" font-weight="800" text-anchor="end">+ GDP + CO₂</text>
      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="900">Fosfoenolpiruvato Carboxiquinasa (PEPCK-C)</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 4.1.1.32 (Mg²⁺, GTP)</text>
        <text x="0" y="32" fill="#b45309" font-size="11" font-weight="700">Descarboxilación exergónica impulsora</text>
      </g>
    </g>
    """)

    # =========================================================================
    # FASE 3: FASE REVERSA DE TRIOSAS (ASCENDENTE)
    # =========================================================================
    # PEP
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=1870,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 Carbonos (Enol-fosfato)",
        detalle="Inicio del flujo glucolítico reverso",
        svg_estructura=FOSFOENOLPIRUVATO,
        dx_texto=140
    ))

    # Reacción Reversa: Enolasa
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=1770,
        enzima="Enolasa",
        ec="EC 4.2.1.11 (⇄, + 2 H₂O)",
        salida_agua=True,
        reversible=True
    ))

    # 2-PG
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=1670,
        nombre="2-Fosfoglicerato",
        carbonos="3 Carbonos",
        detalle="Hidratación reversible de PEP",
        svg_estructura=FOSFOGLICERATO_2,
        dx_texto=140
    ))

    # Reacción Reversa: PGM
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=1570,
        enzima="Fosfoglicerato Mutasa",
        ec="EC 5.4.2.1 (⇄)",
        reversible=True
    ))

    # 3-PG
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=1470,
        nombre="3-Fosfoglicerato",
        carbonos="3 Carbonos",
        detalle="Substrato para fosforilación endergónica",
        svg_estructura=FOSFOGLICERATO_3,
        dx_texto=140
    ))

    # Reacción Reversa: Fosfoglicerato Quinasa
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=1370,
        enzima="Fosfoglicerato Quinasa",
        ec="EC 2.7.2.3 (⇄)",
        entra_energia="- 2 ATP",
        sale_energia="+ 2 ADP",
        reversible=True
    ))

    # 1,3-BPG
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=1270,
        nombre="1,3-Bisfosfoglicerato",
        carbonos="3 Carbonos (Acil-fosfato)",
        detalle="Substrato para reducción por NADH",
        svg_estructura=BISFOSFOGLICERATO_1_3,
        dx_texto=140
    ))

    # Reacción Reversa: GAPDH
    svg_parts.append("""
    <g transform="translate(675, 1170)">
      <line x1="-3.5" y1="52" x2="-3.5" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="3.5" y1="0" x2="3.5" y2="52" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <path d="M -85 38 Q -30 38 -4 26" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-92" y="42" fill="#059669" font-size="12" font-weight="800" text-anchor="end">- 2 NADH + 2 H⁺</text>
      <path d="M -4 20 Q -30 9 -85 9" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-92" y="13" fill="#475569" font-size="12" font-weight="800" text-anchor="end">+ 2 NAD⁺ + 2 Pi</text>
      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="14.5" font-weight="800">GAPDH (Reducción Reversa)</text>
        <text x="0" y="15" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 1.2.1.12 (Consume el NADH de la lanzadera)</text>
      </g>
    </g>
    """)

    # Bifurcación Triosas: DHAP y GAP
    svg_parts.append(crear_metabolito(
        x=450, y=1060,
        nombre="Dihidroxiacetona-Ⓟ",
        carbonos="3 Carbonos (Cetotriosa)",
        detalle="Aporte desde Glicerol lipolítico",
        svg_estructura=DIHIDROXIACETONA_FOSFATO,
        texto_izquierda=True
    ))

    svg_parts.append(crear_metabolito(
        x=760, y=1060,
        nombre="Gliceraldehído-3-Ⓟ",
        carbonos="3 Carbonos (Aldotriosa)",
        detalle="Substrato de condensación aldólica",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO,
        dx_texto=140
    ))

    # TPI (Conexión reversible)
    svg_parts.append("""
    <g transform="translate(630, 1095)">
      <line x1="-50" y1="-3" x2="50" y2="-3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="50" y1="3" x2="-50" y2="3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(0, -12)">
        <text x="0" y="-8" fill="#0f172a" font-size="13" font-weight="800" text-anchor="middle">Triosa Fosfato Isomerasa</text>
        <text x="0" y="6" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1 (⇄)</text>
      </g>
    </g>
    """)

    # Reacción Reversa: Aldolasa (Condensación de DHAP + GAP ➔ F-1,6-BP)
    svg_parts.append("""
    <g transform="translate(675, 960)">
      <path d="M -110 50 Q -70 25 0 0" fill="none" stroke="#ea580c" stroke-width="2.4"/>
      <path d="M 110 50 Q 70 25 0 0" fill="none" stroke="#ea580c" stroke-width="2.4"/>
      <line x1="0" y1="0" x2="0" y2="-35" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(20, -10)">
        <text x="0" y="0" fill="#0f172a" font-size="14.5" font-weight="800">Aldolasa A / B (Condensación)</text>
        <text x="0" y="15" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 4.1.2.13 (3C + 3C ➔ 6C)</text>
      </g>
    </g>
    """)

    # Fructosa-1,6-Bisfosfato
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=830,
        nombre="Fructosa-1,6-Bisfosfato",
        carbonos="6 Carbonos (Hexosa Bisfosforilada)",
        detalle="Substrato del segundo bypass gluconeogénico",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO,
        dx_texto=140
    ))

    # =========================================================================
    # BYPASS 2: FRUCTOSA-1,6-BISFOSFATASA-1 (FBPasa-1)
    # =========================================================================
    svg_parts.append("""
    <!-- Reacción FBPasa-1 (Bypass 2 Irreversible) -->
    <g transform="translate(675, 725)">
      <line x1="0" y1="52" x2="0" y2="0" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M -85 38 Q -30 38 -4 26" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="-92" y="42" fill="#0284c7" font-size="12" font-weight="800" text-anchor="end">+ H₂O</text>
      <path d="M -4 20 Q -30 9 -85 9" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-92" y="13" fill="#059669" font-size="12" font-weight="800" text-anchor="end">+ Pi libre (Hidrólisis)</text>
      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="900">Fructosa-1,6-Bisfosfatasa-1 (FBPasa-1)</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 3.1.3.11 (Paso Limitante Clave)</text>
        <text x="0" y="32" fill="#16a34a" font-size="11" font-weight="700">⊕ Citrato, ATP (Señal de carga energética alta)</text>
        <text x="0" y="46" fill="#e11d48" font-size="11" font-weight="700">⊣ F-2,6-BP, AMP (Inhibición potente alostérica)</text>
      </g>
    </g>
    """)

    # Fructosa-6-Fosfato
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=620,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Cetosa)",
        detalle="Substrato de isomerización a aldosa",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        dx_texto=140
    ))

    # Reacción Reversa: Fosfoglucosa Isomerasa
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=530,
        enzima="Fosfoglucosa Isomerasa",
        ec="EC 5.3.1.9 (⇄)",
        reversible=True
    ))

    # Glucosa-6-Fosfato
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=420,
        nombre="Glucosa-6-Fosfato (G-6-P)",
        carbonos="6 Carbonos (Hexosa Fosforilada)",
        detalle="Transportada al Retículo Endoplásmico para el clivaje final",
        svg_estructura=GLUCOSA_6_FOSFATO,
        dx_texto=140
    ))

    # =========================================================================
    # BYPASS 3: RETÍCULO ENDOPLÁSMICO Y GLUCOSA-6-FOSFATASA
    # =========================================================================
    svg_parts.append(f"""
    <!-- Complejo de la Glucosa-6-Fosfatasa en el RE (Bypass 3) -->
    <g transform="translate(180, 360)">
      {RE_GLUCOSA_6_FOSFATASA}
      <g transform="translate(0, 95)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="13.5" font-weight="900" fill="#0f172a">
          Glucosa-6-Fosfatasa (EC 3.1.3.9)
        </text>
        <text x="0" y="18" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#b45309">
          • Exclusiva de Hígado y Riñón (Músculo carece de ella)
        </text>
        <text x="0" y="34" font-family="'Inter', sans-serif" font-size="10.5" fill="#475569">
          • T1 transporta G-6-P al lumen; la fosfatasa hidroliza el fosfato;
        </text>
        <text x="0" y="48" font-family="'Inter', sans-serif" font-size="10.5" fill="#475569">
          • T2/T3 devuelven Glucosa libre y Pi al citosol para su exportación.
        </text>
      </g>
    </g>

    <!-- Flechas hacia el complejo del RE y regreso de glucosa libre -->
    <path d="M 620 450 Q 420 450 360 410" fill="none" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arrowBlue)"/>
    <path d="M 360 380 Q 520 350 620 310" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
    """)

    # D-Glucosa Libre (Producto Final en x=X_EJE, y=270)
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=270,
        nombre="D-Glucosa Libre",
        carbonos="6 Carbonos (Glucosa neutra exportable)",
        detalle="Asciende hacia el transportador GLUT-2 para exportación sanguínea",
        svg_estructura=GLUCOSA,
        dx_texto=140
    ))

    # Flecha desde D-Glucosa libre hacia GLUT-2 en la membrana plasmática
    svg_parts.append("""
    <line x1="675" y1="260" x2="675" y2="135" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    """)

    # =========================================================================
    # PANELES LATERALES DE RIGOR UNIVERSITARIO
    # =========================================================================
    svg_parts.append("""
    <!-- PANEL DE BALANCE ENERGÉTICO GLOBAL -->
    <g transform="translate(920, 1270)">
      <rect x="0" y="0" width="390" height="245" rx="12" fill="#ffffff" stroke="#ea580c" stroke-width="2.2" filter="drop-shadow(0 4px 10px rgba(0,0,0,0.06))"/>
      <text x="20" y="30" fill="#0f172a" font-size="15" font-weight="900">BALANCE ENERGÉTICO GLOBAL</text>
      <text x="20" y="52" fill="#c2410c" font-size="12" font-weight="800">Costo estequiométrico por 1 Glucosa:</text>
      <text x="20" y="78" fill="#dc2626" font-size="12.5" font-weight="700">• 2 Piruvato Carboxilasa ➔ - 2 ATP</text>
      <text x="20" y="98" fill="#dc2626" font-size="12.5" font-weight="700">• 2 PEPCK Citosólica ➔ - 2 GTP</text>
      <text x="20" y="118" fill="#dc2626" font-size="12.5" font-weight="700">• 2 Fosfoglicerato Quinasa ➔ - 2 ATP</text>
      <text x="20" y="138" fill="#059669" font-size="12.5" font-weight="700">• 2 GAPDH ➔ - 2 NADH + 2 H⁺</text>
      
      <line x1="20" y1="154" x2="370" y2="154" stroke="#e2e8f0" stroke-width="1.5"/>
      <text x="20" y="176" fill="#0f172a" font-size="12.5" font-weight="900">GASTO TOTAL: 6 Enlaces ~P</text>
      <text x="20" y="196" fill="#64748b" font-size="10.5">2 Piruvato + 4 ATP + 2 GTP + 2 NADH + 6 H₂O ➔</text>
      <text x="20" y="210" fill="#64748b" font-size="10.5">Glucosa + 4 ADP + 2 GDP + 6 Pi + 2 NAD⁺</text>
      <text x="20" y="228" fill="#047857" font-size="10.5" font-weight="700">ΔG'° ≈ -37.7 kJ/mol (Fisiológicamente Irreversible)</text>
    </g>

    <!-- PANEL DE PRECURSORES GLUCONEOGÉNICOS -->
    <g transform="translate(920, 1560)">
      <rect x="0" y="0" width="390" height="190" rx="12" fill="#f8fafc" stroke="#64748b" stroke-width="2"/>
      <text x="20" y="28" fill="#0f172a" font-size="14.5" font-weight="900">PRECURSORES NO GLUCÍDICOS</text>
      
      <text x="20" y="54" fill="#b45309" font-size="12" font-weight="800">1. Lactato (Ciclo de Cori):</text>
      <text x="20" y="70" fill="#475569" font-size="11">Músculo en esfuerzo anaeróbico y eritrocitos ➔ Hígado.</text>

      <text x="20" y="96" fill="#0284c7" font-size="12" font-weight="800">2. Glicerol (Lipólisis de TAG):</text>
      <text x="20" y="112" fill="#475569" font-size="11">Glicerol Quinasa ➔ Glicerol-3-P ➔ DHAP (Citosol).</text>

      <text x="20" y="138" fill="#047857" font-size="12" font-weight="800">3. Aminoácidos Glucogénicos:</text>
      <text x="20" y="154" fill="#475569" font-size="11">Alanina (Ciclo Glucosa-Alanina) y Glutamina ➔ Piruvato/OAA.</text>
      <text x="20" y="172" fill="#dc2626" font-size="10.5" font-weight="700">* Leucina y Lisina son exclusivamente cetogénicos (no rinden glucosa).</text>
    </g>
    """)

    # Ensamblar HTML completo
    html_final = CABECERA_HTML + "\n".join(svg_parts) + PIE_HTML

    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_salida = os.path.join(dir_actual, "Gluconeogenesis.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(html_final)

    # Extraer y escribir Gluconeogenesis.svg puro
    inicio_svg = html_final.find("<svg ")
    fin_svg = html_final.rfind("</svg>") + 6
    if inicio_svg != -1 and fin_svg != -1:
        svg_puro = html_final[inicio_svg:fin_svg]
        ruta_svg = os.path.join(dir_actual, "Gluconeogenesis.svg")
        with open(ruta_svg, "w", encoding="utf-8") as f_svg:
            f_svg.write(svg_puro)
        print(f"✅ SVG puro guardado en: {ruta_svg}")

    print(f"✅ Mapa Individual de Gluconeogénesis generado con éxito en: {ruta_salida}")

if __name__ == "__main__":
    generar_mapa_gluconeogenesis()
