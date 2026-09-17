#!/usr/bin/env python3
"""
MAQUETA GLOBAL DEL MAPA METABÓLICO INTEGRADO (PROTOTIPO DE ARQUITECTURA)
========================================================================
Este prototipo resuelve las dos grandes dudas de escala y arquitectura:
1. GEOGRAFÍA MULTI-COMPARTIMENTAL: Citosol, Membrana Plasmática, Mitocondria,
   Espacio Intermembrana, Retículo y Sangre.
2. ESCALA Y TAMAÑO DE MOLÉCULAS: Las moléculas mantienen su tamaño editorial
   real (~80-100 px), y se incluye un VISOR INTERACTIVO con Pan & Zoom
   (rueda del ratón y arrastrar) para explorar la célula entera sin perder legibilidad.
"""

import os
import sys

# Importamos las estructuras de las rutas que ya tenemos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "01_CARBOHIDRATOS", "01_glucolisis")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "01_CARBOHIDRATOS", "04_via_pentosas_fosfato")))

from estructuras_glucosa import (
    GLUCOSA, GLUCOSA_6_FOSFATO, FRUCTOSA_6_FOSFATO, FRUCTOSA_1_6_BISFOSFATO,
    DIHIDROXIACETONA_FOSFATO, GLICERALDEHIDO_3_FOSFATO, BISFOSFOGLICERATO_1_3,
    FOSFOGLICERATO_3, FOSFOGLICERATO_2, FOSFOENOLPIRUVATO, PIRUVATO
)
from estructuras_pentosas import (
    RIBULOSA_5_FOSFATO, RIBOSA_5_FOSFATO, XILULOSA_5_FOSFATO
)

ANCHO_MAPA = 2600
ALTO_MAPA = 2400

PLANTILLA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Esquema Global Integrado - Mapa Metabólico Celular</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #0f172a;
      color: #f8fafc;
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    /* Barra de herramientas superior flotante */
    .topbar {{
      height: 55px;
      background: #1e293b;
      border-bottom: 1px solid #334155;
      padding: 0 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      z-index: 100;
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}

    .topbar h1 {{
      font-size: 16px;
      font-weight: 800;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .topbar-badge {{
      background: #ea580c;
      color: #fff;
      font-size: 10px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
      text-transform: uppercase;
    }}

    /* Controles de Zoom */
    .zoom-controls {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: #0f172a;
      padding: 4px 10px;
      border-radius: 8px;
      border: 1px solid #334155;
    }}

    .zoom-btn {{
      background: #334155;
      color: #f8fafc;
      border: none;
      width: 28px;
      height: 28px;
      border-radius: 5px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: background 0.15s;
    }}

    .zoom-btn:hover {{
      background: #ea580c;
    }}

    .zoom-label {{
      font-size: 12px;
      font-family: 'JetBrains Mono', monospace;
      color: #94a3b8;
      width: 55px;
      text-align: center;
    }}

    /* Contenedor del visor Pan & Zoom */
    #visor-viewport {{
      flex: 1;
      width: 100%;
      height: calc(100vh - 55px);
      overflow: hidden;
      cursor: grab;
      position: relative;
      background: radial-gradient(circle at center, #1e293b 0%, #0f172a 100%);
    }}

    #visor-viewport:active {{
      cursor: grabbing;
    }}

    #canvas-container {{
      transform-origin: 0 0;
      position: absolute;
      top: 0;
      left: 0;
      box-shadow: 0 25px 60px rgba(0,0,0,0.5);
      border-radius: 12px;
      background: #ffffff;
    }}

    /* Leyenda flotante de compartimentos */
    .compartimentos-legend {{
      position: absolute;
      bottom: 20px;
      left: 20px;
      background: rgba(15, 23, 42, 0.9);
      backdrop-filter: blur(8px);
      border: 1px solid #334155;
      padding: 12px 18px;
      border-radius: 10px;
      font-size: 12px;
      display: flex;
      gap: 15px;
      z-index: 90;
    }}

    .legend-item {{
      display: flex;
      align-items: center;
      gap: 7px;
    }}

    .legend-color {{
      width: 12px;
      height: 12px;
      border-radius: 3px;
    }}
  </style>
