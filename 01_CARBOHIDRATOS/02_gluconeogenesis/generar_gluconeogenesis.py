#!/usr/bin/env python3
"""
MAPA INDIVIDUAL DE LA GLUCONEOGÉNESIS (VÍA ANABÓLICA DE LA GLUCOSA)
===================================================================
Visualización Bioquímica Universitaria de Alta Precisión y Claridad Editorial.
- Compartimentación celular tripartita:
  1. Base: Matriz Mitocondrial con Piruvato Carboxilasa (PC), Biotina,
     Oxalacetato y la Lanzadera Mitocondrial de Malato (OGC).
  2. Centro: Citosol con PEPCK, fase reversa de triosas y FBPasa-1 (Bypass 2).
  3. Cima: Retículo Endoplásmico con el sistema Glucosa-6-Fosfatasa (Bypass 3),
     exportación de glucosa libre y cruce por GLUT-2 hacia la sangre.
- Sin globos artificiales en metabolitos.
- Balances energéticos rigurosos (-4 ATP, -2 GTP, -2 NADH).
- Entradas anapleróticas: Lactato (Cori), Alanina y Glicerol.
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
ALTO_CANVAS = 2650

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

        <!-- Gradientes -->
        <linearGradient id="gradCitosolGNG" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#ffffff" />
          <stop offset="10%" stop-color="#f8fafc" />
          <stop offset="60%" stop-color="#f0fdf4" stop-opacity="0.3" />
          <stop offset="85%" stop-color="#f8fafc" />
          <stop offset="100%" stop-color="#ffffff" />
        </linearGradient>

        <radialGradient id="gradMitoGNG" cx="50%" cy="100%" r="90%">
          <stop offset="0%" stop-color="#fef3c7" stop-opacity="1" />
          <stop offset="50%" stop-color="#fffbeb" stop-opacity="0.95" />
          <stop offset="85%" stop-color="#fed7aa" stop-opacity="0.9" />
          <stop offset="100%" stop-color="#f59e0b" stop-opacity="0.8" />
        </radialGradient>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def generar_entorno_gluconeogenesis(ancho, alto, y_mito=2100):
    """Genera la membrana plasmática arriba con GLUT-2, el RE y la mitocondria abajo."""
    return f"""
    <!-- Fondo Citoplasmático Acuoso -->
    <rect width="{ancho}" height="{alto}" fill="url(#gradCitosolGNG)"/>

    <!-- ============================================================= -->
    <!-- MEMBRANA PLASMÁTICA SUPERIOR (y = 0 a 110)                   -->
    <!-- ============================================================= -->
    <path d="M 0 0 L {ancho} 0 L {ancho} 65 Q {ancho*0.5} 75 0 65 Z" fill="#f1f5f9"/>
    <line x1="0" y1="65" x2="{ancho}" y2="65" stroke="#cbd5e1" stroke-width="2.5"/>
    <text x="{ancho/2}" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#475569" text-anchor="middle" letter-spacing="3">
      ESPACIO EXTRACELULAR • CAPILARES HEPÁTICOS • [GLUCEMIA AYUNO] ≈ 70-100 mg/dL
    </text>

    <!-- Bicapa Fosfolipídica Superior -->
    <rect x="0" y="65" width="{ancho}" height="24" fill="#e2e8f0" opacity="0.6"/>
    <rect x="0" y="77" width="{ancho}" height="22" fill="#f8fafc" opacity="0.9"/>
    <line x1="0" y1="110" x2="{ancho}" y2="110" stroke="#94a3b8" stroke-width="2" stroke-dasharray="8 4"/>

    <!-- Cabezas polares fosfolípidos -->
    <g fill="#0284c7" opacity="0.75">
      {' '.join([f'<circle cx="{i}" cy="{69 + (i%4)}" r="3"/><circle cx="{i}" cy="{81 + (i%4)}" r="3"/>' for i in range(25, ancho, 32)])}
    </g>

    <!-- Transportador GLUT-2 (Exportador hepático de Glucosa libre) -->
    <g transform="translate(640, 58)">
      <path d="M 0 5 C 10 -12, 26 -12, 32 5 C 36 18, 32 35, 23 40 C 12 43, 2 34, 0 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <path d="M 75 5 C 65 -12, 49 -12, 43 5 C 39 18, 43 35, 52 40 C 63 43, 73 34, 75 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <ellipse cx="37" cy="20" rx="10" ry="17" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8"/>
      <!-- Glucosa saliendo -->
      <polygon points="37,13 43,16 43,23 37,26 31,23 31,16" fill="#ffffff" stroke="#ea580c" stroke-width="1.8"/>
      <text x="37" y="50" fill="#0369a1" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-2</text>
    </g>

    <!-- Flecha de salida de glucosa hacia la sangre -->
    <line x1="677" y1="130" x2="677" y2="38" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
    <text x="730" y="85" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#c2410c">
      Exportación a Sangre (Km ≈ 15-20 mM)
    </text>

    <!-- ============================================================= -->
    <!-- COMPARTIMENTO MITOCONDRIAL INFERIOR                           -->
    <!-- ============================================================= -->
    <g id="mitocondria-gng" transform="translate(0, {y_mito})">
      <!-- Membrana Mitocondrial Externa Lisa (MME) -->
      <path d="M 0 50 C 350 15, 800 20, {ancho} 40 L {ancho} 550 L 0 550 Z" 
            fill="url(#gradMitoGNG)" stroke="#b45309" stroke-width="3.8"/>
      
      <!-- Espacio Intermembrana (EIM) -->
      <path d="M 0 68 C 350 33, 800 38, {ancho} 58" 
            fill="none" stroke="#78350f" stroke-width="2.2" stroke-dasharray="7 4"/>

      <!-- Crestas Mitocondriales Internas (MMI) -->
      <path d="M 60 140 C 140 80, 180 160, 270 110 C 330 160, 280 200, 150 190 Z" 
            fill="#fef3c7" stroke="#b45309" stroke-width="2.5" opacity="0.85"/>
      <path d="M 980 140 C 1080 80, 1140 160, 1240 110 C 1310 160, 1260 210, 1100 195 Z" 
            fill="#fef3c7" stroke="#b45309" stroke-width="2.5" opacity="0.85"/>

      <!-- Transportador MPC (Entrada de Piruvato) -->
      <g transform="translate(645, 24)">
        <rect x="0" y="0" width="65" height="30" rx="7" fill="#b45309" stroke="#78350f" stroke-width="2"/>
        <text x="32" y="20" fill="#ffffff" font-size="12" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MPC</text>
      </g>

      <!-- Rótulo de la matriz -->
      <text x="70" y="85" font-family="'Inter', sans-serif" font-size="16" font-weight="900" fill="#78350f" letter-spacing="1">
        MATRIZ MITOCONDRIAL (INICIO DEL BYPASS 1)
      </text>

      <!-- Transportador de Dicarboxilatos (Salida de Malato hacia el citosol) -->
      <g transform="translate(380, 24)">
        <rect x="0" y="0" width="75" height="30" rx="7" fill="#047857" stroke="#064e3b" stroke-width="2"/>
        <text x="37" y="20" fill="#ffffff" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">OGC / SLC25</text>
      </g>
      <text x="417" y="10" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#047857" text-anchor="middle">
        Lanzadera Malato/α-KG
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
    """Generador de reacción gluconeogénica ascendente (de abajo hacia arriba)."""
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
        # Flecha irreversible apuntando hacia arriba
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
    """Genera el documento completo de Gluconeogénesis."""
    svg_parts = []

    # 1. Capa de entorno celular
    svg_parts.append(generar_entorno_gluconeogenesis(ANCHO_CANVAS, ALTO_CANVAS, y_mito=2140))

    X_EJE = 620
    X_FLECHA = 675

    # =========================================================================
    # FASE 1: MITOCONDRIA Y BYPASS 1A (EN LA BASE)
    # =========================================================================
    # Piruvato mitocondrial
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=2220,
        nombre="Piruvato (Mitocondrial)",
        carbonos="3 Carbonos (α-Cetoácido)",
        detalle="Ingreso por MPC • Sustrato de carboxilación",
        svg_estructura=PIRUVATO,
        dx_texto=140
    ))

    # Entrada de Lactato (Ciclo de Cori) a la izquierda de Piruvato
    svg_parts.append(f"""
    <!-- Vía del Lactato (Ciclo de Cori) -->
    <g transform="translate(180, 2210)">
      {LACTATO}
      <g transform="translate(110, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="800">L-Lactato (Ciclo de Cori)</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700">Proveniente de músculo y eritrocitos</text>
      </g>
    </g>
    <!-- Flecha Lactato ➔ Piruvato con LDH -->
    <g transform="translate(420, 2245)">
      <line x1="0" y1="0" x2="160" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M 30 -12 Q 75 -22 120 -12" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="75" y="-26" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">+ NAD⁺</text>
      <path d="M 30 12 Q 75 22 120 12" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="75" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">+ NADH + H⁺</text>
      <text x="75" y="-5" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Lactato DH (LDH)</text>
    </g>
    """)

    # Reacción: Piruvato Carboxilasa (Bypass 1A)
    svg_parts.append("""
    <!-- Reacción: Piruvato Carboxilasa (PC) -->
    <g transform="translate(675, 2335)">
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
        x=X_EJE, y=2415,
        nombre="Oxalacetato (OAA Mitocondrial)",
        carbonos="4 Carbonos (Dicarboxilato α-Cetoácido)",
        detalle="No puede cruzar la MMI directamente",
        svg_estructura=OXALACETATO,
        dx_texto=140
    ))

    # Lanzadera de Malato (mMDH hacia la izquierda)
    svg_parts.append("""
    <!-- Reacción Malato Deshidrogenasa Mitocondrial (mMDH) -->
    <g transform="translate(580, 2465)">
      <line x1="0" y1="0" x2="-140" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M -25 -14 Q -70 -26 -115 -14" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-70" y="-28" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">+ NADH + H⁺ ➔ + NAD⁺</text>
      <g transform="translate(-70, 18)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">MDH Mitocondrial</text>
        <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#64748b" text-anchor="middle">EC 1.1.1.37 (Reducción)</text>
      </g>
    </g>
    """)

    # L-Malato mitocondrial (x = 330, y = 2415)
    svg_parts.append(crear_metabolito(
        x=330, y=2415,
        nombre="L-Malato",
        carbonos="4 Carbonos (Hidroxiácido)",
        detalle="Vehículo permeable para salir al citosol",
        svg_estructura=MALATO,
        texto_izquierda=True
    ))

    # Salida por transportador OGC hacia el citosol
    svg_parts.append("""
    <!-- Malato cruza la membrana mitocondrial hacia arriba -->
    <path d="M 370 2415 L 370 2050" fill="none" stroke="#047857" stroke-width="3" stroke-dasharray="8 4" marker-end="url(#arrowFlow)"/>
    <g transform="translate(290, 2120)">
      <text x="0" y="0" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#047857" text-anchor="end">
        Exportación Citosólica vía OGC
      </text>
      <text x="0" y="14" font-family="'Inter', sans-serif" font-size="10" fill="#64748b" text-anchor="end">
        Transporte equivalente de poder reductor
      </text>
    </g>
    """)

    # =========================================================================
    # FASE 2: CITOSOL Y BYPASS 1B (PEPCK)
    # =========================================================================
    # Malato citosólico en (330, 1940)
    svg_parts.append(crear_metabolito(
        x=330, y=1940,
        nombre="L-Malato (Citosólico)",
        carbonos="4 Carbonos",
        detalle="Reoxidado para liberar NADH y OAA",
        svg_estructura=MALATO,
        texto_izquierda=True
    ))

    # Reacción cMDH (Malato ➔ OAA citosólico)
    svg_parts.append("""
    <!-- Reacción MDH Citosólica (cMDH) -->
    <g transform="translate(440, 1990)">
      <line x1="0" y1="0" x2="140" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M 25 -14 Q 70 -26 115 -14" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="70" y="-28" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">+ NAD⁺ ➔ + NADH + H⁺</text>
      <g transform="translate(70, 18)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">MDH Citosólica</text>
        <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#64748b" text-anchor="middle">EC 1.1.1.37 (Regenera NADH para GAPDH)</text>
      </g>
    </g>
    """)

    # Oxalacetato citosólico en (X_EJE, 1940)
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=1940,
        nombre="Oxalacetato (OAA Citosólico)",
        carbonos="4 Carbonos",
        detalle="Substrato de descarboxilación y fosforilación",
        svg_estructura=OXALACETATO,
        dx_texto=140
    ))

    # Reacción: PEPCK (Bypass 1B)
    svg_parts.append("""
    <!-- Reacción PEPCK Citosólica -->
    <g transform="translate(675, 1845)">
      <line x1="0" y1="52" x2="0" y2="0" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M -85 38 Q -30 38 -4 26" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrowRed)"/>
      <text x="-92" y="42" fill="#dc2626" font-size="12" font-weight="800" text-anchor="end">- 1 GTP</text>
      <path d="M -4 20 Q -30 9 -85 9" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-92" y="13" fill="#475569" font-size="12" font-weight="800" text-anchor="end">+ GDP + CO₂</text>
      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="900">Fosfoenolpiruvato Carboxiquinasa (PEPCK-C)</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 4.1.1.32 (Mg²⁺, GTP)</text>
        <text x="0" y="32" fill="#b45309" font-size="11" font-weight="700">Descarboxilación impulsora exergónica</text>
      </g>
    </g>
    """)

    # =========================================================================
    # FASE 3: FASE REVERSA DE TRIOSAS (ASCENDENTE)
    # =========================================================================
    # PEP
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=1740,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 Carbonos (Enol-fosfato)",
        detalle="Inicio del flujo glucolítico reverso",
        svg_estructura=FOSFOENOLPIRUVATO,
        dx_texto=140
    ))

    # Reacción Reversa: Enolasa
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=1640,
        enzima="Enolasa",
        ec="EC 4.2.1.11 (⇄, + 2 H₂O)",
        salida_agua=True,
        reversible=True
    ))

    # 2-PG
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=1540,
        nombre="2-Fosfoglicerato",
        carbonos="3 Carbonos",
        detalle="Hidratación reversible de PEP",
        svg_estructura=FOSFOGLICERATO_2,
        dx_texto=140
    ))

    # Reacción Reversa: PGM
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=1440,
        enzima="Fosfoglicerato Mutasa",
        ec="EC 5.4.2.1 (⇄)",
        reversible=True
    ))

    # 3-PG
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=1340,
        nombre="3-Fosfoglicerato",
        carbonos="3 Carbonos",
        detalle="Substrato para fosforilación endergónica",
        svg_estructura=FOSFOGLICERATO_3,
        dx_texto=140
    ))

    # Reacción Reversa: Fosfoglicerato Quinasa
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=1240,
        enzima="Fosfoglicerato Quinasa",
        ec="EC 2.7.2.3 (⇄)",
        entra_energia="- 2 ATP",
        sale_energia="+ 2 ADP",
        reversible=True
    ))

    # 1,3-BPG
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=1140,
        nombre="1,3-Bisfosfoglicerato",
        carbonos="3 Carbonos (Acil-fosfato)",
        detalle="Substrato para reducción por NADH",
        svg_estructura=BISFOSFOGLICERATO_1_3,
        dx_texto=140
    ))

    # Reacción Reversa: GAPDH
    svg_parts.append("""
    <g transform="translate(675, 1040)">
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
        x=450, y=930,
        nombre="Dihidroxiacetona-Ⓟ",
        carbonos="3 Carbonos (Cetotriosa)",
        detalle="Aporte desde Glicerol lipolítico",
        svg_estructura=DIHIDROXIACETONA_FOSFATO,
        texto_izquierda=True
    ))

    svg_parts.append(crear_metabolito(
        x=760, y=930,
        nombre="Gliceraldehído-3-Ⓟ",
        carbonos="3 Carbonos (Aldotriosa)",
        detalle="Substrato de condensación aldólica",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO,
        dx_texto=140
    ))

    # TPI (Conexión reversible)
    svg_parts.append("""
    <g transform="translate(630, 965)">
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
    <g transform="translate(675, 830)">
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
        x=X_EJE, y=700,
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
    <g transform="translate(675, 595)">
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
        x=X_EJE, y=490,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Cetosa)",
        detalle="Substrato de isomerización a aldosa",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        dx_texto=140
    ))

    # Reacción Reversa: Fosfoglucosa Isomerasa
    svg_parts.append(crear_reaccion_ascendente(
        x=X_FLECHA, y=400,
        enzima="Fosfoglucosa Isomerasa",
        ec="EC 5.3.1.9 (⇄)",
        reversible=True
    ))

    # Glucosa-6-Fosfato
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=290,
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
    <g transform="translate(180, 230)">
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
    <path d="M 620 320 Q 420 320 360 280" fill="none" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arrowBlue)"/>
    <path d="M 360 250 Q 520 220 620 180" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
    """)

    # D-Glucosa Libre (Producto Final)
    svg_parts.append(crear_metabolito(
        x=X_EJE, y=140,
        nombre="D-Glucosa Libre",
        carbonos="6 Carbonos (Glucosa neutra exportable)",
        detalle="Sale de la célula hacia la circulación sanguínea vía GLUT-2",
        svg_estructura=GLUCOSA,
        dx_texto=140
    ))

    # =========================================================================
    # PANELES LATERALES DE RIGOR UNIVERSITARIO
    # =========================================================================
    svg_parts.append("""
    <!-- PANEL DE BALANCE ENERGÉTICO GLOBAL -->
    <g transform="translate(920, 1140)">
      <rect x="0" y="0" width="390" height="230" rx="12" fill="#ffffff" stroke="#ea580c" stroke-width="2.2" filter="drop-shadow(0 4px 10px rgba(0,0,0,0.06))"/>
      <text x="20" y="30" fill="#0f172a" font-size="15" font-weight="900">BALANCE ENERGÉTICO GLOBAL</text>
      <text x="20" y="52" fill="#c2410c" font-size="12" font-weight="800">Costo estequiométrico por 1 Glucosa:</text>
      <text x="20" y="78" fill="#dc2626" font-size="12.5" font-weight="700">• 2 Piruvato Carboxilasa ➔ - 2 ATP</text>
      <text x="20" y="98" fill="#dc2626" font-size="12.5" font-weight="700">• 2 PEPCK Citosólica ➔ - 2 GTP</text>
      <text x="20" y="118" fill="#dc2626" font-size="12.5" font-weight="700">• 2 Fosfoglicerato Quinasa ➔ - 2 ATP</text>
      <text x="20" y="138" fill="#059669" font-size="12.5" font-weight="700">• 2 GAPDH ➔ - 2 NADH + 2 H⁺</text>
      
      <line x1="20" y1="154" x2="370" y2="154" stroke="#e2e8f0" stroke-width="1.5"/>
      <text x="20" y="176" fill="#0f172a" font-size="12.5" font-weight="900">GASTO TOTAL: 6 Enlaces ~P</text>
      <text x="20" y="196" fill="#64748b" font-size="11">
        2 Piruvato + 4 ATP + 2 GTP + 2 NADH + 6 H₂O ➔ Glucosa + 4 ADP + 2 GDP + 6 Pi + 2 NAD⁺
      </text>
      <text x="20" y="214" fill="#047857" font-size="11" font-weight="700">ΔG'° ≈ -37.7 kJ/mol (Fisiológicamente Irreversible)</text>
    </g>

    <!-- PANEL DE PRECURSORES GLUCONEOGÉNICOS -->
    <g transform="translate(920, 1430)">
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

    ruta_salida = os.path.join(os.path.dirname(__file__), "Gluconeogenesis.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"✅ Mapa Individual de Gluconeogénesis generado con éxito en: {ruta_salida}")

if __name__ == "__main__":
    generar_mapa_gluconeogenesis()
