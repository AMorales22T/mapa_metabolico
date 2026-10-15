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

def construir_banda_izquierda():
    """Genera las rutas, estructuras y esquemas anatómicos de la banda izquierda (X in [-760, 0])."""
    p = ['<g id="ampliacion_tematica_izquierda">']

    # -------------------------------------------------------------------------
    # VÍA 18: DIGESTIÓN Y ABSORCIÓN DE LÍPIDOS DIETARIOS
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_digestion_lipidos" class="ruta-metabolica">')
    p.append(encabezado_via(-710, 480, 18, "DIGESTIÓN Y TRANSPORTE DE LÍPIDOS DIETARIOS", "Luz intestinal • Emulsión micelar • Enterocito • Linfa quilífera", color="#0d9488"))

    # Micela mixta y lipasa pancreática
    p.append(ea.esquema_micela_mixta(cx=-520, cy=610, radio=66))
    
    p.append("""
    <g id="rx_lipasa_pancreatica" transform="translate(-360, 560)">
      <rect x="0" y="0" width="260" height="92" rx="8" fill="#f0fdfa" stroke="#0d9488" stroke-width="2"/>
      <text x="130" y="22" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f766e" text-anchor="middle">LIPASA PANCREÁTICA</text>
      <text x="130" y="38" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#134e4a" text-anchor="middle">EC 3.1.1.3 + Colipasa</text>
      <line x1="15" y1="46" x2="245" y2="46" stroke="#ccfbf1" stroke-width="1.5"/>
      <text x="130" y="64" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">TAG + 2 H₂O ➔</text>
      <text x="130" y="80" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#ea580c" text-anchor="middle">2-MAG + 2 Ácidos Grasos</text>
    </g>
    """)

    # Enterocito anatómico
    p.append(ea.esquema_enterocito(x=-690, y=720, w=620, h=360))

    # Quilomicrón naciente
    p.append(ea.esquema_lipoproteina(cx=-480, cy=1170, radio=66, tipo="QUILOMICRÓN", apoproteina="ApoB-48", color_apo="#dc2626"))
    
    # Canal linfático hacia el torrente vascular continuo (Y=350)
    p.append("""
    <g id="drenaje_linfatico_a_sangre">
      <path d="M -410 1170 C -150 1170, -70 560, -70 418" fill="none" stroke="#16a34a" stroke-width="3.5" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
      <rect x="-240" y="445" width="150" height="34" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
      <text x="-165" y="461" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#15803d" text-anchor="middle">CONDUCTO TORÁCICO</text>
      <text x="-165" y="473" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#166534" text-anchor="middle">Drenaje linfático ➔ Sangre</text>
    </g>
    """)
    p.append('</g>')

    # -------------------------------------------------------------------------
    # VÍA 19: TEJIDO ADIPOSO (CASCADA LIPOLÍTICA COMPLETA CON ESTRUCTURAS)
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_tejido_adiposo" class="ruta-metabolica">')
    p.append(encabezado_via(-710, 1290, 19, "TEJIDO ADIPOSO: CASCADA LIPOLÍTICA COMPLETA", "Gota lipídica • ATGL ➔ HSL ➔ MGL con estructuras químicas completas", color="#ea580c"))

    # Contenedor del adipocito
    p.append("""
    <g transform="translate(-690, 1340)">
      <!-- Membrana celular adipocitaria -->
      <rect x="0" y="0" width="620" height="960" rx="16" fill="#fffbeb" stroke="#d97706" stroke-width="3" opacity="0.95"/>
      <text x="310" y="30" font-family="'Inter', sans-serif" font-size="13.5" font-weight="900" fill="#78350f" text-anchor="middle">ADIPOCITO UNILOCULAR: GOTA LIPÍDICA Y LIPÓLISIS SECUENCIAL</text>
      
      <!-- Control hormonal nítido -->
      <g transform="translate(30, 45)">
        <rect x="0" y="0" width="260" height="38" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
        <text x="130" y="17" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#15803d" text-anchor="middle">[+ INSULINA]</text>
        <text x="130" y="30" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#166534" text-anchor="middle">↑ Síntesis TAG / Inhibe ATGL y HSL</text>
      </g>
      <g transform="translate(330, 45)">
        <rect x="0" y="0" width="260" height="38" rx="6" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>
        <text x="130" y="17" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#b91c1c" text-anchor="middle">[+ GLUCAGÓN / ADRENALINA]</text>
        <text x="130" y="30" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#991b1b" text-anchor="middle">PKA fosforila Perilipina-1 (PLIN1) y HSL</text>
      </g>
    </g>
    """)

    # PASO 1: TRIACILGLICEROL ➔ ATGL ➔ DAG + 1º AG
    p.append(nodo_libre(-660, 1450, "Triacilglicerol de Reserva", "TAG", ea.TRIACILGLICEROL, "m_adipo_tag", dx=190, dy=20, detalle="Almacenado en gota lipídica con PLIN1"))
    p.append(reaccion_flecha(-520, 1560, 60, "ATGL (Lipasa Adiposa de TAG)", entra="+ H₂O", sale="+ 1º AG libre", ec="EC 3.1.1.3 (+ CGI-58)", color="#ea580c", id_rx="rx_atgl"))

    # PASO 2: 1,2-DIACILGLICEROL ➔ HSL ➔ 2-MAG + 2º AG
    p.append(nodo_libre(-660, 1670, "1,2-Diacilglicerol (DAG)", "DAG", ea.DIACILGLICEROL, "m_adipo_dag", dx=190, dy=20, detalle="Sustrato de HSL fosforilada por PKA"))
    p.append(reaccion_flecha(-520, 1780, 60, "HSL (Lipasa Sensible a Hormonas)", entra="+ H₂O", sale="+ 2º AG libre", ec="EC 3.1.1.79 (PKA / Glucagón)", color="#ea580c", id_rx="rx_hsl"))

    # PASO 3: 2-MONOACILGLICEROL ➔ MGL ➔ GLICEROL LIBRE + 3º AG
    p.append(nodo_libre(-660, 1890, "2-Monoacilglicerol (2-MAG)", "MAG", ea.MONOACILGLICEROL_2, "m_adipo_mag", dx=190, dy=20, detalle="Sustrato final de MGL citosólica"))
    p.append(reaccion_flecha(-520, 2000, 60, "MGL (Monoacilglicerol Lipasa)", entra="+ H₂O", sale="+ 3º AG libre", ec="EC 3.1.1.23", color="#ea580c", id_rx="rx_mgl"))

    # PRODUCTO FINAL: GLICEROL LIBRE
    p.append(nodo_libre(-660, 2110, "Glicerol Libre", "3C", ea.GLICEROL_ESTRUCTURA, "m_adipo_glicerol", dx=190, dy=20, detalle="El adipocito carece de Glicerol Quinasa"))

    # =========================================================================
    # CONEXIONES VASCULARES Y COLECTORES CON LÍNEAS Y FLECHAS PUNTEADAS (0 SOLAPAMIENTOS)
    # =========================================================================
    p.append("""
    <!-- 1. POOL COLECTOR DE LOS 3 ÁCIDOS GRASOS LIBRES -->
    <g id="colector_3ag_adipocito">
      <!-- Convergencia de los 3 cortes enzimáticos (ATGL, HSL, MGL) hacia el Pool con flechas punteadas -->
      <path d="M -580 1590 C -450 1590, -360 1700, -280 1700" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>
      <path d="M -580 1810 C -450 1810, -360 1726, -280 1726" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>
      <path d="M -580 2030 C -450 2030, -360 1750, -280 1750" fill="none" stroke="#ea580c" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowOrange)"/>

      <!-- Caja del Pool de 3 AG libres -->
      <rect x="-280" y="1680" width="190" height="92" rx="10" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
      <text x="-185" y="1703" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" text-anchor="middle">POOL: 3 AG LIBRES</text>
      <text x="-185" y="1720" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#ea580c" text-anchor="middle">3 (R-COO⁻) de ATGL/HSL/MGL</text>
      <line x1="-270" y1="1728" x2="-100" y2="1728" stroke="#fed7aa" stroke-width="1"/>
      <text x="-185" y="1744" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#0f172a" text-anchor="middle">Transportador CD36 / FATP</text>
      <text x="-185" y="1760" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#64748b" text-anchor="middle">+ Albúmina Sérica en Sangre</text>
    </g>

    <!-- Salida y transporte vascular de 3 AG + Albúmina con línea y flechas punteadas ascendentes -->
    <g id="salida_vascular_adipocito">
      <path d="M -90 1726 L -40 1726 L -40 425" fill="none" stroke="#ea580c" stroke-width="2.8" stroke-dasharray="8 5" marker-end="url(#arrowOrange)"/>
      <g transform="translate(-40, 1080)">
        <rect x="-85" y="-14" width="170" height="28" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1.6"/>
        <text x="0" y="4" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#c2410c" text-anchor="middle">3 AG + Albúmina ➔ Sangre</text>
      </g>
    </g>

    <!-- 2. COLECTOR Y SALIDA DE GLICEROL LIBRE POR AQUAPORINA-7 -->
    <g id="colector_glicerol_adipocito">
      <!-- Flecha punteada desde la molécula de Glicerol hacia el colector -->
      <path d="M -340 2120 L -280 2120" fill="none" stroke="#0284c7" stroke-width="2" stroke-dasharray="6 4" marker-end="url(#arrowBlue)"/>

      <!-- Caja de salida de Glicerol -->
      <rect x="-280" y="2080" width="190" height="80" rx="10" fill="#f0f9ff" stroke="#0284c7" stroke-width="2"/>
      <text x="-185" y="2102" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0369a1" text-anchor="middle">GLICEROL LIBRE</text>
      <text x="-185" y="2118" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0284c7" text-anchor="middle">El adipocito carece de GK</text>
      <line x1="-270" y1="2126" x2="-100" y2="2126" stroke="#bae6fd" stroke-width="1"/>
      <text x="-185" y="2142" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#0f172a" text-anchor="middle">Aquaporina-7 (AQP7)</text>
      <text x="-185" y="2154" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#64748b" text-anchor="middle">➔ Sangre a Hígado (GNG)</text>
    </g>

    <!-- Salida y transporte vascular de Glicerol con línea y flechas punteadas ascendentes -->
    <g id="salida_vascular_glicerol">
      <path d="M -90 2120 L -15 2120 L -15 425" fill="none" stroke="#0284c7" stroke-width="2.6" stroke-dasharray="8 5" marker-end="url(#arrowBlue)"/>
      <g transform="translate(-15, 1220)">
        <rect x="-80" y="-14" width="160" height="28" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.6"/>
        <text x="0" y="4" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#0369a1" text-anchor="middle">Glicerol ➔ Hígado (GNG)</text>
      </g>
    </g>
    """)
    p.append('</g>')

    # -------------------------------------------------------------------------
    # VÍA 20: MÚSCULO ESQUELÉTICO Y SARCÓMERO EN CONTRACCIÓN (CORI Y CAHILL)
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_musculo_esqueletico" class="ruta-metabolica">')
    p.append(encabezado_via(-710, 2350, 20, "MÚSCULO ESQUELÉTICO: SARCÓMERO EN CONTRACCIÓN", "Anatomía de la miofibrilla estriada • Ciclo de Cori (Lactato) • Cahill (Alanina)", color="#9f1239"))

    # Sarcómero anatómico detallado en contracción
    p.append(ea.esquema_sarcómero_muscular(cx=-380, cy=2520, w=620, h=270))

    # Flujo bioquímico muscular anaerobio acoplado a la contracción
    p.append("""
    <g transform="translate(-690, 2690)">
      <rect x="0" y="0" width="620" height="180" rx="10" fill="#fff1f2" stroke="#9f1239" stroke-width="2"/>
      
      <!-- Panel Cori -->
      <g transform="translate(30, 20)">
        <rect x="0" y="0" width="260" height="90" rx="8" fill="#ffffff" stroke="#e11d48" stroke-width="1.8"/>
        <text x="130" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#be123c" text-anchor="middle">ACOPLAMIENTO CORI (LACTATO)</text>
        <text x="130" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">Glucógeno ➔ Piruvato ➔ Lactato</text>
        <text x="130" y="66" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#059669" text-anchor="middle">LDH-M: Regenera NAD⁺ (+2 ATP)</text>
      </g>
      
      <!-- Panel Cahill -->
      <g transform="translate(330, 20)">
        <rect x="0" y="0" width="260" height="90" rx="8" fill="#ffffff" stroke="#059669" stroke-width="1.8"/>
        <text x="130" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#047857" text-anchor="middle">ACOPLAMIENTO CAHILL (ALANINA)</text>
        <text x="130" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">Piruvato + BCAA ➔ L-Alanina</text>
        <text x="130" y="66" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#0d9488" text-anchor="middle">ALT muscular / Exporta nitrógeno</text>
      </g>

      <!-- Recaptación hepática -->
      <text x="310" y="135" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#881337" text-anchor="middle">➔ Lactato y Alanina viajan por sangre al hepatocito central (Gluconeogénesis y Urea)</text>
      <text x="310" y="155" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#64748b" text-anchor="middle">Permite sostener la contracción anaerobia máxima sin acidificar el sarcoplasma</text>
    </g>
    """)
    p.append('</g>')

    # -------------------------------------------------------------------------
    # VÍA 21: CEREBRO Y SISTEMA NERVIOSO (DIBUJO ANATÓMICO DIDÁCTICO)
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_cerebro_combustibles" class="ruta-metabolica">')
    p.append(encabezado_via(-710, 2920, 21, "CEREBRO Y SISTEMA NERVIOSO: BHE Y NEURONA", "Anatomía del encéfalo • Neurona mielinizada • GLUT1/3 • Cuerpos cetónicos", color="#2563eb"))

    # Dibujo anatómico del cerebro, cerebelo y neurona mielinizada
    p.append(ea.esquema_cerebro_y_neurona_didactico(x=-690, y=2970, w=620, h=420))
    p.append('</g>')

    p.append("</g>")
    return "\n".join(p)


