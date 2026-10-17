# =============================================================================
# MÓDULO DE REVISIÓN: Entorno y Fase Oxidativa (Generación de NADPH)
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/via_04_pentosas_fosfato/generar_pentosas.py (líneas 1 a 430 de 802)
# Descripción      : Reacciones de G6PDH, lactonasa y 6-fosfogluconato deshidrogenasa.
# =============================================================================

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
      width: 1700px;
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
    <svg width="1700" height="2150" viewBox="0 0 1700 2150" xmlns="http://www.w3.org/2000/svg">
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

        <!-- MARCADORES_PANELES -->
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
# 5. PANELES DE CONTEXTO (columna derecha): ¿cuándo y para qué se usa la vía?
# -----------------------------------------------------------------------------
X0 = 1030          # inicio de la columna derecha
WP = 640           # ancho de los paneles
FF = "font-family=\"'Inter', sans-serif\""

MARCADORES_PANELES = """
        <!-- Marcadores de los paneles de contexto (tamaño fijo, independiente del grosor) -->
        <marker id="mOr" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#ea580c"/></marker>
        <marker id="mGr" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#059669"/></marker>
        <marker id="mGy" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#cbd5e1"/></marker>
        <marker id="mPu" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#7c3aed"/></marker>
        <marker id="mRd" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#dc2626"/></marker>
        <marker id="mSl" markerUnits="userSpaceOnUse" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#475569"/></marker>
"""

