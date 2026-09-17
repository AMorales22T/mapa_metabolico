#!/usr/bin/env python3
"""
MAPA INTEGRADO DE CARBOHIDRATOS: GLUCOGÉNESIS • GLUCÓLISIS • PENTOSAS FOSFATO
=============================================================================
Este mapa integra lateralmente las tres rutas principales de carbohidratos
sin modificar ninguno de los módulos individuales existentes:
1. IZQUIERDA: Metabolismo del Glucógeno (Glucogénesis)
   - G-6-P ⇄ G-1-P ➔ UDP-Glucosa ➔ Cebador Glucogenina con Lupa Molecular ➔
     Glucógeno Sintasa ➔ Enzima Ramificadora ➔ Gránulo de inclusión citosólico.
2. CENTRO: Glucólisis Completa (11 metabolitos y 10 reacciones)
   - Membrana continua con receptor GLUT-4 y Lupa de Difusión Facilitada.
   - El nodo Glucosa-6-Fosfato (G-6-P) como centro distribuidor triple.
   - Bifurcación de Aldolasa (DHAP y GAP con TPI horizontal).
   - Fase de Rendimiento completa hasta Piruvato y transportador MPC mitocondrial.
3. DERECHA: Vía de las Pentosas Fosfato (10 metabolitos)
   - Fase Oxidativa: G6PDH, Lactonasa, 6-PGDH (producción de 2 NADPH y CO2).
   - Fase No Oxidativa: TK1, Transaldolasa y TK2.
   - Salida hacia Síntesis de Nucleótidos (PRPP).
   - Las 3 conexiones biológicas de retorno hacia F-6-P y GAP de la Glucólisis.
4. ENTORNO CONTINUO:
   - Membrana plasmática bicapa continua que cruza de izquierda a derecha.
   - Citoesqueleto continuo, polirribosomas y vesículas translúcidas.
   - Estilo editorial biológico idéntico a las láminas individuales.
"""

import os
import sys

DIR_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(DIR_BASE, "01_glucolisis"))
sys.path.append(os.path.join(DIR_BASE, "04_via_pentosas_fosfato"))
sys.path.append(os.path.join(DIR_BASE, "03_glucogenogenesis_y_glucogenolisis"))

from estructuras_glucosa import (
    GLUCOSA, GLUCOSA_6_FOSFATO, FRUCTOSA_6_FOSFATO, FRUCTOSA_1_6_BISFOSFATO,
    DIHIDROXIACETONA_FOSFATO, GLICERALDEHIDO_3_FOSFATO, BISFOSFOGLICERATO_1_3,
    FOSFOGLICERATO_3, FOSFOGLICERATO_2, FOSFOENOLPIRUVATO, PIRUVATO
)

from estructuras_pentosas import (
    FOSFOGLUCONO_LACTONA_6, FOSFOGLUCONATO_6, RIBULOSA_5_FOSFATO,
    RIBOSA_5_FOSFATO, XILULOSA_5_FOSFATO, SEDOHEPTULOSA_7_FOSFATO, ERITROSA_4_FOSFATO
)

from estructuras_glucogeno import (
    GLUCOSA_1_FOSFATO, UDP_GLUCOSA, CEBADOR_GLUCOGENINA,
    LUPA_MECANISMO_CEBADOR, CADENA_GLUCOGENO, GRANULO_CITOSOLICO_INCLUSION
)

