#!/usr/bin/env python3
"""
GENERADOR DE LA RUTA DE BIOSÍNTESIS DE NUCLEÓTIDOS (PURINAS Y PIRIMIDINAS)
==========================================================================
Lámina vectorizada editorial (SVG / HTML) calibrada con 0 solapamientos:
- Sin cajas contenedoras artificiales: estructuras químicas 2D libres.
- Columna izquierda: Síntesis de novo de Purinas y Vías de Salvamento (HGPRT / APRT).
- Columna derecha: Síntesis de novo de Pirimidinas y Timidilato (dTMP).
- Separación geométrica amplia y precisa para garantizar 0 colisiones texto-flecha y texto-texto.
"""

import os
import subprocess
from estructuras_nucleotidos import (
    RIBOSA_5_FOSFATO,
    PRPP,
    ORIGEN_ATOMOS_PURINA,
    ORIGEN_ATOMOS_PIRIMIDINA,
    IMP,
    AMP,
    GMP,
    CARBAMOIL_FOSFATO,
    OROTATO,
    UMP,
    CTP,
    DTMP
)
from entorno_nucleotidos import DEFS_ENTORNO_NUCLEOTIDOS, generar_entorno_nucleotidos_svg

ANCHO = 1450
ALTO = 2250

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vía 15: Biosíntesis de Nucleótidos (Purinas y Pirimidinas)</title>
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
        <!-- Flecha de flujo principal de Nucleótidos (Morado / Violeta) -->
        <marker id="arrowFlowPurine" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
        </marker>
        <!-- Flecha de reactivo / gasto de energía (Rojo carmesí) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de salida / subproducto (Gris pizarra) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <!-- Flecha de ganancia / producto favorable (Verde) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de amino / intermediario (Azul) -->
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#2563eb" />
        </marker>

        {DEFS_ENTORNO_NUCLEOTIDOS}
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""


def nodo_metabolito(x, y, nombre, formula_c, detalle="", svg_estructura="", text_dx=120, text_dy=25):
    """Construye un nodo metabólico libre en el espacio sin cajas artificiales."""
    return f"""
    <!-- Metabolito: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="translate(0, 0)">
        {svg_estructura}
      </g>
      <g transform="translate({text_dx}, {text_dy})">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="900">{nombre}</text>
        <text x="0" y="16" fill="#7c3aed" font-size="11.5" font-weight="800">{formula_c}</text>
        <text x="0" y="30" fill="#64748b" font-size="10" font-weight="600">{detalle}</text>
      </g>
    </g>
    """


