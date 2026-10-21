# =============================================================================
# MÓDULO DE REVISIÓN: Funciones de Bloques de Leyenda y Autoría
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 339 a 679 de 4188)
# Descripción      : Genera el cuadro institucional inferior de 17 vías, código de colores y ficha de autoría.
# =============================================================================

def generar_bloque_leyenda(x=120, y=4220):
    """
    Genera la Leyenda General con:
    1. Lista numerada de 14 vías con sus badges coincidentes con el mapa.
    2. Clave de símbolos ((+), (-), (P), [Hormonal], ⇄, →, - - →, ▭, [nC]).
    3. Código de colores biológicos.
    """
    filas_vias = []
    # Dividir las vías en 2 columnas equilibradas dinámicamente
    mid = (len(regulacion.VIAS) + 1) // 2
    col1 = regulacion.VIAS[:mid]
    col2 = regulacion.VIAS[mid:]

    color_vias = {
        1: "#0284c7", 2: "#7c3aed", 3: "#ea580c", 4: "#059669",
        5: "#c2410c", 6: "#d97706", 7: "#16a34a", 8: "#0284c7",
        9: "#b45309", 10: "#0d9488", 11: "#be123c", 12: "#4f46e5",
        "12B": "#6366f1", 13: "#2563eb", 14: "#0891b2", 15: "#0284c7",
        16: "#475569", 17: "#be123c"
    }

    svg_col1 = []
    y_pos = 0
    for v in col1:
        c_v = color_vias.get(v['n'], "#0284c7")
        svg_col1.append(f"""
        <g id="badge_leyenda_{v['n']}" class="badge-via" data-via="{v['n']}" transform="translate(0, {y_pos})" style="cursor: pointer;">
          <circle cx="12" cy="0" r="10" fill="{c_v}" />
          <text x="12" y="3.5" fill="#ffffff" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{v['n']}</text>
          <text x="30" y="3" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif">{v['nombre']}</text>
          <text x="30" y="16" fill="#64748b" font-size="9" font-family="'Inter', sans-serif">{v['resumen'][:55]}</text>
        </g>
        """)
        y_pos += 44

    svg_col2 = []
    y_pos = 0
    for v in col2:
        c_v = color_vias.get(v['n'], "#0284c7")
        svg_col2.append(f"""
        <g id="badge_leyenda_{v['n']}" class="badge-via" data-via="{v['n']}" transform="translate(0, {y_pos})" style="cursor: pointer;">
          <circle cx="12" cy="0" r="10" fill="{c_v}" />
          <text x="12" y="3.5" fill="#ffffff" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{v['n']}</text>
          <text x="30" y="3" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif">{v['nombre']}</text>
          <text x="30" y="16" fill="#64748b" font-size="9" font-family="'Inter', sans-serif">{v['resumen'][:55]}</text>
        </g>
        """)
        y_pos += 44

    # Símbolos y colores (Columna 3)
    simbolos_items = []
    y_sim = 0
    simbolos_limpios = [
        ("(+)", "Activador alostérico (efector positivo)"),
        ("(-)", "Inhibidor alostérico (efector negativo / retroinhibición)"),
        ("(P)", "Modificación covalente por fosforilación (forma activa)"),
        ("⇄", "Reacción reversible (doble flecha)"),
        ("→", "Reacción irreversible (flecha simple, punto de control)"),
        ("- - →", "Conexión entre vías / transporte"),
        ("▭", "Transportador de membrana (GLUT, MPC, CACT, AGC…)"),
        ("[nC]", "Número de átomos de carbono del metabolito")
    ]
    for sim, desc in simbolos_limpios:
        simbolos_items.append(f"""
        <g transform="translate(0, {y_sim})">
          <rect x="0" y="-10" width="40" height="18" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
          <text x="20" y="3" fill="#0f172a" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{sim}</text>
          <text x="50" y="3" fill="#334155" font-size="10" font-weight="700" font-family="'Inter', sans-serif">{desc}</text>
        </g>
        """)
        y_sim += 26

    colores = [
        ("#ea580c", "Flujo principal de carbono"),
        ("#7c3aed", "Reacciones de Gluconeogénesis (4 enzimas)"),
        ("#b45309", "Glucógeno (Síntesis y lisis)"),
        ("#059669", "Pentosas fosfato &amp; Shunt"),
        ("#2563eb", "Aminoácidos &amp; Ciclo de la Urea"),
        ("#16a34a", "(+) Activador alostérico"),
        ("#dc2626", "(-) Inhibidor alostérico / Gasto ATP"),
        ("#ca8a04", "(P) Modificación covalente activa/inactiva")
    ]
    colores_items = []
    y_col = 0
    for c_hex, c_desc in colores:
        colores_items.append(f"""
        <g transform="translate(0, {y_col})">
          <circle cx="6" cy="0" r="5" fill="{c_hex}"/>
          <text x="18" y="3.5" fill="#334155" font-size="9.5" font-weight="600" font-family="'Inter', sans-serif">{c_desc}</text>
        </g>
        """)
        y_col += 24

    return f"""
    <!-- BLOQUE INSTITUCIONAL: LEYENDA GENERAL DE VÍAS METABÓLICAS Y REGULACIÓN -->
    <g id="bloque_leyenda" data-arrastrable="1" transform="translate({x}, {y})" filter="url(#shadowCard)">
      <!-- Fondo -->
      <rect width="3650" height="480" rx="22" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" />
      <path d="M 0 22 Q 0 0 22 0 L 3628 0 Q 3650 0 3650 22 L 3650 10 L 0 10 Z" fill="url(#gradHeaderAutoria)" />

      <!-- Encabezado -->
      <g transform="translate(35, 30)">
        <rect x="0" y="0" width="230" height="24" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2" />
        <text x="115" y="16" fill="#0369a1" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="1">GUÍA Y CONVENCIONES</text>
        <text x="250" y="18" fill="#0f172a" font-size="19" font-weight="900" font-family="'Inter', sans-serif">LEYENDA DE VÍAS METABÓLICAS &amp; CONTROL ALOSTÉRICO / COVALENTE</text>
        <rect x="1350" y="-3" width="760" height="28" rx="7" fill="#fef3c7" stroke="#d97706" stroke-width="1.2"/>
        <text x="1360" y="15" fill="#92400e" font-size="11" font-weight="800" font-family="'Inter', sans-serif">[Nota] Célula didáctica/hepática: Gluconeogénesis, Cetogénesis y Ciclo de la Urea ocurren primordialmente en hepatocito</text>
      </g>
      <line x1="35" y1="68" x2="3615" y2="68" stroke="#e2e8f0" stroke-width="1.5" />

      <!-- Columnas 1 y 2: Vías (1 a 15) -->
      <g transform="translate(40, 100)">
        <text x="0" y="-12" fill="#0284c7" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">VÍAS METABÓLICAS (1–{mid}):</text>
        {''.join(svg_col1)}
      </g>
      <g transform="translate(940, 100)">
        <text x="0" y="-12" fill="#0284c7" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">VÍAS METABÓLICAS ({mid+1}–{len(regulacion.VIAS)}):</text>
        {''.join(svg_col2)}
      </g>

      <line x1="1840" y1="85" x2="1840" y2="430" stroke="#f1f5f9" stroke-width="2" />

      <!-- Columna 3: Símbolos -->
      <g transform="translate(1870, 100)">
        <text x="0" y="-12" fill="#0f766e" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">CONVENCIONES Y EFECTORES:</text>
        {''.join(simbolos_items)}
      </g>

      <line x1="2670" y1="85" x2="2670" y2="430" stroke="#f1f5f9" stroke-width="2" />

      <!-- Columna 4: Código de Colores -->
      <g transform="translate(2700, 100)">
        <text x="0" y="-12" fill="#b45309" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">CÓDIGO DE COLORES:</text>
        {''.join(colores_items)}
      </g>

      <line x1="3050" y1="85" x2="3050" y2="430" stroke="#f1f5f9" stroke-width="2" />

      <!-- Columna 5: Clasificación Enzimática EC -->
      <g id="leyenda_col_ec" transform="translate(3080, 100)">
        <text x="0" y="-12" fill="#7c3aed" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">NOMENCLATURA ENZIMÁTICA (EC):</text>
        
        <!-- Header badge y título -->
        <g transform="translate(0, -2)">
          <rect x="0" y="-8" width="84" height="21" rx="5" fill="#f5f3ff" stroke="#c4b5fd" stroke-width="1.2"/>
          <text x="42" y="6.5" fill="#6d28d9" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC x.x.x.x</text>
          <text x="96" y="6.5" fill="#0f172a" font-size="11" font-weight="800" font-family="'Inter', sans-serif">Comisión de Enzimas (Enzyme Commission)</text>
        </g>
        
        <!-- Intro -->
        <text x="0" y="34" fill="#475569" font-size="10" font-weight="600" font-family="'Inter', sans-serif">Código numérico de 4 cifras que identifica cada enzima por la reacción que cataliza:</text>

        <!-- 1.ª Cifra -->
        <text x="0" y="58" fill="#1e293b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif"><tspan fill="#7c3aed" font-weight="900">1.ª cifra</tspan> · Clase principal de reacción (1 a 7):</text>

        <!-- 7 Clases en 2 columnas -->
        <!-- Columna A (1-4) -->
        <g transform="translate(0, 70)">
          <g transform="translate(0, 0)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">1</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Oxidorreductasas</tspan> (redox / electrones)</text>
          </g>
          <g transform="translate(0, 23)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">2</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Transferasas</tspan> (transferencia de grupos)</text>
          </g>
          <g transform="translate(0, 46)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Hidrolasas</tspan> (ruptura de enlaces por H₂O)</text>
          </g>
          <g transform="translate(0, 69)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">4</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Liasas</tspan> (ruptura/adición sin agua)</text>
          </g>
        </g>

        <!-- Columna B (5-7) -->
        <g transform="translate(265, 70)">
          <g transform="translate(0, 0)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">5</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Isomerasas</tspan> (isomerización estructural)</text>
          </g>
          <g transform="translate(0, 23)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">6</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Ligasas</tspan> (unión molecular + hidrólisis ATP)</text>
          </g>
          <g transform="translate(0, 46)">
            <rect x="0" y="-8" width="17" height="17" rx="4" fill="#ede9fe" stroke="#a78bfa" stroke-width="1"/>
            <text x="8.5" y="4.5" fill="#6d28d9" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">7</text>
            <text x="24" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Translocasas</tspan> (transporte de membrana)</text>
          </g>
        </g>

        <!-- 2.ª y 3.ª Cifras -->
        <g transform="translate(0, 168)">
          <rect x="0" y="-8" width="54" height="18" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
          <text x="27" y="4.5" fill="#0f172a" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">2.ª, 3.ª</text>
          <text x="63" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Subclase y sub-subclase:</tspan> tipo de grupo funcional o sustrato donador/aceptor.</text>
        </g>

        <!-- 4.ª Cifra -->
        <g transform="translate(0, 196)">
          <rect x="0" y="-8" width="54" height="18" rx="4" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
          <text x="27" y="4.5" fill="#0f172a" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">4.ª</text>
          <text x="63" y="4.5" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif"><tspan font-weight="800">Número de orden:</tspan> identificador secuencial de la enzima dentro de su sub-subclase.</text>
        </g>

        <!-- Micro-tarjeta de ejemplo -->
        <g transform="translate(0, 226)">
          <rect x="0" y="0" width="530" height="44" rx="7" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2"/>
          <text x="12" y="18" fill="#64748b" font-size="9" font-weight="800" font-family="'JetBrains Mono', monospace">Ejemplo:</text>
          <text x="74" y="18" fill="#0f172a" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace">EC 2.7.1.1 · Hexoquinasa</text>
          <text x="12" y="33" fill="#64748b" font-size="8.5" font-family="'Inter', sans-serif">2: Transferasa ➔ 7: Fosfotransferasa ➔ 1: Aceptor grupo -OH ➔ 1: D-hexosa-6-fosfotransferasa</text>
        </g>
      </g>
    </g>
    """

