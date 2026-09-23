#!/usr/bin/env python3
"""
GENERADOR DEL MAPA: CADENA TRANSPORTADORA DE ELECTRONES Y ATP SINTASA
=====================================================================
Módulo autónomo ("individual") con el mismo estilo editorial que la Glucólisis:
- Estructuras químicas SVG propias (NADH, FADH₂, CoQ, citocromo c, O₂, H₂O).
- Entorno mitocondrial real: citosol, MME (VDAC), EIM (gradiente H⁺),
  MMI (bicapa lipídica) y matriz mitocondrial.
- Cinco complejos incrustados en la bicapa: I, II, III, IV y ATP sintasa (F₀F₁).
- Transportadores móviles: ubiquinona (Q/QH₂) y citocromo c.
- Paneles universitarios: ciclo Q, hemo c, estequiometría P/O e inhibidores.

Salidas: Cadena_Transporte_Electrones.html y Cadena_Transporte_Electrones.svg
"""

import os

from estructuras_cadena_transporte import (
    NADH,
    NAD_PLUS,
    FADH2,
    FAD,
    UBIQUINONA,
    UBIQUINOL,
    CITOCROMO_C,
    OXIGENO,
    AGUA,
    SUCCINATO,
    FUMARATO,
)
from entorno_cte import DEFS_ENTORNO_CTE, generar_entorno_cte_svg

# -----------------------------------------------------------------------------
# 1. GEOMETRÍA GENERAL DEL LIENZO
# -----------------------------------------------------------------------------
ANCHO_CANVAS = 1700
ALTO_CANVAS = 2200

Y_MME = 112
Y_EIM_INI = 132
Y_EIM_FIN = 545
Y_MMI_INI = 545
Y_MMI_FIN = 645
Y_MATRIZ_INI = 645

# Coordenada X central de cada complejo
X_I, X_II, X_Q, X_III, X_CYC, X_IV, X_V = 180, 470, 655, 855, 1015, 1230, 1510

# Paleta por complejo (familia mitocondrial del Manual de Estilo)
COL_I, COL_I_CLARO = "#0369a1", "#e0f2fe"
COL_II, COL_II_CLARO = "#047857", "#d1fae5"
COL_III, COL_III_CLARO = "#7c3aed", "#ede9fe"
COL_IV, COL_IV_CLARO = "#b45309", "#fef3c7"
COL_V, COL_V_CLARO = "#be123c", "#ffe4e6"
COL_Q = "#d97706"
COL_CYC = "#0891b2"


# -----------------------------------------------------------------------------
# 2. CABECERA HTML / SVG
# -----------------------------------------------------------------------------
CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cadena Transportadora de Electrones y ATP Sintasa</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;600;700;800&display=swap" rel="stylesheet">
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
      width: {ANCHO_CANVAS}px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 12px;
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.14);
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
"""

DEFS_MARCADORES = f"""
      <defs>
        <!-- Flecha de flujo metabólico principal (Naranja) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de flujo de electrones (Roja) -->
        <marker id="arrowElectron" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de gasto / reactivo (Roja) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de salida de subproducto (Gris pizarra) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <!-- Flecha de ganancia / poder reductor (Verde esmeralda) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de agua / transporte (Azul) -->
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>
        <!-- Flecha de la familia mitocondrial (Ámbar) -->
        <marker id="arrowAmber" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#b45309" />
        </marker>

        {DEFS_ENTORNO_CTE}
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""


# -----------------------------------------------------------------------------
# 3. FUNCIONES GENERADORAS DE ELEMENTOS GENÉRICOS
# -----------------------------------------------------------------------------
def crear_especie(x, y, nombre, detalle, svg_estructura, escala=1.0,
                  dx_texto=180, pos_texto="derecha", detalle2="", color_nombre="#0f172a"):
    """
    Coloca una estructura química con su rótulo.
    pos_texto: "derecha" | "abajo" | "izquierda"
    """
    linea2 = (f'<text x="0" y="36" fill="#64748b" font-size="10.5">{detalle2}</text>'
              if detalle2 else "")

    if pos_texto == "derecha":
        bloque_texto = f"""
        <g transform="translate({dx_texto}, 24)">
          <text x="0" y="0" fill="{color_nombre}" font-size="17" font-weight="800">{nombre}</text>
          <text x="0" y="19" fill="#ea580c" font-size="11.5" font-weight="700">{detalle}</text>
          {linea2}
        </g>"""
    elif pos_texto == "izquierda":
        bloque_texto = f"""
        <g transform="translate({-dx_texto}, 24)">
          <text x="0" y="0" fill="{color_nombre}" font-size="17" font-weight="800" text-anchor="end">{nombre}</text>
          <text x="0" y="19" fill="#ea580c" font-size="11.5" font-weight="700" text-anchor="end">{detalle}</text>
        </g>"""
    else:  # abajo
        bloque_texto = f"""
        <g transform="translate(0, {dx_texto})">
          <text x="0" y="0" fill="{color_nombre}" font-size="16" font-weight="800" text-anchor="middle">{nombre}</text>
          <text x="0" y="19" fill="#ea580c" font-size="11" font-weight="700" text-anchor="middle">{detalle}</text>
          {linea2}
        </g>"""

    return f"""
    <!-- Especie: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="scale({escala})">
        {svg_estructura}
      </g>
      {bloque_texto}
    </g>
    """