# =============================================================================
# CONTENIDOS METABÓLICOS DE LA BANDA DERECHA
# =============================================================================

def construir_banda_derecha():
    """Genera las rutas, estructuras y esquemas anatómicos de la banda derecha (X in [5800, 6560])."""
    p = ['<g id="ampliacion_tematica_derecha">']

    # -------------------------------------------------------------------------
    # VÍA 22: CASCADA DE LIPOPROTEÍNAS PLASMÁTICAS Y TRANSPORTE REVERSO
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_lipoproteinas" class="ruta-metabolica">')
    p.append(encabezado_via(5850, 480, 22, "LIPOPROTEÍNAS PLASMÁTICAS Y TRANSPORTE REVERSO", "VLDL ➔ IDL ➔ LDL (LDLR) • HDL y Transporte Reverso de Colesterol (SR-B1)", color="#2563eb"))

    p.append(ea.esquema_lipoproteina(cx=6020, cy=610, radio=66, tipo="VLDL HEPÁTICA", apoproteina="ApoB-100", color_apo="#dc2626"))
    p.append(ea.esquema_lipoproteina(cx=6380, cy=610, radio=58, tipo="LDL (COLESTEROL)", apoproteina="ApoB-100", color_apo="#dc2626"))

    p.append("""
    <g id="rx_lpl_lh" transform="translate(6120, 560)">
      <path d="M -30 50 L 50 50" fill="none" stroke="#2563eb" stroke-width="3" marker-end="url(#arrowBlue)"/>
      <rect x="-10" y="10" width="80" height="30" rx="5" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
      <text x="30" y="28" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#1d4ed8" text-anchor="middle">LPL + LH</text>
      <text x="30" y="66" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#64748b" text-anchor="middle">Pérdida TAG</text>
    </g>
    """)

    # Endocitosis de LDL mediada por Receptor (LDLR)
    p.append("""
    <g id="rx_ldlr_endocitosis" transform="translate(5860, 720)">
      <rect x="0" y="0" width="650" height="145" rx="10" fill="#f8fafc" stroke="#2563eb" stroke-width="2"/>
      <text x="325" y="26" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#1d4ed8" text-anchor="middle">ENDOCITOSIS DE LDL MEDIADA POR RECEPTOR (LDLR)</text>
      <text x="325" y="50" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">1. ApoB-100 se une al Receptor LDLR en fositas recubiertas de clatrina</text>
      <text x="325" y="72" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">2. Degradación lisosómica: Libera Colesterol Libre Intracelular</text>
      <line x1="30" y1="84" x2="620" y2="84" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="325" y="104" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" text-anchor="middle">Efecto del Colesterol Libre Intracelular:</text>
      <text x="325" y="126" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">↓ HMG-CoA Reductasa  |  ↓ Síntesis LDLR (SREBP-2)  |  ↑ ACAT (Ésteres de colesterilo)</text>
    </g>
    """)

    # HDL y Transporte Reverso de Colesterol
    p.append(ea.esquema_lipoproteina(cx=6020, cy=970, radio=52, tipo="HDL MADURA", apoproteina="ApoA-I", color_apo="#059669"))
    
    p.append("""
    <g id="rx_transporte_reverso_hdl" transform="translate(6120, 900)">
      <rect x="0" y="0" width="390" height="140" rx="10" fill="#f0fdf4" stroke="#059669" stroke-width="2"/>
      <text x="195" y="26" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#047857" text-anchor="middle">TRANSPORTE REVERSO DE COLESTEROL (HDL)</text>
      <text x="195" y="50" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#0f172a" text-anchor="middle">1. ApoA-I capta colesterol periférico vía ABCA1 / ABCG1</text>
      <text x="195" y="72" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#059669" text-anchor="middle">2. LCAT (activada por ApoA-I) esterifica el colesterol hacia el núcleo</text>
      <text x="195" y="94" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#0f172a" text-anchor="middle">3. Captación selectiva hepática mediante Receptor SR-B1</text>
      <text x="195" y="118" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#047857" text-anchor="middle">➔ Excreción hepática como Sales Biliares en bilis</text>
    </g>
    """)
    p.append('</g>')

    # -------------------------------------------------------------------------
    # VÍA 23: BIOSÍNTESIS DE TRIACILGLICEROLES Y FOSFOLÍPIDOS DE MEMBRANA
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_sintesis_tag_fosfolipidos" class="ruta-metabolica">')
    p.append(encabezado_via(5850, 1130, 23, "BIOSÍNTESIS DE TRIACILGLICEROLES Y FOSFOLÍPIDOS", "Vía de Kennedy • Glicerol-3-P ➔ LPA ➔ PA ➔ DAG ➔ TAG / Fosfolípidos de Bicapa", color="#7c3aed"))

    p.append(nodo_libre(5880, 1240, "Glicerol-3-Fosfato", "3C", ea.GLICEROL_ESTRUCTURA, "m_der_g3p", dx=140, dy=20, detalle="Desde DHAP o Glicerol libre"))
    p.append(reaccion_flecha(6020, 1350, 70, "GPAT (Glicerol-3-P Aciltransferasa)", entra="+ Acil-CoA", sale="+ CoASH", ec="EC 2.3.1.15", color="#7c3aed", id_rx="rx_gpat"))
    
    p.append(nodo_libre(5880, 1450, "Lisofosfatidato (LPA)", "1-Acil", ea.LISOFOSFATIDATO, "m_der_lpa", dx=190, dy=20, detalle="Intermediario monoacilado"))
    p.append(reaccion_flecha(6020, 1570, 70, "AGPAT (Acilglicerol-P Aciltransferasa)", entra="+ Acil-CoA", sale="+ CoASH", ec="EC 2.3.1.51", color="#7c3aed", id_rx="rx_agpat"))

    p.append(nodo_libre(5880, 1670, "ÁCIDO FOSFATÍDICO (PA)", "1,2-Diacil-3-P", ea.ACIDO_FOSFATIDICO, "m_der_pa", dx=190, dy=20, detalle="PUNTO DE BIFURCACIÓN CENTRAL"))
    p.append(reaccion_flecha(6020, 1790, 70, "PAP (Fosfatidato Fosfatasa / Lipina-1)", entra="+ H₂O", sale="+ Pi", ec="EC 3.1.3.4", color="#7c3aed", id_rx="rx_pap"))

    p.append(nodo_libre(5880, 1890, "1,2-Diacilglicerol (DAG)", "DAG", ea.DIACILGLICEROL, "m_der_dag", dx=190, dy=20, detalle="Precursor de TAG y Fosfolípidos"))

    # Bifurcación TAG / Fosfolípidos
    p.append("""
    <g transform="translate(6020, 2010)">
      <path d="M -40 0 C -120 40, -140 70, -140 100" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowOrange)"/>
      <rect x="-240" y="30" width="150" height="40" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1.8"/>
      <text x="-165" y="48" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#c2410c" text-anchor="middle">DGAT + Acil-CoA</text>
      <text x="-165" y="62" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#ea580c" text-anchor="middle">EC 2.3.1.20</text>

      <path d="M 40 0 C 70 40, 100 70, 100 100" fill="none" stroke="#0284c7" stroke-width="3" marker-end="url(#arrowBlue)"/>
      <rect x="135" y="30" width="160" height="40" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.8"/>
      <text x="215" y="48" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0369a1" text-anchor="middle">CPT + CDP-Colina</text>
      <text x="215" y="62" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#0284c7" text-anchor="middle">Vía de Kennedy (Bicapas)</text>
    </g>
    """)

    p.append(nodo_libre(5850, 2150, "Triacilglicerol (TAG)", "Reserva", ea.TRIACILGLICEROL, "m_der_tag_reserva", dx=190, dy=20, detalle="Almacenamiento energético en gotas"))
    p.append(nodo_libre(6220, 2150, "Fosfatidilcolina (PC)", "Membrana", ea.FOSFATIDILCOLINA, "m_der_pc_membrana", dx=175, dy=20, detalle="Fosfolípido mayoritario de bicapas"))
    p.append('</g>')

    # -------------------------------------------------------------------------
    # VÍA 24: BIOSÍNTESIS DE AMINOÁCIDOS NO ESENCIALES
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_biosintesis_aminoacidos" class="ruta-metabolica">')
    p.append(encabezado_via(5850, 2350, 24, "BIOSÍNTESIS DE AMINOÁCIDOS NO ESENCIALES", "Esqueletos centrales de Glucólisis y Krebs ➔ Transaminación (PLP)", color="#059669"))

    # Piruvato a Alanina
    p.append(nodo_libre(5880, 2430, "Piruvato (Glucólisis)", "3C", eaa.PIRUVATO_AMINO, "m_aa_pyr", dx=140, dy=20, detalle="Esqueleto cetoácido"))
    p.append(reaccion_flecha(6020, 2525, 55, "ALT (Alanina Aminotransferasa)", entra="+ Glutamato", sale="+ α-KG", ec="EC 2.6.1.2 (PLP)", color="#059669", reversible=True, id_rx="rx_alt_amino"))
    p.append(nodo_libre(5880, 2600, "L-Alanina", "3C", eaa.ALANINA, "m_aa_ala", dx=140, dy=20, detalle="Transaminación directa"))

    # Oxalacetato a Aspartato y Asparagina
    p.append(nodo_libre(6220, 2430, "Oxalacetato (Krebs)", "4C", eaa.OXALACETATO_AMINO, "m_aa_oaa", dx=140, dy=20, detalle="Cetoácido dicarboxílico"))
    p.append(reaccion_flecha(6360, 2565, 55, "AST (Aspartato Aminotransferasa)", entra="+ Glu", sale="+ α-KG", ec="EC 2.6.1.1 (PLP)", color="#059669", reversible=True, curvas_side="right", text_dx=-14, text_anchor="end", id_rx="rx_ast_amino"))
    p.append(nodo_libre(6220, 2640, "L-Aspartato", "4C", eaa.ASPARTATO_AMINO, "m_aa_asp", dx=140, dy=20, detalle="Donador de N en Urea"))
    p.append(reaccion_flecha(6360, 2775, 55, "Asparagina Sintetasa", entra="+ Gln + ATP", sale="+ Glu + AMP + PPi", ec="EC 6.3.5.4", color="#059669", curvas_side="right", text_dx=-14, text_anchor="end", id_rx="rx_asn_sintetasa"))
    p.append(nodo_libre(6220, 2850, "L-Asparagina", "4C", ea.L_ASPARAGINA, "m_aa_asn", dx=140, dy=20, detalle="Amida neutra"))

    # α-Cetoglutarato a Glutamato, Glutamina y Prolina
    p.append(nodo_libre(5880, 2715, "α-Cetoglutarato (Krebs)", "5C", eaa.ALFA_CETOGLUTARATO, "m_aa_akg", dx=140, dy=20, detalle="Colector común de nitrógeno"))
    p.append(reaccion_flecha(6020, 2870, 55, "GDH (Glutamato DH)", entra="+ NH₄⁺ + NADPH", sale="+ NADP⁺", ec="EC 1.4.1.3", color="#059669", reversible=True, id_rx="rx_gdh_amino"))
    p.append(nodo_libre(5880, 2945, "L-Glutamato", "5C", eaa.GLUTAMATO, "m_aa_glu", dx=140, dy=20, detalle="Aminoácido central del metabolismo"))
    
    p.append("""
    <g id="rx_gln_sintetasa" transform="translate(6020, 3080)">
      <path d="M 0 0 L 0 50" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>
      <text x="14" y="26" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a">Glutamina Sintetasa (+ NH₄⁺, ATP)</text>
    </g>
    """)
    p.append(nodo_libre(5880, 3150, "L-Glutamina", "5C", eaa.GLUTAMINA, "m_aa_gln", dx=140, dy=20, detalle="Transporte no tóxico de amonio"))
    p.append(nodo_libre(6220, 3150, "L-Prolina", "5C", ea.L_PROLINA, "m_aa_pro", dx=140, dy=20, detalle="Iminoácido cíclico"))

    # 3-Fosfoglicerato a Serina, Glicina y Cisteína
    p.append(nodo_libre(5880, 3300, "3-Fosfoglicerato (Glucólisis)", "3C-P", ea.GLICEROL_ESTRUCTURA, "m_aa_3pg", dx=140, dy=20, detalle="Vía de biosíntesis de serina"))
    p.append(reaccion_flecha(6020, 3410, 55, "Vía de Fosfoserina (3 pasos)", entra="+ NAD⁺ + Glu", sale="+ NADH + α-KG + Pi", ec="PHGDH / PSAT / PSP", color="#059669", id_rx="rx_via_serina"))
    p.append(nodo_libre(5880, 3485, "L-Serina", "3C", ea.L_SERINA, "m_aa_ser", dx=140, dy=20, detalle="Precursor de Gly, Cys y Esfingolípidos"))

    p.append(reaccion_flecha(6020, 3610, 55, "SHMT (Serina Hidroximetiltransferasa)", entra="+ THF", sale="+ N⁵,N¹⁰-CH₂-THF", ec="EC 2.1.2.1 (PLP)", color="#059669", reversible=True, id_rx="rx_shmt"))
    p.append(nodo_libre(5880, 3685, "Glicina", "2C", ea.L_GLICINA, "m_aa_gly", dx=140, dy=20, detalle="Hemo • Purinas • Glutatión"))
    p.append(nodo_libre(6220, 3685, "L-Cisteína", "3C", ea.L_CISTEINA, "m_aa_cys", dx=140, dy=20, detalle="Azufre derivado de Metionina"))

    # Fenilalanina a Tirosina
    p.append(nodo_libre(5880, 3840, "L-Fenilalanina (Esencial)", "9C", eda.FENILALANINA, "m_aa_phe", dx=140, dy=20, detalle="Aminoácido aromático dietario"))
    p.append(reaccion_flecha(6020, 4005, 55, "PAH (Fenilalanina Hidroxilasa)", entra="+ O₂ + BH₄", sale="+ BH₂ + H₂O", ec="EC 1.14.16.1", color="#059669", id_rx="rx_pah"))
    p.append(nodo_libre(5880, 4080, "L-Tirosina", "9C", eda.TIROSINA, "m_aa_tyr", dx=140, dy=20, detalle="Precursor de Catecolaminas y Melanina"))
    p.append('</g>')

    # -------------------------------------------------------------------------
    # VÍA 25: CONMUTADOR VISUAL DE ESTADOS METABÓLICOS Y HORMONALES
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_conmutador_estados" class="ruta-metabolica">')
    p.append(encabezado_via(5850, 4270, 25, "INTEGRACIÓN POR ESTADOS METABÓLICOS Y HORMONALES", "Conmutador de flujos energéticos • Posprandial vs Ayuno vs Ejercicio", color="#ea580c"))

    p.append("""
    <g transform="translate(5860, 4330)">
      <rect x="0" y="0" width="650" height="540" rx="12" fill="#fffbeb" stroke="#d97706" stroke-width="2.5"/>
      <text x="325" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#92400e" text-anchor="middle">CONMUTADOR DE FLUJOS ENERGÉTICOS INTERTISULARES</text>

      <g transform="translate(25, 55)">
        <rect x="0" y="0" width="290" height="140" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
        <text x="145" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">ESTADO POSPRANDIAL (INSULINA ↑)</text>
        <text x="145" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Hígado: Glucógeno ↑ + Lipogénesis ↑</text>
        <text x="145" y="68" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Adipocito: GLUT-4 ↑ + Síntesis TAG ↑</text>
        <text x="145" y="90" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Músculo: Glucógeno ↑ + Síntesis proteica ↑</text>
        <line x1="20" y1="102" x2="270" y2="102" stroke="#bbf7d0" stroke-width="1.5"/>
        <text x="145" y="122" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#166534" text-anchor="middle">ALMACENAMIENTO Y ANABOLISMO</text>
      </g>

      <g transform="translate(335, 55)">
        <rect x="0" y="0" width="290" height="140" rx="8" fill="#ffffff" stroke="#ea580c" stroke-width="2"/>
        <text x="145" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#c2410c" text-anchor="middle">AYUNO TEMPRANO (GLUCAGÓN ↑)</text>
        <text x="145" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Hígado: Glucogenólisis ↑ + GNG ↑</text>
        <text x="145" y="68" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Adipocito: Lipólisis masiva (ATGL/HSL)</text>
        <text x="145" y="90" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Músculo: β-Oxidación de AG (ahorra glucosa)</text>
        <line x1="20" y1="102" x2="270" y2="102" stroke="#fed7aa" stroke-width="1.5"/>
        <text x="145" y="122" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#9a3412" text-anchor="middle">MANTENIMIENTO DE LA NORMOGLUCEMIA</text>
      </g>

      <g transform="translate(25, 215)">
        <rect x="0" y="0" width="290" height="140" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="2"/>
        <text x="145" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#6d28d9" text-anchor="middle">AYUNO PROLONGADO (CETONAS ↑)</text>
        <text x="145" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Hígado: Cetogénesis acelerada</text>
        <text x="145" y="68" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Cerebro: Consume β-Hidroxibutirato (60%)</text>
        <text x="145" y="90" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Proteólisis muscular: Disminuye marcadamente</text>
        <line x1="20" y1="102" x2="270" y2="102" stroke="#ddd6fe" stroke-width="1.5"/>
        <text x="145" y="122" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#5b21b6" text-anchor="middle">PRESERVACIÓN DE LA MASA MUSCULAR</text>
      </g>

      <g transform="translate(335, 215)">
        <rect x="0" y="0" width="290" height="140" rx="8" fill="#ffffff" stroke="#dc2626" stroke-width="2"/>
        <text x="145" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#b91c1c" text-anchor="middle">EJERCICIO VIGOROSO (AMPK ↑)</text>
        <text x="145" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Músculo: Glucógeno local ➔ + ATP rápido</text>
        <text x="145" y="68" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Glucólisis anaerobia: Genera Lactato</text>
        <text x="145" y="90" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Ciclo de Cori: Lactato ➔ Hígado ➔ Glucosa</text>
        <line x1="20" y1="102" x2="270" y2="102" stroke="#fecaca" stroke-width="1.5"/>
        <text x="145" y="122" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#991b1b" text-anchor="middle">REGENERACIÓN CONTINUA DE NAD⁺</text>
      </g>

      <g transform="translate(25, 375)">
        <rect x="0" y="0" width="600" height="145" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="1.8"/>
        <text x="300" y="26" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#b45309" text-anchor="middle">LEYENDA DE FLUJOS DE COMBUSTIBLE INTERTISULAR</text>
        <text x="300" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">• Glucosa: Cerebro (obligatorio) • Eritrocitos (exclusivo) • Músculo/Hígado (almacén)</text>
        <text x="300" y="74" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">• Ácidos Grasos + Albúmina: Músculo y Miocardio en reposo • Hígado en ayuno</text>
        <text x="300" y="96" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">• Cuerpos Cetónicos: Riñón, Músculo y Adaptación Cerebral durante el ayuno</text>
        <text x="300" y="124" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#047857" text-anchor="middle">El Hígado actúa como el órgano amortiguador y distribuidor central del organismo</text>
      </g>
    </g>
    """)
    p.append('</g>')

    p.append("</g>")
    return "\n".join(p)


