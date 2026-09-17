#!/usr/bin/env python3
"""
GENERADOR DEL CITOSOL METABÓLICO COMPLETO CON SISTEMA DE LUPA MOLECULAR
=======================================================================
Este script mapea y grafica el panorama integral del CITOSOL CELULAR:
- Delimitación cerrada de la célula (membrana plasmática bicapa lipídica)
- Límites de organelos asociados (mitocondria y retículo endoplásmico)
- TODAS las rutas que ocurren en el citosol y sus interconexiones nodales:
  1. Glucólisis completa
  2. Gluconeogénesis (reversión citosólica)
  3. Vía de las Pentosas Fosfato (Fase oxidativa y no oxidativa)
  4. Metabolismo del Glucógeno (Glucogénesis y Glucogenólisis)
  5. Biosíntesis de Ácidos Grasos y TAGs (Glicerol-3P, ACC, FAS)
  6. Destinos del Piruvato (Lactato/LDH, Alanina/ALT, MPC mitocondrial)
  7. Síntesis de Nucleótidos (PRPP -> Purinas / Pirimidinas)
  8. Ciclo de la Urea (Tramo citosólico: Citrulina -> Argininosuccinato -> Arginina -> Urea)
- Sistema interactivo dual:
  * Pan & Zoom libre (rueda del ratón y arrastre)
  * LUPA MOLECULAR interactiva (lente de aumento flotante 2.5x con HUD informativo)
  * Filtros de rutas para aislar visualmente cada proceso
"""

import os
import sys

# Importar estructuras existentes
DIR_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "01_glucolisis"))
sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "04_via_pentosas_fosfato"))

from estructuras_glucosa import (
    GLUCOSA, GLUCOSA_6_FOSFATO, FRUCTOSA_6_FOSFATO, FRUCTOSA_1_6_BISFOSFATO,
    DIHIDROXIACETONA_FOSFATO, GLICERALDEHIDO_3_FOSFATO, BISFOSFOGLICERATO_1_3,
    FOSFOGLICERATO_3, FOSFOGLICERATO_2, FOSFOENOLPIRUVATO, PIRUVATO
)
from estructuras_pentosas import (
    RIBULOSA_5_FOSFATO, RIBOSA_5_FOSFATO, XILULOSA_5_FOSFATO
)

ANCHO_CANVAS = 3200
ALTO_CANVAS = 2600