def crear_chip(x, y, texto, subtexto="", color="#0369a1", color_claro="#e0f2fe", ancho=None):
    """Pastilla identificativa de un complejo (nombre + subtítulo)."""
    ancho_final = ancho if ancho else max(150, int(len(texto) * 8.2) + 30)
    sub = (f'<text x="{ancho_final // 2}" y="30" fill="#475569" font-size="9" '
           f'font-family="\'JetBrains Mono\', monospace" text-anchor="middle">{subtexto}</text>'
           if subtexto else "")
    alto = 40 if subtexto else 26
    return f"""
    <g transform="translate({x}, {y})">
      <rect x="0" y="0" width="{ancho_final}" height="{alto}" rx="{alto // 2}"
            fill="{color_claro}" stroke="{color}" stroke-width="1.8"/>
      <text x="{ancho_final // 2}" y="17" fill="{color}" font-size="12.5" font-weight="900"
            text-anchor="middle">{texto}</text>
      {sub}
    </g>
    """


def crear_tarjeta(x, y, ancho, alto, titulo, color, color_claro, contenido):
    """Tarjeta educativa universitaria con cabecera coloreada."""
    return f"""
    <g transform="translate({x}, {y})">
      <rect x="0" y="0" width="{ancho}" height="{alto}" rx="12" fill="#ffffff"
            stroke="#cbd5e1" stroke-width="1.8" filter="drop-shadow(0 10px 20px rgba(0,0,0,0.07))"/>
      <rect x="0" y="0" width="{ancho}" height="38" rx="12" fill="{color_claro}" stroke="{color}" stroke-width="1.8"/>
      <rect x="0" y="26" width="{ancho}" height="12" fill="{color_claro}"/>
      <text x="{ancho // 2}" y="25" font-family="'Inter', sans-serif" font-size="13" font-weight="900"
            fill="{color}" text-anchor="middle" letter-spacing="0.4">{titulo}</text>
      {contenido}
    </g>
    """


# -----------------------------------------------------------------------------
# 4. LOS CINCO COMPLEJOS RESPIRATORIOS INCRUSTADOS EN LA BICAPA
# -----------------------------------------------------------------------------
def _borde_membrana(y_ini=495, y_fin=690):
    """Devuelve las coordenadas útiles de la zona transmembrana."""
    return y_ini, y_fin


def complejo_i():
    """Complejo I: NADH:ubiquinona oxidorreductasa (L invertida, 4 H⁺ bombeados)."""
    return f"""
    <!-- ===== COMPLEJO I: brazo hidrofóbico + brazo hidrofílico matricial ===== -->
    <path d="M 60 520 Q 60 495 85 495 L 275 495 Q 300 495 300 520 L 300 665
             Q 300 690 275 690 L 258 690 L 258 985 Q 258 1010 233 1010
             L 128 1010 Q 103 1010 103 985 L 103 690 L 85 690 Q 60 690 60 665 Z"
          fill="{COL_I_CLARO}" stroke="{COL_I}" stroke-width="2.8"/>
    <!-- Subunidades sugeridas -->
    <line x1="130" y1="500" x2="130" y2="686" stroke="{COL_I}" stroke-width="1.1" stroke-dasharray="5 5" opacity="0.5"/>
    <line x1="200" y1="500" x2="200" y2="686" stroke="{COL_I}" stroke-width="1.1" stroke-dasharray="5 5" opacity="0.5"/>
    <line x1="103" y1="800" x2="258" y2="800" stroke="{COL_I}" stroke-width="1.1" stroke-dasharray="5 5" opacity="0.5"/>
    <line x1="103" y1="905" x2="258" y2="905" stroke="{COL_I}" stroke-width="1.1" stroke-dasharray="5 5" opacity="0.5"/>
    <text x="180" y="576" fill="{COL_I}" font-size="14" font-weight="900" text-anchor="middle">Complejo I</text>
    <text x="180" y="596" fill="#0f172a" font-size="9" font-weight="700" text-anchor="middle"
          font-family="'JetBrains Mono', monospace">NADH:ubiquinona oxidorreductasa</text>
    <!-- Centro FMN y centros Fe-S en el brazo matricial -->
    <circle cx="180" cy="730" r="6" fill="#f59e0b" stroke="#b45309" stroke-width="1.4"/>
    <text x="180" y="734" fill="#78350f" font-size="6.5" font-weight="900" text-anchor="middle">FMN</text>
    <circle cx="150" cy="800" r="5" fill="#dc2626" stroke="#991b1b" stroke-width="1.2"/>
    <circle cx="210" cy="860" r="5" fill="#dc2626" stroke="#991b1b" stroke-width="1.2"/>
    <circle cx="160" cy="920" r="5" fill="#dc2626" stroke="#991b1b" stroke-width="1.2"/>
    <text x="180" y="982" fill="#991b1b" font-size="8.5" font-weight="800" text-anchor="middle">8 centros [Fe-S]</text>
    <text x="180" y="836" fill="#0f172a" font-size="8.5" font-weight="800"
          transform="rotate(-90 180 836)" text-anchor="middle">NADH ➔ FMN ➔ Fe-S ➔ Q</text>
    """


