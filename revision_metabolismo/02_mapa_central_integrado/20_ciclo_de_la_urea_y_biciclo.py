# =============================================================================
# MÓDULO DE REVISIÓN: Vía 14: Ciclo de la Urea y Biciclo de Krebs-Henseleit
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 3096 a 3443 de 4188)
# Descripción      : CPS-I, OTC, ASS1, ASL, ARG1, transportadores ORNT1/Citrina y conexión por fumarato/aspartato.
# =============================================================================

    # =========================================================================
    # 13. CICLO DE LA UREA Y BICICLO DE KREBS (CUADRANTE DERECHO - ENTORNO REAL)
    # =========================================================================
    x_u_l = 4100  # Carril Izquierdo (Carbamoil-P, CPS-1, Aspartato, Fumarato, Biciclo)
    x_u_c = 4420  # Carril Central (Flujo principal: Citrulina, Arg-Succ, Arginina, Urea)
    x_u_r = 4640  # Carril Derecho (Lanzadera de Ornitina, ORNT1)

    partes.append(f'''
    <!-- ================================================================= -->
    <!-- RUTA 13: CICLO DE LA UREA (DESINTOXICACIÓN HEPÁTICA DE NITRÓGENO)   -->
    <!-- ================================================================= -->
    <g id="ruta_ciclo_urea">
      <!-- Rótulo de la Ruta flotando libremente en citosol superior (despejado a la izquierda de la excreción) -->
      {badge_via(14, 4040, 230)}
      <g id="rotulo_ciclo_urea" data-arrastrable="1" transform="translate(4210, 235)">
        <text x="0" y="0" fill="#0f766e" font-size="24" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="3">CICLO DE LA UREA</text>
        <text x="0" y="24" fill="#64748b" font-size="12" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Desintoxicación Hepática de Amonio • Biciclo de Krebs • Excreción Renal</text>
      </g>
    ''')

    # -------------------------------------------------------------------------
    # FASE MATRICIAL MITOCONDRIAL (Y > 2160)
    # -------------------------------------------------------------------------

    # 1. Sustratos Iniciales (NH4+ libre + HCO3-)
    partes.append(nodo_libre(
        x_u_l - 40, 3240,
        "Sustratos de Nitrógeno", "NH₄⁺ + HCO₃⁻",
        UREA_IONES_INICIALES, "m_u_sustratos_inicio",
        text_right=True, dx=190,
        detalle="Amonio aportado por GLDH matricial"
    ))

    # Reacción 1: CPS-1 (Carbamoil Fosfato Sintetasa I)
    partes.append(f'''
    <g id="rx_u_cps1" data-arrastrable="1" transform="translate({x_u_l}, 3060)">
      <!-- Flecha vertical ascendente -->
      <line x1="0" y1="120" x2="0" y2="-10" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de 2 ATP (lado izquierdo) -->
      <path d="M -75 90 Q -25 90 -4 65" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-80" y="93" fill="#dc2626" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">- 2 ATP</text>

      <!-- Salida de 2 ADP + Pi (lado izquierdo) -->
      <path d="M -4 35 Q -25 20 -75 20" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-80" y="24" fill="#475569" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ 2 ADP + Pi</text>

      <!-- Metadatos de CPS-1 -->
      <g transform="translate(20, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="12.5" font-weight="900" font-family="'Inter', sans-serif">Carbamoil Fosfato Sintetasa I (CPS-1)</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">EC 6.3.4.16 (Mitocondrial)</text>
        <text x="0" y="27" fill="#16a34a" font-size="10" font-weight="800" font-family="'Inter', sans-serif">⊕ N-Acetilglutamato (NAG) activador obligado</text>
        <text x="0" y="40" fill="#b45309" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Paso limitante irreversible</text>
      </g>
    </g>
    ''')

    # 2. Carbamoil Fosfato (1C)
    partes.append(nodo_libre(
        x_u_l - 40, 2860,
        "Carbamoil Fosfato", "1C",
        UREA_CARBAMOIL_P, "m_u_carbamoil_p",
        text_right=True, dx=140,
        detalle="1ᵉʳ nitrógeno activado en anhidro fosfato"
    ))

    # 3. L-Ornitina en Matriz Mitocondrial (X=4700, texto orientado hacia el interior de la matriz)
    partes.append(nodo_libre(
        x_u_r - 40, 2860,
        "L-Ornitina (Matriz)", "5C",
        UREA_ORNITINA, "m_u_ornitina_mito",
        text_right=False, dx=-15,
        detalle="Aceptor regenerado por ORNT1 ↻"
    ))

    # Reacción 2: OTC (Ornitina Transcarbamilasa)
    partes.append(f'''
    <g id="rx_u_otc" data-arrastrable="1" transform="translate({x_u_c}, 2670)">
      <!-- Curva desde Carbamoil-P hacia OTC -->
      <path d="M -200 160 Q -70 60 -4 20" fill="none" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

      <!-- Curva desde Ornitina matricial hacia OTC -->
      <path d="M 220 160 Q 90 60 4 20" fill="none" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowFlow)"/>

      <!-- Flecha vertical ascendente hacia Citrulina -->
      <line x1="0" y1="20" x2="0" y2="-65" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Salida de Pi libre (lado izquierdo) -->
      <path d="M -4 -15 Q -35 -25 -75 -25" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-80" y="-21" fill="#475569" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ Pi (Fosfato libre)</text>

      <!-- Metadatos de OTC -->
      <g transform="translate(18, -35)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif">Ornitina Transcarbamilasa</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">OTC • EC 2.1.3.3 (Mitocondrial)</text>
        <text x="0" y="25" fill="#0f766e" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Formación del grupo ureido</text>
      </g>
    </g>
    ''')

    # 4. L-Citrulina en Matriz Mitocondrial
    partes.append(nodo_libre(
        x_u_c - 40, 2370,
        "L-Citrulina (Matriz)", "6C",
        UREA_CITRULINA, "m_u_citrulina_mito",
        text_right=True, dx=140,
        detalle="1ᵉʳ nitrógeno fijado ➔ Exportación"
    ))

    # -------------------------------------------------------------------------
    # FASE TRANSLOCACIÓN MMI (Y ≈ 2160)
    # -------------------------------------------------------------------------

    # A. Transportador SLC25A13 (Citrina) en el carril central
    partes.append(f'''
    <g id="trans_u_citrina" data-arrastrable="1" transform="translate({x_u_c}, 2160)">
      <!-- Flechas de translocación ascendente de Citrulina -->
      <path d="M 0 160 L 0 25" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)" fill="none"/>
      <path d="M 0 -25 L 0 -85" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)" fill="none"/>

      <!-- Cápsula del transportador sobre MMI -->
      <rect x="-60" y="-18" width="120" height="36" rx="8" fill="#92400e" stroke="#78350f" stroke-width="2"/>
      <text x="0" y="4" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">SLC25A13</text>
      <text x="0" y="30" fill="#78350f" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Citrina (Exportador Citrulina)</text>
    </g>
    ''')

    # B. Transportador SLC25A15 (ORNT1) en el carril derecho
    partes.append(f'''
    <g id="trans_u_ornt1" data-arrastrable="1" transform="translate({x_u_r}, 2160)">
      <!-- Cápsula del transportador sobre MMI -->
      <rect x="-60" y="-18" width="120" height="36" rx="8" fill="#1d4ed8" stroke="#1e3a8a" stroke-width="2"/>
      <text x="0" y="4" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">SLC25A15</text>
      <text x="0" y="30" fill="#1e40af" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">ORNT1 (Carrier Ornitina)</text>
    </g>
    ''')

    # -------------------------------------------------------------------------
    # FASE CITOSÓLICA Y BICICLO DE KREBS-HENSELEIT (Y < 2160)
    # -------------------------------------------------------------------------

    # 5. L-Citrulina en Citosol
    partes.append(nodo_libre(
        x_u_c - 22, 1865,
        "L-Citrulina (Citosol)", "6C",
        UREA_CITRULINA, "m_u_citrulina_cito",
        text_right=True, dx=160,
        detalle="Recibida por SLC25A13 para condensación"
    ))

    # 6. BICICLO DE KREBS-HENSELEIT EN CARRIL IZQUIERDO (Fumarato ➔ L-Malato ➔ OAA ➔ L-Aspartato)
    # 6A. Fumarato libre resultante de ASL (X=4040, Y=1130)
    partes.append(nodo_libre(
        x_u_l - 60, 1130,
        "Fumarato", "4C",
        UREA_FUMARATO, "m_u_fumarato",
        text_right=False, dx=-20,
        detalle="Subproducto de escisión trans (ASL)"
    ))

    # Paso 1 del Biciclo: Fumarasa Citosólica (Fumarato + H2O ➔ L-Malato)
    partes.append(f'''
    <g id="rx_u_biciclo_fumarasa" data-arrastrable="1" transform="translate({x_u_l - 15}, 1248)">
      <line x1="0" y1="0" x2="0" y2="38" stroke="#ea580c" stroke-width="2.4" stroke-dasharray="6 3" marker-end="url(#arrowFlow)"/>
      <text x="14" y="16" fill="#c2410c" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">BICICLO: Fumarasa Citosólica</text>
      <text x="14" y="28" fill="#0284c7" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">+ H₂O (Hidratación)</text>
    </g>
    ''')

    # 6B. Intermediario 1 del Biciclo: L-Malato (Citosol) [4C]
    partes.append(nodo_libre(
        x_u_l - 60, 1295,
        "L-Malato (Biciclo)", "4C",
        GLUCONEO_MALATO, "m_u_malato_biciclo",
        text_right=False, dx=-20,
        detalle="Intermediario citosólico"
    ))

    # Paso 2 del Biciclo: MDH1 Citosólica (L-Malato + NAD+ ➔ OAA + NADH)
    partes.append(f'''
    <g id="rx_u_biciclo_mdh1" data-arrastrable="1" transform="translate({x_u_l - 15}, 1415)">
      <line x1="0" y1="0" x2="0" y2="38" stroke="#ea580c" stroke-width="2.4" stroke-dasharray="6 3" marker-end="url(#arrowFlow)"/>
      <text x="14" y="16" fill="#c2410c" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">MDH1 (Malato DH Citosólica)</text>
      <text x="14" y="28" fill="#059669" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">+ NAD⁺ ➔ + NADH + H⁺</text>
    </g>
    ''')

    # 6C. Intermediario 2 del Biciclo: Oxalacetato (Citosol) [4C]
    partes.append(nodo_libre(
        x_u_l - 60, 1465,
        "Oxalacetato (Biciclo)", "4C",
        GLUCONEO_OXALACETATO, "m_u_oaa_biciclo",
        text_right=False, dx=-20,
        detalle="Aceptor de grupo amino"
    ))

    # Paso 3 del Biciclo: AST / GOT1 Citosólica (OAA + L-Glutamato ➔ L-Aspartato + α-KG)
    partes.append(f'''
    <g id="rx_u_biciclo_got1" data-arrastrable="1" transform="translate({x_u_l - 15}, 1585)">
      <line x1="0" y1="0" x2="0" y2="38" stroke="#0d9488" stroke-width="2.4" stroke-dasharray="6 3" marker-end="url(#arrowTeal)"/>
      <text x="14" y="16" fill="#0f766e" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">AST / GOT1 (PLP)</text>
      <text x="14" y="28" fill="#2563eb" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">+ L-Glutamato ➔ + α-KG</text>
    </g>
    ''')

    # 6D. Donador lateral de nitrógeno: L-Aspartato (regenerado por el Biciclo y por Aralar)
    partes.append(nodo_libre(
        x_u_l - 60, 1635,
        "L-Aspartato", "4C",
        UREA_ASPARTATO, "m_u_aspartato",
        text_right=False, dx=-20,
        detalle="Aporta el 2º nitrógeno de la urea"
    ))

    # Reacción 3: ASS (Argininosuccinato Sintetasa)
    partes.append(f'''
    <g id="rx_u_ass" data-arrastrable="1" transform="translate({x_u_c}, 1610)">
      <!-- Flecha ascendente desde Citrulina -->
      <line x1="0" y1="240" x2="0" y2="-10" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de L-Aspartato desde el Biciclo de Krebs en el carril izquierdo -->
      <path d="M -275 115 Q -120 95 -4 25" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de 1 ATP (lado derecho) -->
      <path d="M 65 65 Q 25 65 4 45" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="70" y="68" fill="#dc2626" font-size="11" font-weight="800" font-family="'Inter', sans-serif">- 1 ATP</text>

      <!-- Salida de AMP + PPi (lado derecho) -->
      <path d="M 4 15 Q 25 5 65 5" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="70" y="9" fill="#475569" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">+ AMP + PPi (➔ 2 Pi)</text>

      <!-- Metadatos de ASS -->
      <g transform="translate(-18, -12)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Argininosuccinato</text>
        <text x="0" y="13" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Sintetasa (ASS1)</text>
        <text x="0" y="26" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 6.3.4.5 (Citosólica)</text>
        <text x="0" y="38" fill="#15803d" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">Intermedio Citrulil-AMP activado</text>
      </g>
    </g>
    ''')

    # 7. L-Argininosuccinato (10C) - Intermediario que une ambos nitrógenos
    partes.append(nodo_libre(
        x_u_c - 50, 1330,
        "L-Argininosuccinato", "10C",
        UREA_ARGININOSUCCINATO, "m_u_argininosuccinato",
        text_right=True, dx=165,
        detalle="Condensado Citrulina-Aspartato"
    ))

    # Reacción 4: ASL (Argininosuccinato Liasa)
    partes.append(f'''
    <g id="rx_u_asl" data-arrastrable="1" transform="translate({x_u_c}, 1190)">
      <!-- Flecha vertical ascendente hacia Arginina -->
      <line x1="0" y1="100" x2="0" y2="-10" stroke="#0d9488" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

      <!-- Salida lateral hacia la IZQUIERDA de FUMARATO -->
      <path d="M -4 45 Q -80 45 -180 45" fill="none" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      <text x="-110" y="25" fill="#c2410c" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">⮜ + Fumarato (4C)</text>

      <!-- Metadatos de la ASL -->
      <g transform="translate(18, 15)">
        <text x="0" y="0" fill="#0f172a" font-size="12" font-weight="900" font-family="'Inter', sans-serif">Argininosuccinato Liasa (ASL)</text>
        <text x="0" y="13" fill="#64748b" font-size="9.5" font-family="'JetBrains Mono', monospace">EC 4.3.2.1 (Eliminación trans)</text>
        <text x="0" y="25" fill="#be185d" font-size="9" font-weight="700" font-family="'Inter', sans-serif">Escisión del esqueleto de 4C</text>
      </g>
    </g>
    ''')

    # 9. L-Arginina (6C) (carril central, X=4420, Y=1160)
    partes.append(nodo_libre(
        x_u_c - 40, 1010,
        "L-Arginina", "6C",
        UREA_ARGININA, "m_u_arginina",
        text_right=True, dx=145,
        detalle="Grupo guanidino cargado"
    ))

    # Reacción 5: Arginasa 1 (ARG1) - Bifurcación hacia Urea y Ornitina
    partes.append(f'''
    <g id="rx_u_arg1" data-arrastrable="1" transform="translate({x_u_c}, 830)">
      <!-- Entrada de Agua para la hidrólisis -->
      <path d="M -75 35 Q -25 35 -4 50" fill="none" stroke="#0284c7" stroke-width="2" marker-end="url(#arrowBlue)"/>
      <text x="-80" y="38" fill="#0284c7" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">+ H₂O</text>

      <!-- Flecha vertical hacia UREA -->
      <line x1="0" y1="120" x2="0" y2="-90" stroke="#dc2626" stroke-width="2.8" marker-end="url(#arrowRed)"/>

      <!-- Flecha curva hacia la derecha hacia Ornitina citosólica (X=4700) -->
      <path d="M 0 50 Q 75 50 140 25" fill="none" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowTeal)"/>
      <text x="45" y="24" fill="#0f766e" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">➔ Retorno Ornitina</text>

      <!-- Metadatos de ARG1 (lado izquierdo) -->
      <g transform="translate(-20, -10)">
        <text x="0" y="-15" fill="#0f172a" font-size="12.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Arginasa 1 (ARG1)</text>
        <text x="0" y="-2" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 3.5.3.1 (Mn²⁺)</text>
        <text x="0" y="11" fill="#15803d" font-size="9.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">Hidrólisis terminal hepática</text>
      </g>
    </g>
    ''')

    # 10. L-Ornitina Citosólica (Regenerada, X=4700, Y=960)
    partes.append(nodo_libre(
        4570, 810,
        "L-Ornitina (Citosol)", "5C",
        UREA_ORNITINA, "m_u_ornitina_cito",
        text_right=True, dx=110,
        detalle="Regenerada tras hidrólisis"
    ))

    # Canal de retorno de Ornitina hacia ORNT1
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="canal_retorno_ornitina" data-arrastrable="1">
          <path d="M {x_u_r} 910 L {x_u_r} 2140" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-dasharray="8 5" marker-end="url(#arrowBlueAmino)"/>
          <path d="M {x_u_r} 2180 L {x_u_r} 2850" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-dasharray="8 5" marker-end="url(#arrowBlueAmino)"/>
          <g transform="translate({x_u_r}, 1600)">
            <rect x="-85" y="-12" width="170" height="24" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.2"/>
            <text x="0" y="4" fill="#1d4ed8" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">↓ ORNT1 (SLC25A15)</text>
          </g>
        </g>
        ''')

    # 11. UREA (Carbamida) - Producto final de desecho (X=4420, Y=780)
    partes.append(nodo_libre(
        x_u_c - 30, 630,
        "UREA (Carbamida)", "1C",
        UREA_MOL, "m_u_urea",
        text_right=True, dx=110,
        detalle="Diamida neutra no tóxica (2 nitrógenos)"
    ))

    # 12. Excreción directa de Urea al torrente sanguíneo superior
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="excrecion_urea_sangre" data-arrastrable="1">
          <path d="M {x_u_c} 600 L {x_u_c} 74" fill="none" stroke="#dc2626" stroke-width="3.2" stroke-dasharray="8 4" marker-end="url(#arrowRed)"/>
          <text x="{x_u_c + 18}" y="380" fill="#b91c1c" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 {x_u_c + 18} 380)">➔ EXCRECIÓN DE UREA AL TORRENTE SANGUÍNEO HEPÁTICO (➔ RIÑÓN)</text>

          <!-- Biomarcador vascular en el capilar superior -->
          <ellipse cx="{x_u_c}" cy="38" rx="26" ry="16" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
          <text x="{x_u_c}" y="42" fill="#dc2626" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">UREA</text>
          <text x="{x_u_c}" y="60" fill="#fca5a5" font-size="7.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Excreción</text>
        </g>
        ''')

    partes.append(f'</g>')

