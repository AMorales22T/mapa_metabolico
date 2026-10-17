# =============================================================================
# MÓDULO DE REVISIÓN: Mitocondria Biológica y Funciones Constructoras
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/carbohidratos_unidos/generar_carbohidratos_unidos.py (líneas 340 a 532 de 1241)
# Descripción      : Renderizado mitocondrial y helpers de metabolitos y reacciones.
# =============================================================================

def generar_mitocondria_biologica(x_inicio=1020, ancho_mito=2350, y_base=2220):
    """
    Genera la mitocondria biológica completa en la base, amplia y detallada
    con doble membrana, crestas invaginadas, MPC y acople con PDH y Krebs.
    """
    x_piruvato_global, _ = punto_nodo("piruvato")
    x_acetil_global, y_acetil_global = punto_nodo("acetil_coa")
    x_piruvato_local = x_piruvato_global - x_inicio
    x_acetil_local = x_acetil_global - x_inicio
    y_acetil_local = y_acetil_global - y_base

    return f"""
    <!-- ================================================================= -->
    <!-- MITOCONDRIA: ORGANELO CONECTADO Y ABIERTO A FUTURAS RUTAS          -->
    <!-- ================================================================= -->
    <g id="mitocondria-organelo" transform="translate({x_inicio}, {y_base})">
      <!-- Membrana externa: forma arriñonada, ya no una franja flotante -->
      <path d="M -485 235 C -455 105, -220 28, 75 78 C 360 18, 650 36, 910 70
               C 1190 20, 1470 48, 1670 78 C 1970 30, 2250 68, 2310 170
               C 2365 270, 2270 414, 2050 468 C 1690 520, 1330 465, 1010 488
               C 650 515, 220 520, -120 470 C -390 430, -540 350, -485 235 Z"
            fill="url(#gradMitocondria)" stroke="#92400e" stroke-width="6"/>

      <!-- Espacio intermembrana: doble contorno reconocible -->
      <path d="M -420 245 C -380 145, -190 82, 80 112 C 360 62, 650 78, 900 108
               C 1190 68, 1460 88, 1640 110 C 1930 72, 2170 98, 2255 180
               C 2300 260, 2200 365, 2020 415 C 1680 458, 1320 410, 1000 432
               C 650 458, 270 470, -100 420 C -350 385, -475 330, -420 245 Z"
            fill="#fffbeb" fill-opacity="0.55" stroke="#b45309" stroke-width="3" stroke-dasharray="10 6"/>

      <!-- Matriz mitocondrial: gran espacio interno para futuras rutas -->
      <path d="M -350 260 C -250 170, -60 145, 145 168 C 350 118, 560 150, 710 165
               C 960 120, 1210 145, 1430 170 C 1700 130, 1970 155, 2110 215
               C 2160 280, 2070 335, 1900 360 C 1600 395, 1300 350, 1010 375
               C 700 395, 360 410, 80 365 C -120 350, -400 330, -350 260 Z"
            fill="#fef3c7" fill-opacity="0.52" stroke="#d97706" stroke-width="3"/>

      <!-- Crestas internas onduladas, dejando corredores libres entre ellas -->
      <g fill="none" stroke="#b45309" stroke-width="5" stroke-linecap="round" opacity="0.72">
        <path d="M -300 275 C -210 205, -135 315, -45 238 C 35 180, 100 290, 180 225"/>
        <path d="M 215 315 C 300 240, 370 350, 455 275 C 525 220, 590 325, 665 260"/>
        <path d="M 300 245 C 390 180, 465 300, 555 225 C 635 170, 700 300, 790 235"/>
        <path d="M 915 290 C 1010 215, 1080 330, 1175 250 C 1260 190, 1335 315, 1420 245"/>
        <path d="M 1535 295 C 1630 220, 1700 330, 1790 255 C 1865 205, 1930 300, 2000 250"/>
      </g>
      <g fill="#fef9c3" stroke="#d97706" stroke-width="2" opacity="0.82">
        <ellipse cx="430" cy="275" rx="82" ry="27"/>
        <ellipse cx="1045" cy="300" rx="92" ry="28"/>
        <ellipse cx="1660" cy="300" rx="90" ry="27"/>
      </g>

      <!-- Título integrado en el propio orgánulo -->
      <text x="1280" y="145" fill="#78350f" font-size="22" font-weight="900" letter-spacing="1.4">MATRIZ MITOCONDRIAL</text>
      <text x="1280" y="169" fill="#92400e" font-size="12" font-weight="700">Conversión del piruvato y oxidación aeróbica</text>

      <!-- MPC en el punto de contacto con el piruvato -->
      <g transform="translate(530, 78)">
        <rect x="0" y="0" width="66" height="38" rx="9" fill="#92400e" stroke="#78350f" stroke-width="2.5"/>
        <text x="33" y="25" fill="#ffffff" font-size="15" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MPC</text>
      </g>
      <circle cx="505" cy="97" r="18" fill="#92400e"/>
      <text x="505" y="103" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">1</text>
      <text x="620" y="94" fill="#78350f" font-size="13" font-weight="900">TRANSPORTE</text>
      <text x="620" y="112" fill="#92400e" font-size="10.5" font-weight="700">Piruvato + H⁺ atraviesan MPC</text>

      <!-- Conexión visible desde el piruvato citosólico hasta el MPC -->
      <path d="M {x_piruvato_local} -200 C {x_piruvato_local + 20} -145, 560 -45, 563 80" fill="none" stroke="#ea580c" stroke-width="4" stroke-dasharray="12 8" marker-end="url(#arrowFlow)"/>

      <!-- Flecha de lectura: del transportador hacia PDH -->
      <path d="M 600 110 C 690 105, 735 135, 770 168" fill="none" stroke="#ea580c" stroke-width="4" marker-end="url(#arrowFlow)"/>

      <!-- PDH como segunda estación dentro de la matriz -->
      <g transform="translate(965, 145)">
        <circle cx="-290" cy="28" r="18" fill="#c2410c"/>
        <text x="-290" y="34" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">2</text>
        <rect x="-245" y="0" width="500" height="86" rx="14" fill="#fff7ed" fill-opacity="0.96" stroke="#c2410c" stroke-width="2.5"/>
        <text x="5" y="25" fill="#78350f" font-size="16" font-weight="900" text-anchor="middle">PDH: PIRUVATO ➔ ACETIL-CoA</text>
        <text x="5" y="47" fill="#c2410c" font-size="12" font-weight="800" text-anchor="middle">+ CoA-SH + NAD⁺ ➔ CO₂ + NADH</text>
        <text x="5" y="68" fill="#64748b" font-size="11" text-anchor="middle">E1 (TPP) • E2 (Lipoamida) • E3 (FAD)</text>
      </g>

      <!-- Entrada al ciclo de Krebs, como tercer paso explícito -->
      <path d="M 1220 205 C 1320 240, 1390 268, 1450 290" fill="none" stroke="#ea580c" stroke-width="4" marker-end="url(#arrowFlow)"/>
      <g transform="translate({x_acetil_local}, {y_acetil_local})">
        <circle cx="-285" cy="32" r="18" fill="#d97706"/>
        <text x="-285" y="38" fill="#ffffff" font-size="15" font-weight="900" text-anchor="middle">3</text>
        <rect x="-240" y="0" width="520" height="72" rx="12" fill="#fffbeb" fill-opacity="0.96" stroke="#d97706" stroke-width="2.5"/>
        <text x="20" y="26" fill="#92400e" font-size="15" font-weight="900" text-anchor="middle">ACETIL-CoA ➔ CICLO DE KREBS</text>
        <text x="20" y="49" fill="#b45309" font-size="12" font-weight="700" text-anchor="middle">+ Oxalacetato ➔ Citrato (6C)</text>
      </g>

      <!-- Zona libre para ampliar el mapa mitocondrial -->
      <text x="2070" y="300" fill="#92400e" font-size="12" font-weight="800" opacity="0.72">NADH / FADH₂ → cadena respiratoria</text>
      <path d="M 1970 320 Q 2150 350 2260 300" fill="none" stroke="#b45309" stroke-width="2.5" stroke-dasharray="9 7" opacity="0.62"/>
    </g>
    """

