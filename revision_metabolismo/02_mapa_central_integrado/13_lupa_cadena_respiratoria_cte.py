# =============================================================================
# MÓDULO DE REVISIÓN: Vía 7: Lupa de la Cadena Respiratoria y ATP Sintasa
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 2386 a 2467 de 4188)
# Descripción      : Inserción y escalado de los Complejos I-IV, ubiquinona, citocromo c y F0F1-ATP sintasa.
# =============================================================================

    # =========================================================================
    # 8. MATRIZ DERECHA: CADENA RESPIRATORIA REAL DEL USUARIO (CON ZOOM)
    # =========================================================================
    cte_defs, cte_body = cargar_cte_original_usuario()

    x_ancla_cresta = 2633
    y_ancla_cresta = y_mito + 25

    x_cte_marco = 2553
    y_cte_marco = 2440
    w_cte_marco = 1190
    h_cte_marco = 820

    partes.append(badge_via(7, x_ancla_cresta - 95, y_ancla_cresta - 5))
    partes.append(f"""
    <!-- ================================================================= -->
    <!-- CADENA DE TRANSPORTE DE ELECTRONES Y ATP SINTASA                  -->
    <!-- ================================================================= -->
    <g id="lupa_cadena_respiratoria" data-arrastrable="1">

      <!-- 1. Punto de Anclaje sobre la Cresta Mitocondrial Real -->
      <g id="ancla_cresta_mmi" transform="translate({x_ancla_cresta}, {y_ancla_cresta})">
        <rect x="-65" y="-18" width="130" height="36" rx="10" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
        <text x="0" y="5" fill="#ffffff" font-size="12.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">CRESTA MMI</text>
        <text x="0" y="34" fill="#78350f" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Cresta Respiratoria: Complejos I–IV &amp; F₀F₁</text>
      </g>

      <!-- 4. Cuerpo y Bisel de la Lente Panorámica de Zoom -->
      <rect x="{x_cte_marco - 6}" y="{y_cte_marco - 6}" width="{w_cte_marco + 12}" height="{h_cte_marco + 12}" rx="28" fill="#ffffff" stroke="#0284c7" stroke-width="6"/>
      <rect x="{x_cte_marco}" y="{y_cte_marco}" width="{w_cte_marco}" height="{h_cte_marco}" rx="24" fill="none" stroke="#38bdf8" stroke-width="2.2" stroke-dasharray="8 4"/>

      <!-- ClipPath para recortar el interior panorámico -->
      <defs>
        <clipPath id="clipLupaCTE">
          <rect x="{x_cte_marco}" y="{y_cte_marco}" width="{w_cte_marco}" height="{h_cte_marco}" rx="24"/>
        </clipPath>
      </defs>

      <!-- 5. Contenido Real Exacto del archivo del usuario: Cadena_Transporte_Electrones.svg -->
      <g clip-path="url(#clipLupaCTE)">
        <g transform="translate({x_cte_marco + 20}, {y_cte_marco + 10})">
          {cte_body}

          <!-- Figuritas moleculares vectoriales añadidas sobre el diseño del usuario con espaciado óptimo -->
          <!-- 1. Estructura real de NADH entrando a Complejo I -->
          <g transform="translate(75, 690) scale(0.48)">
            {CTE_NADH}
          </g>

          <!-- 2. Estructura real de FADH2 entrando a Complejo II -->
          <g transform="translate(275, 690) scale(0.48)">
            {CTE_FADH2}
          </g>

          <!-- 3. Estructura real de Ubiquinona debajo de los títulos de MMI/Matriz (sin amontonar) -->
          <g transform="translate(375, 520) scale(0.46)">
            {UBIQUINONA}
          </g>

          <!-- 4. Estructura real de Citocromo c en el EIM (zona libre superior) -->
          <g transform="translate(605, 175) scale(0.44)">
            {CITOCROMO_C}
          </g>

          <!-- 5. Estructuras de Oxígeno y Agua en Complejo IV -->
          <g transform="translate(660, 560) scale(0.48)">
            {OXIGENO}
          </g>
          <g transform="translate(740, 560) scale(0.48)">
            {AGUA}
          </g>
        </g>

        <!-- Badge Identificador Inferior -->
        <rect x="{x_cte_marco + w_cte_marco//2 - 350}" y="{y_cte_marco + h_cte_marco - 34}" width="700" height="28" rx="14" fill="#0f172a" opacity="0.95"/>
        <text x="{x_cte_marco + w_cte_marco//2}" y="{y_cte_marco + h_cte_marco - 16}" fill="#ffffff" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
          CADENA DE TRANSPORTE DE ELECTRONES Y ATP SINTASA
        </text>
      </g>
    </g>
    """)

