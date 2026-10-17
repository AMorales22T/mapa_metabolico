# =============================================================================
# MÓDULO DE REVISIÓN: Contrato de Layout y Entorno Celular Continuo
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/carbohidratos_unidos/generar_carbohidratos_unidos.py (líneas 1 a 339 de 1241)
# Descripción      : Coordenadas maestras, validación geométrica y dibujo del citosol.
# =============================================================================

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
sys.path.append(os.path.join(DIR_BASE, "via_01_glucolisis"))
sys.path.append(os.path.join(DIR_BASE, "via_04_pentosas_fosfato"))
sys.path.append(os.path.join(DIR_BASE, "via_03_glucogenogenesis_y_glucogenolisis"))

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

# Lienzo horizontal para cartulina: deja tres corredores legibles y una base
# mitocondrial amplia, sin cambiar las proporciones de las rutas individuales.
ANCHO_CANVAS = 3600
ALTO_CANVAS = 2940

# ============================================================================
# CONTRATO DE LAYOUT DEL MAPA UNIFICADO
# ============================================================================
# Estas reglas sólo afectan a este mapa integrado. Las rutas individuales
# siguen siendo sus propias composiciones y no se modifican.
MODO_BOCETO = False

BANDAS = {
    # (y_inicial, y_final): el eje Y depende del compartimento celular.
    "extracelular": (0, 140),
    "citosol": (140, 2380),
    "matriz_mitocondrial": (2380, ALTO_CANVAS),
}

CARRILES_CITOSOL = {
    # Cada ruta conserva este intervalo X de principio a fin.
    "glucogenesis_glucogenolisis": (100, 1050),
    "glucolisis_gluconeogenesis": (1150, 2050),
    "pentosas_fosfato": (2350, 3500),
    # Espacio reservado para futuras rutas citosólicas.
    "reserva_citosolica": (2050, 2350),
}

CARRILES_MITOCONDRIA = {
    "entrada_piruvato_pdh": (500, 2050),
    "ciclo_krebs": (1650, 2800),
    "reserva_matriz": (2650, 3350),
}

# Nodos de unión: se registran una vez y las rutas futuras deben apuntar aquí.
# La estructura molecular completa se dibuja sólo en el nodo maestro; las
# conexiones secundarias serán flechas, no copias de la molécula.
NODOS_UNION = {
    "glucosa_6_fosfato": {
        "x": 1520, "y": 375, "banda": "citosol",
        "carril": "glucolisis_gluconeogenesis",
    },
    "piruvato": {
        "x": 1520, "y": 2180, "banda": "citosol",
        "carril": "glucolisis_gluconeogenesis",
    },
    "acetil_coa": {
        "x": 2500, "y": 2650, "banda": "matriz_mitocondrial",
        "carril": "ciclo_krebs",
    },
}


def validar_contrato_layout():
    """Falla pronto si un nodo compartido se sale de su banda o carril."""
    for nombre, nodo in NODOS_UNION.items():
        y_min, y_max = BANDAS[nodo["banda"]]
        if not y_min <= nodo["y"] <= y_max:
            raise ValueError(f"Nodo {nombre} fuera de su banda: y={nodo['y']}")

        carriles = CARRILES_CITOSOL if nodo["banda"] == "citosol" else CARRILES_MITOCONDRIA
        x_min, x_max = carriles[nodo["carril"]]
        if not x_min <= nodo["x"] <= x_max:
            raise ValueError(f"Nodo {nombre} fuera de su carril: x={nodo['x']}")


def punto_nodo(nombre):
    """Devuelve el punto maestro para que una ruta futura pueda conectarse."""
    try:
        nodo = NODOS_UNION[nombre]
    except KeyError as exc:
        raise KeyError(f"Nodo de unión no registrado: {nombre}") from exc
    return nodo["x"], nodo["y"]


