#!/usr/bin/env python3
"""
MAPA INTEGRADO DE CARBOHIDRATOS: GLUCOGÉNESIS • GLUCÓLISIS • PENTOSAS FOSFATO
=============================================================================
Versión Cartulina Limpia y Fiel a los Diseños Originales:
- Sin globos ni cajas artificiales envolviendo metabolitos o títulos.
- Eliminados los letreros de cabecera ("Síntesis de Glucógeno", "Eje Glucolítico", "Vía Pentosas").
- Conexiones horizontales segmentadas limpiamente:
  * Fosfoglucomutasa: segmento G6P ➔ Reacción con flechas ⇄ y textos ➔ segmento a G1P.
  * G6PDH: segmento G6P ➔ Reacción con flecha, cofactores (+NADP⁺/+NADPH) y texto ➔ segmento a Lactona.
- Zoom de Cebadores restaurado exactamente como en Glucogénesis:
  * Cebador Glucogenina-(Glc)₈ con textos libres a su derecha.
  * Líneas de proyección cónica punteadas hacia la Lente Circular de Zoom.
  * Caja explicativa de acoplamiento catalítico y elongación al lado de la lupa.
- Transcetolasa (TK1) con holgura vertical completa (>100px) debajo de la caja de Síntesis de Nucleótidos.
- Matriz mitocondrial biológica en la base, amplia y detallada con MPC, PDH y Ciclo de Krebs.
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

ANCHO_CANVAS = 3400
ALTO_CANVAS = 2600

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Metabolismo Integrado de Carbohidratos - Formato Cartulina / Póster</title>
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
      padding: 15px;
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
        <!-- Marcadores de flechas estandarizados -->
        <marker id="arrowFlow" markerWidth="7" markerHeight="7" refX="5.5" refY="3.5" orient="auto">
          <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#ea580c" />
        </marker>
        <marker id="arrowRed" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#dc2626" />
        </marker>
        <marker id="arrowSlate" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#475569" />
        </marker>
        <marker id="arrowGreen" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#059669" />
        </marker>
        <marker id="arrowBlue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#0284c7" />
        </marker>
        <marker id="arrowPurple" markerWidth="7" markerHeight="7" refX="5.5" refY="3.5" orient="auto">
          <path d="M 0 0 L 7 3.5 L 0 7 Z" fill="#7c3aed" />
        </marker>

        <!-- Gradientes celulares -->
        <linearGradient id="gradCitosolUnificado" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#ffffff" stop-opacity="1" />
          <stop offset="5%" stop-color="#f8fafc" stop-opacity="0.9" />
          <stop offset="50%" stop-color="#f0fdf4" stop-opacity="0.25" />
          <stop offset="85%" stop-color="#f8fafc" stop-opacity="0.9" />
          <stop offset="100%" stop-color="#ffffff" stop-opacity="1" />
        </linearGradient>

        <radialGradient id="gradMitocondria" cx="50%" cy="100%" r="90%">
          <stop offset="0%" stop-color="#fef3c7" stop-opacity="1" />
          <stop offset="45%" stop-color="#fffbeb" stop-opacity="0.95" />
          <stop offset="75%" stop-color="#fed7aa" stop-opacity="0.9" />
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

def generar_entorno_celular_continuo(ancho, alto):
    """Genera la membrana continua superior, citoesqueleto y vesículas."""
    return f"""
    <!-- Fondo Citoplasmático Acuoso -->
    <rect width="{ancho}" height="{alto}" fill="url(#gradCitosolUnificado)"/>

    <!-- ============================================================= -->
    <!-- MEMBRANA PLASMÁTICA CONTINUA (CRUZA TODO EL CITOSOL ARRIBA)   -->
    <!-- ============================================================= -->
    <!-- Espacio Extracelular / Sangre -->
    <path d="M 0 0 L {ancho} 0 L {ancho} 80 Q {ancho*0.5} 92 0 80 Z" fill="#f1f5f9"/>
    <line x1="0" y1="80" x2="{ancho}" y2="80" stroke="#cbd5e1" stroke-width="2.5"/>
    <text x="{ancho/2}" y="38" font-family="'Inter', sans-serif" font-size="15" font-weight="900" fill="#475569" text-anchor="middle" letter-spacing="3">
      ESPACIO EXTRACELULAR (TORRENTE SANGUÍNEO • LÍQUIDO INTERSTICIAL • [GLUCOSA] ≈ 5 mM)
    </text>

    <!-- Bicapa Fosfolipídica Continua (y = 80 a 140) -->
    <!-- Hoja Externa -->
    <rect x="0" y="80" width="{ancho}" height="28" fill="#e2e8f0" opacity="0.6"/>
    <!-- Colas Hidrofóbicas -->
    <rect x="0" y="94" width="{ancho}" height="26" fill="#f8fafc" opacity="0.9"/>
    <!-- Hoja Interna (Citosólica) -->
    <rect x="0" y="120" width="{ancho}" height="20" fill="#e2e8f0" opacity="0.6"/>
    <line x1="0" y1="140" x2="{ancho}" y2="140" stroke="#94a3b8" stroke-width="2" stroke-dasharray="8 4"/>

    <!-- Cabezas polares fosfolípidos vectoriales a lo largo de la membrana -->
    <g fill="#0284c7" opacity="0.75">
      {' '.join([f'<circle cx="{i}" cy="{84 + (i%4)}" r="3"/><circle cx="{i}" cy="{96 + (i%4)}" r="3"/>' for i in range(25, ancho, 30)])}
    </g>

    <!-- ============================================================= -->
    <!-- RECEPTOR GLUT-4 CON LUPA MOLECULAR (EN EL EJE GLUCOLÍTICO)    -->
    <!-- ============================================================= -->
    <g transform="translate(1540, 72)">
      <!-- Canal transmembrana GLUT-4 -->
      <path d="M 0 6 C 10 -14, 28 -14, 34 6 C 38 20, 34 38, 25 44 C 12 47, 2 37, 0 24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
      <path d="M 80 6 C 70 -14, 52 -14, 46 6 C 42 20, 46 38, 55 44 C 68 47, 78 37, 80 24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
      <ellipse cx="40" cy="22" rx="11" ry="19" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
      <!-- Molécula de Glucosa ingresando por el poro -->
      <polygon points="40,15 46,18 46,25 40,28 34,25 34,18" fill="#ffffff" stroke="#ea580c" stroke-width="1.8"/>
      <circle cx="34" cy="18" r="2.2" fill="#dc2626"/>
      <text x="40" y="52" fill="#0369a1" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-4</text>
    </g>

    <!-- Flujo de entrada de D-Glucosa a través de GLUT-4 -->
    <line x1="1580" y1="46" x2="1580" y2="72" stroke="#ea580c" stroke-width="2.5"/>
    <line x1="1580" y1="112" x2="1580" y2="150" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

    <!-- Lupa Molecular del GLUT-4 -->
    <g stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4 3" opacity="0.75">
      <line x1="1540" y1="92" x2="1395" y2="120" />
      <line x1="1550" y1="72" x2="1360" y2="70" />
    </g>
    <g transform="translate(1290, 115)">
      <circle cx="0" cy="0" r="74" fill="#ffffff" stroke="#0284c7" stroke-width="3.5" />
      <circle cx="0" cy="0" r="70" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2" />
      <!-- Bicapa ampliada en la lupa -->
      <g opacity="0.85">
        <g fill="#0284c7">
          <circle cx="-55" cy="-9" r="5.5"/><circle cx="-40" cy="-9" r="5.5"/><circle cx="-25" cy="-9" r="5.5"/>
          <circle cx="25" cy="-9" r="5.5"/><circle cx="40" cy="-9" r="5.5"/><circle cx="55" cy="-9" r="5.5"/>
        </g>
        <g stroke="#94a3b8" stroke-width="1.5" fill="none">
          <path d="M -55 -4 Q -57 2 -53 8"/><path d="M -40 -4 Q -42 2 -38 8"/><path d="M -25 -4 Q -27 2 -23 8"/>
          <path d="M 25 -4 Q 23 2 27 8"/><path d="M 40 -4 Q 38 2 42 8"/><path d="M 55 -4 Q 53 2 57 8"/>
          <path d="M -55 19 Q -57 13 -53 8"/><path d="M -40 19 Q -42 13 -38 8"/><path d="M -25 19 Q -27 13 -23 8"/>
          <path d="M 25 19 Q 23 13 27 8"/><path d="M 40 19 Q 38 13 42 8"/><path d="M 55 19 Q 53 13 57 8"/>
        </g>
        <g fill="#0284c7">
          <circle cx="-55" cy="24" r="5.5"/><circle cx="-40" cy="24" r="5.5"/><circle cx="-25" cy="24" r="5.5"/>
          <circle cx="25" cy="24" r="5.5"/><circle cx="40" cy="24" r="5.5"/><circle cx="55" cy="24" r="5.5"/>
        </g>
      </g>
      <!-- Hélices transmembrana -->
      <path d="M -20 -26 C -10 -30, -5 -18, -5 0 C -5 18, -10 30, -20 26 C -30 22, -28 -22, -20 -26 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <path d="M 20 -26 C 10 -30, 5 -18, 5 0 C 5 18, 10 30, 20 26 C 30 22, 28 -22, 20 -26 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <ellipse cx="0" cy="0" rx="7.5" ry="20" fill="#bae6fd" opacity="0.6"/>
      <!-- Molécula de glucosa en paso -->
      <g transform="translate(0, -6)">
        <polygon points="0,-11 10,-4 10,7 0,13 -10,7 -10,-4" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
        <circle cx="-10" cy="-4" r="3.2" fill="#ffffff"/>
        <text x="-10" y="-1" fill="#dc2626" font-size="6.5" font-weight="900" text-anchor="middle">O</text>
        <circle cx="15" cy="7" r="4.5" fill="#ffedd5" stroke="#ea580c" stroke-width="1.3"/>
        <text x="15" y="9.5" fill="#ea580c" font-size="5.5" font-weight="900" text-anchor="middle">OH</text>
      </g>
      <path d="M 0 -28 L 0 -17" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <path d="M 0 11 L 0 28" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <rect x="-60" y="48" width="120" height="17" rx="5" fill="#0f172a" opacity="0.9"/>
      <text x="0" y="60" fill="#ffffff" font-size="8.5" font-weight="800" text-anchor="middle" letter-spacing="0.5">DIFUSIÓN FACILITADA</text>
    </g>

    <!-- ============================================================= -->
    <!-- CITOESQUELETO CONTINUO Y ELEMENTOS CELULARES                  -->
    <!-- ============================================================= -->
    <g opacity="0.22" stroke="#94a3b8" fill="none">
      <path d="M 50 180 Q 800 240 1600 200 T 3350 230" stroke-width="2" stroke-dasharray="14 7"/>
      <path d="M 20 620 Q 900 680 1800 630 T 3380 670" stroke-width="1.8" stroke-dasharray="10 5"/>
      <path d="M 60 1200 Q 1000 1280 2000 1220 T 3340 1260" stroke-width="2" stroke-dasharray="16 8"/>
      <path d="M 40 1800 Q 850 1880 1750 1820 T 3360 1870" stroke-width="1.8" stroke-dasharray="12 6"/>
    </g>

    <!-- Vesículas citosólicas translúcidas -->
    <g opacity="0.35">
      <circle cx="220" cy="380" r="24" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
      <circle cx="1100" cy="480" r="26" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2"/>
      <circle cx="2180" cy="520" r="22" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
      <circle cx="3200" cy="680" r="28" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
    </g>
    """

def generar_mitocondria_biologica(x_inicio=1020, ancho_mito=2350, y_base=2220):
    """
    Genera la mitocondria biológica completa en la base, amplia y detallada
    con doble membrana, crestas invaginadas, MPC y acople con PDH y Krebs.
    """
    return f"""
    <!-- ================================================================= -->
    <!-- MITOCONDRIA BIOLÓGICA REAL (BASE AMPLIA Y PROFUNDA)               -->
    <!-- ================================================================= -->
    <g id="mitocondria-organelo" transform="translate({x_inicio}, {y_base})">
      <!-- Membrana Mitocondrial Externa Lisa (MME - Ámbar Cálido) -->
      <path d="M 0 55 C 350 10, 800 15, 1250 40 C 1700 65, 2050 20, {ancho_mito} 45 L {ancho_mito} 360 L 0 360 Z" 
            fill="url(#gradMitocondria)" stroke="#b45309" stroke-width="4"/>
      
      <!-- Espacio Intermembrana (EIM - Compartimento de acumulación de H⁺) -->
      <path d="M 0 72 C 350 27, 800 32, 1250 57 C 1700 82, 2050 37, {ancho_mito} 62" 
            fill="none" stroke="#78350f" stroke-width="2.5" stroke-dasharray="7 4"/>

      <!-- Crestas Mitocondriales Reales (Invaginaciones profundas de la MMI) -->
      <!-- Cresta Izquierda (Zona 1) -->
      <path d="M 80 140 C 160 80, 200 170, 300 110 C 370 170, 310 220, 160 200 Z" 
            fill="#fef3c7" stroke="#b45309" stroke-width="2.8" opacity="0.9"/>
      <!-- Cresta Central-Izquierda (Zona 2) -->
      <path d="M 380 160 C 450 110, 520 180, 600 130 C 670 180, 620 230, 480 210 Z" 
            fill="#fef3c7" stroke="#b45309" stroke-width="2.8" opacity="0.9"/>
      <!-- Cresta Central-Derecha (Zona 3) -->
      <path d="M 820 150 C 920 90, 980 170, 1080 120 C 1160 170, 1100 220, 950 205 Z" 
            fill="#fef3c7" stroke="#b45309" stroke-width="2.8" opacity="0.9"/>
      <!-- Cresta Derecha Grande (Zona 4) -->
      <path d="M 1400 140 C 1520 80, 1600 160, 1720 110 C 1820 160, 1760 220, 1550 200 Z" 
            fill="#fef3c7" stroke="#b45309" stroke-width="2.8" opacity="0.9"/>
      <!-- Cresta Extremo Derecho (Zona 5) -->
      <path d="M 1950 130 C 2050 80, 2120 160, 2220 110 C 2300 160, 2250 220, 2080 205 Z" 
            fill="#fef3c7" stroke="#b45309" stroke-width="2.8" opacity="0.9"/>

      <!-- Transportador MPC (Complejo Carrier de Piruvato) incrustado en la membrana -->
      <g transform="translate(530, 22)">
        <rect x="0" y="0" width="60" height="32" rx="8" fill="#b45309" stroke="#78350f" stroke-width="2.2"/>
        <text x="30" y="21" fill="#ffffff" font-size="13" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MPC</text>
      </g>

      <!-- Flecha vertical de translocación del Piruvato cruzando el MPC -->
      <line x1="560" y1="-8" x2="560" y2="70" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>

      <!-- Rótulo de Transportador MPC -->
      <g transform="translate(605, 38)">
        <text x="0" y="0" fill="#78350f" font-size="12" font-weight="900">Transportador Mitocondrial de Piruvato (MPC-1 / MPC-2)</text>
        <text x="0" y="14" fill="#92400e" font-size="10.5" font-weight="700">Simporte H⁺ / Piruvato a través de la Membrana Mitocondrial Interna</text>
      </g>

      <!-- Bloque Bioquímico: Complejo Piruvato Deshidrogenasa (PDH) -->
      <g transform="translate(560, 95)">
        <rect x="-210" y="0" width="420" height="74" rx="10" fill="#ffffff" stroke="#b45309" stroke-width="2.2" filter="drop-shadow(0 4px 8px rgba(0,0,0,0.08))"/>
        <text x="0" y="22" fill="#78350f" font-size="15" font-weight="900" text-anchor="middle">COMPLEJO PIRUVATO DESHIDROGENASA (PDH)</text>
        <text x="0" y="42" fill="#c2410c" font-size="12" font-weight="800" text-anchor="middle">Piruvato + CoA-SH + NAD⁺ ➔ Acetil-CoA + CO₂ + NADH + H⁺</text>
        <text x="0" y="59" fill="#64748b" font-size="11" text-anchor="middle">E1 (TPP) • E2 (Lipoamida) • E3 (FAD / NAD⁺) • EC 1.2.4.1 (Irreversible)</text>
      </g>

      <!-- Flecha desde PDH hacia Acetil-CoA / Krebs -->
      <line x1="560" y1="169" x2="560" y2="198" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Bloque: Ingreso al Ciclo de Krebs -->
      <g transform="translate(560, 202)">
        <rect x="-230" y="0" width="460" height="60" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
        <text x="0" y="24" fill="#92400e" font-size="15" font-weight="900" text-anchor="middle">ACETIL-CoA (2C) ➔ DESTINO: CICLO DE KREBS (TCA)</text>
        <text x="0" y="45" fill="#b45309" font-size="12" font-weight="700" text-anchor="middle">Condensación con Oxalacetato (4C) vía Citrato Sintasa ➔ Citrato (6C)</text>
      </g>

      <!-- Paneles Explicativos de la Matriz Mitocondrial a la derecha -->
      <g transform="translate(1320, 110)">
        <rect x="0" y="0" width="950" height="155" rx="12" fill="#ffffff" stroke="#d97706" stroke-width="2.2" opacity="0.95"/>
        <text x="25" y="32" fill="#78350f" font-size="18" font-weight="900">MATRIZ MITOCONDRIAL: HUB AERÓBICO DE OXIDACIÓN Y ENERGÍA</text>
        <text x="25" y="60" fill="#0f172a" font-size="13" font-weight="700">• Rendimiento Energético Total: Oxidación aeróbica completa de Glucosa ➔ 30 a 32 ATP.</text>
        <text x="25" y="82" fill="#c2410c" font-size="13" font-weight="700">• Cadena de Transporte de Electrones: Los NADH y FADH₂ alimentan los Complejos I-IV en la MMI.</text>
        <text x="25" y="104" fill="#047857" font-size="12.5" font-weight="700">• Destino Anaplerótico: El Piruvato también puede carboxilarse a Oxalacetato vía Piruvato Carboxilasa.</text>
        <text x="25" y="128" fill="#64748b" font-size="12">• Fosforilación Oxidativa: Gradiente electroquímico de protones en el EIM activa la ATP Sintasa (F₀F₁).</text>
      </g>
    </g>
    """

def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False, dx_texto=140):
    """
    Generador modular de metabolitos LIMPIO (SIN globos ni rectángulos artificiales).
    """
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

def crear_reaccion(x, y, enzima, ec="", regulacion="", entra_energia="", sale_energia="", 
                   reversible=False, es_ganancia=False, salida_agua=False, altura=50):
    """Generador de reacción vertical estándar."""
    curvas_energia = ""
    if entra_energia:
        color_entrada = "#dc2626" if not es_ganancia else "#475569"
        marcador_entrada = "url(#arrowRed)" if not es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -85 9 Q -30 9 -4 20" fill="none" stroke="{color_entrada}" stroke-width="2" marker-end="{marcador_entrada}"/>
        <text x="-92" y="13" fill="{color_entrada}" font-size="12" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
    if sale_energia:
        color_salida = "#059669" if es_ganancia else "#475569"
        marcador_salida = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -4 26 Q -30 37 -85 37" fill="none" stroke="{color_salida}" stroke-width="2" marker-end="{marcador_salida}"/>
        <text x="-92" y="41" fill="{color_salida}" font-size="12" font-weight="800" text-anchor="end">{sale_energia}</text>
        """
    if salida_agua:
        curvas_energia += """
        <path d="M -4 26 Q -30 37 -80 37" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
        <text x="-86" y="41" fill="#0284c7" font-size="12" font-weight="800" text-anchor="end">- 2 H₂O</text>
        """

    if reversible:
        flecha = f"""
        <line x1="-3.5" y1="0" x2="-3.5" y2="{altura}" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        <line x1="3.5" y1="{altura}" x2="3.5" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        """
    else:
        flecha = f"""
        <line x1="0" y1="0" x2="0" y2="{altura}" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="30" fill="{color_reg}" font-size="11" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
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

def crear_paso_no_oxidativo(x, y, enzima, ec, sustratos_txt, productos_txt):
    """Generador de nodo de transferencia no oxidativa."""
    return f"""
    <!-- Reacción de Transferencia: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="-3.5" y1="0" x2="-3.5" y2="48" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="3.5" y1="48" x2="3.5" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(22, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">{enzima}</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        <text x="0" y="32" fill="#c2410c" font-size="11.5" font-weight="700">{sustratos_txt} ⇄ {productos_txt}</text>
      </g>
    </g>
    """

def generar_mapa_carbohidratos():
    """Compila las tres rutas conectadas biológicamente en el citosol unificado."""
    svg_parts = []

    # 1. Capa de entorno celular continuo (Membrana arriba y citoesqueleto)
    svg_parts.append(generar_entorno_celular_continuo(ANCHO_CANVAS, ALTO_CANVAS))

    # 2. Mitocondria Biológica amplia en la base
    svg_parts.append(generar_mitocondria_biologica(x_inicio=1020, ancho_mito=2350, y_base=2220))

    # =========================================================================
    # RUTA CENTRAL: LA GLUCÓLISIS (EJE X = 1520 a 1580)
    # =========================================================================
    X_GLU = 1520
    X_FLECHA = 1580

    # 1. D-Glucosa
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=170,
        nombre="D-Glucosa",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Entrada directa desde el GLUT-4",
        svg_estructura=GLUCOSA,
        dx_texto=140
    ))

    # Reacción 1: Hexoquinasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=275,
        enzima="Hexoquinasa",
        ec="EC 2.7.1.1 (Mg²⁺)",
        regulacion="⊣ G-6-P | ⊕ Insulina",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 2. Glucosa-6-Fosfato (EL NODO CENTRAL DISTRIBUIDOR - LIMPIO, SIN GLOBO)
    svg_parts.append(f"""
    <!-- Nodo Central: Glucosa-6-Fosfato -->
    <g transform="translate({X_GLU}, 375)">
      {GLUCOSA_6_FOSFATO}
    </g>
    <g transform="translate({X_FLECHA}, 465)">
      <text x="0" y="0" fill="#0f172a" font-size="17" font-weight="800" text-anchor="middle">Glucosa-6-Fosfato (G-6-P)</text>
      <text x="0" y="18" fill="#ea580c" font-size="12.5" font-weight="700" text-anchor="middle">6 Carbonos (Hexosa Ⓟ)</text>
    </g>
    """)

    # =========================================================================
    # CONEXIÓN HORIZONTAL SEGMENTADA: G-6-P ⇄ FOSFOGLUCOMUTASA ⇄ G-1-P
    # =========================================================================
    # Segmento 1: desde G-6-P (x=1470) hasta Fosfoglucomutasa (x=1070)
    # Enzima: Fosfoglucomutasa en x=1000 con sus flechas ⇄ sin ser atravesada por líneas
    # Segmento 2: desde Fosfoglucomutasa (x=930) hasta Haworth de G1P (x=675)
    svg_parts.append("""
    <!-- Conexión horizontal hacia la Glucogénesis (Segmento 1) -->
    <line x1="1470" y1="410" x2="1080" y2="410" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

    <!-- Reacción Fosfoglucomutasa (Totalmente despejada) -->
    <g transform="translate(1000, 410)">
      <line x1="-35" y1="-3" x2="35" y2="-3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="35" y1="3" x2="-35" y2="3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(0, -12)">
        <text x="0" y="-12" font-family="'Inter', sans-serif" font-size="14.5" font-weight="800" fill="#0f172a" text-anchor="middle">Fosfoglucomutasa</text>
        <text x="0" y="2" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748b" text-anchor="middle">EC 5.4.2.2 (⇄)</text>
        <text x="0" y="-25" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#d97706" text-anchor="middle">Interm. Glucosa-1,6-BP</text>
      </g>
    </g>

    <!-- Conexión horizontal hacia G-1-P (Segmento 2) -->
    <line x1="920" y1="410" x2="680" y2="410" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
    """)

    # =========================================================================
    # RUTA LATERAL IZQUIERDA: GLUCOGÉNESIS
    # =========================================================================
    # 2. α-D-Glucosa-1-Fosfato (G-1-P)
    # Estructura en x=530, texto a la izquierda sin globos
    svg_parts.append(crear_metabolito(
        x=530, y=375,
        nombre="α-D-Glucosa-1-Fosfato",
        carbonos="6 Carbonos (Fosfato en C1-α)",
        detalle="Sustrato de activación por UTP",
        svg_estructura=GLUCOSA_1_FOSFATO,
        texto_izquierda=True
    ))

    # Reacción 2: UDP-Glucosa Pirofosforilasa
    svg_parts.append("""
    <g transform="translate(520, 505)">
      <line x1="0" y1="0" x2="0" y2="52" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M -90 10 Q -35 10 -4 22" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-98" y="14" fill="#475569" font-size="12" font-weight="800" text-anchor="end">+ UTP</text>
      <path d="M -4 30 Q -35 42 -90 42" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-98" y="46" fill="#059669" font-size="12" font-weight="800" text-anchor="end">+ PPi ➔ 2 Pi (Pirofosfatasa)</text>
      <g transform="translate(22, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">UDP-Glucosa Pirofosforilasa</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 2.7.7.9 (Impulso por PPi)</text>
        <text x="0" y="32" fill="#059669" font-size="11" font-weight="700">ΔG'° ≈ -19.2 kJ/mol (Irreversible)</text>
      </g>
    </g>
    """)

    # 3. UDP-Glucosa (Uridina Difosfato Glucosa)
    svg_parts.append(crear_metabolito(
        x=280, y=605,
        nombre="UDP-Glucosa",
        carbonos="Nucleótido-Azúcar activado",
        detalle="Donador de glucosa de alta energía",
        svg_estructura=UDP_GLUCOSA,
        dx_texto=290
    ))

    # =========================================================================
    # 4. CEBADOR MOLECULAR DE GLUCOGENINA + LUPA MOLECULAR (DISEÑO ORIGINAL)
    # =========================================================================
    Y_CEBADOR = 770
    svg_parts.append(f"""
    <!-- CEBADOR MOLECULAR DE GLUCOGENINA (LIBRE, SIN GLOBO) -->
    <g transform="translate(140, {Y_CEBADOR})">
      {CEBADOR_GLUCOGENINA}
      
      <!-- Textos del cebador a la derecha -->
      <g transform="translate(370, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="900">Cebador: Glucogenina-(Glc)₈</text>
        <text x="0" y="18" fill="#b45309" font-size="11.5" font-weight="700">Dímero autoglucosilante (EC 2.4.1.186)</text>
        <text x="0" y="34" fill="#64748b" font-size="10.5">• Anclaje covalente en residuo Tyr-194</text>
        <text x="0" y="48" fill="#dc2626" font-size="10.5" font-weight="800">• Extremo 4-OH libre: Sustrato aceptor</text>
        <text x="0" y="63" fill="#64748b" font-size="10">Requerido: Glucógeno Sintasa no inicia de novo</text>
      </g>
    </g>

    <!-- LÍNEAS DE PROYECCIÓN CÓNICA HACIA LA LUPA DE ZOOM MOLECULAR -->
    <g stroke="#ea580c" stroke-width="1.4" stroke-dasharray="4 3" opacity="0.65">
      <line x1="435" y1="{Y_CEBADOR + 35}" x2="255" y2="{Y_CEBADOR + 180}"/>
      <line x1="435" y1="{Y_CEBADOR + 15}" x2="160" y2="{Y_CEBADOR + 140}"/>
    </g>

    <!-- LUPA DE ZOOM MOLECULAR: ACOPLAMIENTO CATALÍTICO CEBADOR + SINTASA -->
    <g transform="translate(180, {Y_CEBADOR + 210})">
      {LUPA_MECANISMO_CEBADOR}
    </g>

    <!-- EXPLICACIÓN BIOQUÍMICA A LA DERECHA DE LA LUPA -->
    <g transform="translate(340, {Y_CEBADOR + 175})">
      <rect x="0" y="0" width="460" height="95" rx="8" fill="#f8fafc" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="16" y="22" fill="#1d4ed8" font-size="12" font-weight="900">MECANISMO DE ACOPLAMIENTO Y ELONGACIÓN</text>
      <text x="16" y="40" fill="#0f172a" font-size="10.5" font-weight="600">
        1. La <tspan font-weight="800" fill="#2563eb">Glucógeno Sintasa</tspan> abraza el extremo <tspan font-weight="800" fill="#dc2626">4-OH</tspan> de la cadena cebadora.
      </text>
      <text x="16" y="58" fill="#0f172a" font-size="10.5" font-weight="600">
        2. El oxígeno ataca al <tspan font-weight="800" fill="#ea580c">C1</tspan> de la <tspan font-weight="800">UDP-Glucosa</tspan>, expulsando al grupo UDP.
      </text>
      <text x="16" y="76" fill="#059669" font-size="10.5" font-weight="800">
        3. Se forma el nuevo enlace α(1→4) y la cadena se alarga un residuo a la vez.
      </text>
    </g>
    """)

    # Reacción 3: Glucógeno Sintasa (debajo de la lupa)
    Y_RX_SINTASA = Y_CEBADOR + 325
    svg_parts.append(f"""
    <!-- Reacción: Glucógeno Sintasa -->
    <g transform="translate(520, {Y_RX_SINTASA})">
      <line x1="0" y1="0" x2="0" y2="55" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M -4 30 Q -35 42 -90 42" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="-98" y="46" fill="#0284c7" font-size="12" font-weight="800" text-anchor="end">+ UDP libre</text>
      <g transform="translate(22, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">Glucógeno Sintasa</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 2.4.1.11 (Paso Limitante Clave)</text>
        <text x="0" y="32" fill="#16a34a" font-size="11" font-weight="700">⊕ Insulina (PP1), G-6-P</text>
        <text x="0" y="46" fill="#e11d48" font-size="11" font-weight="700">⊣ Glucagón, Adrenalina (PKA / GSK-3)</text>
      </g>
    </g>
    """)

    # Reacción 4: Enzima Ramificante
    Y_RX_RAMIF = Y_RX_SINTASA + 95
    svg_parts.append(f"""
    <!-- Reacción: Enzima Ramificadora -->
    <g transform="translate(520, {Y_RX_RAMIF})">
      <line x1="0" y1="0" x2="0" y2="50" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(22, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">Enzima Ramificadora del Glucógeno</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 2.4.1.18 (Amilo α-1,4 ➔ α-1,6)</text>
        <text x="0" y="32" fill="#c2410c" font-size="11" font-weight="700">Transfiere bloque de ~7 glucosas; ramifica cada 8-12 residuos</text>
      </g>
    </g>
    """)

    # 5. CADENA DE GLUCÓGENO RAMIFICADA (SIN GLOBO)
    Y_GLUC = Y_RX_RAMIF + 80
    svg_parts.append(f"""
    <!-- Polímero de Glucógeno Completo -->
    <g transform="translate(180, {Y_GLUC})">
      <g transform="translate(0, 30)">
        {CADENA_GLUCOGENO}
      </g>
      <g transform="translate(420, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="17" font-weight="900">Glucógeno (n + 1)</text>
        <text x="0" y="18" fill="#d97706" font-size="12.5" font-weight="800">Polisacárido de Reserva Energética</text>
        <text x="0" y="34" fill="#64748b" font-size="11">• Enlaces principales α(1→4) y ramas α(1→6)</text>
        <text x="0" y="48" fill="#b45309" font-size="11" font-weight="700">• Múltiples extremos no reductores para rápida lisis</text>
        <text x="0" y="63" fill="#64748b" font-size="10.5">Hasta 55,000 unidades de glucosa por partícula</text>
      </g>
    </g>
    """)

    # 6. GRÁNULO CITOSÓLICO DE INCLUSIÓN
    Y_GRANULO = Y_GLUC + 200
    svg_parts.append(f"""
    <!-- SECCIÓN ANATÓMICA: EL GRÁNULO DE GLUCÓGENO EN EL CITOSOL -->
    <g transform="translate(140, {Y_GRANULO})">
      <rect x="0" y="0" width="760" height="165" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="1.8"/>
      <g transform="translate(15, 15)">
        {GRANULO_CITOSOLICO_INCLUSION}
      </g>
      <g transform="translate(180, 24)">
        <text x="0" y="0" fill="#92400e" font-size="14" font-weight="900">¿POR QUÉ FLOTA EN EL CITOSOL Y CÓMO SALE DE LA CÉLULA?</text>
        <text x="0" y="20" fill="#0f172a" font-size="11" font-weight="700">
          • Inclusión no membranosa: Permite almacenar miles de glucosas sin alterar la presión osmótica celular.
        </text>
        <text x="0" y="38" fill="#dc2626" font-size="11" font-weight="700">
          • Nunca sale como polímero: No puede cruzar la membrana plasmática.
        </text>
        <text x="0" y="56" fill="#047857" font-size="11" font-weight="700">
          • En hígado: Glucógeno ➔ G-1-P ➔ G-6-P ➔ Glucosa libre (Glucosa-6-Fosfatasa en RE) ➔ GLUT-2 a sangre.
        </text>
        <text x="0" y="74" fill="#475569" font-size="10.5">
          • En músculo: Carece de Glucosa-6-Fosfatasa; el glucógeno se destina exclusivamente a ATP por Glucólisis.
        </text>
      </g>
    </g>
    """)

    # =========================================================================
    # CONEXIÓN HORIZONTAL SEGMENTADA: G-6-P ➔ G6PDH ➔ LACTONA (SHUNT PENTOSAS)
    # =========================================================================
    # Segmento 1: desde G-6-P (x=1680) hasta G6PDH (x=2000)
    # Enzima: G6PDH en x=2070 con flecha y cofactores limpios sin líneas atravesándola
    # Segmento 2: desde G6PDH (x=2140) hasta Lactona (x=2430)
    svg_parts.append("""
    <!-- Conexión horizontal hacia Shunt de Pentosas (Segmento 1) -->
    <line x1="1680" y1="410" x2="2010" y2="410" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>

    <!-- Reacción G6PDH (Totalmente despejada) -->
    <g transform="translate(2080, 410)">
      <line x1="-35" y1="0" x2="35" y2="0" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>
      <path d="M -35 -12 Q -12 -24 15 -12" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-30" y="-26" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#475569">+ NADP⁺</text>
      
      <path d="M -35 12 Q -12 24 15 12" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-30" y="30" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#059669">+ NADPH + H⁺</text>
      
      <g transform="translate(0, -2)">
        <text x="0" y="-12" font-family="'Inter', sans-serif" font-size="14.5" font-weight="800" fill="#0f172a" text-anchor="middle">G6PDH</text>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="11" fill="#64748b" text-anchor="middle">EC 1.1.1.49</text>
      </g>
    </g>

    <!-- Conexión horizontal hacia Lactona (Segmento 2) -->
    <line x1="2150" y1="410" x2="2430" y2="410" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>
    """)

    # =========================================================================
    # RUTA LATERAL DERECHA: VÍA DE LAS PENTOSAS FOSFATO (X ≈ 2450 a 3150)
    # =========================================================================
    # 1. 6-Fosfoglucono-δ-Lactona
    svg_parts.append(crear_metabolito(
        x=2440, y=375,
        nombre="6-Fosfoglucono-δ-Lactona",
        carbonos="6 Carbonos (Lactona intramolecular)",
        detalle="Primer intermediario oxidativo",
        svg_estructura=FOSFOGLUCONO_LACTONA_6,
        dx_texto=140
    ))

    # Reacción 2: Lactonasa
    svg_parts.append("""
    <g transform="translate(2760, 420)">
      <line x1="0" y1="0" x2="65" y2="0" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M 12 -14 Q 32 -26 52 -14" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="32" y="-28" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0284c7" text-anchor="middle">+ H₂O</text>
      <text x="32" y="18" font-family="'Inter', sans-serif" font-size="13.5" font-weight="800" fill="#0f172a" text-anchor="middle">Lactonasa</text>
      <text x="32" y="32" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#64748b" text-anchor="middle">EC 3.1.1.31</text>
    </g>
    """)

    # 2. 6-Fosfogluconato
    svg_parts.append(crear_metabolito(
        x=2860, y=375,
        nombre="6-Fosfogluconato",
        carbonos="6 Carbonos (Ácido aldónico Ⓟ)",
        detalle="Substrato de descarboxilación oxidativa",
        svg_estructura=FOSFOGLUCONATO_6,
        dx_texto=140
    ))

    # Reacción 3: 6-Fosfogluconato Deshidrogenasa (Vertical descendente)
    svg_parts.append("""
    <g transform="translate(2800, 510)">
      <line x1="0" y1="0" x2="0" y2="52" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
      <path d="M -85 10 Q -30 10 -4 20" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-92" y="14" fill="#475569" font-size="12" font-weight="800" text-anchor="end">+ NADP⁺</text>
      
      <path d="M -4 28 Q -30 38 -85 38" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-92" y="42" fill="#059669" font-size="12" font-weight="800" text-anchor="end">+ NADPH + H⁺</text>
      
      <path d="M 4 28 Q 30 38 85 38" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="92" y="42" fill="#475569" font-size="12" font-weight="800">+ CO₂</text>
      
      <g transform="translate(22, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">6-Fosfogluconato Deshidrogenasa</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 1.1.1.44 (Genera 2.º NADPH)</text>
      </g>
    </g>
    """)

    # 3. D-Ribulosa-5-Fosfato
    svg_parts.append(crear_metabolito(
        x=2720, y=610,
        nombre="D-Ribulosa-5-Fosfato",
        carbonos="5 Carbonos (Cetopentosa Ⓟ)",
        detalle="Encrucijada entre isomerización y epimerización",
        svg_estructura=RIBULOSA_5_FOSFATO,
        dx_texto=140
    ))

    # Bifurcación Isomerasa / Epimerasa
    svg_parts.append("""
    <g transform="translate(2800, 750)">
      <!-- Rama Izquierda a Xilulosa-5-P -->
      <path d="M -15 0 Q -100 25 -150 65" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(-140, 20)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Fosfopentosa Epimerasa</text>
        <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#64748b" text-anchor="middle">EC 5.1.3.1 (Inversión en C3)</text>
      </g>
      <!-- Rama Derecha a Ribosa-5-P -->
      <path d="M 15 0 Q 100 25 160 65" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(140, 20)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#0f172a" text-anchor="middle">Fosfopentosa Isomerasa</text>
        <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="10.5" fill="#64748b" text-anchor="middle">EC 5.3.1.6 (Cetosa ⇄ Aldosa)</text>
      </g>
    </g>
    """)

    # 4a. Xilulosa-5-P (a la izquierda)
    svg_parts.append(crear_metabolito(
        x=2480, y=835,
        nombre="D-Xilulosa-5-P",
        carbonos="5 Carbonos (Epímero C3)",
        detalle="Donador de 2C a la Transcetolasa",
        svg_estructura=XILULOSA_5_FOSFATO,
        texto_izquierda=True
    ))

    # 4b. Ribosa-5-P (a la derecha)
    svg_parts.append(crear_metabolito(
        x=2960, y=835,
        nombre="D-Ribosa-5-P",
        carbonos="5 Carbonos (Pentosa Aldosa)",
        detalle="Precursora de Nucleótidos y Ácidos Nucleicos",
        svg_estructura=RIBOSA_5_FOSFATO,
        dx_texto=140
    ))

    # Salida hacia Síntesis de Nucleótidos desde Ribosa-5-P (y = 960)
    svg_parts.append("""
    <g transform="translate(3030, 955)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>
      <g transform="translate(0, 42)">
        <rect x="-105" y="0" width="210" height="40" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="2"/>
        <text x="0" y="16" fill="#6d28d9" font-size="12" font-weight="900" text-anchor="middle">SÍNTESIS DE NUCLEÓTIDOS</text>
        <text x="0" y="30" fill="#7c3aed" font-size="10" font-weight="700" text-anchor="middle">PRPP ➔ ARN, ADN, ATP, GTP</text>
      </g>
    </g>
    """)

    # Fase No Oxidativa: TK1 (DESPEJADA >100 px debajo de la caja morada, en y = 1110)
    svg_parts.append(crear_paso_no_oxidativo(
        x=2780, y=1110,
        enzima="Transcetolasa (TK1)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Ribosa-5-P (5C)",
        productos_txt="GAP (3C) + Sedoheptulosa-7-P (7C)"
    ))

    # Sedoheptulosa-7-P (Izquierda)
    svg_parts.append(crear_metabolito(
        x=2480, y=1210,
        nombre="Sedoheptulosa-7-P",
        carbonos="7 Carbonos (Heptosa Ⓟ)",
        detalle="Intermediario transitorio de 7C",
        svg_estructura=SEDOHEPTULOSA_7_FOSFATO,
        texto_izquierda=True
    ))

    # GAP (Derecha)
    svg_parts.append(crear_metabolito(
        x=2960, y=1210,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="Aceptor intermedio",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO,
        dx_texto=140
    ))

    # Transaldolasa (TA)
    svg_parts.append(crear_paso_no_oxidativo(
        x=2780, y=1340,
        enzima="Transaldolasa (TA)",
        ec="EC 2.2.1.2 (Base de Schiff con Lys)",
        sustratos_txt="Sedoheptulosa-7-P (7C) + GAP (3C)",
        productos_txt="Eritrosa-4-P (4C) + Fructosa-6-P (6C)"
    ))

    # Eritrosa-4-P (Izquierda)
    svg_parts.append(crear_metabolito(
        x=2480, y=1440,
        nombre="D-Eritrosa-4-P",
        carbonos="4 Carbonos (Tetrosa)",
        detalle="Precursor de Aminoácidos Aromáticos",
        svg_estructura=ERITROSA_4_FOSFATO,
        texto_izquierda=True
    ))

    # F6P (1er reingreso - Derecha)
    svg_parts.append(crear_metabolito(
        x=2960, y=1440,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡1.er Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        dx_texto=140
    ))

    # TK2
    svg_parts.append(crear_paso_no_oxidativo(
        x=2780, y=1570,
        enzima="Transcetolasa (TK2)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Eritrosa-4-P (4C)",
        productos_txt="Fructosa-6-P (6C) + GAP (3C)"
    ))

    # F6P (2º reingreso)
    svg_parts.append(crear_metabolito(
        x=2480, y=1670,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡2.º Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        texto_izquierda=True
    ))

    # GAP (3er reingreso)
    svg_parts.append(crear_metabolito(
        x=2960, y=1670,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="¡3.er Reingreso a la Glucólisis!",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO,
        dx_texto=140
    ))

    # BANNER DE BALANCE FINAL DE PENTOSAS
    svg_parts.append("""
    <g transform="translate(2780, 1830)">
      <rect x="-260" y="-14" width="520" height="74" rx="12" fill="#ffffff" stroke="#7c3aed" stroke-width="2.2" filter="drop-shadow(0 4px 8px rgba(0,0,0,0.06))"/>
      <text x="0" y="14" fill="#6d28d9" font-size="14" font-weight="900" text-anchor="middle">BALANCE TOTAL DE LA FASE NO OXIDATIVA</text>
      <text x="0" y="34" fill="#0f172a" font-size="12.5" font-weight="800" text-anchor="middle">3 Pentosas (5C) ⇄ 2 Fructosa-6-P (6C) + 1 Gliceraldehído-3-P (3C)</text>
      <text x="0" y="50" fill="#047857" font-size="11.5" font-weight="700" text-anchor="middle">Todos los carbonos se reciclan de vuelta hacia el eje de la Glucólisis citosólica</text>
    </g>
    """)

    # =========================================================================
    # FLECHAS DE RETORNO/RECICLAJE HACIA LA GLUCÓLISIS CENTRAL
    # =========================================================================
    svg_parts.append("""
    <!-- RETORNO 1: Fructosa-6-P hacia F6P Central -->
    <path d="M 2960 1485 C 2400 1400 1950 900 1690 635" fill="none" stroke="#059669" stroke-width="2.8" stroke-dasharray="9 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(2100, 890)">
      <text x="0" y="0" fill="#047857" font-size="11" font-weight="800" text-anchor="middle">RETORNO: F-6-P A GLUCÓLISIS</text>
    </g>

    <!-- RETORNO 2: GAP hacia GAP Central -->
    <path d="M 2960 1715 C 2480 1640 2000 1350 1810 1140" fill="none" stroke="#059669" stroke-width="2.8" stroke-dasharray="9 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(2280, 1370)">
      <text x="0" y="0" fill="#047857" font-size="11" font-weight="800" text-anchor="middle">RETORNO: GAP A GLUCÓLISIS</text>
    </g>
    """)

    # =========================================================================
    # RESTO DEL EJE GLUCOLÍTICO (CENTRAL: X_GLU = 1520, X_FLECHA = 1580)
    # =========================================================================
    # Reacción 2: Fosfoglucosa Isomerasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=530,
        enzima="Fosfoglucosa Isomerasa",
        ec="EC 5.3.1.9 (⇄)",
        reversible=True
    ))

    # 3. Fructosa-6-Fosfato (RECIBE RETORNO DE PENTOSAS)
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=610,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Cetosa Ⓟ)",
        detalle="Punto receptor de Transcetolasa / Transaldolasa",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        dx_texto=140
    ))

    # Reacción 3: PFK-1
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=725,
        enzima="Fosfofructoquinasa-1 (PFK-1)",
        ec="EC 2.7.1.11 (Compromiso Clave)",
        regulacion="⊣ ATP, Citrato | ⊕ AMP, F-2,6-BP",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 4. Fructosa-1,6-Bisfosfato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=825,
        nombre="Fructosa-1,6-Bisfosfato",
        carbonos="6 Carbonos (Fructofuranosa 1,6-Ⓟ)",
        detalle="Molécula simétrica lista para clivaje",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO,
        dx_texto=140
    ))

    # Reacción 4: Aldolasa
    svg_parts.append("""
    <g transform="translate(1580, 940)">
      <line x1="0" y1="0" x2="0" y2="40" stroke="#ea580c" stroke-width="2.8"/>
      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="14.5" font-weight="800">Aldolasa A (Clivaje C3-C4)</text>
        <text x="0" y="15" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 4.1.2.13 (Retroaldólica)</text>
      </g>
      <path d="M 0 40 Q -70 55 -110 80" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <path d="M 0 40 Q 70 55 110 80" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
    </g>
    """)

    # 5a. DHAP y 5b. GAP (Bifurcación simétrica)
    svg_parts.append(crear_metabolito(
        x=1320, y=1035,
        nombre="Dihidroxiacetona-Ⓟ",
        carbonos="3 Carbonos (Cetotriosa)",
        detalle="Isomerizada por TPI",
        svg_estructura=DIHIDROXIACETONA_FOSFATO,
        texto_izquierda=True
    ))

    svg_parts.append(crear_metabolito(
        x=1680, y=1035,
        nombre="Gliceraldehído-3-Ⓟ",
        carbonos="3 Carbonos (Aldotriosa)",
        detalle="Continúa la vía oxidativa",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO,
        dx_texto=140
    ))

    # TPI (Conexión horizontal reversible entre triosas)
    svg_parts.append("""
    <g transform="translate(1540, 1070)">
      <line x1="-70" y1="-3" x2="70" y2="-3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="70" y1="3" x2="-70" y2="3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(0, -12)">
        <text x="0" y="-8" fill="#0f172a" font-size="13.5" font-weight="800" text-anchor="middle">Triosa Fosfato Isomerasa</text>
        <text x="0" y="6" fill="#64748b" font-size="11" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1 (⇄)</text>
      </g>
    </g>
    """)

    # Convergencia a 2x GAP (Limpia, sin globo)
    svg_parts.append("""
    <g transform="translate(1580, 1180)">
      <path d="M 1720 1120 Q 1720 1160 1580 1180" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="0" y="0" fill="#c2410c" font-size="12.5" font-weight="900" text-anchor="middle">
        FASE DE BENEFICIO (× 2 TRIOSAS)
      </text>
    </g>
    """)

    # Reacción 6: GAPDH
    svg_parts.append("""
    <g transform="translate(1580, 1235)">
      <line x1="-3.5" y1="0" x2="-3.5" y2="52" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="3.5" y1="52" x2="3.5" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <path d="M -85 10 Q -30 10 -4 20" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-92" y="14" fill="#475569" font-size="12" font-weight="800" text-anchor="end">+ 2 NAD⁺ + 2 Pi</text>
      <path d="M -4 28 Q -30 38 -85 38" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-92" y="42" fill="#059669" font-size="12" font-weight="800" text-anchor="end">+ 2 NADH + 2 H⁺</text>
      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="14.5" font-weight="800">GAPDH (Gliceraldehído-3-P DH)</text>
        <text x="0" y="15" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 1.2.1.12 (Cisteína catalítica)</text>
      </g>
    </g>
    """)

    # 5. 1,3-Bisfosfoglicerato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1345,
        nombre="1,3-Bisfosfoglicerato",
        carbonos="3 Carbonos (Acil-fosfato de alta energía)",
        detalle="Primer intermediario de alto potencial Ⓟ",
        svg_estructura=BISFOSFOGLICERATO_1_3,
        dx_texto=140
    ))

    # Reacción 7: Fosfoglicerato Quinasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1460,
        enzima="Fosfoglicerato Quinasa",
        ec="EC 2.7.2.3 (Fosforilación a nivel de sustrato)",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True,
        reversible=True
    ))

    # 6. 3-Fosfoglicerato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1560,
        nombre="3-Fosfoglicerato",
        carbonos="3 Carbonos (Carboxilato)",
        detalle="Substrato de mutación intramolecular",
        svg_estructura=FOSFOGLICERATO_3,
        dx_texto=140
    ))

    # Reacción 8: Fosfoglicerato Mutasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1670,
        enzima="Fosfoglicerato Mutasa",
        ec="EC 5.4.2.1 (Intermediario 2,3-BPG)",
        reversible=True
    ))

    # 7. 2-Fosfoglicerato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1770,
        nombre="2-Fosfoglicerato",
        carbonos="3 Carbonos (Éster fosfórico C2)",
        detalle="Substrato para deshidratación",
        svg_estructura=FOSFOGLICERATO_2,
        dx_texto=140
    ))

    # Reacción 9: Enolasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1880,
        enzima="Enolasa",
        ec="EC 4.2.1.11 (Mg²⁺, Deshidratación)",
        salida_agua=True,
        reversible=True
    ))

    # 8. PEP
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1980,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 Carbonos (Enol-fosfato)",
        detalle="Mayor potencial de transferencia Ⓟ (ΔG'° = -61.9 kJ/mol)",
        svg_estructura=FOSFOENOLPIRUVATO,
        dx_texto=140
    ))

    # Reacción 10: Piruvato Quinasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=2090,
        enzima="Piruvato Quinasa",
        ec="EC 2.7.1.40 (K⁺, Mg²⁺)",
        regulacion="⊣ ATP, Alanina | ⊕ F-1,6-BP",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True
    ))

    # 9. Piruvato (Llega en x=1520, y=2180)
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=2180,
        nombre="Piruvato",
        carbonos="3 Carbonos (α-Cetoácido)",
        detalle="Destino terminal: cruce al interior mitocondrial vía MPC",
        svg_estructura=PIRUVATO,
        dx_texto=140
    ))

    # Ensamblar HTML completo
    html_final = CABECERA_HTML + "\n".join(svg_parts) + PIE_HTML

    ruta_salida = os.path.join(os.path.dirname(__file__), "Carbohidratos_Unidos.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"✅ Mapa Integrado de Carbohidratos generado con éxito en: {ruta_salida}")

if __name__ == "__main__":
    generar_mapa_carbohidratos()
