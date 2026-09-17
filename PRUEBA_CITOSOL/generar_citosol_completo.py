#!/usr/bin/env python3
"""
ESQUEMA INTEGRAL DEL CITOSOL CELULAR (COMPARTIMENTO CERRADO Y MAPA DE RUTAS)
=============================================================================
Este script plasma la visión conceptual y espacial de todo el CITOSOL como
un compartimento cerrado y definido dentro del mapa celular:
1. Membrana Plasmática cerrada con el receptor GLUT-4 y su lupa de aumento molecular real.
2. Ejes completamente desarrollados:
   - Glucólisis completa (11 metabolitos y 10 reacciones).
   - Vía de las Pentosas Fosfato completa (Fase oxidativa y no oxidativa con
     Transcetolasas, Transaldolasa y retorno a F6P y GAP).
3. Representación espacial de las rutas citosólicas restantes:
   - Metabolismo del Glucógeno (Glucogénesis y Glucogenólisis) a la izquierda de G6P.
   - Bypass de Gluconeogénesis (G6Pasa, FBPasa-1 y PEPCK citosólica).
   - Síntesis de Nucleótidos a partir de Ribosa-5-P / PRPP a la derecha.
   - Metabolismo de Lípidos Citosólicos:
     * DHAP -> Glicerol-3-P -> Triglicéridos (TAGs).
     * Citrato mitocondrial -> Acetil-CoA -> Malonil-CoA -> Palmitato (FAS).
   - Cruces del Piruvato: L-Lactato (LDH), L-Alanina (ALT) y cruce MPC a mitocondria.
   - Tramo Citosólico del Ciclo de la Urea (Citrulina -> Argininosuccinato -> Arginina -> Urea).
4. Límites biológicos de organelos: Mitocondria con doble membrana y transportadores.
5. Estilo editorial de libro de bioquímica médica (sin índices que tapen).
"""

import os
import sys

# Importar estructuras químicas
DIR_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(DIR_RAIZ, "01_CARBOHIDRATOS", "01_glucolisis"))
sys.path.append(os.path.join(DIR_RAIZ, "01_CARBOHIDRATOS", "04_via_pentosas_fosfato"))

from estructuras_glucosa import (
    GLUCOSA, GLUCOSA_6_FOSFATO, FRUCTOSA_6_FOSFATO, FRUCTOSA_1_6_BISFOSFATO,
    DIHIDROXIACETONA_FOSFATO, GLICERALDEHIDO_3_FOSFATO, BISFOSFOGLICERATO_1_3,
    FOSFOGLICERATO_3, FOSFOGLICERATO_2, FOSFOENOLPIRUVATO, PIRUVATO
)

from estructuras_pentosas import (
    FOSFOGLUCONO_LACTONA_6, FOSFOGLUCONATO_6, RIBULOSA_5_FOSFATO,
    RIBOSA_5_FOSFATO, XILULOSA_5_FOSFATO, SEDOHEPTULOSA_7_FOSFATO, ERITROSA_4_FOSFATO
)

ANCHO_CANVAS = 2500
ALTO_CANVAS = 2500

# -----------------------------------------------------------------------------
# GENERADORES DE METABOLITOS Y REACCIONES
# -----------------------------------------------------------------------------
def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False):
    """Construye el bloque SVG de un metabolito con estructura y rótulos."""
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
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800" {alineacion}>{nombre}</text>
        <text x="0" y="17" fill="#ea580c" font-size="11.5" font-weight="700" {alineacion}>{carbonos}</text>
        <text x="0" y="32" fill="#64748b" font-size="10.5" {alineacion}>{detalle}</text>
      </g>
    </g>
    """

def crear_reaccion(x, y, enzima, ec="", regulacion="", entra_energia="", sale_energia="", 
                   reversible=False, es_ganancia=False, salida_agua=False, altura=48):
    """Genera una reacción vertical con cofactores y enzimas."""
    curvas_energia = ""
    if entra_energia:
        color_entrada = "#dc2626" if not es_ganancia else "#475569"
        marcador_entrada = "url(#arrowRed)" if not es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -75 8 Q -25 8 -4 18" fill="none" stroke="{color_entrada}" stroke-width="1.8" marker-end="{marcador_entrada}"/>
        <text x="-80" y="11" fill="{color_entrada}" font-size="10.5" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
    if sale_energia:
        color_salida = "#059669" if es_ganancia else "#475569"
        marcador_salida = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -4 24 Q -25 34 -75 34" fill="none" stroke="{color_salida}" stroke-width="1.8" marker-end="{marcador_salida}"/>
        <text x="-80" y="37" fill="{color_salida}" font-size="10.5" font-weight="800" text-anchor="end">{sale_energia}</text>
        """
    if salida_agua:
        curvas_energia += """
        <path d="M -4 24 Q -25 34 -70 34" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-75" y="37" fill="#0284c7" font-size="10.5" font-weight="800" text-anchor="end">- 2 H₂O</text>
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
        regulacion_svg = f'<text x="0" y="26" fill="{color_reg}" font-size="9.5" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha}
      {curvas_energia}
      <g transform="translate(18, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">{enzima}</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">{ec}</text>
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
        <text x="-70" y="11" fill="#475569" font-size="10" font-weight="800" text-anchor="end">+ NADP⁺</text>
        <path d="M -4 24 Q -25 34 -70 34" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
        <text x="-75" y="38" fill="#059669" font-size="10" font-weight="800" text-anchor="end">+ NADPH + H⁺</text>
        """
    if entra_agua:
        curvas += """
        <path d="M -65 8 Q -25 8 -4 18" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
        <text x="-70" y="11" fill="#0284c7" font-size="10" font-weight="800" text-anchor="end">+ H₂O</text>
        """
    if salida_co2:
        curvas += """
        <path d="M 4 24 Q 25 34 65 34" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
        <text x="70" y="38" fill="#475569" font-size="10" font-weight="800">+ CO₂</text>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="26" fill="{color_reg}" font-size="9" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción Oxidativa: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="0" y1="0" x2="0" y2="{altura}" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      {curvas}
      <g transform="translate(18, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800">{enzima}</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """

def crear_paso_no_oxidativo(x, y, enzima, ec, sustratos_txt, productos_txt):
    """Genera un nodo de transferencia no oxidativa."""
    return f"""
    <!-- Reacción de Transferencia: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="-3" y1="0" x2="-3" y2="45" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="45" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <g transform="translate(18, 10)">
        <text x="0" y="0" fill="#0f172a" font-size="12.5" font-weight="800">{enzima}</text>
        <text x="0" y="14" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        <text x="0" y="28" fill="#c2410c" font-size="9.5" font-weight="700">{sustratos_txt} ⇄ {productos_txt}</text>
      </g>
    </g>
    """

# -----------------------------------------------------------------------------
# DIBUJO DEL ENTORNO BIOLÓGICO: MEMBRANA CERRADA, GLUT-4 CON LUPA Y MITOCONDRIA
# -----------------------------------------------------------------------------
def generar_entorno_celular(ancho, alto):
    """Genera la anatomía que CIERRA y define el citosol como un compartimento."""
    return f"""
    <!-- Medio Extracelular circundante de fondo -->
    <rect width="{ancho}" height="{alto}" fill="#f1f5f9"/>

    <!-- ============================================================= -->
    <!-- FORMA CERRADA DE LA CÉLULA (MEMBRANA PLASMÁTICA ENVOLVENTE)   -->
    <!-- ============================================================= -->
    <!-- Espacio del Citosol cerrado (Fondo blanco translúcido biológico) -->
    <path d="M 220,120 
             C 800,60 1700,60 2320,120 
             C 2460,200 2460,2100 2300,2380 
             C 1700,2480 800,2480 180,2380 
             C 40,2100 40,200 220,120 Z" 
          fill="#ffffff" 
          stroke="#0284c7" 
          stroke-width="12" 
          stroke-linejoin="round"/>

    <!-- Detalle de la bicapa fosfolipídica externa -->
    <path d="M 220,120 
             C 800,60 1700,60 2320,120 
             C 2460,200 2460,2100 2300,2380 
             C 1700,2480 800,2480 180,2380 
             C 40,2100 40,200 220,120 Z" 
          fill="url(#gradCitosolSuave)" 
          stroke="#38bdf8" 
          stroke-width="4" 
          stroke-dasharray="8 5"/>

    <!-- Rótulo elegante en el espacio extracelular -->
    <text x="1250" y="45" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#64748b" text-anchor="middle" letter-spacing="2">
      ESPACIO EXTRACELULAR (SANGRE / LÍQUIDO INTERSTICIAL)
    </text>

    <!-- ============================================================= -->
    <!-- EL TRANSPORTADOR GLUT-4 EN LA MEMBRANA REAL                  -->
    <!-- ============================================================= -->
    <g transform="translate(680, 75)">
      <!-- Lóbulo proteico izquierdo -->
      <path d="M 0 5 C 10 -12, 28 -12, 34 5 C 38 18, 34 36, 25 42 C 12 45, 2 35, 0 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <!-- Lóbulo proteico derecho -->
      <path d="M 80 5 C 70 -12, 52 -12, 46 5 C 42 18, 46 36, 55 42 C 68 45, 78 35, 80 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <!-- Poro central acuoso -->
      <ellipse cx="40" cy="20" rx="10" ry="18" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8"/>
      <!-- Glucosa cruzando por el canal -->
      <polygon points="40,14 45,17 45,23 40,26 35,23 35,17" fill="#ffffff" stroke="#ea580c" stroke-width="1.6"/>
      <circle cx="35" cy="17" r="2" fill="#dc2626"/>
      <!-- Rótulo en la proteína -->
      <text x="40" y="49" fill="#0369a1" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-4</text>
    </g>

    <!-- Flecha de entrada de Glucosa hacia el citosol -->
    <line x1="720" y1="50" x2="720" y2="75" stroke="#ea580c" stroke-width="2.2"/>
    <line x1="720" y1="115" x2="720" y2="140" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

    <!-- ============================================================= -->
    <!-- ZOOM MOLECULAR / LUPA CIENTÍFICA DEL RECEPTOR GLUT-4          -->
    <!-- ============================================================= -->
    <!-- Líneas de proyección cónica desde el GLUT hacia la lupa -->
    <g stroke="#38bdf8" stroke-width="1.4" stroke-dasharray="4 3" opacity="0.7">
      <line x1="680" y1="95" x2="525" y2="120" />
      <line x1="690" y1="75" x2="490" y2="70" />
    </g>

    <!-- Ventana Circular de Zoom (Lupa de Aumento Molecular) -->
    <g transform="translate(420, 115)">
      <circle cx="0" cy="0" r="70" fill="#ffffff" stroke="#0284c7" stroke-width="3.5" />
      <circle cx="0" cy="0" r="66" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />

      <!-- Bicapa lipídica ampliada dentro de la lupa -->
      <g opacity="0.85">
        <!-- Fosfolípidos arriba -->
        <g fill="#0284c7">
          <circle cx="-55" cy="-8" r="5"/><circle cx="-40" cy="-8" r="5"/><circle cx="-25" cy="-8" r="5"/>
          <circle cx="25" cy="-8" r="5"/><circle cx="40" cy="-8" r="5"/><circle cx="55" cy="-8" r="5"/>
        </g>
        <!-- Colas hidrofóbicas -->
        <g stroke="#94a3b8" stroke-width="1.4" fill="none">
          <path d="M -55 -3 Q -57 2 -53 7"/><path d="M -40 -3 Q -42 2 -38 7"/><path d="M -25 -3 Q -27 2 -23 7"/>
          <path d="M 25 -3 Q 23 2 27 7"/><path d="M 40 -3 Q 38 2 42 7"/><path d="M 55 -3 Q 53 2 57 7"/>
          <path d="M -55 17 Q -57 12 -53 7"/><path d="M -40 17 Q -42 12 -38 7"/><path d="M -25 17 Q -27 12 -23 7"/>
          <path d="M 25 17 Q 23 12 27 7"/><path d="M 40 17 Q 38 12 42 7"/><path d="M 55 17 Q 53 12 57 7"/>
        </g>
        <!-- Fosfolípidos abajo -->
        <g fill="#0284c7">
          <circle cx="-55" cy="22" r="5"/><circle cx="-40" cy="22" r="5"/><circle cx="-25" cy="22" r="5"/>
          <circle cx="25" cy="22" r="5"/><circle cx="40" cy="22" r="5"/><circle cx="55" cy="22" r="5"/>
        </g>
      </g>

      <!-- Proteína GLUT ampliada -->
      <path d="M -18 -24 C -9 -28, -4 -16, -4 0 C -4 16, -9 28, -18 24 C -27 20, -25 -20, -18 -24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <path d="M 18 -24 C 9 -28, 4 -16, 4 0 C 4 16, 9 28, 18 24 C 27 20, 25 -20, 18 -24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <ellipse cx="0" cy="0" rx="7" ry="20" fill="#bae6fd" opacity="0.6"/>

      <!-- Molécula de Glucosa cruzando (Haworth) -->
      <g transform="translate(0, -7)">
        <polygon points="0,-11 10,-5 10,6 0,13 -10,6 -10,-5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
        <circle cx="-10" cy="-5" r="3" fill="#ffffff"/>
        <text x="-10" y="-3" fill="#dc2626" font-size="6" font-weight="900" text-anchor="middle">O</text>
        <circle cx="15" cy="6" r="4.5" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
        <text x="15" y="8.5" fill="#ea580c" font-size="5.5" font-weight="900" text-anchor="middle">OH</text>
      </g>

      <path d="M 0 -28 L 0 -17" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <path d="M 0 11 L 0 28" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>

      <rect x="-60" y="47" width="120" height="16" rx="4" fill="#0f172a" opacity="0.9"/>
      <text x="0" y="59" fill="#ffffff" font-size="8" font-weight="800" text-anchor="middle" letter-spacing="0.5">DIFUSIÓN FACILITADA</text>
    </g>

    <!-- ============================================================= -->
    <!-- LIMITES BIOLÓGICOS DE LA MITOCONDRIA (ABAJO A LA DERECHA)    -->
    <!-- ============================================================= -->
    <g id="mitocondria-celular" transform="translate(1000, 2180)">
      <!-- Membrana externa lisa -->
      <path d="M 0,60 C 250,15 900,15 1380,60 L 1380,240 L 0,240 Z" fill="#fffbeb" stroke="#ea580c" stroke-width="4"/>
      <!-- Crestas onduladas internas -->
      <path d="M 20,85 Q 80,125 140,90 T 260,95 T 380,90 T 500,100 T 620,90 T 740,95 T 860,90 T 980,100 T 1100,90 T 1220,95 T 1350,85" 
            fill="none" stroke="#f59e0b" stroke-width="2.8" stroke-dasharray="8 5"/>
      <rect x="0" y="100" width="1380" height="140" fill="#fef3c7" opacity="0.65"/>

      <!-- Transportador MPC (Piruvato) -->
      <rect x="30" y="42" width="34" height="38" rx="7" fill="#ea580c" stroke="#fed7aa" stroke-width="2"/>
      <text x="47" y="65" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">MPC</text>
      <text x="75" y="65" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#c2410c">Transportador MPC (Piruvato a Matriz)</text>

      <!-- Lanzadera de Citrato (Hacia la síntesis de ácidos grasos citosólica) -->
      <rect x="420" y="42" width="34" height="38" rx="7" fill="#d97706" stroke="#fde68a" stroke-width="2"/>
      <text x="437" y="65" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">CIC</text>
      <text x="465" y="65" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#b45309">Transportador Tricarboxilato (Citrato a Citosol)</text>

      <!-- Lanzadera Ornitina/Citrulina (Ciclo de la Urea) -->
      <rect x="880" y="42" width="34" height="38" rx="7" fill="#059669" stroke="#a7f3d0" stroke-width="2"/>
      <text x="897" y="65" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">ORNT</text>
      <text x="925" y="65" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#047857">Lanzadera Ornitina / Citrulina (Urea)</text>

      <!-- Rótulo de Matriz Mitocondrial -->
      <text x="650" y="150" font-family="'Inter', sans-serif" font-size="15" font-weight="900" fill="#b45309" letter-spacing="1.5">
        MATRIZ MITOCONDRIAL (PDH • CICLO DE KREBS • CADENA RESPIRATORIA • β-OXIDACIÓN)
      </text>
    </g>
    """