ANCHO_CANVAS = 3300
ALTO_CANVAS = 2550

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Metabolismo Integrado de Carbohidratos - Glucogénesis • Glucólisis • Pentosas</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #cbd5e1;
      color: #0f172a;
      padding: 25px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .lienzo-svg {{
      width: 100%;
      max-width: {ANCHO_CANVAS}px;
      background: #ffffff;
      border: 1px solid #94a3b8;
      border-radius: 12px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Marcadores de flechas estandarizados -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>
        <marker id="arrowPurple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
        </marker>

        <!-- Gradiente citoplasmático unificado -->
        <linearGradient id="gradCitosolUnificado" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#ffffff" stop-opacity="1" />
          <stop offset="8%" stop-color="#f8fafc" stop-opacity="0.85" />
          <stop offset="50%" stop-color="#f0fdf4" stop-opacity="0.3" />
          <stop offset="85%" stop-color="#f8fafc" stop-opacity="0.85" />
          <stop offset="100%" stop-color="#ffffff" stop-opacity="1" />
        </linearGradient>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def generar_entorno_celular_continuo(ancho, alto):
    """Genera la membrana continua superior, citoesqueleto y mitocondria."""
    return f"""
    <!-- Fondo Citoplasmático Acuoso -->
    <rect width="{ancho}" height="{alto}" fill="url(#gradCitosolUnificado)"/>

    <!-- ============================================================= -->
    <!-- MEMBRANA PLASMÁTICA CONTINUA (CRUZA TODO EL CITOSOL ARRIBA)   -->
    <!-- ============================================================= -->
    <!-- Espacio Extracelular / Sangre -->
    <path d="M 0 0 L {ancho} 0 L {ancho} 75 Q {ancho*0.5} 90 0 75 Z" fill="#f1f5f9"/>
    <line x1="0" y1="75" x2="{ancho}" y2="75" stroke="#cbd5e1" stroke-width="2"/>
    <text x="{ancho/2}" y="36" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#64748b" text-anchor="middle" letter-spacing="2">
      ESPACIO EXTRACELULAR (SANGRE / LÍQUIDO INTERSTICIAL)
    </text>

    <!-- Bicapa Fosfolipídica Ondulada Continua -->
    <g stroke="#0284c7" stroke-width="2.5" fill="none">
      <path d="M 0 77 Q 500 90 1100 78 T 2200 84 T {ancho} 78" />
      <path d="M 0 89 Q 500 102 1100 90 T 2200 96 T {ancho} 90" />
    </g>
    <!-- Cabezas polares de fosfolípidos a lo largo de toda la membrana -->
    <g fill="#38bdf8" opacity="0.55">
      {' '.join([f'<circle cx="{i}" cy="{77 + (i%4)}" r="2.5"/><circle cx="{i}" cy="{89 + (i%4)}" r="2.5"/>' for i in range(20, ancho, 30)])}
    </g>

    <!-- ============================================================= -->
    <!-- RECEPTOR GLUT-4 CON LUPA MOLECULAR (EN EL EJE GLUCOLÍTICO)    -->
    <!-- ============================================================= -->
    <g transform="translate(1480, 68)">
      <path d="M 0 5 C 10 -12, 28 -12, 34 5 C 38 18, 34 36, 25 42 C 12 45, 2 35, 0 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <path d="M 80 5 C 70 -12, 52 -12, 46 5 C 42 18, 46 36, 55 42 C 68 45, 78 35, 80 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <ellipse cx="40" cy="20" rx="10" ry="18" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8"/>
      <polygon points="40,14 45,17 45,23 40,26 35,23 35,17" fill="#ffffff" stroke="#ea580c" stroke-width="1.6"/>
      <circle cx="35" cy="17" r="2" fill="#dc2626"/>
      <text x="40" y="49" fill="#0369a1" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-4</text>
    </g>

    <line x1="1520" y1="42" x2="1520" y2="68" stroke="#ea580c" stroke-width="2.2"/>
    <line x1="1520" y1="108" x2="1520" y2="135" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

    <!-- Lupa Molecular del GLUT-4 -->
    <g stroke="#38bdf8" stroke-width="1.4" stroke-dasharray="4 3" opacity="0.7">
      <line x1="1480" y1="88" x2="1335" y2="115" />
      <line x1="1490" y1="68" x2="1300" y2="65" />
    </g>
    <g transform="translate(1230, 110)">
      <circle cx="0" cy="0" r="68" fill="#ffffff" stroke="#0284c7" stroke-width="3.5" />
      <circle cx="0" cy="0" r="64" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
      <g opacity="0.85">
        <g fill="#0284c7">
          <circle cx="-50" cy="-8" r="5"/><circle cx="-36" cy="-8" r="5"/><circle cx="-22" cy="-8" r="5"/>
          <circle cx="22" cy="-8" r="5"/><circle cx="36" cy="-8" r="5"/><circle cx="50" cy="-8" r="5"/>
        </g>
        <g stroke="#94a3b8" stroke-width="1.4" fill="none">
          <path d="M -50 -3 Q -52 2 -48 7"/><path d="M -36 -3 Q -38 2 -34 7"/><path d="M -22 -3 Q -24 2 -20 7"/>
          <path d="M 22 -3 Q 20 2 24 7"/><path d="M 36 -3 Q 34 2 38 7"/><path d="M 50 -3 Q 48 2 52 7"/>
          <path d="M -50 17 Q -52 12 -48 7"/><path d="M -36 17 Q -38 12 -34 7"/><path d="M -22 17 Q -24 12 -20 7"/>
          <path d="M 22 17 Q 20 12 24 7"/><path d="M 36 17 Q 34 12 38 7"/><path d="M 50 17 Q 48 12 52 7"/>
        </g>
        <g fill="#0284c7">
          <circle cx="-50" cy="22" r="5"/><circle cx="-36" cy="22" r="5"/><circle cx="-22" cy="22" r="5"/>
          <circle cx="22" cy="22" r="5"/><circle cx="36" cy="22" r="5"/><circle cx="50" cy="22" r="5"/>
        </g>
      </g>
      <path d="M -18 -24 C -9 -28, -4 -16, -4 0 C -4 16, -9 28, -18 24 C -27 20, -25 -20, -18 -24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <path d="M 18 -24 C 9 -28, 4 -16, 4 0 C 4 16, 9 28, 18 24 C 27 20, 25 -20, 18 -24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <ellipse cx="0" cy="0" rx="6.5" ry="18" fill="#bae6fd" opacity="0.6"/>
      <g transform="translate(0, -6)">
        <polygon points="0,-10 9,-4 9,6 0,12 -9,6 -9,-4" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
        <circle cx="-9" cy="-4" r="3" fill="#ffffff"/>
        <text x="-9" y="-2" fill="#dc2626" font-size="6" font-weight="900" text-anchor="middle">O</text>
        <circle cx="14" cy="6" r="4" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
        <text x="14" y="8" fill="#ea580c" font-size="5" font-weight="900" text-anchor="middle">OH</text>
      </g>
      <path d="M 0 -26 L 0 -15" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <path d="M 0 10 L 0 26" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <rect x="-55" y="45" width="110" height="15" rx="4" fill="#0f172a" opacity="0.9"/>
      <text x="0" y="56" fill="#ffffff" font-size="7.5" font-weight="800" text-anchor="middle" letter-spacing="0.5">DIFUSIÓN FACILITADA</text>
    </g>

    <!-- ============================================================= -->
    <!-- CITOESQUELETO CONTINUO QUE CRUZA LAS TRES RUTAS               -->
    <!-- ============================================================= -->
    <g opacity="0.3" stroke="#94a3b8" fill="none">
      <path d="M 60 220 Q 800 150 1600 240 T {ancho-60} 200" stroke-width="1.7" stroke-dasharray="8 6"/>
      <path d="M 80 520 Q 900 600 1700 540 T {ancho-80} 560" stroke-width="1.5" stroke-dasharray="7 7"/>
      <path d="M 50 880 Q 850 820 1650 890 T {ancho-50} 860" stroke-width="1.6" stroke-dasharray="8 5"/>
      <path d="M 70 1350 Q 950 1420 1750 1370 T {ancho-70} 1390" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 60 1780 Q 850 1720 1650 1800 T {ancho-60} 1760" stroke-width="1.6" stroke-dasharray="6 6"/>
      <path d="M 80 2200 Q 750 2250 1450 2200 T {ancho-80} 2220" stroke-width="1.5" stroke-dasharray="7 7"/>
    </g>

    <!-- Polirribosomas en racimos libres en el citoplasma -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="180" cy="180" r="2.5"/><circle cx="186" cy="182" r="2"/><circle cx="184" cy="188" r="2.3"/>
      <circle cx="950" cy="220" r="2.5"/><circle cx="956" cy="222" r="2"/><circle cx="954" cy="228" r="2.3"/>
      <circle cx="2100" cy="240" r="2.5"/><circle cx="2106" cy="242" r="2"/><circle cx="2104" cy="248" r="2.3"/>
      <circle cx="3150" cy="380" r="2.5"/><circle cx="3156" cy="382" r="2"/><circle cx="3154" cy="388" r="2.3"/>
      <circle cx="160" cy="740" r="2.5"/><circle cx="166" cy="742" r="2"/><circle cx="164" cy="748" r="2.3"/>
      <circle cx="1100" cy="820" r="2.5"/><circle cx="1106" cy="822" r="2"/><circle cx="1104" cy="828" r="2.3"/>
      <circle cx="2150" cy="920" r="2.5"/><circle cx="2156" cy="922" r="2"/><circle cx="2154" cy="928" r="2.3"/>
      <circle cx="3180" cy="1200" r="2.5"/><circle cx="3186" cy="1202" r="2"/><circle cx="3184" cy="1208" r="2.3"/>
      <circle cx="200" cy="1650" r="2.5"/><circle cx="206" cy="1652" r="2"/><circle cx="204" cy="1658" r="2.3"/>
      <circle cx="1080" cy="1720" r="2.5"/><circle cx="1086" cy="1722" r="2"/><circle cx="1084" cy="1728" r="2.3"/>
      <circle cx="2200" cy="1600" r="2.5"/><circle cx="2206" cy="1602" r="2"/><circle cx="2204" cy="1608" r="2.3"/>
    </g>

    <!-- Vesículas citosólicas translúcidas de transporte -->
    <g opacity="0.28">
      <circle cx="200" cy="360" r="22" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="200" cy="360" r="16" fill="none" stroke="#7dd3fc" stroke-width="1"/>
      <circle cx="1050" cy="460" r="24" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="1050" cy="460" r="17" fill="none" stroke="#fbbf24" stroke-width="1"/>
      <circle cx="2150" cy="500" r="20" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="2150" cy="500" r="14" fill="none" stroke="#7dd3fc" stroke-width="1"/>
      <circle cx="3120" cy="650" r="26" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="3120" cy="650" r="19" fill="none" stroke="#7dd3fc" stroke-width="1"/>
    </g>

    <!-- ============================================================= -->
    <!-- MITOCONDRIA BIOLÓGICA EN LA BASE (RECEPTORA DE PIRUVATO)      -->
    <!-- ============================================================= -->
    <g id="mitocondria-base" transform="translate(1480, 2220)">
      <path d="M 0 60 C 250 10 750 10 1050 60 L 1050 280 L 0 280 Z" fill="#fffbeb" stroke="#ea580c" stroke-width="4"/>
      <path d="M 20 85 Q 80 125 140 90 T 260 95 T 380 90 T 500 100 T 620 90 T 740 95 T 860 90 T 980 95 T 1030 85" 
            fill="none" stroke="#f59e0b" stroke-width="2.8" stroke-dasharray="8 5"/>
      <rect x="0" y="100" width="1050" height="180" fill="#fef3c7" opacity="0.65"/>
      <rect x="30" y="42" width="34" height="38" rx="7" fill="#ea580c" stroke="#fed7aa" stroke-width="2"/>
      <text x="47" y="65" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">MPC</text>
      <text x="75" y="65" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#c2410c">Transportador Mitocondrial de Piruvato (MPC)</text>
      <text x="500" y="150" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#b45309" letter-spacing="1.5">
        MATRIZ MITOCONDRIAL (PDH • CICLO DE KREBS • CADENA RESPIRATORIA)
      </text>
    </g>
    """

def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False, dx_texto=135):
    """Generador modular de metabolitos con estructura y textos."""
    if texto_izquierda:
        pos_estructura = f"translate({dx_texto}, 0)"
        pos_texto = f"translate({dx_texto - 20}, 25)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = f"translate({dx_texto}, 25)"
        alineacion = ''

    return f"""
    <!-- Metabolito: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="{pos_estructura}">
        {svg_estructura}
      </g>
      <g transform="{pos_texto}">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800" {alineacion}>{nombre}</text>
        <text x="0" y="17" fill="#ea580c" font-size="11.5" font-weight="700" {alineacion}>{carbonos}</text>
        <text x="0" y="32" fill="#64748b" font-size="10.5" {alineacion}>{detalle}</text>
      </g>
    </g>
    """

def crear_reaccion(x, y, enzima, ec="", regulacion="", entra_energia="", sale_energia="", 
                   reversible=False, es_ganancia=False, salida_agua=False, altura=48):
    """Generador de reacción vertical estándar."""
    curvas_energia = ""
    if entra_energia:
        color_entrada = "#dc2626" if not es_ganancia else "#475569"
        marcador_entrada = "url(#arrowRed)" if not es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -75 8 Q -25 8 -4 18" fill="none" stroke="{color_entrada}" stroke-width="1.8" marker-end="{marcador_entrada}"/>
        <text x="-80" y="11" fill="{color_entrada}" font-size="10.5" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
    if sale_energia:
        color_salida = "#059669" if es_ganancia else "#475569"
        marcador_salida = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -4 24 Q -25 34 -75 34" fill="none" stroke="{color_salida}" stroke-width="1.8" marker-end="{marcador_salida}"/>
        <text x="-80" y="37" fill="{color_salida}" font-size="10.5" font-weight="800" text-anchor="end">{sale_energia}</text>
        """
    if salida_agua:
        curvas_energia += """
        <path d="M -4 24 Q -25 34 -70 34" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-75" y="37" fill="#0284c7" font-size="10.5" font-weight="800" text-anchor="end">- 2 H₂O</text>
        """

    if reversible:
        flecha = f"""
        <line x1="-3" y1="0" x2="-3" y2="{altura}" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        <line x1="3" y1="{altura}" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        """
    else:
        flecha = f"""
        <line x1="0" y1="0" x2="0" y2="{altura}" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="26" fill="{color_reg}" font-size="9.5" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha}
      {curvas_energia}
      <g transform="translate(18, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">{enzima}</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """

def crear_reaccion_oxidativa(x, y, enzima, ec="", regulacion="", genera_nadph=False, entra_agua=False, salida_co2=False, altura=48):
    """Generador de reacción de fase oxidativa de pentosas."""
    curvas = ""
    if genera_nadph:
        curvas += """
        <path d="M -65 8 Q -25 8 -4 18" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="-70" y="11" fill="#475569" font-size="10" font-weight="800" text-anchor="end">+ NADP⁺</text>
        <path d="M -4 24 Q -25 34 -70 34" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
        <text x="-75" y="38" fill="#059669" font-size="10" font-weight="800" text-anchor="end">+ NADPH + H⁺</text>
        """
    if entra_agua:
        curvas += """
        <path d="M -65 8 Q -25 8 -4 18" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-70" y="11" fill="#0284c7" font-size="10" font-weight="800" text-anchor="end">+ H₂O</text>
        """
    if salida_co2:
        curvas += """
        <path d="M 4 24 Q 25 34 65 34" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="70" y="38" fill="#475569" font-size="10" font-weight="800">+ CO₂</text>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="26" fill="{color_reg}" font-size="9" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción Oxidativa: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="0" y1="0" x2="0" y2="{altura}" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      {curvas}
      <g transform="translate(18, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">{enzima}</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """

def crear_paso_no_oxidativo(x, y, enzima, ec, sustratos_txt, productos_txt):
    """Generador de nodo de transferencia no oxidativa."""
    return f"""
    <!-- Reacción de Transferencia: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="-3" y1="0" x2="-3" y2="45" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="45" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(18, 10)">
        <text x="0" y="0" fill="#0f172a" font-size="12.5" font-weight="800">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        <text x="0" y="28" fill="#c2410c" font-size="9.5" font-weight="700">{sustratos_txt} ⇄ {productos_txt}</text>
      </g>
    </g>
    """

def generar_mapa_carbohidratos():
    """Compila las tres rutas conectadas biológicamente en el citosol unificado."""
    svg_parts = []

    # 1. Capa de entorno citoplasmático continuo
    svg_parts.append(generar_entorno_celular_continuo(ANCHO_CANVAS, ALTO_CANVAS))

    # =========================================================================
    # RUTA CENTRAL: LA GLUCÓLISIS (EJE X ≈ 1475 a 1520)
    # =========================================================================
    X_GLU = 1475
    X_FLECHA = 1520

    # 1. D-Glucosa
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=140,
        nombre="D-Glucosa",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Entrada directa desde el GLUT-4",
        svg_estructura=GLUCOSA
    ))

    # Reacción 1: Hexoquinasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=250,
        enzima="Hexoquinasa",
        ec="EC 2.7.1.1 (Mg²⁺)",
        regulacion="⊣ G-6-P | ⊕ Insulina",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 2. Glucosa-6-Fosfato (EL GRAN NODO CENTRAL DISTRIBUIDOR)
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=365,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa Ⓟ)",
        detalle="Nodo Central: Glucólisis • Glucógeno • Pentosas",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # Reacción 2: Fosfoglucosa Isomerasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=505,
        enzima="Fosfoglucosa Isomerasa",
        ec="EC 5.3.1.9 (⇄)",
        reversible=True
    ))

    # 3. Fructosa-6-Fosfato (RECIBE RETORNO DE PENTOSAS)
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=605,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Cetosa Ⓟ)",
        detalle="Punto receptor de Transcetolasa / Transaldolasa",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # Reacción 3: PFK-1
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=745,
        enzima="Fosfofructoquinasa-1 (PFK-1)",
        ec="EC 2.7.1.11 (Compromiso Clave)",
        regulacion="⊣ ATP, Citrato | ⊕ AMP, F-2,6-BP",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 4. Fructosa-1,6-Bisfosfato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=845,
        nombre="Fructosa-1,6-Bisfosfato",
        carbonos="6 Carbonos (Hexosa Bis-Ⓟ)",
        detalle="Sustrato de escisión aldólica",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO
    ))

    # Bifurcación Aldolasa y Triosas
    svg_parts.append(f"""
    <g transform="translate({X_FLECHA}, 965)">
      <path d="M -15 0 Q -100 25 -140 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <path d="M 15 0 Q 100 25 150 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(0, 24)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">Aldolasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 4.1.2.13 (⇄)</text>
      </g>
    </g>

    <!-- DHAP (Izquierda del eje central) -->
    {crear_metabolito(
        x=1250, y=1045,
        nombre="Dihidroxiacetona-P",
        carbonos="3 Carbonos (Cetotriosa)",
        detalle="Interconvertible con GAP",
        svg_estructura=DIHIDROXIACETONA_FOSFATO,
        texto_izquierda=True
    )}

    <!-- GAP (Derecha del eje central) -->
    {crear_metabolito(
        x=1690, y=1045,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Aldotriosa)",
        detalle="Continúa hacia el rendimiento",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    )}

    <!-- TPI Horizontal Reversible -->
    <g transform="translate({X_FLECHA}, 1075)">
      <line x1="-90" y1="-3" x2="80" y2="-3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="80" y1="3" x2="-90" y2="3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <text x="-5" y="-12" fill="#0f172a" font-size="10.5" font-weight="800" text-anchor="middle">Triosa Fosfato Isomerasa (TPI)</text>
      <text x="-5" y="16" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1 (⇄)</text>
    </g>

    <!-- Transición a Fase 2 -->
    <path d="M 1730 1145 Q 1730 1180 1520 1200" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <g transform="translate(1520, 1185)">
      <rect x="-95" y="-11" width="190" height="22" rx="11" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
      <text x="0" y="4" fill="#c2410c" font-size="10.5" font-weight="800" text-anchor="middle">FASE 2: RENDIMIENTO (× 2)</text>
    </g>
    """)

    # Fase de Rendimiento
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1220,
        enzima="GAPDH",
        ec="EC 1.2.1.12 (⇄)",
        entra_energia="+ 2 NAD⁺ + 2 Pi",
        sale_energia="+ 2 NADH + 2 H⁺",
        reversible=True,
        es_ganancia=True
    ))

    # 5. 1,3-BPG
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1315,
        nombre="1,3-Bisfosfoglicerato",
        carbonos="3 Carbonos (Acil-fosfato)",
        detalle="Fosforilación a nivel de sustrato",
        svg_estructura=BISFOSFOGLICERATO_1_3
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1435,
        enzima="Fosfoglicerato Quinasa (PGK)",
        ec="EC 2.7.2.3 (⇄)",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        reversible=True,
        es_ganancia=True
    ))

    # 6. 3-PG
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1530,
        nombre="3-Fosfoglicerato",
        carbonos="3 Carbonos (Ácido carboxílico Ⓟ)",
        detalle="Intermediario glucolítico",
        svg_estructura=FOSFOGLICERATO_3
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1650,
        enzima="Fosfogliceromutasa",
        ec="EC 5.4.2.11 (⇄)",
        reversible=True
    ))

    # 7. 2-PG
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1740,
        nombre="2-Fosfoglicerato",
        carbonos="3 Carbonos (Éster interno)",
        detalle="Sustrato de la enolasa",
        svg_estructura=FOSFOGLICERATO_2
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1850,
        enzima="Enolasa",
        ec="EC 4.2.1.11 (Mg²⁺, ⇄)",
        salida_agua=True,
        reversible=True
    ))

    # 8. PEP
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1950,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 Carbonos (Enol-fosfato)",
        detalle="Mayor potencial de transferencia Ⓟ",
        svg_estructura=FOSFOENOLPIRUVATO
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=2080,
        enzima="Piruvato Quinasa",
        ec="EC 2.7.1.40 (K⁺, Mg²⁺)",
        regulacion="⊣ ATP, Alanina | ⊕ F-1,6-BP",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True
    ))

    # 9. Piruvato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=2180,
        nombre="Piruvato",
        carbonos="3 Carbonos (α-Cetoácido)",
        detalle="Nodo terminal hacia MPC mitocondrial",
        svg_estructura=PIRUVATO
    ))

    # Conexión Piruvato -> Mitocondria
    svg_parts.append("""
    <path d="M 1630 2230 Q 1700 2230 1515 2240" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
    """)


    # =========================================================================
    # RUTA LATERAL IZQUIERDA: GLUCOGÉNESIS (SÍNTESIS DE GLUCÓGENO)
    # =========================================================================
    # FLECHA DE CONEXIÓN G-6-P -> GLUCOGÉNESIS
    svg_parts.append("""
    <!-- Conexión horizontal desde G-6-P hacia la Glucogénesis -->
    <path d="M 1430 395 Q 1000 340 700 395" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
    <g transform="translate(1060, 345)">
      <rect x="-105" y="-12" width="210" height="24" rx="12" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
      <text x="0" y="4" fill="#c2410c" font-size="10" font-weight="800" text-anchor="middle">
        HACIA LA SÍNTESIS DE GLUCÓGENO
      </text>
    </g>
    """)

    # 1. Reacción Fosfoglucomutasa (en la conexión hacia la izquierda)
    svg_parts.append("""
    <g transform="translate(850, 395)">
      <path d="M -30 -12 Q -10 -22 10 -12" fill="none" stroke="#475569" stroke-width="1.6" marker-end="url(#arrowSlate)"/>
      <text x="-25" y="-26" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#475569">Ser-OH Fosforilada</text>
      <text x="0" y="-5" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">Fosfoglucomutasa</text>
      <text x="0" y="8" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#64748b" text-anchor="middle">EC 5.4.2.2 (⇄)</text>
    </g>
    """)

    # 2. α-D-Glucosa-1-Fosfato (G-1-P)
    svg_parts.append(crear_metabolito(
        x=450, y=365,
        nombre="α-D-Glucosa-1-Fosfato",
        carbonos="6 Carbonos (Fosfato en C1-α)",
        detalle="Substrato de activación por UTP",
        svg_estructura=GLUCOSA_1_FOSFATO,
        dx_texto=175
    ))

    # Reacción 2: UDP-Glucosa Pirofosforilasa
    svg_parts.append("""
    <g transform="translate(495, 520)">
      <line x1="0" y1="0" x2="0" y2="60" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M -65 10 Q -20 10 -4 20" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-70" y="13" fill="#dc2626" font-size="10.5" font-weight="800" text-anchor="end">- 1 UTP</text>
      <path d="M -4 30 Q -20 40 -65 40" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-70" y="44" fill="#475569" font-size="10" font-weight="800" text-anchor="end">+ PPᵢ ➔ 2 Pᵢ</text>
      <g transform="translate(18, 16)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">UDP-Glucosa Pirofosforilasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">EC 2.7.7.9 (Mg²⁺)</text>
        <text x="0" y="26" fill="#16a34a" font-size="9" font-weight="700">⊕ Impulsada por Pirofosfatasa</text>
      </g>
    </g>
    """)

    # 3. UDP-Glucosa
    svg_parts.append(crear_metabolito(
        x=340, y=650,
        nombre="UDP-Glucosa",
        carbonos="Nucleótido-Azúcar activado",
        detalle="Donador de unidades glucosilo",
        svg_estructura=UDP_GLUCOSA,
        dx_texto=280
    ))

    # 4. Cebador de Glucogenina + Lupa Molecular
    Y_CEB = 820
    svg_parts.append(f"""
    <!-- CEBADOR MOLECULAR DE GLUCOGENINA -->
    <g transform="translate(250, {Y_CEB})">
      {CEBADOR_GLUCOGENINA}
      <g transform="translate(370, 22)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900">Cebador: Glucogenina-(Glc)₈</text>
        <text x="0" y="16" fill="#b45309" font-size="11" font-weight="700">Dímero autoglucosilante (Tyr-194)</text>
        <text x="0" y="30" fill="#dc2626" font-size="10" font-weight="800">• Extremo 4-OH aceptor libre</text>
      </g>
    </g>

    <!-- Lupa de Zoom Molecular del acoplamiento catalítico -->
    <g stroke="#ea580c" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.65">
      <line x1="550" y1="{Y_CEB + 30}" x2="380" y2="{Y_CEB + 160}"/>
    </g>
    <g transform="translate(300, {Y_CEB + 190})">
      {LUPA_MECANISMO_CEBADOR}
    </g>
    """)

    # Reacción 3: Glucógeno Sintasa
    Y_RX_SINT = Y_CEB + 320
    svg_parts.append(f"""
    <g transform="translate(495, {Y_RX_SINT})">
      <line x1="0" y1="0" x2="0" y2="55" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M -4 25 Q -20 35 -65 35" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="-70" y="38" fill="#0284c7" font-size="10" font-weight="800" text-anchor="end">+ UDP libre</text>
      <g transform="translate(18, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">Glucógeno Sintasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">EC 2.4.1.11 (Elongación α-1,4)</text>
        <text x="0" y="26" fill="#16a34a" font-size="9" font-weight="700">⊕ Insulina, G-6-P | ⊣ Glucagón</text>
      </g>
    </g>
    """)

    # Reacción 4: Enzima Ramificadora
    Y_RX_RAM = Y_RX_SINT + 80
    svg_parts.append(f"""
    <g transform="translate(495, {Y_RX_RAM})">
      <line x1="0" y1="0" x2="0" y2="50" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <g transform="translate(18, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">Enzima Ramificadora</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">EC 2.4.1.18 (Ramas α-1,6)</text>
      </g>
    </g>
    """)

    # Polímero de Glucógeno y Gránulo Citosólico
    Y_GLUCO_POL = Y_RX_RAM + 75
    svg_parts.append(f"""
    <g transform="translate(360, {Y_GLUCO_POL})">
      <g transform="translate(0, 35)">
        {CADENA_GLUCOGENO}
      </g>
      <g transform="translate(360, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="900">Glucógeno (n + 1)</text>
        <text x="0" y="16" fill="#d97706" font-size="11.5" font-weight="800">Enlaces α(1→4) y ramificaciones α(1→6)</text>
      </g>
    </g>

    <!-- Gránulo de Inclusión Citosólica -->
    <g transform="translate(260, {Y_GLUCO_POL + 160})">
      <rect x="0" y="0" width="560" height="135" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="1.6"/>
      <g transform="translate(10, 8)">
        {GRANULO_CITOSOLICO_INCLUSION}
      </g>
      <g transform="translate(150, 22)">
        <text x="0" y="0" fill="#92400e" font-size="11.5" font-weight="900">GRÁNULO CITOSÓLICO DE INCLUSIÓN (~20-30 nm)</text>
        <text x="0" y="18" fill="#0f172a" font-size="9.5" font-weight="700">• No membranoso e insoluble: Almacena glucosa sin riesgo osmótico.</text>
        <text x="0" y="34" fill="#dc2626" font-size="9.5" font-weight="700">• Nunca sale como polímero: Solo sale como glucosa libre hepática.</text>
        <text x="0" y="50" fill="#047857" font-size="9">Degradación in situ por Fosforilasa ➔ G-1-P ➔ G-6-P ➔ GLUT-2.</text>
      </g>
    </g>
    """)


    # =========================================================================
    # RUTA LATERAL DERECHA: VÍA DE LAS PENTOSAS FOSFATO (X ≈ 2200 a 3100)
    # =========================================================================
    # FLECHA DE CONEXIÓN G-6-P -> PENTOSAS
    svg_parts.append("""
    <!-- Conexión horizontal desde G-6-P hacia las Pentosas -->
    <path d="M 1630 395 Q 1950 340 2260 395" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
    <g transform="translate(1950, 345)">
      <rect x="-105" y="-12" width="210" height="24" rx="12" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
      <text x="0" y="4" fill="#6d28d9" font-size="10" font-weight="800" text-anchor="middle">
        HACIA EL SHUNT DE PENTOSAS
      </text>
    </g>
    """)

    # Reacción G6PDH
    svg_parts.append(f"""
    <g transform="translate(2100, 395)">
      <path d="M -30 -12 Q -10 -22 10 -12" fill="none" stroke="#475569" stroke-width="1.6" marker-end="url(#arrowSlate)"/>
      <text x="-25" y="-24" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#475569">+ NADP⁺</text>
      <path d="M -30 12 Q -10 22 10 12" fill="none" stroke="#059669" stroke-width="1.6" marker-end="url(#arrowGreen)"/>
      <text x="-25" y="28" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#059669">+ NADPH</text>
      <text x="0" y="-5" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">G6PDH</text>
      <text x="0" y="8" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#64748b" text-anchor="middle">EC 1.1.1.49</text>
    </g>
    """)

    # 1. 6-Fosfoglucono-δ-Lactona
    svg_parts.append(crear_metabolito(
        x=2280, y=365,
        nombre="6-Fosfoglucono-δ-Lactona",
        carbonos="6 Carbonos (Lactona)",
        detalle="Éster intramolecular hidrolizable",
        svg_estructura=FOSFOGLUCONO_LACTONA_6
    ))

    # Reacción 2: Lactonasa
    svg_parts.append("""
    <g transform="translate(2540, 415)">
      <line x1="0" y1="0" x2="55" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M 10 -12 Q 28 -22 45 -12" fill="none" stroke="#0284c7" stroke-width="1.6" marker-end="url(#arrowBlue)"/>
      <text x="28" y="-25" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#0284c7" text-anchor="middle">+ H₂O</text>
      <text x="28" y="15" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">Lactonasa</text>
    </g>
    """)

    # 2. 6-Fosfogluconato
    svg_parts.append(crear_metabolito(
        x=2650, y=365,
        nombre="6-Fosfogluconato",
        carbonos="6 Carbonos (Cadena lineal)",
        detalle="Ácido descarboxilable generador de NADPH",
        svg_estructura=FOSFOGLUCONATO_6
    ))

    # Reacción 3: 6-PGDH bajando a Ribulosa-5-P
    svg_parts.append(crear_reaccion_oxidativa(
        x=2780, y=520,
        enzima="6-Fosfogluconato Deshidrogenasa",
        ec="EC 1.1.1.44 (Descarboxilación)",
        genera_nadph=True,
        salida_co2=True,
        altura=54
    ))

    # 3. Ribulosa-5-P
    svg_parts.append(crear_metabolito(
        x=2650, y=605,
        nombre="D-Ribulosa-5-Fosfato",
        carbonos="5 Carbonos (Pentosa Cetosa)",
        detalle="Cruce a la fase no oxidativa",
        svg_estructura=RIBULOSA_5_FOSFATO
    ))

    # Ramificación X5P y R5P
    svg_parts.append("""
    <g transform="translate(2780, 755)">
      <path d="M -20 0 Q -100 25 -150 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(-165, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="10.5" font-weight="800" text-anchor="end">Fosfopentosa Epimerasa</text>
        <text x="0" y="12" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 5.1.3.1 (⇄)</text>
      </g>
      <path d="M 20 0 Q 100 25 160 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(155, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="10.5" font-weight="800">Fosfopentosa Isomerasa</text>
        <text x="0" y="12" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace">EC 5.3.1.6 (⇄)</text>
      </g>
    </g>
    """)

    # 4a. Xilulosa-5-P
    svg_parts.append(crear_metabolito(
        x=2400, y=835,
        nombre="D-Xilulosa-5-P",
        carbonos="5 Carbonos (Epímero C3)",
        detalle="Donador de 2C (TPP)",
        svg_estructura=XILULOSA_5_FOSFATO,
        texto_izquierda=True
    ))

    # 4b. Ribosa-5-P
    svg_parts.append(crear_metabolito(
        x=2880, y=835,
        nombre="D-Ribosa-5-P",
        carbonos="5 Carbonos (Pentosa Aldosa)",
        detalle="Precursora de Nucleótidos",
        svg_estructura=RIBOSA_5_FOSFATO
    ))

    # Salida hacia Síntesis de Nucleótidos
    svg_parts.append("""
    <g transform="translate(2930, 970)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
      <g transform="translate(0, 42)">
        <rect x="-90" y="0" width="180" height="36" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
        <text x="0" y="15" fill="#6d28d9" font-size="10" font-weight="900" text-anchor="middle">SÍNTESIS DE NUCLEÓTIDOS</text>
        <text x="0" y="28" fill="#7c3aed" font-size="8.5" font-weight="600" text-anchor="middle">PRPP ➔ ARN, ADN, ATP, GTP</text>
      </g>
    </g>
    """)

    # Fase No Oxidativa: TK1, TA, TK2
    svg_parts.append(crear_paso_no_oxidativo(
        x=2680, y=1025,
        enzima="Transcetolasa (TK1)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Ribosa-5-P (5C)",
        productos_txt="GAP (3C) + Sedoheptulosa-7-P (7C)"
    ))

    # Sedoheptulosa-7-P
    svg_parts.append(crear_metabolito(
        x=2400, y=1105,
        nombre="Sedoheptulosa-7-P",
        carbonos="7 Carbonos (Cetosa)",
        detalle="Intermediario de 7C",
        svg_estructura=SEDOHEPTULOSA_7_FOSFATO,
        texto_izquierda=True
    ))

    # GAP intermediario
    svg_parts.append(crear_metabolito(
        x=2880, y=1105,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="Intermediario transferible",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))

    # TA
    svg_parts.append(crear_paso_no_oxidativo(
        x=2680, y=1255,
        enzima="Transaldolasa (TA)",
        ec="EC 2.2.1.2 (Base de Schiff con Lisina)",
        sustratos_txt="Sedoheptulosa-7-P (7C) + GAP (3C)",
        productos_txt="Fructosa-6-P (6C) + Eritrosa-4-P (4C)"
    ))

    # Eritrosa-4-P
    svg_parts.append(crear_metabolito(
        x=2400, y=1335,
        nombre="D-Eritrosa-4-P",
        carbonos="4 Carbonos (Tetrosa)",
        detalle="Aceptor para segunda transcetolasa",
        svg_estructura=ERITROSA_4_FOSFATO,
        texto_izquierda=True
    ))

    # F6P (1er reingreso)
    svg_parts.append(crear_metabolito(
        x=2880, y=1335,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡1.er Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # TK2
    svg_parts.append(crear_paso_no_oxidativo(
        x=2680, y=1485,
        enzima="Transcetolasa (TK2)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Eritrosa-4-P (4C)",
        productos_txt="Fructosa-6-P (6C) + GAP (3C)"
    ))

    # F6P (2º reingreso)
    svg_parts.append(crear_metabolito(
        x=2400, y=1565,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡2.º Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        texto_izquierda=True
    ))

    # GAP (2º reingreso)
    svg_parts.append(crear_metabolito(
        x=2880, y=1565,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="¡Reingreso de triosa a la Glucólisis!",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))

    # =========================================================================
    # LAS 3 FLECHAS DE RETORNO HACIA LA GLUCÓLISIS CENTRAL
    # =========================================================================
    svg_parts.append("""
    <!-- RETORNO 1: Fructosa-6-P hacia F6P Central -->
    <path d="M 2870 1375 C 2350 1300 1900 950 1630 635" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(2050, 900)">
      <rect x="-85" y="-11" width="170" height="22" rx="11" fill="#ecfdf5" stroke="#059669" stroke-width="1.6"/>
      <text x="0" y="4" fill="#047857" font-size="10" font-weight="800" text-anchor="middle">RETORNO: F-6-P A GLUCÓLISIS</text>
    </g>

    <!-- RETORNO 2: GAP hacia GAP Central -->
    <path d="M 2870 1600 C 2400 1550 1980 1300 1800 1095" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(2250, 1380)">
      <rect x="-85" y="-11" width="170" height="22" rx="11" fill="#ecfdf5" stroke="#059669" stroke-width="1.6"/>
      <text x="0" y="4" fill="#047857" font-size="10" font-weight="800" text-anchor="middle">RETORNO: GAP A GLUCÓLISIS</text>
    </g>
    """)

    # Ensamblar HTML completo
    html_final = CABECERA_HTML + "\n".join(svg_parts) + PIE_HTML

    ruta_salida = os.path.join(os.path.dirname(__file__), "Carbohidratos_Unidos.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"✅ Mapa Integrado de Carbohidratos generado con éxito en: {ruta_salida}")

if __name__ == "__main__":
    generar_mapa_carbohidratos()
