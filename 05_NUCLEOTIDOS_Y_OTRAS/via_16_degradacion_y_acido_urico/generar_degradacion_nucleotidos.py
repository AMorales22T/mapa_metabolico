#!/usr/bin/env python3
"""
GENERADOR DE LA RUTA DE DEGRADACIÓN DE NUCLEÓTIDOS Y FORMACIÓN DE ÁCIDO ÚRICO
=============================================================================
Lámina vectorizada editorial (SVG / HTML) calibrada con 0 solapamientos:
- Estructuras químicas 2D libres en el espacio sin cajas contenedoras.
- Dihidrouracilo, Dihidrotimina y cadenas abiertas lineales (β-Ureidopropionato y β-Ureidoisobutirato)
  dibujadas con fórmulas químicas vectoriales completas.
- Separación milimétrica de ejes para evitar cualquier colisión texto-flecha o texto-texto.
"""

import os
import subprocess
from estructuras_degradacion import (
    ADENOSINA,
    INOSINA,
    HIPOXANTINA,
    GUANINA,
    XANTINA,
    ACIDO_URICO,
    URACILO,
    TIMINA,
    DIHIDROURACILO,
    DIHIDROTIMINA,
    BETA_UREIDOPROPIONATO,
    BETA_UREIDOISOBUTIRATO,
    BETA_ALANINA,
    BETA_AMINOISOBUTIRATO
)
from entorno_degradacion import DEFS_ENTORNO_DEGRADACION, generar_entorno_degradacion_svg