def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False, dx_texto=140):
    """
    Generador modular de metabolitos LIMPIO (SIN globos ni rectángulos artificiales).
    """
    if texto_izquierda:
        pos_estructura = "translate(0, 0)"
        pos_texto = f"translate(-25, 28)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = f"translate({dx_texto}, 28)"
        alineacion = ''

    estructura_render = "" if MODO_BOCETO else svg_estructura

    return f"""
    <!-- Metabolito: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="{pos_estructura}">
        {estructura_render}
      </g>
      <g transform="{pos_texto}">
        <text x="0" y="0" fill="#0f172a" font-size="17" font-weight="800" {alineacion}>{nombre}</text>
        <text x="0" y="20" fill="#ea580c" font-size="13" font-weight="700" {alineacion}>{carbonos}</text>
        <text x="0" y="37" fill="#475569" font-size="12" font-weight="600" {alineacion}>{detalle}</text>
      </g>
    </g>
    """

def crear_reaccion(x, y, enzima, ec="", regulacion="", entra_energia="", sale_energia="", 
                   reversible=False, es_ganancia=False, salida_agua=False, altura=50):
    """Generador de reacción vertical estándar."""
    curvas_energia = ""
    if entra_energia:
        color_entrada = "#dc2626" if not es_ganancia else "#475569"
        marcador_entrada = "url(#arrowRed)" if not es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -85 9 Q -30 9 -4 20" fill="none" stroke="{color_entrada}" stroke-width="2" marker-end="{marcador_entrada}"/>
        <text x="-92" y="13" fill="{color_entrada}" font-size="12" font-weight="800" text-anchor="end">{entra_energia}</text>
        """
    if sale_energia:
        color_salida = "#059669" if es_ganancia else "#475569"
        marcador_salida = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas_energia += f"""
        <path d="M -4 26 Q -30 37 -85 37" fill="none" stroke="{color_salida}" stroke-width="2" marker-end="{marcador_salida}"/>
        <text x="-92" y="41" fill="{color_salida}" font-size="12" font-weight="800" text-anchor="end">{sale_energia}</text>
        """
    if salida_agua:
        curvas_energia += """
        <path d="M -4 26 Q -30 37 -80 37" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
        <text x="-86" y="41" fill="#0284c7" font-size="12" font-weight="800" text-anchor="end">- 2 H₂O</text>
        """

    if reversible:
        flecha = f"""
        <line x1="-3.5" y1="0" x2="-3.5" y2="{altura}" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        <line x1="3.5" y1="{altura}" x2="3.5" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        """
    else:
        flecha = f"""
        <line x1="0" y1="0" x2="0" y2="{altura}" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>
        """

    regulacion_svg = ""
    if regulacion:
        color_reg = "#e11d48" if "⊣" in regulacion else "#16a34a"
        regulacion_svg = f'<text x="0" y="30" fill="{color_reg}" font-size="11" font-weight="700">{regulacion}</text>'

    return f"""
    <!-- Reacción: {enzima} -->
    <g transform="translate({x}, {y})">
      {flecha}
      {curvas_energia}
      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="14.5" font-weight="800">{enzima}</text>
        <text x="0" y="15" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        {regulacion_svg}
      </g>
    </g>
    """

def crear_paso_no_oxidativo(x, y, enzima, ec, sustratos_txt, productos_txt):
    """Generador de nodo de transferencia no oxidativa."""
    return f"""
    <!-- Reacción de Transferencia: {enzima} -->
    <g transform="translate({x}, {y})">
      <line x1="-3.5" y1="0" x2="-3.5" y2="48" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="3.5" y1="48" x2="3.5" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(22, 12)">
        <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="800">{enzima}</text>
        <text x="0" y="16" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        <text x="0" y="32" fill="#c2410c" font-size="11.5" font-weight="700">{sustratos_txt} ⇄ {productos_txt}</text>
      </g>
    </g>
    """

