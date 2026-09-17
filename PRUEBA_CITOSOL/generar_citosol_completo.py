#!/usr/bin/env python3
"""
CITOSOL METABÓLICO INTEGRADO: GLUCÓLISIS + PENTOSAS FOSFATO + INTERCONEXIONES
=============================================================================
Este módulo une de forma real, biológica y sin choques:
1. El eje principal de la Glucólisis (11 metabolitos y 10 reacciones).
2. La Vía de las Pentosas Fosfato completa (Fase Oxidativa y No Oxidativa con
   Transcetolasa 1, Transaldolasa y Transcetolasa 2, con sus 10 metabolitos).
3. Las 3 interconexiones de retorno biológico:
   - Salida desde G6P hacia G6PDH.
   - Retorno de Fructosa-6-Fosfato hacia la Glucólisis.
   - Retorno de Gliceraldehído-3-Fosfato hacia la Glucólisis.
4. Entorno de Citosol Celular real: Membrana plasmática superior con GLUT,
   citoesqueleto, polirribosomas, Glucógeno a la izquierda, fermentación láctica (LDH)
   y Mitocondria biológica inferior con transportador MPC.
5. Diseño editorial limpio estilo libro de texto universitario (Lehninger / Stryer):
   sin índices ni barras que tapen el contenido.
"""

import os
import sys

# Rutas a los módulos existentes
DIR_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(DIR_RAIZ, "01_CARBOHIDRATOS", "01_glucolisis"))
sys.path.append(os.path.join(DIR_RAIZ, "01_CARBOHIDRATOS", "04_via_pentosas_fosfato"))

from estructuras_glucosa import (
    GLUCOSA,
    GLUCOSA_6_FOSFATO,
    FRUCTOSA_6_FOSFATO,
    FRUCTOSA_1_6_BISFOSFATO,
    DIHIDROXIACETONA_FOSFATO,
    GLICERALDEHIDO_3_FOSFATO,
    BISFOSFOGLICERATO_1_3,
    FOSFOGLICERATO_3,
    FOSFOGLICERATO_2,
    FOSFOENOLPIRUVATO,
    PIRUVATO
)

from estructuras_pentosas import (
    FOSFOGLUCONO_LACTONA_6,
    FOSFOGLUCONATO_6,
    RIBULOSA_5_FOSFATO,
    RIBOSA_5_FOSFATO,
    XILULOSA_5_FOSFATO,
    SEDOHEPTULOSA_7_FOSFATO,
    ERITROSA_4_FOSFATO
)

# Dimensiones del lienzo editorial integrado
ANCHO_CANVAS = 2200
ALTO_CANVAS = 2450

# -----------------------------------------------------------------------------
# ESTRUCTURAS QUÍMICAS ADICIONALES DEL CITOSOL (ESTILO EDITORIAL)
# -----------------------------------------------------------------------------
ESTRUCTURA_LACTATO = """
<g id="mol-lactato-editorial">
  <!-- Proyección de Fischer para L-Lactato -->
  <text x="50" y="15" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">COO⁻</text>
  <line x1="50" y1="20" x2="50" y2="40" stroke="#0f172a" stroke-width="2"/>
  <line x1="20" y1="40" x2="80" y2="40" stroke="#0f172a" stroke-width="2"/>
  <text x="15" y="44" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="600" fill="#0f172a" text-anchor="end">H</text>
  <text x="85" y="44" font-family="'JetBrains Mono', monospace" font-size="13" font-weight="600" fill="#0284c7" text-anchor="start">OH</text>
  <line x1="50" y1="40" x2="50" y2="60" stroke="#0f172a" stroke-width="2"/>
  <text x="50" y="74" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">CH₃</text>
</g>
"""

ESTRUCTURA_GLUCOGENO = """
<g id="mol-glucogeno-editorial">
  <!-- Representación de gránulo de glucógeno con ramificaciones -->
  <circle cx="50" cy="45" r="32" fill="#fffbeb" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4,3"/>
  <circle cx="50" cy="45" r="7" fill="#d97706"/>
  <circle cx="36" cy="33" r="5" fill="#f59e0b"/>
  <circle cx="64" cy="33" r="5" fill="#f59e0b"/>
  <circle cx="34" cy="57" r="5" fill="#f59e0b"/>
  <circle cx="66" cy="57" r="5" fill="#f59e0b"/>
  <circle cx="50" cy="22" r="4" fill="#fbbf24"/>
  <circle cx="24" cy="45" r="4" fill="#fbbf24"/>
  <circle cx="76" cy="45" r="4" fill="#fbbf24"/>
  <circle cx="50" cy="68" r="4" fill="#fbbf24"/>
  <line x1="50" y1="45" x2="36" y2="33" stroke="#d97706" stroke-width="1.8"/>
  <line x1="50" y1="45" x2="64" y2="33" stroke="#d97706" stroke-width="1.8"/>
  <line x1="50" y1="45" x2="34" y2="57" stroke="#d97706" stroke-width="1.8"/>
  <line x1="50" y1="45" x2="66" y2="57" stroke="#d97706" stroke-width="1.8"/>
</g>
"""