# =============================================================================
# REESTRUCTURACIÓN DE LA LEYENDA INSTITUCIONAL CENTRAL
# =============================================================================

def actualizar_bloque_leyenda_central(inner_svg):
    """
    Modifica el bloque de leyenda del mapa original para:
    1. Distribuir las 25 vías metabólicas en 3 columnas perfectamente equilibradas:
       - Columna 1 (X=40): Vías 1 a 8
       - Columna 2 (X=630): Vías 9 a 16
       - Columna 3 (X=1220): Vías 17 a 25
       Todas alineadas exactamente en la misma cota vertical (Y=100, y=-12).
    2. Cambiar 'CÓDIGO DE COLORES EDITORIAL:' a 'CÓDIGO DE COLORES:'.
    """
    # 1. Cambiar el título de la columna 4
    inner_svg = inner_svg.replace("CÓDIGO DE COLORES EDITORIAL:", "CÓDIGO DE COLORES:")

    vias_todas_col1 = [
        {"n": 1, "nombre": "Glucólisis", "resumen": "Glucosa → 2 Piruvato (+2 ATP, +2 NADH)", "color": "#0284c7"},
        {"n": 2, "nombre": "Gluconeogénesis", "resumen": "Piruvato → Glucosa (4 enzimas clave · hepática)", "color": "#7c3aed"},
        {"n": 3, "nombre": "Glucógeno (Síntesis y lisis)", "resumen": "Glucogenogénesis & Glucogenólisis citosólica", "color": "#b45309"},
        {"n": 4, "nombre": "Vía de las pentosas fosfato", "resumen": "G6P → NADPH + Ribosa-5-P (Fase ox. y no ox.)", "color": "#059669"},
        {"n": 5, "nombre": "Complejo PDH (Piruvato DH)", "resumen": "Piruvato → Acetil-CoA + CO₂ + NADH", "color": "#ea580c"},
        {"n": 6, "nombre": "Ciclo de Krebs (TCA)", "resumen": "Acetil-CoA → 2 CO₂ + 3 NADH + FADH₂ + GTP", "color": "#c2410c"},
        {"n": 7, "nombre": "Cadena Respiratoria & ATPsint", "resumen": "Fosforilación oxidativa (gradiente de H⁺)", "color": "#16a34a"},
        {"n": 8, "nombre": "Lanzaderas (Malato/G3P)", "resumen": "Reoxidación de NADH citosólico hacia la MMI", "color": "#0284c7"},
    ]

    vias_todas_col2 = [
        {"n": 9, "nombre": "β-oxidación (y carnitina)", "resumen": "Palmitoil-CoA → 8 Acetil-CoA + FADH₂ + NADH", "color": "#b45309"},
        {"n": 10, "nombre": "Lipogénesis (FAS)", "resumen": "Acetil-CoA → Malonil-CoA → Palmitato (FAS)", "color": "#0d9488"},
        {"n": 11, "nombre": "Cetogénesis", "resumen": "Acetil-CoA → Acetoacetato y β-Hidroxibutirato", "color": "#be123c"},
        {"n": 12, "nombre": "Síntesis de colesterol", "resumen": "Acetil-CoA → HMG-CoA → Mevalonato → Colesterol", "color": "#4f46e5"},
        {"n": "12B", "nombre": "Destinos esqueletos carbonados", "resumen": "Convergencia de los 20 AA en intermediarios", "color": "#2563eb"},
        {"n": 13, "nombre": "Transaminación y desaminación", "resumen": "Recogida de amino en Glutamato → NH₄⁺", "color": "#2563eb"},
        {"n": 14, "nombre": "Ciclo de la urea", "resumen": "NH₄⁺ + HCO₃⁻ + Aspartato → Urea (hepático)", "color": "#0891b2"},
        {"n": 15, "nombre": "Biosíntesis de nucleótidos", "resumen": "Purinas y Pirimidinas de novo / Salvamento", "color": "#0284c7"},
        {"n": 16, "nombre": "Catabolismo de nucleótidos", "resumen": "Purinas → Ácido Úrico (XOD); Pirimidinas → β-Ala", "color": "#475569"},
    ]

    vias_todas_col3 = [
        {"n": 17, "nombre": "Ciclo de Cori (Músculo ⇄ Hígado)", "resumen": "Lactato muscular anaeróbico ⇄ Glucosa hepática", "color": "#9f1239"},
        {"n": 18, "nombre": "Digestión de lípidos", "resumen": "Micela mixta → Enterocito → Quilomicrón → Linfa", "color": "#0d9488"},
        {"n": 19, "nombre": "Tejido adiposo (lipólisis)", "resumen": "TAG → ATGL/HSL/MGL → 3 AG + Glicerol", "color": "#ea580c"},
        {"n": 20, "nombre": "Músculo esquelético y sarcómero", "resumen": "Contracción de actomiosina; Cori & Cahill", "color": "#9f1239"},
        {"n": 21, "nombre": "Cerebro y combustibles neuronales", "resumen": "Glucosa (GLUT1/3) & adaptación a cetonas (MCT)", "color": "#2563eb"},
        {"n": 22, "nombre": "Lipoproteínas plasmáticas", "resumen": "VLDL → IDL → LDL (ApoB100) y HDL (SR-B1)", "color": "#2563eb"},
        {"n": 23, "nombre": "Biosíntesis de TAG y fosfolípidos", "resumen": "G3P → LPA → PA → DAG → TAG / Fosfolípidos", "color": "#7c3aed"},
        {"n": 24, "nombre": "Biosíntesis de AA no esenciales", "resumen": "Ala, Ser, Gly, Cys, Asp, Asn, Glu, Gln, Pro, Tyr", "color": "#059669"},
        {"n": 25, "nombre": "Integración y conmutador", "resumen": "Flujos de combustible: Posprandial vs Ayuno", "color": "#ea580c"},
    ]

    def render_col(items, x_offset, titulo):
        svg_items = []
        for i, v in enumerate(items):
            y_pos = i * 38
            nom = v['nombre'].replace('&', '&amp;')
            res = v['resumen'][:50].replace('&', '&amp;')
            svg_items.append(f'''
            <g id="badge_leyenda_{v['n']}" class="badge-via" data-via="{v['n']}" transform="translate(0, {y_pos})" style="cursor: pointer;">
              <circle cx="11" cy="0" r="9" fill="{v['color']}"/>
              <text x="11" y="3.5" fill="#ffffff" font-size="8.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{v['n']}</text>
              <text x="26" y="3" fill="#0f172a" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">{nom}</text>
              <text x="26" y="15" fill="#64748b" font-size="8.5" font-family="'Inter', sans-serif">{res}</text>
            </g>''')
        return f'''
        <g transform="translate({x_offset}, 100)">
          <text x="0" y="-12" fill="#0284c7" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">{titulo}</text>
          {''.join(svg_items)}
        </g>'''

    col1_svg = render_col(vias_todas_col1, 40, "VÍAS METABÓLICAS (1–8):")
    col2_svg = render_col(vias_todas_col2, 630, "VÍAS METABÓLICAS (9–16):")
    col3_svg = render_col(vias_todas_col3, 1220, "VÍAS DE INTEGRACIÓN Y ÓRGANOS (17–25):")

    bloque_3_cols = f"""
      <!-- 3 Columnas equilibradas de Vías (1 a 25) alineadas exactamente a Y=100 -->
      {col1_svg}
      {col2_svg}
      {col3_svg}
    """

    # Reemplazar desde el inicio de las columnas de vías hasta la línea divisoria de X=1840
    patron_reemplazo = r'<!-- Columnas 1 y 2: Vías.*?<line x1="1840"'
    if re.search(patron_reemplazo, inner_svg, re.DOTALL):
        inner_svg = re.sub(patron_reemplazo, bloque_3_cols + '\n      <line x1="1840"', inner_svg, count=1, flags=re.DOTALL)

    return inner_svg


