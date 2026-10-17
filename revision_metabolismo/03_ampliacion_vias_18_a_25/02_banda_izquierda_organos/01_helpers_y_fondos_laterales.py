# =============================================================================
# MÓDULO DE REVISIÓN: Helpers Visuales y Fondos de Bandas Laterales
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/generar_ampliacion.py (líneas 1 a 288 de 925)
# Descripción      : Funciones badge_via, encabezado_via, nodo_libre, reaccion_flecha y fondos de bandas izquierda y derecha.
# =============================================================================

#!/usr/bin/env python3
"""
GENERADOR DE PÓSTER METABÓLICO INTEGRADO AMPLIADO (1200 × 900 mm) - VERSIÓN V3
================================================================================
Mejoras implementadas según retroalimentación:
1. Torrente vascular continuo de X=-760 a X=6560 a Y=350..418 px.
2. Banda Izquierda:
   - Vía 18: Digestión de lípidos (micela mixta, enterocito con borde en cepillo, REL, Golgi, quilomicrón y linfa).
   - Vía 19: Tejido adiposo con gota lipídica y cascada secuencial lipolítica completa con estructuras químicas:
     TAG ➔ ATGL ➔ DAG + 1º AG ➔ HSL ➔ 2-MAG + 2º AG ➔ MGL ➔ Glicerol + 3º AG.
   - Vía 20: Músculo esquelético con anatomía científica del sarcómero estriado en contracción (líneas Z, actina, miosina, túbulo T)
     y acoplamiento con Cori (lactato) y Cahill (alanina).
   - Vía 21: Cerebro y sistema nervioso con dibujo anatómico del encéfalo (hemisferio, cerebelo) y neurona multipolar mielinizada,
     con transporte de glucosa (GLUT1/3) y adaptación a cetonas (MCT) sin muros de texto.
3. Banda Derecha:
   - Vía 22: Lipoproteínas plasmáticas (VLDL, LDL, LDLR, HDL, SR-B1).
   - Vía 23: Biosíntesis de TAG y Fosfolípidos (Kennedy: G3P ➔ LPA ➔ PA ➔ DAG ➔ TAG / PC).
   - Vía 24: Biosíntesis de aminoácidos no esenciales (Ala, Ser, Gly, Cys, Asp, Asn, Glu, Gln, Pro, Tyr).
   - Vía 25: Conmutador visual de estados metabólicos.
4. Actualización de la leyenda institucional:
   - Vías metabólicas reorganizadas en 3 columnas equilibradas (1-8, 9-16, 17-25).
   - Título cambiado de 'CÓDIGO DE COLORES EDITORIAL:' a 'CÓDIGO DE COLORES:'.
5. Calibración geométrica de offsets para eliminar solapamientos.
"""

import base64
import os
import re
import shutil
import subprocess
import sys

DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_SCRIPT)
DIR_HTML = os.path.join(DIR_BASE, "versiones_html")
DIR_IMPRESION = os.path.join(DIR_BASE, "versiones_impresion")

sys.path.append(DIR_SCRIPT)
import estructuras_ampliacion as ea
from interactividad_html import construir_html_mapa_ampliado

sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "via_13_transaminacion_y_desaminacion"))
import estructuras_aminoacidos as eaa

sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "via_12b_destinos_esqueletos_carbonados"))
import estructuras_destinos_aa as eda

RUTA_ORIGINAL_HTML = os.path.join(DIR_HTML, "prueba_visual_integrada_conectada.html")
RUTA_OUT_HTML = os.path.join(DIR_SCRIPT, "mapa_cartulina_ampliado.html")
RUTA_OUT_SVG = os.path.join(DIR_SCRIPT, "mapa_cartulina_ampliado.svg")
RUTA_OUT_PDF = os.path.join(DIR_SCRIPT, "mapa_cartulina_ampliado.pdf")
RUTA_OUT_PNG = os.path.join(DIR_SCRIPT, "mapa_cartulina_ampliado_preview.png")
RUTA_COPIA_PDF = os.path.join(DIR_IMPRESION, "mapa_metabolico_integrado_ampliado_120x90cm.pdf")


