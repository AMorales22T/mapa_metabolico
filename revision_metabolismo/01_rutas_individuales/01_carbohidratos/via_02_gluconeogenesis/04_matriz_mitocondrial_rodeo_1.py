# =============================================================================
# MÓDULO DE REVISIÓN: Matriz Mitocondrial y Rodeo 1 (PC y PEPCK)
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/via_02_gluconeogenesis/generar_gluconeogenesis.py (líneas 1091 a 1263 de 1263)
# Descripción      : Carboxilación del piruvato en matriz, lanzadera de malato y cierre del mapa.
# =============================================================================

    # =========================================================================
    # MATRIZ MITOCONDRIAL: PIRUVATO, PC, OAA, mMDH, MALATO Y CATAPLEROSIS DE KREBS
    # =========================================================================

    # -------------------------------------------------------------------------
    # 12. Piruvato Mitocondrial [3 C] alineado en X=1255
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=1255, y=2760,
        nombre="Piruvato (Mitocondrial)",
        carbonos="3 C",
        formula="C₃H₃O₃⁻ (Sustrato de Carboxilación en Matriz)",
        svg_estructura=PIRUVATO,
        dx_texto=100,
        badge_color="#ea580c"
    ))

    # -------------------------------------------------------------------------
    # PASO 1: BYPASS 1A - Piruvato Carboxilasa (PC) en X=1280
    # Sustituye a la Piruvato Quinasa (PK) de la Glucólisis
    # Fijación de Carbono: + CO2 (3C + 1C -> 4C)
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- PASO 1: PIRUVATO CARBOXILASA (PC) -->
    <g transform="translate(1280, 2870)">
      <line x1="0" y1="0" x2="0" y2="130" stroke="#7c3aed" stroke-width="3" marker-end="url(#arrowPurple)"/>
      <path d="M -85 25 Q -30 25 -4 38" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-92" y="29" fill="#dc2626" font-size="11" font-weight="800" text-anchor="end">- 1 ATP</text>
      
      <path d="M -4 54 Q -30 68 -85 68" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-92" y="72" fill="#475569" font-size="11" font-weight="800" text-anchor="end">+ ADP + Pi</text>

      <path d="M -85 105 Q -30 105 -4 85" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="-92" y="109" fill="#0284c7" font-size="11" font-weight="900" text-anchor="end">+ HCO₃⁻ (Fijación de CO₂: 3 C + 1 C -> 4 C)</text>
      
      {badge_paso(1, -25, 65, es_bypass=True, etiqueta="PASO 1")}
      
      <g transform="translate(25, 18)">
        <text x="0" y="-8" fill="#6d28d9" font-size="12" font-weight="900">BYPASS 1A: Piruvato Carboxilasa (PC)</text>
        <text x="0" y="8" fill="#b91c1c" font-size="10" font-weight="800">Sustituye a: Piruvato Quinasa (PK) de la glucólisis</text>
        <text x="0" y="24" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">EC 6.4.1.1 (Requiere Biotina / Vitamina B₇)</text>
        <text x="0" y="40" fill="#16a34a" font-size="10.5" font-weight="800">(+) Acetil-CoA (Activador alostérico obligatorio)</text>
        <text x="0" y="55" fill="#dc2626" font-size="10.5" font-weight="800">(-) ADP (Baja carga energética frena PC)</text>
        <text x="0" y="70" fill="#78350f" font-size="9.5" font-weight="700">Conmutador: Acetil-CoA inhibe PDH y activa PC -> desvía piruvato a glucosa</text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # 13. Oxalacetato Mitocondrial (OAA Mitocondrial) [4 C]
    # Posicionado en X=1255, Y=3070 con dx_texto=100
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=1255, y=3070,
        nombre="Oxalacetato (OAA Mitocondrial)",
        carbonos="4 C",
        formula="C₄H₂O₅²⁻ (MMI carece de carrier directo para OAA)",
        svg_estructura=OXALACETATO,
        dx_texto=100,
        badge_color="#7c3aed"
    ))

    # -------------------------------------------------------------------------
    # OTROS PRECURSORES: CATAPLEROSIS DEL CICLO DE KREBS (AMINOÁCIDOS GLUCOGÉNICOS)
    # Distinguidos claramente de los que entran como Piruvato: alimentan intermediarios de Krebs
    # -------------------------------------------------------------------------
    svg_parts.append("""
    <!-- CATAPLEROSIS DEL CICLO DE KREBS: PRECURSORES QUE ALIMENTAN OAA MATRICIAL -->
    <g transform="translate(1420, 3180)">
      <text x="0" y="0" fill="#b45309" font-size="12.5" font-weight="900">
        PRECURSORES CATAPLERÓTICOS: CICLO DE KREBS (AMINOÁCIDOS)
      </text>
      <text x="0" y="16" fill="#92400e" font-size="10" font-weight="700">
        Precursores que NO pasan por Piruvato: entran como intermediarios de Krebs y forman Oxaloacetato [4 C]:
      </text>

      <g transform="translate(0, 30)">
        <text x="0" y="0" fill="#0f172a" font-size="10" font-weight="800">• α-Cetoglutarato [5 C]:</text>
        <text x="140" y="0" fill="#047857" font-size="9.5">Glutamato, Glutamina, Prolina, Histidina, Arginina</text>

        <text x="0" y="16" fill="#0f172a" font-size="10" font-weight="800">• Succinil-CoA [4 C]:</text>
        <text x="140" y="16" fill="#047857" font-size="9.5">Metionina, Valina, Isoleucina, Treonina, Propionil-CoA (grasas impares)</text>

        <text x="0" y="32" fill="#0f172a" font-size="10" font-weight="800">• Fumarato [4 C]:</text>
        <text x="140" y="32" fill="#047857" font-size="9.5">Fenilalanina, Tirosina, Aspartato</text>

        <text x="0" y="48" fill="#0f172a" font-size="10" font-weight="800">• Oxalacetato directo [4 C]:</text>
        <text x="140" y="48" fill="#047857" font-size="9.5">Aspartato, Asparagina (Transaminación directa por AST)</text>

        <text x="0" y="68" fill="#b91c1c" font-size="9.5" font-weight="800">
          Nota Bioquímica: Acetil-CoA (ácidos grasos pares) NO aporta carbonos netos
        </text>
        <text x="0" y="80" fill="#64748b" font-size="8.5">
          (Entran 2 C como Acetil-CoA y se liberan 2 C como CO₂ en Krebs; balance neto = 0).
        </text>
      </g>

      <!-- Flecha ascendente suave conectando al pool de Oxalacetato matricial -->
      <path d="M 0 10 Q -50 -30 -90 -60" fill="none" stroke="#b45309" stroke-width="2.2" stroke-dasharray="6 3" marker-end="url(#arrowAmber)"/>
      <text x="-65" y="-30" fill="#b45309" font-size="9.5" font-weight="800" text-anchor="middle">➔ Pool OAA [4 C]</text>
    </g>
    """)

    # -------------------------------------------------------------------------
    # PASO 2: mMDH (Malato Deshidrogenasa Mitocondrial)
    # Reduce OAA a Malato gastando 1 NADH matricial
    # Conecta Oxalacetato Mitocondrial (X=1255) con L-Malato Mitocondrial (X=220)
    # Flecha en Y=3270, termina en X=360 (despejada de Malato que está en X=220-310)
    # -------------------------------------------------------------------------
    svg_parts.append(f"""
    <!-- PASO 2: mMDH -->
    <g transform="translate(360, 3270)">
      <line x1="850" y1="0" x2="0" y2="0" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#arrowPurple)"/>
      {badge_paso(2, 820, 0, es_bypass=False, etiqueta="")}

      <g transform="translate(425, -12)">
        <text x="0" y="-12" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#6d28d9" text-anchor="middle">mMDH (MDH Mitocondrial)</text>
        <text x="0" y="2" font-family="'Inter', sans-serif" font-size="9.5" fill="#475569" text-anchor="middle">Reduce OAA a Malato: única vía para exportar el esqueleto de 4C</text>
        <text x="0" y="22" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#dc2626" text-anchor="middle">+ NADH + H⁺ -> + NAD⁺ (Gasta 1 NADH matricial)</text>
      </g>
    </g>
    """)

    # -------------------------------------------------------------------------
    # 14. L-Malato Mitocondrial [4 C]
    # Posicionado en X=220, Y=3200 con fórmula en texto_izquierda
    # -------------------------------------------------------------------------
    svg_parts.append(crear_metabolito(
        x=220, y=3200,
        nombre="L-Malato (Mitocondrial)",
        carbonos="4 C",
        formula="C₄H₄O₅²⁻ (Exportable por OGC)",
        svg_estructura=MALATO,
        texto_izquierda=True,
        badge_color="#047857"
    ))

    # -------------------------------------------------------------------------
    # ESTEQUIOMETRÍA Y BALANCE GLOBAL EN EL ENCABEZADO SUPERIOR DERECHO
    # -------------------------------------------------------------------------
    svg_parts.append("""
    <g transform="translate(1850, 30)">
      <text x="0" y="0" fill="#0f172a" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="end">
        BALANCE GLOBAL: 2 Piruvato (3 C) + 4 ATP + 2 GTP + 2 NADH + 6 H₂O -> D-Glucosa (6 C) + 4 ADP + 2 GDP + 6 Pi + 2 NAD⁺
      </text>
      <text x="0" y="16" fill="#dc2626" font-size="10" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">
        Inversión total de 6 enlaces de alta energía (~P) por cada molécula de glucosa sintetizada
      </text>
    </g>
    """)

    # Ensamblar HTML completo
    html_final = CABECERA_HTML + "\n".join(svg_parts) + PIE_HTML

    dir_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_salida = os.path.join(dir_actual, "Gluconeogenesis.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(html_final)

    # Extraer y escribir Gluconeogenesis.svg puro
    inicio_svg = html_final.find("<svg ")
    fin_svg = html_final.rfind("</svg>") + 6
    if inicio_svg != -1 and fin_svg != -1:
        svg_puro = html_final[inicio_svg:fin_svg]
        ruta_svg = os.path.join(dir_actual, "Gluconeogenesis.svg")
        with open(ruta_svg, "w", encoding="utf-8") as f_svg:
            f_svg.write(svg_puro)
        print(f"✅ SVG puro guardado en: {ruta_svg}")

    print(f"✅ Mapa Individual de Gluconeogénesis generado con éxito en: {ruta_salida}")

if __name__ == "__main__":
    generar_mapa_gluconeogenesis()