# =============================================================================
# ENSAMBLAJE FINAL DEL PÓSTER VECTORIAL COMPLETO
# =============================================================================

def ensamblar_mapa_ampliado():
    print(f"1. Leyendo mapa central original: {RUTA_ORIGINAL_HTML}")
    with open(RUTA_ORIGINAL_HTML, "r", encoding="utf-8") as f:
        html_orig = f.read()

    svg_start = html_orig.find("<svg")
    if svg_start == -1:
        raise ValueError("No se encontró la etiqueta <svg en el archivo original")
    svg_tag_end = html_orig.find(">", svg_start) + 1
    svg_close = html_orig.rfind("</svg>")
    inner_svg_orig = html_orig[svg_tag_end:svg_close]

    print(f"   ✓ Mapa original extraído ({len(inner_svg_orig):,} caracteres)")

    # Actualizar la leyenda central para incluir las nuevas vías y 'CÓDIGO DE COLORES:'
    inner_svg_orig = actualizar_bloque_leyenda_central(inner_svg_orig)
    print("   ✓ Leyenda institucional actualizada con Vías 18–25 y rótulo corregido")

    css_fonts = cargar_fuentes_base64()

    W_CANVAS = 7320
    H_CANVAS = 5490
    VB_X = -760
    VB_Y = -250

    fondo_izq = construir_fondo_izquierdo()
    fondo_der = construir_fondo_derecho()
    banda_izq = construir_banda_izquierda()
    banda_der = construir_banda_derecha()

    svg_final = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W_CANVAS}" height="{H_CANVAS}" viewBox="{VB_X} {VB_Y} {W_CANVAS} {H_CANVAS}">
    <style>
      {css_fonts}
      text {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
    <defs>
      <linearGradient id="print_gradPlasma" x1="0" y1="350" x2="0" y2="431.5" gradientUnits="userSpaceOnUse">
        <stop offset="0%" stop-color="#450a0a" stop-opacity="0.95"/>
        <stop offset="65%" stop-color="#7f1d1d" stop-opacity="0.9"/>
        <stop offset="100%" stop-color="#991b1b" stop-opacity="0.85"/>
      </linearGradient>

      <marker id="arrowOrange" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
        <path d="M0,0 L9,4.5 L0,9 Z" fill="#ea580c"/>
      </marker>
      <marker id="arrowTeal" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
        <path d="M0,0 L9,4.5 L0,9 Z" fill="#0d9488"/>
      </marker>
    </defs>

    <!-- 1. Fondo base del lienzo completo -->
    <g id="print_fondo_base">
      <rect x="{VB_X}" y="{VB_Y}" width="{W_CANVAS}" height="{H_CANVAS}" fill="#f1f5f9" />
    </g>

    <!-- 2. Extensiones laterales biológicas continuas (con torrente vascular a Y=350..418) -->
    {fondo_izq}
    {fondo_der}

    <!-- 3. Contenido íntegro del mapa central original con leyenda actualizada -->
    {inner_svg_orig}

    <!-- 4. Contenidos de ampliación temática en las bandas laterales -->
    {banda_izq}
    {banda_der}

    <!-- 5. Marco perimetral institucional -->
    <g id="print_marco">
      <rect x="-710" y="-200" width="7220" height="5390" rx="14" fill="none" stroke="#0284c7" stroke-width="4.2" />
      <rect x="-703" y="-193" width="7206" height="5376" rx="10" fill="none" stroke="#0d9488" stroke-width="2.4" />
      <rect x="-697" y="-187" width="7194" height="5364" rx="7" fill="none" stroke="#10b981" stroke-width="1.4" />
    </g>

    <!-- 6. Banda superior de cabecera institucional -->
    <g id="print_cabecera">
      <rect x="-710" y="-200" width="7220" height="198" fill="#f8fafc" opacity="0.98" />
      <text x="2900" y="-105" fill="#0f172a" font-size="68" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="4" text-anchor="middle">MAPA METABÓLICO INTEGRADO · VERSIÓN AMPLIADA</text>
      <text x="2900" y="-45" fill="#475569" font-size="17" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Metabolismo Central • Digestión y Transporte Lipídico • Tejido Adiposo • Acoplamiento Muscular • Lipoproteínas • Biosíntesis de Fosfolípidos y Aminoácidos</text>
    </g>

    <!-- 7. Pie de página del póster (1200 x 900 mm) -->
    <g id="print_pie_poster">
      <rect x="-710" y="5130" width="7220" height="95" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" rx="8" />
      <text x="-670" y="5185" fill="#0f172a" font-size="15" font-weight="900" font-family="'Inter', sans-serif">MAPA METABÓLICO INTEGRADO UNIVERSITARIO</text>
      <text x="-670" y="5208" fill="#64748b" font-size="12" font-weight="700" font-family="'Inter', sans-serif">Formato Póster Científico Imprimible: 1200 × 900 mm (Proporción 4:3) • Resolución Ultra-HD Vectorial</text>
      <text x="6450" y="5195" fill="#64748b" font-size="12" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">Bioquímica Humana • Medicina y Ciencias Biomédicas</text>
    </g>
</svg>"""

    print(f"2. Escribiendo SVG ampliado en: {RUTA_OUT_SVG}")
    with open(RUTA_OUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_final)

    print("3. Generando visor interactivo enriquecido de 25 vías...")
    html_final = construir_html_mapa_ampliado(svg_final, W_CANVAS, H_CANVAS, VB_X, VB_Y)

    print(f"   Escribiendo HTML visor interactivo en: {RUTA_OUT_HTML}")
    with open(RUTA_OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_final)

    # Guardar copias directas en versiones_html/
    ruta_copia_html1 = os.path.join(DIR_HTML, "mapa_cartulina_ampliado.html")
    ruta_copia_html2 = os.path.join(DIR_HTML, "mapa_ampliado_interactivo.html")
    ruta_copia_html_num = os.path.join(DIR_HTML, "01_mapa_ampliado_completo_25_vias.html")
    with open(ruta_copia_html1, "w", encoding="utf-8") as f:
        f.write(html_final)
    with open(ruta_copia_html2, "w", encoding="utf-8") as f:
        f.write(html_final)
    with open(ruta_copia_html_num, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"   ✓ Copias interactivas guardadas en:")
    print(f"     - {ruta_copia_html_num} (Entregable principal numerado)")
    print(f"     - {ruta_copia_html1}")
    print(f"     - {ruta_copia_html2}")

    # Exportación con rsvg-convert a PDF y PNG
    rsvg = shutil.which("rsvg-convert")
    if rsvg:
        print("4. Generando PDF imprimible vectorial 1200 × 900 mm con rsvg-convert...")
        cmd_pdf = [
            rsvg, "-f", "pdf",
            "--page-width", "1200mm",
            "--page-height", "900mm",
            "-o", RUTA_OUT_PDF,
            RUTA_OUT_SVG
        ]
        subprocess.run(cmd_pdf, check=True)
        print(f"   ✓ PDF vectorial generado con éxito: {RUTA_OUT_PDF}")

        # Copia de seguridad en versiones_impresion/
        shutil.copy2(RUTA_OUT_PDF, RUTA_COPIA_PDF)
        ruta_copia_pdf_num = os.path.join(DIR_IMPRESION, "01_mapa_ampliado_completo_120x90cm.pdf")
        shutil.copy2(RUTA_OUT_PDF, ruta_copia_pdf_num)
        print(f"   ✓ Copias guardadas en:")
        print(f"     - {ruta_copia_pdf_num} (Entregable principal PDF)")
        print(f"     - {RUTA_COPIA_PDF}")

        print("5. Generando vista previa PNG en alta resolución (2400 × 1800 px)...")
        cmd_png = [
            rsvg,
            "-w", "2400",
            "-h", "1800",
            "-o", RUTA_OUT_PNG,
            RUTA_OUT_SVG
        ]
        subprocess.run(cmd_png, check=True)
        print(f"   ✓ Vista previa PNG generada con éxito: {RUTA_OUT_PNG}")
    else:
        print("   ⚠ rsvg-convert no encontrado en el sistema; solo se crearon SVG y HTML.")

    print("\n=======================================================")
    print("¡AMPLIACIÓN DEL TEMARIO GENERADA EXITOSAMENTE!")
    print("=======================================================")


if __name__ == "__main__":
    ensamblar_mapa_ampliado()