def generar_bloque_autoria(x=3800, y=4220):
    """
    Genera el bloque institucional / autoría de código abierto de formato ampliado
    (1860 × 505 px) con fuentes científicas completas, herramientas de ingeniería,
    enlace a GitHub y código QR escaneable de alta definición.
    """
    qr_path = "M0,0h1v1h-1zM1,0h1v1h-1zM2,0h1v1h-1zM3,0h1v1h-1zM4,0h1v1h-1zM5,0h1v1h-1zM6,0h1v1h-1zM11,0h1v1h-1zM12,0h1v1h-1zM14,0h1v1h-1zM17,0h1v1h-1zM22,0h1v1h-1zM23,0h1v1h-1zM24,0h1v1h-1zM25,0h1v1h-1zM26,0h1v1h-1zM27,0h1v1h-1zM28,0h1v1h-1zM0,1h1v1h-1zM6,1h1v1h-1zM9,1h1v1h-1zM10,1h1v1h-1zM14,1h1v1h-1zM16,1h1v1h-1zM17,1h1v1h-1zM18,1h1v1h-1zM20,1h1v1h-1zM22,1h1v1h-1zM28,1h1v1h-1zM0,2h1v1h-1zM2,2h1v1h-1zM3,2h1v1h-1zM4,2h1v1h-1zM6,2h1v1h-1zM12,2h1v1h-1zM14,2h1v1h-1zM16,2h1v1h-1zM18,2h1v1h-1zM19,2h1v1h-1zM20,2h1v1h-1zM22,2h1v1h-1zM24,2h1v1h-1zM25,2h1v1h-1zM26,2h1v1h-1zM28,2h1v1h-1zM0,3h1v1h-1zM2,3h1v1h-1zM3,3h1v1h-1zM4,3h1v1h-1zM6,3h1v1h-1zM8,3h1v1h-1zM12,3h1v1h-1zM13,3h1v1h-1zM15,3h1v1h-1zM17,3h1v1h-1zM19,3h1v1h-1zM20,3h1v1h-1zM22,3h1v1h-1zM24,3h1v1h-1zM25,3h1v1h-1zM26,3h1v1h-1zM28,3h1v1h-1zM0,4h1v1h-1zM2,4h1v1h-1zM3,4h1v1h-1zM4,4h1v1h-1zM6,4h1v1h-1zM8,4h1v1h-1zM9,4h1v1h-1zM15,4h1v1h-1zM16,4h1v1h-1zM18,4h1v1h-1zM19,4h1v1h-1zM20,4h1v1h-1zM22,4h1v1h-1zM24,4h1v1h-1zM25,4h1v1h-1zM26,4h1v1h-1zM28,4h1v1h-1zM0,5h1v1h-1zM6,5h1v1h-1zM11,5h1v1h-1zM12,5h1v1h-1zM14,5h1v1h-1zM16,5h1v1h-1zM18,5h1v1h-1zM20,5h1v1h-1zM22,5h1v1h-1zM28,5h1v1h-1zM0,6h1v1h-1zM1,6h1v1h-1zM2,6h1v1h-1zM3,6h1v1h-1zM4,6h1v1h-1zM5,6h1v1h-1zM6,6h1v1h-1zM8,6h1v1h-1zM10,6h1v1h-1zM12,6h1v1h-1zM14,6h1v1h-1zM16,6h1v1h-1zM18,6h1v1h-1zM20,6h1v1h-1zM22,6h1v1h-1zM23,6h1v1h-1zM24,6h1v1h-1zM25,6h1v1h-1zM26,6h1v1h-1zM27,6h1v1h-1zM28,6h1v1h-1zM10,7h1v1h-1zM11,7h1v1h-1zM14,7h1v1h-1zM20,7h1v1h-1zM0,8h1v1h-1zM1,8h1v1h-1zM5,8h1v1h-1zM6,8h1v1h-1zM7,8h1v1h-1zM9,8h1v1h-1zM11,8h1v1h-1zM13,8h1v1h-1zM14,8h1v1h-1zM15,8h1v1h-1zM17,8h1v1h-1zM19,8h1v1h-1zM24,8h1v1h-1zM25,8h1v1h-1zM1,9h1v1h-1zM2,9h1v1h-1zM4,9h1v1h-1zM8,9h1v1h-1zM9,9h1v1h-1zM12,9h1v1h-1zM15,9h1v1h-1zM17,9h1v1h-1zM18,9h1v1h-1zM21,9h1v1h-1zM23,9h1v1h-1zM24,9h1v1h-1zM26,9h1v1h-1zM27,9h1v1h-1zM1,10h1v1h-1zM2,10h1v1h-1zM4,10h1v1h-1zM5,10h1v1h-1zM6,10h1v1h-1zM8,10h1v1h-1zM10,10h1v1h-1zM14,10h1v1h-1zM15,10h1v1h-1zM20,10h1v1h-1zM24,10h1v1h-1zM2,11h1v1h-1zM3,11h1v1h-1zM4,11h1v1h-1zM5,11h1v1h-1zM7,11h1v1h-1zM8,11h1v1h-1zM9,11h1v1h-1zM12,11h1v1h-1zM18,11h1v1h-1zM21,11h1v1h-1zM25,11h1v1h-1zM0,12h1v1h-1zM2,12h1v1h-1zM3,12h1v1h-1zM5,12h1v1h-1zM6,12h1v1h-1zM7,12h1v1h-1zM9,12h1v1h-1zM11,12h1v1h-1zM12,12h1v1h-1zM15,12h1v1h-1zM19,12h1v1h-1zM20,12h1v1h-1zM22,12h1v1h-1zM23,12h1v1h-1zM28,12h1v1h-1zM2,13h1v1h-1zM4,13h1v1h-1zM7,13h1v1h-1zM15,13h1v1h-1zM16,13h1v1h-1zM18,13h1v1h-1zM20,13h1v1h-1zM22,13h1v1h-1zM23,13h1v1h-1zM24,13h1v1h-1zM27,13h1v1h-1zM28,13h1v1h-1zM0,14h1v1h-1zM2,14h1v1h-1zM4,14h1v1h-1zM6,14h1v1h-1zM7,14h1v1h-1zM8,14h1v1h-1zM10,14h1v1h-1zM11,14h1v1h-1zM12,14h1v1h-1zM15,14h1v1h-1zM16,14h1v1h-1zM20,14h1v1h-1zM21,14h1v1h-1zM24,14h1v1h-1zM25,14h1v1h-1zM26,14h1v1h-1zM0,15h1v1h-1zM2,15h1v1h-1zM3,15h1v1h-1zM4,15h1v1h-1zM5,15h1v1h-1zM7,15h1v1h-1zM8,15h1v1h-1zM11,15h1v1h-1zM16,15h1v1h-1zM19,15h1v1h-1zM23,15h1v1h-1zM24,15h1v1h-1zM26,15h1v1h-1zM28,15h1v1h-1zM1,16h1v1h-1zM2,16h1v1h-1zM6,16h1v1h-1zM8,16h1v1h-1zM11,16h1v1h-1zM12,16h1v1h-1zM13,16h1v1h-1zM14,16h1v1h-1zM15,16h1v1h-1zM17,16h1v1h-1zM19,16h1v1h-1zM21,16h1v1h-1zM23,16h1v1h-1zM25,16h1v1h-1zM26,16h1v1h-1zM0,17h1v1h-1zM3,17h1v1h-1zM4,17h1v1h-1zM5,17h1v1h-1zM9,17h1v1h-1zM12,17h1v1h-1zM15,17h1v1h-1zM16,17h1v1h-1zM19,17h1v1h-1zM22,17h1v1h-1zM23,17h1v1h-1zM24,17h1v1h-1zM26,17h1v1h-1zM27,17h1v1h-1zM28,17h1v1h-1zM0,18h1v1h-1zM1,18h1v1h-1zM4,18h1v1h-1zM6,18h1v1h-1zM8,18h1v1h-1zM9,18h1v1h-1zM11,18h1v1h-1zM14,18h1v1h-1zM15,18h1v1h-1zM18,18h1v1h-1zM19,18h1v1h-1zM24,18h1v1h-1zM25,18h1v1h-1zM28,18h1v1h-1zM0,19h1v1h-1zM2,19h1v1h-1zM4,19h1v1h-1zM7,19h1v1h-1zM10,19h1v1h-1zM11,19h1v1h-1zM16,19h1v1h-1zM20,19h1v1h-1zM22,19h1v1h-1zM0,20h1v1h-1zM3,20h1v1h-1zM4,20h1v1h-1zM5,20h1v1h-1zM6,20h1v1h-1zM11,20h1v1h-1zM12,20h1v1h-1zM13,20h1v1h-1zM14,20h1v1h-1zM17,20h1v1h-1zM18,20h1v1h-1zM19,20h1v1h-1zM20,20h1v1h-1zM21,20h1v1h-1zM22,20h1v1h-1zM23,20h1v1h-1zM24,20h1v1h-1zM26,20h1v1h-1zM27,20h1v1h-1zM28,20h1v1h-1zM8,21h1v1h-1zM10,21h1v1h-1zM11,21h1v1h-1zM13,21h1v1h-1zM14,21h1v1h-1zM15,21h1v1h-1zM20,21h1v1h-1zM24,21h1v1h-1zM25,21h1v1h-1zM0,22h1v1h-1zM1,22h1v1h-1zM2,22h1v1h-1zM3,22h1v1h-1zM4,22h1v1h-1zM5,22h1v1h-1zM6,22h1v1h-1zM8,22h1v1h-1zM9,22h1v1h-1zM10,22h1v1h-1zM13,22h1v1h-1zM14,22h1v1h-1zM15,22h1v1h-1zM16,22h1v1h-1zM17,22h1v1h-1zM18,22h1v1h-1zM19,22h1v1h-1zM20,22h1v1h-1zM22,22h1v1h-1zM24,22h1v1h-1zM25,22h1v1h-1zM26,22h1v1h-1zM0,23h1v1h-1zM6,23h1v1h-1zM8,23h1v1h-1zM11,23h1v1h-1zM12,23h1v1h-1zM14,23h1v1h-1zM15,23h1v1h-1zM16,23h1v1h-1zM18,23h1v1h-1zM19,23h1v1h-1zM20,23h1v1h-1zM24,23h1v1h-1zM28,23h1v1h-1zM0,24h1v1h-1zM2,24h1v1h-1zM3,24h1v1h-1zM4,24h1v1h-1zM6,24h1v1h-1zM10,24h1v1h-1zM11,24h1v1h-1zM12,24h1v1h-1zM16,24h1v1h-1zM18,24h1v1h-1zM19,24h1v1h-1zM20,24h1v1h-1zM21,24h1v1h-1zM22,24h1v1h-1zM23,24h1v1h-1zM24,24h1v1h-1zM25,24h1v1h-1zM0,25h1v1h-1zM2,25h1v1h-1zM3,25h1v1h-1zM4,25h1v1h-1zM6,25h1v1h-1zM10,25h1v1h-1zM11,25h1v1h-1zM13,25h1v1h-1zM15,25h1v1h-1zM19,25h1v1h-1zM20,25h1v1h-1zM21,25h1v1h-1zM25,25h1v1h-1zM26,25h1v1h-1zM28,25h1v1h-1zM0,26h1v1h-1zM2,26h1v1h-1zM3,26h1v1h-1zM4,26h1v1h-1zM6,26h1v1h-1zM14,26h1v1h-1zM15,26h1v1h-1zM17,26h1v1h-1zM18,26h1v1h-1zM19,26h1v1h-1zM20,26h1v1h-1zM21,26h1v1h-1zM22,26h1v1h-1zM23,26h1v1h-1zM24,26h1v1h-1zM25,26h1v1h-1zM26,26h1v1h-1zM27,26h1v1h-1zM0,27h1v1h-1zM6,27h1v1h-1zM8,27h1v1h-1zM10,27h1v1h-1zM12,27h1v1h-1zM14,27h1v1h-1zM18,27h1v1h-1zM22,27h1v1h-1zM23,27h1v1h-1zM25,27h1v1h-1zM26,27h1v1h-1zM28,27h1v1h-1zM0,28h1v1h-1zM1,28h1v1h-1zM2,28h1v1h-1zM3,28h1v1h-1zM4,28h1v1h-1zM5,28h1v1h-1zM6,28h1v1h-1zM8,28h1v1h-1zM11,28h1v1h-1zM12,28h1v1h-1zM13,28h1v1h-1zM14,28h1v1h-1zM15,28h1v1h-1zM16,28h1v1h-1zM19,28h1v1h-1zM22,28h1v1h-1zM23,28h1v1h-1zM24,28h1v1h-1zM26,28h1v1h-1z"
    return f'''
    <!-- BLOQUE INSTITUCIONAL Y AUTORÍA DE CÓDIGO ABIERTO (ADOLFO MORALES TENA) - FORMATO AMPLIADO -->
    <g id="bloque_autoria" data-arrastrable="1" transform="translate({x}, {y})" filter="url(#shadowCard)">
      <!-- Fondo de la tarjeta -->
      <rect width="1860" height="505" rx="22" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" />
      
      <!-- Barra superior de acento degradado -->
      <path d="M 0 22 Q 0 0 22 0 L 1838 0 Q 1860 0 1860 22 L 1860 10 L 0 10 Z" fill="url(#gradHeaderAutoria)" />

      <!-- Encabezado superior -->
      <g transform="translate(35, 26)">
        <rect x="0" y="0" width="310" height="24" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.2" />
        <text x="155" y="16" fill="#0369a1" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="1">METABOLISMO Y SU REGULACIÓN</text>
        <!-- Título en Arte ASCII: Mapa Metabólico -->
        <text x="330" y="2" fill="#0f172a" font-family="'JetBrains Mono', monospace" font-size="5.4" font-weight="800" xml:space="preserve" style="white-space: pre; line-height: 5.6px;">
          <tspan x="330" y="2"> __  __                         __  __      _        _           _ _           </tspan>
          <tspan x="330" y="7.6">|  \/  | __ _ _ __   __ _      |  \/  | ___| |_ __ _| |__   ___ | (_) ___ ___  </tspan>
          <tspan x="330" y="13.2">| |\/| |/ _` | '_ \ / _` |_____| |\/| |/ _ \ __/ _` | '_ \ / _ \| | |/ __/ _ \ </tspan>
          <tspan x="330" y="18.8">| |  | | (_| | |_) | (_| |_____| |  | |  __/ || (_| | |_) | (_) | | | (_| (_) |</tspan>
          <tspan x="330" y="24.4">|_|  |_|\__,_| .__/ \__,_|     |_|  |_|\___|\__\__,_|_.__/ \___/|_|_|\___\___/ </tspan>
          <tspan x="330" y="30.0">             |_|                                                               </tspan>
        </text>
        <text x="635" y="19" fill="#0f172a" font-size="16.5" font-weight="900" font-family="'Inter', sans-serif">• ARQUITECTURA DE CÓDIGO ABIERTO</text>
        <rect x="1330" y="-2" width="490" height="26" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1" />
        <text x="1575" y="15" fill="#475569" font-size="10.5" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">ARQUITECTURA DE CÓDIGO ABIERTO • FORMATO ULTRA-HD</text>
      </g>
      <line x1="35" y1="64" x2="1825" y2="64" stroke="#e2e8f0" stroke-width="1.5" />

      <!-- ================= COLUMNA 1: AUTORÍA Y PROYECTO ================= -->
      <g transform="translate(35, 82)">
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" letter-spacing="1.2">AUTOR &amp; DESARROLLO:</text>
        <text x="0" y="48" fill="#0f172a" font-size="24" font-weight="900" font-family="'Inter', sans-serif">Adolfo Morales Tena</text>
        <text x="0" y="72" fill="#0284c7" font-size="13" font-weight="700" font-family="'Inter', sans-serif">Estudiante de Bioquímica y Biología Molecular</text>
        
        <rect x="0" y="94" width="465" height="42" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.2" />
        <text x="16" y="112" fill="#334155" font-size="10" font-weight="700" font-family="'Inter', sans-serif">PROYECTO UNIVERSITARIO DE BIOQUÍMICA MÉDICA</text>
        <text x="16" y="126" fill="#64748b" font-size="9.5" font-family="'Inter', sans-serif">Mapas Metabólicos Integrados • Redes Bioquímicas de Alta Fidelidad</text>

        <!-- Botón interactivo de GitHub -->
        <g transform="translate(0, 155)">
          <a href="https://github.com/AMorales22T/mapa_metabolico" target="_blank">
            <rect x="0" y="0" width="465" height="52" rx="10" fill="#0f172a" stroke="#1e293b" stroke-width="1.5" style="cursor: pointer;" />
            <g transform="translate(16, 14)">
              <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" fill="#ffffff" />
            </g>
            <text x="52" y="22" fill="#94a3b8" font-size="10" font-weight="800" font-family="'Inter', sans-serif">REPOSITORIO ABIERTO EN GITHUB:</text>
            <text x="52" y="40" fill="#38bdf8" font-size="13" font-weight="700" font-family="'JetBrains Mono', monospace">https://github.com/AMorales22T/mapa_metabolico</text>
          </a>
        </g>

        <!-- Bloque de licencia MIT -->
        <g transform="translate(0, 226)">
          <rect x="0" y="0" width="465" height="42" rx="8" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1" />
          <rect x="12" y="10" width="95" height="22" rx="5" fill="#e2e8f0" />
          <text x="59.5" y="25" fill="#334155" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MIT LICENSE</text>
          <text x="120" y="26" fill="#475569" font-size="10" font-weight="700" font-family="'Inter', sans-serif">Libre distribución, estudio y docencia biomédica</text>
        </g>
        
        <text x="0" y="302" fill="#64748b" font-size="10" font-weight="600" font-family="'Inter', sans-serif">Contribuciones, issues y sugerencias bienvenidas en GitHub.</text>
        <text x="0" y="320" fill="#94a3b8" font-size="9" font-family="'Inter', sans-serif">Diseñado y validado según estándares docentes internacionales.</text>
      </g>

      <!-- Divisor vertical 1 -->
      <line x1="535" y1="80" x2="535" y2="480" stroke="#e2e8f0" stroke-width="1.5" />

      <!-- ================= COLUMNA 2: FUENTES CIENTÍFICAS Y HERRAMIENTAS ================= -->
      <g transform="translate(565, 82)">
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" letter-spacing="1.2">FUENTES CIENTÍFICAS &amp; BIBLIOGRAFÍA DE REFERENCIA:</text>
        
        <g transform="translate(0, 32)">
          <text x="0" y="0" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">Lehninger: Principios de Bioquímica</tspan> (D. L. Nelson, M. M. Cox — 7.ª y 8.ª Ed., W. H. Freeman)</text>
          <text x="0" y="21" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">Harper: Bioquímica Ilustrada</tspan> (V. Rodwell, D. Bender, K. Botham, P. Kennelly, A. Weil — 31.ª y 32.ª Ed.)</text>
          <text x="0" y="42" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">Bioquímica con Aplicaciones Clínicas</tspan> (Thomas M. Devlin — 4.ª y 5.ª Ed., Ed. Reverté)</text>
          <text x="0" y="63" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">Bioquímica</tspan> (J. M. Berg, J. L. Tymoczko, G. J. Gatto Jr., L. Stryer — 8.ª y 9.ª Ed., Ed. Reverté / W.H. Freeman)</text>
          <text x="0" y="84" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">Biochemical Pathways: An Atlas of Biochemistry and Molecular Biology</tspan> (G. Michal &amp; D. Schomburg / Roche)</text>
          <text x="0" y="105" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="900" fill="#0f172a">KEGG Pathway Database</tspan> &amp; Nomenclatura Enzimática Internacional (Comisión de Enzimas NC-IUBMB / IUPAC)</text>
        </g>

        <!-- Divisor interno horizontal -->
        <line x1="0" y1="165" x2="875" y2="165" stroke="#f1f5f9" stroke-width="1.5" />

        <text x="0" y="190" fill="#64748b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" letter-spacing="1.2">HERRAMIENTAS DE INGENIERÍA &amp; ARQUITECTURA TECNOLÓGICA:</text>
        <g transform="translate(0, 206)">
          <text x="0" y="0" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">Python 3:</tspan> Motor de generación algorítmica, geometría analítica de curvas Bézier y cálculo estequiométrico.</text>
          <text x="0" y="21" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">Algoritmo A* de Enrutamiento:</tspan> Conexión libre de colisiones entre metabolitos de vías cruzadas.</text>
          <text x="0" y="42" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">SVG 1.1 W3C:</tspan> Renderizado vectorial puro escalable sin pérdida de calidad (85+ metabolitos con fórmula química).</text>
          <text x="0" y="63" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">Stack Web (HTML5 / CSS3 / ES6):</tspan> Visores interactivos con zoom/pan (CTM), buscador reactivo y aislamiento de rutas.</text>
          <text x="0" y="84" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">librsvg (rsvg-convert) &amp; libqrencode:</tspan> Exportación a PDF Ultra-HD (1200×900 mm a 300 DPI) y QR vectorial.</text>
          <text x="0" y="105" fill="#334155" font-size="11" font-weight="600" font-family="'Inter', sans-serif">• <tspan font-weight="800" fill="#0f172a">Git &amp; GitHub Actions:</tspan> Control de versiones, integración continua e interoperabilidad abierta.</text>
        </g>
      </g>

      <!-- Divisor vertical 2 -->
      <line x1="1470" y1="80" x2="1470" y2="480" stroke="#e2e8f0" stroke-width="1.5" />

      <!-- ================= COLUMNA 3: CÓDIGO QR Y ESCANEO DIRECTO ================= -->
      <g transform="translate(1495, 82)">
        <text x="165" y="16" fill="#64748b" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" letter-spacing="1.2" text-anchor="middle">ACCESO MÓVIL DIRECTO:</text>

        <!-- Contenedor QR estilizado -->
        <g transform="translate(20, 32)">
          <rect x="0" y="0" width="290" height="290" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.5" />
          <!-- Marco interior blanco -->
          <rect x="14" y="14" width="262" height="262" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
          <!-- QR escalado a 8.0x (29 módulos * 8.0 = 232 px, centrado en 262 con margen 15 px) -->
          <g transform="translate(29, 29) scale(8.0)">
            <path d="{qr_path}" fill="#0f172a" />
          </g>
        </g>

        <!-- Textos bajo el QR -->
        <text x="165" y="348" fill="#0f172a" font-size="13" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">ESCANEAR CON SMARTPHONE</text>
        <text x="165" y="368" fill="#0284c7" font-size="11" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">github.com/AMorales22T/mapa_metabolico</text>
        <text x="165" y="388" fill="#64748b" font-size="9.5" font-weight="600" font-family="'Inter', sans-serif" text-anchor="middle">Acceso instantáneo a código fuente, SVG,</text>
        <text x="165" y="402" fill="#64748b" font-size="9.5" font-weight="600" font-family="'Inter', sans-serif" text-anchor="middle">visores interactivos y versiones imprimibles PDF</text>
      </g>
    </g>
    '''

