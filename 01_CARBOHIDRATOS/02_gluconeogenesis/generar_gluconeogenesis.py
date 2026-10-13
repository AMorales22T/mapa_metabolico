#!/usr/bin/env python3
"""
MAPA METABÓLICO INTEGRADO DE LA GLUCONEOGÉNESIS (VÍA ANABÓLICA DE LA GLUCOSA)
=============================================================================
Visualización Rigurosa de Biología Estructural y Bioquímica Universitaria.
Diseñado bajo el estándar de un mapa metabólico de bioquímica real:
- Estructuras químicas moleculares completas (Fischer, Haworth, Kekulé) sin puntos.
- Los 3 Bypasses de la glucólisis claramente destacados con enzimas sustituidas:
    * Bypass 1: Piruvato -> Oxaloacetato -> PEP (PC, PEPCK; sustituye a Piruvato Quinasa / PK).
    * Bypass 2: F-1,6-BP -> F-6-P (FBPasa-1, hidrólisis de fosfato; sustituye a PFK-1).
    * Bypass 3: G-6-P -> Glucosa (G6Pase en el RE; sustituye a Hexoquinasa/Glucoquinasa / HK/GK).
- Regulación tándem explícita PFK-2 / FBPasa-2 con estructura de F-2,6-BP, enzima bifuncional,
  cascada hormonal hepática (Glucagón/PKA vs Insulina/PP1) y conexiones alostéricas diana directas.
- Reorganización total de precursores con estructuras completas y puntos de entrada exactos:
    * Glicerol -> Glicerol-3-P -> DHAP (entra a triosas fosfato sin pasar por piruvato).
    * L-Lactato -> Piruvato (Ciclo de Cori funcional músculo-hígado, LDH, NAD+/NADH).
    * L-Alanina -> Piruvato (Ciclo de Cahill glucosa-alanina, ALT, transaminación a glutamato/urea).
    * Cataplerosis del Ciclo de Krebs (distinguida de piruvato: alimenta el pool de Oxaloacetato).
- Reacciones compartidas y reversibles distinguidas con dobles flechas continuas verdes.
- Transporte mitocondrial del oxaloacetato (Lanzadera de Malato OGC y balance redox NADH/NAD+).
- Destino y rastreo del número de carbonos (6C, 4C, 3C), fijación (+CO2) y liberación (-CO2).
- Cero cajas de texto, tarjetas ni paneles explicativos: información sobre estructuras y flechas.
- Cero solapamientos ni cruces confusos.
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
    OXALACETATO, MALATO, LACTATO, RE_GLUCOSA_6_FOSFATASA, GLICEROL,
    GLICEROL_3_FOSFATO, FRUCTOSA_2_6_BISFOSFATO
)

from estructuras_aminoacidos import (
    ALANINA as AMINO_ALANINA
)

ANCHO_CANVAS = 1900
ALTO_CANVAS = 3700

# Ejes de alineación principales
X_EJE = 680        # Eje central de estructuras de hexosas y triosas
X_FLECHA = 720     # Eje vertical de flechas principales

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gluconeogénesis - Mapa Bioquímico y Biología Estructural</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700;800;900&display=swap" rel="stylesheet">
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
        <!-- Marcadores estándar de flecha -->
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

        <!-- Marcadores para Regulación Alostérica: Activación (+) e Inhibición (-) -->
        <marker id="markerActivaVerde" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
          <path d="M 0 0 L 8 4 L 0 8 Z" fill="#16a34a" />
        </marker>
        <marker id="markerInhibeRojo" markerWidth="8" markerHeight="10" refX="3" refY="5" orient="auto">
          <line x1="2" y1="0" x2="2" y2="10" stroke="#dc2626" stroke-width="3.5" stroke-linecap="round"/>
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
    color_fondo = "#7c3aed" if es_bypass else "#059669"
    texto_etiq = f'<text x="18" y="4" fill="{color_fondo}" font-size="10.5" font-weight="900" font-family="\'Inter\', sans-serif">{etiqueta}</text>' if etiqueta else ""
    return f"""
    <g class="badge-paso" transform="translate({x}, {y})">
      <circle cx="0" cy="0" r="12" fill="{color_fondo}" stroke="#ffffff" stroke-width="2"/>
      <text x="0" y="4" fill="#ffffff" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{num}</text>
      {texto_etiq}
    </g>
    """

def generar_entorno_gluconeogenesis(ancho, alto, y_mito=2650):
    """Entorno biológico abierto sin cajas pesadas con rótulos de compartimento explícitos."""
    return f"""
    <!-- Fondo Citoplasmático Celular -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#gradCitosol)" />

    <!-- Filamentos citoesqueléticos tenues -->
    <g opacity="0.2" stroke="#94a3b8" fill="none">
      <path d="M 50 240 Q 350 180 700 260 T {ancho-50} 230" stroke-width="1.4" stroke-dasharray="8 6" />
      <path d="M 60 560 Q 400 620 780 570 T {ancho-60} 600" stroke-width="1.2" stroke-dasharray="6 6" />
      <path d="M 40 1020 Q 420 960 820 1030 T {ancho-40} 990" stroke-width="1.4" stroke-dasharray="8 5" />
      <path d="M 50 1480 Q 380 1540 740 1490 T {ancho-50} 1520" stroke-width="1.4" stroke-dasharray="7 7" />
      <path d="M 40 1950 Q 450 1900 880 1960 T {ancho-40} 1920" stroke-width="1.4" stroke-dasharray="8 6" />
    </g>

    <!-- Membrana plasmática superior (Sangre / Espacio Extracelular) -->
    <path d="M 0 0 L {ancho} 0 L {ancho} 65 Q {ancho*0.5} 88 0 65 Z" fill="url(#gradExtracelular)" stroke="#cbd5e1" stroke-width="1"/>
    <text x="50" y="26" fill="#475569" font-size="12" font-weight="900" letter-spacing="1">ESPACIO EXTRACELULAR / TORRENTE SANGUÍNEO</text>
    <text x="50" y="44" fill="#0284c7" font-size="10.5" font-weight="700">[Glucemia Fisiológica en Ayuno: 70-100 mg/dL (Mantenida por Hígado y Riñón)]</text>

    <!-- Bicapa Fosfolipídica Ondulada Celular -->
    <path d="M 0 65 Q {ancho*0.5} 88 {ancho} 65" fill="none" stroke="#0284c7" stroke-width="7" stroke-linecap="round"/>
    <path d="M 0 72 Q {ancho*0.5} 95 {ancho} 72" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round"/>

    <!-- Transportador GLUT-2 en la membrana plasmática (Exporta Glucosa libre) -->
    <g transform="translate(680, 48)">
      <path d="M 0 5 C 10 -12, 28 -12, 34 5 C 38 18, 34 36, 25 42 C 12 45, 2 35, 0 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <path d="M 80 5 C 70 -12, 52 -12, 46 5 C 42 18, 46 36, 55 42 C 68 45, 78 35, 80 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <ellipse cx="40" cy="20" rx="10" ry="18" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8"/>
      
      <!-- Molécula de glucosa saliendo hacia la sangre -->
      <polygon points="40,14 45,17 45,23 40,26 35,23 35,17" fill="#ffffff" stroke="#ea580c" stroke-width="1.5"/>
      <circle cx="35" cy="17" r="2" fill="#dc2626"/>

      <text x="40" y="49" fill="#0369a1" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-2</text>
    </g>

    <!-- Flecha de salida hacia el torrente sanguíneo (PASO 14) -->
    <line x1="720" y1="120" x2="720" y2="82" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    {badge_paso(14, 750, 102, es_bypass=False, etiqueta="PASO 14: Liberación a Sangre (Km ≈ 15-20 mM)")}

    <!-- Rótulo de Compartimento: CITOSOL -->
    <g transform="translate(50, 110)">
      <text x="0" y="0" fill="#1e293b" font-size="22" font-weight="900" letter-spacing="2">CITOSOL</text>
      <text x="0" y="18" fill="#64748b" font-size="11" font-weight="700">Fase citoplasmática: tramos reversibles y bypasses hidrolíticos/descarboxilantes</text>
    </g>

    <!-- Mitocondria Biológica (Compartimento Matriz) -->
    <g id="mitocondria-biologica-gng" transform="translate(0, {y_mito})">
      <!-- Membrana Mitocondrial Externa Lisa -->
      <path d="M 0 50 Q 400 15 800 35 T {ancho} 25 L {ancho} {alto - y_mito} L 0 {alto - y_mito} Z" 
            fill="url(#gradMitocondria)" stroke="#b45309" stroke-width="3"/>
      
      <!-- Espacio Intermembrana -->
      <path d="M 0 65 Q 400 30 800 50 T {ancho} 40" 
            fill="none" stroke="#78350f" stroke-width="1.8" stroke-dasharray="6 3"/>

      <!-- Crestas Mitocondriales de la MMI -->
      <path d="M 60 160 C 130 90, 170 190, 270 130 C 330 190, 280 240, 140 220 Z" 
            fill="#fef3c7" stroke="#b45309" stroke-width="2" opacity="0.8"/>

      <!-- Transportador MPC (Carrier Mitocondrial de Piruvato) alineado en X=1280 -->
      <g transform="translate(1245, 22)">
        <rect x="0" y="0" width="70" height="26" rx="6" fill="#b45309" stroke="#78350f" stroke-width="1.8"/>
        <text x="35" y="18" fill="#ffffff" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MPC</text>
      </g>
      <text x="1280" y="12" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#78350f" text-anchor="middle">
        Carrier MPC (SLC54A1)
      </text>

      <!-- Rótulo de la Matriz Mitocondrial -->
      <g transform="translate(50, 95)">
        <text x="0" y="0" fill="#78350f" font-size="22" font-weight="900" letter-spacing="2">MATRIZ MITOCONDRIAL</text>
        <text x="0" y="18" fill="#92400e" font-size="11.5" font-weight="700">Fase inicial de la Gluconeogénesis: fijación de CO₂ y centro de Cataplerosis</text>
      </g>

      <!-- Transportador OGC (Lanzadera Malato / α-KG) alineado en X=220 -->
      <g transform="translate(185, 22)">
        <rect x="0" y="0" width="70" height="26" rx="6" fill="#047857" stroke="#064e3b" stroke-width="1.8"/>
        <text x="35" y="17" fill="#ffffff" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">OGC</text>
      </g>
      <text x="220" y="12" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#047857" text-anchor="middle">
        Carrier Malato / α-KG (SLC25A11)
      </text>
    </g>
    """

def crear_metabolito(x, y, nombre, carbonos, formula="", svg_estructura="", texto_izquierda=False, dx_texto=115, badge_color="#ea580c"):
    """Metabolito abierto donde la estructura molecular es protagonista con badge de carbonos visible."""
    rotulo_formula = f'<text x="0" y="32" fill="#64748b" font-size="10" font-family="\'JetBrains Mono\', monospace">{formula}</text>' if formula else ""

    if texto_izquierda:
        pos_estructura = "translate(0, 0)"
        pos_texto = "translate(-30, 24)"
        badge_svg = f"""
        <g transform="translate(0, -18)">
          <rect x="-42" y="0" width="42" height="18" rx="4" fill="{badge_color}" opacity="0.14"/>
          <rect x="-42" y="0" width="42" height="18" rx="4" fill="none" stroke="{badge_color}" stroke-width="1.4"/>
          <text x="-21" y="13" fill="{badge_color}" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{carbonos}</text>
        </g>
        """
        alineacion = 'text-anchor="end"'
        rotulo_formula = f'<text x="0" y="32" fill="#64748b" font-size="10" font-family="\'JetBrains Mono\', monospace" {alineacion}>{formula}</text>' if formula else ""
        return f"""
        <!-- Metabolito: {nombre} -->
        <g transform="translate({x}, {y})">
          <g transform="{pos_estructura}">
            {svg_estructura}
          </g>
          <g transform="{pos_texto}">
            {badge_svg}
            <text x="0" y="14" fill="#0f172a" font-size="15" font-weight="900" font-family="'Inter', sans-serif" {alineacion}>{nombre}</text>
            {rotulo_formula}
          </g>
        </g>
        """
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = f"translate({dx_texto}, 24)"
        badge_svg = f"""
        <g transform="translate(0, -18)">
          <rect x="0" y="0" width="42" height="18" rx="4" fill="{badge_color}" opacity="0.14"/>
          <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="{badge_color}" stroke-width="1.4"/>
          <text x="21" y="13" fill="{badge_color}" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{carbonos}</text>
        </g>
        """
        rotulo_formula = f'<text x="0" y="32" fill="#64748b" font-size="10" font-family="\'JetBrains Mono\', monospace">{formula}</text>' if formula else ""
        return f"""
        <!-- Metabolito: {nombre} -->
        <g transform="translate({x}, {y})">
          <g transform="{pos_estructura}">
            {svg_estructura}
          </g>
          <g transform="{pos_texto}">
            {badge_svg}
            <text x="0" y="14" fill="#0f172a" font-size="15" font-weight="900" font-family="'Inter', sans-serif">{nombre}</text>
            {rotulo_formula}
          </g>
        </g>
        """

def crear_reaccion_ascendente(x, y, enzima, ec="", entra_energia="", sale_energia="", delta_co2="",
                              activadores=None, inhibidores=None, reversible=False, 
                              salida_agua=False, entrada_agua=False, altura=55, num_paso=None, 
                              es_bypass=False, titulo_bypass="", sustituye_glucolisis="", nota_adicional="", etiqueta_paso=""):
    """Flecha ascendente con moduladores alostéricos, energía, CO2 y distinción de bypass vs reversible."""
    curvas_energia = ""
    y_arco_in = 52
    y_arco_out = 32
    y_arco_co2 = 12

    if entra_energia:
        curvas_energia += f"""
        <path d="M -85 {y_arco_in} Q -30 {y_arco_in} -4 38" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
        <text x="-92" y="{y_arco_in + 4}" fill="#dc2626" font-size="11" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
    if sale_energia:
        curvas_energia += f"""
        <path d="M -4 28 Q -30 {y_arco_out} -85 {y_arco_out}" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="-92" y="{y_arco_out + 4}" fill="#475569" font-size="11" font-weight="800" text-anchor="end">{sale_energia}</text>
        """
    if delta_co2:
        if delta_co2.startswith("+") or "Fijación" in delta_co2:
            curvas_energia += f"""
            <path d="M -85 52 Q -30 52 -4 36" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
            <text x="-92" y="56" fill="#0284c7" font-size="11" font-weight="900" text-anchor="end">{delta_co2}</text>
            """
        else:
            curvas_energia += f"""
            <path d="M -4 20 Q -30 {y_arco_co2} -85 {y_arco_co2}" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
            <text x="-92" y="{y_arco_co2 + 4}" fill="#ea580c" font-size="11" font-weight="900" text-anchor="end">{delta_co2}</text>
            """

    if entrada_agua:
        curvas_energia += f"""
        <path d="M -85 48 Q -30 48 -4 34" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-92" y="52" fill="#0284c7" font-size="11" font-weight="800" text-anchor="end">+ H₂O</text>
        """

    if salida_agua:
        curvas_energia += f"""
        <path d="M -85 38 Q -30 38 -4 26" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-92" y="42" fill="#0284c7" font-size="11" font-weight="800" text-anchor="end">+ H₂O</text>
        """

    if es_bypass:
        color_flecha = "#7c3aed"
        marker_url = "url(#arrowPurple)"
        flecha = f"""
        <line x1="0" y1="{altura}" x2="0" y2="0" stroke="{color_flecha}" stroke-width="3" marker-end="{marker_url}"/>
        """
        encabezado_tipo = f"""
        <text x="0" y="-12" fill="#6d28d9" font-size="11" font-weight="900" font-family="'Inter', sans-serif">{titulo_bypass}</text>
        <text x="0" y="0" fill="#b91c1c" font-size="10" font-weight="800" font-family="'Inter', sans-serif">Sustituye a: {sustituye_glucolisis}</text>
        """
        y_text_enz = 15
    elif reversible:
        color_flecha = "#059669"
        flecha = f"""
        <line x1="-3.5" y1="{altura}" x2="-3.5" y2="0" stroke="{color_flecha}" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
        <line x1="3.5" y1="0" x2="3.5" y2="{altura}" stroke="{color_flecha}" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
        """
        encabezado_tipo = f"""
        <text x="0" y="-2" fill="#059669" font-size="9" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="0.5">[REVERSIBLE: MISMA ENZIMA QUE EN GLUCÓLISIS]</text>
        """
        y_text_enz = 13
    else:
        color_flecha = "#ea580c"
        flecha = f"""
        <line x1="0" y1="{altura}" x2="0" y2="0" stroke="{color_flecha}" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
        """
        encabezado_tipo = ""
        y_text_enz = 12

    # Moduladores alostéricos y notas directas
    moduladores_svg = ""
    y_mod = y_text_enz + 26
    if activadores:
        texto_act = "(+) " + ", ".join(activadores)
        moduladores_svg += f'<text x="0" y="{y_mod}" fill="#16a34a" font-size="10.5" font-weight="800">{texto_act}</text>'
        y_mod += 14
    if inhibidores:
        texto_inh = "(-) " + ", ".join(inhibidores)
        moduladores_svg += f'<text x="0" y="{y_mod}" fill="#dc2626" font-size="10.5" font-weight="800">{texto_inh}</text>'
        y_mod += 14
    if nota_adicional:
        moduladores_svg += f'<text x="0" y="{y_mod}" fill="#475569" font-size="9.5" font-weight="700">{nota_adicional}</text>'

    badge_svg = badge_paso(num_paso, -26, altura // 2, es_bypass=es_bypass, etiqueta="") if num_paso else ""

    return f"""
    <!-- Reacción Ascendente: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha}
      {curvas_energia}
      {badge_svg}
      <g transform="translate(32, 10)">
        {encabezado_tipo}
        <text x="0" y="{y_text_enz}" fill="#0f172a" font-size="14" font-weight="900">{enzima}</text>
        <text x="0" y="{y_text_enz + 13}" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {moduladores_svg}
      </g>
    </g>
    """

def generar_mapa_gluconeogenesis():
    """Generador principal con precursores integrados y regulación explícita PFK-2/FBPasa-2/F-2,6-BP."""
    svg_parts = []

    # 1. Capa de entorno celular biológico (ancho=1900, alto=3700, y_mito=2650)
    svg_parts.append(generar_entorno_gluconeogenesis(ANCHO_CANVAS, ALTO_CANVAS, y_mito=2650))

    # =========================================================================
    # EJE CENTRAL: RUTA DE ESTRUCTURAS QUÍMICAS (PASOS 1 AL 14)
    # =========================================================================

    # -------------------------------------------------------------------------
    # 1. D-Glucosa Libre (Producto Final)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=150,
        nombre="D-Glucosa Libre",
        carbonos="6 C",
        formula="C₆H₁₂O₆ (Hexosa neutra, exportable por GLUT-2)",
        svg_estructura=GLUCOSA,
        dx_texto=135,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 13: BYPASS 3 - Glucosa-6-Fosfatasa en el Retículo Endoplásmico
    # Sustituye a la Hexoquinasa / Glucoquinasa de la Glucólisis
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- PASO 13: BYPASS 3 - G6Pasa en el RE (cisterna + bicapa + T1/T2/T3) -->
    <g transform="translate(40, 195)">
      {RE_GLUCOSA_6_FOSFATASA}
      {badge_paso(13, 12, -48, es_bypass=True, etiqueta="PASO 13: BYPASS 3")}
    </g>

    <!-- Flechas citosol <-> RE (coordenadas absolutas) -->
    <path d="M 645 428 Q 530 452 424 462" fill="none" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowPurple)"/>
    <path d="M 424 273 Q 545 262 642 198" fill="none" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    <path d="M 424 220 L 478 220" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
    <rect x="482" y="211" width="38" height="18" rx="9" fill="#fef3c7" stroke="#b45309" stroke-width="1.6"/>
    <text x="501" y="224.5" font-size="10.5" font-weight="900" fill="#b45309" text-anchor="middle" font-family="'Inter', sans-serif">Pi</text>
    """)

    # -------------------------------------------------------------------------
    # 2. Glucosa-6-Fosfato (G-6-P)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=385,
        nombre="Glucosa-6-Fosfato (G-6-P)",
        carbonos="6 C",
        formula="C₆H₁₁O₉P²⁻ (Hexosa fosforilada)",
        svg_estructura=GLUCOSA_6_FOSFATO,
        dx_texto=135,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 12: Fosfoglucosa Isomerasa (PGI) - Reacción Reversible Compartida
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=500,
        enzima="Fosfoglucosa Isomerasa (PGI)",
        ec="EC 5.3.1.9",
        altura=45,
        reversible=True,
        num_paso=12,
        es_bypass=False,
        etiqueta_paso="PASO 12"
    ))

    # -------------------------------------------------------------------------
    # 3. Fructosa-6-Fosfato (F-6-P)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=600,
        nombre="Fructosa-6-Fosfato (F-6-P)",
        carbonos="6 C",
        formula="C₆H₁₁O₉P²⁻ (Cetosa fosforilada)",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        dx_texto=135,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 11: BYPASS 2 - Fructosa-1,6-Bisfosfatasa-1 (FBPasa-1)
    # Sustituye a la Fosfofructocinasa-1 (PFK-1) de la Glucólisis
    # Muestra también la flecha glucolítica opuesta de PFK-1 para visibilizar el ciclo de sustrato
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- REACCIÓN ASCENDENTE: FBPasa-1 (GLUCONEOGÉNESIS) Y REACCIÓN DESCENDENTE OPUESTA PFK-1 (GLUCÓLISIS) -->
    <g transform="translate({X_FLECHA}, 715)">
      <!-- Flecha ascendente morada de FBPasa-1 (Gluconeogénesis) -->
      <line x1="-8" y1="55" x2="-8" y2="0" stroke="#7c3aed" stroke-width="3" marker-end="url(#arrowPurple)"/>
      {badge_paso(11, -34, 27, es_bypass=True, etiqueta="")}

      <!-- Curvas de energía de FBPasa-1: hidrólisis simple (+H2O -> +Pi) -->
      <path d="M -90 48 Q -40 48 -12 34" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="-96" y="52" fill="#0284c7" font-size="11" font-weight="800" text-anchor="end">+ H₂O</text>

      <path d="M -12 20 Q -40 16 -90 16" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-96" y="20" fill="#475569" font-size="11" font-weight="800" text-anchor="end">+ Pi</text>

      <!-- Flecha descendente complementaria de PFK-1 (Glucólisis) -->
      <line x1="8" y1="0" x2="8" y2="55" stroke="#ea580c" stroke-width="2.2" stroke-dasharray="5 3" marker-end="url(#arrowFlow)"/>

      <!-- Textos de FBPasa-1 y mención de PFK-1 en columna central (X = 744 a 980) -->
      <g transform="translate(24, 8)">
        <text x="0" y="-10" fill="#6d28d9" font-size="11" font-weight="900" font-family="'Inter', sans-serif">BYPASS 2</text>
        <text x="0" y="2" fill="#b91c1c" font-size="10" font-weight="800" font-family="'Inter', sans-serif">Sustituye a: Fosfofructocinasa-1 (PFK-1)</text>
        
        <text x="0" y="16" fill="#0f172a" font-size="13" font-weight="900">Fructosa-1,6-Bisfosfatasa-1 (FBPasa-1)</text>
        <text x="0" y="29" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">EC 3.1.3.11 (Hidrólisis simple de fosfato)</text>
        
        <text x="0" y="43" fill="#16a34a" font-size="10" font-weight="800">(+) Citrato (Abundancia energética)</text>
        <text x="0" y="56" fill="#dc2626" font-size="10" font-weight="800">(-) AMP, Fructosa-2,6-bisfosfato (F-2,6-BP)</text>

        <!-- Rótulo directo de la flecha glucolítica PFK-1 -->
        <text x="0" y="70" fill="#ea580c" font-size="10" font-weight="800">
          [Glucólisis: PFK-1 (EC 2.7.1.11) invierte 1 ATP]
        </text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # MÓDULO EXPLÍCITO: ENZIMA BIFUNCIONAL PFK-2 / FBPasa-2, FRUCTOSA-2,6-BISFOSFATO (F-2,6-BP)
    # Y CASCADA HORMONAL HEPÁTICA (GLUCAGÓN / PKA vs INSULINA / PP1)
    # Ubicado en X = 1360 a 1880 con total holgura espacial
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- MÓDULO REGULATORIO PFK-2 / FBPasa-2 Y F-2,6-BP -->
    <g transform="translate(1360, 560)">
      <!-- Rótulo del Sistema -->
      <text x="0" y="0" fill="#6d28d9" font-size="12.5" font-weight="900" letter-spacing="0.5">
        ENZIMA BIFUNCIONAL HEPÁTICA: PFK-2 / FBPasa-2
      </text>
      <text x="0" y="14" fill="#475569" font-size="9.5" font-weight="700">
        Control maestro del conmutador alostérico Glucólisis ⇄ Gluconeogénesis
      </text>

      <!-- 1. Enzima Bifuncional Hepática PFK-2/FBPasa-2 (Diagrama de Dominios) -->
      <g transform="translate(0, 26)">
        <rect x="0" y="0" width="160" height="26" rx="5" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>
        <text x="80" y="17" fill="#b91c1c" font-size="10" font-weight="900" text-anchor="middle">Dominio PFK-2 (Quinasa)</text>

        <!-- Enlace peptídico central con residuo regulatorio Ser-32 -->
        <line x1="160" y1="13" x2="200" y2="13" stroke="#0f172a" stroke-width="2"/>
        <circle cx="180" cy="13" r="9" fill="#fef9c3" stroke="#b45309" stroke-width="1.6"/>
        <text x="180" y="16" fill="#78350f" font-size="8" font-weight="900" text-anchor="middle">Ser-32</text>

        <rect x="200" y="0" width="170" height="26" rx="5" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
        <text x="285" y="17" fill="#6d28d9" font-size="10" font-weight="900" text-anchor="middle">Dominio FBPasa-2 (Fosfatasa)</text>

        <text x="380" y="17" fill="#64748b" font-size="9" font-weight="700">(Misma proteína dímera)</text>
      </g>

      <!-- 2. Cascada Hormonal Hepática: Glucagón vs Insulina -->
      <g transform="translate(0, 68)">
        <!-- Vía Glucagón (Ayuno) -->
        <g transform="translate(0, 0)">
          <path d="M 0 8 L 30 8" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
          <text x="36" y="11" fill="#ea580c" font-size="10" font-weight="900">Glucagón (Ayuno)</text>
          <text x="135" y="11" fill="#b45309" font-size="9.5" font-weight="800">➔ cAMP ↑ ➔ PKA ➔ Fosforila Ser-32 ➔</text>
          <text x="330" y="11" fill="#7c3aed" font-size="10" font-weight="900">ACTIVA FBPasa-2</text>
        </g>

        <!-- Vía Insulina (Posprandial) -->
        <g transform="translate(0, 20)">
          <path d="M 0 8 L 30 8" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
          <text x="36" y="11" fill="#0284c7" font-size="10" font-weight="900">Insulina (Saciedad)</text>
          <text x="135" y="11" fill="#0369a1" font-size="9.5" font-weight="800">➔ PP1 (Fosfatasa) ➔ Desfosforila Ser-32 ➔</text>
          <text x="330" y="11" fill="#b91c1c" font-size="10" font-weight="900">ACTIVA PFK-2</text>
        </g>
      </g>

      <!-- 3. Ciclo Local de Interconversión F-6-P ⇄ F-2,6-BP con Estructura Molecular -->
      <g transform="translate(30, 115)">
        <!-- Conector superior desde el pool de F-6-P -->
        <text x="150" y="0" fill="#0f172a" font-size="11" font-weight="900" text-anchor="middle">
          Fructosa-6-Fosfato (F-6-P) [Pool Citosólico]
        </text>

        <!-- Flecha hacia abajo: Actividad PFK-2 (Insulina) -->
        <line x1="70" y1="12" x2="70" y2="52" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
        <g transform="translate(62, 34)">
          <text x="-10" y="-3" fill="#dc2626" font-size="9.5" font-weight="900" text-anchor="end">PFK-2 (- 1 ATP)</text>
          <text x="-10" y="9" fill="#991b1b" font-size="8.5" font-weight="700" text-anchor="end">[Insulina activa]</text>
        </g>

        <!-- Flecha hacia arriba: Actividad FBPasa-2 (Glucagón) -->
        <line x1="230" y1="52" x2="230" y2="12" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arrowPurple)"/>
        <g transform="translate(238, 34)">
          <text x="10" y="-3" fill="#7c3aed" font-size="9.5" font-weight="900">FBPasa-2 (+ H₂O ➔ + Pi)</text>
          <text x="10" y="9" fill="#5b21b6" font-size="8.5" font-weight="700">[Glucagón/PKA activa]</text>
        </g>

        <!-- Estructura molecular de F-2,6-BP centrada -->
        <g transform="translate(100, 60)">
          {FRUCTOSA_2_6_BISFOSFATO}
          
          <g transform="translate(125, 24)">
            <g transform="translate(0, -18)">
              <rect x="0" y="0" width="42" height="18" rx="4" fill="#7c3aed" opacity="0.14"/>
              <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#7c3aed" stroke-width="1.4"/>
              <text x="21" y="13" fill="#7c3aed" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">6 C</text>
            </g>
            <text x="0" y="14" fill="#0f172a" font-size="13" font-weight="900">Fructosa-2,6-Bisfosfato (F-2,6-BP)</text>
            <text x="0" y="27" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">Señal alostérica potente</text>
          </g>
        </g>

        <!-- Consecuencia fisiológica explicada directamente -->
        <g transform="translate(0, 185)">
          <text x="0" y="0" fill="#047857" font-size="10.5" font-weight="900">
            EFECTO DEL AYUNO (GLUCAGÓN / ADRENALINA):
          </text>
          <text x="0" y="14" fill="#15803d" font-size="9.5" font-weight="700">
            FBPasa-2 degrada F-2,6-BP ➔ Caída de F-2,6-BP ➔ DESINHIBICIÓN DE FBPasa-1 ➔ VÍA GLUCONEOGÉNICA ACTIVA
          </text>
        </g>
      </g>
    </g>

    <!-- 4. LÍNEAS DE REGULACIÓN ALOSTÉRICA DIRECTAS: Conectan desde F-2,6-BP al borde derecho de FBPasa-1 y PFK-1 (terminando en X=1000 sin cruzar textos) -->
    <!-- Conexión 1: F-2,6-BP INHIBE ALOSTÉRICAMENTE FBPasa-1 -->
    <path d="M 1450 780 Q 1200 730 1005 730" fill="none" stroke="#dc2626" stroke-width="2.6" stroke-dasharray="6 4" marker-end="url(#markerInhibeRojo)"/>
    <text x="1220" y="722" fill="#dc2626" font-size="10" font-weight="900" text-anchor="middle">
      (-) Inhibe alostéricamente FBPasa-1 (Gluconeogénesis ↓)
    </text>

    <!-- Conexión 2: F-2,6-BP ACTIVA ALOSTÉRICAMENTE PFK-1 -->
    <path d="M 1450 795 Q 1200 785 1005 785" fill="none" stroke="#16a34a" stroke-width="2.6" stroke-dasharray="6 4" marker-end="url(#markerActivaVerde)"/>
    <text x="1220" y="780" fill="#16a34a" font-size="10" font-weight="900" text-anchor="middle">
      (+) Activa alostéricamente PFK-1 (Glucólisis ↑)
    </text>
    """)

    # -------------------------------------------------------------------------
    # 4. Fructosa-1,6-Bisfosfato (F-1,6-BP)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=860,
        nombre="Fructosa-1,6-Bisfosfato (F-1,6-BP)",
        carbonos="6 C",
        formula="C₆H₁₀O₁₂P₂⁴⁻ (Hexosa bisfosforilada)",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO,
        dx_texto=135,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 10: Aldolasa - Condensación Aldólica Reversible (3C + 3C -> 6C)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=980,
        enzima="Aldolasa A / B (Condensación Aldólica)",
        ec="EC 4.1.2.13 (Condensación reversible: 3 C + 3 C -> 6 C)",
        altura=45,
        reversible=True,
        num_paso=10,
        es_bypass=False,
        etiqueta_paso="PASO 10"
    ))

    # -------------------------------------------------------------------------
    # PRECURSOR 3: GLICEROL [3 C] - REORGANIZACIÓN COMPLETA
    # Incorporación directa a nivel de Triosas Fosfato (DHAP) con Glicerol-3-P
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- PRECURSOR 3: GLICEROL Y SU INCORPORACIÓN DIRECTA A DHAP VIA GLICEROL-3-FOSFATO -->
    <g transform="translate(60, 1050)">
      <!-- Encabezado del Precursor -->
      <g transform="translate(0, -18)">
        <rect x="0" y="0" width="42" height="18" rx="4" fill="#0284c7" opacity="0.14"/>
        <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#0284c7" stroke-width="1.4"/>
        <text x="21" y="13" fill="#0284c7" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
      </g>
      <text x="48" y="-4" fill="#0284c7" font-size="12" font-weight="900">PRECURSOR: GLICEROL</text>
      <text x="0" y="14" fill="#64748b" font-size="9.5">Origen: Lipólisis de Triglicéridos en Tejido Adiposo</text>

      <!-- 1. Molécula: Glicerol [3 C] -->
      <g transform="translate(0, 24)">
        {GLICEROL}
      </g>
      <g transform="translate(100, 48)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">Glicerol [3 C]</text>
        <text x="0" y="14" fill="#64748b" font-size="9.5">Lipólisis adiposa libera glicerol a sangre</text>
      </g>

      <!-- 2. Reacción: Glicerol Cinasa (GK) con gasto de 1 ATP -->
      <g transform="translate(50, 140)">
        <line x1="0" y1="0" x2="0" y2="40" stroke="#dc2626" stroke-width="2.4" marker-end="url(#arrowRed)"/>
        
        <!-- Curvas de ATP -> ADP -->
        <path d="M -60 10 Q -25 10 -4 18" fill="none" stroke="#dc2626" stroke-width="1.6" marker-end="url(#arrowRed)"/>
        <text x="-65" y="14" fill="#dc2626" font-size="10" font-weight="800" text-anchor="end">- 1 ATP</text>
        
        <path d="M -4 24 Q -25 32 -60 32" fill="none" stroke="#475569" stroke-width="1.6" marker-end="url(#arrowSlate)"/>
        <text x="-65" y="36" fill="#475569" font-size="10" font-weight="800" text-anchor="end">+ ADP</text>

        <g transform="translate(15, 16)">
          <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Glicerol Cinasa (GK)</text>
          <text x="0" y="12" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 2.7.1.30 (Hepática)</text>
        </g>
      </g>

      <!-- 3. Molécula: Glicerol-3-Fosfato [3 C] -->
      <g transform="translate(0, 200)">
        {GLICEROL_3_FOSFATO}
        <g transform="translate(100, 50)">
          <g transform="translate(0, -18)">
            <rect x="0" y="0" width="42" height="18" rx="4" fill="#0284c7" opacity="0.14"/>
            <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#0284c7" stroke-width="1.4"/>
            <text x="21" y="13" fill="#0284c7" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
          </g>
          <text x="0" y="14" fill="#0f172a" font-size="13" font-weight="800">Glicerol-3-Fosfato (G-3-P)</text>
          <text x="0" y="28" fill="#64748b" font-size="9.5">Intermediario fosforilado</text>
        </g>
      </g>

      <!-- 4. Reacción Redox: G3PDH (+ NAD+ -> + NADH + H+) y Conexión DIRECTA a DHAP -->
      <path d="M 60 330 Q 180 340 320 230 Q 360 190 390 120" fill="none" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>
      <g transform="translate(150, 310)">
        <text x="0" y="0" fill="#059669" font-size="11" font-weight="900">G3PDH Citosólica (EC 1.1.1.8)</text>
        <text x="0" y="14" fill="#047857" font-size="10.5" font-weight="800">+ NAD⁺ ➔ + NADH + H⁺</text>
        <text x="0" y="28" fill="#0284c7" font-size="9.5" font-weight="800">➔ ENTRADA DIRECTA A NIVEL DE TRIOSAS (DHAP)</text>
        <text x="0" y="40" fill="#64748b" font-size="9">Se incorpora a la ruta SIN pasar por Piruvato ni Mitocondria</text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # 5. Triosas Fosfato: DHAP y Gliceraldehído-3-P (Equilibrio por TPI)
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- TRIOSAS FOSFATO: DHAP Y GAP -->
    <g transform="translate(450, 1070)">
      {DIHIDROXIACETONA_FOSFATO}
      <g transform="translate(20, 120)">
        <rect x="0" y="-12" width="40" height="17" rx="4" fill="#ea580c" opacity="0.14"/>
        <rect x="0" y="-12" width="40" height="17" rx="4" fill="none" stroke="#ea580c" stroke-width="1.3"/>
        <text x="20" y="1" fill="#ea580c" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
      </g>
      <text x="40" y="140" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">DHAP</text>
      <text x="40" y="153" fill="#64748b" font-size="9" text-anchor="middle">Cetotriosa Fosfato</text>
    </g>

    <g transform="translate(750, 1070)">
      {GLICERALDEHIDO_3_FOSFATO}
      <g transform="translate(20, 120)">
        <rect x="0" y="-12" width="40" height="17" rx="4" fill="#ea580c" opacity="0.14"/>
        <rect x="0" y="-12" width="40" height="17" rx="4" fill="none" stroke="#ea580c" stroke-width="1.3"/>
        <text x="20" y="1" fill="#ea580c" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
      </g>
      <text x="40" y="140" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">Gliceraldehído-3-P</text>
      <text x="40" y="153" fill="#64748b" font-size="9" text-anchor="middle">Aldotriosa Fosfato</text>
    </g>

    <!-- Conexión y equilibrio TPI entre triosas -->
    <g transform="translate(575, 1105)">
      <line x1="0" y1="-3" x2="80" y2="-3" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <line x1="80" y1="3" x2="0" y2="3" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="40" y="-8" fill="#059669" font-size="10" font-weight="900" text-anchor="middle">TPI (Isomerasa)</text>
      <text x="40" y="18" fill="#64748b" font-size="8.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1 (Reversible)</text>
    </g>

    <!-- Flechas ascendentes convergiendo a Aldolasa -->
    <path d="M 500 1060 Q 590 1010 700 1025" fill="none" stroke="#059669" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
    <path d="M 780 1060 Q 750 1010 720 1025" fill="none" stroke="#059669" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
    """)

    # -------------------------------------------------------------------------
    # PASO 9: GAPDH - Reducción Reversa (Consume NADH citosólico)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 60, y=1260,
        enzima="GAPDH (Reducción Reversa)",
        ec="EC 1.2.1.12",
        altura=55,
        entra_energia="+ 2 NADH + 2 H⁺",
        sale_energia="+ 2 NAD⁺ + 2 Pi",
        nota_adicional="[Consume el NADH citosólico generado por la lanzadera de Malato (cMDH) / LDH / G3PDH]",
        reversible=True,
        num_paso=9,
        es_bypass=False,
        etiqueta_paso="PASO 9"
    ))

    # -------------------------------------------------------------------------
    # 6. 1,3-Bisfosfoglicerato (1,3-BPG)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE + 60, y=1345,
        nombre="1,3-Bisfosfoglicerato (1,3-BPG)",
        carbonos="3 C",
        formula="C₃H₄O₁₀P₂⁴⁻ (Acil-fosfato de alta energía)",
        svg_estructura=BISFOSFOGLICERATO_1_3,
        dx_texto=135,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 8: Fosfoglicerato Cinasa (PGK) - Reversible (Gasto de 2 ATP)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 60, y=1460,
        enzima="Fosfoglicerato Cinasa (PGK)",
        ec="EC 2.7.2.3",
        altura=50,
        entra_energia="- 2 ATP",
        sale_energia="+ 2 ADP",
        nota_adicional="[Invierte 2 ATP por cada molécula de glucosa generada]",
        reversible=True,
        num_paso=8,
        es_bypass=False,
        etiqueta_paso="PASO 8"
    ))

    # -------------------------------------------------------------------------
    # 7. 3-Fosfoglicerato (3-PG)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE + 60, y=1545,
        nombre="3-Fosfoglicerato (3-PG)",
        carbonos="3 C",
        formula="C₃H₄O₇P³⁻",
        svg_estructura=FOSFOGLICERATO_3,
        dx_texto=135,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 7: Fosfoglicerato Mutasa (PGM) - Reversible
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 60, y=1660,
        enzima="Fosfoglicerato Mutasa (PGM)",
        ec="EC 5.4.2.1",
        altura=50,
        reversible=True,
        num_paso=7,
        es_bypass=False,
        etiqueta_paso="PASO 7"
    ))

    # -------------------------------------------------------------------------
    # 8. 2-Fosfoglicerato (2-PG)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE + 60, y=1745,
        nombre="2-Fosfoglicerato (2-PG)",
        carbonos="3 C",
        formula="C₃H₄O₇P³⁻",
        svg_estructura=FOSFOGLICERATO_2,
        dx_texto=135,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 6: Enolasa - Hidratación Reversa
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 60, y=1860,
        enzima="Enolasa (Hidratación Reversa)",
        ec="EC 4.2.1.11",
        altura=50,
        entra_energia="+ H₂O",
        reversible=True,
        num_paso=6,
        es_bypass=False,
        etiqueta_paso="PASO 6"
    ))

    # -------------------------------------------------------------------------
    # 9. Fosfoenolpiruvato (PEP)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE + 60, y=1945,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 C",
        formula="C₃H₂O₆P³⁻ (Enol-fosfato de altísima energía)",
        svg_estructura=FOSFOENOLPIRUVATO,
        dx_texto=135,
        badge_color="#7c3aed"
    ))

    # -------------------------------------------------------------------------
    # PASO 5: BYPASS 1B - PEPCK Citosólica (PCK1)
    # Sustituye a la Piruvato Quinasa (PK) de la Glucólisis
    # Descarboxilación: - CO2 (4C - 1C -> 3C)
    # -------------------------------------------------------------------------
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA + 60, y=2070,
        enzima="PEPCK Citosólica (PCK1)",
        ec="EC 4.1.1.32 (Fosforilación y descarboxilación concertada)",
        altura=60,
        entra_energia="- 1 GTP",
        sale_energia="+ GDP",
        delta_co2="- CO₂ (Descarboxilación: 4 C - 1 C -> 3 C)",
        inhibidores=["ADP (Baja carga energética desvía OAA a Krebs)"],
        nota_adicional="[Inducción génica: Glucagón y Cortisol (CREB/FOXO1) inducen síntesis de PEPCK]",
        reversible=False,
        num_paso=5,
        es_bypass=True,
        titulo_bypass="BYPASS 1B",
        sustituye_glucolisis="Piruvato Quinasa (PK) de la glucólisis"
    ))

    # -------------------------------------------------------------------------
    # RÓTULO DIRECTO DEL BALANCE DE CARBONOS DEL BYPASS 1
    # -------------------------------------------------------------------------
    svg_parts.append("""
    <g transform="translate(340, 2030)">
      <text x="0" y="0" fill="#047857" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace">
        BALANCE DE CARBONOS BYPASS 1:
      </text>
      <text x="0" y="15" fill="#047857" font-size="10" font-family="'JetBrains Mono', monospace">
        3 C (Piruvato) + CO₂ (PC) -> 4 C (OAA) - CO₂ (PEPCK) -> 3 C (PEP)
      </text>
      <text x="0" y="28" fill="#15803d" font-size="9.5" font-weight="700">
        El esqueleto de 3 carbonos del precursor se conserva intacto en el balance neto
      </text>
    </g>
    """)

    # -------------------------------------------------------------------------
    # 10. Oxalacetato Citosólico (OAA Citosólico) [4 C]
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=X_EJE + 60, y=2175,
        nombre="Oxalacetato (OAA Citosólico)",
        carbonos="4 C",
        formula="C₄H₂O₅²⁻ (Dicarboxilato de 4 C)",
        svg_estructura=OXALACETATO,
        dx_texto=105,
        badge_color="#7c3aed"
    ))

    # -------------------------------------------------------------------------
    # 11. L-Malato Citosólico [4 C]
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=220, y=2175,
        nombre="L-Malato (Citosólico)",
        carbonos="4 C",
        formula="C₄H₄O₅²⁻",
        svg_estructura=MALATO,
        texto_izquierda=True,
        badge_color="#047857"
    ))

    # -------------------------------------------------------------------------
    # PASO 4: cMDH (Malato Deshidrogenasa Citosólica)
    # Regenera NADH citosólico imprescindible para GAPDH
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- PASO 4: MDH CITOSÓLICA (cMDH) -->
    <g transform="translate(340, 2235)">
      <line x1="0" y1="0" x2="370" y2="0" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>
      {badge_paso(4, 25, 0, es_bypass=False, etiqueta="")}

      <g transform="translate(185, -12)">
        <text x="0" y="-12" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#6d28d9" text-anchor="middle">cMDH (MDH Citosólica)</text>
        <text x="0" y="2" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#0284c7" text-anchor="middle">Exportación de equivalentes reductores: regenera NADH para GAPDH</text>
        <text x="0" y="22" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#059669" text-anchor="middle">+ NAD⁺ -> + NADH + H⁺</text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # PASO 3: Transporte Transmembrana de Malato vía Carrier OGC (SLC25A11)
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- PASO 3: SALIDA POR CARRIER OGC (TRANSPORTE FÍSICO) -->
    <path d="M 220 3180 L 220 2680 Q 220 2660 220 2480 L 220 2270" fill="none" stroke="#047857" stroke-width="3" stroke-dasharray="8 4" marker-end="url(#arrowGreen)"/>
    {badge_paso(3, 220, 2620, es_bypass=False, etiqueta="")}
    <g transform="translate(245, 2585)">
      <text x="0" y="0" fill="#047857" font-size="11" font-weight="900" font-family="'Inter', sans-serif">Transporte Físico OGC (Antiporte Malato²⁻ / α-KG²⁻)</text>
      <text x="0" y="13" fill="#15803d" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">SLC25A11: exporta esqueleto de 4C y equivalente reductor (NADH) al citosol</text>
      <text x="0" y="26" fill="#64748b" font-size="9" font-family="'Inter', sans-serif">La MMI es completamente impermeable al Oxaloacetato</text>
    </g>
    """)

    # -------------------------------------------------------------------------
    # PRECURSORES CITOSÓLICOS: L-LACTATO (CICLO DE CORI) Y L-ALANINA (CICLO DE CAHILL)
    # Reorganizados con conexión funcional a músculo e hígado, convergencia en Piruvato
    # -------------------------------------------------------------------------

    # PRECURSOR 1: L-Lactato [3 C] (Ciclo de Cori Músculo-Hígado)
    svg_parts.append(f"""
    <!-- PRECURSOR 1: L-LACTATO Y CICLO DE CORI -->
    <g transform="translate(1060, 2150)">
      <!-- Encabezado con Carbonos -->
      <g transform="translate(0, -18)">
        <rect x="0" y="0" width="42" height="18" rx="4" fill="#7c3aed" opacity="0.14"/>
        <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#7c3aed" stroke-width="1.4"/>
        <text x="21" y="13" fill="#7c3aed" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
      </g>
      <text x="48" y="-4" fill="#7c3aed" font-size="12" font-weight="900">PRECURSOR: L-LACTATO</text>
      <text x="0" y="14" fill="#0284c7" font-size="10" font-weight="800">Ciclo de Cori (Intercambio Funcional Músculo ⇄ Hígado)</text>
      <text x="0" y="26" fill="#64748b" font-size="9">Glucólisis anaerobia en eritrocito/músculo genera lactato ➔ sangre ➔ hígado</text>

      <!-- Molécula de Lactato con estructura completa -->
      <g transform="translate(0, 36)">
        {LACTATO}
      </g>

      <!-- Reacción de la Lactato Deshidrogenasa (LDH) -->
      <g transform="translate(115, 56)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">L-Lactato [3 C]</text>
        <text x="0" y="16" fill="#7c3aed" font-size="11" font-weight="800">LDH (Lactato Deshidrogenasa / EC 1.1.1.27)</text>
        <text x="0" y="30" fill="#059669" font-size="11" font-weight="900">+ NAD⁺ ➔ + NADH + H⁺</text>
        <text x="0" y="44" fill="#047857" font-size="9.5" font-weight="700">Genera NADH citosólico imprescindible para GAPDH</text>
      </g>

      <!-- Flecha diagonal convergente hacia Piruvato citosólico -->
      <path d="M 60 145 Q 120 190 160 225" fill="none" stroke="#7c3aed" stroke-width="2.4" marker-end="url(#arrowPurple)"/>
      <text x="120" y="180" fill="#7c3aed" font-size="10" font-weight="800">LDH ➔ Piruvato</text>
    </g>
    """)

    # PRECURSOR 2: L-Alanina [3 C] (Ciclo Glucosa-Alanina / Cahill)
    svg_parts.append(f"""
    <!-- PRECURSOR 2: L-ALANINA Y CICLO DE CAHILL -->
    <g transform="translate(1500, 2150)">
      <!-- Encabezado con Carbonos -->
      <g transform="translate(0, -18)">
        <rect x="0" y="0" width="42" height="18" rx="4" fill="#ea580c" opacity="0.14"/>
        <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#ea580c" stroke-width="1.4"/>
        <text x="21" y="13" fill="#ea580c" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
      </g>
      <text x="48" y="-4" fill="#ea580c" font-size="12" font-weight="900">PRECURSOR: L-ALANINA</text>
      <text x="0" y="14" fill="#b45309" font-size="10" font-weight="800">Ciclo Glucosa-Alanina / Cahill (Proteólisis Muscular)</text>
      <text x="0" y="26" fill="#64748b" font-size="9">Exporta nitrógeno al Ciclo de la Urea y esqueleto carbonado a Glucosa</text>

      <!-- Molécula de Alanina con estructura completa -->
      <g transform="translate(0, 36)">
        {AMINO_ALANINA}
      </g>

      <!-- Reacción de la Alanina Aminotransferasa (ALT) -->
      <g transform="translate(115, 56)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">L-Alanina [3 C]</text>
        <text x="0" y="16" fill="#ea580c" font-size="11" font-weight="800">ALT (Alanina Aminotransferasa / EC 2.6.1.2)</text>
        <text x="0" y="30" fill="#0284c7" font-size="10.5" font-weight="900">+ α-Cetoglutarato ➔ + L-Glutamato</text>
        <text x="0" y="44" fill="#4338ca" font-size="9.5" font-weight="700">Transferencia del grupo amino (⁺NH₃) hacia la Urea</text>
      </g>

      <!-- Flecha diagonal convergente hacia Piruvato citosólico -->
      <path d="M 20 145 Q -70 190 -170 225" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="-95" y="180" fill="#ea580c" font-size="10" font-weight="800">ALT ➔ Piruvato</text>
    </g>
    """)

    # -------------------------------------------------------------------------
    # CONVERGENCIA EN CITOSOL: Piruvato Citosólico [3 C] alineado en X=1280
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- METABOLITO: PIRUVATO CITOSÓLICO [3 C] (PUNTO DE CONVERGENCIA) -->
    <g transform="translate(1255, 2380)">
      {PIRUVATO}
      <g transform="translate(100, 24)">
        <g transform="translate(0, -18)">
          <rect x="0" y="0" width="42" height="18" rx="4" fill="#ea580c" opacity="0.14"/>
          <rect x="0" y="0" width="42" height="18" rx="4" fill="none" stroke="#ea580c" stroke-width="1.4"/>
          <text x="21" y="13" fill="#ea580c" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3 C</text>
        </g>
        <text x="0" y="14" fill="#0f172a" font-size="14" font-weight="900">Piruvato (Citosólico) [3 C]</text>
        <text x="0" y="28" fill="#0369a1" font-size="10" font-weight="800">Convergencia de Precursores (Lactato y Alanina)</text>
      </g>
    </g>

    <!-- Flecha descendente directa que cruza el transportador MPC en X=1280 -->
    <line x1="1280" y1="2470" x2="1280" y2="2735" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    """)

    # =========================================================================
    # MATRIZ MITOCONDRIAL: PIRUVATO, PC, OAA, mMDH, MALATO Y CATAPLEROSIS DE KREBS
    # =========================================================================

    # -------------------------------------------------------------------------
    # 12. Piruvato Mitocondrial [3 C] alineado en X=1255
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=1255, y=2760,
        nombre="Piruvato (Mitocondrial)",
        carbonos="3 C",
        formula="C₃H₃O₃⁻ (Sustrato de Carboxilación en Matriz)",
        svg_estructura=PIRUVATO,
        dx_texto=100,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 1: BYPASS 1A - Piruvato Carboxilasa (PC) en X=1280
    # Sustituye a la Piruvato Quinasa (PK) de la Glucólisis
    # Fijación de Carbono: + CO2 (3C + 1C -> 4C)
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- PASO 1: PIRUVATO CARBOXILASA (PC) -->
    <g transform="translate(1280, 2870)">
      <line x1="0" y1="0" x2="0" y2="130" stroke="#7c3aed" stroke-width="3" marker-end="url(#arrowPurple)"/>
      <path d="M -85 25 Q -30 25 -4 38" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-92" y="29" fill="#dc2626" font-size="11" font-weight="800" text-anchor="end">- 1 ATP</text>
      
      <path d="M -4 54 Q -30 68 -85 68" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-92" y="72" fill="#475569" font-size="11" font-weight="800" text-anchor="end">+ ADP + Pi</text>

      <path d="M -85 105 Q -30 105 -4 85" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="-92" y="109" fill="#0284c7" font-size="11" font-weight="900" text-anchor="end">+ HCO₃⁻ (Fijación de CO₂: 3 C + 1 C -> 4 C)</text>
      
      {badge_paso(1, -25, 65, es_bypass=True, etiqueta="PASO 1")}
      
      <g transform="translate(25, 18)">
        <text x="0" y="-8" fill="#6d28d9" font-size="12" font-weight="900">BYPASS 1A: Piruvato Carboxilasa (PC)</text>
        <text x="0" y="8" fill="#b91c1c" font-size="10" font-weight="800">Sustituye a: Piruvato Quinasa (PK) de la glucólisis</text>
        <text x="0" y="24" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">EC 6.4.1.1 (Requiere Biotina / Vitamina B₇)</text>
        <text x="0" y="40" fill="#16a34a" font-size="10.5" font-weight="800">(+) Acetil-CoA (Activador alostérico obligatorio)</text>
        <text x="0" y="55" fill="#dc2626" font-size="10.5" font-weight="800">(-) ADP (Baja carga energética frena PC)</text>
        <text x="0" y="70" fill="#78350f" font-size="9.5" font-weight="700">Conmutador: Acetil-CoA inhibe PDH y activa PC -> desvía piruvato a glucosa</text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # 13. Oxalacetato Mitocondrial (OAA Mitocondrial) [4 C]
    # Posicionado en X=1255, Y=3070 con dx_texto=100
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=1255, y=3070,
        nombre="Oxalacetato (OAA Mitocondrial)",
        carbonos="4 C",
        formula="C₄H₂O₅²⁻ (MMI carece de carrier directo para OAA)",
        svg_estructura=OXALACETATO,
        dx_texto=100,
        badge_color="#7c3aed"
    ))

    # -------------------------------------------------------------------------
    # OTROS PRECURSORES: CATAPLEROSIS DEL CICLO DE KREBS (AMINOÁCIDOS GLUCOGÉNICOS)
    # Distinguidos claramente de los que entran como Piruvato: alimentan intermediarios de Krebs
    # -------------------------------------------------------------------------
    svg_parts.append("""
    <!-- CATAPLEROSIS DEL CICLO DE KREBS: PRECURSORES QUE ALIMENTAN OAA MATRICIAL -->
    <g transform="translate(1420, 3180)">
      <text x="0" y="0" fill="#b45309" font-size="12.5" font-weight="900">
        PRECURSORES CATAPLERÓTICOS: CICLO DE KREBS (AMINOÁCIDOS)
      </text>
      <text x="0" y="16" fill="#92400e" font-size="10" font-weight="700">
        Precursores que NO pasan por Piruvato: entran como intermediarios de Krebs y forman Oxaloacetato [4 C]:
      </text>

      <g transform="translate(0, 30)">
        <text x="0" y="0" fill="#0f172a" font-size="10" font-weight="800">• α-Cetoglutarato [5 C]:</text>
        <text x="140" y="0" fill="#047857" font-size="9.5">Glutamato, Glutamina, Prolina, Histidina, Arginina</text>

        <text x="0" y="16" fill="#0f172a" font-size="10" font-weight="800">• Succinil-CoA [4 C]:</text>
        <text x="140" y="16" fill="#047857" font-size="9.5">Metionina, Valina, Isoleucina, Treonina, Propionil-CoA (grasas impares)</text>

        <text x="0" y="32" fill="#0f172a" font-size="10" font-weight="800">• Fumarato [4 C]:</text>
        <text x="140" y="32" fill="#047857" font-size="9.5">Fenilalanina, Tirosina, Aspartato</text>

        <text x="0" y="48" fill="#0f172a" font-size="10" font-weight="800">• Oxalacetato directo [4 C]:</text>
        <text x="140" y="48" fill="#047857" font-size="9.5">Aspartato, Asparagina (Transaminación directa por AST)</text>

        <text x="0" y="68" fill="#b91c1c" font-size="9.5" font-weight="800">
          Nota Bioquímica: Acetil-CoA (ácidos grasos pares) NO aporta carbonos netos
        </text>
        <text x="0" y="80" fill="#64748b" font-size="8.5">
          (Entran 2 C como Acetil-CoA y se liberan 2 C como CO₂ en Krebs; balance neto = 0).
        </text>
      </g>

      <!-- Flecha ascendente suave conectando al pool de Oxalacetato matricial -->
      <path d="M 0 10 Q -50 -30 -90 -60" fill="none" stroke="#b45309" stroke-width="2.2" stroke-dasharray="6 3" marker-end="url(#arrowAmber)"/>
      <text x="-65" y="-30" fill="#b45309" font-size="9.5" font-weight="800" text-anchor="middle">➔ Pool OAA [4 C]</text>
    </g>
    """)

    # -------------------------------------------------------------------------
    # PASO 2: mMDH (Malato Deshidrogenasa Mitocondrial)
    # Reduce OAA a Malato gastando 1 NADH matricial
    # Conecta Oxalacetato Mitocondrial (X=1255) con L-Malato Mitocondrial (X=220)
    # Flecha en Y=3270, termina en X=360 (despejada de Malato que está en X=220-310)
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- PASO 2: mMDH -->
    <g transform="translate(360, 3270)">
      <line x1="850" y1="0" x2="0" y2="0" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>
      {badge_paso(2, 820, 0, es_bypass=False, etiqueta="")}

      <g transform="translate(425, -12)">
        <text x="0" y="-12" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#6d28d9" text-anchor="middle">mMDH (MDH Mitocondrial)</text>
        <text x="0" y="2" font-family="'Inter', sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">Reduce OAA a Malato: única vía para exportar el esqueleto de 4C</text>
        <text x="0" y="22" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#dc2626" text-anchor="middle">+ NADH + H⁺ -> + NAD⁺ (Gasta 1 NADH matricial)</text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # 14. L-Malato Mitocondrial [4 C]
    # Posicionado en X=220, Y=3200 con fórmula en texto_izquierda
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=220, y=3200,
        nombre="L-Malato (Mitocondrial)",
        carbonos="4 C",
        formula="C₄H₄O₅²⁻ (Exportable por OGC)",
        svg_estructura=MALATO,
        texto_izquierda=True,
        badge_color="#047857"
    ))

    # -------------------------------------------------------------------------
    # ESTEQUIOMETRÍA Y BALANCE GLOBAL EN EL ENCABEZADO SUPERIOR DERECHO
    # -------------------------------------------------------------------------
    svg_parts.append("""
    <g transform="translate(1850, 30)">
      <text x="0" y="0" fill="#0f172a" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="end">
        BALANCE GLOBAL: 2 Piruvato (3 C) + 4 ATP + 2 GTP + 2 NADH + 6 H₂O -> D-Glucosa (6 C) + 4 ADP + 2 GDP + 6 Pi + 2 NAD⁺
      </text>
      <text x="0" y="16" fill="#dc2626" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">
        Inversión total de 6 enlaces de alta energía (~P) por cada molécula de glucosa sintetizada
      </text>
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