def complejo_ii():
    """Complejo II: Succinato deshidrogenasa (única enzima del ciclo de Krebs unida a membrana)."""
    return f"""
    <!-- ===== COMPLEJO II: SDH (FAD covalente, no bombea protones) ===== -->
    <path d="M 385 520 Q 385 495 410 495 L 535 495 Q 560 495 560 520 L 560 665
             Q 560 690 535 690 L 425 690 Q 400 690 400 665 L 400 520 Z"
          fill="{COL_II_CLARO}" stroke="{COL_II}" stroke-width="2.8"/>
    <!-- Dominio matricial con la subunidad catalítica -->
    <rect x="410" y="680" width="120" height="150" rx="22" fill="{COL_II_CLARO}" stroke="{COL_II}" stroke-width="2.8"/>
    <text x="470" y="700" fill="{COL_II}" font-size="13" font-weight="900" text-anchor="middle">Complejo II</text>
    <text x="470" y="716" fill="#0f172a" font-size="8.5" font-weight="700" text-anchor="middle"
          font-family="'JetBrains Mono', monospace">Succinato DH (SDH)</text>
    <!-- Subunidades SDHA / SDHB / SDHC-SDHD -->
    <rect x="418" y="726" width="104" height="30" rx="10" fill="#fef3c7" stroke="#b45309" stroke-width="1.4"/>
    <text x="470" y="746" fill="#78350f" font-size="8.5" font-weight="900" text-anchor="middle">SDHA • FAD</text>
    <rect x="418" y="762" width="104" height="28" rx="10" fill="#d1fae5" stroke="#047857" stroke-width="1.4"/>
    <text x="470" y="781" fill="#065f46" font-size="8.5" font-weight="900" text-anchor="middle">SDHB • [Fe-S]</text>
    <text x="470" y="812" fill="#0369a1" font-size="8.5" font-weight="800" text-anchor="middle">SDHC / SDHD (hemo b)</text>
    <!-- Sitio catalítico -->
    <text x="470" y="860" fill="#78350f" font-size="9.5" font-weight="800" text-anchor="middle">Succinato ➔ Fumarato</text>
    """


def complejo_iii():
    """Complejo III: Citocromo bc₁ con el ciclo Q (4 H⁺ bombeados)."""
    return f"""
    <!-- ===== COMPLEJO III: bc₁ con dominio en el EIM ===== -->
    <path d="M 768 520 Q 768 495 793 495 L 927 495 Q 952 495 952 520 L 952 665
             Q 952 690 927 690 L 793 690 Q 768 690 768 665 Z"
          fill="{COL_III_CLARO}" stroke="{COL_III}" stroke-width="2.8"/>
    <!-- Dominio soluble en el espacio intermembrana (Rieske / cit c₁) -->
    <rect x="795" y="404" width="130" height="92" rx="22" fill="{COL_III_CLARO}" stroke="{COL_III}" stroke-width="2.8"/>
    <text x="860" y="440" fill="{COL_III}" font-size="13" font-weight="900" text-anchor="middle">Complejo III</text>
    <text x="860" y="456" fill="#0f172a" font-size="8.5" font-weight="700" text-anchor="middle"
          font-family="'JetBrains Mono', monospace">Citocromo bc₁</text>
    <text x="860" y="480" fill="#4c1d95" font-size="8.5" font-weight="800" text-anchor="middle">Cit c₁ ➔ citocromo c</text>
    <!-- Grupos hemo -->
    <circle cx="810" cy="560" r="7" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.6"/>
    <text x="810" y="563" fill="#5b21b6" font-size="6.5" font-weight="900" text-anchor="middle">bL</text>
    <circle cx="910" cy="600" r="7" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.6"/>
    <text x="910" y="603" fill="#5b21b6" font-size="6.5" font-weight="900" text-anchor="middle">bH</text>
    <text x="860" y="556" fill="#5b21b6" font-size="9" font-weight="800" text-anchor="middle">Ciclo Q</text>
    <text x="860" y="586" fill="#0f172a" font-size="8" font-weight="700" text-anchor="middle">QH₂ ➔ Q•⁻ ➔ Q</text>
    <text x="860" y="668" fill="#0f172a" font-size="8.5" font-weight="800" text-anchor="middle">2 e⁻ por ciclo • 4 H⁺ al EIM</text>
    """


def complejo_iv():
    """Complejo IV: Citocromo c oxidasa (reduce el O₂ a agua, 2 H⁺ bombeados)."""
    return f"""
    <!-- ===== COMPLEJO IV: citocromo c oxidasa (COX) ===== -->
    <path d="M 1135 520 Q 1135 495 1160 495 L 1330 495 Q 1355 495 1355 520 L 1355 665
             Q 1355 690 1330 690 L 1160 690 Q 1135 690 1135 665 Z"
          fill="{COL_IV_CLARO}" stroke="{COL_IV}" stroke-width="2.8"/>
    <!-- Dominio matricial (sitio de reducción del O₂) -->
    <rect x="1175" y="680" width="140" height="112" rx="22" fill="{COL_IV_CLARO}" stroke="{COL_IV}" stroke-width="2.8"/>
    <text x="1245" y="576" fill="{COL_IV}" font-size="14" font-weight="900" text-anchor="middle">Complejo IV</text>
    <text x="1245" y="596" fill="#0f172a" font-size="8.5" font-weight="700" text-anchor="middle"
          font-family="'JetBrains Mono', monospace">Citocromo c oxidasa</text>
    <!-- Centros redox -->
    <circle cx="1180" cy="740" r="7" fill="#fef3c7" stroke="#b45309" stroke-width="1.6"/>
    <text x="1180" y="743" fill="#78350f" font-size="6" font-weight="900" text-anchor="middle">CuA</text>
    <circle cx="1245" cy="760" r="7" fill="#fef3c7" stroke="#b45309" stroke-width="1.6"/>
    <text x="1245" y="763" fill="#78350f" font-size="6" font-weight="900" text-anchor="middle">hema</text>
    <circle cx="1310" cy="740" r="7" fill="#fef3c7" stroke="#b45309" stroke-width="1.6"/>
    <text x="1310" y="743" fill="#78350f" font-size="6" font-weight="900" text-anchor="middle">CuB</text>
    <text x="1245" y="786" fill="#7c2d12" font-size="8.5" font-weight="800" text-anchor="middle">O₂ + 4 H⁺ + 4 e⁻</text>
    """


