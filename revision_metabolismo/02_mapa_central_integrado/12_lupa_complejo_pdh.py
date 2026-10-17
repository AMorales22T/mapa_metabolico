# =============================================================================
# MÓDULO DE REVISIÓN: Vía 5: Lupa del Complejo Piruvato Deshidrogenasa (PDH)
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 2136 a 2385 de 4188)
# Descripción      : Detalle de E1, E2, E3, 5 cofactores y regulación por cinasa PDK y fosfatasa PDP.
# =============================================================================

    # =========================================================================
    # 7B. COMPLEJO PIRUVATO DESHIDROGENASA (PDH) - VÍA 5
    # =========================================================================
    # Marco panorámico rectangular con bisel cian (idéntico a la Lupa de la CTE)
    # Ubicado en la zona matricial media-inferior: X=1460, Y=3440, W=800, H=700
    x_pdh_marco = 1460
    y_pdh_marco = 3440
    w_pdh_marco = 800
    h_pdh_marco = 700

    partes.append(f"""
    <!-- ================================================================= -->
    <!-- PANEL DETALLADO: COMPLEJO PIRUVATO DESHIDROGENASA (PDH)           -->
    <!-- ================================================================= -->
    <g id="lupa_piruvato_deshidrogenasa" data-arrastrable="1">

      <!-- 2. Cuerpo y Bisel de la Lente Panorámica de Zoom (Estilo CTE) -->
      <rect x="{x_pdh_marco - 6}" y="{y_pdh_marco - 6}" width="{w_pdh_marco + 12}" height="{h_pdh_marco + 12}" rx="24" fill="#ffffff" stroke="#0284c7" stroke-width="5"/>
      <rect x="{x_pdh_marco}" y="{y_pdh_marco}" width="{w_pdh_marco}" height="{h_pdh_marco}" rx="20" fill="#ffffff" stroke="#38bdf8" stroke-width="2" stroke-dasharray="8 4"/>

      <!-- ClipPath para recortar el interior panorámico -->
      <defs>
        <clipPath id="clipLupaPDH">
          <rect x="{x_pdh_marco}" y="{y_pdh_marco}" width="{w_pdh_marco}" height="{h_pdh_marco}" rx="20"/>
        </clipPath>
      </defs>

      <!-- 3. Contenido Interior con Aumento: Mecanismo + Regulación + Toxicología -->
      <g clip-path="url(#clipLupaPDH)">
        <!-- Fondo cálido de matriz ampliada -->
        <rect x="{x_pdh_marco}" y="{y_pdh_marco}" width="{w_pdh_marco}" height="{h_pdh_marco}" fill="#fffdf7"/>

        <g transform="translate({x_pdh_marco + 20}, {y_pdh_marco + 15})">
          <!-- Cabecera Interior de la Lupa -->
          <g transform="translate(0, 8)">
            <rect x="0" y="0" width="32" height="26" rx="6" fill="#ea580c"/>
            <text x="16" y="18" fill="#ffffff" font-size="14" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">5</text>
            <text x="42" y="17" fill="#0f172a" font-size="14.5" font-weight="900" font-family="'Inter', sans-serif">COMPLEJO PIRUVATO DESHIDROGENASA (PDH)</text>
            <text x="42" y="31" fill="#ea580c" font-size="9.5" font-weight="700" font-family="'Inter', sans-serif">Detalle en alta resolución de la reacción: Piruvato ➔ Acetil-CoA (Entrada MPC superior)</text>
          </g>

          <!-- Línea divisoria vertical entre mecanismo (izq) y regulación (der) -->
          <line x1="385" y1="50" x2="385" y2="665" stroke="#e2e8f0" stroke-width="1.5" stroke-dasharray="4 4"/>

          <!-- =========================================================== -->
          <!-- COLUMNA IZQUIERDA: MECANISMO CATALÍTICO PASO A PASO         -->
          <!-- =========================================================== -->
          <g transform="translate(0, 52)">
            <text x="0" y="10" fill="#c2410c" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">I. MECANISMO CATALÍTICO CON ESTRUCTURAS QUÍMICAS</text>

            <!-- 1. Piruvato (Sustrato 3C) -->
            <g transform="translate(55, 16)">
              <rect x="0" y="0" width="128" height="44" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1.4"/>
              <g transform="translate(8, 2) scale(0.40)">
                {PIRUVATO}
              </g>
              <text x="136" y="17" fill="#9a3412" font-size="10.5" font-weight="900" font-family="'Inter', sans-serif">1. Piruvato (3C)</text>
              <text x="136" y="30" fill="#64748b" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">α-Cetoácido alimentador</text>
            </g>

            <!-- PASO 1: E1 Piruvato Deshidrogenasa (TPP) -->
            <path d="M 118 62 L 118 98" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
            <path d="M 114 78 Q 82 86 58 86" fill="none" stroke="#dc2626" stroke-width="1.7" marker-end="url(#arrowRed)"/>
            <text x="53" y="90" fill="#dc2626" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">+ CO₂ ↑</text>
            <g transform="translate(130, 72)">
              <text x="0" y="0" fill="#0f172a" font-size="10" font-weight="900" font-family="'Inter', sans-serif">Paso 1 — E₁: Piruvato DH (TPP)</text>
              <text x="0" y="12" fill="#ea580c" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Descarboxilación: carbanión TPP ataca C=O</text>
            </g>

            <!-- 2. Hidroxietil-TPP (Intermediario E1) -->
            <g transform="translate(48, 100)">
              <rect x="0" y="0" width="142" height="44" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.3"/>
              <g transform="translate(6, 2) scale(0.42)">
                {PDH_HIDROXIETIL_TPP}
              </g>
              <text x="150" y="17" fill="#1e293b" font-size="10" font-weight="900" font-family="'Inter', sans-serif">2. Hidroxietil-TPP (E₁)</text>
              <text x="150" y="30" fill="#64748b" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Unidad 2C activa unida a B₁</text>
            </g>

            <!-- PASO 2A: E2 Dihidrolipoil Transacetilasa (Oxidación y transferencia al brazo lipoilo) -->
            <path d="M 118 146 L 118 182" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
            <path d="M 68 160 Q 94 160 114 168" fill="none" stroke="#d97706" stroke-width="1.7" marker-end="url(#arrowAmber)"/>
            <text x="64" y="164" fill="#b45309" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ Lipoamida</text>
            <g transform="translate(130, 158)">
              <text x="0" y="0" fill="#0f172a" font-size="10" font-weight="900" font-family="'Inter', sans-serif">Paso 2a — E₂: Oxidación (Brazo 14 Å)</text>
              <text x="0" y="12" fill="#64748b" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Abre puente S–S y forma tioéster de alta E</text>
            </g>

            <!-- 3. Acetil-Lipoamida (Intermediario E2) -->
            <g transform="translate(42, 184)">
              <rect x="0" y="0" width="154" height="44" rx="6" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.3"/>
              <g transform="translate(6, 2) scale(0.42)">
                {PDH_ACETIL_LIPOAMIDA}
              </g>
              <text x="162" y="17" fill="#92400e" font-size="10" font-weight="900" font-family="'Inter', sans-serif">3. Acetil-Lipoamida (E₂)</text>
              <text x="162" y="30" fill="#b45309" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Tioéster (~S–C=O) en Lys-E₂</text>
            </g>

            <!-- PASO 2B: E2 Transacetilación a CoA-SH -->
            <path d="M 118 230 L 118 268" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
            <path d="M 68 242 Q 94 242 114 250" fill="none" stroke="#7c3aed" stroke-width="1.7" marker-end="url(#arrowPurple)"/>
            <text x="64" y="246" fill="#7c3aed" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">+ CoA-SH</text>
            <path d="M 122 252 Q 152 260 178 260" fill="none" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
            <text x="184" y="253" fill="#ea580c" font-size="10" font-weight="900" font-family="'Inter', sans-serif">➔ Acetil-CoA (2C)</text>
            <text x="184" y="264" fill="#0f172a" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">Paso 2b: Transesterificación</text>

            <!-- 4. Dihidrolipoamida reducida (-SH HS-) -->
            <g transform="translate(42, 270)">
              <rect x="0" y="0" width="154" height="44" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.3"/>
              <g transform="translate(6, 2) scale(0.42)">
                {PDH_DIHIDROLIPOAMIDA}
              </g>
              <text x="162" y="17" fill="#991b1b" font-size="10" font-weight="900" font-family="'Inter', sans-serif">4. Dihidrolipoamida (E₂)</text>
              <text x="162" y="30" fill="#b91c1c" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Ditiol reducido (–SH HS–)</text>
            </g>

            <!-- PASO 3: E3 Dihidrolipoil Deshidrogenasa (FAD -> NAD+) -->
            <path d="M 118 316 L 118 354" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
            <path d="M 68 328 Q 94 328 114 336" fill="none" stroke="#475569" stroke-width="1.7" marker-end="url(#arrowSlate)"/>
            <text x="64" y="332" fill="#475569" font-size="9" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ NAD⁺</text>
            <path d="M 122 338 Q 152 346 178 346" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
            <text x="184" y="336" fill="#0f172a" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">Paso 3 — E₃: Dihidrolipoil DH</text>
            <text x="184" y="349" fill="#059669" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif">+ NADH + H⁺ <tspan fill="#64748b" font-size="8.5">(vía FAD ➔ FADH₂)</tspan></text>

            <!-- 5. Lipoamida Oxidada regenerada (S-S) -->
            <g transform="translate(42, 356)">
              <rect x="0" y="0" width="154" height="44" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.3"/>
              <g transform="translate(6, 2) scale(0.42)">
                {PDH_LIPOAMIDA_OXIDADA}
              </g>
              <text x="162" y="17" fill="#15803d" font-size="10" font-weight="900" font-family="'Inter', sans-serif">5. Lipoamida Oxidada (S–S)</text>
              <text x="162" y="30" fill="#166534" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Puente disulfuro regenerado ↺</text>
            </g>

            <!-- Retorno cíclico punteado de la Lipoamida Oxidada hacia el Paso 2a (por el margen izquierdo seguro X=12) -->
            <path d="M 42 378 L 14 378 Q 6 378 6 370 L 6 154 Q 6 146 14 146 L 62 146" fill="none" stroke="#d97706" stroke-width="1.9" stroke-dasharray="5 3" marker-end="url(#arrowAmber)"/>
            <text x="18" y="285" fill="#b45309" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(-90 18 285)" text-anchor="middle">↺ RETORNO CÍCLICO LIPOAMIDA (E₃ ➔ E₂)</text>

            <!-- Barra inferior de Balance Estequiométrico Global y 5 Cofactores -->
            <rect x="4" y="408" width="372" height="36" rx="6" fill="#fff7ed" stroke="#fdba74" stroke-width="1.2"/>
            <text x="190" y="422" fill="#9a3412" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">ESTEQUIOMETRÍA: Piruvato + CoA-SH + NAD⁺ ➔ Acetil-CoA + CO₂ + NADH + H⁺</text>
            <text x="190" y="436" fill="#c2410c" font-size="8.2" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">5 Cofactores: TPP (B₁) • Lipoamida • CoA-SH (B₅) • FAD (B₂) • NAD⁺ (B₃)</text>
          </g>

          <!-- =========================================================== -->
          <!-- COLUMNA DERECHA: REGULACIÓN DINÁMICA Y DIANAS TOXICOLÓGICAS  -->
          <!-- =========================================================== -->
          <g transform="translate(405, 52)">
            <text x="0" y="12" fill="#0f172a" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif">II. CONTROL COVALENTE Y ALOSTÉRICO</text>

            <!-- Circuito PDK / PDP -->
            <g transform="translate(0, 30)">
              <!-- Estimuladores de PDK -->
              <g transform="translate(180, -10)">
                <text x="0" y="0" fill="#dc2626" font-size="10" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">(+) Estimulan PDK (Inactivan):</text>
                <text x="0" y="13" fill="#7f1d1d" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">NADH, Acetil-CoA, ATP</text>
                <path d="M 0 15 L 0 26" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
              </g>

              <!-- Nodo E1 Activa -->
              <g transform="translate(10, 60)">
                <ellipse cx="55" cy="0" rx="55" ry="20" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
                <text x="55" y="-2" fill="#15803d" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">E1 ACTIVA</text>
                <text x="55" y="10" fill="#166534" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Ser-OH (Desfosforilada)</text>
              </g>

              <!-- Flecha PDK Inactivadora arqueada bien por encima -->
              <path d="M 125 44 C 155 12, 205 12, 235 44" fill="none" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
              <g transform="translate(180, 40)">
                <text x="0" y="0" fill="#dc2626" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">PDK (+ATP)</text>
              </g>

              <!-- Nodo E1 Inactiva -->
              <g transform="translate(245, 60)">
                <ellipse cx="58" cy="0" rx="58" ry="20" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
                <text x="58" y="-2" fill="#991b1b" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">E1 INACTIVA</text>
                <text x="58" y="10" fill="#7f1d1d" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">(P) Ser-O-P (Fosforilada)</text>
              </g>

              <!-- Flecha PDP Activadora arqueada bien por debajo -->
              <path d="M 235 76 C 205 116, 155 116, 125 76" fill="none" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arrowGreen)"/>
              <g transform="translate(180, 94)">
                <text x="0" y="0" fill="#16a34a" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">PDP (+H₂O)</text>
              </g>

              <!-- Estimuladores de PDP -->
              <g transform="translate(180, 128)">
                <path d="M 0 0 L 0 -10" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
                <text x="0" y="14" fill="#16a34a" font-size="10" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">(+) Estimulan PDP (Activan):</text>
                <text x="0" y="27" fill="#14532d" font-size="9" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Ca²⁺ (músculo) • Insulina (hígado)</text>
              </g>

              <!-- Inhibidores de PDK -->
              <g transform="translate(10, 128)">
                <text x="0" y="0" fill="#15803d" font-size="9.5" font-weight="800" font-family="'Inter', sans-serif">⊣ Inhiben PDK:</text>
                <text x="0" y="13" fill="#334155" font-size="8.5" font-family="'Inter', sans-serif">Piruvato, ADP, NAD⁺</text>
              </g>
            </g>

            <!-- Retroinhibición directa por producto -->
            <g transform="translate(0, 195)">
              <line x1="0" y1="0" x2="360" y2="0" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="3 3"/>
              <text x="0" y="18" fill="#0f172a" font-size="11" font-weight="900" font-family="'Inter', sans-serif">RETROINHIBICIÓN DIRECTA POR PRODUCTO</text>
              
              <g transform="translate(0, 34)">
                <path d="M 5 6 L 45 6" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#inhibitionT)"/>
                <text x="52" y="10" fill="#dc2626" font-size="10" font-weight="900" font-family="'Inter', sans-serif">⊣ E2:</text>
                <text x="85" y="10" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif">Inhibida por <tspan font-weight="800" fill="#b91c1c">Acetil-CoA</tspan> (competitivo)</text>
              </g>

              <g transform="translate(0, 56)">
                <path d="M 5 6 L 45 6" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#inhibitionT)"/>
                <text x="52" y="10" fill="#dc2626" font-size="10" font-weight="900" font-family="'Inter', sans-serif">⊣ E3:</text>
                <text x="85" y="10" fill="#334155" font-size="9.5" font-family="'Inter', sans-serif">Inhibida por cociente elevado <tspan font-weight="800" fill="#b91c1c">NADH/NAD⁺</tspan></text>
              </g>
            </g>

            <!-- =========================================================== -->
            <!-- CORRELACIÓN CLÍNICA Y FARMACOLÓGICA DIRECTA                  -->
            <!-- =========================================================== -->
            <g transform="translate(0, 290)">
              <line x1="0" y1="0" x2="360" y2="0" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="3 3"/>
              <text x="0" y="18" fill="#be123c" font-size="11" font-weight="900" font-family="'Inter', sans-serif">III. CORRELACIÓN CLÍNICA Y TOXICOLOGÍA</text>

              <!-- Diana 1: E1 / TPP -->
              <g transform="translate(0, 34)">
                <rect x="0" y="0" width="355" height="58" rx="6" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.2"/>
                <g transform="translate(10, 15)">
                  <text x="0" y="0" fill="#be123c" font-size="10" font-weight="900" font-family="'Inter', sans-serif">DIANA E1: DÉFICIT DE TIAMINA (B₁) &amp; ACIDOSIS LÁCTICA</text>
                  <text x="0" y="13" fill="#334155" font-size="8.5" font-family="'Inter', sans-serif">• Carencia B₁ ➔ Agota TPP ➔ <tspan font-weight="700">Beriberi</tspan> y <tspan font-weight="700">Wernicke-Korsakoff</tspan></text>
                  <text x="0" y="25" fill="#be123c" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">• Piruvato acumulado se reduce a Lactato por la LDH</text>
                </g>
              </g>

              <!-- Diana 2: E2 / Arsenito -->
              <g transform="translate(0, 102)">
                <rect x="0" y="0" width="355" height="58" rx="6" fill="#fff1f2" stroke="#f43f5e" stroke-width="1.2"/>
                <g transform="translate(10, 15)">
                  <text x="0" y="0" fill="#be123c" font-size="10" font-weight="900" font-family="'Inter', sans-serif">DIANA E2: ENVENENAMIENTO POR ARSENITO (AsO₂⁻)</text>
                  <text x="0" y="13" fill="#334155" font-size="8.5" font-family="'Inter', sans-serif">• Quelato cíclico irreversible con tioles (-SH) de lipoamida</text>
                  <text x="0" y="25" fill="#15803d" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">• Antídoto de rescate: BAL (Dimercaprol ditiol)</text>
                </g>
              </g>
            </g>
          </g>
        </g>
      </g>
    </g>
    """)