def _t(x, y, s, size=10, w=700, fill="#475569", anchor="start", extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'

def _pill(cx, cy, s, color, bg, w=None, h=18, fs=10, op=1):
    w = w or (len(s) * (fs * 0.62) + 18)
    return (f'<g opacity="{op}"><rect x="{cx-w/2:.1f}" y="{cy-h/2}" width="{w:.1f}" height="{h}" rx="{h/2}" fill="{bg}" stroke="{color}" stroke-width="1.5"/>'
            f'<text x="{cx}" y="{cy+fs*0.36:.1f}" font-size="{fs}" font-weight="900" fill="{color}" text-anchor="middle">{s}</text></g>')

def _line(x1, y1, x2, y2, color="#ea580c", m="mOr", w=2.4, dash=False):
    d = ' stroke-dasharray="5 4"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}"{d} marker-end="url(#{m})"/>'

def _path(d, color="#ea580c", m="mOr", w=2.4, dash=False):
    ds = ' stroke-dasharray="5 4"' if dash else ''
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}"{ds} marker-end="url(#{m})"/>'

def _card(x, y, w, h, border, fill="#ffffff", rx=14):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{border}" stroke-width="1.8"/>'

def _seccion(y, titulo, sub=""):
    s = f'<rect x="{X0}" y="{y}" width="{WP}" height="26" rx="13" fill="#0f172a"/>'
    s += _t(X0 + 18, y + 17.5, titulo, 11.5, 900, "#ffffff", extra='letter-spacing="1.5"')
    if sub:
        s += _t(X0 + WP - 16, y + 17, sub, 10, 700, "#94a3b8", "end")
    return s

# ---- A. Los 4 modos --------------------------------------------------------
def _modo(y, n, titulo, col, bg, lineas, chip, flags):
    g = [f'<g transform="translate({X0},{y})">', _card(0, 0, WP, 120, col, "#ffffff")]
    g.append(_pill(14 + (len(titulo) * 6.4 + 24) / 2, 18, titulo, col, bg, len(titulo) * 6.4 + 24, 20, 10.5))
    for i, ln in enumerate(lineas):
        g.append(_t(14, 48 + 13 * i, ln, 10, 600, "#475569"))
    g.append(_pill(14 + (len(chip) * 6.2 + 20) / 2, 100, chip, "#047857", "#d1fae5", len(chip) * 6.2 + 20, 18, 10))
    # --- mini diagrama ---
    on, off = ("#ea580c", "mOr"), ("#cbd5e1", "mGy")
    def A(flag): return on if flag else off
    # nodos
    pos = dict(G6P=(236, 38, 56), RU=(356, 38, 62), R5=(466, 38, 54), NU=(576, 38, 96), FG=(356, 94, 100))
    act_nodes = flags["nodes"]
    for k, (cx, cy, w) in pos.items():
        nm = dict(G6P="G6P", RU="Ru5P", R5="R5P", NU="NUCLEÓTIDOS", FG="F6P + GAP")[k]
        if k in ("R5", "NU"):
            col2, bg2 = "#7c3aed", "#f5f3ff"
        elif k == "FG":
            col2, bg2 = "#b45309", "#fef3c7"
        else:
            col2, bg2 = "#c2410c", "#ffedd5"
        g.append(_pill(cx, cy, nm, col2, bg2, w, 20, 10, 1 if k in act_nodes else 0.35))
    # a1: oxidativa G6P -> Ru5P
    c, m = A(flags["ox"])
    g.append(_line(266, 38, 322, 38, c, m, 2.6 if flags["ox"] else 1.8, not flags["ox"]))
    if flags["ox"]:
        g.append(_pill(294, 22, "2 NADPH", "#047857", "#d1fae5", 56, 14, 8.5))
    else:
        g.append(_t(294, 26, "✕ sin fase ox.", 8.5, 800, "#94a3b8", "middle"))
    # a2: Ru5P -> R5P ; a3: R5P -> nucleótidos
    c, m = A(flags["iso"]); g.append(_line(389, 38, 436, 38, c, m, 2.6 if flags["iso"] else 1.8, not flags["iso"]))
    c, m = A(flags["iso"]); g.append(_line(494, 38, 526, 38, c, m, 2.6 if flags["iso"] else 1.8, not flags["iso"]))
    # a4: Ru5P <-> F6P+GAP (no oxidativa)
    d4 = flags["nox"]
    if d4 == "down":
        g.append(_line(356, 50, 356, 82, *on, 2.6))
    elif d4 == "up":
        g.append(_line(356, 82, 356, 50, *on, 2.6))
    else:
        g.append(_line(356, 50, 356, 82, *off, 1.8, True))
    # a5: lazo con G6P
    if flags["loop"] == "back":
        g.append(_path("M 306 94 L 236 94 L 236 52", *on, 2.4)); g.append(_t(236, 112, "recicla a G6P", 8.5, 800, "#c2410c", "middle"))
    elif flags["loop"] == "in":
        g.append(_path("M 236 52 L 236 94 L 304 94", *on, 2.4)); g.append(_t(236, 112, "viene de la glucólisis", 8.5, 800, "#c2410c", "middle"))
    # a6: a glucólisis
    if flags["gly"]:
        g.append(_line(408, 94, 470, 94, *on, 2.6)); g.append(_pill(548, 94, "→ piruvato + ATP", "#b45309", "#fef3c7", 128, 18, 9.5))
    g.append('</g>')
    return "\n".join(g)

def panel_modos(y):
    s = [_seccion(y, "¿CUÁNDO SE USA LA VÍA?", "4 modos según lo que necesite la célula")]
    modos = [
        ("MODO 1 · NADPH ≫ R5P", "#059669", "#d1fae5",
         ["Hígado, tejido adiposo, mama lactante,", "corteza suprarrenal: síntesis de", "ácidos grasos y esteroides"],
         "1 G6P → 12 NADPH",
         dict(nodes={"G6P", "RU", "FG"}, ox=True, iso=False, nox="down", loop="back", gly=False)),
        ("MODO 2 · R5P ≫ NADPH", "#7c3aed", "#f5f3ff",
         ["Células en división (médula ósea,", "mucosa, tumores): síntesis de", "nucleótidos y ácidos nucleicos"],
         "R5P sin gastar NADPH",
         dict(nodes={"G6P", "RU", "R5", "NU", "FG"}, ox=False, iso=True, nox="up", loop="in", gly=False)),
        ("MODO 3 · R5P = NADPH", "#0284c7", "#e0f2fe",
         ["Demanda equilibrada de ribosa", "y de NADPH: solo la fase oxidativa", "+ isomerasa"],
         "1 R5P + 2 NADPH + CO₂",
         dict(nodes={"G6P", "RU", "R5", "NU"}, ox=True, iso=True, nox=None, loop=None, gly=False)),
        ("MODO 4 · NADPH + ATP", "#b45309", "#fef3c7",
         ["Hace falta NADPH y ATP, no ribosa:", "la pentosa vuelve a la glucólisis", "y se oxida hasta piruvato"],
         "NADPH + ATP",
         dict(nodes={"G6P", "RU", "FG"}, ox=True, iso=False, nox="down", loop=None, gly=True)),
    ]
    cy = y + 38
    for n, (t, c, bg, ls, chip, fl) in enumerate(modos):
        s.append(_modo(cy, n + 1, t, c, bg, ls, chip, fl)); cy += 132
    return "\n".join(s), cy

# ---- B. Interruptor ---------------------------------------------------------
def panel_interruptor(y):
    h = 210
    s = [_seccion(y, "INTERRUPTOR DE LA VÍA: G6PDH", "paso limitante")]
    s.append(f'<g transform="translate({X0},{y+38})">')
    s.append(_card(0, 0, WP, h - 38, "#cbd5e1"))
    s.append('<defs><linearGradient id="gradInterruptor" x1="0" x2="1"><stop offset="0" stop-color="#34d399"/><stop offset="0.5" stop-color="#fbbf24"/><stop offset="1" stop-color="#f87171"/></linearGradient></defs>')
    # gauge
    s.append(_t(24, 28, "NADP⁺ ALTO", 10.5, 900, "#047857")); s.append(_t(320, 28, "NADPH ALTO", 10.5, 900, "#b91c1c", "end"))
    s.append('<rect x="24" y="38" width="296" height="16" rx="8" fill="url(#gradInterruptor)"/>')
    s.append('<circle cx="64" cy="46" r="11" fill="#ffffff" stroke="#047857" stroke-width="3"/>')
    s.append(_pill(94, 84, "G6PDH ON", "#047857", "#d1fae5", 92, 20, 10.5)); s.append(_t(94, 106, "se consume NADPH", 9.5, 700, "#475569", "middle"))
    s.append(_pill(250, 84, "G6PDH OFF", "#b91c1c", "#fee2e2", 96, 20, 10.5)); s.append(_t(250, 106, "sobra NADPH", 9.5, 700, "#475569", "middle"))
    s.append(_pill(172, 138, "Insulina ↑ → más G6PDH (dieta rica en carbohidratos)", "#7c3aed", "#f5f3ff", 300, 20, 9.5))
    # bucle
    s.append(_pill(400, 46, "NADP⁺", "#475569", "#f1f5f9", 66, 22, 11))
    s.append(_pill(580, 46, "NADPH", "#047857", "#d1fae5", 70, 22, 11))
    s.append(_line(436, 46, 542, 46, "#ea580c", "mOr", 2.6)); s.append(_t(489, 36, "vía de las pentosas", 9.5, 800, "#c2410c", "middle"))
    s.append(_pill(490, 128, "USO REDUCTOR", "#b45309", "#fef3c7", 120, 22, 10.5))
    s.append(_path("M 574 58 C 574 100 548 120 552 120", "#059669", "mGr", 2.2))
    s.append(_path("M 430 120 C 400 112 396 90 398 60", "#475569", "mSl", 2.2))
    s.append(_t(612, 112, "⊣ NADPH", 10, 900, "#b91c1c", "end")); s.append(_t(612, 124, "frena G6PDH", 9, 700, "#b91c1c", "end"))
    s.append(_t(384, 112, "⊕ NADP⁺", 10, 900, "#047857", "end")); s.append(_t(384, 124, "activa G6PDH", 9, 700, "#047857", "end"))
    s.append('</g>')
    return "\n".join(s), y + h + 14

# ---- C. Hub de usos del NADPH ----------------------------------------------
def _glifo(kind, cx, cy, col):
    if kind == "gota":
        return f'<path d="M {cx} {cy-11} C {cx+11} {cy+1} {cx+10} {cy+11} {cx} {cy+11} C {cx-10} {cy+11} {cx-11} {cy+1} {cx} {cy-11} Z" fill="#fef3c7" stroke="{col}" stroke-width="2"/>'
    if kind == "escudo":
        return f'<path d="M {cx} {cy-12} L {cx+11} {cy-7} L {cx+9} {cy+5} Q {cx} {cy+12} {cx} {cy+12} Q {cx} {cy+12} {cx-9} {cy+5} L {cx-11} {cy-7} Z" fill="#d1fae5" stroke="{col}" stroke-width="2"/>'
    if kind == "estrella":
        pts = " ".join(f"{cx+(11 if i%2==0 else 5)*__import__('math').cos(__import__('math').pi*i/5-1.5708):.1f},{cy+(11 if i%2==0 else 5)*__import__('math').sin(__import__('math').pi*i/5-1.5708):.1f}" for i in range(10))
        return f'<polygon points="{pts}" fill="#fee2e2" stroke="{col}" stroke-width="2"/>'
    if kind == "hex":
        return f'<polygon points="{cx},{cy-12} {cx+10},{cy-6} {cx+10},{cy+6} {cx},{cy+12} {cx-10},{cy+6} {cx-10},{cy-6}" fill="#e0f2fe" stroke="{col}" stroke-width="2"/>'
    if kind == "adn":
        return (f'<path d="M {cx-8} {cy-11} C {cx+10} {cy-4} {cx-10} {cy+4} {cx+8} {cy+11}" fill="none" stroke="{col}" stroke-width="2.2"/>'
                f'<path d="M {cx+8} {cy-11} C {cx-10} {cy-4} {cx+10} {cy+4} {cx-8} {cy+11}" fill="none" stroke="#7c3aed" stroke-width="2.2"/>')
    return f'<circle cx="{cx}" cy="{cy}" r="10" fill="#ede9fe" stroke="{col}" stroke-width="2"/><text x="{cx}" y="{cy+4}" font-size="10" font-weight="900" fill="{col}" text-anchor="middle">NO</text>'

def panel_hub(y):
    h = 470
    s = [_seccion(y, "NADPH: ¿PARA QUÉ SE USA?", "poder reductor de la célula")]
    s.append(f'<g transform="translate({X0},{y+38})">')
    s.append(_card(0, 0, WP, h - 38, "#cbd5e1"))
    cx, cy = 320, 216
    usos = [
        (10, 20, "gota", "#b45309", "SÍNTESIS REDUCTORA", ["Ácidos grasos, colesterol,", "esteroides"], "hígado · adiposo · mama"),
        (430, 20, "escudo", "#047857", "ANTIOXIDANTE", ["GSSG → 2 GSH", "(H₂O₂ → H₂O con GSH)"], "eritrocito · cristalino"),
        (10, 165, "adn", "#475569", "DESOXIRRIBONUCLEÓTIDOS", ["Ribonucleótido reductasa", "(vía tiorredoxina)"], "células en división"),
        (430, 165, "estrella", "#dc2626", "EXPLOSIÓN RESPIRATORIA", ["NADPH oxidasa → O₂⁻", "mata bacterias"], "neutrófilos · macrófagos"),
        (10, 310, "hex", "#0284c7", "DETOXIFICACIÓN", ["Citocromo P450", "(fármacos y xenobióticos)"], "hígado"),
        (430, 310, "no", "#7c3aed", "ÓXIDO NÍTRICO", ["NO sintasa:", "arginina → NO + citrulina"], "endotelio · macrófagos"),
    ]
    for (x, yy, k, c, tit, ls, tej) in usos:
        ex = x + 200 if x < 300 else x
        ey = yy + 56
        sx, sy = (cx - 58 * (1 if x > 300 else -1) if False else (cx + (-58 if x < 300 else 58))), cy + (-32 if yy < 100 else (0 if yy < 250 else 32))
        s.append(_line(sx, sy, ex + (2 if x < 300 else -2), ey, "#059669", "mGr", 2.4))
    s.append(f'<circle cx="{cx}" cy="{cy}" r="58" fill="#dcfce7" stroke="#059669" stroke-width="3"/>')
    s.append(_t(cx, cy - 2, "NADPH", 21, 900, "#047857", "middle")); s.append(_t(cx, cy + 16, "poder reductor", 10, 700, "#059669", "middle"))
    for (x, yy, k, c, tit, ls, tej) in usos:
        s.append(_card(x, yy, 200, 112, c, "#ffffff", 12))
        s.append(_glifo(k, x + 26, yy + 28, c))
        s.append(_t(x + 46, yy + 24, tit, 9.5, 900, c, extra=""))
        for i, ln in enumerate(ls):
            s.append(_t(x + 14, yy + 52 + 13 * i, ln, 10, 600, "#475569"))
        s.append(_pill(x + 100, yy + 92, tej, c, "#ffffff", 180, 16, 9))
    s.append('</g>')
    return "\n".join(s), y + h + 14

# ---- D. Tejidos ------------------------------------------------------------
def panel_tejidos(y):
    h = 160
    s = [_seccion(y, "ACTIVIDAD POR TEJIDO", "según su demanda de NADPH / ribosa")]
