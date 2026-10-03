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

from entorno_cte import DEFS_ENTORNO_CTE, generar_entorno_cte_svg

# -----------------------------------------------------------------------------
# 1. GEOMETRÍA GENERAL DEL LIENZO
# -----------------------------------------------------------------------------
ANCHO_CANVAS = 1150
ALTO_CANVAS = 820

Y_MME = 90
Y_EIM_INI = 104
Y_EIM_FIN = 330
Y_MMI_INI = 330
Y_MMI_FIN = 430
Y_MATRIZ_INI = 430

# Coordenada X central de cada complejo
X_I, X_II, X_Q, X_III, X_CYC, X_IV, X_V = 120, 300, 405, 520, 620, 730, 950

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
    <!-- ===== COMPLEJO I: brazo transmembrana + brazo hidrofílico matricial ===== -->
    <rect x="45" y="336" width="150" height="88" rx="16"
          fill="{COL_I_CLARO}" stroke="{COL_I}" stroke-width="2.6"/>
    <path d="M 62 424 L 178 424 L 178 548 Q 178 562 164 562 L 76 562 Q 62 562 62 548 Z"
          fill="{COL_I_CLARO}" stroke="{COL_I}" stroke-width="2.6"/>

    <!-- Subunidades sugeridas -->
    <line x1="95" y1="338" x2="95" y2="422" stroke="{COL_I}" stroke-width="1" stroke-dasharray="4 4" opacity="0.5"/>
    <line x1="145" y1="338" x2="145" y2="422" stroke="{COL_I}" stroke-width="1" stroke-dasharray="4 4" opacity="0.5"/>
    <line x1="64" y1="492" x2="176" y2="492" stroke="{COL_I}" stroke-width="1" stroke-dasharray="4 4" opacity="0.5"/>

    <!-- Identificación dentro del propio complejo (sin chips flotantes) -->
    <text x="120" y="362" fill="{COL_I}" font-size="12" font-weight="900" text-anchor="middle" font-family="'Inter', sans-serif">Complejo I</text>
    <text x="120" y="380" fill="#0f172a" font-size="7.2" font-weight="700" text-anchor="middle" font-family="'Inter', sans-serif">NADH:ubiquinona oxidorreductasa</text>
    <text x="120" y="398" fill="#64748b" font-size="6.8" font-weight="700" text-anchor="middle"
          font-family="'JetBrains Mono', monospace">EC 1.6.5.3 • 4 H⁺ bombeados</text>

    <!-- Cadena FMN ➔ centros Fe-S -->
    <text x="120" y="440" fill="#0f172a" font-size="7" font-weight="800" text-anchor="middle">NADH ➔ FMN ➔ Fe-S ➔ Q</text>
    <circle cx="115" cy="456" r="5.5" fill="#f59e0b" stroke="#b45309" stroke-width="1.3"/>
    <text x="115" y="459" fill="#78350f" font-size="5.2" font-weight="900" text-anchor="middle">FMN</text>
    <circle cx="88" cy="488" r="4.5" fill="#dc2626" stroke="#991b1b" stroke-width="1.1"/>
    <circle cx="148" cy="506" r="4.5" fill="#dc2626" stroke="#991b1b" stroke-width="1.1"/>
    <circle cx="95" cy="528" r="4.5" fill="#dc2626" stroke="#991b1b" stroke-width="1.1"/>
    <text x="120" y="550" fill="#991b1b" font-size="6.8" font-weight="800" text-anchor="middle">8 centros [Fe-S]</text>
    """


def complejo_ii():
    """Complejo II: Succinato deshidrogenasa (única enzima del ciclo de Krebs unida a membrana)."""
    return f"""
    <!-- ===== COMPLEJO II: SDH (FAD covalente, no bombea protones) ===== -->
    <rect x="245" y="336" width="110" height="88" rx="16"
          fill="{COL_II_CLARO}" stroke="{COL_II}" stroke-width="2.6"/>
    <rect x="255" y="424" width="90" height="132" rx="16"
          fill="{COL_II_CLARO}" stroke="{COL_II}" stroke-width="2.6"/>

    <text x="300" y="362" fill="{COL_II}" font-size="12" font-weight="900" text-anchor="middle" font-family="'Inter', sans-serif">Complejo II</text>
    <text x="300" y="380" fill="#0f172a" font-size="7.2" font-weight="700" text-anchor="middle" font-family="'Inter', sans-serif">Succinato DH (SDH)</text>
    <text x="300" y="398" fill="#64748b" font-size="6.8" font-weight="700" text-anchor="middle"
          font-family="'JetBrains Mono', monospace">EC 1.3.5.1 • 0 H⁺</text>

    <!-- Subunidades SDHA / SDHB / SDHC-SDHD -->
    <rect x="264" y="436" width="72" height="22" rx="8" fill="#fef3c7" stroke="#b45309" stroke-width="1.2"/>
    <text x="300" y="451" fill="#78350f" font-size="6.8" font-weight="900" text-anchor="middle">SDHA • FAD</text>
    <rect x="264" y="464" width="72" height="22" rx="8" fill="#d1fae5" stroke="#047857" stroke-width="1.2"/>
    <text x="300" y="479" fill="#065f46" font-size="6.8" font-weight="900" text-anchor="middle">SDHB • [Fe-S]</text>
    <text x="300" y="504" fill="#0369a1" font-size="6.8" font-weight="800" text-anchor="middle">SDHC / SDHD (hemo b)</text>
    <text x="300" y="530" fill="#78350f" font-size="8" font-weight="800" text-anchor="middle">Succinato ➔ Fumarato</text>
    """


def complejo_iii():
    """Complejo III: Citocromo bc₁ con el ciclo Q (4 H⁺ bombeados)."""
    return f"""
    <!-- ===== COMPLEJO III: bc₁ con dominio soluble en el EIM ===== -->
    <rect x="450" y="336" width="140" height="88" rx="16"
          fill="{COL_III_CLARO}" stroke="{COL_III}" stroke-width="2.6"/>
    <rect x="472" y="258" width="96" height="78" rx="16"
          fill="{COL_III_CLARO}" stroke="{COL_III}" stroke-width="2.6"/>

    <text x="520" y="284" fill="{COL_III}" font-size="12" font-weight="900" text-anchor="middle">Complejo III</text>
    <text x="520" y="298" fill="#0f172a" font-size="7" font-weight="700" text-anchor="middle">Citocromo bc₁</text>
    <text x="520" y="312" fill="#64748b" font-size="6.8" font-weight="700" text-anchor="middle"
          font-family="'JetBrains Mono', monospace">EC 7.1.1.8 • 4 H⁺</text>
    <text x="520" y="326" fill="#4c1d95" font-size="6.8" font-weight="800" text-anchor="middle">Cit c₁ ➔ citocromo c</text>

    <!-- Grupos hemo bL / bH y ciclo Q -->
    <circle cx="482" cy="372" r="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.4"/>
    <text x="482" y="375" fill="#5b21b6" font-size="5.5" font-weight="900" text-anchor="middle">bL</text>
    <circle cx="558" cy="402" r="6" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.4"/>
    <text x="558" y="405" fill="#5b21b6" font-size="5.5" font-weight="900" text-anchor="middle">bH</text>
    <text x="520" y="360" fill="#5b21b6" font-size="8" font-weight="800" text-anchor="middle">Ciclo Q</text>
    <text x="520" y="390" fill="#0f172a" font-size="6.8" font-weight="700" text-anchor="middle">QH₂ ➔ Q•⁻ ➔ Q</text>
    <text x="520" y="418" fill="#0f172a" font-size="7" font-weight="800" text-anchor="middle">2 e⁻ • 4 H⁺ al EIM</text>
    """


def complejo_iv():
    """Complejo IV: Citocromo c oxidasa (reduce el O₂ a agua, 2 H⁺ bombeados)."""
    return f"""
    <!-- ===== COMPLEJO IV: citocromo c oxidasa (COX) ===== -->
    <rect x="660" y="336" width="140" height="88" rx="16"
          fill="{COL_IV_CLARO}" stroke="{COL_IV}" stroke-width="2.6"/>
    <rect x="678" y="424" width="104" height="108" rx="16"
          fill="{COL_IV_CLARO}" stroke="{COL_IV}" stroke-width="2.6"/>

    <text x="730" y="370" fill="{COL_IV}" font-size="12.5" font-weight="900" text-anchor="middle">Complejo IV</text>
    <text x="730" y="385" fill="#0f172a" font-size="7" font-weight="700" text-anchor="middle">Citocromo c oxidasa</text>
    <text x="730" y="400" fill="#64748b" font-size="6.8" font-weight="700" text-anchor="middle"
          font-family="'JetBrains Mono', monospace">EC 7.1.1.9 • 2 H⁺</text>

    <!-- Centros redox -->
    <circle cx="695" cy="450" r="6" fill="#fef3c7" stroke="#b45309" stroke-width="1.4"/>
    <text x="695" y="453" fill="#78350f" font-size="5.2" font-weight="900" text-anchor="middle">CuA</text>
    <circle cx="730" cy="472" r="6" fill="#fef3c7" stroke="#b45309" stroke-width="1.4"/>
    <text x="730" y="475" fill="#78350f" font-size="5.2" font-weight="900" text-anchor="middle">hema</text>
    <circle cx="765" cy="450" r="6" fill="#fef3c7" stroke="#b45309" stroke-width="1.4"/>
    <text x="765" y="453" fill="#78350f" font-size="5.2" font-weight="900" text-anchor="middle">CuB</text>

    <!-- Aceptor final de electrones -->
    <text x="730" y="506" fill="#7c2d12" font-size="7.5" font-weight="800" text-anchor="middle">O₂ + 4 H⁺ + 4 e⁻</text>
    <text x="730" y="521" fill="#7c2d12" font-size="7.5" font-weight="800" text-anchor="middle">➔ 2 H₂O</text>
    """


def atp_sintasa():
    """ATP sintasa (F₀F₁): motor rotatorio acoplado a la fuerza protón-motriz."""
    return f"""
    <!-- ===== ATP SINTASA (F₀F₁) ===== -->
    <!-- F₀: sector transmembrana (canal de protones) -->
    <rect x="880" y="336" width="130" height="88" rx="16"
          fill="{COL_V_CLARO}" stroke="{COL_V}" stroke-width="2.6"/>
    <!-- Eje central (subunidad γ) -->
    <rect x="932" y="424" width="26" height="42" rx="9" fill="#fda4af" stroke="{COL_V}" stroke-width="1.8"/>
    <!-- F₁: cabeza catalítica -->
    <rect x="862" y="466" width="166" height="150" rx="42"
          fill="{COL_V_CLARO}" stroke="{COL_V}" stroke-width="2.6"/>
    <!-- Tallo periférico (b₂ / OSCP) -->
    <path d="M 850 372 L 850 546 Q 850 578 872 586"
          fill="none" stroke="{COL_V}" stroke-width="8" stroke-linecap="round" opacity="0.7"/>

    <text x="945" y="350" fill="#9f1239" font-size="8" font-weight="900" text-anchor="middle">F₀</text>
    <text x="945" y="370" fill="{COL_V}" font-size="12" font-weight="900" text-anchor="middle">ATP Sintasa</text>
    <text x="945" y="385" fill="#0f172a" font-size="7" font-weight="700" text-anchor="middle">F₀F₁ (Complejo V)</text>
    <text x="945" y="400" fill="#64748b" font-size="6.8" font-weight="700" text-anchor="middle"
          font-family="'JetBrains Mono', monospace">EC 7.1.2.2</text>

    <!-- Cabeza F₁ con las tres conformaciones catalíticas -->
    <text x="945" y="492" fill="{COL_V}" font-size="11" font-weight="900" text-anchor="middle">F₁</text>
    <circle cx="905" cy="524" r="15" fill="#ffffff" stroke="{COL_V}" stroke-width="1.6"/>
    <text x="905" y="528" fill="#9f1239" font-size="8" font-weight="900" text-anchor="middle">β-L</text>
    <circle cx="985" cy="524" r="15" fill="#ffffff" stroke="{COL_V}" stroke-width="1.6"/>
    <text x="985" y="528" fill="#9f1239" font-size="8" font-weight="900" text-anchor="middle">β-T</text>
    <circle cx="945" cy="566" r="15" fill="#ffffff" stroke="{COL_V}" stroke-width="1.6"/>
    <text x="945" y="570" fill="#9f1239" font-size="8" font-weight="900" text-anchor="middle">β-O</text>
    <text x="945" y="602" fill="#9f1239" font-size="6.8" font-weight="800" text-anchor="middle">Rotación γ • 3 H⁺ / vuelta</text>
    """


# -----------------------------------------------------------------------------
# 5. ELEMENTOS DE FLUJO: ELECTRONES Y PROTONES
# -----------------------------------------------------------------------------
def ruta_electrones():
    """Trazado discontinuo del flujo de electrones: I/II ➔ Q ➔ III ➔ cit c ➔ IV ➔ O₂."""
    return f"""
    <!-- ===== FLUJO DE ELECTRONES (línea roja discontinua sobre la bicapa) ===== -->
    <g fill="none" stroke="#dc2626" stroke-width="2.2" stroke-dasharray="8 5">
      <!-- Complejo I ➔ Q (arco superior que evita cortar el Complejo II) -->
      <path d="M 195 352 C 220 326, 370 326, 395 365" marker-end="url(#arrowElectron)"/>
      <path d="M 355 380 L 381 380" marker-end="url(#arrowElectron)"/>
      <path d="M 429 380 L 446 380" marker-end="url(#arrowElectron)"/>
      <path d="M 590 380 L 599 380" marker-end="url(#arrowElectron)"/>
      <path d="M 641 380 L 656 380" marker-end="url(#arrowElectron)"/>
    </g>

    <!-- Transportador móvil liposoluble: UBIQUINONA (Q ⇄ QH₂) -->
    <g transform="translate({X_Q}, 380)">
      <polygon points="0,-16 14,-8 14,8 0,16 -14,8 -14,-8"
               fill="#fef3c7" stroke="{COL_Q}" stroke-width="2"/>
      <text x="0" y="4" fill="#92400e" font-size="9.5" font-weight="900" text-anchor="middle">Q</text>
    </g>
    <text x="{X_Q}" y="412" fill="#92400e" font-size="8" font-weight="900" text-anchor="middle">Q ⇄ QH₂</text>

    <!-- Transportador móvil soluble: CITOCROMO c -->
    <g transform="translate({X_CYC}, 380)">
      <circle cx="0" cy="0" r="18" fill="#cffafe" stroke="{COL_CYC}" stroke-width="2.2"/>
      <text x="0" y="4" fill="#0e7490" font-size="8.5" font-weight="900" text-anchor="middle">cit c</text>
    </g>
    <text x="{X_CYC}" y="412" fill="#0e7490" font-size="8" font-weight="900" text-anchor="middle">Fe³⁺ ⇄ Fe²⁺</text>
    """


def bombeo_protones():
    """Arcos de bombeo de H⁺ desde la matriz hacia el EIM a través de I, III y IV."""
    return f"""
    <!-- ===== BOMBEO DE PROTONES H⁺ (matriz ➔ EIM) ===== -->
    <g fill="none" stroke="#ea580c" stroke-width="2.8" stroke-linecap="round">
      <path d="M 182 434 Q 235 392 235 330 Q 235 262 190 226" marker-end="url(#arrowFlow)"/>
      <path d="M 578 434 Q 630 392 630 330 Q 630 264 590 230" marker-end="url(#arrowFlow)"/>
      <path d="M 792 434 Q 830 392 830 330 Q 830 268 806 240" marker-end="url(#arrowFlow)"/>
    </g>
    <g font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c">
      <text x="250" y="266">4 H⁺</text>
      <text x="646" y="272">4 H⁺</text>
      <text x="844" y="292">2 H⁺</text>
    </g>

    <!-- ===== RETORNO DE PROTONES POR LA ATP SINTASA (EIM ➔ matriz) ===== -->
    <path d="M 1020 236 Q 1090 290 1085 346 Q 1080 398 1010 424 Q 972 440 950 462"
          fill="none" stroke="#ea580c" stroke-width="3.2" stroke-linecap="round" marker-end="url(#arrowFlow)"/>
    <text x="988" y="286" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c">≈ 4 H⁺</text>
    <text x="988" y="300" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c">por ATP</text>

    <!-- Acoplamiento quimiosmótico (cartel de estilo) -->
    <g transform="translate(60, 150)">
      <rect x="0" y="0" width="330" height="42" rx="10" fill="#ffffff" stroke="#ea580c" stroke-width="1.6" opacity="0.95"/>
      <text x="165" y="17" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#9a3412" text-anchor="middle">
        ACOPLAMIENTO QUIMIOSMÓTICO (MITCHELL, 1961)
      </text>
      <text x="165" y="32" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#475569" text-anchor="middle">
        El gradiente de H⁺ (Δp) impulsa la síntesis de ATP
      </text>
    </g>
    """


def reacciones_matriz():
    """Donantes de electrones, reducción del O₂ y síntesis de ATP en la matriz."""
    return f"""
    <!-- ===== DONANTE 1: NADH ➔ Complejo I ===== -->
    <g transform="translate(40, 620)">
      <rect x="0" y="0" width="150" height="54" rx="10" fill="#dcfce7" stroke="#059669" stroke-width="1.8"/>
      <text x="75" y="20" font-family="'Inter', sans-serif" font-size="13" font-weight="900"
            fill="#065f46" text-anchor="middle">NADH + H⁺</text>
      <text x="75" y="34" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700"
            fill="#047857" text-anchor="middle">10 H⁺ bombeados</text>
      <text x="75" y="47" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700"
            fill="#047857" text-anchor="middle">≈ 2.5 ATP</text>
    </g>
    <path d="M 115 616 L 115 570" fill="none" stroke="#059669" stroke-width="2.4" marker-end="url(#arrowGreen)"/>
    <text x="126" y="598" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#047857">e⁻</text>

    <!-- ===== DONANTE 2: FADH₂ ➔ Complejo II (vía ubiquinona) ===== -->
    <g transform="translate(240, 620)">
      <rect x="0" y="0" width="150" height="54" rx="10" fill="#dcfce7" stroke="#059669" stroke-width="1.8"/>
      <text x="75" y="20" font-family="'Inter', sans-serif" font-size="13" font-weight="900"
            fill="#065f46" text-anchor="middle">FADH₂</text>
      <text x="75" y="34" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700"
            fill="#047857" text-anchor="middle">6 H⁺ bombeados</text>
      <text x="75" y="47" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700"
            fill="#047857" text-anchor="middle">≈ 1.5 ATP</text>
    </g>
    <path d="M 315 616 Q 315 590 302 568" fill="none" stroke="#059669" stroke-width="2.4" marker-end="url(#arrowGreen)"/>
    <text x="322" y="598" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#047857">e⁻</text>

    <!-- ===== SÍNTESIS DE ATP EN LA CABEZA F₁ (fosforilación oxidativa) ===== -->
    <g transform="translate(860, 646)">
      <rect x="0" y="0" width="170" height="32" rx="16" fill="#ffffff" stroke="#475569" stroke-width="1.8"/>
      <text x="85" y="21" font-family="'Inter', sans-serif" font-size="12" font-weight="900"
            fill="#334155" text-anchor="middle">ADP + Pi</text>
    </g>
    <path d="M 945 642 L 945 622" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>

    <g transform="translate(860, 700)">
      <rect x="0" y="0" width="170" height="34" rx="17" fill="#dcfce7" stroke="#059669" stroke-width="2.2"/>
      <text x="85" y="23" font-family="'Inter', sans-serif" font-size="14" font-weight="900"
            fill="#065f46" text-anchor="middle">ATP + H₂O</text>
    </g>
    <path d="M 1032 610 Q 1085 660 1035 698" fill="none" stroke="#059669" stroke-width="2.4" marker-end="url(#arrowGreen)"/>
    <text x="945" y="756" font-family="'Inter', sans-serif" font-size="9" font-weight="700"
          fill="#065f46" text-anchor="middle">Fosforilación oxidativa</text>
    """


# -----------------------------------------------------------------------------
# 6. PANELES INFORMATIVOS UNIVERSITARIOS (INFERIOR DE LA MATRIZ)
# -----------------------------------------------------------------------------
def crear_paneles_informativos():
    contenido_q = f"""
      <g transform="translate(20, 54)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#92400e">¿QUÉ ES LA UBIQUINONA (CoQ₁₀)?</text>
        <text x="0" y="20" font-family="'Inter', sans-serif" font-size="9.5" fill="#334155">• Benzoquinona con cola isoprenoide de 10 unidades, marcadamente lipófila.</text>
        <text x="0" y="38" font-family="'Inter', sans-serif" font-size="9.5" fill="#334155">• Único transportador móvil NO proteico: difunde dentro de la bicapa.</text>
        <text x="0" y="56" font-family="'Inter', sans-serif" font-size="9.5" fill="#334155">• Recoge los electrones del Complejo I y del Complejo II.</text>
      </g>
      <g transform="translate(20, 148)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#92400e">CICLO Q (Complejo III: bifurcación de electrones)</text>
        <rect x="0" y="10" width="490" height="30" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="1.3"/>
        <text x="12" y="30" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="800" fill="#9a3412">QH₂  ➔  Q•⁻ (semiquinona)  ➔  Q</text>
        <text x="0" y="58" font-family="'Inter', sans-serif" font-size="9.5" fill="#334155">• Rama de baja energía (hemo bL ➔ bH): reduce Q a semiquinona.</text>
        <text x="0" y="76" font-family="'Inter', sans-serif" font-size="9.5" fill="#334155">• Rama de alta energía (Rieske ➔ cit c₁): reduce al citocromo c.</text>
        <text x="0" y="94" font-family="'Inter', sans-serif" font-size="9.5" fill="#334155">• Se transfieren 2 e⁻ por ciclo y se translocan 4 H⁺ al EIM.</text>
      </g>
      <g transform="translate(20, 278)">
        <rect x="0" y="0" width="490" height="112" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="1.3"/>
        <text x="12" y="20" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#92400e">ESCALA DE POTENCIALES DE REDUCCIÓN (E°')</text>
        <text x="12" y="42" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#334155">NAD⁺ / NADH .......... −0.32 V</text>
        <text x="12" y="60" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#334155">Q / QH₂ .................. +0.04 V</text>
        <text x="12" y="78" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#334155">cit c (Fe³⁺/Fe²⁺) ...... +0.22 V</text>
        <text x="12" y="96" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#334155">O₂ / H₂O ................ +0.82 V</text>
      </g>
    """

    contenido_citc = f"""
      <g transform="translate(20, 54)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0e7490">¿QUÉ ES EL CITOCROMO c?</text>
        <text x="0" y="20" font-family="'Inter', sans-serif" font-size="9.5" fill="#334155">• Proteína globular soluble (~12.4 kDa) del espacio intermembrana.</text>
        <text x="0" y="38" font-family="'Inter', sans-serif" font-size="9.5" fill="#334155">• Hemo c unido de forma covalente por dos enlaces tioéter a Cys.</text>
        <text x="0" y="56" font-family="'Inter', sans-serif" font-size="9.5" fill="#334155">• Transporta UN solo electrón entre el Complejo III y el Complejo IV.</text>
        <text x="0" y="74" font-family="'Inter', sans-serif" font-size="9.5" fill="#334155">• Ciclo redox del hierro: Fe³⁺ ⇄ Fe²⁺; nunca abandona el EIM.</text>
      </g>
      <g transform="translate(20, 148)">
        <rect x="0" y="0" width="490" height="112" rx="8" fill="#ecfeff" stroke="#0891b2" stroke-width="1.3"/>
        <text x="12" y="20" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#0e7490">ESTRUCTURA Y LIGANDOS AXIALES</text>
        <text x="12" y="40" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#155e75">• Ligando axial proximal: His18</text>
        <text x="12" y="58" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#155e75">• Ligando axial distal: Met80</text>
        <text x="12" y="76" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#155e75">• Cadena polipeptídica de ~104 residuos</text>
        <text x="12" y="96" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#0891b2">• Permite el salto de e⁻ del cit c₁ (III) hacia CuA (IV).</text>
      </g>
      <g transform="translate(20, 278)">
        <rect x="0" y="0" width="490" height="112" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.3"/>
        <text x="12" y="20" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#334155">PAPEL DEL CITOCROMO c EN LA APOPTOSIS</text>
        <text x="12" y="40" font-family="'Inter', sans-serif" font-size="9.5" fill="#475569">• Su liberación al citosol activa la caspasa-9 (vía intrínseca).</text>
        <text x="12" y="58" font-family="'Inter', sans-serif" font-size="9.5" fill="#475569">• Forma el apoptosoma junto con Apaf-1 y el citocromo c.</text>
        <text x="12" y="76" font-family="'Inter', sans-serif" font-size="9.5" fill="#475569">• Es una de las proteínas más conservadas de la evolución.</text>
        <text x="12" y="96" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#0369a1">• También actúa como eliminador de radicales superóxido.</text>
      </g>
    """

    contenido_rendimiento = f"""
      <g transform="translate(20, 54)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a">BOMBEO DE PROTONES POR COMPLEJO</text>
        <rect x="0" y="10" width="490" height="106" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="1.3"/>
        <text x="12" y="28" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#92400e">DONANTE     I / III / IV     H⁺ TOTALES</text>
        <text x="12" y="48" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#334155">NADH        4 / 4 / 2         10</text>
        <text x="12" y="68" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#334155">FADH₂       — / 4 / 2          6</text>
        <text x="12" y="88" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#334155">Succinato   —  / —  / —        0</text>
        <text x="12" y="106" font-family="'Inter', sans-serif" font-size="9" fill="#9a3412">El Complejo II no bombea: cede los e⁻ directamente a la ubiquinona.</text>
      </g>
      <g transform="translate(20, 194)">
        <text x="0" y="0" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a">RELACIÓN P/O Y COSTE REAL DEL ATP</text>
        <rect x="0" y="10" width="490" height="96" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.3"/>
        <text x="12" y="30" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#334155">NADH:  10 H⁺ ÷ 4 = 2.5 ATP</text>
        <text x="12" y="50" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#334155">FADH₂:  6 H⁺ ÷ 4 = 1.5 ATP</text>
        <text x="12" y="70" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#9a3412">Coste = 4 H⁺ por ATP</text>
        <text x="12" y="88" font-family="'Inter', sans-serif" font-size="9" fill="#475569">3 H⁺ por la F₀F₁ + 1 H⁺ por la translocasa ANT/Pi.</text>
      </g>
      <g transform="translate(20, 330)">
        <rect x="0" y="0" width="490" height="60" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.3"/>
        <text x="12" y="20" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#15803d">BALANCE FINAL DE LA RESPIRACIÓN CELULAR</text>
        <text x="12" y="38" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#166534">10 NADH × 2.5 + 2 FADH₂ × 1.5 + 4 ATP = 30 - 32 ATP / glucosa</text>
        <text x="12" y="54" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#047857">Rendimiento ≈ 34 % • el resto se disipa como calor corporal.</text>
      </g>
    """

    contenido_inhibidores = f"""
      <g transform="translate(20, 54)">
        <rect x="0" y="0" width="490" height="182" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.3"/>
        <text x="12" y="20" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#991b1b">INHIBIDORES ESPECÍFICOS (⊣)</text>
        <text x="12" y="42" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#991b1b">⊣ Complejo I: rotenona, amital, piericidina</text>
        <text x="12" y="60" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#991b1b">⊣ Complejo II: malonato (competitivo con succinato)</text>
        <text x="12" y="78" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#991b1b">⊣ Complejo III: antimicina A, mixotiazol</text>
        <text x="12" y="96" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#991b1b">⊣ Complejo IV: cianuro, CO, azida, H₂S</text>
        <text x="12" y="114" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#991b1b">⊣ ATP sintasa: oligomicina (subunidad c de F₀)</text>
        <text x="12" y="136" font-family="'Inter', sans-serif" font-size="9" fill="#7f1d1d">• Cianuro y CO bloquean el hemo a₃: paro respiratorio total.</text>
        <text x="12" y="152" font-family="'Inter', sans-serif" font-size="9" fill="#7f1d1d">• El malonato es un análogo estructural del succinato.</text>
        <text x="12" y="168" font-family="'Inter', sans-serif" font-size="9" fill="#7f1d1d">• Con cianuro el NADH queda totalmente reducido y Δp colapsa.</text>
      </g>
      <g transform="translate(20, 262)">
        <rect x="0" y="0" width="490" height="128" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.3"/>
        <text x="12" y="20" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#1e40af">DESACOPLADORES Y TERMOGÉNESIS</text>
        <text x="12" y="42" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#1e3a8a">• 2,4-dinitrofenol (DNP): transporta H⁺ a favor de gradiente</text>
        <text x="12" y="60" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#1e3a8a">• FCCP y valinomicina: colapsan la fuerza protón-motriz</text>
        <text x="12" y="78" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#1e3a8a">• UCP1 (termogenina) del tejido adiposo pardo</text>
        <text x="12" y="100" font-family="'Inter', sans-serif" font-size="9" fill="#1e3a8a">El flujo de e⁻ se acelera y la energía se disipa como CALOR, no como ATP.</text>
        <text x="12" y="118" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#1d4ed8">Consecuencia clínica: hipertermia (el DNP causó muertes en los años 30).</text>
      </g>
    """

    return f"""
    <!-- ================================================================= -->
    <!-- PANELES EDUCATIVOS UNIVERSITARIOS (PARTE INFERIOR DE LA MATRIZ)   -->
    <!-- ================================================================= -->
    {crear_tarjeta(30, 790, 530, 410, "ZOOM MOLECULAR: UBIQUINONA (CoQ₁₀) Y CICLO Q", COL_Q, "#fffbeb", contenido_q)}
    {crear_tarjeta(590, 790, 530, 410, "ZOOM MOLECULAR: CITOCROMO c", COL_CYC, "#ecfeff", contenido_citc)}
    {crear_tarjeta(30, 1220, 530, 410, "ESTOEQUIOMETRÍA P/O Y RENDIMIENTO ENERGÉTICO", "#047857", "#f0fdf4", contenido_rendimiento)}
    {crear_tarjeta(590, 1220, 530, 410, "INHIBIDORES, DESACOPLADORES Y REGULACIÓN", "#dc2626", "#fef2f2", contenido_inhibidores)}
    """


def leyenda_final():
    """Franja de leyenda cromática del flujo de información del mapa."""
    return f"""
    <g transform="translate(30, 1655)">
      <rect x="0" y="0" width="1090" height="54" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>
      <text x="20" y="23" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a">LEYENDA</text>
      <g transform="translate(95, 8)">
        <line x1="0" y1="8" x2="40" y2="8" stroke="#dc2626" stroke-width="2.4" stroke-dasharray="8 5"/>
        <text x="48" y="12" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#475569">Flujo de electrones (e⁻)</text>
      </g>
      <g transform="translate(265, 8)">
        <line x1="0" y1="8" x2="40" y2="8" stroke="#ea580c" stroke-width="2.8"/>
        <text x="48" y="12" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#475569">Bombeo de protones (H⁺)</text>
      </g>
      <g transform="translate(470, 8)">
        <rect x="0" y="0" width="15" height="15" rx="4" fill="#dcfce7" stroke="#059669" stroke-width="1.5"/>
        <text x="23" y="12" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#475569">Ganancia / poder reductor</text>
      </g>
      <g transform="translate(680, 8)">
        <rect x="0" y="0" width="15" height="15" rx="4" fill="#ffedd5" stroke="#ea580c" stroke-width="1.5"/>
        <text x="23" y="12" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#475569">Grupo fosfato (Ⓟ)</text>
      </g>
      <g transform="translate(870, 8)">
        <rect x="0" y="0" width="15" height="15" rx="4" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
        <text x="23" y="12" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#475569">Inhibidor (⊣) / desacoplador</text>
      </g>
      <text x="20" y="44" font-family="'Inter', sans-serif" font-size="9.5" font-style="italic" fill="#64748b">
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

    # Paneles educativos y leyenda (¡Eliminados a petición del usuario para ahorrar espacio!)
    # partes.append(crear_paneles_informativos())
    # partes.append(leyenda_final())

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
