# =============================================================================
# MÓDULO DE REVISIÓN: Entorno, Mitocondria y Componentes de Gluconeogénesis
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/via_02_gluconeogenesis/generar_gluconeogenesis.py (líneas 1 a 520 de 1263)
# Descripción      : Funciones de lienzo, mitocondria, retículo endoplásmico y tarjetas de reacción.
# =============================================================================

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

sys.path.append(os.path.join(DIR_BASE, "via_01_glucolisis"))
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.join(DIR_ROOT, "04_NITROGENO_Y_AMINOACIDOS", "via_13_transaminacion_y_desaminacion"))

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
    <!-- PASO 13: BYPASS 3 - G6Pasa en el RE (cisterna + bicapa + T1/T2/T3 + estructuras en el lumen) -->
    <g transform="translate(40, 195)">
      {RE_GLUCOSA_6_FOSFATASA}
      {badge_paso(13, 12, -48, es_bypass=True, etiqueta="PASO 13: BYPASS 3")}
    </g>

    <!-- Flechas citosol <-> RE (coordenadas absolutas) -->
    <path d="M 645 428 Q 590 505 502 521" fill="none" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowPurple)"/>
    <path d="M 502 281 Q 590 272 642 198" fill="none" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    <path d="M 502 220 L 548 220" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
    <circle cx="566" cy="220" r="12" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
    <text x="566" y="224" font-size="11" font-weight="900" fill="#c2410c" text-anchor="middle" font-family="'Inter', sans-serif">Pᵢ</text>
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