def atp_sintasa():
    """ATP sintasa (F₀F₁): motor rotatorio acoplado a la fuerza protón-motriz."""
    return f"""
    <!-- ===== ATP SINTASA (F₀F₁) ===== -->
    <!-- F₀: sector transmembrana (canal de protones) -->
    <path d="M 1445 520 Q 1445 495 1470 495 L 1570 495 Q 1595 495 1595 520 L 1595 665
             Q 1595 690 1570 690 L 1470 690 Q 1445 690 1445 665 Z"
          fill="{COL_V_CLARO}" stroke="{COL_V}" stroke-width="2.8"/>
    <!-- Eje central (subunidad γ) -->
    <rect x="1507" y="690" width="26" height="80" rx="10" fill="#fda4af" stroke="{COL_V}" stroke-width="2"/>
    <!-- F₁: cabeza catalítica -->
    <rect x="1430" y="770" width="180" height="210" rx="46" fill="{COL_V_CLARO}" stroke="{COL_V}" stroke-width="2.8"/>
    <!-- Tallo periférico (b₂ / OSCP) -->
    <path d="M 1420 600 L 1420 900 Q 1420 940 1445 950" fill="none" stroke="{COL_V}" stroke-width="9" stroke-linecap="round" opacity="0.75"/>
    <text x="1330" y="700" fill="{COL_V}" font-size="9" font-weight="800" text-anchor="middle"
          transform="rotate(-90 1330 700)">Tallo periférico b₂ / OSCP</text>

    <text x="1520" y="576" fill="{COL_V}" font-size="13" font-weight="900" text-anchor="middle">ATP Sintasa</text>
    <text x="1520" y="594" fill="#0f172a" font-size="8" font-weight="700" text-anchor="middle"
          font-family="'JetBrains Mono', monospace">F₀F₁ (Complejo V)</text>
    <text x="1520" y="530" fill="#9f1239" font-size="9" font-weight="900" text-anchor="middle">F₀</text>

    <!-- Cabeza F₁ con las tres conformaciones catalíticas -->
    <text x="1520" y="806" fill="{COL_V}" font-size="12" font-weight="900" text-anchor="middle">F₁</text>
    <circle cx="1475" cy="845" r="17" fill="#ffffff" stroke="{COL_V}" stroke-width="1.8"/>
    <text x="1475" y="849" fill="#9f1239" font-size="9" font-weight="900" text-anchor="middle">β-L</text>
    <circle cx="1565" cy="845" r="17" fill="#ffffff" stroke="{COL_V}" stroke-width="1.8"/>
    <text x="1565" y="849" fill="#9f1239" font-size="9" font-weight="900" text-anchor="middle">β-T</text>
    <circle cx="1520" cy="905" r="17" fill="#ffffff" stroke="{COL_V}" stroke-width="1.8"/>
    <text x="1520" y="909" fill="#9f1239" font-size="9" font-weight="900" text-anchor="middle">β-O</text>
    <text x="1520" y="955" fill="#9f1239" font-size="9" font-weight="800" text-anchor="middle">Rotación γ (3 H⁺ / vuelta)</text>
    """


# -----------------------------------------------------------------------------
# 5. ELEMENTOS DE FLUJO: ELECTRONES Y PROTONES
# -----------------------------------------------------------------------------
def ruta_electrones():
    """Trazado discontinuo del flujo de electrones: I/II ➔ Q ➔ III ➔ cit c ➔ IV ➔ O₂."""
    return f"""
    <!-- ===== FLUJO DE ELECTRONES (línea roja discontinua) ===== -->
    <g fill="none" stroke="#dc2626" stroke-width="2.4" stroke-dasharray="9 6">
      <path d="M 300 590 L 630 590" marker-end="url(#arrowElectron)"/>
      <path d="M 560 590 L 630 590" marker-end="url(#arrowElectron)"/>
      <path d="M 682 590 L 764 590" marker-end="url(#arrowElectron)"/>
      <path d="M 952 590 L 996 590" marker-end="url(#arrowElectron)"/>
      <path d="M 1042 590 L 1131 590" marker-end="url(#arrowElectron)"/>
      <path d="M 1245 695 L 1245 862" marker-end="url(#arrowElectron)"/>
    </g>

    <!-- Transportador móvil: UBIQUINONA (Q ⇄ QH₂) en la bicapa -->
    <g transform="translate({X_Q}, 590)">
      <polygon points="0,-17 15,-8 15,9 0,18 -15,9 -15,-8" fill="#fef3c7" stroke="{COL_Q}" stroke-width="2.2"/>
      <text x="0" y="4" fill="#92400e" font-size="11" font-weight="900" text-anchor="middle">Q</text>
      <polyline points="-15,-8 -26,-16 -36,-6 -46,-14" fill="none" stroke="{COL_Q}" stroke-width="2"/>
      <text x="0" y="34" fill="#92400e" font-size="9" font-weight="900" text-anchor="middle">Q ⇄ QH₂</text>
    </g>

    <!-- Transportador móvil: CITOCROMO c (proteína soluble del EIM) -->
    <g transform="translate({X_CYC}, 590)">
      <circle cx="0" cy="0" r="19" fill="#cffafe" stroke="{COL_CYC}" stroke-width="2.4"/>
      <rect x="-7" y="-7" width="14" height="14" rx="3" fill="#ffedd5" stroke="#b45309" stroke-width="1.5"/>
      <text x="0" y="4" fill="#b45309" font-size="8" font-weight="900" text-anchor="middle">Fe</text>
      <text x="0" y="36" fill="#0e7490" font-size="9" font-weight="900" text-anchor="middle">Cit c</text>
    </g>
    """