</head>
<body>

  <!-- Barra de control superior -->
  <header class="topbar">
    <h1>
      🔬 Plano Maestro Celular
      <span class="topbar-badge">Prototipo de Integración</span>
    </h1>
    
    <div class="zoom-controls">
      <button class="zoom-btn" onclick="zoomIn()" title="Acercar">+</button>
      <button class="zoom-btn" onclick="zoomOut()" title="Alejar">-</button>
      <button class="zoom-btn" onclick="resetZoom()" title="Ajustar al 100%">1:1</button>
      <button class="zoom-btn" onclick="fitView()" title="Ver Todo">⊡</button>
      <span class="zoom-label" id="zoom-indicator">100%</span>
    </div>
  </header>

  <!-- Visor interactivo -->
  <main id="visor-viewport">
    <div id="canvas-container">
      
      <!-- LIENZO SVG GIGANTE DE LA CÉLULA (2600 x 2400) -->
      <svg width="{ANCHO_MAPA}" height="{ALTO_MAPA}" viewBox="0 0 {ANCHO_MAPA} {ALTO_MAPA}" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
          </marker>
          <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
            <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
          </marker>
          <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
            <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
          </marker>
          <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
            <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
          </marker>
          <marker id="arrowPurple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
          </marker>

          <!-- Gradiente del Citosol Celular -->
          <linearGradient id="bgCitosol" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc" />
            <stop offset="20%" stop-color="#f0fdf4" stop-opacity="0.85" />
            <stop offset="70%" stop-color="#f8fafc" stop-opacity="0.6" />
            <stop offset="100%" stop-color="#f0fdf4" stop-opacity="0.9" />
          </linearGradient>

          <!-- Gradiente de la Matriz Mitocondrial -->
          <radialGradient id="bgMitocondria" cx="50%" cy="50%" r="60%">
            <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.95" />
            <stop offset="70%" stop-color="#fffbeb" stop-opacity="0.9" />
            <stop offset="100%" stop-color="#fef9c3" stop-opacity="0.8" />
          </radialGradient>
        </defs>

        <!-- ============================================================= -->
        <!-- 1. COMPARTIMENTO: MEDIO EXTRACELULAR (ARRIBA)                 -->
        <!-- ============================================================= -->
        <rect x="0" y="0" width="{ANCHO_MAPA}" height="90" fill="#e2e8f0" />
        <text x="50" y="45" fill="#475569" font-size="14" font-weight="900" letter-spacing="2">
          MEDIO EXTRACELULAR / TORRENTE SANGUÍNEO (Glucosa, Ácidos Grasos, Oxígeno)
        </text>

        <!-- Bicapa lipídica de la Membrana Plasmática -->
        <path d="M 0 90 Q 1300 120 {ANCHO_MAPA} 90" fill="none" stroke="#0284c7" stroke-width="10" stroke-linecap="round"/>
        <path d="M 0 100 Q 1300 130 {ANCHO_MAPA} 100" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>

        <!-- ============================================================= -->
        <!-- 2. COMPARTIMENTO: EL GRAN CITOSOL ACUOSO                      -->
        <!-- ============================================================= -->
        <rect x="0" y="100" width="{ANCHO_MAPA}" height="2300" fill="url(#bgCitosol)" />

        <!-- Citoesqueleto y filamentos atravesando el citoplasma -->
        <g opacity="0.25" stroke="#94a3b8" fill="none">
          <path d="M 50 250 Q 700 180 1400 280 T 2550 240" stroke-width="2.5" stroke-dasharray="10 8" />
          <path d="M 50 650 Q 800 750 1500 680 T 2550 720" stroke-width="2.2" stroke-dasharray="9 7" />
          <path d="M 50 1250 Q 900 1150 1600 1280 T 2550 1220" stroke-width="2.2" stroke-dasharray="10 8" />
        </g>

        <!-- ============================================================= -->
        <!-- 3. DELIMITACIÓN DE TERRITORIOS METABÓLICOS EN EL CITOSOL     -->
        <!-- ============================================================= -->

        <!-- TERRITORIO 1: METABOLISMO DE LÍPIDOS (Izquierda) -->
        <g transform="translate(100, 300)" opacity="0.8">
          <rect x="0" y="0" width="550" height="950" rx="16" fill="#fffbeb" stroke="#d97706" stroke-width="2" stroke-dasharray="8 6"/>
          <text x="30" y="45" fill="#b45309" font-size="16" font-weight="900">CITOSOL • METABOLISMO DE LÍPIDOS</text>
          <text x="30" y="70" fill="#78350f" font-size="12" font-weight="600">Síntesis de Ácidos Grasos • Lipogénesis • Glicerol-3-P</text>
          <circle cx="275" cy="500" r="120" fill="none" stroke="#d97706" stroke-width="1.5" stroke-dasharray="4 4"/>
          <text x="275" y="505" fill="#b45309" font-size="13" font-weight="800" text-anchor="middle">ÁCIDO GRASO SINTASA (FAS)</text>
        </g>

        <!-- TERRITORIO 2: EJE GLUCOLÍTICO (Centro-Izquierda) -->
        <g transform="translate(750, 150)">
          <!-- Rótulo de la Glucólisis -->
          <rect x="0" y="0" width="520" height="1900" rx="16" fill="#ffffff" stroke="#ea580c" stroke-width="1.5" opacity="0.4"/>
          <text x="30" y="-15" fill="#ea580c" font-size="16" font-weight="900" letter-spacing="1">EJE GLUCOLÍTICO (GLUCÓLISIS)</text>

          <!-- Transportador GLUT en la membrana -->
          <g transform="translate(140, -60)">
            <rect x="0" y="0" width="70" height="30" rx="8" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
            <text x="35" y="19" fill="#ffffff" font-size="11" font-weight="800" text-anchor="middle">GLUT-4</text>
            <line x1="35" y1="35" x2="35" y2="70" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
          </g>

          <!-- Glucosa (Inicio) -->
          <g transform="translate(100, 80)">
            <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
            <circle cx="16" cy="22" r="7" fill="#ffffff"/><text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>
            <text x="120" y="35" fill="#0f172a" font-size="18" font-weight="800">D-Glucosa (6C)</text>
          </g>

          <!-- Flecha HK -->
          <line x1="135" y1="160" x2="135" y2="210" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
          <text x="155" y="190" fill="#0f172a" font-size="12" font-weight="800">Hexoquinasa (-1 ATP)</text>

          <!-- Glucosa-6-P -->
          <g transform="translate(100, 230)">
            <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
            <circle cx="16" cy="22" r="7" fill="#ffffff"/><text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>
            <circle cx="0" cy="-2" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/><text x="0" y="3" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
            <text x="120" y="35" fill="#0f172a" font-size="18" font-weight="800">Glucosa-6-P (6C)</text>
            <text x="120" y="52" fill="#7c3aed" font-size="11" font-weight="700">⇄ ENCRUCIJADA METABÓLICA</text>
          </g>

          <!-- Flechas continuas que bajan hacia el piruvato -->
          <line x1="135" y1="310" x2="135" y2="400" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
          <text x="155" y="360" fill="#64748b" font-size="12">F6P → F-1,6-BP → Triosas (DHAP / GAP) ...</text>

          <!-- Piruvato al final -->
          <g transform="translate(100, 1720)">
            <text x="0" y="0" fill="#0f172a" font-size="18" font-weight="800">Piruvato (3C × 2)</text>
            <text x="0" y="20" fill="#ea580c" font-size="12" font-weight="700">Destino: Entrada a la Mitocondria</text>
          </g>

          <!-- Flecha cruzando hacia la mitocondria -->
          <line x1="135" y1="1760" x2="135" y2="1860" stroke="#ea580c" stroke-width="3.5" marker-end="url(#arrowFlow)"/>
        </g>

        <!-- CONEXIÓN REAL 1: BIFURCACIÓN HORIZONTAL HACIA PENTOSAS FOSFATO -->
        <g transform="translate(990, 395)">
          <path d="M 0 0 L 320 0" fill="none" stroke="#ea580c" stroke-width="3" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
          <text x="160" y="-12" fill="#c2410c" font-size="13" font-weight="900" text-anchor="middle">
            → ENTRADA AL SHUNT DE PENTOSAS FOSFATO
          </text>
        </g>

        <!-- TERRITORIO 3: VÍA DE LAS PENTOSAS FOSFATO (Centro-Derecha) -->
        <g transform="translate(1330, 250)">
          <rect x="0" y="0" width="560" height="1100" rx="16" fill="#f0fdf4" stroke="#059669" stroke-width="2"/>
          <text x="30" y="45" fill="#065f46" font-size="16" font-weight="900">CITOSOL • VÍA DE LAS PENTOSAS FOSFATO</text>
          <text x="30" y="70" fill="#047857" font-size="12" font-weight="600">Producción de NADPH • Síntesis de Nucleótidos (Ribosa-5-P)</text>

          <!-- Reacción G6PDH -->
          <g transform="translate(60, 120)">
            <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="800">1. Glucosa-6-P DH (G6PDH)</text>
            <text x="0" y="20" fill="#059669" font-size="12" font-weight="800">★ Generación de 2 NADPH (Poder reductor biosintético)</text>
            <text x="0" y="45" fill="#64748b" font-size="12">6-Fosfoglucono-δ-lactona → 6-Fosfogluconato</text>
          </g>

          <!-- Ribulosa-5-P y bifurcación -->
          <g transform="translate(60, 280)">
            <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">2. Ribulosa-5-Fosfato (5C)</text>
            <!-- Ribosa-5-P -->
            <g transform="translate(260, 60)">
              <rect x="0" y="0" width="200" height="70" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="2"/>
              <text x="100" y="28" fill="#6d28d9" font-size="13" font-weight="800" text-anchor="middle">D-Ribosa-5-P (5C)</text>
              <text x="100" y="48" fill="#7c3aed" font-size="11" font-weight="700" text-anchor="middle">→ Síntesis de ADN / ARN / ATP</text>
            </g>
          </g>

          <!-- Fase No Oxidativa: Retorno de F6P y GAP hacia la Glucólisis -->
          <g transform="translate(60, 520)">
            <rect x="0" y="0" width="460" height="90" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="230" y="28" fill="#0f172a" font-size="13" font-weight="800" text-anchor="middle">Fase No Oxidativa: Transcetolasa (TPP) + Transaldolasa</text>
            <text x="230" y="52" fill="#c2410c" font-size="12" font-weight="800" text-anchor="middle">3 Pentosas (5C) ⇄ 2 Fructosa-6-P (6C) + 1 GAP (3C)</text>
          </g>

          <!-- Flecha de reingreso hacia la Glucólisis -->
          <path d="M 60 565 L -60 565" fill="none" stroke="#ea580c" stroke-width="2.8" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
          <text x="-70" y="555" fill="#c2410c" font-size="11" font-weight="800" text-anchor="end">← Reingreso a F6P y GAP</text>
        </g>

        <!-- TERRITORIO 4: METABOLISMO DEL GLUCÓGENO (Derecha Alta) -->
        <g transform="translate(1930, 250)" opacity="0.8">
          <rect x="0" y="0" width="580" height="600" rx="16" fill="#fdf4ff" stroke="#c026d3" stroke-width="2" stroke-dasharray="8 6"/>
          <text x="30" y="45" fill="#a21caf" font-size="16" font-weight="900">CITOSOL • METABOLISMO DEL GLUCÓGENO</text>
          <text x="30" y="70" fill="#86198f" font-size="12" font-weight="600">Glucogenogénesis (Síntesis) • Glucogenólisis (Degradación)</text>
          <!-- Polímero de Glucógeno ramificado -->
          <circle cx="290" cy="320" r="100" fill="#fce7f3" stroke="#db2777" stroke-width="2"/>
          <text x="290" y="325" fill="#be185d" font-size="15" font-weight="900" text-anchor="middle">GLUCÓGENO (Polímero)</text>
        </g>


        <!-- ============================================================= -->
        <!-- 4. COMPARTIMENTO GIGANTE: LA MITOCONDRIA BIOLÓGICA REAL       -->
        <!-- ============================================================= -->
        <g transform="translate(0, 1750)">
          
          <!-- Membrana Mitocondrial Externa Lisa (Ámbar Oscuro) -->
          <path d="M 0 100 Q 1300 20 {ANCHO_MAPA} 100 L {ANCHO_MAPA} 650 L 0 650 Z" fill="#fef3c7" stroke="#b45309" stroke-width="5"/>
          
          <!-- Espacio Intermembrana (Gradiente electroquímico de protones H+) -->
          <path d="M 0 125 Q 1300 45 {ANCHO_MAPA} 125" fill="none" stroke="#78350f" stroke-width="3" stroke-dasharray="8 4"/>
          <text x="60" y="90" fill="#92400e" font-size="13" font-weight="900" letter-spacing="1">
            ESPACIO INTERMEMBRANA MITOCONDRIAL (Acumulación de H⁺ • Lanzaderas de Malato/Glicerol-P)
          </text>

          <!-- Membrana Mitocondrial Interna con CRESTAS ONDULADAS GIGANTES -->
          <g fill="none" stroke="#b45309" stroke-width="4" stroke-linecap="round">
            <!-- Crestas profundas -->
            <path d="M 100 250 C 250 150, 300 350, 480 200 C 600 350, 500 450, 250 400" />
            <path d="M 1800 220 C 2000 120, 2100 320, 2350 200 C 2450 320, 2350 420, 2000 380" />
          </g>

          <!-- Gran rótulo de la Matriz Mitocondrial -->
          <text x="1300" y="160" fill="#78350f" font-size="24" font-weight="900" text-anchor="middle" letter-spacing="3">
            MATRIZ MITOCONDRIAL
          </text>

          <!-- Transportador MPC donde entra el Piruvato -->
          <g transform="translate(855, 75)">
            <rect x="0" y="0" width="60" height="32" rx="8" fill="#b45309" stroke="#78350f" stroke-width="2"/>
            <text x="30" y="21" fill="#ffffff" font-size="11" font-weight="900" text-anchor="middle">MPC</text>
          </g>

          <!-- ZONA A: COMPLEJO PIRUVATO DESHIDROGENASA (PDH) -->
          <g transform="translate(730, 210)">
            <rect x="0" y="0" width="310" height="85" rx="12" fill="#ffffff" stroke="#b45309" stroke-width="2"/>
            <text x="155" y="28" fill="#78350f" font-size="13" font-weight="900" text-anchor="middle">COMPLEJO PIRUVATO DH (PDH)</text>
            <text x="155" y="48" fill="#ea580c" font-size="11" font-weight="800" text-anchor="middle">Piruvato (3C) → Acetil-CoA (2C) + CO₂</text>
            <text x="155" y="66" fill="#059669" font-size="11" font-weight="700" text-anchor="middle">+ 1 NADH (Poder reductor)</text>
            
            <!-- Flecha hacia el Ciclo de Krebs -->
            <path d="M 155 85 L 155 135" stroke="#b45309" stroke-width="3" marker-end="url(#arrowFlow)"/>
          </g>

          <!-- ZONA B: EL GRAN CICLO DE KREBS (ÁCIDO CÍTRICO) -->
          <g transform="translate(885, 470)">
            <circle cx="0" cy="0" r="110" fill="#fffbeb" stroke="#b45309" stroke-width="4"/>
            <text x="0" y="-20" fill="#78350f" font-size="16" font-weight="900" text-anchor="middle">CICLO DE KREBS</text>
            <text x="0" y="5" fill="#92400e" font-size="12" font-weight="700" text-anchor="middle">(Ciclo del Ácido Cítrico)</text>
            <text x="0" y="28" fill="#059669" font-size="11" font-weight="800" text-anchor="middle">Genera: 3 NADH + 1 FADH₂ + 1 GTP</text>
            <text x="0" y="48" fill="#dc2626" font-size="11" font-weight="700" text-anchor="middle">Libera: 2 CO₂</text>
          </g>

          <!-- ZONA C: CADENA DE TRANSPORTE DE ELECTRONES Y ATP SINTASA -->
          <g transform="translate(1400, 360)">
            <rect x="0" y="0" width="750" height="150" rx="14" fill="#ffffff" stroke="#0284c7" stroke-width="2.5"/>
            <text x="375" y="32" fill="#0369a1" font-size="14" font-weight="900" text-anchor="middle">
              FOSFORILACIÓN OXIDATIVA • CRESTAS MITOCONDRIALES
            </text>
            
            <!-- Complejos I, II, III, IV y Complejo V (ATP Sintasa) -->
            <g transform="translate(40, 55)">
              <rect x="0" y="0" width="80" height="50" rx="6" fill="#0284c7"/><text x="40" y="30" fill="#fff" font-size="11" font-weight="800" text-anchor="middle">Comp I</text>
              <rect x="110" y="0" width="80" height="50" rx="6" fill="#0284c7"/><text x="150" y="30" fill="#fff" font-size="11" font-weight="800" text-anchor="middle">Comp II</text>
              <rect x="220" y="0" width="80" height="50" rx="6" fill="#0284c7"/><text x="260" y="30" fill="#fff" font-size="11" font-weight="800" text-anchor="middle">Comp III</text>
              <rect x="330" y="0" width="80" height="50" rx="6" fill="#0284c7"/><text x="370" y="30" fill="#fff" font-size="11" font-weight="800" text-anchor="middle">Comp IV</text>
              <!-- ATP Sintasa destacada -->
              <rect x="470" y="-10" width="160" height="65" rx="8" fill="#ea580c"/><text x="550" y="25" fill="#fff" font-size="12" font-weight="900" text-anchor="middle">ATP SINTASA (F₀F₁)</text>
              <text x="550" y="42" fill="#ffedd5" font-size="10" font-weight="800" text-anchor="middle">ADP + Pi → ATP ★</text>
            </g>
          </g>

        </g>

      </svg>

    </div>
  </main>

  <!-- Leyenda flotante en pantalla -->
  <div class="compartimentos-legend">
    <div class="legend-item"><div class="legend-color" style="background:#e2e8f0; border:1px solid #94a3b8;"></div>Medio Extracelular</div>
    <div class="legend-item"><div class="legend-color" style="background:#0284c7;"></div>Membrana Plasmática</div>
    <div class="legend-item"><div class="legend-color" style="background:#f0fdf4; border:1px solid #86efac;"></div>Citosol</div>
    <div class="legend-item"><div class="legend-color" style="background:#fef3c7; border:1px solid #f59e0b;"></div>Mitocondria</div>
    <div class="legend-item"><div class="legend-color" style="background:#ea580c;"></div>Rutas de Carbohidratos</div>
    <div class="legend-item"><div class="legend-color" style="background:#7c3aed;"></div>Nucleótidos</div>
  </div>

  <!-- SCRIPT INTERACTIVO PAN & ZOOM -->
  <script>
    const viewport = document.getElementById('visor-viewport');
    const container = document.getElementById('canvas-container');
    const indicator = document.getElementById('zoom-indicator');

    let scale = 0.55; // Escala inicial para ver casi toda la célula
    let pointX = 50;
    let pointY = 20;
    let startX = 0;
    let startY = 0;
    let isPanning = false;

    function updateTransform() {{
      container.style.transform = `translate(${{pointX}}px, ${{pointY}}px) scale(${{scale}})`;
      indicator.textContent = Math.round(scale * 100) + '%';
    }}

    // Zoom con la rueda del ratón centrado en el cursor
    viewport.addEventListener('wheel', function(e) {{
      e.preventDefault();
      const xs = (e.clientX - pointX) / scale;
      const ys = (e.clientY - pointY) / scale;
      const delta = -e.deltaY;
      
      if (delta > 0) {{
        scale = Math.min(scale * 1.15, 3.5); // Máximo 350% zoom
      }} else {{
        scale = Math.max(scale / 1.15, 0.25); // Mínimo 25% zoom
      }}

      pointX = e.clientX - xs * scale;
      pointY = e.clientY - ys * scale;
      updateTransform();
    }});

    // Arrastrar (Pan) con clic sostenido
    viewport.addEventListener('mousedown', function(e) {{
      isPanning = true;
      startX = e.clientX - pointX;
      startY = e.clientY - pointY;
    }});

    window.addEventListener('mousemove', function(e) {{
      if (!isPanning) return;
      pointX = e.clientX - startX;
      pointY = e.clientY - startY;
      updateTransform();
    }});

    window.addEventListener('mouseup', function() {{
      isPanning = false;
    }});

    // Botones de zoom
    function zoomIn() {{
      scale = Math.min(scale * 1.25, 3.5);
      updateTransform();
    }}

    function zoomOut() {{
      scale = Math.max(scale / 1.25, 0.25);
      updateTransform();
    }}

    function resetZoom() {{
      scale = 1.0;
      pointX = (viewport.clientWidth - {ANCHO_MAPA} * scale) / 2;
      pointY = 30;
      updateTransform();
    }}

    function fitView() {{
      const scaleX = (viewport.clientWidth - 40) / {ANCHO_MAPA};
      const scaleY = (viewport.clientHeight - 40) / {ALTO_MAPA};
      scale = Math.min(scaleX, scaleY);
      pointX = (viewport.clientWidth - {ANCHO_MAPA} * scale) / 2;
      pointY = 20;
      updateTransform();
    }}

    // Iniciar con vista ajustada al tamaño de la pantalla
    fitView();
  </script>

</body>
</html>
"""

def main():
    ruta_salida = os.path.join(os.path.dirname(__file__), "mapa_celular_integrado.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(PLANTILLA_HTML)
    print(f"✅ ¡Maqueta global interactiva generada con éxito en: {ruta_salida}!")

if __name__ == "__main__":
    main()