def reaccion_vertical(x, y, h, enzima, ec="", regulacion="", clinica="", entra="", sale=""):
    """Genera una reacción vertical con curvas compactas que respetan los márgenes."""
    curvas = ""
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

    flecha = f"""
    <line x1="0" y1="0" x2="0" y2="{h}" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowFlowPurine)"/>
    """

    reg_svg = ""
    if regulacion:
        color_reg = "#dc2626" if "⊖" in regulacion or "Inhib" in regulacion else "#16a34a"
        reg_svg = f'<text x="0" y="24" fill="{color_reg}" font-size="9" font-weight="800">{regulacion}</text>'

    clin_svg = ""
    if clinica:
        clin_svg = f'<text x="0" y="36" fill="#be185d" font-size="9" font-family="\'JetBrains Mono\', monospace" font-weight="700">{clinica}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha}
      {curvas}
      <g transform="translate(14, 11)">
        <text x="0" y="0" fill="#0f172a" font-size="11.5" font-weight="900">{enzima}</text>
        <text x="0" y="12" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        {reg_svg}
        {clin_svg}
      </g>
    </g>
    """


def main():
    svg_elements = []

    # 1. ENTORNO BIOLÓGICO CELULAR DE FONDO
    svg_elements.append(generar_entorno_nucleotidos_svg(ancho=ANCHO, alto=ALTO))

    # =========================================================================
    # RÓTULO PRINCIPAL Y BADGE EDITORIAL
    # =========================================================================
    svg_elements.append("""
    <g transform="translate(60, 45)">
      <circle cx="20" cy="20" r="18" fill="#7c3aed" />
      <text x="20" y="26" font-family="'Inter', sans-serif" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle">15</text>
      
      <text x="50" y="17" font-family="'Inter', sans-serif" font-size="20" font-weight="900" fill="#0f172a">BIOSÍNTESIS DE NUCLEÓTIDOS: PURINAS Y PIRIMIDINAS</text>
      <text x="50" y="34" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#7c3aed">Rutas de novo convergentes sobre PRPP y vías de salvamento celular</text>
    </g>
    """)

    # =========================================================================
    # PARTE SUPERIOR: PRECURSORES COMUNES (RIBOSA-5-P -> PRPP)
    # =========================================================================
    # Ribosa-5-P (centro superior, X=620, Y=85)
    svg_elements.append(nodo_metabolito(
        x=600, y=85,
        nombre="D-Ribosa-5-Fosfato",
        formula_c="[5C] · Precursor de Pentosas",
        detalle="Procede de la Vía de las Pentosas P",
        svg_estructura=RIBOSA_5_FOSFATO,
        text_dx=120, text_dy=40
    ))

    # Reacción común: PRPP Sintetasa (X=650, Y=195)
    svg_elements.append(reaccion_vertical(
        x=650, y=195, h=45,
        enzima="PRPP Sintetasa",
        ec="EC 2.7.6.1 (Mg²⁺)",
        regulacion="⊕ Pi | ⊖ Purinas (AMP, GMP, IMP)",
        clinica="Regulación alostérica estricta",
        entra="- 1 ATP",
        sale="+ 1 AMP (libera PPi)"
    ))

    # PRPP (X=560, Y=265)
    svg_elements.append(nodo_metabolito(
        x=540, y=265,
        nombre="5-Fosforribosil-1-Pirofosfato (PRPP)",
        formula_c="[5C] · Ribosa activada con pirofosfato",
        detalle="Sustrato dador común para purinas y pirimidinas",
        svg_estructura=PRPP,
        text_dx=180, text_dy=45
    ))

    # Conectores de bifurcación desde PRPP (X=560 a 280 y X=800 a 1040)
    svg_elements.append("""
    <!-- Conectores de bifurcación desde PRPP -->
    <path d="M 540 375 Q 380 405 280 440" fill="none" stroke="#7c3aed" stroke-width="2.4" marker-end="url(#arrowFlowPurine)"/>
    <text x="360" y="365" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#7c3aed">Entrada a Purinas de novo</text>

    <path d="M 850 375 Q 980 405 1040 440" fill="none" stroke="#7c3aed" stroke-width="2.4" stroke-dasharray="4 3" marker-end="url(#arrowFlowPurine)"/>
    <text x="920" y="365" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#7c3aed">Aporte a UMP Sintasa</text>
    """)

    # =========================================================================
    # COLUMNA IZQUIERDA: SÍNTESIS DE PURINAS (X=60 a 660)
    # =========================================================================
    svg_elements.append("""
    <!-- Título de sección: Purinas -->
    <g transform="translate(80, 435)">
      <text x="0" y="18" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#6d28d9" letter-spacing="1">SÍNTESIS DE NOVO DE PURINAS</text>
      <line x1="0" y1="26" x2="380" y2="26" stroke="#7c3aed" stroke-width="2"/>
    </g>
    """)

    # Reacción limitante: Glutamina-PRPP Amidotransferasa (X=280, Y=475)
    svg_elements.append(reaccion_vertical(
        x=280, y=475, h=50,
        enzima="Glutamina-PRPP Amidotransferasa",
        ec="EC 2.4.2.14",
        regulacion="⊕ PRPP | ⊖ IMP, AMP, GMP",
        clinica="Paso comprometido limitante de purinas",
        entra="- L-Glutamina",
        sale="+ L-Glutamato + PPi"
    ))

    # Metabolito: 5-Fosforribosilamina (PRA)
    svg_elements.append("""
    <g transform="translate(200, 555)">
      <circle cx="70" cy="15" r="6" fill="#7c3aed"/>
      <text x="85" y="19" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a">5-Fosforribosilamina (PRA)</text>
      <text x="85" y="33" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#7c3aed">[5C] · Primer intermediario comprometido</text>
    </g>
    """)

    # Esquema didáctico: Ensamble del anillo purínico
    svg_elements.append("""
    <!-- Esquema didáctico de aportes atómicos al anillo -->
    <g transform="translate(150, 605)">
      """ + ORIGEN_ATOMOS_PURINA + """
    </g>
    <!-- Flecha de ensamblaje multienzimático de 9 pasos -->
    <g transform="translate(280, 750)">
      <line x1="0" y1="0" x2="0" y2="40" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowFlowPurine)"/>
      <text x="14" y="16" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a">9 Pasos sucesivos de ensamblaje</text>
      <text x="14" y="28" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="600" fill="#64748b">GAR ➔ FGAR ➔ FGAM ➔ AIR ➔ CAIR ➔ SAICAR ➔ AICAR ➔ FAICAR</text>
      <text x="14" y="38" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#dc2626">Gasto neto: 4 ATP adicionales</text>
    </g>
    """)

    # Intermediario clave: IMP (X=180, Y=810)
    svg_elements.append(nodo_metabolito(
        x=170, y=810,
        nombre="Inosina Monofosfato (IMP)",
        formula_c="[10C] · Nucleótido purínico maestro",
        detalle="Punto de bifurcación hacia AMP y GMP",
        svg_estructura=IMP,
        text_dx=140, text_dy=55
    ))

    # Bifurcación IMP hacia AMP (Izquierda X=170) y GMP (Derecha X=480)
    svg_elements.append("""
    <!-- Conectores de bifurcación desde IMP -->
    <path d="M 210 940 Q 180 970 170 1000" fill="none" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arrowFlowPurine)"/>
    <text x="120" y="960" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#7c3aed">Rama AMP</text>

    <path d="M 330 940 Q 420 970 480 1000" fill="none" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#arrowFlowPurine)"/>
    <text x="410" y="960" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#7c3aed">Rama GMP</text>
    """)

    # --- Rama Izquierda: AMP (Eje X=170) ---
    svg_elements.append(reaccion_vertical(
        x=170, y=1010, h=48,
        enzima="Adenilsuccinato Sintetasa",
        ec="EC 6.3.4.4",
        regulacion="⊖ Inhibida por AMP",
        clinica="Usa energía cruzada de GTP",
        entra="- GTP + Asp",
        sale="+ GDP + Pi"
    ))
    svg_elements.append(reaccion_vertical(
        x=170, y=1080, h=45,
        enzima="Adenilsuccinato Liasa",
        ec="EC 4.3.2.2",
        regulacion="",
        clinica="Libera intermediario a Krebs",
        sale="+ Fumarato"
    ))
    svg_elements.append(nodo_metabolito(
        x=90, y=1145,
        nombre="AMP (Adenilato)",
        formula_c="[10C] · Adenosina monofosfato",
        detalle="Fosforilación a ADP y ATP",
        svg_estructura=AMP,
        text_dx=115, text_dy=50
    ))

    # --- Rama Derecha: GMP (Eje X=480) ---
    svg_elements.append(reaccion_vertical(
        x=480, y=1010, h=48,
        enzima="IMP Deshidrogenasa",
        ec="EC 1.1.1.205",
        regulacion="⊖ Inhibida por GMP",
        clinica="Diana de Micofenolato mofetilo",
        entra="- NAD⁺ + H₂O",
        sale="+ NADH + H⁺"
    ))
    svg_elements.append(reaccion_vertical(
        x=480, y=1080, h=45,
        enzima="GMP Sintetasa",
        ec="EC 6.3.5.2",
        regulacion="",
        clinica="Usa energía cruzada de ATP",
        entra="- ATP + Gln",
        sale="+ AMP + PPi + Glu"
    ))
    svg_elements.append(nodo_metabolito(
        x=420, y=1145,
        nombre="GMP (Guanilato)",
        formula_c="[10C] · Guanosina monofosfato",
        detalle="Fosforilación a GDP y GTP",
        svg_estructura=GMP,
        text_dx=115, text_dy=50
    ))

    # =========================================================================
    # VÍA DE SALVAMENTO / RECICLAJE DE PURINAS (Inferior Izquierda, Y=1320 a 1600)
    # Sin cajas contenedoras artificiales
    # =========================================================================
    svg_elements.append("""
    <g transform="translate(80, 1315)">
      <text x="0" y="18" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#9d174d" letter-spacing="1">VÍAS DE SALVAMENTO / RECICLAJE (PURINAS)</text>
      <line x1="0" y1="26" x2="420" y2="26" stroke="#db2777" stroke-width="2"/>
      <text x="0" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#475569">Reactivación directa de bases nitrogenadas consumiendo PRPP:</text>
    </g>

    <!-- Reacción de Salvamento APRT -->
    <g transform="translate(90, 1380)">
      <line x1="0" y1="12" x2="50" y2="12" stroke="#db2777" stroke-width="2.2" marker-end="url(#arrowFlowPurine)"/>
      <text x="60" y="12" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a">Adenina + PRPP ➔ AMP + PPi</text>
      <text x="60" y="28" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#7c3aed">APRT (Adenina fosforribosiltransferasa · EC 2.4.2.7)</text>
      <text x="60" y="42" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b">Déficit: Litiasis renal de 2,8-dihidroxiadenina</text>
    </g>

    <!-- Reacción de Salvamento HGPRT -->
    <g transform="translate(90, 1450)">
      <line x1="0" y1="12" x2="50" y2="12" stroke="#db2777" stroke-width="2.2" marker-end="url(#arrowFlowPurine)"/>
      <text x="60" y="10" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a">Hipoxantina + PRPP ➔ IMP + PPi</text>
      <text x="60" y="26" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a">Guanina + PRPP ➔ GMP + PPi</text>
      <text x="60" y="44" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#7c3aed">HGPRT (Hipoxantina-guanina fosforribosiltransferasa · EC 2.4.2.8)</text>
      <text x="60" y="58" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#dc2626">Déficit congénito: Síndrome de Lesch-Nyhan (hiperuricemia y automutilación)</text>
    </g>
    """)

    # =========================================================================
    # COLUMNA DERECHA: SÍNTESIS DE NOVO DE PIRIMIDINAS (X=740 a 1400)
    # =========================================================================
    svg_elements.append("""
    <!-- Título de sección: Pirimidinas -->
    <g transform="translate(740, 435)">
      <text x="0" y="18" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#6d28d9" letter-spacing="1">SÍNTESIS DE NOVO DE PIRIMIDINAS</text>
      <line x1="0" y1="26" x2="420" y2="26" stroke="#7c3aed" stroke-width="2"/>
    </g>
    """)

    # Reacción 1: CPS-II Citosólica (X=980, Y=475)
    svg_elements.append(reaccion_vertical(
        x=980, y=475, h=50,
        enzima="Carbamoil Fosfato Sintetasa II (CPS-II)",
        ec="EC 6.3.5.5 (Citosólica)",
        regulacion="⊕ PRPP, ATP | ⊖ UTP",
        clinica="Punto de control primario de pirimidinas",
        entra="- 2 ATP + Gln + HCO₃⁻",
        sale="+ 2 ADP + Pi + Glu"
    ))

    # Carbamoil Fosfato Citosólico (X=900, Y=545)
    svg_elements.append(nodo_metabolito(
        x=890, y=545,
        nombre="Carbamoil Fosfato",
        formula_c="[1C] · Dador de N3 y C2",
        detalle="Producido en citosol (CPS-II)",
        svg_estructura=CARBAMOIL_FOSFATO,
        text_dx=120, text_dy=25
    ))

    # Reacciones intermedias: ATCasa, Dihidroorotasa y DHODH (bien espaciadas)
    svg_elements.append(reaccion_vertical(
        x=980, y=625, h=45,
        enzima="Aspartato Transcarbamoilasa (ATCasa)",
        ec="EC 2.1.3.2",
        regulacion="⊕ ATP | ⊖ CTP",
        clinica="Condensa con Aspartato a N-carbamoilaspartato",
        entra="- L-Aspartato",
        sale="+ Pi"
    ))

    svg_elements.append(reaccion_vertical(
        x=980, y=695, h=45,
        enzima="Dihidroorotasa",
        ec="EC 3.5.2.3",
        regulacion="",
        clinica="Cierre catalítico del anillo a Dihidroorotato",
        sale="- H₂O"
    ))

    # Reacción mitocondrial: DHODH acoplada a MMI
    svg_elements.append(reaccion_vertical(
        x=980, y=765, h=45,
        enzima="Dihidroorotato Deshidrogenasa (DHODH)",
        ec="EC 1.3.5.2 (Membrana Interna MMI)",
        regulacion="",
        clinica="Diana de Leflunomida / Teriflunomida",
        entra="- CoQ (Ubiquinona)",
        sale="+ CoQH₂"
    ))

    # Esquema didáctico: Origen de átomos del anillo pirimidínico
    svg_elements.append("""
    <g transform="translate(870, 835)">
      """ + ORIGEN_ATOMOS_PIRIMIDINA + """
    </g>
    """)

    # Intermediario clave: OROTATO (X=890, Y=990)
    svg_elements.append(nodo_metabolito(
        x=880, y=990,
        nombre="Ácido Orótico (Orotato)",
        formula_c="[5C] · Base pirimidínica oxidada",
        detalle="Sustrato receptor del PRPP",
        svg_estructura=OROTATO,
        text_dx=120, text_dy=35
    ))

    # Enzima bifuncional: UMP Sintasa (X=980, Y=1075)
    svg_elements.append(reaccion_vertical(
        x=980, y=1075, h=52,
        enzima="UMP Sintasa (OPRT + OMPDC)",
        ec="EC 2.4.2.10 / EC 4.1.1.23",
        regulacion="",
        clinica="Déficit: Aciduria Orótica Hereditaria",
        entra="- PRPP",
        sale="+ PPi + CO₂"
    ))

    # Producto pirimidínico central: UMP (X=890, Y=1150)
    svg_elements.append(nodo_metabolito(
        x=880, y=1150,
        nombre="Uridina Monofosfato (UMP)",
        formula_c="[9C] · Nucleótido pirimidínico raíz",
        detalle="Precursor de ribonucleótidos U/C y dTMP",
        svg_estructura=UMP,
        text_dx=125, text_dy=50
    ))

    # Fosforilaciones UMP -> UDP -> UTP y síntesis de CTP
    svg_elements.append("""
    <!-- Fosforilaciones de UMP a UTP -->
    <g transform="translate(980, 1285)">
      <line x1="0" y1="0" x2="0" y2="40" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowFlowPurine)"/>
      <text x="14" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a">Nucleósido Quinasas (UMP ➔ UDP ➔ UTP)</text>
      <text x="14" y="30" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b">EC 2.7.4.4 / EC 2.7.4.6 · Gasto de 2 ATP</text>
    </g>
    """)

    # CTP Sintetasa (X=980, Y=1345)
    svg_elements.append(reaccion_vertical(
        x=980, y=1345, h=48,
        enzima="CTP Sintetasa",
        ec="EC 6.3.4.2",
        regulacion="⊕ GTP | ⊖ CTP",
        clinica="Aminación dependiente de Glutamina",
        entra="- ATP + Glutamina",
        sale="+ ADP + Pi + Glu"
    ))

    # CTP (X=880, Y=1415)
    svg_elements.append(nodo_metabolito(
        x=870, y=1415,
        nombre="Citidina Trifosfato (CTP)",
        formula_c="[9C] · Precursor de ARN y Lípidos",
        detalle="Sustrato para síntesis de fosfolípidos",
        svg_estructura=CTP,
        text_dx=140, text_dy=40
    ))

    # =========================================================================
    # SÍNTESIS DE DESOXIRRIBONUCLEÓTIDOS Y TIMIDILATO (dTMP) (Y=1545 a 2050)
    # =========================================================================
    svg_elements.append("""
    <g transform="translate(740, 1530)">
      <text x="0" y="18" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#6d28d9" letter-spacing="1">SÍNTESIS DE DESOXIRRIBONUCLEÓTIDOS Y TIMIDILATO (dTMP)</text>
      <line x1="0" y1="26" x2="480" y2="26" stroke="#7c3aed" stroke-width="2"/>
    </g>
    """)

    # Ribonucleótido Reductasa (RNR, X=980, Y=1570)
    svg_elements.append(reaccion_vertical(
        x=980, y=1570, h=48,
        enzima="Ribonucleótido Reductasa (RNR)",
        ec="EC 1.17.4.1 (Reduce UDP ➔ dUDP)",
        regulacion="⊕ ATP | ⊖ dATP (Sitio global)",
        clinica="Diana quimioterápica: Hidroxiurea",
        entra="- Tiorredoxina reducida",
        sale="+ Tiorredoxina oxidada"
    ))

    # Conversión dUDP -> dUMP (X=980, Y=1645)
    svg_elements.append("""
    <g transform="translate(980, 1640)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#7c3aed" stroke-width="2.6" marker-end="url(#arrowFlowPurine)"/>
      <text x="14" y="14" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a">dUTPasa / Desaminasa (dUDP ➔ dUTP ➔ dUMP)</text>
      <text x="14" y="27" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b">EC 3.6.1.23 · Evita la incorporación letal de uracilo al ADN</text>
    </g>
    """)

    # Timidilato Sintasa (X=980, Y=1695)
    svg_elements.append(reaccion_vertical(
        x=980, y=1695, h=52,
        enzima="Timidilato Sintasa",
        ec="EC 2.1.1.45 (Metila dUMP ➔ dTMP)",
        regulacion="",
        clinica="Inhibidor suicida: 5-Fluorouracilo (5-FU)",
        entra="- N⁵,N¹⁰-Metileno-THF",
        sale="+ 7,8-Dihidrofolato"
    ))

    # Metabolito clave de ADN: dTMP (X=880, Y=1775)
    svg_elements.append(nodo_metabolito(
        x=870, y=1775,
        nombre="Desoxitimidina Monofosfato (dTMP)",
        formula_c="[10C] · Monómero exclusivo del ADN",
        detalle="Posee el grupo 5-metilo distintivo",
        svg_estructura=DTMP,
        text_dx=140, text_dy=55
    ))

    # Ciclo del Folato acoplado: Dihidrofolato Reductasa (DHFR, X=980, Y=1925)
    svg_elements.append(reaccion_vertical(
        x=980, y=1925, h=48,
        enzima="Dihidrofolato Reductasa (DHFR)",
        ec="EC 1.5.1.3 (DHF ➔ THF)",
        regulacion="",
        clinica="Dianas farmacológicas: Metotrexato, Trimetoprima",
        entra="- NADPH + H⁺",
        sale="+ NADP⁺"
    ))

    # =========================================================================
    # BLOQUE DE RESUMEN METABÓLICO AL PIE (Y=2080)
    # Sin cajas contenedoras artificiales
    # =========================================================================
    svg_elements.append("""
    <g transform="translate(80, 2080)">
      <line x1="0" y1="0" x2="1280" y2="0" stroke="#cbd5e1" stroke-width="1.5"/>
      
      <!-- Columna 1 -->
      <g transform="translate(0, 25)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#7c3aed">BALANCE BIOENERGÉTICO</text>
        <text x="0" y="20" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• Síntesis de Novo: Alto coste energético (gasto de 5 a 6 ATP equivalentes por nucleótido purínico).</text>
        <text x="0" y="38" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• Vía de Salvamento: Ahorro masivo de ATP (1 PRPP por base reciclada), esencial en encéfalo y eritrocitos.</text>
        <text x="0" y="56" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• Asimetría de síntesis: Purinas ensamblan el anillo sobre PRPP; Pirimidinas forman el anillo libre primero.</text>
      </g>

      <!-- Columna 2 -->
      <g transform="translate(680, 25)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#7c3aed">REGULACIÓN CRUZADA PURINA / PIRIMIDINA</text>
        <text x="0" y="20" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• GTP estimula la síntesis de AMP; ATP estimula la de GMP y la activación de CPS-II y ATCasa.</text>
        <text x="0" y="38" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• El balance recíproco asegura proporciones equimolares de purinas y pirimidinas.</text>
        <text x="0" y="56" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a">• RNR controla la reserva de los 4 desoxirribonucleótidos (retroinhibida por dATP).</text>
      </g>
    </g>
    """)

    codigo_svg = "\n".join(svg_elements)
    documento_html = CABECERA_HTML + codigo_svg + PIE_HTML

    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_html = os.path.join(dir_actual, "Sintesis_Purinas_y_Pirimidinas.html")
    ruta_svg = os.path.join(dir_actual, "Sintesis_Purinas_y_Pirimidinas.svg")
    ruta_png = os.path.join(dir_actual, "Sintesis_Purinas_y_Pirimidinas_preview.png")

    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(documento_html)
    print(f"✓ Archivo HTML guardado: {ruta_html}")

    svg_completo = f"""<svg width="{ANCHO}" height="{ALTO}" viewBox="0 0 {ANCHO} {ALTO}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrowFlowPurine" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
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
        {DEFS_ENTORNO_NUCLEOTIDOS}
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