ANCHO = 1420
ALTO = 2220

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vía 16: Catabolismo de Nucleótidos y Formación de Ácido Úrico</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #e2e8f0;
      color: #0f172a;
      padding: 30px 15px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .lienzo-svg {{
      width: {ANCHO}px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO}" height="{ALTO}" viewBox="0 0 {ANCHO} {ALTO}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Flecha de flujo catabólico de Purinas (Morado / Rubí) -->
        <marker id="arrowFlowDeg" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#9333ea" />
        </marker>
        <!-- Flecha de reactivo / gasto (Rojo) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de salida / subproducto (Gris) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <!-- Flecha de poder reductor / ganancia (Verde) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de agua / amino (Azul) -->
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#2563eb" />
        </marker>

        {DEFS_ENTORNO_DEGRADACION}
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""


def nodo_metabolito(x, y, nombre, formula_c, detalle="", svg_estructura="", text_dx=120, text_dy=25):
    """Metabolito con su estructura química 2D flotando libremente sin cajas."""
    return f"""
    <!-- Metabolito: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="translate(0, 0)">
        {svg_estructura}
      </g>
      <g transform="translate({text_dx}, {text_dy})">
        <text x="0" y="0" fill="#0f172a" font-size="14.5" font-weight="900">{nombre}</text>
        <text x="0" y="16" fill="#9333ea" font-size="11" font-weight="800">{formula_c}</text>
        <text x="0" y="30" fill="#64748b" font-size="9.5" font-weight="600">{detalle}</text>
      </g>
    </g>
    """


def reaccion_vertical(x, y, h, enzima, ec="", clinica="", entra="", sale="", invert_curvas=False):
    """Reacción vertical con curvas compactas que respetan los márgenes."""
    curvas = ""
    if not invert_curvas:
        if entra:
            curvas += f"""
            <path d="M -35 8 Q -15 8 -4 16" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
            <text x="-40" y="11" fill="#dc2626" font-size="9.5" font-weight="800" text-anchor="end">{entra}</text>
            """
        if sale:
            curvas += f"""
            <path d="M -4 24 Q -15 32 -35 32" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
            <text x="-40" y="35" fill="#475569" font-size="9.5" font-weight="800" text-anchor="end">{sale}</text>
            """
        text_trans = "translate(14, 11)"
    else:
        # Curvas hacia la derecha si el margen izquierdo está muy ajustado
        if entra:
            curvas += f"""
            <path d="M 40 8 Q 15 8 4 16" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
            <text x="45" y="11" fill="#dc2626" font-size="9.5" font-weight="800" text-anchor="start">{entra}</text>
            """
        if sale:
            curvas += f"""
            <path d="M 4 24 Q 15 32 40 32" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
            <text x="45" y="35" fill="#475569" font-size="9.5" font-weight="800" text-anchor="start">{sale}</text>
            """
        text_trans = "translate(-14, 11)"

    flecha = f"""
    <line x1="0" y1="0" x2="0" y2="{h}" stroke="#9333ea" stroke-width="2.6" marker-end="url(#arrowFlowDeg)"/>
    """

    clin_svg = ""
    if clinica:
        clin_svg = f'<text x="0" y="24" fill="#be185d" font-size="9" font-family="\'JetBrains Mono\', monospace" font-weight="700">{clinica}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha}
      {curvas}
      <g transform="{text_trans}">
        <text x="0" y="0" fill="#0f172a" font-size="11.5" font-weight="900">{enzima}</text>
        <text x="0" y="12" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        {clin_svg}
      </g>
    </g>
    """


def main():
    svg_elements = []

    # 1. Fondo biológico orgánico
    svg_elements.append(generar_entorno_degradacion_svg(ancho=ANCHO, alto=ALTO))

    # =========================================================================
    # RÓTULO PRINCIPAL Y LEYENDA SUPERIOR
    # =========================================================================
    svg_elements.append("""
    <g transform="translate(60, 45)">
      <circle cx="20" cy="20" r="18" fill="#9333ea" />
      <text x="20" y="26" font-family="'Inter', sans-serif" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle">16</text>
      
      <text x="50" y="17" font-family="'Inter', sans-serif" font-size="20" font-weight="900" fill="#0f172a">CATABOLISMO DE NUCLEÓTIDOS Y FORMACIÓN DE ÁCIDO ÚRICO</text>
      <text x="50" y="34" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#9333ea">Degradación purínica oxidativa hacia Urato vs apertura de pirimidinas a intermediarios hidrosolubles</text>
    </g>
    """)

    # =========================================================================
    # COLUMNA IZQUIERDA: CATABOLISMO DE PURINAS (X=60 a 660)
    # =========================================================================
    svg_elements.append("""
    <!-- Título de sección: Purinas -->
    <g transform="translate(80, 95)">
      <text x="0" y="18" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#7e22ce" letter-spacing="1">CATABOLISMO DE PURINAS (CONVERGENCIA A URATO)</text>
      <line x1="0" y1="26" x2="420" y2="26" stroke="#9333ea" stroke-width="2"/>
    </g>
    """)

    # --- Rama AMP / Adenosina (Eje X=130) ---
    svg_elements.append("""
    <g transform="translate(80, 140)">
      <circle cx="50" cy="12" r="5" fill="#9333ea"/>
      <text x="65" y="16" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a">AMP (Adenilato)</text>
    </g>
    """)
    svg_elements.append(reaccion_vertical(
        x=130, y=170, h=35,
        enzima="5'-Nucleotidasa",
        ec="EC 3.1.3.5",
        clinica="Desfosforila a nucleósido",
        entra="- H₂O",
        sale="+ Pi"
    ))
    svg_elements.append(nodo_metabolito(
        x=70, y=225,
        nombre="Adenosina",
        formula_c="[10C] · Nucleósido de Adenina",
        detalle="Sustrato de desaminación",
        svg_estructura=ADENOSINA,
        text_dx=120, text_dy=55
    ))
    svg_elements.append(reaccion_vertical(
        x=130, y=365, h=40,
        enzima="Adenosina Desaminasa (ADA)",
        ec="EC 3.5.4.4",
        clinica="Déficit: SCID (Inmunodeficiencia)",
        entra="- H₂O",
        sale="+ NH₄⁺"
    ))
    svg_elements.append(nodo_metabolito(
        x=70, y=425,
        nombre="Inosina",
        formula_c="[10C] · Nucleósido de Hipoxantina",
        detalle="Intermediario tras desaminación",
        svg_estructura=INOSINA,
        text_dx=120, text_dy=55
    ))
    svg_elements.append(reaccion_vertical(
        x=130, y=565, h=38,
        enzima="Purina Nucleósido Fosforilasa",
        ec="EC 2.4.2.1 (PNP)",
        clinica="Fosforólisis del enlace beta",
        entra="- Pi",
        sale="+ Ribosa-1-P"
    ))
    svg_elements.append(nodo_metabolito(
        x=70, y=625,
        nombre="Hipoxantina",
        formula_c="[5C] · Base purínica libre",
        detalle="Primer sustrato de XOD",
        svg_estructura=HIPOXANTINA,
        text_dx=120, text_dy=30
    ))

    # --- Rama GMP / Guanina (Eje X=460) ---
    svg_elements.append("""
    <g transform="translate(410, 140)">
      <circle cx="50" cy="12" r="5" fill="#9333ea"/>
      <text x="65" y="16" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a">GMP (Guanilato)</text>
    </g>
    """)
    svg_elements.append(reaccion_vertical(
        x=460, y=170, h=35,
        enzima="5'-Nucleotidasa",
        ec="EC 3.1.3.5",
        clinica="Genera Guanosina libre",
        entra="- H₂O",
        sale="+ Pi"
    ))
    svg_elements.append("""
    <g transform="translate(410, 225)">
      <circle cx="50" cy="12" r="5" fill="#9333ea"/>
      <text x="65" y="16" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a">Guanosina</text>
      <text x="65" y="30" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#9333ea">[10C] · Nucleósido</text>
    </g>
    """)
    svg_elements.append(reaccion_vertical(
        x=460, y=275, h=38,
        enzima="Purina Nucleósido Fosforilasa",
        ec="EC 2.4.2.1 (PNP)",
        clinica="Cliva a Guanina libre",
        entra="- Pi",
        sale="+ Ribosa-1-P"
    ))
    svg_elements.append(nodo_metabolito(
        x=390, y=335,
        nombre="Guanina",
        formula_c="[5C] · Base purínica libre",
        detalle="Sustrato de Guanasa",
        svg_estructura=GUANINA,
        text_dx=120, text_dy=30
    ))
    svg_elements.append(reaccion_vertical(
        x=460, y=475, h=40,
        enzima="Guanasa (Guanina Desaminasa)",
        ec="EC 3.5.4.3",
        clinica="Desaminación a Xantina",
        entra="- H₂O",
        sale="+ NH₄⁺"
    ))

    # --- Convergencia central en XANTINA (Eje X=300) ---
    svg_elements.append("""
    <!-- Conectores convergentes hacia Xantina -->
    <path d="M 130 720 Q 130 775 280 780" fill="none" stroke="#9333ea" stroke-width="2.4" marker-end="url(#arrowFlowDeg)"/>
    <g transform="translate(170, 735)">
      <text x="0" y="0" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a">XOD (Oxidación en C2)</text>
      <text x="0" y="12" font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#dc2626">Diana: Alopurinol / Febuxostat</text>
    </g>

    <path d="M 460 550 Q 430 710 320 780" fill="none" stroke="#9333ea" stroke-width="2.4" marker-end="url(#arrowFlowDeg)"/>
    """)

    # Xantina
    svg_elements.append(nodo_metabolito(
        x=220, y=805,
        nombre="Xantina",
        formula_c="[5C] · 2,6-Dioxipurina",
        detalle="Intermediario común purínico",
        svg_estructura=XANTINA,
        text_dx=130, text_dy=30
    ))

    # Xantina Oxidasa hacia Ácido Úrico
    svg_elements.append(reaccion_vertical(
        x=300, y=945, h=50,
        enzima="Xantina Oxidasa (XOD)",
        ec="EC 1.17.3.2 (Oxidación en C8)",
        clinica="Inhibida por Alopurinol y Febuxostat",
        entra="- H₂O + O₂",
        sale="+ H₂O₂"
    ))

    # Ácido Úrico / Urato
    svg_elements.append(nodo_metabolito(
        x=210, y=1035,
        nombre="Ácido Úrico (Urato)",
        formula_c="[5C] · 2,6,8-Trioxipurina",
        detalle="Producto catabólico final en humanos",
        svg_estructura=ACIDO_URICO,
        text_dx=140, text_dy=30
    ))

    # Sección clínica de hiperuricemia y excreción (sin cajas)
    svg_elements.append("""
    <g transform="translate(80, 1190)">
      <text x="0" y="18" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#be123c">FISIOPATOLOGÍA CLÍNICA: HIPERURICEMIA Y GOTA</text>
      <line x1="0" y1="24" x2="420" y2="24" stroke="#f43f5e" stroke-width="1.8"/>
      <text x="0" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• pKₐ = 5.4 ➔ a pH fisiológico (7.4) circula como ion urato monosódico.</text>
      <text x="0" y="60" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• Límite de solubilidad en plasma: ~6.8 mg/dL (404 µmol/L).</text>
      <text x="0" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• Precipitación en microcristales ➔ Artritis gotosa aguda y tofos.</text>
      <text x="0" y="92" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#e11d48">Tratamiento: Alopurinol / Febuxostat (inhiben XOD) · Uricosúricos</text>
    </g>

    <!-- Transición al túbulo renal -->
    <path d="M 300 1300 L 300 1880" fill="none" stroke="#e11d48" stroke-width="2.2" stroke-dasharray="5 4" marker-end="url(#arrowRed)"/>
    <text x="315" y="1845" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#be123c">Filtración y secreción renal (Transportador URAT1 · Probenecid)</text>
    """)

    # =========================================================================
    # COLUMNA DERECHA: CATABOLISMO DE PIRIMIDINAS (X=720 a 1380)
    # ESTRUCTURAS QUÍMICAS COMPLETAS DIBUJADAS EN CADA PASO
    # =========================================================================
    svg_elements.append("""
    <!-- Título de sección: Pirimidinas -->
    <g transform="translate(740, 95)">
      <text x="0" y="18" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#7e22ce" letter-spacing="1">CATABOLISMO DE PIRIMIDINAS (PRODUCTOS SOLUBLES)</text>
      <line x1="0" y1="26" x2="440" y2="26" stroke="#9333ea" stroke-width="2"/>
    </g>
    """)

    # Paso 1: Bases libres Uracilo y Timina (Y=145)
    svg_elements.append(nodo_metabolito(
        x=720, y=145,
        nombre="Uracilo (de CMP / UMP)",
        formula_c="[4C] · Base libre pirimidínica",
        detalle="Clivaje de citosina y uridina",
        svg_estructura=URACILO,
        text_dx=100, text_dy=15
    ))

    svg_elements.append(nodo_metabolito(
        x=1080, y=145,
        nombre="Timina (de dTMP)",
        formula_c="[5C] · 5-Metiluracilo libre",
        detalle="Recambio de ADN celular",
        svg_estructura=TIMINA,
        text_dx=120, text_dy=15
    ))

    # Reacción 1: DPD (Dihidropirimidina Deshidrogenasa)
    svg_elements.append(reaccion_vertical(
        x=920, y=240, h=45,
        enzima="Dihidropirimidina Deshidrogenasa (DPD)",
        ec="EC 1.3.1.2 (Satura C5=C6)",
        clinica="Déficit: Toxicidad severa por 5-FU",
        entra="- NADPH + H⁺",
        sale="+ NADP⁺"
    ))

    # Paso 2: Intermediarios reducidos DIHIDROURACILO y DIHIDROTIMINA (Y=310)
    svg_elements.append(nodo_metabolito(
        x=720, y=310,
        nombre="Dihidrouracilo",
        formula_c="[4C] · Anillo saturado sin C=C",
        detalle="Intermediario reducido de uracilo",
        svg_estructura=DIHIDROURACILO,
        text_dx=100, text_dy=15
    ))

    svg_elements.append(nodo_metabolito(
        x=1080, y=310,
        nombre="Dihidrotimina",
        formula_c="[5C] · Anillo saturado con metilo",
        detalle="Intermediario reducido de timina",
        svg_estructura=DIHIDROTIMINA,
        text_dx=120, text_dy=15
    ))

    # Reacción 2: Dihidropirimidinasa (Hidrólisis con apertura de anillo)
    svg_elements.append(reaccion_vertical(
        x=920, y=410, h=42,
        enzima="Dihidropirimidinasa",
        ec="EC 3.5.2.2 (Apertura del anillo pirimidínico)",
        clinica="Rompe enlace C4-N3 hidrolíticamente",
        entra="- H₂O"
    ))

    # Paso 3: Cadenas abiertas lineales BETA-UREIDOPROPIONATO y BETA-UREIDOISOBUTIRATO (Y=485)
    svg_elements.append(nodo_metabolito(
        x=660, y=485,
        nombre="β-Ureidopropionato",
        formula_c="[4C] · Uracilo lineal abierto",
        detalle="Carbamoil unido a propionato",
        svg_estructura=BETA_UREIDOPROPIONATO,
        text_dx=165, text_dy=15
    ))

    svg_elements.append(nodo_metabolito(
        x=1050, y=485,
        nombre="β-Ureidoisobutirato",
        formula_c="[5C] · Timina lineal abierta",
        detalle="Carbamoil con metilo lateral",
        svg_estructura=BETA_UREIDOISOBUTIRATO,
        text_dx=165, text_dy=15
    ))

    # Reacción 3: beta-Ureidopropionasa (Descarbamilación)
    svg_elements.append(reaccion_vertical(
        x=920, y=585, h=45,
        enzima="β-Ureidopropionasa",
        ec="EC 3.5.1.6 (Libera CO₂ y amonio)",
        clinica="Genera aminoácidos beta libres",
        entra="- H₂O",
        sale="+ CO₂ + NH₄⁺"
    ))

    # Paso 4: Productos finales solubles BETA-ALANINA y BETA-AMINOISOBUTIRATO (Y=660)
    svg_elements.append(nodo_metabolito(
        x=720, y=660,
        nombre="β-Alanina",
        formula_c="[3C] · Aminoácido beta no proteico",
        detalle="Muy soluble · Convierte a Acetil-CoA",
        svg_estructura=BETA_ALANINA,
        text_dx=110, text_dy=15
    ))

    svg_elements.append(nodo_metabolito(
        x=1080, y=660,
        nombre="β-Aminoisobutirato",
        formula_c="[4C] · Aminoácido beta soluble",
        detalle="Transaminado a Succinil-CoA",
        svg_estructura=BETA_AMINOISOBUTIRATO,
        text_dx=110, text_dy=15
    ))

    # Destinos energéticos (sin cajas)
    svg_elements.append("""
    <g transform="translate(740, 770)">
      <text x="0" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#15803d">DESTINO ENERGÉTICO DE PIRIMIDINAS (SIN RIESGO DE CRISTALIZACIÓN)</text>
      <line x1="0" y1="22" x2="480" y2="22" stroke="#16a34a" stroke-width="1.8"/>
      <text x="0" y="42" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• β-Alanina ➔ Malonil semialdehído ➔ Acetil-CoA (alimenta lípidos o Krebs).</text>
      <text x="0" y="60" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• β-Aminoisobutirato ➔ Metilmalonato semialdehído ➔ Succinil-CoA (Krebs).</text>
      <text x="0" y="78" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#059669">Alta hidrosolubilidad: se excretan fácilmente sin formar tofos ni cálculos.</text>
    </g>
    """)

    # =========================================================================
    # BALANCE Y CONTRASTE CLÍNICO AL PIE (Y=1970)
    # =========================================================================
    svg_elements.append("""
    <g transform="translate(80, 1980)">
      <line x1="0" y1="0" x2="1260" y2="0" stroke="#cbd5e1" stroke-width="1.5"/>
      
      <!-- Columna 1 -->
      <g transform="translate(0, 25)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#9333ea">CONTRASTE CLÍNICO: PURINAS VS PIRIMIDINAS</text>
        <text x="0" y="20" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• Purinas: El anillo bicíclico no se escinde en humanos; se oxida a Ácido Úrico poco hidrosoluble.</text>
        <text x="0" y="38" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• Pérdida evolutiva: Homínidos perdieron la enzima Uricasa (Urato oxidasa) hace ~15 millones de años.</text>
        <text x="0" y="56" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• Hipótesis evolutiva: El urato elevado sirvió como potente antioxidante plasmático y retenedor de sodio.</text>
      </g>

      <!-- Columna 2 -->
      <g transform="translate(660, 25)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#9333ea">MANEJO TERAPÉUTICO Y DIANAS ENZIMÁTICAS</text>
        <text x="0" y="20" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• Alopurinol: Hipoxantina análoga que la XOD convierte en Aloxantina (inhibidor suicida de XOD).</text>
        <text x="0" y="38" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• Febuxostat: Inhibidor no purínico potente y selectivo de la Xantina Oxidasa.</text>
        <text x="0" y="56" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• Rasburicasa (Uricasa recombinante): Tratamiento de urgencia del Síndrome de Lisis Tumoral.</text>
      </g>
    </g>
    """)

    codigo_svg = "\n".join(svg_elements)
    documento_html = CABECERA_HTML + codigo_svg + PIE_HTML

    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_html = os.path.join(dir_actual, "Degradacion_Nucleotidos_y_Acido_Urico.html")
    ruta_svg = os.path.join(dir_actual, "Degradacion_Nucleotidos_y_Acido_Urico.svg")
    ruta_png = os.path.join(dir_actual, "Degradacion_Nucleotidos_y_Acido_Urico_preview.png")

    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(documento_html)
    print(f"✓ Archivo HTML guardado: {ruta_html}")

    svg_completo = f"""<svg width="{ANCHO}" height="{ALTO}" viewBox="0 0 {ANCHO} {ALTO}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrowFlowDeg" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#9333ea" />
        </marker>
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#2563eb" />
        </marker>
        {DEFS_ENTORNO_DEGRADACION}
      </defs>
      {codigo_svg}
    </svg>"""

    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_completo)
    print(f"✓ Archivo SVG guardado: {ruta_svg}")

    try:
        subprocess.run(["rsvg-convert", "-w", str(ANCHO * 2), ruta_svg, "-o", ruta_png], check=True)
        print(f"✓ Preview PNG generado con éxito: {ruta_png}")
    except Exception as e:
        print(f"! Error generando preview PNG: {e}")


if __name__ == "__main__":
    main()
