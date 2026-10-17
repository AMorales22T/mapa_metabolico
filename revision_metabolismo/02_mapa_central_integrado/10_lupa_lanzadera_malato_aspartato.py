# =============================================================================
# MÓDULO DE REVISIÓN: Vía 8A: Lupa de la Lanzadera Malato-Aspartato
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 1829 a 2027 de 4188)
# Descripción      : Panel técnico con antiporter OGC, antiporter Aralar/AGC, cMDH, mMDH, AST1 y AST2.
# =============================================================================

    # =========================================================================
    # 6. LANZADERA MALATO-ASPARTATO: PANEL TÉCNICO REGULATORIO
    # =========================================================================
    cx_lupa = 1026
    cy_lupa = 1544
    r_lupa = 310
    x_ancla_mmi = 1026
    y_ancla_mmi = y_mito - 16

    partes.append(badge_via(8, 956, y_ancla_mmi - 25))
    partes.append(f"""
    <!-- ================================================================= -->
    <!-- PANEL TÉCNICO: LANZADERA MALATO-ASPARTATO                         -->
    <!-- ================================================================= -->
    <g id="lupa_lanzadera_malato_aspartato" data-arrastrable="1">

      <!-- 1. Punto de Anclaje sobre la Membrana Mitocondrial Real -->
      <g id="ancla_lanzadera_mmi" transform="translate({x_ancla_mmi}, {y_ancla_mmi})">
        <rect x="-55" y="-18" width="110" height="36" rx="8" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
        <text x="0" y="5" fill="#ffffff" font-size="13" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">OGC / AGC</text>
        <text x="0" y="34" fill="#78350f" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Lanzadera Malato-Aspartato</text>
      </g>

      <!-- 2. Cuerpo y Bisel del Panel Técnico -->
      <rect x="{cx_lupa - r_lupa}" y="{cy_lupa - r_lupa}" width="{r_lupa * 2}" height="{r_lupa * 2}" rx="18" fill="#ffffff" stroke="#0284c7" stroke-width="2.5"/>

      <!-- ClipPath para recortar el interior del panel -->
      <defs>
        <clipPath id="clipLupaLanzadera">
          <rect x="{cx_lupa - r_lupa}" y="{cy_lupa - r_lupa}" width="{r_lupa * 2}" height="{r_lupa * 2}" rx="18"/>
        </clipPath>
      </defs>

      <!-- 4. Contenido Interior con Ciclo Cerrado, 5 Estructuras y Flechas Punteadas -->
      <g clip-path="url(#clipLupaLanzadera)">
        <!-- Fondo CITOPLASMA (Mitad Superior en Verde Suave) -->
        <rect x="{cx_lupa - r_lupa - 10}" y="{cy_lupa - r_lupa - 10}" width="{r_lupa * 2 + 20}" height="{r_lupa + 10}" fill="#f0fdf4"/>

        <!-- Fondo MATRIZ MITOCONDRIAL (Mitad Inferior en Ámbar Suave) -->
        <rect x="{cx_lupa - r_lupa - 10}" y="{cy_lupa}" width="{r_lupa * 2 + 20}" height="{r_lupa + 10}" fill="#fffbeb"/>

        <!-- Bicapa MMI transversal divisoria en la lupa -->
        <rect x="{cx_lupa - r_lupa - 10}" y="{cy_lupa - 20}" width="{r_lupa * 2 + 20}" height="40" fill="#fed7aa" stroke="#d97706" stroke-width="2.5"/>
        <text x="{cx_lupa}" y="{cy_lupa + 4}" fill="#92400e" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MMI (BICAPA INTERNA)</text>

        <!-- Cabezas de fosfolípidos en MMI -->
        <g fill="#d97706" opacity="0.6">
          <circle cx="{cx_lupa - 290}" cy="{cy_lupa - 14}" r="2.6"/><circle cx="{cx_lupa - 275}" cy="{cy_lupa - 14}" r="2.6"/>
          <circle cx="{cx_lupa - 290}" cy="{cy_lupa + 14}" r="2.6"/><circle cx="{cx_lupa - 275}" cy="{cy_lupa + 14}" r="2.6"/>
          <circle cx="{cx_lupa + 275}" cy="{cy_lupa - 14}" r="2.6"/><circle cx="{cx_lupa + 290}" cy="{cy_lupa - 14}" r="2.6"/>
          <circle cx="{cx_lupa + 275}" cy="{cy_lupa + 14}" r="2.6"/><circle cx="{cx_lupa + 290}" cy="{cy_lupa + 14}" r="2.6"/>
        </g>

        <!-- Transportador Izquierdo: SLC25A12 (Aralar / AGC1) -->
        <g transform="translate({cx_lupa - 220}, {cy_lupa - 24})">
          <rect x="-38" y="0" width="76" height="48" rx="10" fill="#ec4899" stroke="#db2777" stroke-width="2"/>
          <text x="0" y="19" fill="#831843" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">Aralar</text>
          <text x="0" y="35" fill="#9d174d" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Asp⁻ ⇄ Glu⁻</text>
        </g>

        <!-- Transportador Derecho: SLC25A11 (OGC) -->
        <g transform="translate({cx_lupa + 220}, {cy_lupa - 24})">
          <rect x="-38" y="0" width="76" height="48" rx="10" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
          <text x="0" y="19" fill="#78350f" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">OGC</text>
          <text x="0" y="35" fill="#92400e" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Mal²⁻ ⇄ α-KG²⁻</text>
        </g>

        <!-- =========================================================== -->
        <!-- ZONA 1: CITOPLASMA (ARRIBA) - GOT1 Y cMDH                   -->
        <!-- =========================================================== -->
        <g transform="translate({cx_lupa}, {cy_lupa - 282})">
          <rect x="-220" y="-12" width="440" height="24" rx="12" fill="#f1f5f9" stroke="#0284c7" stroke-width="1.6"/>
          <text x="0" y="4" fill="#0369a1" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="0.8">
            CITOSOL: GOT1 / cAST (TRANSAMINACIÓN) &amp; cMDH (REDUCCIÓN)
          </text>
        </g>

        <!-- Estructura Citosólica 1 (Izquierda): L-Aspartato (Citosol) -->
        <g transform="translate({cx_lupa - 245}, {cy_lupa - 252})">
          <g transform="scale(0.60)">{LANZ_ASP}</g>
          <text x="24" y="86" fill="#831843" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Aspartato</text>
          <text x="24" y="98" fill="#db2777" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Citosol</text>
        </g>

        <!-- Reacción 1 (Izquierda ➔ Centro): GOT1 / cAST (Punteada) -->
        <g transform="translate({cx_lupa - 185}, {cy_lupa - 212})">
          <line x1="0" y1="0" x2="142" y2="0" stroke="#db2777" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowRed)"/>
          <text x="71" y="-10" fill="#be123c" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">GOT1 (cAST)</text>
          <text x="71" y="15" fill="#64748b" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">+ α-KG ➔ + L-Glu</text>
        </g>

        <!-- Estructura Citosólica 2 (Centro): Oxalacetato (Citosol) -->
        <g transform="translate({cx_lupa - 24}, {cy_lupa - 252})">
          <g transform="scale(0.60)">{LANZ_OAA}</g>
          <text x="24" y="86" fill="#0f172a" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Oxalacetato</text>
          <text x="24" y="98" fill="#ea580c" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Citosol</text>
        </g>

        <!-- Reacción 2 (Centro ➔ Derecha): cMDH (Punteada) -->
        <g transform="translate({cx_lupa + 38}, {cy_lupa - 212})">
          <line x1="0" y1="0" x2="146" y2="0" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
          <text x="73" y="-10" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">cMDH</text>
          <path d="M 12 10 Q 73 28 134 10" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
          <text x="73" y="34" fill="#dc2626" font-size="9" font-weight="800" text-anchor="middle">- NADH + H⁺ ➔ + NAD⁺</text>
          <text x="73" y="45" fill="#047857" font-size="8" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">(regenera NAD⁺ p/ Glucólisis)</text>
        </g>

        <!-- Estructura Citosólica 3 (Derecha): L-Malato (Citosol) -->
        <g transform="translate({cx_lupa + 196}, {cy_lupa - 252})">
          <g transform="scale(0.60)">{LANZ_MALATO}</g>
          <text x="24" y="86" fill="#0f172a" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Malato</text>
          <text x="24" y="98" fill="#0284c7" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Citosol</text>
        </g>

        <!-- =========================================================== -->
        <!-- SUB-CICLO CENTRAL DE ANTIPUERTO: L-GLUTAMATO Y α-KG         -->
        <!-- =========================================================== -->
        <!-- Estructura acoplada: L-Glutamato [5C] -->
        <g transform="translate({cx_lupa - 148}, {cy_lupa - 134})">
          <g transform="scale(0.48)">{LANZ_GLU}</g>
          <text x="48" y="28" fill="#9d174d" font-size="9" font-weight="800" font-family="'Inter', sans-serif">L-Glutamato</text>
          <text x="48" y="40" fill="#be185d" font-size="8" font-weight="700" font-family="'JetBrains Mono', monospace">[5C] (entra a matriz)</text>
        </g>
        <!-- Flecha punteada de L-Glutamato bajando hacia GOT2 (cruza MMI en hueco libre cx-115) -->
        <path d="M {cx_lupa - 115} {cy_lupa - 62} L {cx_lupa - 115} {cy_lupa + 84}" fill="none" stroke="#be185d" stroke-width="1.9" stroke-dasharray="5 3" marker-end="url(#arrowRed)"/>

        <!-- Estructura acoplada: α-Cetoglutarato [5C] -->
        <g transform="translate({cx_lupa + 32}, {cy_lupa - 134})">
          <g transform="scale(0.48)">{LANZ_AKG}</g>
          <text x="44" y="28" fill="#92400e" font-size="9" font-weight="800" font-family="'Inter', sans-serif">α-Cetoglutarato</text>
          <text x="44" y="40" fill="#d97706" font-size="8" font-weight="700" font-family="'JetBrains Mono', monospace">[5C] (sale a citosol)</text>
        </g>
        <!-- Flecha punteada de α-KG subiendo desde GOT2 hacia GOT1 (pasa en cy+42 sobre OAA y cruza MMI en cx+95) -->
        <path d="M {cx_lupa - 85} {cy_lupa + 84} L {cx_lupa - 85} {cy_lupa + 42} L {cx_lupa + 95} {cy_lupa + 42} L {cx_lupa + 95} {cy_lupa - 62}" fill="none" stroke="#d97706" stroke-width="1.9" stroke-dasharray="5 3" marker-end="url(#arrowFlow)"/>

        <!-- =========================================================== -->
        <!-- FLECHAS VERTICALES DE TRANSPORTE TRANSMEMBRANA (PUNTEADAS)  -->
        <!-- =========================================================== -->
        <!-- Derecha: L-Malato baja desde el citosol, entra a OGC y sale hacia la matriz -->
        <path d="M {cx_lupa + 220} {cy_lupa - 144} L {cx_lupa + 220} {cy_lupa - 28}" fill="none" stroke="#0284c7" stroke-width="2.8" stroke-dasharray="6 4" marker-end="url(#arrowBlue)"/>
        <path d="M {cx_lupa + 220} {cy_lupa + 26} L {cx_lupa + 220} {cy_lupa + 58}" fill="none" stroke="#0284c7" stroke-width="2.8" stroke-dasharray="6 4" marker-end="url(#arrowBlue)"/>
        <text x="{cx_lupa + 206}" y="{cy_lupa - 44}" fill="#0284c7" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">Malato²⁻ ↓</text>

        <!-- Izquierda: L-Aspartato sube desde la matriz, entra a Aralar y retorna al citosol -->
        <path d="M {cx_lupa - 220} {cy_lupa + 58} L {cx_lupa - 220} {cy_lupa + 28}" fill="none" stroke="#db2777" stroke-width="2.8" stroke-dasharray="6 4" marker-end="url(#arrowRed)"/>
        <path d="M {cx_lupa - 220} {cy_lupa - 26} L {cx_lupa - 220} {cy_lupa - 144}" fill="none" stroke="#db2777" stroke-width="2.8" stroke-dasharray="6 4" marker-end="url(#arrowRed)"/>
        <text x="{cx_lupa - 206}" y="{cy_lupa - 44}" fill="#db2777" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="start">↑ Aspartato</text>

        <!-- =========================================================== -->
        <!-- ZONA 2: MATRIZ MITOCONDRIAL (ABAJO) - mMDH Y GOT2           -->
        <!-- =========================================================== -->
        <!-- Estructura Matricial 1 (Derecha): L-Malato (Matriz) -->
        <g transform="translate({cx_lupa + 196}, {cy_lupa + 66})">
          <g transform="scale(0.60)">{LANZ_MALATO}</g>
          <text x="24" y="86" fill="#0f172a" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Malato (Matriz)</text>
          <text x="24" y="98" fill="#0284c7" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Pool Krebs</text>
        </g>

        <!-- Reacción 3 (Derecha ➔ Centro): mMDH (Punteada hacia la izquierda) -->
        <g transform="translate({cx_lupa + 184}, {cy_lupa + 106})">
          <line x1="0" y1="0" x2="-146" y2="0" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="6 4" marker-end="url(#arrowFlow)"/>
          <text x="-73" y="-10" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">mMDH</text>
          <path d="M -12 10 Q -73 28 -134 10" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
          <text x="-73" y="34" fill="#059669" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">+ NAD⁺ ➔ + NADH + H⁺</text>
          <text x="-73" y="46" fill="#047857" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">➔ Complejo I (2.5 ATP)</text>
        </g>

        <!-- Estructura Matricial 2 (Centro): Oxalacetato (Matriz) -->
        <g transform="translate({cx_lupa - 24}, {cy_lupa + 66})">
          <g transform="scale(0.60)">{LANZ_OAA}</g>
          <text x="24" y="86" fill="#0f172a" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Oxalacetato</text>
          <text x="24" y="98" fill="#ea580c" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Matriz</text>
        </g>

        <!-- Reacción 4 (Centro ➔ Izquierda): GOT2 / mAST (Punteada hacia la izquierda) -->
        <g transform="translate({cx_lupa - 43}, {cy_lupa + 106})">
          <line x1="0" y1="0" x2="-142" y2="0" stroke="#db2777" stroke-width="2.4" stroke-dasharray="6 4" marker-end="url(#arrowRed)"/>
          <text x="-71" y="-10" fill="#be123c" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">GOT2 (mAST)</text>
          <text x="-71" y="15" fill="#64748b" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">+ L-Glu ➔ + α-KG</text>
        </g>

        <!-- Estructura Matricial 3 (Izquierda): L-Aspartato (Matriz) -->
        <g transform="translate({cx_lupa - 245}, {cy_lupa + 66})">
          <g transform="scale(0.60)">{LANZ_ASP}</g>
          <text x="24" y="86" fill="#831843" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Aspartato</text>
          <text x="24" y="98" fill="#db2777" font-size="8.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[4C] Matriz</text>
        </g>

        <!-- Banner Explicativo Inferior -->
        <g transform="translate({cx_lupa}, {cy_lupa + 268})">
          <rect x="-215" y="-13" width="430" height="26" rx="13" fill="#0f172a" opacity="0.95"/>
          <text x="0" y="4" fill="#ffffff" font-size="11" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
            LANZADERA MALATO-ASPARTATO (CICLO CERRADO)
          </text>
        </g>
      </g>
    </g>
    """)