def flecha_a_nodo(nombre, x_origen, y_origen, color="#059669", dash="9 5"):
    """Genera una conexión secundaria hacia un nodo ya existente."""
    x_destino, y_destino = punto_nodo(nombre)
    return f'<path d="M {x_origen} {y_origen} L {x_destino} {y_destino}" fill="none" stroke="{color}" stroke-width="2.8" stroke-dasharray="{dash}" marker-end="url(#arrowGreen)"/>'

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
          <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
          <stop offset="5%" stop-color="#f0fdf4" stop-opacity="0.8" />
          <stop offset="50%" stop-color="#f8fafc" stop-opacity="0.5" />
          <stop offset="90%" stop-color="#f0fdf4" stop-opacity="0.7" />
          <stop offset="100%" stop-color="#f8fafc" stop-opacity="1" />
        </linearGradient>

        <radialGradient id="haloCitosolUnificado" cx="50%" cy="48%" r="72%">
          <stop offset="0%" stop-color="#bbf7d0" stop-opacity="0.14" />
          <stop offset="55%" stop-color="#dcfce7" stop-opacity="0.07" />
          <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
        </radialGradient>

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

    <!-- El citosol se percibe como un medio acuoso, no como una caja cerrada. -->
    <ellipse cx="{ancho/2}" cy="1280" rx="{ancho*0.47}" ry="1090" fill="url(#haloCitosolUnificado)"/>
    <g transform="translate(155, 215)" opacity="0.88">
      <text x="0" y="0" fill="#166534" font-size="18" font-weight="900" letter-spacing="2.2">CITOSOL</text>
      <path d="M 0 12 Q 130 25 280 12" fill="none" stroke="#4ade80" stroke-width="2"/>
      <text x="0" y="34" fill="#15803d" font-size="11.5" font-weight="700">Medio acuoso celular: las rutas se cruzan, se ramifican y regresan aquí</text>
    </g>

    <!-- Ondulaciones de flujo citosólico: dan profundidad sin encerrar las rutas -->
    <g fill="none" stroke="#86efac" opacity="0.22">
      <path d="M 80 520 Q 720 450 1320 540 T 2500 520 T 3520 560" stroke-width="3" stroke-dasharray="18 14"/>
      <path d="M 80 920 Q 650 1010 1240 900 T 2500 940 T 3520 880" stroke-width="2" stroke-dasharray="12 16"/>
      <path d="M 80 1800 Q 720 1710 1350 1810 T 2500 1780 T 3520 1840" stroke-width="2.5" stroke-dasharray="20 18"/>
    </g>

    <!-- Polirribosomas flotantes: textura celular tomada del diseño de Glucólisis -->
    <g fill="#64748b" opacity="0.23">
      <g transform="translate(140, 410)"><circle cx="0" cy="0" r="4"/><circle cx="11" cy="3" r="3"/><circle cx="18" cy="11" r="3.5"/><circle cx="8" cy="16" r="3"/><circle cx="-3" cy="12" r="3.5"/></g>
      <g transform="translate(3330, 470)"><circle cx="0" cy="0" r="4"/><circle cx="11" cy="3" r="3"/><circle cx="18" cy="11" r="3.5"/><circle cx="8" cy="16" r="3"/><circle cx="-3" cy="12" r="3.5"/></g>
      <g transform="translate(1160, 1480)"><circle cx="0" cy="0" r="4"/><circle cx="11" cy="3" r="3"/><circle cx="18" cy="11" r="3.5"/><circle cx="8" cy="16" r="3"/><circle cx="-3" cy="12" r="3.5"/></g>
      <g transform="translate(2250, 1970)"><circle cx="0" cy="0" r="4"/><circle cx="11" cy="3" r="3"/><circle cx="18" cy="11" r="3.5"/><circle cx="8" cy="16" r="3"/><circle cx="-3" cy="12" r="3.5"/></g>
    </g>

    <!-- ============================================================= -->
    <!-- MEMBRANA PLASMÁTICA CONTINUA (CRUZA TODO EL CITOSOL ARRIBA)   -->
    <!-- ============================================================= -->
    <!-- Espacio Extracelular / Sangre -->
    <path d="M 0 0 L {ancho} 0 L {ancho} 60 Q {ancho*0.5} 86 0 60 Z" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
    <text x="35" y="32" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#64748b" letter-spacing="1.5">
      ESPACIO EXTRACELULAR (SANGRE / LÍQUIDO INTERSTICIAL)
    </text>

    <!-- Bicapa fosfolipídica ondulada, como en via_01_glucolisis -->
    <path d="M 0 60 Q {ancho*0.25} 88 {ancho*0.5} 60 T {ancho} 60" fill="none" stroke="#0284c7" stroke-width="9" stroke-linecap="round"/>
    <path d="M 0 69 Q {ancho*0.25} 97 {ancho*0.5} 69 T {ancho} 69" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>

    <!-- Cabezas polares decorativas siguiendo la onda -->
    <g fill="#0284c7" opacity="0.65">
      <circle cx="120" cy="64" r="3"/><circle cx="135" cy="66" r="3"/><circle cx="150" cy="68" r="3"/>
      <circle cx="860" cy="71" r="3"/><circle cx="875" cy="70" r="3"/><circle cx="890" cy="68" r="3"/>
      <circle cx="2700" cy="69" r="3"/><circle cx="2715" cy="67" r="3"/><circle cx="2730" cy="65" r="3"/>
      <circle cx="3370" cy="64" r="3"/><circle cx="3385" cy="63" r="3"/><circle cx="3400" cy="62" r="3"/>
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