# Moléculas complementarias del Citosol (Glucógeno, G1P, Lactato, Alanina, etc.)
MOLECULAS_EXTRA = """
<!-- GLUCOSA-1-FOSFATO -->
<g id="mol-g1p">
  <rect x="-42" y="-38" width="84" height="76" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8" opacity="0.95"/>
  <polygon points="-24,-8 0,-20 24,-8 24,14 0,24 -24,14" fill="none" stroke="#f8fafc" stroke-width="2.2" stroke-linejoin="round"/>
  <line x1="24" y1="14" x2="33" y2="24" stroke="#f59e0b" stroke-width="2"/>
  <circle cx="37" cy="28" r="8" fill="#f59e0b"/>
  <text x="37" y="31" font-family="'Inter', sans-serif" font-size="8" font-weight="900" fill="#0f172a" text-anchor="middle">P</text>
  <text x="0" y="48" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#f1f5f9" text-anchor="middle">α-D-Glucosa-1-P</text>
</g>

<!-- UDP-GLUCOSA -->
<g id="mol-udp-glucosa">
  <rect x="-48" y="-38" width="96" height="76" rx="10" fill="#1e293b" stroke="#f59e0b" stroke-width="1.8" opacity="0.95"/>
  <polygon points="-28,-8 -8,-18 10,-8 10,12 -8,20 -28,12" fill="none" stroke="#f8fafc" stroke-width="2" stroke-linejoin="round"/>
  <rect x="18" y="-10" width="24" height="20" rx="4" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="30" y="4" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#ffffff" text-anchor="middle">UDP</text>
  <text x="0" y="48" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#f1f5f9" text-anchor="middle">UDP-Glucosa</text>
</g>

<!-- POLÍMERO DE GLUCÓGENO -->
<g id="mol-glucogeno">
  <circle cx="0" cy="0" r="44" fill="#1e293b" stroke="#eab308" stroke-width="2.5" stroke-dasharray="6,3" opacity="0.95"/>
  <!-- Ramificaciones esquemáticas -->
  <circle cx="0" cy="0" r="8" fill="#eab308"/>
  <circle cx="-18" cy="-14" r="6" fill="#ca8a04"/>
  <circle cx="18" cy="-14" r="6" fill="#ca8a04"/>
  <circle cx="-20" cy="16" r="6" fill="#ca8a04"/>
  <circle cx="20" cy="16" r="6" fill="#ca8a04"/>
  <circle cx="0" cy="-28" r="5" fill="#facc15"/>
  <circle cx="-30" cy="0" r="5" fill="#facc15"/>
  <circle cx="30" cy="0" r="5" fill="#facc15"/>
  <circle cx="0" cy="28" r="5" fill="#facc15"/>
  <line x1="0" y1="0" x2="-18" y2="-14" stroke="#eab308" stroke-width="2"/>
  <line x1="0" y1="0" x2="18" y2="-14" stroke="#eab308" stroke-width="2"/>
  <line x1="0" y1="0" x2="-20" y2="16" stroke="#eab308" stroke-width="2"/>
  <line x1="0" y1="0" x2="20" y2="16" stroke="#eab308" stroke-width="2"/>
  <text x="0" y="58" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#fde047" text-anchor="middle">GLUCÓGENO (n)</text>
  <text x="0" y="70" font-family="'Inter', sans-serif" font-size="7.5" fill="#94a3b8" text-anchor="middle">(Enlaces α-1,4 y α-1,6)</text>
</g>

<!-- L-LACTATO -->
<g id="mol-lactato">
  <rect x="-42" y="-35" width="84" height="70" rx="10" fill="#1e293b" stroke="#ec4899" stroke-width="1.8" opacity="0.95"/>
  <text x="0" y="-12" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#f43f5e" text-anchor="middle">COO⁻</text>
  <text x="0" y="3" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#f8fafc" text-anchor="middle">H — C — OH</text>
  <text x="0" y="18" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#f8fafc" text-anchor="middle">CH₃</text>
  <text x="0" y="46" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#f1f5f9" text-anchor="middle">L-Lactato</text>
</g>

<!-- L-ALANINA -->
<g id="mol-alanina">
  <rect x="-42" y="-35" width="84" height="70" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.8" opacity="0.95"/>
  <text x="0" y="-12" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#f43f5e" text-anchor="middle">COO⁻</text>
  <text x="0" y="3" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="600" fill="#38bdf8" text-anchor="middle">H₃N⁺— C — H</text>
  <text x="0" y="18" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#f8fafc" text-anchor="middle">CH₃</text>
  <text x="0" y="46" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#f1f5f9" text-anchor="middle">L-Alanina</text>
</g>

<!-- L-GLICEROL-3-FOSFATO -->
<g id="mol-glicerol-3p">
  <rect x="-44" y="-38" width="88" height="76" rx="10" fill="#1e293b" stroke="#06b6d4" stroke-width="1.8" opacity="0.95"/>
  <text x="0" y="-15" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#f8fafc" text-anchor="middle">CH₂OH</text>
  <text x="0" y="-1" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="600" fill="#f8fafc" text-anchor="middle">HO — C — H</text>
  <text x="0" y="13" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="600" fill="#f8fafc" text-anchor="middle">CH₂ — O — Ⓟ</text>
  <text x="0" y="48" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#f1f5f9" text-anchor="middle">Glicerol-3-P</text>
</g>

<!-- ACETIL-CoA CITOSÓLICO -->
<g id="mol-acetil-coa">
  <rect x="-45" y="-32" width="90" height="64" rx="10" fill="#1e293b" stroke="#eab308" stroke-width="1.8" opacity="0.95"/>
  <text x="0" y="-6" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#f8fafc" text-anchor="middle">CH₃ — C = O</text>
  <text x="0" y="10" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#eab308" text-anchor="middle">| S-CoA</text>
  <text x="0" y="42" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#f1f5f9" text-anchor="middle">Acetil-CoA (citosol)</text>
</g>

<!-- MALONIL-CoA -->
<g id="mol-malonil-coa">
  <rect x="-48" y="-35" width="96" height="70" rx="10" fill="#1e293b" stroke="#eab308" stroke-width="1.8" opacity="0.95"/>
  <text x="0" y="-10" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#f43f5e" text-anchor="middle">⁻OOC — CH₂</text>
  <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#f8fafc" text-anchor="middle">C = O</text>
  <text x="0" y="17" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#eab308" text-anchor="middle">| S-CoA</text>
  <text x="0" y="46" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#f1f5f9" text-anchor="middle">Malonil-CoA</text>
</g>

<!-- PALMITATO (ÁCIDO GRASO 16:0) -->
<g id="mol-palmitato">
  <rect x="-55" y="-32" width="110" height="64" rx="10" fill="#1e293b" stroke="#ca8a04" stroke-width="1.8" opacity="0.95"/>
  <text x="0" y="-4" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="700" fill="#f8fafc" text-anchor="middle">CH₃(CH₂)₁₄COO⁻</text>
  <text x="0" y="12" font-family="'Inter', sans-serif" font-size="7.5" fill="#fde047" text-anchor="middle">(Vía FAS / 14 NADPH)</text>
  <text x="0" y="42" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#f1f5f9" text-anchor="middle">Palmitato (16:0)</text>
</g>

<!-- PRPP (Fosforribosil pirofosfato) -->
<g id="mol-prpp">
  <rect x="-45" y="-36" width="90" height="72" rx="10" fill="#1e293b" stroke="#a855f7" stroke-width="1.8" opacity="0.95"/>
  <polygon points="-20,-5 0,-18 20,-5 12,14 -12,14" fill="none" stroke="#f8fafc" stroke-width="2"/>
  <circle cx="-25" cy="-8" r="6" fill="#a855f7"/>
  <text x="-25" y="-6" font-family="'Inter', sans-serif" font-size="6" font-weight="800" fill="#fff" text-anchor="middle">5-P</text>
  <circle cx="25" cy="-8" r="7" fill="#ec4899"/>
  <text x="25" y="-6" font-family="'Inter', sans-serif" font-size="6" font-weight="800" fill="#fff" text-anchor="middle">1-PP</text>
  <text x="0" y="46" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#f1f5f9" text-anchor="middle">PRPP (Nucleótidos)</text>
</g>

<!-- NUCLEÓTIDOS PURINAS Y PIRIMIDINAS -->
<g id="mol-nucleotidos-pool">
  <rect x="-55" y="-35" width="110" height="70" rx="10" fill="#1e293b" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4,2" opacity="0.95"/>
  <text x="0" y="-10" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800" fill="#c084fc" text-anchor="middle">IMP, AMP, GMP</text>
  <text x="0" y="5" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#f472b6" text-anchor="middle">UMP, CMP, TMP</text>
  <text x="0" y="18" font-family="'Inter', sans-serif" font-size="7.5" fill="#94a3b8" text-anchor="middle">ARN / ADN</text>
  <text x="0" y="46" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#e2e8f0" text-anchor="middle">Pool Nucleótidos</text>
</g>

<!-- CITRULINA CITOSÓLICA (Ciclo Urea) -->
<g id="mol-citrulina">
  <rect x="-45" y="-32" width="90" height="64" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.8" opacity="0.95"/>
  <text x="0" y="-6" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#34d399" text-anchor="middle">H₂N-CO-NH-(CH₂)₃</text>
  <text x="0" y="9" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#f8fafc" text-anchor="middle">CH(NH₃⁺)COO⁻</text>
  <text x="0" y="42" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#f1f5f9" text-anchor="middle">L-Citrulina</text>
</g>

<!-- ARGININOSUCCINATO -->
<g id="mol-argininosuccinato">
  <rect x="-55" y="-32" width="110" height="64" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.8" opacity="0.95"/>
  <text x="0" y="-4" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#6ee7b7" text-anchor="middle">Arginino-Succinato</text>
  <text x="0" y="11" font-family="'Inter', sans-serif" font-size="7.5" fill="#94a3b8" text-anchor="middle">(+ Aspartato / ATP)</text>
  <text x="0" y="42" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#f1f5f9" text-anchor="middle">Argininosuccinato</text>
</g>

<!-- L-ARGININA -->
<g id="mol-arginina">
  <rect x="-42" y="-32" width="84" height="64" rx="10" fill="#1e293b" stroke="#10b981" stroke-width="1.8" opacity="0.95"/>
  <text x="0" y="-4" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#34d399" text-anchor="middle">HN=C(NH₂)—NH...</text>
  <text x="0" y="11" font-family="'Inter', sans-serif" font-size="7.5" fill="#94a3b8" text-anchor="middle">(Guanidino)</text>
  <text x="0" y="42" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#f1f5f9" text-anchor="middle">L-Arginina</text>
</g>

<!-- UREA -->
<g id="mol-urea">
  <rect x="-38" y="-30" width="76" height="60" rx="10" fill="#1e293b" stroke="#3b82f6" stroke-width="2.2" opacity="0.95"/>
  <text x="0" y="-6" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#60a5fa" text-anchor="middle">H₂N — CO — NH₂</text>
  <text x="0" y="10" font-family="'Inter', sans-serif" font-size="7.5" font-weight="800" fill="#93c5fd" text-anchor="middle">(EXCRECIÓN)</text>
  <text x="0" y="40" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#f1f5f9" text-anchor="middle">UREA</text>
</g>
"""

