#!/usr/bin/env python3
"""
MAPA INDIVIDUAL DE LA GLUCONEOGÉNESIS (VÍA ANABÓLICA DE LA GLUCOSA)
===================================================================
Visualización de Biología Estructural y Bioquímica Universitaria.
Diseñado bajo el rigor de los apuntes oficiales de Metabolismo:
- Énfasis absoluto en las ESTRUCTURAS QUÍMICAS (Fischer, Haworth, Kekulé).
- Integración visual de los PUNTOS DE REGULACIÓN COORDINADOS (Apuntes Tema 4):
  1. Utilización del Piruvato: Acetil-CoA (+) activa PC, (-) inhibe PDH; (-) ADP frena PC.
  2. Utilización del Oxalacetato: Carga energética; (-) ADP inhibe PEPCK; inducción por Glucagón/Cortisol.
  3. El Conmutador Maestro F-6-P <-> F-1,6-BP: Enzima Bifuncional PFK-2 / FBPasa-2 y F-2,6-BP.
  4. Destino de Glucosa-6-P: Complejo luminal del RE hepático/renal.
- Cronología secuencial estricta: Pasos numerados del 1 al 14.
- Sin marcos ni cajas pesadas; diseño abierto y orgánico celular.
- Cero emojis; notación científica universal (+), (-), ->.
"""

import os
import sys

DIR_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIR_ROOT = os.path.dirname(DIR_BASE)

sys.path.append(os.path.join(DIR_BASE, "01_glucolisis"))
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_ROOT, "04_NITROGENO_Y_AMINOACIDOS", "01_transaminacion_y_desaminacion"))

from estructuras_glucosa import (
    GLUCOSA, GLUCOSA_6_FOSFATO, FRUCTOSA_6_FOSFATO, FRUCTOSA_1_6_BISFOSFATO,
    DIHIDROXIACETONA_FOSFATO, GLICERALDEHIDO_3_FOSFATO, BISFOSFOGLICERATO_1_3,
    FOSFOGLICERATO_3, FOSFOGLICERATO_2, FOSFOENOLPIRUVATO, PIRUVATO
)

from estructuras_gluconeogenesis import (
    OXALACETATO, MALATO, LACTATO, RE_GLUCOSA_6_FOSFATASA, GLICEROL
)

from estructuras_aminoacidos import (
    ALANINA as AMINO_ALANINA
)

ANCHO_CANVAS = 1680
ALTO_CANVAS = 3400