def bombeo_protones():
    """Arcos de bombeo de H⁺ desde la matriz hacia el EIM a través de I, III y IV."""
    return f"""
    <!-- ===== BOMBEO DE PROTONES H⁺ (matriz ➔ EIM) ===== -->
    <g fill="none" stroke="#ea580c" stroke-width="3" stroke-linecap="round">
      <path d="M 268 730 Q 330 660 330 520 Q 330 400 292 320" marker-end="url(#arrowFlow)"/>
      <path d="M 938 740 Q 1000 660 1000 520 Q 1000 400 962 320" marker-end="url(#arrowFlow)"/>
      <path d="M 1342 700 Q 1390 640 1390 520 Q 1390 420 1362 350" marker-end="url(#arrowFlow)"/>
    </g>
    <g font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#c2410c">
      <text x="352" y="430">4 H⁺</text>
      <text x="1022" y="430">4 H⁺</text>
      <text x="1398" y="470">2 H⁺</text>
    </g>

    <!-- ===== RETORNO DE PROTONES POR LA ATP SINTASA (EIM ➔ matriz) ===== -->
    <path d="M 1620 320 Q 1690 430 1690 560 Q 1690 690 1610 780"
          fill="none" stroke="#ea580c" stroke-width="3.4" stroke-linecap="round" marker-end="url(#arrowFlow)"/>
    <text x="1636" y="440" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#c2410c">
      ≈ 4 H⁺ / ATP
    </text>

    <!-- Acoplamiento quimiosmótico -->
    <g transform="translate(1080, 300)">
      <rect x="0" y="0" width="330" height="46" rx="10" fill="#ffffff" stroke="#ea580c" stroke-width="1.8" opacity="0.95"/>
      <text x="165" y="18" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#9a3412" text-anchor="middle">
        ACOPLAMIENTO QUIMIOSMÓTICO (MITCHELL, 1961)
      </text>
      <text x="165" y="34" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">
        El bombeo de H⁺ crea la fuerza protón-motriz que impulsa la síntesis de ATP
      </text>
    </g>
    """


def reacciones_matriz():
    """Donantes de electrones, reducción del O₂ y síntesis de ATP en la matriz."""
    return f"""
    <!-- ===== REACCIÓN DEL ACEPTOR FINAL DE ELECTRONES: O₂ ➔ H₂O ===== -->
    <g transform="translate(1150, 880)">
      {OXIGENO}
      <text x="18" y="86" fill="#dc2626" font-size="11" font-weight="900" text-anchor="middle">O₂</text>
    </g>
    <path d="M 1205 905 L 1300 905" fill="none" stroke="#dc2626" stroke-width="2.6" marker-end="url(#arrowElectron)"/>
    <g transform="translate(1315, 880)">
      {AGUA}
    </g>
    <text x="1345" y="972" fill="#0284c7" font-size="10.5" font-weight="900" text-anchor="middle">2 H₂O</text>
    <g transform="translate(1255, 1000)">
      <rect x="0" y="0" width="250" height="24" rx="12" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.6"/>
      <text x="125" y="16" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800"
            fill="#075985" text-anchor="middle">O₂ + 4 H⁺ + 4 e⁻ ➔ 2 H₂O</text>
    </g>

    <!-- ===== DONANTE 1: NADH (brazo matricial del Complejo I) ===== -->
    {crear_especie(60, 1052, "NADH", "10 H⁺ bombeados ➔ ≈ 2.5 ATP", NADH,
                   escala=0.68, dx_texto=178, pos_texto="derecha",
                   detalle2="Donado por el ciclo de Krebs y las lanzaderas")}
    <path d="M 160 1040 Q 170 1010 178 986" fill="none" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>

    <!-- ===== DONANTE 2: FADH₂ (a través de la ubiquinona) ===== -->
    {crear_especie(330, 1052, "FADH₂", "6 H⁺ bombeados ➔ ≈ 1.5 ATP", FADH2,
                   escala=0.62, dx_texto=118, pos_texto="derecha",
                   detalle2="Lanzadera del glicerol-3-P y β-oxidación")}
    <path d="M 430 1040 Q 450 940 466 846" fill="none" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>

    <!-- ===== SÍNTESIS DE ATP EN LA CABEZA F₁ ===== -->
    <g transform="translate(1300, 1082)">
      <rect x="0" y="0" width="150" height="34" rx="17" fill="#ffffff" stroke="#475569" stroke-width="1.8"/>
      <text x="75" y="22" font-family="'Inter', sans-serif" font-size="13" font-weight="900"
            fill="#334155" text-anchor="middle">ADP + Pi</text>
    </g>
    <path d="M 1455 1090 Q 1470 1040 1480 990" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

    <g transform="translate(1550, 1082)">
      <rect x="0" y="0" width="150" height="34" rx="17" fill="#dcfce7" stroke="#059669" stroke-width="2.2"/>
      <text x="75" y="23" font-family="'Inter', sans-serif" font-size="15" font-weight="900"
            fill="#065f46" text-anchor="middle">ATP + H₂O</text>
    </g>
    <path d="M 1580 985 Q 1600 1040 1615 1080" fill="none" stroke="#059669" stroke-width="2.6" marker-end="url(#arrowGreen)"/>
    <text x="1520" y="1140" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700"
          fill="#065f46" text-anchor="middle">Fosforilación oxidativa: la energía del gradiente se convierte en ATP</text>
    """


