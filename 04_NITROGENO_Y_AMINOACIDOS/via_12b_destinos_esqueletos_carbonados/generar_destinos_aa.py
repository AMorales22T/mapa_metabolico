#!/usr/bin/env python3
"""
GENERADOR VECTORIAL EDITORIAL: DESTINOS DE LOS ESQUELETOS CARBONADOS DE AMINOÁCIDOS
==================================================================================
Diseño editorial biológico de alta fidelidad:
- CERO rectángulos artificiales ni cajas envolventes.
- CERO puntos negros para carbonos (conteo expresado en texto claro [xC]).
- Entorno bicompartimental continuo: Citosol vs. Matriz Mitocondrial con doble membrana ondulada.
- Convergencia exacta de los 20 aminoácidos en 7 intermediarios metabólicos centrales.
- Información clínica y cofactores reducida en insignias orgánicas ancladas a diana:
  * ⚠ PKU (PAH / BH4)
  * ⚠ Alcaptonuria (HGD)
  * ⚠ Tirosinemia I (FAH)
  * ⚠ MSUD (BCKDH)
  * ⚠ Homocistinuria (CBS / PLP)
  * ⚠ Acidemia Metilmalónica (MCM / Vit B12)
  * ⚡ PLP, ⚡ Biotina, ⚡ TPP
"""

import os
import sys

DIR_ACTUAL = os.path.dirname(os.path.abspath(__file__))
sys.path.append(DIR_ACTUAL)

from estructuras_destinos_aa import (
    PIRUVATO,
    ACETIL_COA,
    ACETOACETIL_COA,
    ALFACETOGLUTARATO,
    SUCCINIL_COA,
    FUMARATO,
    OXALACETATO,
    FENILALANINA,
    TIROSINA,
    PROPIONIL_COA,
    HOMOCISTEINA,
    L_GLUTAMATO,
    L_ASPARTATO
)
from entorno_destinos_aa import DEFS_ENTORNO_DESTINOS_AA, generar_entorno_destinos_aa_svg

ANCHO_CANVAS = 1920
ALTO_CANVAS = 2240
Y_MEMBRANA = 560