# Coordenadas maestras de alineación
X_EJE = 640       # Eje central de estructuras
X_FLECHA = 690    # Eje vertical de flechas

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gluconeogénesis - Mapa Bioquímico y Biología Estructural</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background-color: #0b0f19;
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
      box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.6);
      border-radius: 12px;
      max-width: 100%;
      height: auto;
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
    text {{ stroke: none !important; }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <style>
          text {{ stroke: none !important; }}
        </style>
        <!-- Marcadores estándar -->
        <marker id="arrowFlow" markerWidth="7" markerHeight="7" refX="5.5" refY="3.5" orient="auto">
          <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#ea580c" />
        </marker>
        <marker id="arrowPurple" markerWidth="7" markerHeight="7" refX="5.5" refY="3.5" orient="auto">
          <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#7c3aed" />
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
        <marker id="arrowAmber" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#b45309" />
        </marker>
        <marker id="arrowSlate" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#475569" />
        </marker>

        <!-- Gradientes celulares abiertos -->
        <linearGradient id="gradCitosol" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
          <stop offset="5%" stop-color="#faf5ff" stop-opacity="0.6" />
          <stop offset="50%" stop-color="#ffffff" stop-opacity="1" />
          <stop offset="85%" stop-color="#faf5ff" stop-opacity="0.5" />
          <stop offset="100%" stop-color="#f8fafc" stop-opacity="1" />
        </linearGradient>

        <linearGradient id="gradExtracelular" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#e2e8f0" stop-opacity="0.8" />
          <stop offset="100%" stop-color="#f1f5f9" stop-opacity="0.95" />
        </linearGradient>

        <radialGradient id="gradMitocondria" cx="50%" cy="100%" r="90%">
          <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.85" />
          <stop offset="60%" stop-color="#fffbeb" stop-opacity="0.75" />
          <stop offset="100%" stop-color="#fef9c3" stop-opacity="0.7" />
        </radialGradient>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def badge_paso(num, x, y, es_bypass=False, etiqueta=""):
    """Insignia circular limpia para señalar el orden cronológico estricto."""
    color_fondo = "#7c3aed" if es_bypass else "#ea580c"
    texto_etiq = f'<text x="22" y="4" fill="{color_fondo}" font-size="11" font-weight="900" font-family="\'Inter\', sans-serif">{etiqueta}</text>' if etiqueta else ""
    return f"""
    <g class="badge-paso" transform="translate({x}, {y})">
      <circle cx="0" cy="0" r="13" fill="{color_fondo}" stroke="#ffffff" stroke-width="2"/>
      <text x="0" y="4" fill="#ffffff" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{num}</text>
      {texto_etiq}
    </g>
    """

def llamada_bypass(x, y, rodeo_num, titulo, sortea_paso):
    """Llamada discreta y tipográfica sin recuadros pesados para marcar los 3 rodeos."""
    return f"""
    <g transform="translate({x}, {y})">
      <line x1="0" y1="-18" x2="0" y2="18" stroke="#7c3aed" stroke-width="3" stroke-linecap="round"/>
      <text x="12" y="-3" fill="#6d28d9" font-size="12" font-weight="900" font-family="'Inter', sans-serif">
        BYPASS {rodeo_num}: {titulo}
      </text>
      <text x="12" y="13" fill="#b91c1c" font-size="10.5" font-weight="700" font-family="'Inter', sans-serif">
        Sortea: Paso {sortea_paso} de Glucólisis (Irreversible)
      </text>
    </g>
    """

def llamada_reversible(x, y):
    """Llamada lateral que delimita la fase reversible de triosas y hexosas."""
    return f"""
    <g transform="translate({x}, {y})">
      <line x1="0" y1="-28" x2="0" y2="28" stroke="#16a34a" stroke-width="3" stroke-linecap="round"/>
      <text x="12" y="-12" fill="#15803d" font-size="12" font-weight="900" font-family="'Inter', sans-serif">
        FASE REVERSIBLE DE GLUCOLISIS
      </text>
      <text x="12" y="3" fill="#047857" font-size="10.5" font-weight="700" font-family="'Inter', sans-serif">
        Mismas enzimas que en Glucólisis (Pasos 9 a 4 en reversa)
      </text>
      <text x="12" y="18" fill="#64748b" font-size="9.5" font-family="'Inter', sans-serif">
        Impulsada por ley de acción de masas, 2 ATP y 2 NADH
      </text>
    </g>
    """

def generar_entorno_gluconeogenesis(ancho, alto, y_mito=2380):
    """Entorno biológico abierto sin cajas pesadas."""
    return f"""
    <!-- Fondo Citoplasmático Celular -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#gradCitosol)" />

    <!-- Filamentos citoesqueléticos tenues -->
    <g opacity="0.25" stroke="#94a3b8" fill="none">
      <path d="M 50 240 Q 350 180 700 260 T {ancho-50} 230" stroke-width="1.4" stroke-dasharray="8 6" />
      <path d="M 60 560 Q 400 620 780 570 T {ancho-60} 600" stroke-width="1.2" stroke-dasharray="6 6" />
      <path d="M 40 1020 Q 420 960 820 1030 T {ancho-40} 990" stroke-width="1.4" stroke-dasharray="8 5" />
      <path d="M 50 1480 Q 380 1540 740 1490 T {ancho-50} 1520" stroke-width="1.4" stroke-dasharray="7 7" />
      <path d="M 40 1950 Q 450 1900 880 1960 T {ancho-40} 1920" stroke-width="1.4" stroke-dasharray="8 6" />
    </g>

    <!-- Membrana plasmática superior (Sangre / Espacio Extracelular) -->
    <path d="M 0 0 L {ancho} 0 L {ancho} 65 Q {ancho*0.5} 90 0 65 Z" fill="url(#gradExtracelular)" stroke="#cbd5e1" stroke-width="1"/>
    <text x="45" y="26" fill="#64748b" font-size="11" font-weight="800" letter-spacing="1">ESPACIO EXTRACELULAR (SANGRE / LÍQUIDO INTERSTICIAL)</text>
    <text x="45" y="44" fill="#0284c7" font-size="10" font-weight="700">[Glucemia en Ayuno Fisiológico] ≈ 70-100 mg/dL (Mantenida por Hígado y Riñón)</text>

    <!-- Bicapa Fosfolipídica Ondulada Celular -->
    <path d="M 0 65 Q {ancho*0.5} 90 {ancho} 65" fill="none" stroke="#0284c7" stroke-width="7" stroke-linecap="round"/>
    <path d="M 0 72 Q {ancho*0.5} 97 {ancho} 72" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>

    <!-- Transportador GLUT-2 en la membrana (Exporta Glucosa libre) -->
    <g transform="translate(650, 48)">
      <path d="M 0 5 C 10 -12, 28 -12, 34 5 C 38 18, 34 36, 25 42 C 12 45, 2 35, 0 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <path d="M 80 5 C 70 -12, 52 -12, 46 5 C 42 18, 46 36, 55 42 C 68 45, 78 35, 80 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <ellipse cx="40" cy="20" rx="10" ry="18" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8"/>
      
      <!-- Molécula de glucosa saliendo hacia la sangre -->
      <polygon points="40,14 45,17 45,23 40,26 35,23 35,17" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
      <circle cx="35" cy="17" r="2" fill="#dc2626"/>

      <text x="40" y="49" fill="#0369a1" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-2</text>
    </g>

    <text x="750" y="55" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c">
      Exportación Sanguínea (Km ≈ 15-20 mM)
    </text>

    <!-- Flecha de salida hacia el torrente sanguíneo (PASO 14) -->
    <line x1="690" y1="128" x2="690" y2="88" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    {badge_paso(14, 690, 108, es_bypass=False, etiqueta="PASO 14: Liberación a Sangre")}

    <!-- Mitocondria Biológica (Compartimento Matriz) -->
    <g id="mitocondria-biologica-gng" transform="translate(0, {y_mito})">
      <!-- Membrana Mitocondrial Externa Lisa -->
      <path d="M 0 50 Q 400 15 800 35 T {ancho} 25 L {ancho} {alto - y_mito} L 0 {alto - y_mito} Z" 
            fill="url(#gradMitocondria)" stroke="#b45309" stroke-width="3"/>
      
      <!-- Espacio Intermembrana -->
      <path d="M 0 65 Q 400 30 800 50 T {ancho} 40" 
            fill="none" stroke="#78350f" stroke-width="1.8" stroke-dasharray="6 3"/>

      <!-- Crestas Mitocondriales de la MMI -->
      <path d="M 80 160 C 150 90, 190 190, 290 130 C 350 190, 300 240, 160 220 Z" 
            fill="#fef3c7" stroke="#b45309" stroke-width="2" opacity="0.8"/>

      <!-- Transportador MPC (Complejo Carrier de Piruvato) -->
      <g transform="translate(660, 22)">
        <rect x="0" y="0" width="60" height="26" rx="6" fill="#b45309" stroke="#78350f" stroke-width="1.8"/>
        <text x="30" y="18" fill="#ffffff" font-size="11" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">MPC</text>
      </g>
      <!-- Flecha del Piruvato cruzando el MPC hacia la Matriz Mitocondrial -->
      <line x1="690" y1="-10" x2="690" y2="55" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Rótulo de la Matriz Mitocondrial -->
      <g transform="translate(50, 75)">
        <text x="0" y="0" fill="#78350f" font-size="16" font-weight="900" letter-spacing="1">MATRIZ MITOCONDRIAL</text>
        <text x="0" y="16" fill="#92400e" font-size="11" font-weight="700">Fase inicial de la Gluconeogénesis y centro de Cataplerosis</text>
      </g>

      <!-- Transportador OGC (Lanzadera Malato / α-KG) en la membrana interna -->
      <g transform="translate(410, 22)">
        <rect x="0" y="0" width="70" height="26" rx="6" fill="#047857" stroke="#064e3b" stroke-width="1.8"/>
        <text x="35" y="17" fill="#ffffff" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">OGC</text>
      </g>
      <text x="445" y="12" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#047857" text-anchor="middle">
        Carrier Malato / α-KG (SLC25A11)
      </text>
    </g>
    """

def generar_lupa_malato(x=170, y=2980):
    """Lupa Molecular para la Lanzadera de Malato (OGC) sin marco pesado."""
    return f"""
    <!-- LUPA DE LA LANZADERA DE MALATO (OGC) -->
    <g stroke="#047857" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.6">
      <line x1="410" y1="2402" x2="{x + 65}" y2="{y - 45}" />
      <line x1="410" y1="2415" x2="{x + 40}" y2="{y + 60}" />
    </g>

    <g transform="translate({x}, {y})">
      <circle cx="0" cy="0" r="72" fill="#ffffff" stroke="#047857" stroke-width="3" />
      <circle cx="0" cy="0" r="68" fill="#f0fdf4" stroke="#dcfce7" stroke-width="1" />

      <!-- Bicapa lipídica de la MMI -->
      <g opacity="0.85">
        <g fill="#047857">
          <circle cx="-52" cy="-9" r="4.5"/><circle cx="-38" cy="-9" r="4.5"/><circle cx="-24" cy="-9" r="4.5"/>
          <circle cx="24" cy="-9" r="4.5"/><circle cx="38" cy="-9" r="4.5"/><circle cx="52" cy="-9" r="4.5"/>
        </g>
        <g stroke="#94a3b8" stroke-width="1.4" fill="none">
          <path d="M -52 -4 Q -54 2 -50 8"/><path d="M -38 -4 Q -40 2 -36 8"/><path d="M -24 -4 Q -26 2 -22 8"/>
          <path d="M 24 -4 Q 22 2 26 8"/><path d="M 38 -4 Q 36 2 40 8"/><path d="M 52 -4 Q 50 2 54 8"/>
        </g>
        <g fill="#047857">
          <circle cx="-52" cy="24" r="4.5"/><circle cx="-38" cy="24" r="4.5"/><circle cx="-24" cy="24" r="4.5"/>
          <circle cx="24" cy="24" r="4.5"/><circle cx="38" cy="24" r="4.5"/><circle cx="52" cy="24" r="4.5"/>
        </g>
      </g>

      <!-- Proteína OGC -->
      <path d="M -18 -24 C -9 -28, -5 -16, -5 0 C -5 16, -9 28, -18 24 C -26 20, -24 -20, -18 -24 Z" fill="#047857" stroke="#064e3b" stroke-width="1.8"/>
      <path d="M 18 -24 C 9 -28, 5 -16, 5 0 C 5 16, 9 28, 18 24 C 26 20, 24 -20, 18 -24 Z" fill="#047857" stroke="#064e3b" stroke-width="1.8"/>
      <ellipse cx="0" cy="0" rx="7" ry="20" fill="#a7f3d0" opacity="0.6"/>

      <!-- Flechas de antiporte -->
      <path d="M -7 20 L -7 -20" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-12" y="2" fill="#059669" font-size="8" font-weight="900" text-anchor="end">Malato²⁻ ↑</text>

      <path d="M 7 -20 L 7 20" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="12" y="2" fill="#475569" font-size="8" font-weight="900">↓ α-KG²⁻</text>

      <rect x="-62" y="48" width="124" height="16" rx="4" fill="#0f172a" opacity="0.9"/>
      <text x="0" y="59" fill="#ffffff" font-size="7.5" font-weight="800" text-anchor="middle" letter-spacing="0.5">
        ANTIPORTE OGC (SLC25A11)
      </text>
    </g>

    <g transform="translate({x + 85}, {y - 45})">
      <text x="0" y="0" fill="#047857" font-size="11" font-weight="900">MECANISMO DE SALIDA DE MALATO</text>
      <text x="0" y="16" fill="#0f172a" font-size="9.5" font-weight="700">1. La MMI carece de carrier para Oxalacetato (OAA).</text>
      <text x="0" y="30" fill="#475569" font-size="9.5">2. mMDH reduce OAA a L-Malato (gasta 1 NADH matricial).</text>
      <text x="0" y="44" fill="#047857" font-size="9.5" font-weight="800">3. OGC exporta Malato al citosol en antiporte con α-KG.</text>
      <text x="0" y="58" fill="#047857" font-size="9.5" font-weight="800">4. cMDH reoxida Malato a OAA y regenera NADH para GAPDH.</text>
    </g>
    """

def crear_metabolito(x, y, nombre, carbonos, formula="", svg_estructura="", texto_izquierda=False, dx_texto=135):
    """Metabolito abierto donde la estructura molecular es protagonista."""
    if texto_izquierda:
        pos_estructura = "translate(0, 0)"
        pos_texto = f"translate(-20, 26)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = f"translate({dx_texto}, 26)"
        alineacion = ''

    rotulo_formula = f'<text x="0" y="34" fill="#64748b" font-size="10.5" font-family="\'JetBrains Mono\', monospace" {alineacion}>{formula}</text>' if formula else ""

    return f"""
    <!-- Metabolito: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="{pos_estructura}">
        {svg_estructura}
      </g>
      <g transform="{pos_texto}">
        <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="900" font-family="'Inter', sans-serif" {alineacion}>{nombre}</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700" {alineacion}>{carbonos}</text>
        {rotulo_formula}
      </g>
    </g>
    """

def crear_reaccion_ascendente(x, y, enzima, ec="", entra_energia="", sale_energia="", 
                              activadores=None, inhibidores=None, reversible=False, 
                              salida_agua=False, altura=52, num_paso=None, es_bypass=False, etiqueta_paso=""):
    """Flecha ascendente con moduladores alostéricos exactos (+ / -) según los apuntes."""
    curvas_energia = ""
    if entra_energia:
        curvas_energia += f"""
        <path d="M -85 38 Q -30 38 -4 26" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
        <text x="-92" y="42" fill="#dc2626" font-size="11.5" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
    if sale_energia:
        curvas_energia += f"""
        <path d="M -4 20 Q -30 9 -85 9" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="-92" y="13" fill="#475569" font-size="11.5" font-weight="800" text-anchor="end">{sale_energia}</text>
        """
    if salida_agua:
        curvas_energia += """
        <path d="M -85 38 Q -30 38 -4 26" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-92" y="42" fill="#0284c7" font-size="11.5" font-weight="800" text-anchor="end">+ H₂O</text>
        """

    color_flecha = "#7c3aed" if es_bypass else "#ea580c"
    marker_url = "url(#arrowPurple)" if es_bypass else "url(#arrowFlow)"

    if reversible:
        flecha = f"""
        <line x1="-3.5" y1="{altura}" x2="-3.5" y2="0" stroke="{color_flecha}" stroke-width="2" marker-end="{marker_url}"/>
        <line x1="3.5" y1="0" x2="3.5" y2="{altura}" stroke="{color_flecha}" stroke-width="2" marker-end="{marker_url}"/>
        """
    else:
        flecha = f"""
        <line x1="0" y1="{altura}" x2="0" y2="0" stroke="{color_flecha}" stroke-width="2.6" marker-end="{marker_url}"/>
        """

    # Moduladores alostéricos directos
    moduladores_svg = ""
    y_mod = 28
    if activadores:
        texto_act = "(+) " + ", ".join(activadores)
        moduladores_svg += f'<text x="0" y="{y_mod}" fill="#16a34a" font-size="10.5" font-weight="800">{texto_act}</text>'
        y_mod += 14
    if inhibidores:
        texto_inh = "(-) " + ", ".join(inhibidores)
        moduladores_svg += f'<text x="0" y="{y_mod}" fill="#dc2626" font-size="10.5" font-weight="800">{texto_inh}</text>'

    badge_svg = badge_paso(num_paso, -25, altura // 2, es_bypass=es_bypass, etiqueta="") if num_paso else ""

    return f"""
    <!-- Reacción Ascendente: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha}
      {curvas_energia}
      {badge_svg}
      <g transform="translate(30, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {moduladores_svg}
      </g>
    </g>
    """

def generar_mapa_gluconeogenesis():
    """Generador principal enfocado en biología estructural y regulación de los apuntes."""
    svg_parts = []

    # 1. Capa de entorno celular biológico (ancho=1680, alto=3400, y_mito=2380)
    svg_parts.append(generar_entorno_gluconeogenesis(ANCHO_CANVAS, ALTO_CANVAS, y_mito=2380))

    # 2. Lupa Molecular de la Lanzadera de Malato (en la matriz izquierda)
    svg_parts.append(generar_lupa_malato(x=150, y=2980))

    # =========================================================================
    # COLUMNA IZQUIERDA: LLAMADAS ESTRUCTURALES Y PRECURSOR GLICEROL
    # =========================================================================

    # Bypass 2 (PFK-1)
    svg_parts.append(llamada_bypass(
        x=80, y=720, rodeo_num=2, 
        titulo="Fructosa-1,6-Bisfosfatasa-1 (FBPasa-1)", 
        sortea_paso="3 (Fosfofructocinasa-1 / PFK-1)"
    ))

    # Fase Reversible de Glucólisis
    svg_parts.append(llamada_reversible(x=80, y=1480))

    # Bypass 1B (Piruvato Cinasa en Citosol)
    svg_parts.append(llamada_bypass(
        x=80, y=2020, rodeo_num="1B", 
        titulo="PEPCK Citosólica (PCK1)", 
        sortea_paso="10 (Piruvato Cinasa / PK)"
    ))

    # Bypass 1A (Piruvato Cinasa en Mitocondria)
    svg_parts.append(llamada_bypass(
        x=80, y=2600, rodeo_num="1A", 
        titulo="Piruvato Carboxilasa (PC)", 
        sortea_paso="10 (Piruvato Cinasa / PK)"
    ))

    # PRECURSOR 3: GLICEROL (LIPÓLISIS ADIPOSA) - Directo sin cajas
    svg_parts.append(f"""
    <!-- PRECURSOR 3: GLICEROL -->
    <g transform="translate(100, 1000)">
      <text x="0" y="0" fill="#0284c7" font-size="12" font-weight="900">PRECURSOR 3: GLICEROL [3C]</text>
      <text x="0" y="14" fill="#64748b" font-size="9.5">Origen: Lipólisis de Triglicéridos (Adipocitos)</text>

      <g transform="translate(0, 24)">
        {GLICEROL}
      </g>

      <g transform="translate(110, 36)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">Glicerol</text>
        <text x="0" y="16" fill="#dc2626" font-size="10" font-weight="700">1. Glicerol Cinasa (- 1 ATP)</text>
        <text x="0" y="28" fill="#64748b" font-size="9.5">-> Glicerol-3-P</text>
        <text x="0" y="44" fill="#059669" font-size="10" font-weight="700">2. G3PDH (+ NAD⁺ -> + NADH)</text>
        <text x="0" y="58" fill="#047857" font-size="10.5" font-weight="800">-> DHAP (Entrada directa)</text>
      </g>

      <!-- Flecha directa hacia DHAP -->
      <path d="M 280 85 Q 360 85 415 65" fill="none" stroke="#0284c7" stroke-width="2.4" marker-end="url(#arrowBlue)"/>
      <text x="360" y="60" fill="#0284c7" font-size="10" font-weight="800">-> DHAP</text>
    </g>
    """)

    # =========================================================================
    # EJE CENTRAL: RUTA DE ESTRUCTURAS QUÍMICAS (PASOS 1 AL 14)
    # =========================================================================

    # 1. D-Glucosa Libre (Producto Final)
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=160,
        nombre="D-Glucosa Libre",
        carbonos="6 Carbonos (Hexosa Neutra)",
        formula="C₆H₁₂O₆ (Exportable vía GLUT-2)",
        svg_estructura=GLUCOSA,
        dx_texto=135
    ))

    # PASO 13: Glucosa-6-Fosfatasa en el RE (Bypass 3 integrado)
    svg_parts.append(f"""
    <!-- PASO 13: GLUCOSA-6-FOSFATASA EN EL RE (BYPASS 3) -->
    <g transform="translate(130, 270)">
      {RE_GLUCOSA_6_FOSFATASA}
      {badge_paso(13, 85, -14, es_bypass=True, etiqueta="PASO 13")}
      <g transform="translate(0, 95)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#6d28d9">
          BYPASS 3: Glucosa-6-Fosfatasa (EC 3.1.3.9)
        </text>
        <text x="0" y="15" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#b91c1c">
          Sortea: Paso 1 (Hexocinasa / HK) de Glucólisis
        </text>
        <text x="0" y="29" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#b45309">
          Exclusiva de Hígado y Corteza Renal (El Músculo carece de ella)
        </text>
        <text x="0" y="42" font-family="'Inter', sans-serif" font-size="9" fill="#475569">
          T1 importa G-6-P; G6Pase hidroliza Pi; T2/T3 devuelven D-Glucosa al citosol.
        </text>
      </g>
    </g>

    <!-- Flechas hacia el complejo del RE y retorno de glucosa -->
    <path d="M 640 400 Q 380 400 320 325" fill="none" stroke="#0284c7" stroke-width="2.4" marker-end="url(#arrowBlue)"/>
    <path d="M 320 275 Q 480 220 650 185" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
    """)

    # 2. Glucosa-6-Fosfato (G-6-P)
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=380,
        nombre="Glucosa-6-Fosfato (G-6-P)",
        carbonos="6 Carbonos (Hexosa Fosforilada)",
        formula="C₆H₁₁O₉P²⁻",
        svg_estructura=GLUCOSA_6_FOSFATO,
        dx_texto=135
    ))

    # PASO 12: Fosfoglucosa Isomerasa (PGI)
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=490,
        enzima="Fosfoglucosa Isomerasa (PGI)",
        ec="EC 5.3.1.9 (Paso 2 Glucólisis en reversa)",
        reversible=True,
        num_paso=12,
        es_bypass=False,
        etiqueta_paso="PASO 12"
    ))

    # 3. Fructosa-6-Fosfato (F-6-P)
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=590,
        nombre="Fructosa-6-Fosfato (F-6-P)",
        carbonos="6 Carbonos (Cetosa Fosforilada)",
        formula="C₆H₁₁O₉P²⁻",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        dx_texto=135
    ))

    # PASO 11: Fructosa-1,6-Bisfosfatasa-1 (FBPasa-1) - BYPASS 2
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=700,
        enzima="Fructosa-1,6-Bisfosfatasa-1 (FBPasa-1)",
        ec="EC 3.1.3.11 (Hidrólisis simple con H₂O; NO rinde ATP)",
        entra_energia="+ H₂O",
        sale_energia="+ Pi",
        activadores=["Citrato"],
        inhibidores=["AMP", "Fructosa-2,6-bisfosfato (F-2,6-BP)"],
        reversible=False,
        num_paso=11,
        es_bypass=True,
        etiqueta_paso="PASO 11"
    ))

    # 4. Fructosa-1,6-Bisfosfato (F-1,6-BP)
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=830,
        nombre="Fructosa-1,6-Bisfosfato",
        carbonos="6 Carbonos (Hexosa Bisfosforilada)",
        formula="C₆H₁₀O₁₂P₂⁴⁻",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO,
        dx_texto=135
    ))

    # PASO 10: Aldolasa (Condensación Aldólica)
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=940,
        enzima="Aldolasa A / B (Condensación Aldólica)",
        ec="EC 4.1.2.13 (3C + 3C -> 6C)",
        reversible=True,
        num_paso=10,
        es_bypass=False,
        etiqueta_paso="PASO 10"
    ))

    # 5. Triosas Fosfato: DHAP y Gliceraldehído-3-P (Equilibrio por TPI)
    svg_parts.append(f"""
    <!-- TRIOSAS FOSFATO: DHAP Y GAP -->
    <g transform="translate(430, 1060)">
      {DIHIDROXIACETONA_FOSFATO}
      <text x="40" y="132" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">DHAP</text>
      <text x="40" y="146" fill="#ea580c" font-size="9.5" font-weight="700" text-anchor="middle">3C (Cetotriosa)</text>
    </g>

    <g transform="translate(710, 1060)">
      {GLICERALDEHIDO_3_FOSFATO}
      <text x="40" y="146" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">Gliceraldehído-3-P</text>
      <text x="40" y="160" fill="#ea580c" font-size="9.5" font-weight="700" text-anchor="middle">3C (Aldotriosa)</text>
    </g>

    <!-- Conexión y equilibrio TPI entre triosas -->
    <g transform="translate(555, 1100)">
      <line x1="0" y1="-3" x2="80" y2="-3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="80" y1="3" x2="0" y2="3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <text x="40" y="-8" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">TPI (Isomerasa)</text>
      <text x="40" y="18" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1</text>
    </g>

    <!-- Flechas ascendentes convergiendo a Aldolasa -->
    <path d="M 480 1050 Q 560 990 670 995" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <path d="M 740 1050 Q 710 990 690 995" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    """)

    # PASO 9: GAPDH (Reducción Reversa)
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 50, y=1210,
        enzima="GAPDH (Reducción Reversa)",
        ec="EC 1.2.1.12 (Consume NADH citosólico de la lanzadera)",
        entra_energia="+ 2 NADH + 2 H⁺",
        sale_energia="+ 2 NAD⁺ + 2 Pi",
        reversible=True,
        num_paso=9,
        es_bypass=False,
        etiqueta_paso="PASO 9"
    ))

    # 6. 1,3-Bisfosfoglicerato
    svg_parts.append(crear_metabolito(
        x=X_EJE + 50, y=1280,
        nombre="1,3-Bisfosfoglicerato (1,3-BPG)",
        carbonos="3 Carbonos (Acil-fosfato de alta energía)",
        formula="C₃H₄O₁₀P₂⁴⁻",
        svg_estructura=BISFOSFOGLICERATO_1_3,
        dx_texto=135
    ))

    # PASO 8: Fosfoglicerato Cinasa (PGK)
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 50, y=1390,
        enzima="Fosfoglicerato Cinasa (PGK)",
        ec="EC 2.7.2.3 (Invierte 2 ATP por glucosa)",
        entra_energia="- 2 ATP",
        sale_energia="+ 2 ADP",
        reversible=True,
        num_paso=8,
        es_bypass=False,
        etiqueta_paso="PASO 8"
    ))

    # 7. 3-Fosfoglicerato (3-PG)
    svg_parts.append(crear_metabolito(
        x=X_EJE + 50, y=1490,
        nombre="3-Fosfoglicerato (3-PG)",
        carbonos="3 Carbonos",
        formula="C₃H₄O₇P³⁻",
        svg_estructura=FOSFOGLICERATO_3,
        dx_texto=135
    ))

    # PASO 7: Fosfoglicerato Mutasa (PGM)
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 50, y=1600,
        enzima="Fosfoglicerato Mutasa (PGM)",
        ec="EC 5.4.2.1 (Paso 8 Glucólisis en reversa)",
        reversible=True,
        num_paso=7,
        es_bypass=False,
        etiqueta_paso="PASO 7"
    ))

    # 8. 2-Fosfoglicerato (2-PG)
    svg_parts.append(crear_metabolito(
        x=X_EJE + 50, y=1700,
        nombre="2-Fosfoglicerato (2-PG)",
        carbonos="3 Carbonos",
        formula="C₃H₄O₇P³⁻",
        svg_estructura=FOSFOGLICERATO_2,
        dx_texto=135
    ))

    # PASO 6: Enolasa (Hidratación Reversa)
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 50, y=1810,
        enzima="Enolasa",
        ec="EC 4.2.1.11 (Hidratación reversible de PEP)",
        entra_energia="+ H₂O",
        reversible=True,
        num_paso=6,
        es_bypass=False,
        etiqueta_paso="PASO 6"
    ))

    # 9. Fosfoenolpiruvato (PEP)
    svg_parts.append(crear_metabolito(
        x=X_EJE + 50, y=1910,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 Carbonos (Enol-fosfato de alta energía)",
        formula="C₃H₂O₆P³⁻",
        svg_estructura=FOSFOENOLPIRUVATO,
        dx_texto=135
    ))

    # PASO 5: PEPCK Citosólica (PCK1) - BYPASS 1B
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 50, y=2020,
        enzima="PEPCK Citosólica (PCK1)",
        ec="EC 4.1.1.32 (Descarboxilación y fosforilación con GTP)",
        entra_energia="- 1 GTP",
        sale_energia="+ GDP + CO₂",
        inhibidores=["ADP (Baja carga energética desvía OAA a Krebs)"],
        reversible=False,
        num_paso=5,
        es_bypass=True,
        etiqueta_paso="PASO 5"
    ))

    # 10. Oxalacetato Citosólico
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=2130,
        nombre="Oxalacetato (OAA Citosólico)",
        carbonos="4 Carbonos (Dicarboxilato)",
        formula="C₄H₂O₅²⁻",
        svg_estructura=OXALACETATO,
        dx_texto=135
    ))

    # PASO 4: cMDH (Malato Deshidrogenasa Citosólica)
    svg_parts.append(f"""
    <!-- PASO 4: MDH CITOSÓLICA (cMDH) -->
    <g transform="translate(420, 2180)">
      <line x1="0" y1="0" x2="160" y2="0" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowPurple)"/>
      {badge_paso(4, -20, 0, es_bypass=False, etiqueta="")}

      <g transform="translate(80, 0)">
        <text x="0" y="-18" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#6d28d9" text-anchor="middle">cMDH (MDH Citosólica)</text>
        <text x="0" y="-6" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#0284c7" text-anchor="middle">Regenera NADH para GAPDH</text>
        <text x="0" y="16" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#059669" text-anchor="middle">+ NAD⁺ -> + NADH + H⁺</text>
      </g>
    </g>
    """)

    # 11. L-Malato Citosólico
    svg_parts.append(crear_metabolito(
        x=300, y=2130,
        nombre="L-Malato (Citosólico)",
        carbonos="4 Carbonos",
        formula="C₄H₄O₅²⁻",
        svg_estructura=MALATO,
        texto_izquierda=True
    ))

    # PASO 3: Salida por Carrier OGC
    svg_parts.append(f"""
    <!-- PASO 3: SALIDA POR CARRIER OGC -->
    <path d="M 365 2720 L 365 2400 Q 365 2375 435 2375 L 435 2235 Q 435 2200 385 2200" fill="none" stroke="#047857" stroke-width="3" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>
    {badge_paso(3, 445, 2350, es_bypass=False, etiqueta="")}
    <g transform="translate(470, 2345)">
      <text x="0" y="0" fill="#047857" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">Lanzadera Malato (OGC ↑)</text>
      <text x="0" y="14" fill="#64748b" font-size="9" font-family="'Inter', sans-serif">Exporta 4C y equivalente reductor (NADH) al citosol</text>
    </g>
    """)

    # =========================================================================
    # MATRIZ MITOCONDRIAL: PIRUVATO, PC, OAA, mMDH Y MALATO
    # =========================================================================

    # 12. Piruvato Mitocondrial
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=2480,
        nombre="Piruvato (Mitocondrial)",
        carbonos="3 Carbonos (α-Cetoácido)",
        formula="C₃H₃O₃⁻",
        svg_estructura=PIRUVATO,
        dx_texto=135
    ))

    # PASO 1: Piruvato Carboxilasa (PC) - BYPASS 1A
    svg_parts.append(f"""
    <!-- PASO 1: PIRUVATO CARBOXILASA (PC) -->
    <g transform="translate(690, 2595)">
      <line x1="0" y1="0" x2="0" y2="55" stroke="#7c3aed" stroke-width="3" marker-end="url(#arrowPurple)"/>
      <path d="M -85 10 Q -30 10 -4 22" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-92" y="14" fill="#dc2626" font-size="11" font-weight="800" text-anchor="end">- 1 ATP + HCO₃⁻</text>
      <path d="M -4 30 Q -30 42 -85 42" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-92" y="46" fill="#475569" font-size="11" font-weight="800" text-anchor="end">+ ADP + Pi</text>
      
      {badge_paso(1, -25, 27, es_bypass=True, etiqueta="PASO 1")}
      
      <g transform="translate(25, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900">Piruvato Carboxilasa (PC)</text>
        <text x="0" y="15" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">EC 6.4.1.1 (Biotina - Vit. B₇)</text>
        <text x="0" y="28" fill="#16a34a" font-size="10.5" font-weight="800">(+) Acetil-CoA (Activador obligatorio)</text>
        <text x="0" y="41" fill="#dc2626" font-size="10.5" font-weight="800">(-) ADP (Baja carga energética frena PC)</text>
      </g>
    </g>
    """)

    # 13. Oxalacetato Mitocondrial
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=2720,
        nombre="Oxalacetato (OAA Mitocondrial)",
        carbonos="4 Carbonos",
        formula="C₄H₂O₅²⁻ (MMI carece de carrier directo)",
        svg_estructura=OXALACETATO,
        dx_texto=135
    ))

    # PASO 2: mMDH (Malato Deshidrogenasa Mitocondrial)
    svg_parts.append(f"""
    <!-- PASO 2: mMDH -->
    <g transform="translate(420, 2770)">
      <line x1="160" y1="0" x2="0" y2="0" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowPurple)"/>
      {badge_paso(2, 180, 0, es_bypass=False, etiqueta="")}

      <g transform="translate(80, 0)">
        <text x="0" y="-18" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#6d28d9" text-anchor="middle">mMDH (MDH Mitocondrial)</text>
        <text x="0" y="-6" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">Reduce OAA para salir por OGC</text>
        <text x="0" y="16" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#059669" text-anchor="middle">+ NADH + H⁺ -> + NAD⁺</text>
      </g>
    </g>
    """)

    # 14. L-Malato Mitocondrial
    svg_parts.append(crear_metabolito(
        x=300, y=2720,
        nombre="L-Malato (Mitocondrial)",
        carbonos="4 Carbonos",
        formula="C₄H₄O₅²⁻ (Sustrato de salida OGC)",
        svg_estructura=MALATO,
        texto_izquierda=True
    ))

    # =========================================================================
    # COLUMNA DERECHA: PUNTOS DE REGULACIÓN DE LOS APUNTES (TEMA 4)
    # =========================================================================

    # -------------------------------------------------------------------------
    # PUNTO 3 DE REGULACIÓN: CONMUTADOR RECÍPROCO F-6-P <-> F-1,6-BP (Y=460)
    # -------------------------------------------------------------------------
    svg_parts.append("""
    <!-- PUNTO 3 DE REGULACIÓN: ENZIMA BIFUNCIONAL Y F-2,6-BP -->
    <g transform="translate(1040, 480)">
      <text x="0" y="0" fill="#6d28d9" font-size="13" font-weight="900">
        PUNTO 3: EL CONMUTADOR RECÍPROCO MAESTRO (F-6-P / F-1,6-BP)
      </text>
      <text x="0" y="16" fill="#475569" font-size="10">
        Mismos moduladores alostéricos para ambas vías, pero en sentido opuesto:
      </text>

      <!-- Comparativa alostérica directa -->
      <g transform="translate(0, 32)">
        <line x1="0" y1="0" x2="560" y2="0" stroke="#e2e8f0" stroke-width="1.2"/>
        
        <!-- FBPasa-1 -->
        <g transform="translate(0, 16)">
          <text x="0" y="0" fill="#7c3aed" font-size="12" font-weight="900">FBPasa-1 (Gluconeogénesis):</text>
          <text x="0" y="16" fill="#16a34a" font-size="11" font-weight="800">(+) Citrato (Abundancia energética)</text>
          <text x="0" y="30" fill="#dc2626" font-size="11" font-weight="800">(-) AMP (Baja carga energética)</text>
          <text x="0" y="44" fill="#dc2626" font-size="11" font-weight="800">(-) Fructosa-2,6-bisfosfato (Inhibidor más potente)</text>
        </g>

        <!-- PFK-1 -->
        <g transform="translate(290, 16)">
          <text x="0" y="0" fill="#ea580c" font-size="12" font-weight="900">PFK-1 (Glucólisis):</text>
          <text x="0" y="16" fill="#16a34a" font-size="11" font-weight="800">(+) AMP, (+) Fructosa-2,6-bisfosfato</text>
          <text x="0" y="30" fill="#dc2626" font-size="11" font-weight="800">(-) ATP (Carga energética alta)</text>
          <text x="0" y="44" fill="#dc2626" font-size="11" font-weight="800">(-) Citrato, (-) H⁺ (Acidosis)</text>
        </g>
      </g>

      <!-- Esquema molecular de la Enzima Bifuncional PFK-2 / FBPasa-2 -->
      <g transform="translate(0, 125)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900">
          La Enzima Bifuncional Tándem (Control Hormonal Hepático):
        </text>
        
        <!-- Cápsula de la proteína tándem con sus dos dominios -->
        <g transform="translate(0, 14)">
          <rect x="0" y="0" width="130" height="28" rx="5" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.4"/>
          <text x="65" y="18" fill="#0369a1" font-size="10" font-weight="800" text-anchor="middle">Dominio PFK-2</text>
          
          <rect x="135" y="0" width="145" height="28" rx="5" fill="#fdf4ff" stroke="#7c3aed" stroke-width="1.4"/>
          <text x="207" y="18" fill="#6d28d9" font-size="10" font-weight="800" text-anchor="middle">Dominio FBPasa-2</text>
          
          <text x="300" y="18" fill="#475569" font-size="10.5">Cadena polipeptídica única</text>
        </g>

        <!-- Reacción que cataliza F-6-P <-> F-2,6-BP -->
        <g transform="translate(0, 60)">
          <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Fructosa-6-P</text>
          <path d="M 90 -4 L 210 -4" stroke="#0284c7" stroke-width="1.6" marker-end="url(#arrowBlue)"/>
          <text x="150" y="-8" fill="#0284c7" font-size="8.5" text-anchor="middle">PFK-2 (-1 ATP)</text>
          <path d="M 210 6 L 90 6" stroke="#7c3aed" stroke-width="1.6" marker-end="url(#arrowPurple)"/>
          <text x="150" y="16" fill="#7c3aed" font-size="8.5" text-anchor="middle">FBPasa-2 (+ H₂O)</text>
          <text x="220" y="0" fill="#6d28d9" font-size="11" font-weight="900">Fructosa-2,6-bisfosfato (F-2,6-BP)</text>
        </g>

        <!-- Estado de Ayuno vs Saciedad -->
        <g transform="translate(0, 105)">
          <text x="0" y="0" fill="#b91c1c" font-size="11" font-weight="900">
            [A] En Ayuno (Glucagón ↑ -> cAMP -> PKA):
          </text>
          <text x="16" y="15" fill="#475569" font-size="10">
            • PKA FOSFORILA la enzima -> Inactiva PFK-2 y ACTIVA FBPasa-2.
          </text>
          <text x="16" y="29" fill="#047857" font-size="10" font-weight="800">
            • Cae [F-2,6-BP] -> Se DESINHIBE FBPasa-1: GLUCONEOGÉNESIS ACTIVADA.
          </text>

          <text x="0" y="52" fill="#0369a1" font-size="11" font-weight="900">
            [B] En Saciedad / Postprandial (Insulina ↑ -> PP1):
          </text>
          <text x="16" y="67" fill="#475569" font-size="10">
            • PP1 DESFOSFORILA la enzima -> ACTIVA PFK-2 e Inactiva FBPasa-2.
          </text>
          <text x="16" y="81" fill="#ea580c" font-size="10" font-weight="800">
            • Sube [F-2,6-BP] -> Activa fuertemente PFK-1: GLUCÓLISIS ENCENDIDA.
          </text>
        </g>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # PUNTO 2 DE REGULACIÓN: OXALACETATO Y PEPCK (Y=1450)
    # -------------------------------------------------------------------------
    svg_parts.append("""
    <!-- PUNTO 2 DE REGULACIÓN: DESTINO DEL OXALACETATO Y PEPCK -->
    <g transform="translate(1040, 1450)">
      <text x="0" y="0" fill="#047857" font-size="13" font-weight="900">
        PUNTO 2: UTILIZACIÓN DEL OXALACETATO Y CONTROL POR ENERGÍA
      </text>
      <text x="0" y="16" fill="#475569" font-size="10">
        El Oxalacetato celular sigue 2 destinos excluyentes según la carga energética:
      </text>

      <g transform="translate(0, 32)">
        <line x1="0" y1="0" x2="560" y2="0" stroke="#e2e8f0" stroke-width="1.2"/>
        
        <g transform="translate(0, 16)">
          <text x="0" y="0" fill="#b45309" font-size="11.5" font-weight="800">
            1. Ciclo de Krebs (Generación de ATP):
          </text>
          <text x="16" y="14" fill="#475569" font-size="10">
            Si la carga energética es baja (alto ADP / bajo ATP), OAA se condensa con Acetil-CoA
          </text>
          <text x="16" y="27" fill="#475569" font-size="10">
            hacia Citrato para quemarse en Krebs y reponer ATP.
          </text>
        </g>

        <g transform="translate(0, 68)">
          <text x="0" y="0" fill="#7c3aed" font-size="11.5" font-weight="800">
            2. Vía Gluconeogénica (PEPCK):
          </text>
          <text x="16" y="14" fill="#475569" font-size="10">
            Si la carga energética es suficiente, OAA se descarboxila a PEP para sintetizar glucosa.
          </text>
          <text x="16" y="28" fill="#dc2626" font-size="10.5" font-weight="800">
            • (-) ADP inhibe fuertemente a PEPCK: No se gasta GTP en biosíntesis si falta energía.
          </text>
          <text x="16" y="42" fill="#16a34a" font-size="10.5" font-weight="800">
            • (+) Inducción génica: Glucagón y Cortisol (CREB / FOXO1) inducen síntesis de PEPCK.
          </text>
        </g>
      </g>

      <!-- Balance Estequiométrico Esencial -->
      <g transform="translate(0, 165)">
        <line x1="0" y1="0" x2="560" y2="0" stroke="#e2e8f0" stroke-width="1.2"/>
        <text x="0" y="18" fill="#0f172a" font-size="12" font-weight="900">
          Balance Bioenergético Global: Gasto de 6 Enlaces ~P
        </text>
        <text x="0" y="34" fill="#dc2626" font-size="10.5" font-weight="700">
          • 2 Piruvato Carboxilasa (Paso 1) -> 2 ATP  |  • 2 PEPCK (Paso 5) -> 2 GTP
        </text>
        <text x="0" y="48" fill="#dc2626" font-size="10.5" font-weight="700">
          • 2 PGK (Paso 8) -> 2 ATP  |  • 2 GAPDH (Paso 9) -> 2 NADH
        </text>
        <text x="0" y="64" fill="#047857" font-size="10" font-family="'JetBrains Mono', monospace">
          2 Piruvato + 4 ATP + 2 GTP + 2 NADH + 6 H₂O -> Glucosa + 4 ADP + 2 GDP + 6 Pi + 2 NAD⁺
        </text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # PRECURSORES BASALES EN CITOSOL: L-LACTATO Y L-ALANINA (Y=2180)
    # -------------------------------------------------------------------------

    # PRECURSOR 1: L-Lactato (Citosol)
    svg_parts.append(f"""
    <!-- PRECURSOR 1: L-LACTATO -->
    <g transform="translate(980, 2180)">
      <text x="0" y="0" fill="#7c3aed" font-size="12" font-weight="900">PRECURSOR 1: L-LACTATO [3C]</text>
      <text x="0" y="14" fill="#64748b" font-size="9.5">Ciclo de Cori (Eritrocitos y Músculo Anaeróbico)</text>

      <g transform="translate(0, 24)">
        {LACTATO}
      </g>

      <g transform="translate(100, 48)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">L-Lactato</text>
        <text x="0" y="16" fill="#7c3aed" font-size="10.5" font-weight="700">LDH (Lactato DH)</text>
        <text x="0" y="29" fill="#059669" font-size="10" font-weight="800">+ NAD⁺ -> + NADH + H⁺</text>
      </g>

      <!-- Flecha hacia Piruvato citosólico / MPC -->
      <path d="M 0 65 Q -150 110 -265 170" fill="none" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arrowPurple)"/>
      <text x="-130" y="105" fill="#7c3aed" font-size="9.5" font-weight="800" text-anchor="middle">-> Piruvato (MPC)</text>
    </g>
    """)

    # PRECURSOR 2: L-Alanina (Citosol)
    svg_parts.append(f"""
    <!-- PRECURSOR 2: L-ALANINA -->
    <g transform="translate(1310, 2180)">
      <text x="0" y="0" fill="#ea580c" font-size="12" font-weight="900">PRECURSOR 2: L-ALANINA [3C]</text>
      <text x="0" y="14" fill="#64748b" font-size="9.5">Ciclo de Cahill (Proteólisis muscular en ayuno)</text>

      <g transform="translate(0, 24)">
        {AMINO_ALANINA}
      </g>

      <g transform="translate(100, 48)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">L-Alanina</text>
        <text x="0" y="16" fill="#ea580c" font-size="10.5" font-weight="700">ALT (Alanina Aminotransferasa)</text>
        <text x="0" y="29" fill="#64748b" font-size="10">+ α-KG -> + Glutamato</text>
      </g>

      <!-- Flecha hacia Piruvato citosólico / MPC -->
      <path d="M 0 65 Q -300 130 -595 170" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <text x="-280" y="135" fill="#ea580c" font-size="9.5" font-weight="800" text-anchor="middle">-> Piruvato (MPC)</text>
    </g>
    """)

    # -------------------------------------------------------------------------
    # PUNTO 1 DE REGULACIÓN: PIRUVATO Y ACETIL-CoA EN LA MATRIZ (Y=2600)
    # -------------------------------------------------------------------------
    svg_parts.append("""
    <!-- PUNTO 1 DE REGULACIÓN: ACETIL-CoA COMO CONMUTADOR MAESTRO -->
    <g transform="translate(1040, 2600)">
      <text x="0" y="0" fill="#b91c1c" font-size="13" font-weight="900">
        PUNTO 1: UTILIZACIÓN DEL PIRUVATO Y EL CONMUTADOR DE ACETIL-CoA
      </text>
      <text x="0" y="16" fill="#475569" font-size="10">
        En ayuno, la β-oxidación de ácidos grasos satura la matriz de Acetil-CoA:
      </text>

      <g transform="translate(0, 32)">
        <line x1="0" y1="0" x2="560" y2="0" stroke="#e2e8f0" stroke-width="1.2"/>
        
        <g transform="translate(0, 16)">
          <text x="0" y="0" fill="#16a34a" font-size="11.5" font-weight="900">
            (+) Activa obligatoriamente a Piruvato Carboxilasa (PC):
          </text>
          <text x="16" y="14" fill="#475569" font-size="10">
            Fuerza la carboxilación de Piruvato a Oxalacetato para la biosíntesis.
          </text>
        </g>

        <g transform="translate(0, 48)">
          <text x="0" y="0" fill="#dc2626" font-size="11.5" font-weight="900">
            (-) Inhibe alostéricamente a Piruvato Deshidrogenasa (PDH):
          </text>
          <text x="16" y="14" fill="#475569" font-size="10">
            Bloquea la combustión oxidativa del piruvato. Se conserva el 100% para generar glucosa.
          </text>
        </g>

        <g transform="translate(0, 80)">
          <text x="0" y="0" fill="#dc2626" font-size="11.5" font-weight="900">
            (-) ADP frena a la Piruvato Carboxilasa:
          </text>
          <text x="16" y="14" fill="#475569" font-size="10">
            Si hay baja carga energética en la célula, se frenan las reacciones de biosíntesis.
          </text>
        </g>
      </g>
    </g>

    <!-- PRECURSOR 4: CICLO DE KREBS Y CATAPLEROSIS -->
    <g transform="translate(1040, 2780)">
      <text x="0" y="0" fill="#b45309" font-size="13" font-weight="900">
        PRECURSOR 4: CATAPLEROSIS DEL CICLO DE KREBS (AMINOÁCIDOS)
      </text>
      <text x="0" y="16" fill="#92400e" font-size="10" font-weight="700">
        Los intermediarios del ciclo abandonan la matriz para alimentar la Gluconeogénesis:
      </text>

      <g transform="translate(0, 28)">
        <text x="0" y="0" fill="#0f172a" font-size="10.5" font-weight="800">• α-Cetoglutarato [5C]:</text>
        <text x="140" y="0" fill="#047857" font-size="10">Glutamato, Glutamina, Prolina, Histidina, Arginina</text>

        <text x="0" y="16" fill="#0f172a" font-size="10.5" font-weight="800">• Succinil-CoA [4C]:</text>
        <text x="140" y="16" fill="#047857" font-size="10">Metionina, Valina, Isoleucina, Treonina, Propionil-CoA</text>

        <text x="0" y="32" fill="#0f172a" font-size="10.5" font-weight="800">• Fumarato [4C]:</text>
        <text x="140" y="32" fill="#047857" font-size="10">Fenilalanina, Tirosina, Aspartato</text>

        <text x="0" y="48" fill="#0f172a" font-size="10.5" font-weight="800">• Oxalacetato [4C]:</text>
        <text x="140" y="48" fill="#047857" font-size="10">Aspartato, Asparagina (Transaminación directa)</text>

        <text x="0" y="70" fill="#b91c1c" font-size="9.5" font-weight="800">
          Nota de Examen: Acetil-CoA (ácidos grasos pares) NO aporta carbonos netos a la glucosa
        </text>
        <text x="0" y="82" fill="#64748b" font-size="9">
          (Entran 2C como Acetil-CoA y salen 2C como CO₂ en Krebs; no hay ganancia neta).
        </text>
      </g>
    </g>

    <!-- Flecha de Cataplerosis conectando Krebs directamente a L-Malato Mitocondrial -->
    <path d="M 1040 2920 L 400 2920 Q 360 2920 360 2800" fill="none" stroke="#b45309" stroke-width="2.6" stroke-dasharray="8 4" marker-end="url(#arrowAmber)"/>
    <text x="680" y="2912" fill="#78350f" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">
      Cataplerosis Krebs -> Pool de L-Malato Mitocondrial ↑
    </text>
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