# -----------------------------------------------------------------------------
# 6. PANELES INFORMATIVOS UNIVERSITARIOS (INFERIOR DE LA MATRIZ)
# -----------------------------------------------------------------------------
def crear_paneles_informativos():
    contenido_q = f"""
      <g transform="translate(24, 66)">
        {UBIQUINONA}
        <text x="97" y="122" fill="#92400e" font-size="12" font-weight="900" text-anchor="middle">Ubiquinona (CoQ₁₀)</text>
        <text x="97" y="138" fill="#475569" font-size="10" text-anchor="middle">Forma oxidada • muy lipófila</text>
      </g>
      <g transform="translate(300, 66)">
        {UBIQUINOL}
        <text x="97" y="122" fill="#92400e" font-size="12" font-weight="900" text-anchor="middle">Ubiquinol (QH₂)</text>
        <text x="97" y="138" fill="#475569" font-size="10" text-anchor="middle">Forma reducida • dona 2 e⁻</text>
      </g>
      <g transform="translate(24, 232)">
        <rect x="0" y="0" width="742" height="34" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="1.4"/>
        <text x="14" y="22" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#92400e">
          CICLO Q (Complejo III): QH₂ ➔ Q•⁻ (semiquinona) ➔ Q; transfiere 1 e⁻ por cada una de sus dos ramas (bL / bH).
        </text>
      </g>
      <g transform="translate(24, 274)">
        <rect x="0" y="0" width="742" height="34" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4"/>
        <text x="14" y="22" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#334155">
          Brazo hidrofóbico: difunde dentro de la bicapa entre I, II y III, sin abandonar la membrana.
        </text>
      </g>
    """

    contenido_citc = f"""
      <g transform="translate(26, 70)">
        {CITOCROMO_C}
        <text x="80" y="146" fill="#0e7490" font-size="12" font-weight="900" text-anchor="middle">Citocromo c</text>
        <text x="80" y="162" fill="#475569" font-size="10" text-anchor="middle">Grupo hemo c • Fe³⁺ ⇄ Fe²⁺</text>
      </g>
      <g transform="translate(280, 74)">
        <rect x="0" y="0" width="486" height="104" rx="8" fill="#ecfeff" stroke="#0891b2" stroke-width="1.4"/>
        <text x="12" y="20" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0e7490">TRANSPORTADOR MÓVIL SOLUBLE DEL EIM</text>
        <text x="12" y="38" font-family="'Inter', sans-serif" font-size="9.5" fill="#155e75">• Transporta 1 solo electrón por molécula (no 2 como la ubiquinona).</text>
        <text x="12" y="54" font-family="'Inter', sans-serif" font-size="9.5" fill="#155e75">• 2 enlaces tioéter covalentes a Cys (hemo unido de forma irreversible).</text>
        <text x="12" y="70" font-family="'Inter', sans-serif" font-size="9.5" fill="#155e75">• Ligandos axiales: His18 (quinto) y Met80 (sexto).</text>
        <text x="12" y="88" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#0891b2">• Choca con cit c₁ (III) y con CuA (IV) en la cara externa de la MMI.</text>
      </g>
      <g transform="translate(26, 240)">
        <rect x="0" y="0" width="742" height="68" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.4"/>
        <text x="14" y="20" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#334155">PAPEL DEL CITOCROMO c EN LA APOPTOSIS</text>
        <text x="14" y="38" font-family="'Inter', sans-serif" font-size="9.5" fill="#475569">• Su liberación al citosol activa la caspasa-9 y la vía intrínseca de muerte celular programada.</text>
        <text x="14" y="54" font-family="'Inter', sans-serif" font-size="9.5" fill="#475569">• La forma mitocondrial es una proteína globular básica de ~12.4 kDa, muy conservada evolutivamente.</text>
      </g>
    """

    contenido_rendimiento = f"""
      <g transform="translate(20, 52)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a">BOMBEO DE PROTONES Y RELACIÓN P/O (ESTEQUIOMETRÍA MODERNA)</text>
        <rect x="0" y="10" width="750" height="116" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="1.3"/>
        <text x="12" y="30" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#92400e">DONANTE        H⁺ BOMBEADOS (I / III / IV)      H⁺ TOTALES      ATP ESTIMADOS</text>
        <text x="12" y="52" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#334155">NADH           4 / 4 / 2                       10              ≈ 2.5 ATP</text>
        <text x="12" y="72" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#334155">FADH₂          — / 4 / 2                       6               ≈ 1.5 ATP</text>
        <text x="12" y="92" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#334155">(desde el Complejo II los e⁻ entran directamente a la ubiquinona)</text>
        <text x="12" y="112" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#9a3412">Coste real ≈ 4 H⁺ por ATP (3 F₀F₁ + 1 translocasa ANT/Pi)</text>
      </g>
      <g transform="translate(20, 188)">
        <rect x="0" y="0" width="750" height="86" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.3"/>
        <text x="12" y="20" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#15803d">BALANCE FINAL DE LA RESPIRACIÓN CELULAR (GLUCOSA)</text>
        <text x="12" y="39" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#166534">Glucólisis (2 ATP + 2 NADH) + PDH (2 × 2.5 ATP) + Krebs (2 ATP + 6 NADH + 2 FADH₂)</text>
        <text x="12" y="57" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#166534">10 NADH × 2.5 + 2 FADH₂ × 1.5 + 4 ATP (sustrato) = 30 - 32 ATP por glucosa</text>
        <text x="12" y="76" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#047857">Rendimiento cercano al 34 % • el resto se disipa como calor corporal</text>
      </g>
      <g transform="translate(20, 288)">
        <rect x="0" y="0" width="750" height="80" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.3"/>
        <text x="12" y="20" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#334155">ACOPLAMIENTO Y CONTROL RESPIRATORIO</text>
        <text x="12" y="38" font-family="'Inter', sans-serif" font-size="9.5" fill="#475569">• La cadena está acoplada: sin ADP (estado 4) el bombeo de H⁺ se frena y el O₂ casi no se consume.</text>
        <text x="12" y="54" font-family="'Inter', sans-serif" font-size="9.5" fill="#475569">• Al aumentar [ADP] (estado 3) se acelera el flujo de electrones: control respiratorio.</text>
        <text x="12" y="70" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#0369a1">• Regulación por la disponibilidad de NADH/FADH₂ y por el potencial de membrana Δψ.</text>
      </g>
    """

    contenido_inhibidores = f"""
      <g transform="translate(20, 52)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a">INHIBIDORES ESPECÍFICOS DE CADA COMPLEJO (VENENOS Y FÁRMACOS)</text>
        <g transform="translate(0, 12)">
          <rect x="0" y="0" width="362" height="152" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.3"/>
          <text x="12" y="20" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800" fill="#991b1b">⊣ COMPLEJO I: Rotenona, Amital, Piericidina</text>
          <text x="12" y="38" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800" fill="#991b1b">⊣ COMPLEJO II: Malonato (competitivo con succinato)</text>
          <text x="12" y="56" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800" fill="#991b1b">⊣ COMPLEJO III: Antimicina A, Mixotiazol</text>
          <text x="12" y="74" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800" fill="#991b1b">⊣ COMPLEJO IV: Cianuro, CO, Azida, H₂S</text>
          <text x="12" y="92" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800" fill="#991b1b">⊣ ATP SINTASA: Oligomicina (subunidad c de F₀)</text>
          <text x="12" y="112" font-family="'Inter', sans-serif" font-size="9" fill="#7f1d1d">• Cianuro y CO bloquean el hema a₃: la respiración se detiene por completo.</text>
          <text x="12" y="128" font-family="'Inter', sans-serif" font-size="9" fill="#7f1d1d">• El malonato es un análogo estructural del succinato (inhibición competitiva).</text>
          <text x="12" y="144" font-family="'Inter', sans-serif" font-size="9" fill="#7f1d1d">• Con cianuro el gradiente de H⁺ desaparece y el NADH queda totalmente reducido.</text>
        </g>
        <g transform="translate(386, 12)">
          <rect x="0" y="0" width="364" height="152" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.3"/>
          <text x="12" y="20" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#1e40af">DESACOPLADORES Y TERMOGÉNESIS</text>
          <text x="12" y="40" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#1e3a8a">• 2,4-Dinitrofenol (DNP): transporta H⁺ a favor de gradiente</text>
          <text x="12" y="56" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#1e3a8a">• Valinomicina (ionóforo de K⁺) y FCCP (protón) rompen Δp</text>
          <text x="12" y="72" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#1e3a8a">• UCP1 = termogenina del tejido adiposo pardo</text>
          <text x="12" y="92" font-family="'Inter', sans-serif" font-size="9" fill="#1e3a8a">Al desacoplar, el flujo de e⁻ se acelera, el O₂ se consume</text>
          <text x="12" y="106" font-family="'Inter', sans-serif" font-size="9" fill="#1e3a8a">sin control y la energía sale como CALOR, no como ATP.</text>
          <text x="12" y="126" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#1d4ed8">Consecuencia: hipertermia (el DNP causó muertes en los años 30).</text>
          <text x="12" y="142" font-family="'Inter', sans-serif" font-size="9" fill="#1e3a8a">Fisiológicamente, UCP1 es la base de la producción de calor en hibernantes.</text>
        </g>
      </g>
    """

    return f"""
    <!-- ================================================================= -->
    <!-- PANELES EDUCATIVOS UNIVERSITARIOS (PARTE INFERIOR DE LA MATRIZ)   -->
    <!-- ================================================================= -->
    {crear_tarjeta(40, 1260, 790, 400, "ZOOM MOLECULAR: UBIQUINONA (CoQ₁₀) Y CICLO Q", COL_Q, "#fffbeb", contenido_q)}
    {crear_tarjeta(870, 1260, 790, 400, "ZOOM MOLECULAR: CITOCROMO c", COL_CYC, "#ecfeff", contenido_citc)}
    {crear_tarjeta(40, 1690, 790, 400, "ESTOEQUIOMETRÍA Y RENDIMIENTO ENERGÉTICO (P/O)", "#047857", "#f0fdf4", contenido_rendimiento)}
    {crear_tarjeta(870, 1690, 790, 400, "INHIBIDORES, DESACOPLADORES Y REGULACIÓN", "#dc2626", "#fef2f2", contenido_inhibidores)}
    """


