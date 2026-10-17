# =============================================================================
# MÓDULO DE REVISIÓN: Función del Ciclo de Cori y Ultraestructura Muscular
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 680 a 1065 de 4188)
# Descripción      : Carga la CTE y dibuja el sarcómero estriado superior y el transporte sanguíneo de L-lactato.
# =============================================================================

def cargar_cte_original_usuario():
    """
    Carga directamente el diseño vectorial exacto del archivo SVG que el usuario ya realizó:
    02_RESPIRACION_Y_ENERGIA/via_07_cadena_respiratoria_atp_sintasa/Cadena_Transporte_Electrones.svg
    """
    import re
    path_cte = os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "via_07_cadena_respiratoria_atp_sintasa", "Cadena_Transporte_Electrones.svg")
    with open(path_cte, "r", encoding="utf-8") as f:
        svg_content = f.read()

    defs_match = re.search(r'<defs>([\s\S]*?)</defs>', svg_content)
    cte_defs = defs_match.group(1) if defs_match else ""

    # Filtrar marcadores duplicados para no crear colisiones en el SVG principal
    for marker_id in ['arrowFlow', 'arrowRed', 'arrowGreen', 'arrowBlue']:
        cte_defs = re.sub(rf'<marker id="{marker_id}"[\s\S]*?</marker>', '', cte_defs)

    body_match = re.search(r'</defs>([\s\S]*?)</svg>', svg_content)
    cte_body = body_match.group(1) if body_match else ""

    # Ajustar el fondo matricial de 1740 a 820 para ceñirse a las reacciones activas
    cte_body = cte_body.replace('height="1740"', 'height="820"')
    
    # Eliminar la cresta derecha que protruye más allá del marco (forma en D de color melocotón en X=1150)
    cte_body = re.sub(r'<path d="M 1150 500 C 1080 500[^"]*" />', '', cte_body)

    return cte_defs, cte_body

