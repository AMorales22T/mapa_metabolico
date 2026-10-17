# =============================================================================
# MÓDULO DE REVISIÓN: Vía 8B: Lupa de la Lanzadera de Glicerol-3-Fosfato
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 3602 a 3715 de 4188)
# Descripción      : Detalle anatómico de cGPDH citosólica y mGPDH dependiente de FAD en la cara externa de la MMI.
# =============================================================================

    # =========================================================================
    # 17. RUTA 8B: LANZADERA DE GLICEROL-3-FOSFATO (G-3-P / DHAP) - LUPA ANATÓMICA
    # =========================================================================
    partes.append(f'<g id="lupa_lanzadera_glicerol_p" data-arrastrable="1">')
    
    y_lanz = 2950
    x_g3p_marco = 4980
    y_g3p_marco = y_lanz - 25
    w_g3p_marco = 810
    h_g3p_marco = 440

    # 1. Bisel y Marco Panorámico de Zoom para Lanzadera Glicerol-P
    partes.append(f'''
    <rect x="{x_g3p_marco - 5}" y="{y_g3p_marco - 5}" width="{w_g3p_marco + 10}" height="{h_g3p_marco + 10}" rx="24" fill="#ffffff" stroke="#ea580c" stroke-width="4"/>
    <rect x="{x_g3p_marco}" y="{y_g3p_marco}" width="{w_g3p_marco}" height="{h_g3p_marco}" rx="20" fill="#ffffff" stroke="#fb923c" stroke-width="1.8" stroke-dasharray="8 4"/>

    <!-- ClipPath para recortar el interior del marco de la lupa -->
    <defs>
      <clipPath id="clipLupaG3P">
        <rect x="{x_g3p_marco}" y="{y_g3p_marco}" width="{w_g3p_marco}" height="{h_g3p_marco}" rx="20"/>
      </clipPath>
    </defs>

    <!-- 2. Estratificación Biológica de Compartimentos Celulares -->
    <g clip-path="url(#clipLupaG3P)">
      <!-- Zona 1: Citosol Celular -->
      <rect x="{x_g3p_marco}" y="{y_g3p_marco}" width="390" height="{h_g3p_marco}" fill="#f8fafc"/>

      <!-- Zona 2: Membrana Mitocondrial Externa (MME con VDAC) -->
      <rect x="{x_g3p_marco + 390}" y="{y_g3p_marco}" width="80" height="{h_g3p_marco}" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.4"/>

      <!-- Zona 3: Espacio Intermembrana (EIM) -->
      <rect x="{x_g3p_marco + 470}" y="{y_g3p_marco}" width="70" height="{h_g3p_marco}" fill="#fff7ed" stroke="#fed7aa" stroke-width="1" stroke-dasharray="4 2"/>

      <!-- Zona 4: Membrana Mitocondrial Interna (MMI) - Cara Externa -->
      <rect x="{x_g3p_marco + 540}" y="{y_g3p_marco}" width="{w_g3p_marco - 540}" height="{h_g3p_marco}" fill="#fef3c7" fill-opacity="0.5" stroke="#ea580c" stroke-width="2"/>

      <!-- Rótulos de Compartimentos en la Cabecera Interna -->
      <g opacity="0.85">
        <text x="{x_g3p_marco + 195}" y="{y_g3p_marco + 20}" fill="#64748b" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="1">CITOSOL CELULAR</text>
        <text x="{x_g3p_marco + 430}" y="{y_g3p_marco + 20}" fill="#475569" font-size="8.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="0.5">MME</text>
        <text x="{x_g3p_marco + 505}" y="{y_g3p_marco + 20}" fill="#c2410c" font-size="8.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="0.5">EIM</text>
        <text x="{x_g3p_marco + 675}" y="{y_g3p_marco + 20}" fill="#9a3412" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" letter-spacing="1">MMI (CARA EXTERNA)</text>
      </g>
    </g>
    ''')

    partes.append(badge_via("8B", x_nuc - 35, y_lanz + 15))
    partes.append(f'''
    <g transform="translate({x_nuc + 5}, {y_lanz + 15})" data-arrastrable="1">
      <text x="0" y="0" fill="#0f172a" font-size="15" font-weight="900" font-family="'Inter', sans-serif">LANZADERA DE GLICEROL-3-FOSFATO (VÍA 8B)</text>
      <text x="0" y="15" fill="#ea580c" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">Inserto Anatómico de Envoltura Mitocondrial • Reoxidación de NADH (1.5 ATP)</text>
    </g>
    ''')

    # Enlace hacia Glucólisis
    if MOSTRAR_CONEXIONES_INTER_RUTA:
        partes.append(f'''
        <g id="conexion_glucolisis_lanz_g3p" data-arrastrable="1">
          <path d="M 1430 920 C 1430 1800, 4800 3050, 5120 3050" fill="none" stroke="#ea580c" stroke-width="2.4" stroke-dasharray="8 5" marker-end="url(#arrowFlow)"/>
        </g>
        ''')
    partes.append(f'''
    <text x="{x_nuc + 20}" y="{y_lanz + 55}" fill="#ea580c" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">➔ de DHAP (Glucólisis Citosólica)</text>
    ''')

    partes.append(nodo_libre(x_nuc + 20, y_lanz + 70, "Dihidroxiacetona-P (DHAP)", "3C", DIHIDROXIACETONA_FOSFATO, "m_lanz_dhap", dx=120, detalle="Aceptor citosólico de electrones"))
    partes.append(reaccion_libre(x_nuc + 75, y_lanz + 185, 45, "cGPDH Citosólica (GPD1)", entra="- NADH + H⁺", sale="+ NAD⁺ (Regenerado)", id_rx="rx_cgpdh"))
    partes.append(nodo_libre(x_nuc + 20, y_lanz + 250, "L-Glicerol-3-Fosfato", "3C", LANZ_G3P, "m_lanz_g3p", dx=100, detalle="Transporta electrones a la MMI"))

    # Cruce VDAC y mGPDH flavoproteína
    partes.append(f'''
    <g id="lanz_mgpdh_mmi" transform="translate({x_nuc + 260}, {y_lanz + 150})" data-arrastrable="1">
      <!-- Porina VDAC en MME -->
      <g transform="translate(10, 42)">
        <rect x="0" y="0" width="46" height="34" rx="7" fill="#cbd5e1" stroke="#475569" stroke-width="1.8"/>
        <text x="23" y="15" fill="#1e293b" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">VDAC</text>
        <text x="23" y="27" fill="#475569" font-size="7.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">Porina MME</text>
      </g>

      <!-- Proteína integral mGPDH anclada a MMI -->
      <g transform="translate(75, 30)">
        <path d="M 0,0 Q 40,-15 50,40 Q 55,90 15,80 Q 0,55 0,25 Z" fill="#fed7aa" stroke="#c2410c" stroke-width="2"/>
        <circle cx="20" cy="40" r="10" fill="#ffedd5" stroke="#ea580c" stroke-width="1.6"/>
        <text x="20" y="43" fill="#9a3412" font-size="7.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">FAD</text>
        <text x="56" y="20" fill="#0f172a" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">mGPDH (GPD2)</text>
        <text x="56" y="32" fill="#9a3412" font-size="8" font-weight="800" font-family="'Inter', sans-serif">Flavoproteína</text>
      </g>

      <!-- Flujo de G-3-P a mGPDH (pasa limpio por debajo de VDAC) -->
      <path d="M 15 110 C 35 110, 55 98, 75 75" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>

      <!-- Retorno de DHAP al citosol (pasa limpio por encima de VDAC) -->
      <path d="M 75 14 C 45 8, 15 8, -15 8" fill="none" stroke="#ea580c" stroke-width="2.2" stroke-dasharray="5 3" marker-end="url(#arrowFlow)"/>
      <text x="30" y="2" fill="#64748b" font-size="8" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Retorno DHAP ➔ Citosol</text>

      <!-- Coenzima Q y Complejo III -->
      <path d="M 135 70 Q 165 70 195 70" fill="none" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arrowBlue)"/>
      <g transform="translate(204, 54)">
        <rect x="0" y="0" width="76" height="30" rx="6" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
        <text x="38" y="13" fill="#0369a1" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">CoQ ➔ CoQH₂</text>
        <text x="38" y="23" fill="#0284c7" font-size="7" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">Ubiquinona</text>
      </g>
      <path d="M 284 69 L 298 69" fill="none" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arrowBlue)"/>
      <g transform="translate(302, 54)">
        <rect x="0" y="0" width="84" height="30" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
        <text x="42" y="13" fill="#15803d" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">COMPLEJO III</text>
        <text x="42" y="23" fill="#16a34a" font-size="7" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">➔ 1.5 ATP neto</text>
      </g>
    </g>
    ''')

    partes.append(f'</g>')

