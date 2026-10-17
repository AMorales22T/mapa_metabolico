# =============================================================================
# REESTRUCTURACIÓN DE LA LEYENDA INSTITUCIONAL CENTRAL
# =============================================================================

def actualizar_bloque_leyenda_central(inner_svg):
    """
    Reestructura y amplía el bloque de leyenda institucional (3650 × 505 px) para aprovechar
    todo el espacio vertical y horizontal en sus 4 secciones:
    1. Vías Metabólicas (1–25) en 3 columnas amplias con badges r=13.5 y tipografía de 13.5/10.8 px.
    2. Convenciones y Efectores con cápsulas grandes (58×30 px), título de 13 px y subtítulo explicativo.
    3. Código de Colores con muestras cuadradas (26×26 px), título de 13 px y desglose funcional.
    4. Nomenclatura Enzimática (EC) ampliada a cuerpo 12–13.5 px ocupando toda la altura de la tarjeta.
    """
    vias_todas_col1 = [
        {"n": 1, "nombre": "Glucólisis", "resumen": "Glucosa → 2 Piruvato (+2 ATP, +2 NADH citosólico)", "color": "#0284c7"},
        {"n": 2, "nombre": "Gluconeogénesis", "resumen": "Piruvato / Lactato / Ala → Glucosa (4 rodeos irreversibles)", "color": "#7c3aed"},
        {"n": 3, "nombre": "Glucógeno (Síntesis y lisis)", "resumen": "Glucogenogénesis (GS) y Glucogenólisis (GP) citosólica", "color": "#b45309"},
        {"n": 4, "nombre": "Vía de las pentosas fosfato", "resumen": "G6P → 2 NADPH + Ribosa-5-P (Fase oxidativa y no oxidativa)", "color": "#059669"},
        {"n": 5, "nombre": "Complejo PDH (Piruvato DH)", "resumen": "Piruvato → Acetil-CoA + CO₂ + NADH (5 cofactores: TPP, Lip, CoA, FAD, NAD⁺)", "color": "#ea580c"},
        {"n": 6, "nombre": "Ciclo de Krebs (TCA)", "resumen": "Acetil-CoA → 2 CO₂ + 3 NADH + FADH₂ + GTP (Matriz mitocondrial)", "color": "#c2410c"},
        {"n": 7, "nombre": "Cadena Respiratoria & ATP Sintasa", "resumen": "Complejos I–IV y Fosforilación oxidativa por fuerza protón-motriz", "color": "#16a34a"},
        {"n": 8, "nombre": "Lanzaderas (Malato-Asp / G3P)", "resumen": "Transferencia de equivalentes reductores (NADH citosólico → MMI)", "color": "#0284c7"},
    ]

    vias_todas_col2 = [
        {"n": 9, "nombre": "β-oxidación (y lanzadera carnitina)", "resumen": "Palmitoil-CoA (16C) → 8 Acetil-CoA + 7 FADH₂ + 7 NADH", "color": "#b45309"},
        {"n": 10, "nombre": "Lipogénesis de novo (ACC / FAS)", "resumen": "Acetil-CoA → Malonil-CoA → Palmitato (consumo de 14 NADPH)", "color": "#0d9488"},
        {"n": 11, "nombre": "Cetogénesis hepática", "resumen": "Acetil-CoA → HMG-CoA → Acetoacetato, D-β-Hidroxibutirato y Acetona", "color": "#be123c"},
        {"n": 12, "nombre": "Síntesis de colesterol", "resumen": "Acetil-CoA → HMG-CoA → Mevalonato (HMGCR) → Escualeno → Colesterol", "color": "#4f46e5"},
        {"n": "12B", "nombre": "Destinos de esqueletos carbonados", "resumen": "Convergencia de los 20 aminoácidos (glucogénicos y cetogénicos)", "color": "#2563eb"},
        {"n": 13, "nombre": "Transaminación y desaminación", "resumen": "Aminotransferasas (ALT/AST con PLP) y Glutamato DH → NH₄⁺", "color": "#2563eb"},
        {"n": 14, "nombre": "Ciclo de la urea (Ornitina)", "resumen": "NH₄⁺ + HCO₃⁻ + Aspartato → Urea excretable (CPS-I a Arginasa)", "color": "#0891b2"},
        {"n": 15, "nombre": "Biosíntesis de nucleótidos", "resumen": "Síntesis de novo y salvamento de Purinas (IMP/AMP/GMP) y Pirimidinas", "color": "#0284c7"},
        {"n": 16, "nombre": "Catabolismo de nucleótidos", "resumen": "Purinas → Hipoxantina → Xantina → Ácido Úrico; Pirimidinas → β-Ala", "color": "#475569"},
    ]

    vias_todas_col3 = [
        {"n": 17, "nombre": "Ciclo de Cori (Músculo ⇄ Hígado)", "resumen": "Lactato muscular anaeróbico reciclado a Glucosa hepática", "color": "#9f1239"},
        {"n": 18, "nombre": "Digestión y absorción de lípidos", "resumen": "Sales biliares → Micela mixta → Enterocito (REL) → Quilomicrón", "color": "#0d9488"},
        {"n": 19, "nombre": "Tejido adiposo (lipólisis secuencial)", "resumen": "TAG → ATGL → DAG → HSL → 2-MAG → MGL → 3 AG libres + Glicerol", "color": "#ea580c"},
        {"n": 20, "nombre": "Músculo esquelético y sarcómero", "resumen": "Contracción actina-miosina dependiente de ATP/Ca²⁺; Cori y Cahill", "color": "#9f1239"},
        {"n": 21, "nombre": "Cerebro y combustibles neuronales", "resumen": "Barrera hematoencefálica: Glucosa (GLUT1/3) y cuerpos cetónicos (MCT)", "color": "#2563eb"},
        {"n": 22, "nombre": "Lipoproteínas plasmáticas", "resumen": "Transporte endógeno VLDL → IDL → LDL (ApoB-100) y reverso HDL", "color": "#2563eb"},
        {"n": 23, "nombre": "Biosíntesis de TAG y fosfolípidos", "resumen": "Vía de Kennedy: G3P → LPA → Ácido Fosfatídico → DAG → TAG / PC", "color": "#7c3aed"},
        {"n": 24, "nombre": "Biosíntesis de AA no esenciales", "resumen": "Síntesis de Ala, Ser, Gly, Cys, Asp, Asn, Glu, Gln, Pro y Tyr", "color": "#059669"},
        {"n": 25, "nombre": "Integración y conmutador hormonal", "resumen": "Coordinación intertisular: Estado Posprandial (Insulina) vs Ayuno", "color": "#ea580c"},
    ]

    def render_col_vias(items, x_offset, titulo):
        svg_items = []
        for i, v in enumerate(items):
            y_pos = i * 42
            nom = v['nombre'].replace('&', '&amp;')
            res = v['resumen'].replace('&', '&amp;')
            fs_num = "9.5" if len(str(v['n'])) > 2 else "11"
            svg_items.append(f'''
            <g id="badge_leyenda_{v['n']}" class="badge-via" data-via="{v['n']}" transform="translate(0, {y_pos})" style="cursor: pointer;">
              <circle cx="14" cy="4" r="13.5" fill="{v['color']}"/>
              <text x="14" y="8" fill="#ffffff" font-size="{fs_num}" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{v['n']}</text>
              <text x="35" y="1" fill="#0f172a" font-size="13.5" font-weight="800" font-family="'Inter', sans-serif">{nom}</text>
              <text x="35" y="17" fill="#475569" font-size="10.2" font-weight="600" font-family="'Inter', sans-serif">{res}</text>
            </g>''')
        return f'''
        <g transform="translate({x_offset}, 118)">
          <text x="0" y="-16" fill="#0284c7" font-size="14" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="0.8">{titulo}</text>
          {''.join(svg_items)}
        </g>'''

    col1_svg = render_col_vias(vias_todas_col1, 35, "VÍAS METABÓLICAS (1–8):")
    col2_svg = render_col_vias(vias_todas_col2, 600, "VÍAS METABÓLICAS (9–16):")
    col3_svg = render_col_vias(vias_todas_col3, 1175, "VÍAS DE INTEGRACIÓN Y ÓRGANOS (17–25):")

    convenciones_data = [
        ("(+)", "#dcfce7", "#16a34a", "#15803d", "Activador alostérico (+)", "Efector positivo que incrementa la afinidad o Vmáx enzimática"),
        ("(-)", "#fee2e2", "#dc2626", "#b91c1c", "Inhibidor alostérico (-)", "Efector negativo o retroinhibición por producto final"),
        ("(P)", "#fef3c7", "#d97706", "#b45309", "Modificación covalente (P)", "Regulación hormonal por fosforilación / desfosforilación"),
        ("⇄", "#f1f5f9", "#64748b", "#0f172a", "Reacción reversible (⇄)", "Etapa cercana al equilibrio termodinámico (ΔG ≈ 0)"),
        ("→", "#ffedd5", "#ea580c", "#c2410c", "Reacción irreversible (→)", "Paso limitante exergónico (ΔG ≪ 0 · punto de control)"),
        ("- - →", "#e0f2fe", "#0284c7", "#0369a1", "Conexión inter-vía (- - →)", "Flujo de metabolitos entre compartimentos o rutas"),
        ("▭", "#ede9fe", "#7c3aed", "#6d28d9", "Transportador de membrana", "Proteínas integrales: GLUT, MPC, CACT, AGC, OGC, MCT"),
        ("[nC]", "#ffedd5", "#ea580c", "#ea580c", "Conteo de carbonos [nC]", "Número de átomos de carbono del esqueleto metabólico"),
    ]
    simbolos_svg = []
    for i, (sim, bg, stroke, fg, tit, sub) in enumerate(convenciones_data):
        y_s = i * 46
        simbolos_svg.append(f'''
        <g transform="translate(0, {y_s})">
          <rect x="0" y="-12" width="56" height="30" rx="7" fill="{bg}" stroke="{stroke}" stroke-width="1.5"/>
          <text x="28" y="8" fill="{fg}" font-size="13" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{sim}</text>
          <text x="68" y="1" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif">{tit}</text>
          <text x="68" y="17" fill="#475569" font-size="10.2" font-weight="600" font-family="'Inter', sans-serif">{sub}</text>
        </g>''')

    colores_data = [
        ("#ea580c", "#ffedd5", "Flujo principal de carbono", "Ejes catabólicos centrales (Glucólisis, PDH, Krebs)"),
        ("#7c3aed", "#ede9fe", "Gluconeogénesis y Fosfolípidos", "Rodeos anabólicos irreversibles y vía de Kennedy"),
        ("#b45309", "#fef3c7", "Glucógeno y β-Oxidación", "Movilización de reservas energéticas y acil-CoA"),
        ("#059669", "#d1fae5", "Pentosas Fosfato y Biosíntesis AA", "Generación de poder reductor (NADPH) y anabolismo"),
        ("#2563eb", "#dbeafe", "Metabolismo Nitrogenado y SNC", "Transaminación, Ciclo de la Urea y lipoproteínas"),
        ("#16a34a", "#dcfce7", "(+) Activación / Síntesis de ATP", "Estimulación alostérica y fosforilación oxidativa"),
        ("#dc2626", "#fee2e2", "(-) Inhibición / Consumo de ATP", "Freno alostérico, patologías y gasto energético"),
        ("#ca8a04", "#fef9c3", "(P) Control Hormonal Covalente", "Señalización Insulina (desfosforila) vs Glucagón (PKA)"),
    ]
    colores_svg = []
    for i, (col, bg, tit, sub) in enumerate(colores_data):
        y_c = i * 46
        colores_svg.append(f'''
        <g transform="translate(0, {y_c})">
          <rect x="0" y="-10" width="26" height="26" rx="7" fill="{bg}" stroke="{col}" stroke-width="2"/>
          <circle cx="13" cy="3" r="6.5" fill="{col}"/>
          <text x="38" y="1" fill="#0f172a" font-size="12.8" font-weight="800" font-family="'Inter', sans-serif">{tit}</text>
          <text x="38" y="17" fill="#475569" font-size="10.2" font-weight="600" font-family="'Inter', sans-serif">{sub}</text>
        </g>''')

    nuevo_bloque_leyenda = f'''<g id="bloque_leyenda" data-arrastrable="1" transform="translate(100, 4220)" filter="url(#shadowCard)">
      <!-- Fondo ampliado a 505 px de alto para alinear con el bloque de autoría -->
      <rect width="3650" height="505" rx="22" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" />
      <path d="M 0 22 Q 0 0 22 0 L 3628 0 Q 3650 0 3650 22 L 3650 10 L 0 10 Z" fill="url(#gradHeaderAutoria)" />

      <!-- Encabezado -->
      <g transform="translate(35, 26)">
        <rect x="0" y="0" width="250" height="30" rx="7" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.4" />
        <text x="125" y="20" fill="#0369a1" font-size="12.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="1">GUÍA Y CONVENCIONES</text>
        <text x="270" y="22" fill="#0f172a" font-size="21" font-weight="900" font-family="'Inter', sans-serif">LEYENDA DE VÍAS METABÓLICAS &amp; CONTROL ALOSTÉRICO / COVALENTE</text>
        <rect x="1480" y="-1" width="900" height="32" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.3"/>
        <text x="1496" y="20" fill="#92400e" font-size="12.5" font-weight="800" font-family="'Inter', sans-serif">[Nota] Célula didáctica integrada: Gluconeogénesis, Cetogénesis y Ciclo de la Urea son primordialmente hepáticos</text>
      </g>
      <line x1="35" y1="72" x2="3615" y2="72" stroke="#e2e8f0" stroke-width="1.8" />

      <!-- Columnas 1, 2 y 3: Las 25 Vías Metabólicas -->
      {col1_svg}
      {col2_svg}
      {col3_svg}

      <line x1="1765" y1="88" x2="1765" y2="485" stroke="#e2e8f0" stroke-width="2" />

      <!-- Columna 4: Convenciones y Efectores -->
      <g transform="translate(1790, 118)">
        <text x="0" y="-16" fill="#0f766e" font-size="14" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="0.8">CONVENCIONES Y EFECTORES:</text>
        {''.join(simbolos_svg)}
      </g>

      <line x1="2485" y1="88" x2="2485" y2="485" stroke="#e2e8f0" stroke-width="2" />

      <!-- Columna 5: Código de Colores -->
      <g transform="translate(2510, 118)">
        <text x="0" y="-16" fill="#b45309" font-size="14" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="0.8">CÓDIGO DE COLORES:</text>
        {''.join(colores_svg)}
      </g>

      <line x1="3020" y1="88" x2="3020" y2="485" stroke="#e2e8f0" stroke-width="2" />

      <!-- Columna 6: Nomenclatura Enzimática (EC) -->
      <g id="leyenda_col_ec" transform="translate(3045, 118)">
        <text x="0" y="-16" fill="#7c3aed" font-size="14" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="0.8">NOMENCLATURA ENZIMÁTICA (EC):</text>

        <!-- Header badge y título -->
        <g transform="translate(0, 4)">
          <rect x="0" y="-12" width="106" height="28" rx="6" fill="#f5f3ff" stroke="#c4b5fd" stroke-width="1.5"/>
          <text x="53" y="7" fill="#6d28d9" font-size="13" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC x.x.x.x</text>
          <text x="118" y="7" fill="#0f172a" font-size="13.5" font-weight="800" font-family="'Inter', sans-serif">Comisión de Enzimas (Enzyme Commission)</text>
        </g>

        <!-- Intro -->
        <text x="0" y="42" fill="#475569" font-size="11.5" font-weight="600" font-family="'Inter', sans-serif">Código internacional de 4 cifras que clasifica cada enzima según la reacción química catalizada:</text>

        <!-- 1.ª Cifra -->
        <text x="0" y="72" fill="#1e293b" font-size="12.5" font-weight="800" font-family="'Inter', sans-serif"><tspan fill="#7c3aed" font-weight="900">1.ª cifra</tspan> · Clase principal de reacción (clases 1 a 7):</text>

        <!-- 7 Clases en 2 columnas -->
        <g transform="translate(0, 96)">
          <g transform="translate(0, 0)">
            <rect x="0" y="-12" width="23" height="23" rx="5" fill="#ede9fe" stroke="#a78bfa" stroke-width="1.3"/>
            <text x="11.5" y="4.5" fill="#6d28d9" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">1</text>
            <text x="32" y="4.5" fill="#334155" font-size="11.5" font-family="'Inter', sans-serif"><tspan font-weight="800" fill="#0f172a">Oxidorreductasas</tspan> (redox / e⁻)</text>
          </g>
          <g transform="translate(0, 32)">
            <rect x="0" y="-12" width="23" height="23" rx="5" fill="#ede9fe" stroke="#a78bfa" stroke-width="1.3"/>
            <text x="11.5" y="4.5" fill="#6d28d9" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">2</text>
            <text x="32" y="4.5" fill="#334155" font-size="11.5" font-family="'Inter', sans-serif"><tspan font-weight="800" fill="#0f172a">Transferasas</tspan> (transfieren grupos)</text>
          </g>
          <g transform="translate(0, 64)">
            <rect x="0" y="-12" width="23" height="23" rx="5" fill="#ede9fe" stroke="#a78bfa" stroke-width="1.3"/>
            <text x="11.5" y="4.5" fill="#6d28d9" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">3</text>
            <text x="32" y="4.5" fill="#334155" font-size="11.5" font-family="'Inter', sans-serif"><tspan font-weight="800" fill="#0f172a">Hidrolasas</tspan> (ruptura con H₂O)</text>
          </g>
          <g transform="translate(0, 96)">
            <rect x="0" y="-12" width="23" height="23" rx="5" fill="#ede9fe" stroke="#a78bfa" stroke-width="1.3"/>
            <text x="11.5" y="4.5" fill="#6d28d9" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">4</text>
            <text x="32" y="4.5" fill="#334155" font-size="11.5" font-family="'Inter', sans-serif"><tspan font-weight="800" fill="#0f172a">Liasas</tspan> (adición/ruptura sin H₂O)</text>
          </g>
        </g>

        <g transform="translate(290, 96)">
          <g transform="translate(0, 0)">
            <rect x="0" y="-12" width="23" height="23" rx="5" fill="#ede9fe" stroke="#a78bfa" stroke-width="1.3"/>
            <text x="11.5" y="4.5" fill="#6d28d9" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">5</text>
            <text x="32" y="4.5" fill="#334155" font-size="11.5" font-family="'Inter', sans-serif"><tspan font-weight="800" fill="#0f172a">Isomerasas</tspan> (reordenamiento)</text>
          </g>
          <g transform="translate(0, 32)">
            <rect x="0" y="-12" width="23" height="23" rx="5" fill="#ede9fe" stroke="#a78bfa" stroke-width="1.3"/>
            <text x="11.5" y="4.5" fill="#6d28d9" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">6</text>
            <text x="32" y="4.5" fill="#334155" font-size="11.5" font-family="'Inter', sans-serif"><tspan font-weight="800" fill="#0f172a">Ligasas</tspan> (unión con gasto de ATP)</text>
          </g>
          <g transform="translate(0, 64)">
            <rect x="0" y="-12" width="23" height="23" rx="5" fill="#ede9fe" stroke="#a78bfa" stroke-width="1.3"/>
            <text x="11.5" y="4.5" fill="#6d28d9" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">7</text>
            <text x="32" y="4.5" fill="#334155" font-size="11.5" font-family="'Inter', sans-serif"><tspan font-weight="800" fill="#0f172a">Translocasas</tspan> (bombas/transporte)</text>
          </g>
        </g>

        <!-- 2.ª y 3.ª Cifras -->
        <g transform="translate(0, 232)">
          <rect x="0" y="-12" width="68" height="24" rx="5" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.3"/>
          <text x="34" y="4.5" fill="#0f172a" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">2.ª y 3.ª</text>
          <text x="80" y="4.5" fill="#334155" font-size="11.5" font-family="'Inter', sans-serif"><tspan font-weight="800" fill="#0f172a">Subclase y sub-subclase:</tspan> enlace químico, grupo donador y aceptor.</text>
        </g>

        <!-- 4.ª Cifra -->
        <g transform="translate(0, 268)">
          <rect x="0" y="-12" width="68" height="24" rx="5" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1.3"/>
          <text x="34" y="4.5" fill="#0f172a" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">4.ª cifra</text>
          <text x="80" y="4.5" fill="#334155" font-size="11.5" font-family="'Inter', sans-serif"><tspan font-weight="800" fill="#0f172a">Número serie:</tspan> identificador específico de la enzima y su sustrato.</text>
        </g>

        <!-- Tarjeta de ejemplo ampliada -->
        <g transform="translate(0, 298)">
          <rect x="0" y="0" width="575" height="62" rx="9" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
          <text x="16" y="24" fill="#7c3aed" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace">Ejemplo:</text>
          <text x="88" y="24" fill="#0f172a" font-size="12.5" font-weight="900" font-family="'JetBrains Mono', monospace">EC 2.7.1.1 · Hexoquinasa / Glucoquinasa</text>
          <text x="16" y="46" fill="#475569" font-size="10.5" font-weight="700" font-family="'Inter', sans-serif">2: Transferasa ➔ 7: Fosfotransferasa ➔ 1: Aceptor grupo hidroxilo (-OH) ➔ 1: D-hexosa-6-fosfotransferasa</text>
        </g>
      </g>
    </g>'''

    patron_bloque = r'<g id="bloque_leyenda"[\s\S]*?(?=\s*<!-- BLOQUE INSTITUCIONAL Y AUTORÍA)'
    if re.search(patron_bloque, inner_svg):
        inner_svg = re.sub(patron_bloque, nuevo_bloque_leyenda + "\n", inner_svg, count=1)

    return inner_svg