def generar_seccion_ciclo_cori_y_musculo():
    """
    Genera el compartimento anatómico extendido del Músculo Esquelético (Vía 17: Ciclo de Cori)
    como franja horizontal continua de extremo a extremo (X=0 a X=5800, Y=10 a Y=340),
    bañado por el torrente sanguíneo vascular (Y=340 a Y=425) que comunica con el hepatocito.
    """
    # 1. Bandas A (Miosina - anisotropas densas periódicas)
    bandas_a = []
    for bx in range(75, 5740, 50):
        bandas_a.append(f'<rect x="{bx}" y="30" width="25" height="274" rx="3" fill="#be123c" opacity="0.055"/>')

    # 2. Discos Z (Líneas Z transversales con α-actinina)
    discos_z = []
    for zx in range(100, 5740, 50):
        discos_z.append(f'<line x1="{zx}" y1="28" x2="{zx}" y2="310" stroke="#9f1239" stroke-width="1.2" stroke-dasharray="4 2" opacity="0.3"/>')

    # 3. Miofibrillas longitudinales continuas
    miofibrillas = []
    for my in [55, 100, 145, 190, 235, 280]:
        miofibrillas.append(f'<line x1="55" y1="{my}" x2="5745" y2="{my}" stroke="#f43f5e" stroke-width="1.2" stroke-dasharray="28 14" opacity="0.22"/>')

    # 4. Túbulos T (invaginaciones sarcolémicas transversales periódicas)
    tubulos_t = []
    for tx in range(180, 5730, 160):
        tubulos_t.append(f'<line x1="{tx}" y1="340" x2="{tx}" y2="315" stroke="#f43f5e" stroke-width="2.2" stroke-linecap="round" opacity="0.65"/><circle cx="{tx}" cy="315" r="2.2" fill="#fda4af"/>')

    # 5. Núcleos periféricos subsarcolémicos multinucleados
    nucleos_sup = [350, 850, 1450, 2050, 2650, 3250, 3850, 4450, 5050, 5500]
    nucleos_inf = [600, 1150, 1750, 2350, 2950, 3550, 4150, 4750, 5300, 5650]
    nucleos_items = []
    for i, nx in enumerate(nucleos_sup, 1):
        nucleos_items.append(f'''
        <g transform="translate({nx}, 24)">
          <ellipse cx="0" cy="0" rx="30" ry="7.5" fill="#312e81" stroke="#4338ca" stroke-width="1.5"/>
          <ellipse cx="-2" cy="0" rx="15" ry="3.5" fill="#6366f1" opacity="0.8"/>
          <circle cx="6" cy="-1" r="1.8" fill="#e0e7ff"/>
          <text x="38" y="3" fill="#4338ca" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif">Núcleo subsarcolémico S{i}</text>
        </g>''')
    for j, nx in enumerate(nucleos_inf, 1):
        nucleos_items.append(f'''
        <g transform="translate({nx}, 325)">
          <ellipse cx="0" cy="0" rx="30" ry="7.5" fill="#312e81" stroke="#4338ca" stroke-width="1.5"/>
          <ellipse cx="-2" cy="0" rx="15" ry="3.5" fill="#6366f1" opacity="0.8"/>
          <circle cx="6" cy="-1" r="1.8" fill="#e0e7ff"/>
          <text x="-38" y="3" fill="#4338ca" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Núcleo subsarcolémico I{j}</text>
        </g>''')

    # 6. Gránulos de glucógeno sarcoplásmico
    glucogeno_pos = [280, 1620, 2520, 3420, 4320, 5220]
    glucogeno_items = []
    for gx in glucogeno_pos:
        glucogeno_items.append(f'''
        <g transform="translate({gx}, 285)" opacity="0.85">
          <circle cx="0" cy="0" r="3.5" fill="#f59e0b" stroke="#d97706" stroke-width="0.8"/>
          <circle cx="7" cy="-3" r="2.8" fill="#fbbf24"/>
          <circle cx="12" cy="2" r="3" fill="#f59e0b"/>
          <circle cx="5" cy="5" r="2.5" fill="#fbbf24"/>
          <text x="20" y="3" fill="#b45309" font-size="7" font-weight="800" font-family="'Inter', sans-serif">Glucógeno muscular (reserva contráctil)</text>
        </g>''')

    # 7. Sarcosomas (Mitocondrias interfibrilares)
    sarcosomas_pos = [1920, 2820, 3720, 4620, 5450]
    sarcosomas_items = []
    for sx in sarcosomas_pos:
        sarcosomas_items.append(f'''
        <g transform="translate({sx}, 210)" opacity="0.85">
          <ellipse cx="0" cy="0" rx="22" ry="12" fill="url(#gradMitocondria)" stroke="#92400e" stroke-width="1.6"/>
          <path d="M -12 0 C -6 -6, 0 6, 8 0" stroke="#b45309" stroke-width="1.8" fill="none" opacity="0.75"/>
          <text x="0" y="22" fill="#92400e" font-size="7" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Sarcosoma (ATP oxidativo)</text>
        </g>''')

    tubulos_str = ''.join(tubulos_t)
    bandas_str = ''.join(bandas_a)
    discos_str = ''.join(discos_z)
    miofibrillas_str = ''.join(miofibrillas)
    nucleos_str = ''.join(nucleos_items)
    glucogeno_str = ''.join(glucogeno_items)
    sarcosomas_str = ''.join(sarcosomas_items)

    return f"""
    <!-- ================================================================= -->
    <!-- RUTA 17: CICLO DE CORI (ACOPLAMIENTO MÚSCULO ESQUELÉTICO ⇄ HÍGADO) -->
    <!-- ================================================================= -->
    <g id="ruta_ciclo_cori" data-arrastrable="1">
      <!-- 1. COMPARTIMENTO ANATÓMICO EXTENDIDO DEL MÚSCULO ESQUELÉTICO (FRANJA COMPLETA 0 A 5800 PX) -->
      <g id="miocito_cori">
        <!-- Fondo y entorno biológico de la fibra muscular estriada -->
        <g id="musculo_esqueletico_biologico">
          <!-- Vientre Anatómico del Fascículo Muscular (Epimisio / Perimisio) -->
          <rect x="0" y="12" width="5800" height="328" fill="url(#gradVientreMuscular)" stroke="#9f1239" stroke-width="3"/>
          <rect x="0" y="16" width="5800" height="320" fill="url(#gradSarcoplasma)" opacity="0.92"/>

          <!-- Inserción Tendinosa / Aponeurosis Fascial Izquierda (X=0 a 55) -->
          <path d="M 0 12 L 55 12 L 55 340 L 0 340 Z" fill="url(#gradFasciaTendinosa)" stroke="#94a3b8" stroke-width="2"/>
          <g fill="none" stroke="#cbd5e1" stroke-width="1.3" stroke-linecap="round" opacity="0.75">
            <path d="M 5 60 Q 25 55 55 58"/>
            <path d="M 5 110 Q 28 105 55 108"/>
            <path d="M 5 160 Q 30 160 55 160"/>
            <path d="M 5 210 Q 28 215 55 212"/>
            <path d="M 5 260 Q 25 265 55 262"/>
            <path d="M 5 300 Q 25 305 55 302"/>
          </g>
          <text x="28" y="176" fill="#64748b" font-size="8" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle" transform="rotate(-90 28 176)" letter-spacing="1.5">INSERCIÓN TENDINOSA (FASCIA)</text>

          <!-- Inserción Tendinosa / Aponeurosis Fascial Derecha (X=5745 a 5800) -->
          <path d="M 5745 12 L 5800 12 L 5800 340 L 5745 340 Z" fill="url(#gradFasciaTendinosa)" stroke="#94a3b8" stroke-width="2"/>
          <g fill="none" stroke="#cbd5e1" stroke-width="1.3" stroke-linecap="round" opacity="0.75">
            <path d="M 5745 58 Q 5775 55 5795 60"/>
            <path d="M 5745 108 Q 5772 105 5795 110"/>
            <path d="M 5745 160 Q 5770 160 5795 160"/>
            <path d="M 5745 212 Q 5772 215 5795 210"/>
            <path d="M 5745 262 Q 5775 265 5795 260"/>
            <path d="M 5745 302 Q 5775 305 5795 300"/>
          </g>
          <text x="5772" y="176" fill="#64748b" font-size="8" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle" transform="rotate(-90 5772 176)" letter-spacing="1.5">INSERCIÓN TENDINOSA (FASCIA)</text>

          <!-- Sarcolema continuo inferior (Membrana plasmática excitable limitante en Y=340) -->
          <line x1="0" y1="340" x2="5800" y2="340" stroke="#9f1239" stroke-width="5" stroke-linecap="square"/>
          <line x1="0" y1="337" x2="5800" y2="337" stroke="#e11d48" stroke-width="2" stroke-dasharray="14 4"/>

          <!-- Túbulos T (Invaginaciones sarcolémicas transversales periódicas hacia el sarcoplasma) -->
          {tubulos_str}

          <!-- Estriaciones Histológicas Periódicas (Bandas A - Miosina Anisótropa) -->
          <g>
            {bandas_str}
          </g>

          <!-- Discos Z (Líneas Z transversales que delimitan cada sarcómero periódico) -->
          <g>
            {discos_str}
          </g>

          <!-- Miofibrillas longitudinales continuas (Haces paralelos de F-Actina y Miosina II) -->
          <g>
            {miofibrillas_str}
          </g>

          <!-- Núcleos Periféricos Subsarcolémicos (Sincitio multinucleado típico del miocito esquelético) -->
          {nucleos_str}

          <!-- Gránulos de Glucógeno Muscular Sarcoplásmico -->
          {glucogeno_str}

          <!-- Sarcosomas (Mitocondrias interfibrilares del miocito) -->
          {sarcosomas_str}

          <!-- Infografías ultraestructurales educativas integradas a lo largo de la fibra -->
          <!-- 1. Módulo Arquitectura del Sarcómero (X=2050) -->
          <g transform="translate(2050, 95)" opacity="0.9">
            <rect x="-200" y="-18" width="400" height="42" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.2"/>
            <text x="0" y="-4" fill="#9f1239" font-size="9" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">|◀───────────── SARCÓMERO (~2.5 µm) ─────────────▶|</text>
            <text x="0" y="10" fill="#be123c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Línea Z (α-Actinina) • Banda I (Actina F) • Banda A (Miosina II) • Zona H • Línea M</text>
            <text x="0" y="19" fill="#881337" font-size="6.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Unidad morfofuncional contráctil delimitada entre dos discos Z consecutivos</text>
          </g>

          <!-- 2. Módulo Tríada Sarcoplásmica (X=2950) -->
          <g transform="translate(2950, 95)" opacity="0.9">
            <rect x="-210" y="-18" width="420" height="42" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.2"/>
            <text x="0" y="-4" fill="#9f1239" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">TRÍADA SARCOPLÁSMICA &amp; ACOPLAMIENTO EXCITACIÓN-CONTRACCIÓN</text>
            <text x="0" y="10" fill="#be123c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Invaginación de Túbulo T flanqueada por 2 Cisternas terminales del Retículo Sarcoplásmico</text>
            <text x="0" y="19" fill="#881337" font-size="6.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Potencial de acción ➔ Sensor DHPR (Cav1.1) ➔ Canal Ryanodina (RyR1) ➔ Salida masiva de Ca²⁺</text>
          </g>

          <!-- 3. Módulo Puentes Cruzados (X=3890) -->
          <g transform="translate(3890, 95)" opacity="0.9">
            <rect x="-210" y="-18" width="420" height="42" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.2"/>
            <text x="0" y="-4" fill="#9f1239" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">CICLO DE PUENTES CRUZADOS &amp; DESLIZAMIENTO DE FILAMENTOS</text>
            <text x="0" y="10" fill="#be123c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Ca²⁺ se une a Troponina C ➔ Tropomiosina expone sitios activos de F-Actina</text>
            <text x="0" y="19" fill="#881337" font-size="6.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Cabezas de Miosina hidrolizan ATP (Miosina ATPasa) ➔ Golpe de fuerza contráctil (Power Stroke)</text>
          </g>

          <!-- 4. Módulo Bioenergética y Fosfágenos (X=4810) -->
          <g transform="translate(4810, 95)" opacity="0.9">
            <rect x="-210" y="-18" width="420" height="42" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.2"/>
            <text x="0" y="-4" fill="#9f1239" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">SISTEMA DE FOSFÁGENOS &amp; BIOENERGÉTICA CONTRÁCTIL INMEDIATA</text>
            <text x="0" y="10" fill="#be123c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Fosfocreatina (PCr) + ADP ⇄ Creatina + ATP (Creatina Cinasa CK-MM / Amortiguador primario)</text>
            <text x="0" y="19" fill="#881337" font-size="6.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Activación alostérica de Glucógeno Fosforilasa b por 5'-AMP muscular ➔ G1P ➔ Glucólisis rápida</text>
          </g>

          <!-- 5. Módulo Diferenciación de Fibras (X=5530) -->
          <g transform="translate(5530, 95)" opacity="0.9">
            <rect x="-170" y="-18" width="340" height="42" rx="8" fill="#fff1f2" stroke="#fda4af" stroke-width="1.2"/>
            <text x="0" y="-4" fill="#9f1239" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">TIPOS DE FIBRAS MUSCULARES</text>
            <text x="0" y="10" fill="#be123c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Tipo I (Rojas, lentas, ricas en mioglobina y sarcosomas / Oxidativas)</text>
            <text x="0" y="19" fill="#881337" font-size="6.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Tipo IIb (Blancas, rápidas, anaerobias / Glucolíticas de alto poder)</text>
          </g>
        </g>

        <!-- Header y Título Editorial del Miocito Esquelético con Badge Vía 17 -->
        {badge_via(17, 85, 38)}
        <g transform="translate(120, 38)">
          <text x="0" y="0" fill="#881337" font-size="13.5" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="0.5">MÚSCULO ESQUELÉTICO (FIBRA SARCOLÉMICA ESTRIADA · CICLO DE CORI)</text>
          <text x="0" y="14" fill="#be123c" font-size="8.5" font-weight="700" font-family="'Inter', sans-serif">Contracción anaerobia vigorosa • Glucólisis anaerobia rápida (+2 ATP netos) • Regeneración de NAD⁺ (LDH-M) • Exportación de Lactato</text>
        </g>

        <!-- Transportador muscular GLUT-4 en el sarcolema inferior (X=140, Y=340) -->
        <g id="carrier_glut4_musculo" transform="translate(107, 327)">
          <rect x="0" y="0" width="66" height="30" rx="6" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
          <text x="33" y="14" fill="#ffffff" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-4</text>
          <text x="33" y="24" fill="#e0f2fe" font-size="7" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">SLC2A4</text>
        </g>
        <!-- Flecha de captación: Glucosa entra desde el sarcolema inferior hacia el sarcoplasma -->
        <line x1="140" y1="327" x2="140" y2="238" stroke="#0284c7" stroke-width="2.4" marker-end="url(#arrowBlue)"/>
        <text x="150" y="285" fill="#0369a1" font-size="8" font-weight="800" font-family="'Inter', sans-serif">Captación ➔</text>

        <!-- Molécula 1: D-Glucosa Muscular (Estructura química completa) -->
        <g id="m_cori_glc_musc" data-arrastrable="1" transform="translate(95, 85)">
          <g>{GLUCOSA}</g>
          <text x="45" y="102" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">D-Glucosa</text>
          <text x="45" y="117" fill="#ea580c" font-size="10.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[6C] Muscular</text>
        </g>

        <!-- Reacción 1: Hexoquinasa muscular (HK-II) -->
        <g transform="translate(210, 130)">
          <line x1="0" y1="0" x2="150" y2="0" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
          <text x="75" y="-12" fill="#c2410c" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Hexoquinasa (HK-II)</text>
          <text x="75" y="-23" fill="#64748b" font-size="7.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 2.7.1.1</text>
          <rect x="43" y="8" width="64" height="18" rx="9" fill="#fee2e2" stroke="#dc2626" stroke-width="1.2"/>
          <text x="75" y="21" fill="#b91c1c" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">− 1 ATP</text>
        </g>

        <!-- Molécula 2: Glucosa-6-Fosfato (Atrapada en el miocito por ausencia de G6Pasa) -->
        <g id="m_cori_g6p_musc" data-arrastrable="1" transform="translate(385, 85)">
          <g>{GLUCOSA_6_FOSFATO}</g>
          <text x="45" y="102" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Glucosa-6-P</text>
          <text x="45" y="117" fill="#ea580c" font-size="10.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[6C] Atrapada</text>
          <rect x="-20" y="125" width="130" height="17" rx="8.5" fill="#fee2e2" stroke="#dc2626" stroke-width="1.1"/>
          <text x="45" y="137" fill="#b91c1c" font-size="7.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">✕ Sin G6Pasa en músculo</text>
        </g>

        <!-- Reacción 2: Glucólisis anaerobia (PFK-1 ➔ Aldolasa ➔ GAPDH ➔ Piruvato Quinasa) -->
        <g transform="translate(520, 130)">
          <line x1="0" y1="0" x2="150" y2="0" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
          <text x="75" y="-12" fill="#c2410c" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">PFK-1 ➔ Piruvato Quinasa</text>
          <text x="75" y="-23" fill="#64748b" font-size="7.5" font-family="'Inter', sans-serif" text-anchor="middle">Glucólisis anaerobia</text>
          <rect x="37" y="8" width="76" height="18" rx="9" fill="#dcfce7" stroke="#16a34a" stroke-width="1.2"/>
          <text x="75" y="21" fill="#15803d" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">+ 2 ATP (neto)</text>
        </g>

        <!-- Molécula 3: Piruvato Muscular (Estructura química completa) -->
        <g id="m_cori_pyr_musc" data-arrastrable="1" transform="translate(695, 85)">
          <g>{PIRUVATO}</g>
          <text x="45" y="102" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Piruvato (x2)</text>
          <text x="45" y="117" fill="#ea580c" font-size="10.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[3C]</text>
        </g>

        <!-- Reacción 3: Lactato Deshidrogenasa muscular (LDH-M / LDHA) -->
        <g transform="translate(805, 130)">
          <line x1="0" y1="0" x2="160" y2="0" stroke="#e11d48" stroke-width="2.6" marker-end="url(#arrowRed)"/>
          <text x="80" y="-17" fill="#be123c" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">LDH-M (LDHA)</text>
          <text x="80" y="-6" fill="#64748b" font-size="8" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 1.1.1.27</text>
          <rect x="18" y="8" width="124" height="18" rx="9" fill="#fee2e2" stroke="#dc2626" stroke-width="1.2"/>
          <text x="80" y="21" fill="#b91c1c" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">+ 2 NADH ➔ + 2 NAD⁺</text>
        </g>

        <!-- Molécula 4: L-Lactato Muscular (Estructura química completa) -->
        <g id="m_cori_lac_musc" data-arrastrable="1" transform="translate(990, 85)">
          <g>{GLUCONEO_LACTATO}</g>
          <text x="45" y="102" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">L-Lactato (x2)</text>
          <text x="45" y="117" fill="#e11d48" font-size="10.5" font-weight="700" font-family="'JetBrains Mono', monospace" text-anchor="middle">[3C]</text>
        </g>

        <!-- Exportación de Lactato hacia MCT4 en el sarcolema inferior -->
        <path d="M 1085 130 C 1170 130, 1220 200, 1245 320" fill="none" stroke="#e11d48" stroke-width="2.4" marker-end="url(#arrowRed)"/>
        <text x="1135" y="112" fill="#be123c" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif">Exporta ➔</text>

        <!-- Transportador sarcolémico MCT4 (SLC16A3) en el sarcolema inferior (X=1248, Y=340) -->
        <g id="carrier_mct4_musculo" transform="translate(1215, 327)">
          <rect x="0" y="0" width="66" height="30" rx="6" fill="#be123c" stroke="#881337" stroke-width="2"/>
          <text x="33" y="14" fill="#ffffff" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MCT4</text>
          <text x="33" y="24" fill="#fecdd3" font-size="7" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">SLC16A3</text>
        </g>
      </g>

      <!-- 2. FLUJOS SANGUÍNEOS CONECTORES Y BIOMOLÉCULAS EN EL TORRENTE VASCULAR -->
      <!-- Biomolécula real de L-Lactato flotando en el torrente sanguíneo (Cori ➔ Hígado) -->
      <g id="m_cori_lac_sangre" data-arrastrable="1" transform="translate(1533, 382)">
        <!-- Cápsula vascular flotante con sombra plasmática -->
        <rect x="-34" y="-28" width="68" height="58" rx="8" fill="#fff1f2" stroke="#e11d48" stroke-width="1.6" filter="drop-shadow(0 2px 5px rgba(190,18,60,0.2))"/>
        
        <!-- Estructura molecular de L-Lactato en sangre -->
        <g transform="translate(-30, -26) scale(0.64)">
          <!-- C1: Carboxilato Superior -->
          <text x="47" y="15" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
          <line x1="47" y1="20" x2="47" y2="30" stroke="#0f172a" stroke-width="1.8" />

          <!-- C2: Carbono quiral H-C-OH -->
          <line x1="40" y1="37" x2="31" y2="37" stroke="#0f172a" stroke-width="1.6" />
          <text x="25" y="41" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#64748b" text-anchor="end">H</text>
          <text x="47" y="41" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" text-anchor="middle">C</text>
          <line x1="54" y1="37" x2="63" y2="37" stroke="#0284c7" stroke-width="1.6" />
          <text x="70" y="41" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0284c7">OH</text>

          <!-- Enlace C2 - C3 -->
          <line x1="47" y1="45" x2="47" y2="55" stroke="#0f172a" stroke-width="1.8" />

          <!-- C3: Grupo Metilo -->
          <text x="47" y="67" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">CH₃</text>
        </g>
        <!-- Rótulo contenido dentro de la cápsula -->
        <text x="0" y="24" font-family="'Inter', sans-serif" font-size="7" font-weight="900" fill="#9f1239" text-anchor="middle">L-Lactato [3C]</text>
      </g>

      <!-- Flujo 1: Lactato muscular sale de MCT4 y viaja a la molécula de L-Lactato en sangre -->
      <path d="M 1248 358 L 1248 398 L 1495 398 L 1499 382" fill="none" stroke="#fb7185" stroke-width="3" stroke-dasharray="6 3" marker-end="url(#arrowRed)"/>

      <!-- Flujo 2: L-Lactato sanguíneo continúa hacia MCT1 hepático -->
      <path d="M 1567 382 L 1587 382 L 1587 403" fill="none" stroke="#fb7185" stroke-width="3" stroke-dasharray="6 3" marker-end="url(#arrowRed)"/>

      <!-- Flujo 3: Glucosa neoglucogénica sale de GLUT-2 hepático y viaja hacia GLUT-4 muscular -->
      <path d="M 1480 415 L 1480 368 L 140 368 L 140 358" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="8 4" marker-end="url(#arrowBlue)"/>
      <g transform="translate(750, 352)">
        <rect x="-110" y="-9" width="220" height="18" rx="5" fill="#082f49" stroke="#0284c7" stroke-width="1" opacity="0.95"/>
        <text x="0" y="3.5" fill="#e0f2fe" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">Glucosa neoglucogénica ➔ Músculo (GLUT-4)</text>
      </g>

      <!-- 3. BALANCE BIOEDITORIAL DEL CICLO EN PILLS COMPACTAS (EN EL LUMEN VASCULAR) -->
      <g id="balance_pills_cori">
        <!-- Pill Músculo -->
        <g transform="translate(1840, 385)">
          <rect x="-135" y="-10" width="270" height="20" rx="10" fill="#ffe4e6" stroke="#be123c" stroke-width="1.5"/>
          <text x="0" y="4" fill="#be123c" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">MÚSCULO · Glucólisis anaerobia · +2 ATP netos</text>
        </g>

        <!-- Pill Hígado -->
        <g transform="translate(2200, 385)">
          <rect x="-165" y="-10" width="330" height="20" rx="10" fill="#fef3c7" stroke="#a16207" stroke-width="1.5"/>
          <text x="0" y="4" fill="#a16207" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">HÍGADO · Gluconeogénesis · −6 ~P (−4 ATP, −2 GTP)</text>
        </g>

        <!-- Pill Balance Neto -->
        <g transform="translate(2580, 385)">
          <rect x="-165" y="-10" width="330" height="20" rx="10" fill="#fee2e2" stroke="#b91c1c" stroke-width="1.5"/>
          <text x="0" y="4" fill="#b91c1c" font-size="9" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">BALANCE NETO · −4 ATP (Deuda de O₂ saldada)</text>
        </g>
      </g>

      <!-- 4. CONTINUIDAD DE LA CIRCULACIÓN SISTÉMICA & ÓRGANOS EXTRAHEPÁTICOS -->
      <g id="sistema_vascular_extrahepatico">
        <g transform="translate(3400, 385)">
          <rect x="-180" y="-11" width="360" height="22" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1" opacity="0.9"/>
          <text x="0" y="4" fill="#fecdd3" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="0.5">CIRCULACIÓN SISTÉMICA VASCULAR · HOMEOSTASIS DEL ORGANISMO</text>
        </g>

        <g transform="translate(4250, 385)">
          <rect x="-190" y="-11" width="380" height="22" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1" opacity="0.9"/>
          <text x="0" y="4" fill="#fecdd3" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="0.5">TRANSPORTE DE LÍPIDOS &amp; CUERPOS CETÓNICOS (ALBÚMINA / LIPOPROTEÍNAS)</text>
        </g>

        <g transform="translate(5150, 385)">
          <rect x="-170" y="-11" width="340" height="22" rx="6" fill="#1e293b" stroke="#334155" stroke-width="1" opacity="0.9"/>
          <text x="0" y="4" fill="#fecdd3" font-size="8.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="0.5">DEPURACIÓN RENAL · EXCRECIÓN DE UREA Y ÁCIDO ÚRICO</text>
        </g>
      </g>
    </g>
    """

