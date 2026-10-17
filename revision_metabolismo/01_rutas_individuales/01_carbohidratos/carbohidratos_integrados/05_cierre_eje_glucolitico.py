# =============================================================================
# MÓDULO DE REVISIÓN: Tramo Inferior de Glucólisis hasta Piruvato
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/carbohidratos_unidos/generar_carbohidratos_unidos.py (líneas 1032 a 1241 de 1241)
# Descripción      : Bifurcación de triosas fosfato, fase de beneficio energético y piruvato.
# =============================================================================

    # =========================================================================
    # RESTO DEL EJE GLUCOLÍTICO (CENTRAL: X_GLU = 1520, X_FLECHA = 1580)
    # =========================================================================
    # Reacción 2: Fosfoglucosa Isomerasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=530,
        enzima="Fosfoglucosa Isomerasa",
        ec="EC 5.3.1.9 (⇄)",
        reversible=True
    ))

    # 3. Fructosa-6-Fosfato (RECIBE RETORNO DE PENTOSAS)
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=610,
        nombre="Fructosa-6-Fosfato",
        carbonos="6 Carbonos (Cetosa Ⓟ)",
        detalle="Punto receptor de Transcetolasa / Transaldolasa",
        svg_estructura=FRUCTOSA_6_FOSFATO,
        dx_texto=140
    ))

    # Reacción 3: PFK-1
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=725,
        enzima="Fosfofructoquinasa-1 (PFK-1)",
        ec="EC 2.7.1.11 (Compromiso Clave)",
        regulacion="⊣ ATP, Citrato | ⊕ AMP, F-2,6-BP",
        entra_energia="- 1 ATP",
        sale_energia="+ 1 ADP"
    ))

    # 4. Fructosa-1,6-Bisfosfato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=825,
        nombre="Fructosa-1,6-Bisfosfato",
        carbonos="6 Carbonos (Fructofuranosa 1,6-Ⓟ)",
        detalle="Molécula simétrica lista para clivaje",
        svg_estructura=FRUCTOSA_1_6_BISFOSFATO,
        dx_texto=140
    ))

    # Reacción 4: Aldolasa
    svg_parts.append("""
    <g transform="translate(1580, 940)">
      <line x1="0" y1="0" x2="0" y2="40" stroke="#ea580c" stroke-width="2.8"/>
      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="14.5" font-weight="800">Aldolasa A (Clivaje C3-C4)</text>
        <text x="0" y="15" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 4.1.2.13 (Retroaldólica)</text>
      </g>
      <path d="M 0 40 Q -70 55 -110 80" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <path d="M 0 40 Q 70 55 110 80" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
    </g>
    """)

    # 5a. DHAP y 5b. GAP (Bifurcación simétrica)
    svg_parts.append(crear_metabolito(
        x=1320, y=1035,
        nombre="Dihidroxiacetona-Ⓟ",
        carbonos="3 Carbonos (Cetotriosa)",
        detalle="Isomerizada por TPI",
        svg_estructura=DIHIDROXIACETONA_FOSFATO,
        texto_izquierda=True
    ))

    svg_parts.append(crear_metabolito(
        x=1680, y=1035,
        nombre="Gliceraldehído-3-Ⓟ",
        carbonos="3 Carbonos (Aldotriosa)",
        detalle="Continúa la vía oxidativa",
        svg_estructura=GLICERALDEHIDO_3_FOSFATO,
        dx_texto=140
    ))

    # TPI (Conexión horizontal reversible entre triosas)
    svg_parts.append("""
    <g transform="translate(1540, 1070)">
      <line x1="-70" y1="-3" x2="70" y2="-3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="70" y1="3" x2="-70" y2="3" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <g transform="translate(0, -12)">
        <text x="0" y="-8" fill="#0f172a" font-size="13.5" font-weight="800" text-anchor="middle">Triosa Fosfato Isomerasa</text>
        <text x="0" y="6" fill="#64748b" font-size="11" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 5.3.1.1 (⇄)</text>
      </g>
    </g>
    """)

    # Convergencia a 2x GAP (Limpia, sin globo)
    svg_parts.append("""
    <g transform="translate(1580, 1180)">
      <path d="M 1720 1120 Q 1720 1160 1580 1180" fill="none" stroke="#ea580c" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <text x="0" y="0" fill="#c2410c" font-size="12.5" font-weight="900" text-anchor="middle">
        FASE DE BENEFICIO (× 2 TRIOSAS)
      </text>
    </g>
    """)

    # Reacción 6: GAPDH
    svg_parts.append("""
    <g transform="translate(1580, 1235)">
      <line x1="-3.5" y1="0" x2="-3.5" y2="52" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="3.5" y1="52" x2="3.5" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <path d="M -85 10 Q -30 10 -4 20" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrowSlate)"/>
      <text x="-92" y="14" fill="#475569" font-size="12" font-weight="800" text-anchor="end">+ 2 NAD⁺ + 2 Pi</text>
      <path d="M -4 28 Q -30 38 -85 38" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-92" y="42" fill="#059669" font-size="12" font-weight="800" text-anchor="end">+ 2 NADH + 2 H⁺</text>
      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="14.5" font-weight="800">GAPDH (Gliceraldehído-3-P DH)</text>
        <text x="0" y="15" fill="#64748b" font-size="11.5" font-family="'JetBrains Mono', monospace">EC 1.2.1.12 (Cisteína catalítica)</text>
      </g>
    </g>
    """)

    # 5. 1,3-Bisfosfoglicerato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1345,
        nombre="1,3-Bisfosfoglicerato",
        carbonos="3 Carbonos (Acil-fosfato de alta energía)",
        detalle="Primer intermediario de alto potencial Ⓟ",
        svg_estructura=BISFOSFOGLICERATO_1_3,
        dx_texto=140
    ))

    # Reacción 7: Fosfoglicerato Quinasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1460,
        enzima="Fosfoglicerato Quinasa",
        ec="EC 2.7.2.3 (Fosforilación a nivel de sustrato)",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True,
        reversible=True
    ))

    # 6. 3-Fosfoglicerato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1560,
        nombre="3-Fosfoglicerato",
        carbonos="3 Carbonos (Carboxilato)",
        detalle="Substrato de mutación intramolecular",
        svg_estructura=FOSFOGLICERATO_3,
        dx_texto=140
    ))

    # Reacción 8: Fosfoglicerato Mutasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1670,
        enzima="Fosfoglicerato Mutasa",
        ec="EC 5.4.2.1 (Intermediario 2,3-BPG)",
        reversible=True
    ))

    # 7. 2-Fosfoglicerato
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1770,
        nombre="2-Fosfoglicerato",
        carbonos="3 Carbonos (Éster fosfórico C2)",
        detalle="Substrato para deshidratación",
        svg_estructura=FOSFOGLICERATO_2,
        dx_texto=140
    ))

    # Reacción 9: Enolasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=1880,
        enzima="Enolasa",
        ec="EC 4.2.1.11 (Mg²⁺, Deshidratación)",
        salida_agua=True,
        reversible=True
    ))

    # 8. PEP
    svg_parts.append(crear_metabolito(
        x=X_GLU, y=1980,
        nombre="Fosfoenolpiruvato (PEP)",
        carbonos="3 Carbonos (Enol-fosfato)",
        detalle="Mayor potencial de transferencia Ⓟ (ΔG'° = -61.9 kJ/mol)",
        svg_estructura=FOSFOENOLPIRUVATO,
        dx_texto=140
    ))

    # Reacción 10: Piruvato Quinasa
    svg_parts.append(crear_reaccion(
        x=X_FLECHA, y=2090,
        enzima="Piruvato Quinasa",
        ec="EC 2.7.1.40 (K⁺, Mg²⁺)",
        regulacion="⊣ ATP, Alanina | ⊕ F-1,6-BP",
        entra_energia="- 2 ADP",
        sale_energia="+ 2 ATP",
        es_ganancia=True
    ))

    # 9. Piruvato: nodo maestro compartido con la mitocondria
    svg_parts.append(crear_metabolito(
        x=X_PIRUVATO, y=Y_PIRUVATO,
        nombre="Piruvato",
        carbonos="3 Carbonos (α-Cetoácido)",
        detalle="Destino terminal: cruce al interior mitocondrial vía MPC",
        svg_estructura=PIRUVATO,
        dx_texto=140
    ))

    # Ensamblar HTML completo
    html_final = CABECERA_HTML + "\n".join(svg_parts) + PIE_HTML

    ruta_salida = os.path.join(os.path.dirname(__file__), "Carbohidratos_Unidos.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"✅ Mapa Integrado de Carbohidratos generado con éxito en: {ruta_salida}")

if __name__ == "__main__":
    generar_mapa_carbohidratos()