# -----------------------------------------------------------------------------
# GENERADORES DE ELEMENTOS BIOLÓGICOS Y METABÓLICOS
# -----------------------------------------------------------------------------
def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False):
    """Construye el bloque SVG de un metabolito con su estructura y textos alineados."""
    if texto_izquierda:
        pos_estructura = "translate(150, 0)"
        pos_texto = "translate(130, 25)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = "translate(135, 25)"
        alineacion = ''

    return f"""
    <!-- Metabolito: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="{pos_estructura}">
        {svg_estructura}
      </g>
      <g transform="{pos_texto}">
        <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="800" {alineacion}>{nombre}</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700" {alineacion}>{carbonos}</text>
        <text x="0" y="34" fill="#64748b" font-size="11" {alineacion}>{detalle}</text>
      </g>
    </g>
    """

def crear_reaccion(x, y, enzima, ec="", regulacion="", entra_energia="", sale_energia="", 
                   reversible=False, es_ganancia=False, salida_agua=False, altura=48):
    """Genera una reacción vertical limpia con cofactores y enzimas."""
    curvas_energia = ""
    
    if entra_energia:
        color_entrada = "#dc2626" if not es_ganancia else "#475569"
        marcador_entrada = "url(#arrowRed)" if not es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -75 8 Q -25 8 -4 18" fill="none" stroke="{color_entrada}" stroke-width="1.8" marker-end="{marcador_entrada}"/>
        <text x="-80" y="11" fill="{color_entrada}" font-size="11" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
        
    if sale_energia:
        color_salida = "#059669" if es_ganancia else "#475569"
        marcador_salida = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -4 24 Q -25 34 -75 34" fill="none" stroke="{color_salida}" stroke-width="1.8" marker-end="{marcador_salida}"/>
        <text x="-80" y="37" fill="{color_salida}" font-size="11" font-weight="800" text-anchor="end">{sale_energia}</text>
        """

    if salida_agua:
        curvas_energia += """
        <path d="M -4 24 Q -25 34 -70 34" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-75" y="37" fill="#0284c7" font-size="11" font-weight="800" text-anchor="end">- 2 H₂O</text>
        """

    if reversible:
        flecha = f"""
        <line x1="-3" y1="0" x2="-3" y2="{altura}" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        <line x1="3" y1="{altura}" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        """
    else:
        flecha = f"""
        <line x1="0" y1="0" x2="0" y2="{altura}" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="26" fill="{color_reg}" font-size="10" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha}
      {curvas_energia}
      <g transform="translate(18, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">{enzima}</text>
        <text x="0" y="13" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """

def crear_reaccion_oxidativa(x, y, enzima, ec="", regulacion="", genera_nadph=False, entra_agua=False, salida_co2=False, altura=48):
    """Genera una reacción de la fase oxidativa de pentosas fosfato."""
    curvas = ""
    if genera_nadph:
        curvas += """
        <path d="M -65 8 Q -25 8 -4 18" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="-70" y="11" fill="#475569" font-size="10.5" font-weight="800" text-anchor="end">+ NADP⁺</text>
        <path d="M -4 24 Q -25 34 -70 34" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
        <text x="-75" y="38" fill="#059669" font-size="10.5" font-weight="800" text-anchor="end">+ NADPH + H⁺</text>
        """
    if entra_agua:
        curvas += """
        <path d="M -65 8 Q -25 8 -4 18" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-70" y="11" fill="#0284c7" font-size="10.5" font-weight="800" text-anchor="end">+ H₂O</text>
        """
    if salida_co2:
        curvas += """
        <path d="M 4 24 Q 25 34 65 34" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="70" y="38" fill="#475569" font-size="10.5" font-weight="800">+ CO₂</text>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="26" fill="{color_reg}" font-size="9.5" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción Oxidativa: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="0" y1="0" x2="0" y2="{altura}" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      {curvas}
      <g transform="translate(18, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">{enzima}</text>
        <text x="0" y="13" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """

def crear_paso_no_oxidativo(x, y, enzima, ec, sustratos_txt, productos_txt):
    """Genera un nodo de transferencia no oxidativa (Transcetolasa / Transaldolasa)."""
    return f"""
    <!-- Reacción de Transferencia: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="-3" y1="0" x2="-3" y2="45" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="45" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>

      <g transform="translate(18, 10)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">{ec}</text>
        <text x="0" y="28" fill="#c2410c" font-size="10" font-weight="700">{sustratos_txt} ⇄ {productos_txt}</text>
      </g>
    </g>
    """

# -----------------------------------------------------------------------------
# DIBUJO DEL ENTORNO BIOLÓGICO CELULAR COMPLETO
# -----------------------------------------------------------------------------
def generar_entorno_celular_citosol(ancho, alto):
    """Genera la anatomía celular biológica envolvente (Membrana, Citosol y Mitocondria)."""
    return f"""
    <!-- Fondo Citoplasmático Acuoso -->
    <rect width="{ancho}" height="{alto}" fill="#ffffff"/>
    <rect width="{ancho}" height="{alto}" fill="url(#gradCitosolLuz)"/>

    <!-- ============================================================= -->
    <!-- MEMBRANA PLASMÁTICA CELULAR (ARRIBA)                           -->
    <!-- ============================================================= -->
    <!-- Medio Extracelular / Sangre -->
    <path d="M 0 0 L {ancho} 0 L {ancho} 80 Q {ancho*0.5} 90 0 80 Z" fill="#f1f5f9"/>
    <line x1="0" y1="80" x2="{ancho}" y2="80" stroke="#cbd5e1" stroke-width="2"/>

    <!-- Bicapa lipídica ondulada -->
    <g stroke="#0284c7" stroke-width="2.5" fill="none">
      <path d="M 0 82 Q 400 95 900 80 T 1800 85 T {ancho} 80" />
      <path d="M 0 94 Q 400 107 900 92 T 1800 97 T {ancho} 92" />
    </g>
    <!-- Cabezas polares de fosfolípidos -->
    <g fill="#38bdf8" opacity="0.6">
      {' '.join([f'<circle cx="{i}" cy="{82 + (i%5)}" r="2.5"/><circle cx="{i}" cy="{94 + (i%5)}" r="2.5"/>' for i in range(15, ancho, 25)])}
    </g>

    <!-- TRANSPORTADOR GLUT-4 (ARRIBA A LA IZQUIERDA, EJE GLUCOLÍTICO) -->
    <g transform="translate(425, 75)">
      <!-- Canal proteico transmembrana -->
      <rect x="-35" y="-12" width="70" height="34" rx="8" fill="#ea580c" stroke="#fed7aa" stroke-width="2"/>
      <text x="0" y="10" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">GLUT-4</text>
      <!-- Flecha de entrada de Glucosa desde la sangre -->
      <path d="M 0 -25 L 0 35" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <text x="0" y="-32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#c2410c" text-anchor="middle">D-Glucosa en Sangre</text>
    </g>

    <!-- ============================================================= -->
    <!-- CITOESQUELETO Y ESTRUCTURAS DEL CITOSOL                        -->
    <!-- ============================================================= -->
    <g opacity="0.3" stroke="#94a3b8" fill="none">
      <path d="M 60 220 Q 500 160 1100 240 T {ancho-60} 210" stroke-width="1.6" stroke-dasharray="8 6"/>
      <path d="M 80 540 Q 600 620 1200 560 T {ancho-80} 580" stroke-width="1.5" stroke-dasharray="7 7"/>
      <path d="M 50 900 Q 550 840 1150 910 T {ancho-50} 880" stroke-width="1.6" stroke-dasharray="8 5"/>
      <path d="M 70 1350 Q 650 1420 1250 1370 T {ancho-70} 1390" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 60 1800 Q 550 1740 1100 1820 T {ancho-60} 1780" stroke-width="1.6" stroke-dasharray="6 6"/>
    </g>

    <!-- Polirribosomas flotantes en el citoplasma -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="180" cy="180" r="2.5"/><circle cx="186" cy="182" r="2"/><circle cx="184" cy="188" r="2.3"/>
      <circle cx="950" cy="280" r="2.5"/><circle cx="956" cy="282" r="2"/><circle cx="954" cy="288" r="2.3"/>
      <circle cx="1900" cy="450" r="2.5"/><circle cx="1906" cy="452" r="2"/><circle cx="1904" cy="458" r="2.3"/>
      <circle cx="180" cy="1200" r="2.5"/><circle cx="186" cy="1202" r="2"/><circle cx="184" cy="1208" r="2.3"/>
      <circle cx="1050" cy="1450" r="2.5"/><circle cx="1056" cy="1452" r="2"/><circle cx="1054" cy="1458" r="2.3"/>
      <circle cx="1920" cy="1600" r="2.5"/><circle cx="1926" cy="1602" r="2"/><circle cx="1924" cy="1608" r="2.3"/>
    </g>

    <!-- ============================================================= -->
    <!-- MITOCONDRIA BIOLÓGICA REAL (INFERIOR DERECHA / CENTRO)         -->
    <!-- ============================================================= -->
    <g id="mitocondria-real" transform="translate(680, 2180)">
      <!-- Membrana externa -->
      <path d="M 0 60 C 250 10 900 10 1350 60 L 1350 220 L 0 220 Z" fill="#fffbeb" stroke="#ea580c" stroke-width="3.5"/>
      <!-- Membrana interna con crestas onduladas -->
      <path d="M 20 80 Q 80 120 140 85 T 260 90 T 380 85 T 500 95 T 620 85 T 740 90 T 860 85 T 980 95 T 1100 85 T 1220 90 T 1330 80" 
            fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-dasharray="7 4"/>
      
      <!-- Fondo de la Matriz Mitocondrial -->
      <rect x="0" y="95" width="1350" height="125" fill="#fef3c7" opacity="0.6"/>

      <!-- Transportador MPC (Complejo de Piruvato) -->
      <rect x="25" y="45" width="30" height="34" rx="6" fill="#ea580c" stroke="#fed7aa" stroke-width="2"/>
      <text x="40" y="66" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">MPC</text>
      <text x="65" y="65" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#c2410c">Transportador Mitocondrial de Piruvato</text>
      
      <!-- Anuncio sutil de destino mitocondrial -->
      <text x="450" y="145" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#d97706" letter-spacing="1">MATRIZ MITOCONDRIAL (PDH • CICLO DE KREBS • CADENA RESPIRATORIA)</text>
    </g>
    """

def generar_html_completo():
    """Genera el código HTML y SVG completo integrando ambas rutas."""
    svg_parts = []

    # 1. Capa de entorno citosólico
    svg_parts.append(generar_entorno_celular_citosol(ANCHO_CANVAS, ALTO_CANVAS))

    # =========================================================================
    # EJE 1: RUTA GLUCOLÍTICA (IZQUIERDA: X ≈ 425)
    # =========================================================================
    X_GLU = 380
    X_FLECHA = 425

    # 1. D-Glucosa
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=125,
        nombre="D-Glucosa",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Sustrato libre captado del GLUT-4",
        svg_estructura=GLUCOSA
    ))

    # Reacción 1: Hexoquinasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=235,
        enzima="Hexoquinasa",
        ec="EC 2.7.1.1 (Mg²⁺)",
        regulacion="⊣ G-6-P | ⊕ Insulina",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 2. Glucosa-6-Fosfato (EL GRAN NODO CONECTOR DEL CITOSOL)
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=345,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa Ⓟ)",
        detalle="Nodo: Glucólisis • Glucógeno • Pentosas",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # RAMA LATERAL IZQUIERDA: METABOLISMO DEL GLUCÓGENO
    svg_parts.append(f"""
    <!-- Conexión G6P <-> Glucógeno a la izquierda -->
    <g transform="translate(360, 395)">
      <line x1="-15" y1="-2" x2="-140" y2="-2" stroke="#f59e0b" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="-140" y1="4" x2="-15" y2="4" stroke="#f59e0b" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <text x="-75" y="-10" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#d97706" text-anchor="middle">Fosfoglucomutasa ⇄ G-1-P</text>
    </g>
    <!-- Glucógeno -->
    <g transform="translate(100, 350)">
      <g transform="translate(0, 0)">
        {ESTRUCTURA_GLUCOGENO}
      </g>
      <g transform="translate(110, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">Glucógeno (n)</text>
        <text x="0" y="17" fill="#d97706" font-size="11" font-weight="700">Reserva Glucídica</text>
        <text x="0" y="32" fill="#64748b" font-size="10">Glucogénesis / Glucogenólisis</text>
      </g>
    </g>
    """)

    # Reacción 2: Fosfoglucosa Isomerasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=490,
        enzima="Fosfoglucosa Isomerasa",
        ec="EC 5.3.1.9 (⇄)",
        reversible=True
    ))

    # 3. Fructosa-6-Fosfato (RECIBE EL RETORNO DE PENTOSAS FOSFATO)
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=595,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Cetosa Ⓟ)",
        detalle="Receptor de Transcetolasa / Transaldolasa",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # Reacción 3: Fosfofructoquinasa-1 (PFK-1)
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=740,
        enzima="Fosfofructoquinasa-1 (PFK-1)",
        ec="EC 2.7.1.11 (Compromiso Clave)",
        regulacion="⊣ ATP, Citrato | ⊕ AMP, F-2,6-BP",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 4. Fructosa-1,6-Bisfosfato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=840,
        nombre="Fructosa-1,6-Bisfosfato",
        carbonos="6 Carbonos (Hexosa Bis-Ⓟ)",
        detalle="Sustrato de escisión aldólica",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO
    ))

    # ZONA DE TRIOSAS: Aldolasa, DHAP, GAP y TPI
    svg_parts.append(f"""
    <!-- Bifurcación Aldolasa -->
    <g transform="translate({X_FLECHA}, 960)">
      <path d="M -15 0 Q -100 25 -140 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <path d="M 15 0 Q 100 25 150 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(0, 24)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">Aldolasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 4.1.2.13 (⇄)</text>
      </g>
    </g>

    <!-- DHAP (Izquierda) -->
    {crear_metabolito(
        x=160, y=1040,
        nombre="Dihidroxiacetona-P",
        carbonos="3 Carbonos (Cetotriosa)",
        detalle="Interconvertible con GAP",
        svg_estructura=DIHIDROXIACETONA_FOSFATO,
        texto_izquierda=True
    )}

    <!-- GAP (Derecha, Eje Glucolítico) -->
    {crear_metabolito(
        x=600, y=1040,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Aldotriosa)",
        detalle="Continúa hacia el rendimiento",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    )}

    <!-- TPI Horizontal Reversible -->
    <g transform="translate(425, 1070)">
      <line x1="-90" y1="-3" x2="80" y2="-3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="80" y1="3" x2="-90" y2="3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <text x="-5" y="-12" fill="#0f172a" font-size="10.5" font-weight="800" text-anchor="middle">Triosa Fosfato Isomerasa (TPI)</text>
      <text x="-5" y="16" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1 (⇄)</text>
    </g>

    <!-- Entrada hacia la Fase 2 (Rendimiento) -->
    <path d="M 640 1140 Q 640 1175 425 1195" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <g transform="translate(425, 1180)">
      <rect x="-95" y="-11" width="190" height="22" rx="11" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
      <text x="0" y="4" fill="#c2410c" font-size="10.5" font-weight="800" text-anchor="middle">FASE 2: RENDIMIENTO (× 2)</text>
    </g>
    """)

    # FASE 2: RENDIMIENTO
    # Reacción 5: GAPDH
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1215,
        enzima="Gliceraldehído-3-P DH (GAPDH)",
        ec="EC 1.2.1.12 (⇄)",
        entra_energia="+ 2 NAD⁺ + 2 Pi",
        sale_energia="+ 2 NADH + 2 H⁺",
        reversible=True,
        es_ganancia=True
    ))

    # 5. 1,3-Bisfosfoglicerato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1310,
        nombre="1,3-Bisfosfoglicerato",
        carbonos="3 Carbonos (Acil-fosfato de alta energía)",
        detalle="Primer paso fosforilante a nivel de sustrato",
        svg_estructura=BISFOSFOGLICERATO_1_3
    ))

    # Reacción 6: PGK
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1430,
        enzima="Fosfoglicerato Quinasa (PGK)",
        ec="EC 2.7.2.3 (⇄)",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        reversible=True,
        es_ganancia=True
    ))

    # 6. 3-Fosfoglicerato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1525,
        nombre="3-Fosfoglicerato",
        carbonos="3 Carbonos (Ácido carboxílico Ⓟ)",
        detalle="Intermediario glucolítico",
        svg_estructura=FOSFOGLICERATO_3
    ))

    # Reacción 7: Fosfogliceromutasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1645,
        enzima="Fosfogliceromutasa",
        ec="EC 5.4.2.11 (⇄)",
        reversible=True
    ))

    # 7. 2-Fosfoglicerato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1735,
        nombre="2-Fosfoglicerato",
        carbonos="3 Carbonos (Éster fosfato interno)",
        detalle="Sustrato de deshidratación",
        svg_estructura=FOSFOGLICERATO_2
    ))

    # Reacción 8: Enolasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1845,
        enzima="Enolasa",
        ec="EC 4.2.1.11 (Mg²⁺, ⇄)",
        salida_agua=True,
        reversible=True
    ))

    # 8. Fosfoenolpiruvato (PEP)
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1945,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 Carbonos (Enol-fosfato)",
        detalle="Compuesto de mayor potencial fosforilante",
        svg_estructura=FOSFOENOLPIRUVATO
    ))

    # Reacción 9: Piruvato Quinasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=2075,
        enzima="Piruvato Quinasa",
        ec="EC 2.7.1.40 (K⁺, Mg²⁺)",
        regulacion="⊣ ATP, Alanina | ⊕ F-1,6-BP",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True
    ))

    # 9. Piruvato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=2175,
        nombre="Piruvato",
        carbonos="3 Carbonos (α-Cetoácido)",
        detalle="Nodo terminal citosólico hacia MPC / LDH",
        svg_estructura=PIRUVATO
    ))

    # DESTINOS DEL PIRUVATO EN EL CITOSOL:
    # A) Fermentación Láctica a la izquierda
    svg_parts.append(f"""
    <!-- Lactato Deshidrogenasa hacia la izquierda -->
    <g transform="translate(360, 2225)">
      <line x1="-15" y1="-2" x2="-140" y2="-2" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="-140" y1="4" x2="-15" y2="4" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <!-- Regeneración de NAD+ -->
      <path d="M -50 -10 Q -80 -25 -110 -10" fill="none" stroke="#059669" stroke-width="1.6" marker-end="url(#arrowGreen)"/>
      <text x="-80" y="-30" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#059669" text-anchor="middle">NADH + H⁺ ⇄ NAD⁺</text>
      <text x="-80" y="20" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">Lactato DH (LDH)</text>
    </g>
    <!-- Molécula de L-Lactato -->
    <g transform="translate(90, 2180)">
      <g transform="translate(0, 0)">
        {ESTRUCTURA_LACTATO}
      </g>
      <g transform="translate(100, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">L-Lactato</text>
        <text x="0" y="17" fill="#ea580c" font-size="11" font-weight="700">3 Carbonos (Hidroxiácido)</text>
        <text x="0" y="32" fill="#64748b" font-size="10">Destino anaerobio / Ciclo de Cori</text>
      </g>
    </g>

    <!-- B) Entrada de Piruvato a Mitocondria hacia el transportador MPC -->
    <path d="M 520 2235 Q 620 2235 700 2240" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
    """)


    # =========================================================================
    # EJE 2: VÍA DE LAS PENTOSAS FOSFATO (DERECHA: X ≈ 1100 a 2050)
    # =========================================================================
    # CONEXIÓN 1: Salida desde G6P Glucolítica hacia G6PDH
    svg_parts.append("""
    <!-- Conexión física desde G6P hacia la Vía de las Pentosas Fosfato -->
    <path d="M 540 375 Q 850 345 1070 375" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
    <g transform="translate(805, 335)">
      <rect x="-85" y="-12" width="170" height="24" rx="12" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
      <text x="0" y="4" fill="#6d28d9" font-size="10.5" font-weight="800" text-anchor="middle">ENTRADA AL SHUNT DE PENTOSAS</text>
    </g>
    """)

    # FASE 1: FASE OXIDATIVA
    # Reacción 1: G6PDH
    svg_parts.append(f"""
    <!-- Reacción G6PDH en la conexión -->
    <g transform="translate(950, 375)">
      <path d="M -30 -15 Q -10 -25 10 -15" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-25" y="-30" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#475569">+ NADP⁺</text>
      <path d="M -30 15 Q -10 25 10 15" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="-25" y="32" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#059669">+ NADPH + H⁺</text>
      <text x="0" y="-8" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">G6PDH</text>
      <text x="0" y="7" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">EC 1.1.1.49</text>
    </g>
    """)

    # 1. 6-Fosfoglucono-δ-Lactona
    svg_parts.append(crear_metabolito(
        x=1100, y=345,
        nombre="6-Fosfoglucono-δ-Lactona",
        carbonos="6 Carbonos (Lactona)",
        detalle="Éster intramolecular hidrolizable",
        svg_estructura=FOSFOGLUCONO_LACTONA_6
    ))

    # Reacción 2: Lactonasa horizontal
    svg_parts.append("""
    <g transform="translate(1360, 395)">
      <line x1="0" y1="0" x2="60" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M 10 -15 Q 30 -25 50 -15" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="30" y="-30" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0284c7" text-anchor="middle">+ H₂O</text>
      <text x="30" y="16" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">6-P-Gluconolactonasa</text>
      <text x="30" y="28" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">EC 3.1.1.31</text>
    </g>
    """)

    # 2. 6-Fosfogluconato
    svg_parts.append(crear_metabolito(
        x=1470, y=345,
        nombre="6-Fosfogluconato",
        carbonos="6 Carbonos (Cadena lineal)",
        detalle="Ácido descarboxilable generador de NADPH",
        svg_estructura=FOSFOGLUCONATO_6
    ))

    # Reacción 3: 6-Fosfogluconato DH (Descarboxilación Oxidativa bajando a Ribulosa-5-P)
    svg_parts.append(crear_reaccion_oxidativa(
        x=1600, y=510,
        enzima="6-Fosfogluconato Deshidrogenasa",
        ec="EC 1.1.1.44 (Descarboxilación)",
        genera_nadph=True,
        salida_co2=True,
        altura=54
    ))

    # 3. D-Ribulosa-5-Fosfato
    svg_parts.append(crear_metabolito(
        x=1470, y=600,
        nombre="D-Ribulosa-5-Fosfato",
        carbonos="5 Carbonos (Pentosa Cetosa)",
        detalle="Cruce de la fase oxidativa a la no oxidativa",
        svg_estructura=RIBULOSA_5_FOSFATO
    ))

    # Ramificación de Ribulosa-5-P hacia Xilulosa-5-P e Isomerasa a Ribosa-5-P
    svg_parts.append("""
    <g transform="translate(1600, 755)">
      <!-- Rama Izquierda (Epimerasa -> Xilulosa-5-P) -->
      <path d="M -20 0 Q -110 30 -160 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(-175, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800" text-anchor="end">Fosfopentosa Epimerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 5.1.3.1 (⇄)</text>
      </g>

      <!-- Rama Derecha (Isomerasa -> Ribosa-5-P) -->
      <path d="M 20 0 Q 110 30 180 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(175, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Fosfopentosa Isomerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 5.3.1.6 (⇄)</text>
      </g>
    </g>
    """)

    # 4a. D-Xilulosa-5-P (Izquierda)
    svg_parts.append(crear_metabolito(
        x=1200, y=835,
        nombre="D-Xilulosa-5-P",
        carbonos="5 Carbonos (Epímero C3)",
        detalle="Donador de 2C (TPP)",
        svg_estructura=XILULOSA_5_FOSFATO,
        texto_izquierda=True
    ))

    # 4b. D-Ribosa-5-P (Derecha)
    svg_parts.append(crear_metabolito(
        x=1750, y=835,
        nombre="D-Ribosa-5-P",
        carbonos="5 Carbonos (Pentosa Aldosa)",
        detalle="Precursora de Nucleótidos",
        svg_estructura=RIBOSA_5_FOSFATO
    ))

    # SALIDA HACIA SÍNTESIS DE NUCLEÓTIDOS (Debajo de Ribosa-5-P)
    svg_parts.append("""
    <g transform="translate(1920, 890)">
      <line x1="0" y1="0" x2="0" y2="35" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
      <g transform="translate(0, 42)">
        <rect x="-95" y="0" width="190" height="38" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
        <text x="0" y="16" fill="#6d28d9" font-size="10" font-weight="800" text-anchor="middle">SÍNTESIS DE NUCLEÓTIDOS</text>
        <text x="0" y="29" fill="#7c3aed" font-size="9" font-weight="600" text-anchor="middle">ATP • GTP • ARN • ADN • PRPP</text>
      </g>
    </g>
    """)

    # FASE 2: FASE NO OXIDATIVA
    # PASO 1: TRANSCETOLASA 1 (X5P + R5P ⇄ S7P + GAP)
    svg_parts.append(crear_paso_no_oxidativo(
        x=1520, y=1025,
        enzima="Transcetolasa (TK1)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Ribosa-5-P (5C)",
        productos_txt="GAP (3C) + Sedoheptulosa-7-P (7C)"
    ))

    # Productos del Paso 1:
    # Sedoheptulosa-7-P (Izquierda)
    svg_parts.append(crear_metabolito(
        x=1200, y=1105,
        nombre="Sedoheptulosa-7-P",
        carbonos="7 Carbonos (Cetosa)",
        detalle="Intermediario de 7C",
        svg_estructura=SEDOHEPTULOSA_7_FOSFATO,
        texto_izquierda=True
    ))

    # GAP intermediario (Derecha)
    svg_parts.append(crear_metabolito(
        x=1750, y=1105,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="Intermediario transferible",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))

    # PASO 2: TRANSALDOLASA (S7P + GAP ⇄ F6P + E4P)
    svg_parts.append(crear_paso_no_oxidativo(
        x=1520, y=1255,
        enzima="Transaldolasa (TA)",
        ec="EC 2.2.1.2 (Base de Schiff con Lisina)",
        sustratos_txt="Sedoheptulosa-7-P (7C) + GAP (3C)",
        productos_txt="Fructosa-6-P (6C) + Eritrosa-4-P (4C)"
    ))

    # Productos del Paso 2:
    # Eritrosa-4-P (Izquierda)
    svg_parts.append(crear_metabolito(
        x=1200, y=1335,
        nombre="D-Eritrosa-4-P",
        carbonos="4 Carbonos (Tetrosa)",
        detalle="Aceptor para la segunda transcetolasa",
        svg_estructura=ERITROSA_4_FOSFATO,
        texto_izquierda=True
    ))

    # Fructosa-6-P (Derecha) - ¡1er REINGRESO!
    svg_parts.append(crear_metabolito(
        x=1750, y=1335,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡1.er Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # PASO 3: TRANSCETOLASA 2 (X5P + E4P ⇄ F6P + GAP)
    svg_parts.append(crear_paso_no_oxidativo(
        x=1520, y=1485,
        enzima="Transcetolasa (TK2)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Eritrosa-4-P (4C)",
        productos_txt="Fructosa-6-P (6C) + GAP (3C)"
    ))

    # Productos del Paso 3:
    # Fructosa-6-P (Izquierda) - ¡2º REINGRESO!
    svg_parts.append(crear_metabolito(
        x=1200, y=1565,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡2.º Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        texto_izquierda=True
    ))

    # GAP (Derecha) - ¡REINGRESO DE TRIOSA!
    svg_parts.append(crear_metabolito(
        x=1750, y=1565,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="¡Reingreso de triosa a la Glucólisis!",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))


    # =========================================================================
    # CONEXIONES DE RETORNO FÍSICO A LA GLUCÓLISIS (EL PUENTE BIOLÓGICO REAL)
    # =========================================================================
    svg_parts.append("""
    <!-- RETORNO 1: Desde Fructosa-6-P (Paso 2) hacia F6P de la Glucólisis -->
    <path d="M 1740 1375 C 1450 1300 950 1000 520 625" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(1080, 880)">
      <rect x="-85" y="-11" width="170" height="22" rx="11" fill="#ecfdf5" stroke="#059669" stroke-width="1.6"/>
      <text x="0" y="4" fill="#047857" font-size="10" font-weight="800" text-anchor="middle">RETORNO: F-6-P A GLUCÓLISIS</text>
    </g>

    <!-- RETORNO 2: Desde GAP (Paso 3) hacia GAP de la Glucólisis -->
    <path d="M 1740 1600 C 1350 1550 900 1350 720 1085" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(1180, 1400)">
      <rect x="-85" y="-11" width="170" height="22" rx="11" fill="#ecfdf5" stroke="#059669" stroke-width="1.6"/>
      <text x="0" y="4" fill="#047857" font-size="10" font-weight="800" text-anchor="middle">RETORNO: GAP A GLUCÓLISIS</text>
    </g>
    """)

    # Unir todo el SVG
    svg_final = "\n".join(svg_parts)

    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Citosol Celular Integrado - Glucólisis y Pentosas Fosfato</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #e2e8f0;
      color: #0f172a;
      padding: 25px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .lienzo-svg {{
      width: 100%;
      max-width: {ANCHO_CANVAS}px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 10px;
      box-shadow: 0 15px 40px rgba(0, 0, 0, 0.12);
      overflow: hidden;
    }}
    svg {{
      display: block;
      width: 100%;
      height: auto;
    }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" viewBox="0 0 {ANCHO_CANVAS} {ALTO_CANVAS}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Marcadores de flechas estandarizados -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
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
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>
        <marker id="arrowPurple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#7c3aed" />
        </marker>

        <!-- Gradiente biológico del Citosol -->
        <linearGradient id="gradCitosolLuz" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#ffffff" stop-opacity="1" />
          <stop offset="10%" stop-color="#f8fafc" stop-opacity="0.8" />
          <stop offset="50%" stop-color="#f0fdf4" stop-opacity="0.5" />
          <stop offset="85%" stop-color="#f8fafc" stop-opacity="0.8" />
          <stop offset="100%" stop-color="#ffffff" stop-opacity="1" />
        </linearGradient>

        <!-- ESTRUCTURAS QUÍMICAS -->
        {ESTRUCTURA_LACTATO}
        {ESTRUCTURA_GLUCOGENO}
      </defs>

      {svg_final}
    </svg>
  </div>
</body>
</html>
"""
    return html_template

if __name__ == "__main__":
    ruta_salida = os.path.join(os.path.dirname(__file__), "citosol_completo.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(generar_html_completo())
    print(f"✅ Mapa del Citosol Integrado generado con éxito en: {ruta_salida}")