def leyenda_final():
    """Franja de leyenda cromática del flujo de información del mapa."""
    return f"""
    <g transform="translate(40, 2110)">
      <rect x="0" y="0" width="1620" height="54" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
      <text x="24" y="23" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a">LEYENDA</text>
      <g transform="translate(110, 8)">
        <line x1="0" y1="8" x2="46" y2="8" stroke="#dc2626" stroke-width="2.6" stroke-dasharray="9 6"/>
        <text x="56" y="12" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#475569">Flujo de electrones (e⁻)</text>
      </g>
      <g transform="translate(340, 8)">
        <line x1="0" y1="8" x2="46" y2="8" stroke="#ea580c" stroke-width="3"/>
        <text x="56" y="12" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#475569">Bombeo de protones (H⁺)</text>
      </g>
      <g transform="translate(620, 8)">
        <rect x="0" y="0" width="16" height="16" rx="4" fill="#dcfce7" stroke="#059669" stroke-width="1.6"/>
        <text x="26" y="12" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#475569">Ganancia energética / poder reductor</text>
      </g>
      <g transform="translate(1000, 8)">
        <rect x="0" y="0" width="16" height="16" rx="4" fill="#ffedd5" stroke="#ea580c" stroke-width="1.6"/>
        <text x="26" y="12" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#475569">Grupo fosfato (Ⓟ)</text>
      </g>
      <g transform="translate(1270, 8)">
        <rect x="0" y="0" width="16" height="16" rx="4" fill="#fef2f2" stroke="#dc2626" stroke-width="1.6"/>
        <text x="26" y="12" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#475569">Inhibidor (⊣) / desacoplador</text>
      </g>
      <text x="24" y="44" font-family="'Inter', sans-serif" font-size="10" font-style="italic" fill="#64748b">
        Mapa 03 • Cadena Transportadora de Electrones y ATP Sintasa • Bioquímica Metabólica Universitaria
      </text>
    </g>
    """


