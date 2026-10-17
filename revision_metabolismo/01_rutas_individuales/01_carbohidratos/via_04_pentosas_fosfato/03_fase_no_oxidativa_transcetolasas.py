# =============================================================================
# MÓDULO DE REVISIÓN: Fase No Oxidativa (Transcetolasa y Transaldolasa)
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/via_04_pentosas_fosfato/generar_pentosas.py (líneas 431 a 802 de 802)
# Descripción      : Interconversión de azúcares de 3C, 4C, 5C, 6C y 7C y reciclaje a glucólisis.
# =============================================================================

    s.append(f'<g transform="translate({X0},{y+38})">'); s.append(_card(0, 0, WP, h - 38, "#cbd5e1"))
    s.append(_t(20, 26, "ALTA", 10.5, 900, "#047857"))
    altos = ["hígado", "tejido adiposo", "mama lactante", "corteza suprarrenal", "gónadas", "eritrocito", "cristalino / córnea", "médula ósea · tumores"]
    x, yy = 78, 22
    for a in altos:
        w = len(a) * 6.3 + 22
        if x + w > WP - 14:
            x, yy = 78, yy + 26
        s.append(_pill(x + w / 2, yy, a, "#047857", "#d1fae5", w, 18, 10)); x += w + 8
    s.append(_t(20, 100, "BAJA", 10.5, 900, "#64748b"))
    s.append(_pill(78 + 76, 96, "músculo esquelético", "#64748b", "#f1f5f9", 152, 18, 10))
    s.append(_t(250, 100, "poca síntesis reductora", 9.5, 700, "#94a3b8"))
    s.append('</g>')
    return "\n".join(s), y + h + 14

# ---- E. Clínica ------------------------------------------------------------
def _cadena(y0, items, col, bg):
    n = len(items); w = (WP - 40 - 16 * (n - 1)) / n; out = []
    for i, it in enumerate(items):
        x = 20 + i * (w + 16)
        ultimo = i == n - 1
        out.append(f'<rect x="{x:.1f}" y="{y0}" width="{w:.1f}" height="36" rx="9" fill="{"#fee2e2" if ultimo else bg}" stroke="{"#dc2626" if ultimo else col}" stroke-width="1.8"/>')
        a, b = (it if isinstance(it, tuple) else (it, ""))
        if b:
            out.append(_t(x + w / 2, y0 + 15, a, 10, 900, "#dc2626" if ultimo else col, "middle")); out.append(_t(x + w / 2, y0 + 28, b, 9, 700, "#475569", "middle"))
        else:
            out.append(_t(x + w / 2, y0 + 22, a, 10, 900, "#dc2626" if ultimo else col, "middle"))
        if not ultimo:
            out.append(_line(x + w + 1, y0 + 18, x + w + 15, y0 + 18, "#475569", "mSl", 2))
    return "\n".join(out)

def panel_clinica(y):
    h = 290
    s = [_seccion(y, "CLÍNICA: CUANDO FALLA LA VÍA", "")]
    s.append(f'<g transform="translate({X0},{y+38})">'); s.append(_card(0, 0, WP, h - 38, "#fca5a5"))
    s.append(_t(20, 26, "DÉFICIT DE G6PDH", 11, 900, "#b91c1c")); s.append(_t(160, 26, "el eritrocito depende de la vía para su NADPH", 9.5, 700, "#64748b"))
    s.append(_cadena(38, [("G6PDH", "✕ déficit"), ("NADPH", "↓"), ("GSH", "↓ (antioxidante)"), ("H₂O₂", "↑ oxida la Hb"), ("HEMÓLISIS", "")], "#b91c1c", "#fff1f2"))
    s.append(_t(20, 96, "Desencadenantes:", 9.5, 900, "#475569")); s.append(_pill(236, 92, "habas (favismo)", "#b91c1c", "#fee2e2", 104, 16, 9)); s.append(_pill(334, 92, "primaquina", "#b91c1c", "#fee2e2", 80, 16, 9)); s.append(_pill(424, 92, "sulfamidas", "#b91c1c", "#fee2e2", 80, 16, 9)); s.append(_pill(514, 92, "infecciones", "#b91c1c", "#fee2e2", 82, 16, 9))
    s.append(_t(20, 118, "Signo típico: cuerpos de Heinz y anemia hemolítica", 9.5, 700, "#64748b"))
    s.append('<line x1="20" y1="132" x2="620" y2="132" stroke="#e2e8f0" stroke-width="1.5"/>')
    s.append(_t(20, 154, "DÉFICIT DE TIAMINA (VIT. B1)", 11, 900, "#b45309")); s.append(_t(222, 154, "el cofactor de la transcetolasa es el TPP", 9.5, 700, "#64748b"))
    s.append(_cadena(166, [("Tiamina", "↓ (alcohol, desnutrición)"), ("Transcetolasa", "↓ TPP"), ("Vía no oxidativa", "↓"), ("WERNICKE-KORSAKOFF", "")], "#b45309", "#fffbeb"))
    s.append(_t(20, 224, "Se evalúa midiendo la actividad de transcetolasa en eritrocitos", 9.5, 700, "#64748b"))
    s.append('</g>')
    return "\n".join(s), y + h + 14