def generar_html_mapa_citosol():
    """Compila el SVG integrando todas las rutas citosólicas con sus conexiones reales."""
    svg_parts = []

    # 1. Anatomía celular y membrana cerrada
    svg_parts.append(generar_entorno_celular(ANCHO_CANVAS, ALTO_CANVAS))

    # =========================================================================
    # EJE 1: GLUCÓLISIS Y BYPASS DE GLUCONEOGÉNESIS (X ≈ 675 a 720)
    # =========================================================================
    X_GLU = 675
    X_FLECHA = 720

    # 1. D-Glucosa
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=145,
        nombre="D-Glucosa",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Entrada al citoplasma desde el GLUT-4",
        svg_estructura=GLUCOSA
    ))

    # Reacción 1: Hexoquinasa vs Glucosa-6-Fosfatasa (Gluconeogénesis)
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=255,
        enzima="Hexoquinasa",
        ec="EC 2.7.1.1 (Mg²⁺)",
        regulacion="⊣ G-6-P | ⊕ Insulina",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))
    # Bypass Gluconeogénesis: G6Pasa
    svg_parts.append("""
    <g transform="translate(635, 255)">
      <path d="M 0 48 L 0 0" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
      <text x="-10" y="24" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0284c7" text-anchor="end">G-6-Fosfatasa (H₂O→Pi)</text>
    </g>
    """)

    # 2. Glucosa-6-Fosfato (GRAN NODO CONECTOR CITOSÓLICO)
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=365,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa Ⓟ)",
        detalle="Nodo central: Glucólisis • Glucógeno • Pentosas",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # Reacción 2: Fosfoglucosa Isomerasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=505,
        enzima="Fosfoglucosa Isomerasa",
        ec="EC 5.3.1.9 (⇄)",
        reversible=True
    ))

    # 3. Fructosa-6-Fosfato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=605,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Cetosa Ⓟ)",
        detalle="Punto de reingreso de las Pentosas Fosfato",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # Reacción 3: PFK-1 vs FBPasa-1 (Gluconeogénesis)
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=750,
        enzima="Fosfofructoquinasa-1 (PFK-1)",
        ec="EC 2.7.1.11 (Compromiso Clave)",
        regulacion="⊣ ATP, Citrato | ⊕ AMP, F-2,6-BP",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))
    # Bypass Gluconeogénesis: FBPasa-1
    svg_parts.append("""
    <g transform="translate(635, 750)">
      <path d="M 0 48 L 0 0" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
      <text x="-10" y="24" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0284c7" text-anchor="end">FBPasa-1 (H₂O→Pi)</text>
    </g>
    """)

    # 4. Fructosa-1,6-Bisfosfato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=850,
        nombre="Fructosa-1,6-Bisfosfato",
        carbonos="6 Carbonos (Hexosa Bis-Ⓟ)",
        detalle="Sustrato de escisión aldólica",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO
    ))

    # Aldolasa y Triosas
    svg_parts.append(f"""
    <g transform="translate({X_FLECHA}, 970)">
      <path d="M -15 0 Q -100 25 -140 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <path d="M 15 0 Q 100 25 150 65" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(0, 24)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">Aldolasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 4.1.2.13 (⇄)</text>
      </g>
    </g>

    <!-- DHAP (Izquierda) -->
    {crear_metabolito(
        x=450, y=1050,
        nombre="Dihidroxiacetona-P",
        carbonos="3 Carbonos (Cetotriosa)",
        detalle="Precursor de la síntesis de TAGs",
        svg_estructura=DIHIDROXIACETONA_FOSFATO,
        texto_izquierda=True
    )}

    <!-- GAP (Derecha) -->
    {crear_metabolito(
        x=890, y=1050,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Aldotriosa)",
        detalle="Continúa hacia el rendimiento",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    )}

    <!-- TPI Horizontal -->
    <g transform="translate({X_FLECHA}, 1080)">
      <line x1="-90" y1="-3" x2="80" y2="-3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="80" y1="3" x2="-90" y2="3" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <text x="-5" y="-12" fill="#0f172a" font-size="10.5" font-weight="800" text-anchor="middle">Triosa Fosfato Isomerasa (TPI)</text>
      <text x="-5" y="16" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1 (⇄)</text>
    </g>

    <!-- Entrada a Fase 2 -->
    <path d="M 930 1150 Q 930 1185 720 1205" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    <g transform="translate(720, 1190)">
      <rect x="-95" y="-11" width="190" height="22" rx="11" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
      <text x="0" y="4" fill="#c2410c" font-size="10.5" font-weight="800" text-anchor="middle">FASE 2: RENDIMIENTO (× 2)</text>
    </g>
    """)

    # Fase de Rendimiento
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1225,
        enzima="GAPDH",
        ec="EC 1.2.1.12 (⇄)",
        entra_energia="+ 2 NAD⁺ + 2 Pi",
        sale_energia="+ 2 NADH + 2 H⁺",
        reversible=True,
        es_ganancia=True
    ))

    # 5. 1,3-BPG
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1320,
        nombre="1,3-Bisfosfoglicerato",
        carbonos="3 Carbonos (Acil-fosfato)",
        detalle="Alta energía de hidrólisis",
        svg_estructura=BISFOSFOGLICERATO_1_3
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1440,
        enzima="Fosfoglicerato Quinasa (PGK)",
        ec="EC 2.7.2.3 (⇄)",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        reversible=True,
        es_ganancia=True
    ))

    # 6. 3-PG
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1535,
        nombre="3-Fosfoglicerato",
        carbonos="3 Carbonos (Ácido carboxílico Ⓟ)",
        detalle="Intermediario glucolítico",
        svg_estructura=FOSFOGLICERATO_3
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1655,
        enzima="Fosfogliceromutasa",
        ec="EC 5.4.2.11 (⇄)",
        reversible=True
    ))

    # 7. 2-PG
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1745,
        nombre="2-Fosfoglicerato",
        carbonos="3 Carbonos (Éster interno)",
        detalle="Sustrato de la enolasa",
        svg_estructura=FOSFOGLICERATO_2
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1855,
        enzima="Enolasa",
        ec="EC 4.2.1.11 (Mg²⁺, ⇄)",
        salida_agua=True,
        reversible=True
    ))

    # 8. PEP
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1955,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 Carbonos (Enol-fosfato)",
        detalle="Mayor potencial de transferencia Ⓟ",
        svg_estructura=FOSFOENOLPIRUVATO
    ))

    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=2085,
        enzima="Piruvato Quinasa",
        ec="EC 2.7.1.40 (K⁺, Mg²⁺)",
        regulacion="⊣ ATP, Alanina | ⊕ F-1,6-BP",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True
    ))

    # Bypass PEPCK Gluconeogénesis (desde Oxalacetato/Malato citosólico)
    svg_parts.append("""
    <g transform="translate(635, 2085)">
      <path d="M 0 48 L 0 0" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
      <text x="-10" y="24" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0284c7" text-anchor="end">PEPCK citosol (GTP→GDP+CO₂)</text>
    </g>
    """)

    # 9. Piruvato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=2185,
        nombre="Piruvato",
        carbonos="3 Carbonos (α-Cetoácido)",
        detalle="Nodo terminal citosólico",
        svg_estructura=PIRUVATO
    ))

    # Conexión directa hacia el transportador MPC de la mitocondria
    svg_parts.append("""
    <path d="M 830 2235 Q 940 2235 1025 2240" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowFlow)"/>
    """)


    # =========================================================================
    # RUTA CITOSÓLICA FALTANTE 1: METABOLISMO DEL GLUCÓGENO (ARRIBA IZQUIERDA)
    # =========================================================================
    svg_parts.append("""
    <!-- TERRITORIO: GLUCÓGENO (Zona Superior Izquierda) -->
    <g transform="translate(180, 320)">
      <!-- Marco territorial sutil -->
      <rect x="0" y="0" width="380" height="150" rx="10" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="6 4" opacity="0.95"/>
      <text x="15" y="22" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#b45309">METABOLISMO DEL GLUCÓGENO</text>
      
      <!-- Reacción Fosfoglucomutasa: G6P <-> G1P -->
      <g transform="translate(260, 65)">
        <line x1="100" y1="0" x2="30" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        <line x1="30" y1="6" x2="100" y2="6" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        <text x="65" y="-8" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#d97706" text-anchor="middle">Fosfoglucomutasa</text>
        <rect x="-25" y="-14" width="50" height="28" rx="5" fill="#ffffff" stroke="#f59e0b" stroke-width="1.5"/>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">G-1-P</text>
      </g>

      <!-- Reacción Glucogenogénesis: G1P -> UDP-Glucosa -> Glucógeno -->
      <g transform="translate(130, 65)">
        <line x1="90" y1="0" x2="30" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
        <text x="60" y="-8" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#d97706" text-anchor="middle">UDP-Glucosa (UTP)</text>
        <!-- Gránulo de Glucógeno -->
        <circle cx="0" cy="0" r="24" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
        <circle cx="0" cy="0" r="6" fill="#b45309"/>
        <circle cx="-10" cy="-8" r="4" fill="#d97706"/><circle cx="10" cy="-8" r="4" fill="#d97706"/>
        <circle cx="-10" cy="8" r="4" fill="#d97706"/><circle cx="10" cy="8" r="4" fill="#d97706"/>
        <text x="0" y="38" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#92400e" text-anchor="middle">GLUCÓGENO (n)</text>
      </g>

      <!-- Glucogenólisis: Glucógeno Fosforilasa (+ Pi -> G1P) -->
      <path d="M 130 90 Q 200 120 260 90" fill="none" stroke="#d97706" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowFlow)"/>
      <text x="200" y="125" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#b45309" text-anchor="middle">Glucógeno Fosforilasa (+ Pi)</text>
    </g>
    <!-- Conexión física desde G6P hacia el territorio del Glucógeno -->
    <path d="M 660 395 L 565 395" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
    """)


    # =========================================================================
    # RUTA CITOSÓLICA FALTANTE 2: METABOLISMO DE LÍPIDOS CITOSÓLICOS (IZQUIERDA)
    # =========================================================================
    svg_parts.append("""
    <!-- TERRITORIO: METABOLISMO DE LÍPIDOS CITOSÓLICO (Zona Media Izquierda) -->
    <g transform="translate(140, 1020)">
      <rect x="0" y="0" width="280" height="260" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8" stroke-dasharray="6 4" opacity="0.95"/>
      <text x="15" y="22" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#15803d">LÍPIDOS CITOSÓLICOS</text>

      <!-- A) Lanzadera Glicerol-3-P (desde DHAP) -->
      <g transform="translate(140, 70)">
        <rect x="-80" y="-16" width="160" height="32" rx="6" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
        <text x="0" y="4" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#166534" text-anchor="middle">L-Glicerol-3-Fosfato</text>
        <text x="0" y="26" font-family="'Inter', sans-serif" font-size="8" fill="#15803d" text-anchor="middle">Glicerol-3-P DH (NADH→NAD⁺)</text>

        <!-- Flecha hacia Síntesis de Triglicéridos -->
        <line x1="0" y1="32" x2="0" y2="60" stroke="#16a34a" stroke-width="2" marker-end="url(#arrowGreen)"/>
        <rect x="-60" y="62" width="120" height="26" rx="6" fill="#dcfce7" stroke="#15803d" stroke-width="1.5"/>
        <text x="0" y="78" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#14532d" text-anchor="middle">TRIGLICÉRIDOS (TAG)</text>
      </g>

      <!-- B) Lipogénesis de novo (Acetil-CoA -> Malonil-CoA -> Palmitato) -->
      <g transform="translate(140, 195)">
        <text x="0" y="-12" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#166534" text-anchor="middle">LIPOGÉNESIS (FAS)</text>
        <rect x="-100" y="-4" width="200" height="26" rx="5" fill="#ffffff" stroke="#16a34a" stroke-width="1.5"/>
        <text x="0" y="13" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#0f172a" text-anchor="middle">Malonil-CoA ➔ Palmitato</text>
        <text x="0" y="36" font-family="'Inter', sans-serif" font-size="8" fill="#15803d" text-anchor="middle">Consume NADPH de Pentosas</text>
      </g>
    </g>

    <!-- Conexión física desde DHAP hacia Glicerol-3-P -->
    <path d="M 430 1090 L 320 1090" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowGreen)"/>

    <!-- Salida de Citrato desde la mitocondria subiendo hacia la Lipogénesis -->
    <path d="M 1430 2180 C 1300 1700 450 1400 320 1230" fill="none" stroke="#d97706" stroke-width="2.2" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
    <text x="620" y="1580" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#b45309" transform="rotate(-30 620 1580)">Citrato a Citosol ➔ Acetil-CoA</text>
    """)


    # =========================================================================
    # RUTA CITOSÓLICA FALTANTE 3: DESTINOS DEL PIRUVATO (FERMENTACIÓN Y ALANINA)
    # =========================================================================
    svg_parts.append("""
    <!-- TERRITORIO: CRUCES DEL PIRUVATO (Zona Inferior Izquierda) -->
    <!-- A) Fermentación Láctica hacia la izquierda -->
    <g transform="translate(650, 2235)">
      <line x1="-15" y1="-2" x2="-140" y2="-2" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="-140" y1="4" x2="-15" y2="4" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <path d="M -50 -10 Q -80 -25 -110 -10" fill="none" stroke="#059669" stroke-width="1.6" marker-end="url(#arrowGreen)"/>
      <text x="-80" y="-28" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#059669" text-anchor="middle">NADH + H⁺ ⇄ NAD⁺</text>
      <text x="-80" y="18" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#0f172a" text-anchor="middle">LDH</text>
    </g>
    <!-- L-Lactato -->
    <g transform="translate(370, 2200)">
      <rect x="0" y="0" width="130" height="60" rx="8" fill="#fdf2f8" stroke="#db2777" stroke-width="1.8"/>
      <text x="65" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#9d174d" text-anchor="middle">L-Lactato</text>
      <text x="65" y="42" font-family="'Inter', sans-serif" font-size="9" fill="#be185d" text-anchor="middle">Destino Anaerobio / Sangre</text>
    </g>

    <!-- B) Transaminación a L-Alanina (ALT) -->
    <g transform="translate(720, 2260)">
      <line x1="0" y1="15" x2="0" y2="55" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <text x="12" y="38" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#047857">ALT (Glutamato ⇄ α-KG)</text>
      <rect x="-60" y="60" width="120" height="28" rx="6" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
      <text x="0" y="78" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#065f46" text-anchor="middle">L-Alanina</text>
    </g>
    """)


    # =========================================================================
    # EJE 2: VÍA DE LAS PENTOSAS FOSFATO (DERECHA: X ≈ 1400 a 2300)
    # =========================================================================
    # Conexión física desde G6P hacia G6PDH
    svg_parts.append("""
    <path d="M 830 395 Q 1150 365 1370 395" fill="none" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
    <g transform="translate(1100, 355)">
      <rect x="-85" y="-12" width="170" height="24" rx="12" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
      <text x="0" y="4" fill="#6d28d9" font-size="10" font-weight="800" text-anchor="middle">ENTRADA AL SHUNT DE PENTOSAS</text>
    </g>
    """)

    # G6PDH
    svg_parts.append(f"""
    <g transform="translate(1250, 395)">
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
        x=1400, y=365,
        nombre="6-Fosfoglucono-δ-Lactona",
        carbonos="6 Carbonos (Lactona)",
        detalle="Éster intramolecular hidrolizable",
        svg_estructura=FOSFOGLUCONO_LACTONA_6
    ))

    # Lactonasa
    svg_parts.append("""
    <g transform="translate(1660, 415)">
      <line x1="0" y1="0" x2="60" y2="0" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M 10 -15 Q 30 -25 50 -15" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="30" y="-30" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#0284c7" text-anchor="middle">+ H₂O</text>
      <text x="30" y="16" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">6-P-Gluconolactonasa</text>
      <text x="30" y="28" font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" text-anchor="middle">EC 3.1.1.31</text>
    </g>
    """)

    # 2. 6-Fosfogluconato
    svg_parts.append(crear_metabolito(
        x=1770, y=365,
        nombre="6-Fosfogluconato",
        carbonos="6 Carbonos (Cadena lineal)",
        detalle="Ácido descarboxilable generador de NADPH",
        svg_estructura=FOSFOGLUCONATO_6
    ))

    # 6-PGDH
    svg_parts.append(crear_reaccion_oxidativa(
        x=1900, y=530,
        enzima="6-Fosfogluconato Deshidrogenasa",
        ec="EC 1.1.1.44 (Descarboxilación)",
        genera_nadph=True,
        salida_co2=True,
        altura=54
    ))

    # 3. Ribulosa-5-P
    svg_parts.append(crear_metabolito(
        x=1770, y=620,
        nombre="D-Ribulosa-5-Fosfato",
        carbonos="5 Carbonos (Pentosa Cetosa)",
        detalle="Cruce a la fase no oxidativa",
        svg_estructura=RIBULOSA_5_FOSFATO
    ))

    # Ramificación X5P y R5P
    svg_parts.append("""
    <g transform="translate(1900, 775)">
      <path d="M -20 0 Q -110 30 -160 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(-175, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800" text-anchor="end">Fosfopentosa Epimerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 5.1.3.1 (⇄)</text>
      </g>
      <path d="M 20 0 Q 110 30 180 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(175, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Fosfopentosa Isomerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 5.3.1.6 (⇄)</text>
      </g>
    </g>
    """)

    # 4a. Xilulosa-5-P
    svg_parts.append(crear_metabolito(
        x=1500, y=855,
        nombre="D-Xilulosa-5-P",
        carbonos="5 Carbonos (Epímero C3)",
        detalle="Donador de 2C (TPP)",
        svg_estructura=XILULOSA_5_FOSFATO,
        texto_izquierda=True
    ))

    # 4b. Ribosa-5-P
    svg_parts.append(crear_metabolito(
        x=2050, y=855,
        nombre="D-Ribosa-5-P",
        carbonos="5 Carbonos (Pentosa Aldosa)",
        detalle="Precursora de Nucleótidos",
        svg_estructura=RIBOSA_5_FOSFATO
    ))


    # =========================================================================
    # RUTA CITOSÓLICA FALTANTE 4: SÍNTESIS DE NUCLEÓTIDOS (EXTREMO DERECHO)
    # =========================================================================
    svg_parts.append("""
    <!-- TERRITORIO: SÍNTESIS DE NUCLEÓTIDOS (Extremo Derecho) -->
    <g transform="translate(2100, 990)">
      <line x1="0" y1="0" x2="0" y2="40" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
      <text x="12" y="24" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#7c3aed">PRPP Sintetasa (ATP→AMP)</text>

      <g transform="translate(0, 48)">
        <rect x="-100" y="0" width="200" height="75" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
        <text x="0" y="18" fill="#6d28d9" font-size="11" font-weight="900" text-anchor="middle">SÍNTESIS DE NUCLEÓTIDOS</text>
        <text x="0" y="34" fill="#7c3aed" font-size="9.5" font-weight="700" text-anchor="middle">PRPP ➔ Purinas (IMP, AMP, GMP)</text>
        <text x="0" y="49" fill="#7c3aed" font-size="9.5" font-weight="700" text-anchor="middle">PRPP ➔ Pirimidinas (UMP, CTP, TMP)</text>
        <text x="0" y="64" fill="#94a3b8" font-size="8.5" text-anchor="middle">Precursores de ARN / ADN en citosol</text>
      </g>
    </g>
    """)


    # =========================================================================
    # FASE NO OXIDATIVA DE PENTOSAS: TK1, TA, TK2 Y RETORNO
    # =========================================================================
    # TK1
    svg_parts.append(crear_paso_no_oxidativo(
        x=1820, y=1045,
        enzima="Transcetolasa (TK1)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Ribosa-5-P (5C)",
        productos_txt="GAP (3C) + Sedoheptulosa-7-P (7C)"
    ))

    # Sedoheptulosa-7-P
    svg_parts.append(crear_metabolito(
        x=1500, y=1125,
        nombre="Sedoheptulosa-7-P",
        carbonos="7 Carbonos (Cetosa)",
        detalle="Intermediario de 7C",
        svg_estructura=SEDOHEPTULOSA_7_FOSFATO,
        texto_izquierda=True
    ))

    # GAP intermediario
    svg_parts.append(crear_metabolito(
        x=2050, y=1125,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="Intermediario transferible",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))

    # TA
    svg_parts.append(crear_paso_no_oxidativo(
        x=1820, y=1275,
        enzima="Transaldolasa (TA)",
        ec="EC 2.2.1.2 (Base de Schiff con Lisina)",
        sustratos_txt="Sedoheptulosa-7-P (7C) + GAP (3C)",
        productos_txt="Fructosa-6-P (6C) + Eritrosa-4-P (4C)"
    ))

    # Eritrosa-4-P
    svg_parts.append(crear_metabolito(
        x=1500, y=1355,
        nombre="D-Eritrosa-4-P",
        carbonos="4 Carbonos (Tetrosa)",
        detalle="Aceptor para segunda transcetolasa",
        svg_estructura=ERITROSA_4_FOSFATO,
        texto_izquierda=True
    ))

    # F6P (1er reingreso)
    svg_parts.append(crear_metabolito(
        x=2050, y=1355,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡1.er Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # TK2
    svg_parts.append(crear_paso_no_oxidativo(
        x=1820, y=1505,
        enzima="Transcetolasa (TK2)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Eritrosa-4-P (4C)",
        productos_txt="Fructosa-6-P (6C) + GAP (3C)"
    ))

    # F6P (2º reingreso)
    svg_parts.append(crear_metabolito(
        x=1500, y=1585,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="¡2.º Reingreso a la Glucólisis!",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        texto_izquierda=True
    ))

    # GAP (2º reingreso)
    svg_parts.append(crear_metabolito(
        x=2050, y=1585,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="¡Reingreso de triosa a la Glucólisis!",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))

    # FLECHAS DE RETORNO FÍSICO A LA GLUCÓLISIS
    svg_parts.append("""
    <!-- RETORNO 1: Fructosa-6-P hacia F6P Glucolítico -->
    <path d="M 2040 1395 C 1650 1320 1200 950 830 635" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(1320, 900)">
      <rect x="-85" y="-11" width="170" height="22" rx="11" fill="#ecfdf5" stroke="#059669" stroke-width="1.6"/>
      <text x="0" y="4" fill="#047857" font-size="10" font-weight="800" text-anchor="middle">RETORNO: F-6-P A GLUCÓLISIS</text>
    </g>

    <!-- RETORNO 2: GAP hacia GAP Glucolítico -->
    <path d="M 2040 1620 C 1650 1560 1200 1320 1010 1095" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
    <g transform="translate(1480, 1420)">
      <rect x="-85" y="-11" width="170" height="22" rx="11" fill="#ecfdf5" stroke="#059669" stroke-width="1.6"/>
      <text x="0" y="4" fill="#047857" font-size="10" font-weight="800" text-anchor="middle">RETORNO: GAP A GLUCÓLISIS</text>
    </g>
    """)


    # =========================================================================
    # RUTA CITOSÓLICA FALTANTE 5: CICLO DE LA UREA (TRAMO CITOSÓLICO)
    # =========================================================================
    svg_parts.append("""
    <!-- TERRITORIO: TRAMO CITOSÓLICO DEL CICLO DE LA UREA (Zona Inferior Derecha) -->
    <g transform="translate(1820, 1850)">
      <rect x="0" y="0" width="380" height="240" rx="10" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8" stroke-dasharray="6 4" opacity="0.95"/>
      <text x="15" y="22" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#1d4ed8">CICLO DE LA UREA (CITOSOL)</text>

      <!-- Entrada de Citrulina desde la matriz mitocondrial -->
      <g transform="translate(60, 60)">
        <rect x="-40" y="-14" width="80" height="28" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#1e40af" text-anchor="middle">Citrulina</text>
        <text x="0" y="24" font-family="'Inter', sans-serif" font-size="8" fill="#60a5fa" text-anchor="middle">(Sale de matriz)</text>
      </g>

      <!-- Reacción: Argininosuccinato Sintetasa (+ Aspartato / ATP) -->
      <path d="M 110 60 L 190 60" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="150" y="52" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#1d4ed8" text-anchor="middle">+ Aspartato / ATP</text>

      <g transform="translate(250, 60)">
        <rect x="-50" y="-14" width="100" height="28" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#1e40af" text-anchor="middle">Argininosuccinato</text>
      </g>

      <!-- Reacción: Argininosuccinato Liasa (Libera Fumarato) -->
      <path d="M 250 80 L 250 125" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="260" y="105" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#1d4ed8">— Fumarato</text>

      <g transform="translate(250, 145)">
        <rect x="-40" y="-14" width="80" height="28" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#1e40af" text-anchor="middle">L-Arginina</text>
      </g>

      <!-- Reacción: Arginasa (Genera Urea y Ornitina) -->
      <path d="M 200 145 L 120 145" stroke="#3b82f6" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="160" y="137" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#2563eb" text-anchor="middle">Arginasa (+ H₂O)</text>

      <!-- UREA (EXCRECIÓN) -->
      <g transform="translate(70, 145)">
        <rect x="-45" y="-16" width="90" height="32" rx="6" fill="#dbeafe" stroke="#1d4ed8" stroke-width="2"/>
        <text x="0" y="4" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="900" fill="#1e3a8a" text-anchor="middle">UREA</text>
        <text x="0" y="28" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#2563eb" text-anchor="middle">Excreción renal</text>
      </g>

      <!-- Ornitina reingresando a la mitocondria -->
      <path d="M 70 170 Q 70 210 20 230" fill="none" stroke="#3b82f6" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowBlue)"/>
      <text x="60" y="210" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#1d4ed8">Ornitina (a matriz)</text>
    </g>

    <!-- Conexión física entre la lanzadera mitocondrial y el ciclo de la urea -->
    <path d="M 1900 2180 L 1900 2100" stroke="#059669" stroke-width="2.2" stroke-dasharray="5 3" marker-end="url(#arrowGreen)"/>
    """)

    # Ensamblar SVG final
    svg_final = "\n".join(svg_parts)

    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>El Citosol Celular - Mapa Compartimental Completo</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #cbd5e1;
      color: #0f172a;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .lienzo-svg {{
      width: 100%;
      max-width: {ANCHO_CANVAS}px;
      background: #f1f5f9;
      border: 1px solid #94a3b8;
      border-radius: 12px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
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

        <!-- Degradado suave citosólico -->
        <radialGradient id="gradCitosolSuave" cx="45%" cy="40%" r="60%">
          <stop offset="0%" stop-color="#ffffff" stop-opacity="1" />
          <stop offset="60%" stop-color="#f8fafc" stop-opacity="0.95" />
          <stop offset="100%" stop-color="#f1f5f9" stop-opacity="0.9" />
        </radialGradient>
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
        f.write(generar_html_mapa_citosol())
    print(f"✅ Esquema cerrado del Citosol con todas las rutas generado en: {ruta_salida}")