# -----------------------------------------------------------------------------
# 7. ENSAMBLADO DEL MAPA
# -----------------------------------------------------------------------------
def construir_cuerpo_svg():
    partes = []

    # Capa de fondo: entorno celular y mitocondrial
    partes.append(generar_entorno_cte_svg(
        ancho=ANCHO_CANVAS, alto=ALTO_CANVAS,
        y_mme=Y_MME, y_eim_ini=Y_EIM_INI, y_eim_fin=Y_EIM_FIN,
        y_mmi_ini=Y_MMI_INI, y_mmi_fin=Y_MMI_FIN
    ))

    # Los cinco complejos incrustados en la bicapa
    partes.append(complejo_i())
    partes.append(complejo_ii())
    partes.append(complejo_iii())
    partes.append(complejo_iv())
    partes.append(atp_sintasa())

    # Flujo de electrones, de protones y reacciones de la matriz
    partes.append(ruta_electrones())
    partes.append(bombeo_protones())
    partes.append(reacciones_matriz())

    # Rótulos superiores de los complejos (chips)
    partes.append(crear_chip(60, 320, "Complejo I", "EC 1.6.5.3 • 4 H⁺", COL_I, COL_I_CLARO, 240))
    partes.append(crear_chip(385, 414, "Complejo II", "EC 1.3.5.1 • 0 H⁺", COL_II, COL_II_CLARO, 180))
    partes.append(crear_chip(1130, 414, "Complejo IV", "EC 7.1.1.9 • 2 H⁺", COL_IV, COL_IV_CLARO, 200))
    partes.append(crear_chip(1410, 414, "ATP Sintasa", "EC 7.1.2.2 • F₀F₁", COL_V, COL_V_CLARO, 200))

    # Paneles educativos y leyenda
    partes.append(crear_paneles_informativos())
    partes.append(leyenda_final())

    return "\n".join(partes)


def main():
    cuerpo = construir_cuerpo_svg()

    html_final = (
        CABECERA_HTML
        + f'    <svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" '
          f'viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">'
        + DEFS_MARCADORES
        + cuerpo
        + PIE_HTML
    )

    svg_final = (
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" '
        f'viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">\n'
        + DEFS_MARCADORES
        + cuerpo
        + "\n</svg>\n"
    )

    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_html = os.path.join(carpeta, "Cadena_Transporte_Electrones.html")
    ruta_svg = os.path.join(carpeta, "Cadena_Transporte_Electrones.svg")

    with open(ruta_html, "w", encoding="utf-8") as archivo:
        archivo.write(html_final)
    with open(ruta_svg, "w", encoding="utf-8") as archivo:
        archivo.write(svg_final)

    print(f"✅ ¡Mapa generado en HTML: {ruta_html}!")
    print(f"✅ ¡Mapa generado en SVG:  {ruta_svg}!")


if __name__ == "__main__":
    main()
