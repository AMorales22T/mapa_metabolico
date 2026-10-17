# =============================================================================
# MÓDULO DE REVISIÓN: Entorno Hepatocelular y Torrente Vascular Sanguíneo
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 1066 a 1250 de 4188)
# Descripción      : Inicio de construir_mapa_organico(), membrana plasmática, endotelio capilar, eritrocitos y GLUT.
# =============================================================================

def construir_mapa_organico():
    partes = []

    # =========================================================================
    # 1. ENTORNO BIOLÓGICO CONTINUO (SIN GLOBOS)
    # =========================================================================
    partes.append(f"""
    <!-- ================================================================= -->
    <!-- CAPA FONDO CITOPLASMÁTICO ACUOSO                                  -->
    <!-- ================================================================= -->
    <rect width="{ANCHO_CANVAS}" height="{ALTO_CANVAS}" fill="url(#gradCitosolUnificado)"/>
    <ellipse cx="{ANCHO_CANVAS/2}" cy="1200" rx="{ANCHO_CANVAS*0.48}" ry="1050" fill="url(#haloCitosolUnificado)"/>

    <!-- Etiqueta de orientación sutil -->
    <g transform="translate(140, 480)" opacity="0.8">
      <text x="0" y="0" fill="#334155" font-size="20" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="3">CITOSOL</text>
      <path d="M 0 10 Q 100 20 200 10" fill="none" stroke="#94a3b8" stroke-width="2"/>
    </g>

    <!-- Microfilamentos del citoesqueleto atravesando el citoplasma -->
    <g fill="none" stroke="#cbd5e1" opacity="0.3">
      <path d="M 60 480 Q 800 420 1600 500 T 3200 460 T 3750 510" stroke-width="2.5" stroke-dasharray="16 12"/>
      <path d="M 60 920 Q 750 990 1500 910 T 3000 950 T 3750 890" stroke-width="2" stroke-dasharray="12 14"/>
      <path d="M 60 1480 Q 900 1400 1800 1490 T 3300 1450 T 3750 1500" stroke-width="2.2" stroke-dasharray="14 10"/>
      <path d="M 60 1980 Q 800 2060 1700 1980 T 3200 2020 T 3750 1970" stroke-width="2" stroke-dasharray="12 12"/>
    </g>

    <!-- Polirribosomas en racimos tenues -->
    <g fill="#64748b" opacity="0.22">
      <g transform="translate(180, 360)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/><circle cx="7" cy="15" r="2.8"/><circle cx="-2" cy="11" r="3.2"/></g>
      <g transform="translate(1120, 480)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/><circle cx="7" cy="15" r="2.8"/><circle cx="-2" cy="11" r="3.2"/></g>
      <g transform="translate(2350, 420)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/><circle cx="7" cy="15" r="2.8"/><circle cx="-2" cy="11" r="3.2"/></g>
      <g transform="translate(3450, 560)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/><circle cx="7" cy="15" r="2.8"/><circle cx="-2" cy="11" r="3.2"/></g>
      <g transform="translate(1080, 1680)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/></g>
      <g transform="translate(2420, 1720)"><circle cx="0" cy="0" r="4"/><circle cx="10" cy="3" r="3"/><circle cx="16" cy="10" r="3.2"/></g>
    </g>

    <!-- Vesículas citosólicas translúcidas -->
    <g opacity="0.32">
      <circle cx="260" cy="520" r="26" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
      <circle cx="1250" cy="740" r="24" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4 2"/>
      <circle cx="2300" cy="800" r="22" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
      <circle cx="3480" cy="980" r="28" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4 2"/>
    </g>
    """)

    # =========================================================================
    # 0. BANDA SUPERIOR: CICLO DE CORI (ACOPLAMIENTO MÚSCULO ⇄ HÍGADO) - VÍA 17
    # =========================================================================
    partes.append(generar_seccion_ciclo_cori_y_musculo())

    # =========================================================================
    # ENTORNO HEPATOCELULAR PRINCIPAL (DESPLAZADO POR Y_OFFSET)
    # =========================================================================
    partes.append(f'<g id="entorno_hepatocito" transform="translate(0, {Y_OFFSET})">')

    # =========================================================================
    # CAPA SANGUÍNEA: TORRENTE VASCULAR / LUMEN CAPILAR REAL
    # =========================================================================
    partes.append(f"""
    <!-- Fondo del Plasma Sanguíneo con Gradiente Vascular Profundo -->
    <path d="M 0 0 L {ANCHO_CANVAS} 0 L {ANCHO_CANVAS} 68 Q {ANCHO_CANVAS*0.5} 95 0 68 Z" fill="url(#gradPlasmaSanguineo)"/>
    
    <!-- Corriente de plasma / flujo sanguíneo laminar -->
    <g fill="none" stroke="#ef4444" opacity="0.3" stroke-linecap="round">
      <path d="M 0 16 Q 800 24 1600 18 T 3200 22 T {ANCHO_CANVAS} 18" stroke-width="2.5" stroke-dasharray="25 15"/>
      <path d="M 0 35 Q 900 42 1800 34 T 3400 38 T {ANCHO_CANVAS} 36" stroke-width="3" stroke-dasharray="35 20"/>
      <path d="M 0 52 Q 750 60 1500 52 T 3100 58 T {ANCHO_CANVAS} 54" stroke-width="2" stroke-dasharray="20 18"/>
    </g>

    <!-- Eritrocitos / Glóbulos Rojos (Bicóncavos) flotando en la sangre -->
    <g id="eritrocitos_torrente" opacity="0.88">
      <!-- Eritrocito 1 (Zona izquierda, cerca de Palmitato) -->
      <g transform="translate(220, 36) rotate(-12)">
        <ellipse cx="0" cy="0" rx="26" ry="17" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="14" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(360, 48) rotate(18)">
        <ellipse cx="0" cy="0" rx="22" ry="14" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.5"/>
        <ellipse cx="0" cy="0" rx="11" ry="6" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
      <g transform="translate(680, 28) rotate(-8)">
        <ellipse cx="0" cy="0" rx="25" ry="16" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="13" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>

      <!-- Eritrocitos 2 (Zona central, cerca de Glucosa / GLUT-4) -->
      <g transform="translate(1200, 38) rotate(15)">
        <ellipse cx="0" cy="0" rx="27" ry="18" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="14" ry="9" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(1480, 26) rotate(-20)">
        <ellipse cx="0" cy="0" rx="24" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6"/>
        <ellipse cx="0" cy="0" rx="12" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
      <g transform="translate(1880, 32) rotate(10)">
        <ellipse cx="0" cy="0" rx="26" ry="17" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="13" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>

      <!-- Eritrocitos 3 (Zona derecha, cerca de Pentosas y Lípidos) -->
      <g transform="translate(2400, 42) rotate(-14)">
        <ellipse cx="0" cy="0" rx="25" ry="16" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="13" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(2750, 24) rotate(22)">
        <ellipse cx="0" cy="0" rx="23" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6"/>
        <ellipse cx="0" cy="0" rx="11" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
      <g transform="translate(3250, 38) rotate(-6)">
        <ellipse cx="0" cy="0" rx="26" ry="17" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="14" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(3580, 28) rotate(16)">
        <ellipse cx="0" cy="0" rx="24" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6"/>
        <ellipse cx="0" cy="0" rx="12" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
      <!-- Eritrocitos 4 (Zona derecha ampliada - Ciclo de la Urea y Excreción) -->
      <g transform="translate(4150, 36) rotate(12)">
        <ellipse cx="0" cy="0" rx="25" ry="16" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="13" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(4650, 42) rotate(-15)">
        <ellipse cx="0" cy="0" rx="24" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6"/>
        <ellipse cx="0" cy="0" rx="12" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
      <!-- Eritrocitos 5 (Zona extendida derecha - Nucleótidos y Eliminación de Urato) -->
      <g transform="translate(5080, 34) rotate(14)">
        <ellipse cx="0" cy="0" rx="25" ry="16" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.8"/>
        <ellipse cx="0" cy="0" rx="13" ry="8" fill="url(#gradEritrocitoCentro)" opacity="0.75"/>
      </g>
      <g transform="translate(5450, 40) rotate(-10)">
        <ellipse cx="0" cy="0" rx="24" ry="15" fill="url(#gradEritrocito)" stroke="#7f1d1d" stroke-width="1.6"/>
        <ellipse cx="0" cy="0" rx="12" ry="7" fill="url(#gradEritrocitoCentro)" opacity="0.7"/>
      </g>
    </g>

    <!-- Albúmina sérica y Lipoproteínas en el plasma -->
    <g opacity="0.6">
      <ellipse cx="490" cy="24" rx="16" ry="11" fill="#fef08a" stroke="#ca8a04" stroke-width="1.2"/>
      <text x="490" y="27" fill="#854d0e" font-size="7.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">ALBÚMINA</text>
      <ellipse cx="2950" cy="28" rx="18" ry="12" fill="#fed7aa" stroke="#ea580c" stroke-width="1.2"/>
      <text x="2950" y="32" fill="#9a3412" font-size="7.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">VLDL / HDL</text>
    </g>

    <!-- Rótulo Principal del Torrente Sanguíneo -->
    <g transform="translate(60, 32)">
      <rect x="0" y="-18" width="230" height="28" rx="6" fill="#450a0a" stroke="#b91c1c" stroke-width="1.5" opacity="0.85"/>
      <text x="14" y="2" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#fecaca" letter-spacing="2.5">
        TORRENTE SANGUÍNEO
      </text>
    </g>

    <!-- ================================================================= -->
    <!-- MEMBRANA PLASMÁTICA CONTINUA Y CANAL GLUT-4 (ARRIBA)              -->
    <!-- ================================================================= -->
    <!-- Doble Bicapa Fosfolipídica Ondulada (Límite Celular) -->
    <path d="M 0 68 Q 1225 95 2450 68 T 4900 68 T {ANCHO_CANVAS} 68" fill="none" stroke="#0284c7" stroke-width="10" stroke-linecap="round"/>
    <path d="M 0 78 Q 1225 105 2450 78 T 4900 78 T {ANCHO_CANVAS} 78" fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>

    <!-- Cabezas polares fosfolipídicas -->
    <g fill="#0284c7" opacity="0.75">
      <circle cx="150" cy="73" r="3.4"/><circle cx="168" cy="75" r="3.4"/><circle cx="186" cy="77" r="3.4"/>
      <circle cx="950" cy="82" r="3.4"/><circle cx="968" cy="81" r="3.4"/><circle cx="986" cy="79" r="3.4"/>
      <circle cx="2800" cy="79" r="3.4"/><circle cx="2818" cy="77" r="3.4"/><circle cx="2836" cy="75" r="3.4"/>
    </g>

    <!-- Canal Transportador GLUT-4 (alineado con la Glucólisis en X=1680) -->
    <g transform="translate(1640, 80)">
      <path d="M 0 6 C 10 -14, 28 -14, 34 6 C 38 20, 34 38, 25 44 C 12 47, 2 37, 0 24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
      <path d="M 80 6 C 70 -14, 52 -14, 46 6 C 42 20, 46 38, 55 44 C 68 47, 78 37, 80 24 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.5"/>
      <ellipse cx="40" cy="22" rx="12" ry="20" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
      <!-- Glucosa entrando desde la sangre -->
      <polygon points="40,15 46,18 46,25 40,28 34,25 34,18" fill="#ffffff" stroke="#ea580c" stroke-width="1.8"/>
      <circle cx="34" cy="18" r="2.2" fill="#dc2626"/>
      <text x="40" y="52" fill="#0369a1" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-4</text>
    </g>

    <!-- Flujo de Glucosa desde la sangre hacia la primera reacción -->
    <line x1="1680" y1="52" x2="1680" y2="80" stroke="#ea580c" stroke-width="2.6"/>
    <line x1="1680" y1="135" x2="1680" y2="152" stroke="#ea580c" stroke-width="2.8" marker-end="url(#arrowFlow)"/>

    <!-- Receptor GLUT-4 en membrana plasmática -->
    """)