# ---- F. Resumen rápido -----------------------------------------------------
def panel_resumen(y):
    h = 190
    s = [_seccion(y, "RESUMEN PARA RECORDAR", "")]
    s.append(f'<g transform="translate({X0},{y+38})">'); s.append(_card(0, 0, WP, h - 38, "#cbd5e1"))
    s.append('<rect x="20" y="16" width="285" height="62" rx="12" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>')
    s.append(_t(162, 36, "FASE OXIDATIVA", 11, 900, "#c2410c", "middle")); s.append(_t(162, 52, "irreversible · produce NADPH + CO₂", 10, 700, "#9a3412", "middle")); s.append(_t(162, 67, "paso clave: G6PDH", 10, 700, "#9a3412", "middle"))
    s.append('<rect x="335" y="16" width="285" height="62" rx="12" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>')
    s.append(_t(477, 36, "FASE NO OXIDATIVA", 11, 900, "#6d28d9", "middle")); s.append(_t(477, 52, "reversible · reordena azúcares (5C ⇄ 3C-6C)", 10, 700, "#5b21b6", "middle")); s.append(_t(477, 67, "transcetolasa (TPP) · transaldolasa", 10, 700, "#5b21b6", "middle"))
    s.append(_pill(162, 102, "G6P + 2 NADP⁺ → Ru5P + CO₂ + 2 NADPH", "#c2410c", "#ffffff", 280, 20, 10))
    s.append(_pill(477, 102, "3 Ru5P ⇄ 2 F6P + 1 GAP", "#6d28d9", "#ffffff", 280, 20, 10))
    s.append(_t(320, 138, "Todo ocurre en el citosol · no se produce ni se consume ATP directamente", 10, 700, "#64748b", "middle"))
    s.append('</g>')
    return "\n".join(s), y + h + 14

def generar_fases_y_balance():
    """Barras de fase en el margen izquierdo + balance de la fase oxidativa junto a la Ru5P."""
    def barra(y1, y2, col, bg, txt):
        ym = (y1 + y2) / 2
        return (f'<rect x="8" y="{y1}" width="22" height="{y2-y1}" rx="11" fill="{bg}" stroke="{col}" stroke-width="1.6"/>'
                f'<text transform="translate(24,{ym}) rotate(-90)" font-size="11" font-weight="900" fill="{col}" text-anchor="middle" letter-spacing="1.5">{txt}</text>')
    return f"""
    <!-- Barras de fase -->
    <g {FF}>
      {barra(88, 880, "#c2410c", "#ffedd5", "FASE OXIDATIVA · IRREVERSIBLE · PRODUCE NADPH")}
      {barra(900, 1980, "#6d28d9", "#f5f3ff", "FASE NO OXIDATIVA · REVERSIBLE · REORDENA AZÚCARES")}
      <!-- Etiqueta de compartimento -->
      <rect x="800" y="30" width="160" height="22" rx="11" fill="#d1fae5" stroke="#059669" stroke-width="1.6"/>
      <text x="880" y="45" font-size="10.5" font-weight="900" fill="#047857" text-anchor="middle">TODO EN EL CITOSOL</text>
    </g>
    """

def generar_panel_derecho(alto):
    partes = [f'<rect x="1000" y="0" width="700" height="{alto}" fill="#f1f5f9"/>',
              '<line x1="1000" y1="0" x2="1000" y2="' + str(alto) + '" stroke="#cbd5e1" stroke-width="2"/>',
              f'<g {FF}>',
              _t(X0, 52, "CONTEXTO: ¿PARA QUÉ Y CUÁNDO?", 22, 900, "#0f172a", extra='letter-spacing="1"'),
              _t(X0, 74, "La misma vía sirve a necesidades distintas según el tejido y el momento", 11.5, 700, "#64748b")]
    y = 96
    for f in (panel_modos, panel_interruptor, panel_hub, panel_tejidos, panel_clinica, panel_resumen):
        svg, y = f(y); partes.append(svg)
    partes.append('</g>')
    return "\n".join(partes), y