def cargar_fuentes_base64():
    """Genera reglas @font-face con archivos woff2 incrustados en base64 si existen."""
    d_inter = "/tmp/fonts_install/node_modules/@fontsource/inter/files"
    d_mono = "/tmp/fonts_install/node_modules/@fontsource/jetbrains-mono/files"
    css_fonts = []

    for w in [400, 600, 700, 800, 900]:
        fpath = os.path.join(d_inter, f"inter-latin-{w}-normal.woff2")
        if os.path.exists(fpath):
            with open(fpath, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("ascii")
            css_fonts.append(f"""
@font-face {{
  font-family: 'Inter';
  font-style: normal;
  font-weight: {w};
  font-display: swap;
  src: url('data:font/woff2;charset=utf-8;base64,{b64}') format('woff2');
}}""")

    for w in [600, 700, 800]:
        fpath = os.path.join(d_mono, f"jetbrains-mono-latin-{w}-normal.woff2")
        if os.path.exists(fpath):
            with open(fpath, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("ascii")
            css_fonts.append(f"""
@font-face {{
  font-family: 'JetBrains Mono';
  font-style: normal;
  font-weight: {w};
  font-display: swap;
  src: url('data:font/woff2;charset=utf-8;base64,{b64}') format('woff2');
}}""")

    return "\n".join(css_fonts)


# =============================================================================
# FUNCIONES AUXILIARES DE RENDERIZADO VISUAL
# =============================================================================

def badge_via(n, x, y, id_badge=None, color="#0284c7"):
    bid = id_badge or f"badge_via_{str(n).replace(' ', '_')}"
    return f"""
    <g id="{bid}" class="badge-via" transform="translate({x}, {y})">
      <circle cx="0" cy="0" r="14" fill="{color}" stroke="#ffffff" stroke-width="2.2" />
      <text x="0" y="5" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{n}</text>
    </g>
    """

def encabezado_via(x, y, n, titulo, subtitulo="", color="#0284c7"):
    sub = f'<text x="{x + 36}" y="{y + 19}" fill="#64748b" font-size="11" font-weight="700" font-family="\'Inter\', sans-serif">{subtitulo}</text>' if subtitulo else ""
    return f"""
    <g class="encabezado-seccion">
      {badge_via(n, x + 14, y + 2, color=color)}
      <text x="{x + 36}" y="{y + 2}" fill="{color}" font-size="15.5" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="0.5">{titulo}</text>
      {sub}
    </g>
    """

def nodo_libre(x, y, nombre, carbonos, svg_mol, id_nodo="", text_right=True, dx=180, dy=24, detalle="", formula=""):
    txt_formula = f'<text x="{dx}" y="{dy + 17}" fill="#ea580c" font-size="11" font-weight="700" font-family="\'JetBrains Mono\', monospace">[{carbonos}] {formula}</text>'
    txt_det = f'<text x="{dx}" y="{dy + 34}" fill="#64748b" font-size="9.5" font-weight="600" font-family="\'Inter\', sans-serif">{detalle}</text>' if detalle else ""
    return f"""
    <g id="{id_nodo}" class="nodo-metabolito-libre" transform="translate({x}, {y})">
      <g>{svg_mol}</g>
      <text x="{dx}" y="{dy}" fill="#0f172a" font-size="14.5" font-weight="800" font-family="'Inter', sans-serif">{nombre}</text>
      {txt_formula}
      {txt_det}
    </g>
    """

def reaccion_flecha(x, y, h, enzima, entra="", sale="", ec="", color="#ea580c", text_dx=14, reversible=False, curvas_side="left", text_anchor="start", id_rx=""):
    curvas = ""
    if curvas_side == "left":
        if entra:
            curvas += f"""
            <path d="M -60 6 Q -20 6 -4 16" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
            <text x="-66" y="9" fill="#dc2626" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{entra}</text>
            """
        if sale:
            curvas += f"""
            <path d="M -4 20 Q -20 30 -60 30" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
            <text x="-66" y="34" fill="#059669" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{sale}</text>
            """
    else:
        if entra:
            curvas += f"""
            <path d="M 60 6 Q 20 6 4 16" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
            <text x="66" y="9" fill="#dc2626" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="start">{entra}</text>
            """
        if sale:
            curvas += f"""
            <path d="M 4 20 Q 20 30 60 30" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
            <text x="66" y="34" fill="#059669" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="start">{sale}</text>
            """
    
    if reversible:
        lineas = f"""
        <line x1="-3" y1="0" x2="-3" y2="{h}" stroke="{color}" stroke-width="2" marker-end="url(#arrowFlow)"/>
        <line x1="3" y1="{h}" x2="3" y2="0" stroke="{color}" stroke-width="2" marker-end="url(#arrowFlow)"/>
        """
    else:
        lineas = f"""<line x1="0" y1="0" x2="0" y2="{h}" stroke="{color}" stroke-width="2.6" marker-end="url(#arrowFlow)"/>"""
        
    anchor_attr = f'text-anchor="{text_anchor}"' if text_anchor != "start" else ""
    txt_ec = f'<text x="{text_dx}" y="{h//2 + 18}" fill="#64748b" font-size="9" font-family="\'JetBrains Mono\', monospace" {anchor_attr}>{ec}</text>' if ec else ""
    id_attr = f'id="{id_rx}"' if id_rx else ""
    return f"""
    <g {id_attr} class="reaccion-paso" transform="translate({x}, {y})">
      {lineas}
      {curvas}
      <text x="{text_dx}" y="{h//2 + 4}" fill="#0f172a" font-size="12" font-weight="800" font-family="'Inter', sans-serif" {anchor_attr}>{enzima}</text>
      {txt_ec}
    </g>
    """


# =============================================================================
# CONSTRUCCIÓN DE LAS BANDAS LATERALES Y CAPAS AMBIENTALES
# =============================================================================

def construir_fondo_izquierdo():
    """Fondo ambiental continuo a la izquierda con torrente vascular alineado a Y=350..418 px."""
    return f"""
    <g id="print_fondo_izq">
      <rect x="-760" y="0" width="760.5" height="5120" fill="url(#gradCitosolUnificado)" />

      <!-- Citoesqueleto y microfilamentos -->
      <g fill="none" stroke="#cbd5e1" opacity="0.3">
        <path d="M -760 480 Q -380 450 60 480" stroke-width="2.5" stroke-dasharray="16 12" />
        <path d="M -760 1120 Q -380 1160 60 1120" stroke-width="2" stroke-dasharray="12 14" />
        <path d="M -760 1880 Q -380 1840 60 1880" stroke-width="2.2" stroke-dasharray="14 10" />
        <path d="M -760 2680 Q -380 2720 60 2680" stroke-width="2" stroke-dasharray="12 12" />
        <path d="M -760 3580 Q -380 3540 60 3580" stroke-width="2.2" stroke-dasharray="14 10" />
      </g>

      <!-- Extensión del vientre muscular superior X: [-760, 0], Y: [12, 340] -->
      <rect x="-760" y="12" width="760.5" height="328" fill="url(#gradVientreMuscular)" stroke="#9f1239" stroke-width="3" />
      <g fill="none" stroke="#f43f5e" opacity="0.18" stroke-dasharray="14 10">
        <line x1="-760" y1="90" x2="0" y2="90" stroke-width="2"/>
        <line x1="-760" y1="180" x2="0" y2="180" stroke-width="2"/>
        <line x1="-760" y1="270" x2="0" y2="270" stroke-width="2"/>
      </g>

      <!-- TORRENTE VASCULAR CONTINUO IZQUIERDO (ALINEADO A Y = 350..418 PX) -->
      <path d="M -760 350 L 0.5 350 L 0.5 418 C -250 415, -500 418, -760 418 Z" fill="url(#print_gradPlasma)" />
      
      <!-- Corriente de plasma laminar continua -->
      <g fill="none" stroke="#ef4444" opacity="0.3" stroke-linecap="round">
        <path d="M -760 366 Q -380 374 0 366" stroke-width="2.5" stroke-dasharray="25 15" />
        <path d="M -760 384 Q -380 392 0 384" stroke-width="3" stroke-dasharray="35 20" />
        <path d="M -760 402 Q -380 410 0 402" stroke-width="2" stroke-dasharray="20 18" />
      </g>

      <!-- Eritrocitos bicóncavos -->
      <g opacity="0.88">
        <g transform="translate(-620, 384) rotate(-14)">
          <ellipse cx="0" cy="0" rx="26" ry="17" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8" />
          <ellipse cx="0" cy="0" rx="14" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75" />
        </g>
        <g transform="translate(-410, 376) rotate(16)">
          <ellipse cx="0" cy="0" rx="24" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6" />
          <ellipse cx="0" cy="0" rx="12" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7" />
        </g>
        <g transform="translate(-190, 388) rotate(-8)">
          <ellipse cx="0" cy="0" rx="25" ry="16" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8" />
          <ellipse cx="0" cy="0" rx="13" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75" />
        </g>
      </g>

      <!-- Membrana plasmática bicapa continua izquierda -->
      <path d="M -760 418 C -500 418, -250 414.7, 0 418 L 15 418.33" fill="none" stroke="#0284c7" stroke-width="10" stroke-linecap="round" />
      <path d="M -760 428 C -500 428, -250 424.7, 0 428 L 15 428.33" fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" />
    </g>
    """


def construir_fondo_derecho():
    """Fondo ambiental continuo a la derecha con torrente vascular alineado a Y=350..418 px."""
    return f"""
    <g id="print_fondo_der">
      <rect x="5800" y="0" width="760" height="5120" fill="url(#gradCitosolUnificado)" />

      <!-- Citoesqueleto y microfilamentos -->
      <g fill="none" stroke="#cbd5e1" opacity="0.3">
        <path d="M 5800 480 Q 6180 510 6560 480" stroke-width="2.5" stroke-dasharray="16 12" />
        <path d="M 5800 1120 Q 6180 1080 6560 1120" stroke-width="2" stroke-dasharray="12 14" />
        <path d="M 5800 1880 Q 6180 1920 6560 1880" stroke-width="2.2" stroke-dasharray="14 10" />
        <path d="M 5800 2680 Q 6180 2640 6560 2680" stroke-width="2" stroke-dasharray="12 12" />
        <path d="M 5800 3580 Q 6180 3620 6560 3580" stroke-width="2.2" stroke-dasharray="14 10" />
      </g>

      <!-- Extensión vascular superior derecha -->
      <rect x="5800" y="12" width="760" height="328" fill="url(#gradVientreMuscular)" stroke="#9f1239" stroke-width="3" />

      <!-- TORRENTE VASCULAR CONTINUO DERECHO (ALINEADO A Y = 350..418 PX) -->
      <path d="M 5800 350 L 6560 350 L 6560 418 C 6350 418, 6050 418, 5800 418 Z" fill="url(#print_gradPlasma)" />

      <!-- Corriente de plasma laminar continua -->
      <g fill="none" stroke="#ef4444" opacity="0.3" stroke-linecap="round">
        <path d="M 5800 366 Q 6180 374 6560 366" stroke-width="2.5" stroke-dasharray="25 15" />
        <path d="M 5800 384 Q 6180 392 6560 384" stroke-width="3" stroke-dasharray="35 20" />
        <path d="M 5800 402 Q 6180 410 6560 402" stroke-width="2" stroke-dasharray="20 18" />
      </g>

      <!-- Eritrocitos bicóncavos -->
      <g opacity="0.88">
        <g transform="translate(5980, 382) rotate(14)">
          <ellipse cx="0" cy="0" rx="25" ry="16" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8" />
          <ellipse cx="0" cy="0" rx="13" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75" />
        </g>
        <g transform="translate(6240, 376) rotate(-12)">
          <ellipse cx="0" cy="0" rx="24" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6" />
          <ellipse cx="0" cy="0" rx="12" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7" />
        </g>
        <g transform="translate(6460, 386) rotate(10)">
          <ellipse cx="0" cy="0" rx="25" ry="16" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8" />
          <ellipse cx="0" cy="0" rx="13" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75" />
        </g>
      </g>

      <!-- Membrana plasmática bicapa continua derecha -->
      <path d="M 5770 431.4 C 5960 431.4, 6250 424, 6560 418" fill="none" stroke="#0284c7" stroke-width="10" stroke-linecap="round" />
      <path d="M 5770 441.4 C 5960 441.4, 6250 434, 6560 428" fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" />
    </g>
    """


# =============================================================================
# CONTENIDOS METABÓLICOS DE LA BANDA IZQUIERDA
# =============================================================================