# =============================================================================
# 1. PLANTILLA BASE HTML
# =============================================================================
CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Destinos de los Esqueletos Carbonados de Aminoácidos</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #0f172a;
      color: #0f172a;
      padding: 30px 15px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .lienzo-svg {{
      width: {ANCHO_CANVAS}px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 16px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.35);
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
    svg text {{ stroke: none; }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        {DEFS_ENTORNO_DESTINOS_AA}
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

# =============================================================================
# 2. COMPONENTES VISUALES ORGÁNICOS
# =============================================================================

def crear_nodo_aa(x, y, nombre, carbonos, clasificacion="glu", detalle=""):
    """
    Rótulo tipográfico orgánico para aminoácidos sin cajas contenedoras ni puntos de carbono.
    """
    colores = {
        "glu": {"dot": "#16a34a", "txt": "#14532d"},
        "ceto": {"dot": "#dc2626", "txt": "#881337"},
        "mixto": {"dot": "#9333ea", "txt": "#581c87"}
    }
    cfg = colores.get(clasificacion, colores["glu"])
    detalle_svg = f'<text x="0" y="27" fill="#64748b" font-size="9" font-weight="600" font-family="\'Inter\', sans-serif">{detalle}</text>' if detalle else ""

    return f"""
    <!-- AA: {nombre} -->
    <g transform="translate({x}, {y})">
      <circle cx="-10" cy="-4" r="4.5" fill="{cfg['dot']}" />
      <text x="0" y="0" fill="{cfg['txt']}" font-size="13.5" font-weight="800" font-family="'Inter', sans-serif">{nombre}</text>
      <text x="0" y="15" fill="#ea580c" font-size="10.5" font-weight="800" font-family="'JetBrains Mono', monospace">[{carbonos}]</text>
      {detalle_svg}
    </g>
    """

def crear_metabolito_hub(x, y, nombre, carbonos, detalle="", svg_estructura="", offset_texto_x=0, offset_texto_y=-35, color_titulo="#0f172a"):
    """
    Bloque vectorial de intermediario con estructura SVG flotante libre.
    """
    return f"""
    <!-- Hub: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="translate({offset_texto_x}, {offset_texto_y})">
        <text x="0" y="0" fill="{color_titulo}" font-size="15" font-weight="900" font-family="'Inter', sans-serif">{nombre}</text>
        <text x="0" y="16" fill="#ea580c" font-size="11" font-weight="800" font-family="'JetBrains Mono', monospace">[{carbonos}]</text>
        <text x="0" y="30" fill="#64748b" font-size="9.5" font-weight="600" font-family="'Inter', sans-serif">{detalle}</text>
      </g>
      <g transform="translate(0, 0)">
        {svg_estructura}
      </g>
    </g>
    """

def crear_badge_clinico(x, y, texto, es_alerta=True, rx=11):
    """
    Píldora reducida para patologías o cofactores anclada a diana.
    """
    fill = "#fee2e2" if es_alerta else "#e0e7ff"
    stroke = "#dc2626" if es_alerta else "#4f46e5"
    txt_col = "#991b1b" if es_alerta else "#312e81"
    ancho = max(len(texto) * 6.8 + 20, 95)

    return f"""
    <!-- Badge: {texto} -->
    <g transform="translate({x}, {y})">
      <rect x="0" y="0" width="{ancho}" height="22" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.2" opacity="0.95"/>
      <text x="{ancho/2}" y="15" fill="{txt_col}" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">{texto}</text>
    </g>
    """

def crear_enzima(x, y, nombre, ec="", cofactor=""):
    """
    Texto jerárquico limpio para la enzima sin cajas ni fondos.
    """
    ec_txt = f'<text x="0" y="13" fill="#64748b" font-size="8.5" font-weight="700" font-family="\'JetBrains Mono\', monospace">{ec}</text>' if ec else ""
    cof_txt = f'<text x="0" y="25" fill="#0284c7" font-size="9" font-weight="800" font-family="\'Inter\', sans-serif">{cofactor}</text>' if cofactor else ""

    return f"""
    <!-- Enzima: {nombre} -->
    <g transform="translate({x}, {y})">
      <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif">{nombre}</text>
      {ec_txt}
      {cof_txt}
    </g>
    """

# =============================================================================
# 3. ENSAMBLAJE DE TODAS LAS VÍAS Y RUTAS
# =============================================================================
def construir_destinos_aa_svg():
    p = []

    # 1. Fondo biológico bicompartimental
    p.append(generar_entorno_destinos_aa_svg(ancho=ANCHO_CANVAS, alto=ALTO_CANVAS, y_membrana=Y_MEMBRANA))

    # Título General Editorial
    p.append("""
    <g transform="translate(60, 48)">
      <text x="0" y="0" fill="#0f172a" font-size="25" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="-0.5">DESTINOS DE LOS ESQUELETOS CARBONADOS DE AMINOÁCIDOS</text>
      <text x="0" y="22" fill="#64748b" font-size="12" font-weight="600" font-family="'Inter', sans-serif">Convergencia anaplerótica y oxidativa de los 20 aminoácidos estándar en 7 puntos de entrada metabólicos</text>
    </g>
    """)

    # -------------------------------------------------------------------------
    # COLUMNA 1 (X=60 a 420): CONVERGENCIA A PIRUVATO [3C] Y OXALACETATO [4C]
    # -------------------------------------------------------------------------
    # Aminoácidos en Citosol
    p.append(crear_nodo_aa(60, 140, "L-Alanina", "3C", "glu", "Transaminación directa (ALT)"))
    p.append(crear_nodo_aa(60, 190, "L-Serina", "3C", "glu", "Deshidratación a Piruvato"))
    p.append(crear_nodo_aa(60, 240, "Glicina", "2C", "glu", "Conversión a Serina (SHMT)"))

    p.append(crear_nodo_aa(230, 140, "L-Cisteína", "3C", "glu", "Desulfuración a Piruvato"))
    p.append(crear_nodo_aa(230, 190, "L-Treonina", "4C", "mixto", "Escisión aldólica a Glicina"))
    p.append(crear_nodo_aa(230, 240, "L-Triptófano", "11C", "mixto", "Vía quinurenina libera Ala"))

    # Enzimas y Cofactores para Piruvato en Citosol
    p.append(crear_enzima(60, 310, "ALT (Alanina Aminotransferasa)", "EC 2.6.1.2", "Transaminación citosólica"))
    p.append(crear_badge_clinico(60, 345, "⚡ PLP (Vitamina B6)", es_alerta=False))
    p.append(crear_enzima(60, 385, "SDH (Serina Deshidratasa)", "EC 4.2.1.22", "- NH₄⁺ hacia piruvato"))

    # Flecha hacia el MPC por el pasillo derecho libre en X=340
    p.append("""
    <g id="flechas_piruvato">
      <path d="M 330 280 L 330 520 Q 330 545 225 545" fill="none" stroke="#16a34a" stroke-width="2.5" marker-end="url(#arrowGreenAA)"/>
    </g>
    """)

    # Cruce MPC descendente a Piruvato en Matriz
    p.append("""
    <path d="M 210 585 L 210 650" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowAmberAA)"/>
    """)

    # HUB 1: PIRUVATO [3C] en Matriz Mitocondrial (X=175, Y=700)
    p.append(crear_metabolito_hub(
        x=175, y=700,
        nombre="PIRUVATO",
        carbonos="3C",
        detalle="Entrada a Acetil-CoA o Carboxilación a OAA",
        svg_estructura=PIRUVATO,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#b45309"
    ))

    # Piruvato -> Acetil-CoA (en matriz hacia la derecha)
    p.append("""
    <path d="M 250 740 L 430 740" fill="none" stroke="#d97706" stroke-width="2.4" marker-end="url(#arrowAmberAA)"/>
    <text x="340" y="730" fill="#9a3412" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Complejo PDH (E1-E2-E3)</text>
    """)

    # Piruvato -> Oxalacetato (hacia abajo en matriz)
    p.append("""
    <path d="M 210 790 L 210 900" fill="none" stroke="#059669" stroke-width="2.4" marker-end="url(#arrowGreenAA)"/>
    <text x="225" y="850" fill="#047857" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">Piruvato Carboxilasa (⚡ Biotina / ATP)</text>
    """)

    # HUB 7: OXALACETATO [4C] en Matriz Mitocondrial (X=175, Y=960)
    p.append(crear_metabolito_hub(
        x=175, y=960,
        nombre="OXALACETATO",
        carbonos="4C",
        detalle="Reinicio del Ciclo de Krebs / Gluconeogénesis",
        svg_estructura=OXALACETATO,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#5b21b6"
    ))

    # Entrada de Asparagina y Aspartato hacia Oxalacetato
    p.append(crear_nodo_aa(60, 1100, "L-Asparagina", "4C", "glu", "Asparaginasa ➔ Aspartato"))
    p.append(crear_nodo_aa(60, 1160, "L-Aspartato", "4C", "glu", "Transaminación directa (AST)"))
    p.append(crear_enzima(60, 1220, "AST (Aspartato Aminotransferasa)", "EC 2.6.1.1", "⚡ PLP (B6)"))
    p.append("""
    <path d="M 235 1140 L 235 1060" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowGreenAA)"/>
    """)

    # Estructura química de L-Aspartato (X=60, Y=1330)
    p.append(crear_metabolito_hub(
        x=60, y=1330,
        nombre="L-Aspartato",
        carbonos="4C",
        detalle="Donador de nitrógeno en ciclo de la urea",
        svg_estructura=L_ASPARTATO,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#047857"
    ))

    # -------------------------------------------------------------------------
    # COLUMNA 2 (X=460 a 900): FENILALANINA, TIROSINA, CETOGÉNICOS Y FUMARATO
    # -------------------------------------------------------------------------
    # Aminoácidos Cetogénicos en Citosol
    p.append(crear_nodo_aa(470, 140, "L-Leucina", "6C", "ceto", "Cetogénico puro (Acetoacetato + Acetil-CoA)"))
    p.append(crear_nodo_aa(720, 140, "L-Lisina", "6C", "ceto", "Cetogénico puro (Vía sacaropina)"))

    # L-Fenilalanina y L-Tirosina en Citosol
    p.append(crear_metabolito_hub(
        x=470, y=240,
        nombre="L-Fenilalanina",
        carbonos="9C",
        detalle="Aminoácido esencial aromático",
        svg_estructura=FENILALANINA,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#7e22ce"
    ))

    # PAH enzima y conversión Phe -> Tyr
    p.append("""
    <path d="M 560 320 L 710 320" fill="none" stroke="#9333ea" stroke-width="2.5" marker-end="url(#arrowPurpleAA)"/>
    """)
    p.append(crear_enzima(580, 265, "Fenilalanina hidroxilasa (PAH)", "EC 1.14.16.1", "⚡ Tetrahidrobiopterina (BH₄)"))
    p.append(crear_badge_clinico(570, 340, "⚠ PKU: Fenilcetonuria (Déficit PAH o BH₄)", es_alerta=True))

    p.append(crear_metabolito_hub(
        x=730, y=240,
        nombre="L-Tirosina",
        carbonos="9C",
        detalle="Precursor de catecolaminas y melanina",
        svg_estructura=TIROSINA,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#7e22ce"
    ))

    # Paso de Tirosina a Homogentisato en Citosol
    p.append("""
    <path d="M 775 425 L 775 460" fill="none" stroke="#9333ea" stroke-width="2.2" marker-end="url(#arrowPurpleAA)"/>
    """)
    p.append(crear_enzima(800, 420, "Homogentisato 1,2-dioxigenasa (HGD)", "EC 1.13.11.5", "Apertura de anillo"))
    p.append(crear_badge_clinico(800, 455, "⚠ Alcaptonuria (Ocronosis y orina oscura)", es_alerta=True))

    # Escisión terminal hacia Matriz Mitocondrial
    p.append("""
    <path d="M 775 500 L 775 540" fill="none" stroke="#9333ea" stroke-width="2.4" marker-end="url(#arrowPurpleAA)"/>
    """)
    p.append(crear_enzima(815, 645, "Fumarilacetoacetasa (FAH)", "EC 3.7.1.2", "Escisión hidrolítica terminal"))
    p.append(crear_badge_clinico(815, 675, "⚠ Tirosinemia I (FAH)", es_alerta=True))

    # HUBS CETOGÉNICOS EN MATRIZ:
    # HUB 2: ACETIL-CoA [2C] (X=460, Y=700)
    p.append(crear_metabolito_hub(
        x=460, y=700,
        nombre="ACETIL-CoA",
        carbonos="2C",
        detalle="Combustible de condensación con OAA",
        svg_estructura=ACETIL_COA,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#854d0e"
    ))

    # HUB 3: ACETOACETIL-CoA [4C] (X=460, Y=940)
    p.append(crear_metabolito_hub(
        x=460, y=940,
        nombre="ACETOACETIL-CoA",
        carbonos="4C",
        detalle="Cuerpo cetónico activado",
        svg_estructura=ACETOACETIL_COA,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#9f1239"
    ))

    # Conexión Tiolasa
    p.append("""
    <path d="M 490 770 L 490 840" fill="none" stroke="#e11d48" stroke-width="2.4" marker-end="url(#arrowRubyAA)"/>
    <text x="515" y="805" fill="#be123c" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">Tiolasa (2 Acetil-CoA ⇌ AcAc-CoA)</text>
    """)

    # HUB 6: FUMARATO [4C] en Matriz Mitocondrial (X=720, Y=1120)
    p.append(crear_metabolito_hub(
        x=720, y=1120,
        nombre="FUMARATO",
        carbonos="4C (Trans)",
        detalle="Punto de convergencia de Phe, Tyr y Ciclo de la Urea",
        svg_estructura=FUMARATO,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#5b21b6"
    ))

    # Flecha escisión Phe/Tyr hacia Fumarato y Acetoacetato
    p.append("""
    <!-- Hacia Fumarato -->
    <path d="M 775 670 L 775 1060" fill="none" stroke="#9333ea" stroke-width="2.2" stroke-dasharray="5 4" marker-end="url(#arrowPurpleAA)"/>
    <text x="785" y="860" fill="#7e22ce" font-size="9.5" font-weight="700" font-family="'Inter', sans-serif">Fumarato libre ➔</text>
    <!-- Hacia Acetoacetato -->
    <path d="M 760 670 Q 710 880 670 930" fill="none" stroke="#9333ea" stroke-width="2.2" stroke-dasharray="5 4" marker-end="url(#arrowPurpleAA)"/>
    """)

    # -------------------------------------------------------------------------
    # COLUMNA 3 (X=1040 a 1480): METIONINA, RAMIFICADOS Y SUCCINIL-CoA
    # -------------------------------------------------------------------------
    # Metionina y Treonina en Citosol
    p.append(crear_nodo_aa(1040, 140, "L-Metionina", "5C", "glu", "Donador metilo universal (SAM)"))
    p.append(crear_nodo_aa(1040, 195, "L-Treonina", "4C", "mixto", "Vía α-cetobutirato a Propionato"))

    # Homocisteína en Citosol
    p.append(crear_metabolito_hub(
        x=1040, y=270,
        nombre="L-Homocisteína",
        carbonos="4C",
        detalle="Cruce de transulfuración vs. remetilación",
        svg_estructura=HOMOCISTEINA,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#b45309"
    ))

    # CBS enzima y patología de Homocistinuria
    p.append("""
    <path d="M 1075 410 L 1095 410" fill="none" stroke="#059669" stroke-width="2.4" marker-end="url(#arrowGreenAA)"/>
    """)
    p.append(crear_enzima(1135, 390, "Cistationina β-sintasa (CBS)", "EC 4.2.1.22", "⚡ PLP (Vitamina B6)"))
    p.append(crear_badge_clinico(1135, 425, "⚠ Homocistinuria (CBS / B6)", es_alerta=True))

    # BCAA: Valina e Isoleucina
    p.append(crear_nodo_aa(1320, 140, "L-Valina", "5C", "glu", "BCAA ramificado glucogénico"))
    p.append(crear_nodo_aa(1320, 195, "L-Isoleucina", "6C", "mixto", "BCAA ramificado glucogénico/cetogénico"))

    # Cruce MMI y Complejo BCKDH en Matriz
    p.append("""
    <path d="M 1360 230 L 1360 600" fill="none" stroke="#059669" stroke-width="2.5" marker-end="url(#arrowGreenAA)"/>
    """)
    p.append(crear_enzima(1300, 625, "Complejo BCKDH (α-Cetoácido DH ramificada)", "EC 1.2.4.4", "⚡ TPP, Lipoato, CoA, FAD, NAD⁺"))
    p.append(crear_badge_clinico(1300, 665, "⚠ MSUD: Jarabe de Arce (Bloqueo BCAA)", es_alerta=True))

    # HUB: PROPIONIL-CoA [3C] en Matriz Mitocondrial (X=1040, Y=680)
    p.append(crear_metabolito_hub(
        x=1040, y=680,
        nombre="PROPIONIL-CoA",
        carbonos="3C",
        detalle="Metabolito común de Met, Thr, Val, Ile y ac. grasos impares",
        svg_estructura=PROPIONIL_COA,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#c2410c"
    ))

    # Flechas convergentes a Propionil-CoA
    p.append("""
    <path d="M 1075 460 L 1075 625" fill="none" stroke="#059669" stroke-width="2.4" marker-end="url(#arrowGreenAA)"/>
    <path d="M 1300 680 Q 1230 710 1180 710" fill="none" stroke="#059669" stroke-width="2.4" marker-end="url(#arrowGreenAA)"/>
    """)

    # Carboxilación dependiente de Biotina (PCC)
    p.append("""
    <path d="M 1110 750 L 1110 830" fill="none" stroke="#d97706" stroke-width="2.5" marker-end="url(#arrowAmberAA)"/>
    """)
    p.append(crear_enzima(1160, 760, "Propionil-CoA Carboxilasa (PCC)", "EC 6.4.1.3", "ATP + HCO₃⁻ ➔ Metilmalonil-CoA"))
    p.append(crear_badge_clinico(1160, 795, "⚡ Biotina (Vitamina B7)", es_alerta=False))

    # Metilmalonil-CoA Mutasa (Dependiente de Vitamina B12)
    p.append(crear_enzima(1160, 860, "Metilmalonil-CoA Mutasa (MCM)", "EC 5.4.99.2", "Isomerización intramolecular"))
    p.append(crear_badge_clinico(1160, 895, "⚠ Acidemia Metilmalónica (Déficit MCM o Vit B12)", es_alerta=True))

    # HUB 5: SUCCINIL-CoA [4C] en Matriz Mitocondrial (X=1040, Y=1040)
    p.append(crear_metabolito_hub(
        x=1040, y=1040,
        nombre="SUCCINIL-CoA",
        carbonos="4C",
        detalle="Intermediario anaplerótico clave del Ciclo de Krebs",
        svg_estructura=SUCCINIL_COA,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#5b21b6"
    ))

    # Flecha final hacia Succinil-CoA
    p.append("""
    <path d="M 1110 920 L 1110 980" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowKrebsAA)"/>
    """)

    # -------------------------------------------------------------------------
    # COLUMNA 4 (X=1500 a 1900): FAMILIA DEL GLUTAMATO Y α-CETOGLUTARATO [5C]
    # -------------------------------------------------------------------------
    # Familia del Glutamato en Citosol
    p.append(crear_nodo_aa(1500, 140, "L-Glutamina", "5C", "glu", "Glutaminasa (GLS) ➔ Glu + NH₄⁺"))
    p.append(crear_nodo_aa(1500, 190, "L-Prolina", "5C", "glu", "Prolina oxidasa ➔ semialdehído"))
    p.append(crear_nodo_aa(1500, 240, "L-Arginina", "6C", "glu", "Ciclo Urea ➔ Ornitina ➔ Glutamato"))
    p.append(crear_nodo_aa(1500, 290, "L-Histidina", "6C", "glu", "Histidasa ➔ FIGLU ➔ Glutamato"))

    # L-Glutamato [5C] en Citosol
    p.append(crear_metabolito_hub(
        x=1720, y=240,
        nombre="L-Glutamato",
        carbonos="5C",
        detalle="Concentrador universal de nitrógeno",
        svg_estructura=L_GLUTAMATO,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#059669"
    ))

    # Flechas hacia L-Glutamato en Citosol
    p.append("""
    <path d="M 1640 215 L 1700 240" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreenAA)"/>
    """)

    # Translocación por transportador hacia la Matriz Mitocondrial
    p.append("""
    <path d="M 1750 400 L 1750 670" fill="none" stroke="#059669" stroke-width="2.5" marker-end="url(#arrowGreenAA)"/>
    """)
    p.append(crear_enzima(1765, 630, "GDH (Glutamato DH)", "EC 1.4.1.2", "NAD(P)⁺ + H₂O ➔ NADH + NH₄⁺"))

    # HUB 4: α-CETOGLUTARATO [5C] en Matriz Mitocondrial (X=1720, Y=730)
    p.append(crear_metabolito_hub(
        x=1720, y=730,
        nombre="α-CETOGLUTARATO",
        carbonos="5C",
        detalle="Cetoácido del Ciclo de Krebs",
        svg_estructura=ALFACETOGLUTARATO,
        offset_texto_x=0, offset_texto_y=-35,
        color_titulo="#5b21b6"
    ))

    # -------------------------------------------------------------------------
    # INTEGRACIÓN ANAPLERÓTICA: ÓRBITA DEL CICLO DE KREBS ENTRE LOS 4 INTERMEDIARIOS
    # Oxalacetato (X=175, Y=960) -> α-KG (X=1720, Y=730) -> Succinil-CoA (X=1040, Y=1040) -> Fumarato (X=720, Y=1120) -> Oxalacetato
    # -------------------------------------------------------------------------
    p.append("""
    <!-- Conectores inter-Krebs tenues (Guía anaplerótica orbital) -->
    <g opacity="0.38" stroke="#7c3aed" stroke-width="2.2" stroke-dasharray="6 5" fill="none">
      <!-- Oxalacetato -> a-KG vía Citrato / Isocitrato -->
      <path d="M 230 980 C 320 860 620 780 950 780 T 1700 780" />
      <!-- a-KG -> Succinil-CoA vía a-KGDH -->
      <path d="M 1740 900 C 1700 1020 1400 1060 1160 1060" />
      <!-- Succinil-CoA -> Fumarato vía Succinato DH -->
      <path d="M 1040 1080 C 960 1120 880 1140 820 1140" />
      <!-- Fumarato -> Oxalacetato vía Malato DH -->
      <path d="M 720 1140 C 550 1140 350 1100 240 1040" />
    </g>
    <text x="560" y="860" fill="#7c3aed" font-size="11" font-weight="800" font-family="'Inter', sans-serif" opacity="0.8" text-anchor="middle">↻ ANAPLEROSIS DEL CICLO DE KREBS</text>
    """)

    # -------------------------------------------------------------------------
    # PIE EDITORIAL Y CLASIFICACIÓN DE AMINOÁCIDOS (SIN RECTÁNGULOS)
    # -------------------------------------------------------------------------
    p.append("""
    <g transform="translate(60, 1540)">
      <text x="0" y="0" fill="#0f172a" font-size="13.5" font-weight="900" font-family="'Inter', sans-serif">CLASIFICACIÓN METABÓLICA DE LOS 20 AMINOÁCIDOS:</text>
      
      <circle cx="10" cy="24" r="5" fill="#16a34a"/>
      <text x="25" y="28" fill="#14532d" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">Glucogénicos puros (14 AA):</text>
      <text x="205" y="28" fill="#475569" font-size="11" font-weight="600" font-family="'Inter', sans-serif">Ala, Arg, Asn, Asp, Cys, Glu, Gln, Gly, His, Met, Pro, Ser, Val, Thr (vía propionato)</text>

      <circle cx="10" cy="48" r="5" fill="#dc2626"/>
      <text x="25" y="52" fill="#881337" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">Cetogénicos estrictos (2 AA):</text>
      <text x="225" y="52" fill="#475569" font-size="11" font-weight="600" font-family="'Inter', sans-serif">Leucina y Lisina (rinden exclusivamente Acetil-CoA / Acetoacetil-CoA)</text>

      <circle cx="10" cy="72" r="5" fill="#9333ea"/>
      <text x="25" y="76" fill="#581c87" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">Mixtos (Glucogénicos y Cetogénicos - 5 AA):</text>
      <text x="325" y="76" fill="#475569" font-size="11" font-weight="600" font-family="'Inter', sans-serif">Isoleucina, Fenilalanina, Triptófano, Tirosina, Treonina</text>

      <text x="0" y="110" fill="#64748b" font-size="10.5" font-weight="600" font-family="'Inter', sans-serif">
        Anotaciones diagnósticas: ⚠=Errores congénitos del metabolismo en la enzima causal  |  ⚡=Cofactores vitamínicos obligados (PLP, BH₄, B₁₂, Biotina, TPP)
      </text>
    </g>
    """)

    return "".join(p)

# =============================================================================
# 4. FUNCIÓN PRINCIPAL DE EJECUCIÓN
# =============================================================================
def main():
    contenido_svg = construir_destinos_aa_svg()

    # SVG Completo
    svg_completo = f"""<svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        {DEFS_ENTORNO_DESTINOS_AA}
      </defs>
      {contenido_svg}
    </svg>"""

    ruta_svg = os.path.join(DIR_ACTUAL, "Destinos_Esqueletos_Carbonados.svg")
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_completo)

    # HTML Completo
    html_completo = CABECERA_HTML + contenido_svg + PIE_HTML
    ruta_html = os.path.join(DIR_ACTUAL, "Destinos_Esqueletos_Carbonados.html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html_completo)

    print(f"✅ Archivo SVG generado exitosamente: {ruta_svg}")
    print(f"✅ Archivo HTML generado exitosamente: {ruta_html}")

    # Renderizado PNG de Alta Resolución
    ruta_png = os.path.join(DIR_ACTUAL, "Destinos_Esqueletos_Carbonados_preview.png")
    import subprocess
    try:
        subprocess.run(["rsvg-convert", "-o", ruta_png, ruta_svg], check=True)
        print(f"✅ Archivo PNG Preview generado exitosamente: {ruta_png}")
    except Exception as e:
        print(f"ℹ️ rsvg-convert no disponible o falló: {e}")

if __name__ == "__main__":
    main()