# -----------------------------------------------------------------------------
# 4. CONSTRUCCIÓN Y GENERACIÓN DEL ARCHIVO
# -----------------------------------------------------------------------------
def main():
    contenido_svg = []

    # =========================================================================
    # CAPA DE FONDO: CITOSOL BIOLÓGICO CELULAR
    # =========================================================================
    contenido_svg.append(generar_citosol_pentosas_svg(ancho=1000, alto=2150))

    # =========================================================================
    # FASE 1: FASE OXIDATIVA
    # =========================================================================

    # 1. Glucosa-6-Fosfato (Despejada de la flecha de entrada)
    contenido_svg.append(crear_metabolito(
        x=340, y=90,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa)",
        detalle="Entrada al Shunt de Pentosas",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # Reacción 1: G6PDH
    contenido_svg.append(crear_reaccion_oxidativa(
        x=385, y=200,
        enzima="Glucosa-6-P Deshidrogenasa (G6PDH)",
        ec="EC 1.1.1.49 (Paso Limitante Clave)",
        regulacion="⊣ NADPH | ⊕ NADP⁺, Insulina",
        genera_nadph=True
    ))

    # 2. 6-Fosfoglucono-δ-lactona
    contenido_svg.append(crear_metabolito(
        x=340, y=285,
        nombre="6-Fosfoglucono-δ-Lactona",
        carbonos="6 Carbonos (Lactona)",
        detalle="Éster intramolecular hidrolizable",
        svg_estructura=FOSFOGLUCONO_LACTONA_6
    ))

    # Reacción 2: Lactonasa (+ H2O)
    contenido_svg.append(crear_reaccion_oxidativa(
        x=385, y=390,
        enzima="6-Fosfogluconolactonasa",
        ec="EC 3.1.1.31 (Mg²⁺)",
        entra_agua=True
    ))

    # 3. 6-Fosfogluconato (Cadena lineal de 135 px de altura)
    contenido_svg.append(crear_metabolito(
        x=340, y=470,
        nombre="6-Fosfogluconato",
        carbonos="6 Carbonos (Cadena lineal)",
        detalle="Ácido descarboxilable",
        svg_estructura=FOSFOGLUCONATO_6
    ))

    # Reacción 3: 6-Fosfogluconato DH (Descarboxilación Oxidativa)
    # Ubicada en y = 650 (50 px de aire libre con el fosfato de arriba)
    contenido_svg.append(crear_reaccion_oxidativa(
        x=385, y=650,
        enzima="6-Fosfogluconato Deshidrogenasa",
        ec="EC 1.1.1.44 (Descarboxilación)",
        genera_nadph=True,
        salida_co2=True
    ))

    # 4. D-Ribulosa-5-Fosfato (Fin de la fase oxidativa)
    contenido_svg.append(crear_metabolito(
        x=340, y=745,
        nombre="D-Ribulosa-5-Fosfato",
        carbonos="5 Carbonos (Pentosa Cetosa)",
        detalle="Cruce a la fase no oxidativa",
        svg_estructura=RIBULOSA_5_FOSFATO
    ))


    # =========================================================================
    # FASE 2: FASE NO OXIDATIVA
    # =========================================================================

    # Ramificación amplia desde Ribulosa-5-P con textos despejados
    contenido_svg.append("""
    <!-- Ramificación amplia de la Ribulosa-5-P (sin solapamiento de textos) -->
    <g transform="translate(385, 905)">
      <!-- Rama Izquierda (Epimerasa -> Xilulosa-5-P) -->
      <path d="M -20 0 Q -110 30 -160 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <!-- Texto de Epimerasa a la izquierda con text-anchor='end' para no pisar la curva -->
      <g transform="translate(-175, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800" text-anchor="end">Fosfopentosa Epimerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 5.1.3.1 (⇄)</text>
      </g>

      <!-- Rama Derecha (Isomerasa -> Ribosa-5-P) -->
      <path d="M 20 0 Q 110 30 180 70" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <!-- Texto de Isomerasa a la derecha sin pisar la curva -->
      <g transform="translate(175, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="11" font-weight="800">Fosfopentosa Isomerasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9" font-family="'JetBrains Mono', monospace">EC 5.3.1.6 (⇄)</text>
      </g>
    </g>
    """)

    # 5a. D-Xilulosa-5-Fosfato (A la izquierda)
    contenido_svg.append(crear_metabolito(
        x=70, y=990,
        nombre="D-Xilulosa-5-P",
        carbonos="5 Carbonos (Epímero C3)",
        detalle="Donador de 2C (TPP)",
        svg_estructura=XILULOSA_5_FOSFATO,
        texto_izquierda=True
    ))

    # 5b. D-Ribosa-5-Fosfato (A la derecha)
    contenido_svg.append(crear_metabolito(
        x=560, y=980,
        nombre="D-Ribosa-5-P",
        carbonos="5 Carbonos (Pentosa Aldosa)",
        detalle="Precursora de Nucleótidos",
        svg_estructura=RIBOSA_5_FOSFATO
    ))

    # SALIDA HACIA SÍNTESIS DE NUCLEÓTIDOS: Bajada vertical limpia debajo de Ribosa-5-P
    contenido_svg.append("""
    <!-- Salida hacia Síntesis de Nucleótidos (Despejada de Ribosa-5-P y de Transcetolasa) -->
    <g transform="translate(730, 1055)">
      <!-- Flecha vertical púrpura que desciende hacia la caja -->
      <line x1="0" y1="0" x2="0" y2="28" stroke="#7c3aed" stroke-width="2.5" marker-end="url(#arrowPurple)"/>
      
      <!-- Caja elegante de Nucleótidos -->
      <g transform="translate(0, 35)">
        <rect x="-95" y="0" width="190" height="38" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8" filter="drop-shadow(0 2px 4px rgba(124,58,237,0.1))"/>
        <text x="0" y="16" fill="#6d28d9" font-size="10" font-weight="800" text-anchor="middle">SÍNTESIS DE NUCLEÓTIDOS</text>
        <text x="0" y="29" fill="#7c3aed" font-size="9" font-weight="600" text-anchor="middle">ATP • GTP • ARN • ADN • PRPP</text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # PASO 1 NO OXIDATIVO: TRANSCETOLASA 1 (X5P + R5P ⇄ S7P + GAP)
    # Ubicada en Y = 1170 (con 60 px de aire libre debajo de la caja morada)
    # -------------------------------------------------------------------------
    contenido_svg.append(crear_paso_no_oxidativo(
        x=385, y=1170,
        enzima="Transcetolasa (TK1)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="Xilulosa-5-P (5C) + Ribosa-5-P (5C)",
        productos_txt="GAP (3C) + Sedoheptulosa-7-P (7C)"
    ))

    # Productos del Paso 1:
    # Sedoheptulosa-7-P (7C) a la izquierda
    contenido_svg.append(crear_metabolito(
        x=70, y=1250,
        nombre="Sedoheptulosa-7-P",
        carbonos="7 Carbonos (Cetosa)",
        detalle="Intermediario de 7C",
        svg_estructura=SEDOHEPTULOSA_7_FOSFATO,
        texto_izquierda=True
    ))

    # Gliceraldehído-3-P (3C) a la derecha
    contenido_svg.append(crear_metabolito(
        x=560, y=1250,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="Intermediario transferible",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))

    # -------------------------------------------------------------------------
    # PASO 2 NO OXIDATIVO: TRANSALDOLASA (S7P + GAP ⇄ F6P + E4P)
    # -------------------------------------------------------------------------
    contenido_svg.append(crear_paso_no_oxidativo(
        x=385, y=1400,
        enzima="Transaldolasa (TA)",
        ec="EC 2.2.1.2 (Base de Schiff con Lisina)",
        sustratos_txt="Sedoheptulosa-7-P (7C) + GAP (3C)",
        productos_txt="Fructosa-6-P (6C) + Eritrosa-4-P (4C)"
    ))

    # Productos del Paso 2:
    # Eritrosa-4-P (4C) a la izquierda
    contenido_svg.append(crear_metabolito(
        x=70, y=1480,
        nombre="D-Eritrosa-4-P",
        carbonos="4 Carbonos (Tetrosa)",
        detalle="Aceptor de la TK2",
        svg_estructura=ERITROSA_4_FOSFATO,
        texto_izquierda=True
    ))

    # Fructosa-6-P (6C) a la derecha (¡Primer reingreso a Glucólisis!)
    contenido_svg.append(crear_metabolito(
        x=560, y=1480,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Furanosa)",
        detalle="→ Reingreso al eje glucolítico",
        svg_estructura=FRUCTOSA_6_FOSFATO
    ))

    # -------------------------------------------------------------------------
    # PASO 3 NO OXIDATIVO: TRANSCETOLASA 2 (X5P + E4P ⇄ F6P + GAP)
    # -------------------------------------------------------------------------
    contenido_svg.append(crear_paso_no_oxidativo(
        x=385, y=1620,
        enzima="Transcetolasa (TK2)",
        ec="EC 2.2.1.1 (Cofactor: TPP, Mg²⁺)",
        sustratos_txt="2ª Xilulosa-5-P (5C) + Eritrosa-4-P (4C)",
        productos_txt="Fructosa-6-P (6C) + GAP (3C)"
    ))

    # Productos finales del Paso 3 (Reingreso total a Glucólisis):
    # Segunda Fructosa-6-P a la izquierda
    contenido_svg.append(crear_metabolito(
        x=70, y=1700,
        nombre="Fructosa-6-P (2ª)",
        carbonos="6 Carbonos (Furanosa)",
        detalle="→ Reingreso al eje glucolítico",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        texto_izquierda=True
    ))

    # Gliceraldehído-3-P (3C) a la derecha
    contenido_svg.append(crear_metabolito(
        x=560, y=1700,
        nombre="Gliceraldehído-3-P",
        carbonos="3 Carbonos (Triosa)",
        detalle="→ Reingreso al eje glucolítico",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO
    ))

    # -------------------------------------------------------------------------
    # BANNER DE BALANCE ESTEQUIOMÉTRICO FINAL Y REINGRESO A GLUCÓLISIS
    # -------------------------------------------------------------------------
    contenido_svg.append("""
    <!-- Banner de Balance y Cierre -->
    <g transform="translate(385, 1890)">
      <rect x="-240" y="0" width="480" height="75" rx="10" fill="#ffffff" stroke="#ea580c" stroke-width="2" filter="drop-shadow(0 4px 8px rgba(0,0,0,0.06))"/>
      <text x="0" y="24" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">BALANCE TOTAL DE LA FASE NO OXIDATIVA</text>
      <text x="0" y="42" fill="#ea580c" font-size="11" font-weight="900" text-anchor="middle">3 Pentosas (5C) ⇄ 2 Fructosa-6-P (6C) + 1 Gliceraldehído-3-P (3C)</text>
      <text x="0" y="58" fill="#64748b" font-size="10" text-anchor="middle">Todos los carbonos se reciclan de vuelta hacia la Glucólisis en citosol</text>
    </g>

    <!-- Flecha de reingreso hacia la izquierda contenida dentro del canvas -->
    <g transform="translate(145, 1925)">
      <path d="M 0 0 L -100 0" fill="none" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#arrowFlow)"/>
      <text x="-50" y="-8" fill="#c2410c" font-size="10" font-weight="800" text-anchor="middle">a Glucólisis</text>
    </g>
    """)

    # Fases, balance oxidativo y columna derecha de contexto
    contenido_svg.append(generar_fases_y_balance())
    panel_svg, _alto = generar_panel_derecho(2150)
    contenido_svg.append(panel_svg)

    # Unir todo el código
    html_final = CABECERA_HTML.replace("<!-- MARCADORES_PANELES -->", MARCADORES_PANELES) + "\n".join(contenido_svg) + PIE_HTML

    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_salida = os.path.join(dir_actual, "Pentosas.html")
    with open(ruta_salida, "w", encoding="utf-8") as archivo:
        archivo.write(html_final)

    # Extraer y escribir Pentosas.svg puro
    inicio_svg = html_final.find("<svg ")
    fin_svg = html_final.rfind("</svg>") + 6
    if inicio_svg != -1 and fin_svg != -1:
        svg_puro = html_final[inicio_svg:fin_svg]
        ruta_svg = os.path.join(dir_actual, "Pentosas.svg")
        with open(ruta_svg, "w", encoding="utf-8") as f_svg:
            f_svg.write(svg_puro)
        print(f"✅ SVG puro guardado en: {ruta_svg}")

    print(f"✅ ¡Vía de las Pentosas Fosfato con colisiones corregidas en: {ruta_salida}!")


if __name__ == "__main__":
    main()