def generar_html_citosol():
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>El Citosol Celular - Mapa Metabólico Integral y Lupa Molecular</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #090d16;
      color: #f8fafc;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      user-select: none;
    }}

    /* Barra Superior */
    .topbar {{
      height: 60px;
      background: #0f172a;
      border-bottom: 1px solid #1e293b;
      padding: 0 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      z-index: 100;
      box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }}

    .topbar-left {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .logo-badge {{
      background: linear-gradient(135deg, #ea580c, #f59e0b);
      color: white;
      font-size: 11px;
      font-weight: 900;
      letter-spacing: 0.5px;
      padding: 4px 10px;
      border-radius: 6px;
      text-transform: uppercase;
    }}

    .topbar-title {{
      font-size: 16px;
      font-weight: 800;
      letter-spacing: -0.3px;
      color: #f8fafc;
    }}

    .topbar-subtitle {{
      font-size: 11px;
      color: #94a3b8;
      font-weight: 500;
    }}

    /* Filtros y Herramientas */
    .toolbar {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .filter-btn {{
      background: #1e293b;
      border: 1px solid #334155;
      color: #cbd5e1;
      padding: 6px 12px;
      border-radius: 7px;
      font-size: 12px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}

    .filter-btn:hover {{
      background: #334155;
      color: #fff;
    }}

    .filter-btn.active {{
      background: #ea580c;
      border-color: #ea580c;
      color: #fff;
      font-weight: 700;
    }}

    /* Botón Lupa */
    .lens-toggle-btn {{
      background: linear-gradient(135deg, #3b82f6, #6366f1);
      border: none;
      color: #fff;
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 12px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 2px 10px rgba(59,130,246,0.3);
      transition: all 0.2s;
    }}

    .lens-toggle-btn:hover {{
      transform: translateY(-1px);
      box-shadow: 0 4px 15px rgba(59,130,246,0.5);
    }}

    .lens-toggle-btn.active {{
      background: linear-gradient(135deg, #10b981, #059669);
      box-shadow: 0 2px 12px rgba(16,185,129,0.4);
    }}

    /* Zoom Controls */
    .zoom-controls {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: #1e293b;
      padding: 4px 8px;
      border-radius: 8px;
      border: 1px solid #334155;
    }}

    .zoom-btn {{
      background: #0f172a;
      color: #f8fafc;
      border: 1px solid #334155;
      width: 28px;
      height: 28px;
      border-radius: 5px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .zoom-btn:hover {{ background: #ea580c; border-color: #ea580c; }}

    .zoom-text {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: #94a3b8;
      width: 48px;
      text-align: center;
    }}

    /* Lienzo Contenedor */
    #viewport-container {{
      flex: 1;
      position: relative;
      overflow: hidden;
      cursor: grab;
      background: radial-gradient(circle at 50% 50%, #0d1527 0%, #070a12 100%);
    }}

    #viewport-container:active {{
      cursor: grabbing;
    }}

    #canvas-wrapper {{
      position: absolute;
      transform-origin: 0 0;
      will-change: transform;
    }}

    svg {{
      display: block;
    }}

    /* HUD de la Lupa Flotante */
    #lens-element {{
      position: absolute;
      width: 280px;
      height: 280px;
      border-radius: 50%;
      border: 3px solid #38bdf8;
      box-shadow: 0 0 35px rgba(56,189,248,0.5), inset 0 0 20px rgba(0,0,0,0.6);
      pointer-events: none;
      overflow: hidden;
      display: none;
      z-index: 500;
      background: #090d16;
    }}

    #lens-element::after {{
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      border-radius: 50%;
      box-shadow: inset 0 0 15px rgba(56,189,248,0.4);
      pointer-events: none;
    }}

    #lens-svg-target {{
      position: absolute;
      transform-origin: 0 0;
    }}

    /* Tarjeta informativa flotante */
    .legend-card {{
      position: absolute;
      bottom: 24px;
      left: 24px;
      background: rgba(15, 23, 42, 0.92);
      backdrop-filter: blur(10px);
      border: 1px solid #334155;
      padding: 16px 20px;
      border-radius: 12px;
      font-size: 12px;
      z-index: 50;
      max-width: 340px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}

    .legend-card h3 {{
      font-size: 13px;
      font-weight: 800;
      margin-bottom: 8px;
      color: #f8fafc;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .legend-item {{
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 6px;
      color: #cbd5e1;
      font-size: 11.5px;
    }}

    .legend-dot {{
      width: 10px;
      height: 10px;
      border-radius: 50%;
      flex-shrink: 0;
    }}
  </style>
</head>
<body>

  <!-- Barra Superior -->
  <header class="topbar">
    <div class="topbar-left">
      <span class="logo-badge">Territorio Celular</span>
      <div>
        <div class="topbar-title">El Gran Citosol Metabólico</div>
        <div class="topbar-subtitle">Mapa de interconexiones citosólicas + Lupa de Inspección Molecular</div>
      </div>
    </div>

    <!-- Barra de Filtros y Lupa -->
    <div class="toolbar">
      <button class="filter-btn active" onclick="setFiltro('all')">Ver Todo</button>
      <button class="filter-btn" onclick="setFiltro('glucolisis')">Glucólisis & Gluconeo</button>
      <button class="filter-btn" onclick="setFiltro('glucogeno')">Glucógeno</button>
      <button class="filter-btn" onclick="setFiltro('pentosas')">Pentosas & Nucleótidos</button>
      <button class="filter-btn" onclick="setFiltro('lipidos')">Lípidos & TAGs</button>
      <button class="filter-btn" onclick="setFiltro('piruvato-urea')">Piruvato & Urea</button>

      <button id="btn-lens" class="lens-toggle-btn" onclick="toggleLens()">
        <span>🔍</span> <span id="btn-lens-text">Activar Lupa (2.5×)</span>
      </button>

      <div class="zoom-controls">
        <button class="zoom-btn" onclick="zoomRelativo(0.8)">−</button>
        <span id="zoom-text" class="zoom-text">65%</span>
        <button class="zoom-btn" onclick="zoomRelativo(1.25)">+</button>
        <button class="zoom-btn" style="width: auto; padding: 0 8px;" onclick="resetZoom()">Ajustar</button>
      </div>
    </div>
  </header>

  <!-- Viewport Pan & Zoom -->
  <main id="viewport-container">
    <div id="canvas-wrapper">
      <svg id="metabolic-svg" width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
        
        <defs>
          <!-- Degradados de Fondo Citosol -->
          <radialGradient id="grad-citosol-interior" cx="50%" cy="45%" r="65%">
            <stop offset="0%" stop-color="#0e172a" stop-opacity="0.95"/>
            <stop offset="60%" stop-color="#0a0f1d" stop-opacity="0.98"/>
            <stop offset="100%" stop-color="#060911" stop-opacity="1"/>
          </radialGradient>

          <!-- Marcadores de Flechas -->
          <marker id="arrow-carbo" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
            <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#f97316"/>
          </marker>
          <marker id="arrow-pentosa" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
            <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#a855f7"/>
          </marker>
          <marker id="arrow-lipido" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
            <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#eab308"/>
          </marker>
          <marker id="arrow-amino" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
            <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#10b981"/>
          </marker>
          <marker id="arrow-gluconeo" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
            <path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#38bdf8"/>
          </marker>

          <!-- ESTRUCTURAS GLUCÓLISIS -->
          {GLUCOSA}
          {GLUCOSA_6_FOSFATO}
          {FRUCTOSA_6_FOSFATO}
          {FRUCTOSA_1_6_BISFOSFATO}
          {DIHIDROXIACETONA_FOSFATO}
          {GLICERALDEHIDO_3_FOSFATO}
          {BISFOSFOGLICERATO_1_3}
          {FOSFOGLICERATO_3}
          {FOSFOGLICERATO_2}
          {FOSFOENOLPIRUVATO}
          {PIRUVATO}

          <!-- ESTRUCTURAS PENTOSAS -->
          {RIBULOSA_5_FOSFATO}
          {RIBOSA_5_FOSFATO}
          {XILULOSA_5_FOSFATO}

          <!-- ESTRUCTURAS NUEVAS DEL CITOSOL -->
          {MOLECULAS_EXTRA}
        </defs>

        <!-- ========================================================== -->
        <!-- 1. FORMA CERRADA DE LA CÉLULA (MEMBRANA PLASMÁTICA CERRADA) -->
        <!-- ========================================================== -->
        <!-- Espacio extracelular de fondo -->
        <rect width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" fill="#04060a"/>

        <!-- Borde celular continuo cerrado (Cápsula orgánica del citosol) -->
        <!-- Membrana plasmática bicapa: exterior #38bdf8, centro hidrofóbico #0369a1 -->
        <path d="M 280,180 
                 C 900,110 2300,110 2920,180 
                 C 3150,220 3150,2100 2950,2400 
                 C 2500,2550 700,2550 250,2400 
                 C 50,2100 50,220 280,180 Z" 
              fill="url(#grad-citosol-interior)" 
              stroke="#0369a1" 
              stroke-width="18" 
              opacity="0.95"/>

        <!-- Detalle de la bicapa externa (cabezas polares de fosfolípidos) -->
        <path d="M 280,180 
                 C 900,110 2300,110 2920,180 
                 C 3150,220 3150,2100 2950,2400 
                 C 2500,2550 700,2550 250,2400 
                 C 50,2100 50,220 280,180 Z" 
              fill="none" 
              stroke="#38bdf8" 
              stroke-width="3" 
              stroke-dasharray="8,6" 
              opacity="0.8"/>

        <!-- ========================================================== -->
        <!-- 2. LÍMITES BIOLÓGICOS DE ORGANELOS EN EL CITOSOL           -->
        <!-- ========================================================== -->
        <!-- A) Mitocondria en la esquina inferior derecha -->
        <g id="organelo-mitocondria">
          <path d="M 2100,1750 
                   C 2550,1700 2900,1950 2900,2380 
                   C 2600,2450 2150,2420 1900,2300 
                   C 1850,2000 1950,1800 2100,1750 Z" 
                fill="#141a29" stroke="#ea580c" stroke-width="6" opacity="0.9"/>
          <path d="M 2120,1770 
                   C 2530,1720 2870,1960 2870,2360 
                   C 2580,2430 2170,2400 1930,2280 
                   C 1880,2020 1980,1820 2120,1770 Z" 
                fill="#181324" stroke="#f59e0b" stroke-width="3" stroke-dasharray="10,5"/>
          
          <!-- Crestas esquemáticas -->
          <path d="M 2150,1820 Q 2300,1900 2200,2000 T 2350,2150" fill="none" stroke="#f59e0b" stroke-width="2.5" opacity="0.4"/>
          <path d="M 2450,1800 Q 2550,1950 2400,2080 T 2600,2250" fill="none" stroke="#f59e0b" stroke-width="2.5" opacity="0.4"/>
          <text x="2400" y="2100" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#f59e0b" opacity="0.6" letter-spacing="2">MATRIZ MITOCONDRIAL</text>
          <text x="2400" y="2120" font-family="'Inter', sans-serif" font-size="10" fill="#94a3b8" opacity="0.6">(PDH, Ciclo de Krebs, Cadena Respiratoria)</text>

          <!-- Transportador MPC (Piruvato) -->
          <rect x="1890" y="2090" width="22" height="42" rx="6" fill="#f97316" stroke="#fed7aa" stroke-width="2"/>
          <text x="1875" y="2115" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800" fill="#fed7aa" text-anchor="end">MPC</text>
        </g>

        <!-- B) Retículo Endoplásmico en la zona izquierda -->
        <g id="organelo-reticulo">
          <path d="M 220,1600 C 260,1500 320,1520 320,1650 C 320,1780 260,1800 300,1920 C 340,2050 280,2150 220,2100" 
                fill="none" stroke="#6366f1" stroke-width="8" opacity="0.35" stroke-linecap="round"/>
          <path d="M 250,1580 C 300,1480 370,1510 360,1640 C 350,1760 310,1820 350,1940" 
                fill="none" stroke="#818cf8" stroke-width="5" opacity="0.3" stroke-linecap="round"/>
          <text x="280" y="1760" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#818cf8" opacity="0.7" transform="rotate(-90 280 1760)">RETÍCULO ENDOPLÁSMICO (REL / RER)</text>
        </g>

        <!-- C) Transportadores de Membrana Plasmática -->
        <!-- GLUT-4 (Glucosa) arriba al centro -->
        <g id="transporte-glut" transform="translate(1300, 140)">
          <rect x="-35" y="-18" width="70" height="36" rx="8" fill="#ea580c" stroke="#fed7aa" stroke-width="2.5"/>
          <text x="0" y="5" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">GLUT-4</text>
          <!-- Flecha entrada de glucosa -->
          <line x1="0" y1="-30" x2="0" y2="40" stroke="#f97316" stroke-width="3" marker-end="url(#arrow-carbo)"/>
        </g>

        <!-- MCT1 (Lactato) izquierda -->
        <g id="transporte-mct" transform="translate(850, 150)">
          <rect x="-30" y="-16" width="60" height="32" rx="7" fill="#db2777" stroke="#fbcfe8" stroke-width="2"/>
          <text x="0" y="5" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">MCT-1</text>
        </g>


        <!-- ========================================================== -->
        <!-- 3. MAPEO INTEGRAL DE TODAS LAS RUTAS DEL CITOSOL           -->
        <!-- ========================================================== -->

        <!-- GRUPO 1: GLUCÓLISIS Y GLUCONEOGÉNESIS (EJE CENTRAL) -->
        <g id="grupo-glucolisis">
          <!-- Conexión Membrana -> Glucosa libre citosol -->
          <use href="#mol-glucosa" x="1300" y="240"/>

          <!-- 1. Hexoquinasa / Glucosa-6-Fosfatasa -->
          <path d="M 1285,285 L 1285,385" stroke="#f97316" stroke-width="2.5" marker-end="url(#arrow-carbo)"/>
          <text x="1275" y="335" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#fb923c" text-anchor="end">Hexoquinasa (ATP→ADP)</text>

          <path d="M 1315,385 L 1315,285" stroke="#38bdf8" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arrow-gluconeo)"/>
          <text x="1325" y="335" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">Glucosa-6-Fosfatasa (H₂O→Pi)</text>

          <!-- G6P (NODO CENTRAL UNIVERSAL) -->
          <use href="#mol-g6p" x="1300" y="440"/>

          <!-- 2. Fosfoglucosa Isomerasa -->
          <line x1="1300" y1="485" x2="1300" y2="575" stroke="#94a3b8" stroke-width="2.2"/>
          <line x1="1295" y1="570" x2="1300" y2="577" stroke="#94a3b8" stroke-width="2.2"/>
          <line x1="1305" y1="490" x2="1300" y2="483" stroke="#94a3b8" stroke-width="2.2"/>
          <text x="1310" y="530" font-family="'Inter', sans-serif" font-size="8.5" font-weight="600" fill="#cbd5e1">Fosfoglucosa Isomerasa</text>

          <!-- F6P -->
          <use href="#mol-f6p" x="1300" y="630"/>

          <!-- 3. PFK-1 vs FBPasa-1 -->
          <path d="M 1285,675 L 1285,765" stroke="#f97316" stroke-width="2.5" marker-end="url(#arrow-carbo)"/>
          <text x="1275" y="720" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#fb923c" text-anchor="end">PFK-1 (ATP→ADP)</text>

          <path d="M 1315,765 L 1315,675" stroke="#38bdf8" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arrow-gluconeo)"/>
          <text x="1325" y="720" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">FBPasa-1 (H₂O→Pi)</text>

          <!-- F1,6BP -->
          <use href="#mol-f16bp" x="1300" y="820"/>

          <!-- 4. Aldolasa (Bifurcación DHAP y GAP) -->
          <path d="M 1270,860 L 1050,935" stroke="#f97316" stroke-width="2" marker-end="url(#arrow-carbo)"/>
          <path d="M 1330,860 L 1450,935" stroke="#f97316" stroke-width="2" marker-end="url(#arrow-carbo)"/>
          <text x="1240" y="895" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#fdba74">Aldolasa</text>

          <!-- DHAP -->
          <use href="#mol-dhap" x="1020" y="980"/>
          <!-- GAP -->
          <use href="#mol-gap" x="1460" y="980"/>

          <!-- TPI Bidireccional -->
          <line x1="1080" y1="975" x2="1400" y2="975" stroke="#94a3b8" stroke-width="2"/>
          <line x1="1080" y1="985" x2="1400" y2="985" stroke="#94a3b8" stroke-width="2"/>
          <text x="1240" y="970" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#cbd5e1" text-anchor="middle">Triosa Fosfato Isomerasa (TPI)</text>

          <!-- Fase de Rendimiento (GAP hacia abajo) -->
          <!-- 5. GAPDH -->
          <path d="M 1460,1025 L 1460,1115" stroke="#f97316" stroke-width="2.2" marker-end="url(#arrow-carbo)"/>
          <text x="1475" y="1070" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#fdba74">GAPDH (NAD⁺ + Pi → NADH)</text>

          <!-- 1,3-BPG -->
          <use href="#mol-13bpg" x="1460" y="1170"/>

          <!-- 6. Fosfoglicerato Quinasa -->
          <path d="M 1460,1215 L 1460,1305" stroke="#f97316" stroke-width="2.2" marker-end="url(#arrow-carbo)"/>
          <text x="1475" y="1260" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#fdba74">PGK (ADP → ATP)</text>

          <!-- 3-PG -->
          <use href="#mol-3pg" x="1460" y="1360"/>

          <!-- 7. Mutasa -->
          <path d="M 1460,1405 L 1460,1495" stroke="#94a3b8" stroke-width="2.2"/>
          <text x="1475" y="1450" font-family="'Inter', sans-serif" font-size="8.5" font-weight="600" fill="#cbd5e1">Fosfogliceromutasa</text>

          <!-- 2-PG -->
          <use href="#mol-2pg" x="1460" y="1550"/>

          <!-- 8. Enolasa -->
          <path d="M 1460,1595 L 1460,1685" stroke="#f97316" stroke-width="2.2" marker-end="url(#arrow-carbo)"/>
          <text x="1475" y="1640" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#fdba74">Enolasa (— H₂O)</text>

          <!-- PEP -->
          <use href="#mol-pep" x="1460" y="1740"/>

          <!-- 9. Piruvato Quinasa vs PEPCK -->
          <path d="M 1445,1785 L 1445,1885" stroke="#f97316" stroke-width="2.5" marker-end="url(#arrow-carbo)"/>
          <text x="1435" y="1835" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#fb923c" text-anchor="end">Piruvato Quinasa (ADP→ATP)</text>

          <!-- Bypass de Gluconeogénesis: PEPCK Citosólica -->
          <path d="M 1475,1885 L 1475,1785" stroke="#38bdf8" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arrow-gluconeo)"/>
          <text x="1485" y="1835" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#38bdf8">PEPCK citosólica (GTP→GDP+CO₂)</text>

          <!-- PIRUVATO -->
          <use href="#mol-piruvato" x="1460" y="1940"/>
        </g>


        <!-- GRUPO 2: METABOLISMO DEL GLUCÓGENO (ZONA SUPERIOR IZQUIERDA) -->
        <g id="grupo-glucogeno">
          <!-- Conexión G6P <-> G1P -->
          <path d="M 1240,440 L 980,440" stroke="#f59e0b" stroke-width="2.2" marker-end="url(#arrow-lipido)"/>
          <text x="1110" y="430" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#fbbf24" text-anchor="middle">Fosfoglucomutasa</text>

          <!-- G1P -->
          <use href="#mol-g1p" x="930" y="440"/>

          <!-- G1P -> UDP-Glucosa -->
          <path d="M 885,440 L 735,440" stroke="#f59e0b" stroke-width="2.2" marker-end="url(#arrow-lipido)"/>
          <text x="810" y="430" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#fbbf24" text-anchor="middle">UDP-Glucosa Pirofosforilasa (UTP→PPi)</text>

          <!-- UDP-Glucosa -->
          <use href="#mol-udp-glucosa" x="680" y="440"/>

          <!-- UDP-Glucosa -> Glucógeno (Glucogenogénesis) -->
          <path d="M 630,440 L 530,440" stroke="#eab308" stroke-width="2.5" marker-end="url(#arrow-lipido)"/>
          <text x="580" y="430" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#fde047" text-anchor="middle">Glucógeno Sintasa</text>

          <!-- Retorno: Glucogenólisis (Glucógeno Fosforilasa -> G1P) -->
          <path d="M 490,475 C 650,530 850,520 920,480" stroke="#ca8a04" stroke-width="2" stroke-dasharray="5,3" fill="none" marker-end="url(#arrow-lipido)"/>
          <text x="700" y="525" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#fde047" text-anchor="middle">Glucógeno Fosforilasa (+ Pi)</text>

          <!-- Molécula de Glucógeno -->
          <use href="#mol-glucogeno" x="440" y="440"/>
        </g>


        <!-- GRUPO 3: VÍA DE LAS PENTOSAS FOSFATO Y NUCLEÓTIDOS (ZONA DERECHA) -->
        <g id="grupo-pentosas">
          <!-- Conexión G6P -> Pentosas -->
          <path d="M 1360,440 L 1750,440" stroke="#a855f7" stroke-width="2.5" marker-end="url(#arrow-pentosa)"/>
          <text x="1555" y="430" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#c084fc" text-anchor="middle">G6PDH (NADP⁺ → NADPH)</text>

          <!-- Ribulosa-5-P -->
          <use href="#mol-ribulosa-5p" x="1810" y="440"/>

          <!-- Epimerasa a Xilulosa-5-P -->
          <path d="M 1810,485 L 1810,615" stroke="#a855f7" stroke-width="2" marker-end="url(#arrow-pentosa)"/>
          <text x="1820" y="550" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#c084fc">Fosfopentosa Epimerasa</text>
          <use href="#mol-xilulosa-5p" x="1810" y="660"/>

          <!-- Isomerasa a Ribosa-5-P -->
          <path d="M 1860,440 L 2170,440" stroke="#a855f7" stroke-width="2.2" marker-end="url(#arrow-pentosa)"/>
          <text x="2015" y="430" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#c084fc" text-anchor="middle">Fosfopentosa Isomerasa</text>
          <use href="#mol-ribosa-5p" x="2220" y="440"/>

          <!-- Reciclaje Transcetolasa / Transaldolasa hacia F6P y GAP -->
          <path d="M 1750,680 C 1580,720 1420,680 1360,640" stroke="#a855f7" stroke-width="2" stroke-dasharray="4,2" fill="none" marker-end="url(#arrow-pentosa)"/>
          <text x="1570" y="705" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#e879f9" text-anchor="middle">Transcetolasa / Transaldolasa (Retorno a F6P y GAP)</text>

          <!-- SÍNTESIS DE NUCLEÓTIDOS (A partir de Ribosa-5-P) -->
          <path d="M 2220,490 L 2220,600" stroke="#8b5cf6" stroke-width="2.5" marker-end="url(#arrow-pentosa)"/>
          <text x="2230" y="545" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#a78bfa">PRPP Sintetasa (ATP→AMP)</text>

          <!-- PRPP -->
          <use href="#mol-prpp" x="2220" y="650"/>

          <!-- Ramificación a Nucleótidos -->
          <path d="M 2220,700 L 2220,810" stroke="#8b5cf6" stroke-width="2.2" marker-end="url(#arrow-pentosa)"/>
          <text x="2230" y="755" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#c4b5fd">Vía Purinas / Pirimidinas (de novo)</text>

          <!-- Pool Nucleótidos -->
          <use href="#mol-nucleotidos-pool" x="2220" y="860"/>
        </g>


        <!-- GRUPO 4: LÍPIDOS, GLICEROL Y TRIGLICÉRIDOS (ZONA MEDIA-BAJA IZQUIERDA) -->
        <g id="grupo-lipidos">
          <!-- Lanzadera Glicerol-3-P (desde DHAP) -->
          <path d="M 965,980 L 780,980" stroke="#06b6d4" stroke-width="2.2" marker-end="url(#arrow-gluconeo)"/>
          <text x="870" y="970" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#22d3ee" text-anchor="middle">Glicerol-3-P Deshidrogenasa (NADH→NAD⁺)</text>

          <!-- Glicerol-3-P -->
          <use href="#mol-glicerol-3p" x="720" y="980"/>

          <!-- Hacia Síntesis de Triacilgliceroles (TAGs) -->
          <path d="M 660,980 L 480,980" stroke="#0891b2" stroke-width="2.2" stroke-dasharray="5,2" marker-end="url(#arrow-gluconeo)"/>
          <text x="570" y="970" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#67e8f9" text-anchor="middle">Esterificación (+ 3 Acil-CoA)</text>
          
          <rect x="360" y="955" width="100" height="50" rx="8" fill="#164e63" stroke="#22d3ee" stroke-width="1.8"/>
          <text x="410" y="980" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#e0f2fe" text-anchor="middle">TRIGLICÉRIDOS</text>
          <text x="410" y="995" font-family="'Inter', sans-serif" font-size="7.5" fill="#a5f3fc" text-anchor="middle">(Reserva lipídica)</text>

          <!-- LIPOGÉNESIS DE NOVO (CITRATO MITOCONDRIAL -> ACETIL-CoA CITOSOL) -->
          <!-- Salida de citrato desde mitocondria a citosol -->
          <path d="M 2100,1850 C 1800,1650 1200,1450 960,1400" stroke="#eab308" stroke-width="2.5" stroke-dasharray="6,3" fill="none" marker-end="url(#arrow-lipido)"/>
          <text x="1450" y="1520" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#facc15" text-anchor="middle">Lanzadera de Citrato (Transportador Tricarboxilato)</text>

          <!-- Acetil-CoA Citosol -->
          <use href="#mol-acetil-coa" x="900" y="1400"/>

          <!-- Acetil-CoA Carboxilasa (ACC) -->
          <path d="M 845,1400 L 720,1400" stroke="#eab308" stroke-width="2.5" marker-end="url(#arrow-lipido)"/>
          <text x="780" y="1390" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#fde047" text-anchor="middle">ACC (Biotina / ATP + CO₂)</text>

          <!-- Malonil-CoA -->
          <use href="#mol-malonil-coa" x="660" y="1400"/>

          <!-- Complejo Ácido Graso Sintasa (FAS) -->
          <path d="M 605,1400 L 480,1400" stroke="#ca8a04" stroke-width="2.5" marker-end="url(#arrow-lipido)"/>
          <text x="540" y="1390" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#fef08a" text-anchor="middle">FAS (14 NADPH)</text>

          <!-- Palmitato -->
          <use href="#mol-palmitato" x="410" y="1400"/>
        </g>


        <!-- GRUPO 5: DESTINOS DEL PIRUVATO Y CICLO DE LA UREA (ZONA INFERIOR) -->
        <g id="grupo-piruvato-urea">
          <!-- A) Fermentación Láctica (LDH) hacia la izquierda -->
          <path d="M 1405,1940 L 1150,1940" stroke="#ec4899" stroke-width="2.5" marker-end="url(#arrow-carbo)"/>
          <text x="1280" y="1930" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#f472b6" text-anchor="middle">LDH (NADH + H⁺ ⇄ NAD⁺)</text>

          <!-- L-Lactato -->
          <use href="#mol-lactato" x="1100" y="1940"/>

          <!-- Lactato saliendo por MCT1 al exterior -->
          <path d="M 1100,1900 C 1050,1500 950,700 850,190" stroke="#db2777" stroke-width="2" stroke-dasharray="6,3" fill="none" marker-end="url(#arrow-carbo)"/>
          <text x="1010" y="1100" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#f472b6" transform="rotate(-85 1010 1100)">Lactato a la sangre (Ciclo de Cori)</text>

          <!-- B) Transaminación a Alanina (ALT) -->
          <path d="M 1460,1985 L 1460,2120" stroke="#10b981" stroke-width="2.2" marker-end="url(#arrow-amino)"/>
          <text x="1475" y="2050" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#34d399">ALT (Glutamato ⇄ α-KG)</text>

          <!-- Alanina -->
          <use href="#mol-alanina" x="1460" y="2170"/>

          <!-- C) Entrada de Piruvato a Mitocondria vía MPC -->
          <path d="M 1520,1950 C 1680,1980 1820,2050 1885,2105" stroke="#f97316" stroke-width="3" fill="none" marker-end="url(#arrow-carbo)"/>
          <text x="1710" y="2035" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#fb923c" text-anchor="middle">Entrada a Matriz (MPC)</text>

          <!-- D) CICLO DE LA UREA: SEGMENTO CITOSÓLICO -->
          <!-- Citrulina sale de mitocondria al citosol -->
          <path d="M 1950,2250 C 1900,2180 1820,2180 1780,2180" stroke="#10b981" stroke-width="2.2" stroke-dasharray="5,2" fill="none" marker-end="url(#arrow-amino)"/>
          <text x="1870" y="2170" font-family="'Inter', sans-serif" font-size="7.5" font-weight="700" fill="#6ee7b7" text-anchor="middle">Citrulina (sale de matriz)</text>

          <!-- Citrulina -->
          <use href="#mol-citrulina" x="1720" y="2180"/>

          <!-- Argininosuccinato Sintetasa (+ Aspartato / ATP) -->
          <path d="M 1720,2140 L 1720,2040" stroke="#10b981" stroke-width="2.2" marker-end="url(#arrow-amino)"/>
          <text x="1710" y="2090" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#34d399" text-anchor="end">ASS (+ Aspartato / ATP→AMP)</text>

          <!-- Argininosuccinato -->
          <use href="#mol-argininosuccinato" x="1720" y="1990"/>

          <!-- Argininosuccinato Liasa (Libera Fumarato) -->
          <path d="M 1780,1990 L 1890,1990" stroke="#10b981" stroke-width="2.2" marker-end="url(#arrow-amino)"/>
          <text x="1835" y="1980" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#34d399" text-anchor="middle">ASL (— Fumarato)</text>

          <!-- Arginina -->
          <use href="#mol-arginina" x="1950" y="1990"/>

          <!-- Arginasa (Genera Urea y Ornitina) -->
          <path d="M 1950,1950 L 1950,1850" stroke="#3b82f6" stroke-width="2.5" marker-end="url(#arrow-gluconeo)"/>
          <text x="1960" y="1900" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#60a5fa">Arginasa (H₂O)</text>

          <!-- UREA -->
          <use href="#mol-urea" x="1950" y="1800"/>

          <!-- Ornitina que reingresa a mitocondria -->
          <path d="M 2000,1990 C 2060,2020 2070,2150 2020,2250" stroke="#10b981" stroke-width="2" stroke-dasharray="5,2" fill="none" marker-end="url(#arrow-amino)"/>
          <text x="2070" y="2100" font-family="'Inter', sans-serif" font-size="7.5" font-weight="700" fill="#6ee7b7">Ornitina (reingreso matriz)</text>
        </g>

      </svg>
    </div>

    <!-- ELEMENTO DE LA LUPA MOLECULAR -->
    <div id="lens-element">
      <svg id="lens-svg-target" width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}">
        <use href="#metabolic-svg"/>
      </svg>
    </div>

    <!-- Tarjeta Informativa de Leyenda -->
    <div class="legend-card">
      <h3><span>🗺️</span> Territorio del Citosol Celular</h3>
      <div class="legend-item">
        <div class="legend-dot" style="background: #f97316;"></div>
        <div><strong>Carbohidratos</strong> (Glucólisis & Gluconeogénesis)</div>
      </div>
      <div class="legend-item">
        <div class="legend-dot" style="background: #eab308;"></div>
        <div><strong>Glucógeno</strong> (Glucogénesis & Glucogenólisis)</div>
      </div>
      <div class="legend-item">
        <div class="legend-dot" style="background: #a855f7;"></div>
        <div><strong>Pentosas Fosfato & Nucleótidos</strong> (NADPH / PRPP)</div>
      </div>
      <div class="legend-item">
        <div class="legend-dot" style="background: #06b6d4;"></div>
        <div><strong>Lípidos & TAGs</strong> (Glicerol-3P, ACC, FAS)</div>
      </div>
      <div class="legend-item">
        <div class="legend-dot" style="background: #10b981;"></div>
        <div><strong>Nitrógeno & Urea</strong> (Alanina, LDH, Ciclo Urea)</div>
      </div>
      <div style="margin-top: 8px; font-size: 10.5px; color: #94a3b8; border-top: 1px solid #334155; padding-top: 6px;">
        💡 <em>Usa la rueda para zoom o activa la <strong>Lupa Molecular</strong> para inspección rápida sin moverte.</em>
      </div>
    </div>
  </main>

  <script>
    // ESTADO DEL VISOR
    let scale = 0.65;
    let pointX = 0;
    let pointY = 0;
    let isDragging = false;
    let startX = 0, startY = 0;
    let lensActive = false;

    const container = document.getElementById('viewport-container');
    const wrapper = document.getElementById('canvas-wrapper');
    const zoomText = document.getElementById('zoom-text');
    const lens = document.getElementById('lens-element');
    const lensSvg = document.getElementById('lens-svg-target');
    const btnLens = document.getElementById('btn-lens');
    const btnLensText = document.getElementById('btn-lens-text');

    function updateTransform() {{
      wrapper.style.transform = `translate(${{pointX}}px, ${{pointY}}px) scale(${{scale}})`;
      zoomText.textContent = `${{Math.round(scale * 100)}}%`;
    }}

    // Centrar inicialmente
    function resetZoom() {{
      const rect = container.getBoundingClientRect();
      scale = Math.min(rect.width / {ANCHO_CANVAS}, rect.height / {ALTO_CANVAS}) * 1.15;
      pointX = (rect.width - {ANCHO_CANVAS} * scale) / 2;
      pointY = 20;
      updateTransform();
    }}
    window.addEventListener('load', resetZoom);
    window.addEventListener('resize', resetZoom);

    function zoomRelativo(factor) {{
      const rect = container.getBoundingClientRect();
      const cx = rect.width / 2;
      const cy = rect.height / 2;
      const newScale = Math.min(Math.max(0.2, scale * factor), 4.0);
      pointX = cx - (cx - pointX) * (newScale / scale);
      pointY = cy - (cy - pointY) * (newScale / scale);
      scale = newScale;
      updateTransform();
    }}

    // PAN (Arrastrar)
    container.addEventListener('mousedown', (e) => {{
      if (e.button !== 0) return;
      isDragging = true;
      startX = e.clientX - pointX;
      startY = e.clientY - pointY;
    }});

    window.addEventListener('mousemove', (e) => {{
      if (isDragging) {{
        pointX = e.clientX - startX;
        pointY = e.clientY - startY;
        updateTransform();
      }}

      // Manejo de la LUPA MOLECULAR
      if (lensActive) {{
        actualizarLupa(e);
      }}
    }});

    window.addEventListener('mouseup', () => {{
      isDragging = false;
    }});

    // ZOOM CON RUEDA DEL RATÓN
    container.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const rect = container.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      const delta = e.deltaY < 0 ? 1.15 : 0.87;
      const newScale = Math.min(Math.max(0.2, scale * delta), 4.0);

      pointX = mouseX - (mouseX - pointX) * (newScale / scale);
      pointY = mouseY - (mouseY - mouseY) * (newScale / scale);
      scale = newScale;
      updateTransform();

      if (lensActive) {{
        actualizarLupa(e);
      }}
    }}, {{ passive: false }});

    // LÓGICA DE LA LUPA MOLECULAR
    function toggleLens() {{
      lensActive = !lensActive;
      if (lensActive) {{
        lens.style.display = 'block';
        btnLens.classList.add('active');
        btnLensText.textContent = 'Desactivar Lupa';
      }} else {{
        lens.style.display = 'none';
        btnLens.classList.remove('active');
        btnLensText.textContent = 'Activar Lupa (2.5×)';
      }}
    }}

    function actualizarLupa(e) {{
      const rect = container.getBoundingClientRect();
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      // Posicionar el círculo de la lupa centrado en el puntero
      const lensRadius = 140;
      lens.style.left = `${{mouseX - lensRadius}}px`;
      lens.style.top = `${{mouseY - lensRadius}}px`;

      // Calcular coordenadas en el SVG original
      const svgX = (mouseX - pointX) / scale;
      const svgY = (mouseY - pointY) / scale;

      // Factor de aumento de la lupa
      const factorAumento = 2.4;
      const targetScale = scale * factorAumento;

      const targetX = lensRadius - svgX * targetScale;
      const targetY = lensRadius - svgY * targetScale;

      lensSvg.style.transform = `translate(${{targetX}}px, ${{targetY}}px) scale(${{targetScale}})`;
    }}

    // FILTRO DE RUTAS
    function setFiltro(ruta) {{
      document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');

      const grupos = [
        'grupo-glucolisis', 'grupo-glucogeno', 'grupo-pentosas', 
        'grupo-lipidos', 'grupo-piruvato-urea'
      ];

      grupos.forEach(id => {{
        const el = document.getElementById(id);
        if (!el) return;
        if (ruta === 'all') {{
          el.style.opacity = '1';
          el.style.filter = 'none';
        }} else if (
          (ruta === 'glucolisis' && id === 'grupo-glucolisis') ||
          (ruta === 'glucogeno' && id === 'grupo-glucogeno') ||
          (ruta === 'pentosas' && id === 'grupo-pentosas') ||
          (ruta === 'lipidos' && id === 'grupo-lipidos') ||
          (ruta === 'piruvato-urea' && id === 'grupo-piruvato-urea')
        ) {{
          el.style.opacity = '1';
          el.style.filter = 'none';
        }} else {{
          el.style.opacity = '0.15';
          el.style.filter = 'grayscale(80%)';
        }}
      }});
    }}
  </script>
</body>
</html>
"""
    return html_content

if __name__ == "__main__":
    ruta_salida = os.path.join(DIR_BASE, "PRUEBA_CITOSOL", "citosol_completo.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(generar_html_citosol())
    print(f"✅ Mapa integral del Citosol con Lupa generado en: {ruta_salida}")
