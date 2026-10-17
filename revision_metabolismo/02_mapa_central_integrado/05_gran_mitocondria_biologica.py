# =============================================================================
# MÓDULO DE REVISIÓN: Gran Mitocondria Biológica con Crestas
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 1251 a 1350 de 4188)
# Descripción      : Dibuja la doble membrana mitocondrial (OMM e IMM) y matriz que aloja las rutas oxidativas.
# =============================================================================

    # =========================================================================
    # 2. GRAN MITOCONDRIA BIOLÓGICA (BASE INFERIOR AMPLIA)
    # =========================================================================
    y_mito = 2160
    partes.append(f"""
    <!-- ================================================================= -->
    <!-- CAPA MATRIZ MITOCONDRIAL ARRIÑONADA Y CRESTAS INTERNAS            -->
    <!-- ================================================================= -->
    <g id="mitocondria_biologica">
      <!-- Membrana Mitocondrial Externa (MME) -->
      <path d="M 35 {y_mito + 180} 
               C 160 {y_mito - 30}, 850 {y_mito - 90}, 1520 {y_mito - 40}
               C 1950 {y_mito - 110}, 2650 {y_mito - 80}, 3350 {y_mito - 30}
               C 3850 {y_mito - 40}, 4350 {y_mito - 20}, 4740 {y_mito + 20}
               C 4880 {y_mito + 100}, 4880 {y_mito + 500}, 4850 {y_mito + 900}
               C 4820 {y_mito + 1400}, 4760 {y_mito + 1800}, 4400 {y_mito + 1940}
               C 3900 {y_mito + 1960}, 2850 {y_mito + 1950}, 1900 {y_mito + 1930}
               C 1100 {y_mito + 1950}, 260 {y_mito + 1850}, 65 {y_mito + 1300}
               C 20 {y_mito + 800}, 18 {y_mito + 400}, 35 {y_mito + 180} Z"
            fill="url(#gradMitocondria)" stroke="#92400e" stroke-width="6"/>

      <!-- Espacio Intermembrana (EIM) -->
      <path d="M 65 {y_mito + 195} 
               C 200 {y_mito}, 870 {y_mito - 55}, 1520 {y_mito - 10}
               C 1940 {y_mito - 75}, 2640 {y_mito - 45}, 3320 {y_mito}
               C 3820 {y_mito - 10}, 4320 {y_mito + 10}, 4700 {y_mito + 45}
               C 4830 {y_mito + 115}, 4830 {y_mito + 490}, 4805 {y_mito + 880}
               C 4775 {y_mito + 1370}, 4715 {y_mito + 1750}, 4370 {y_mito + 1895}
               C 3880 {y_mito + 1910}, 2830 {y_mito + 1900}, 1900 {y_mito + 1885}
               C 1120 {y_mito + 1900}, 300 {y_mito + 1805}, 95 {y_mito + 1275}
               C 48 {y_mito + 790}, 45 {y_mito + 405}, 65 {y_mito + 195} Z"
            fill="#fffbeb" fill-opacity="0.6" stroke="#b45309" stroke-width="3" stroke-dasharray="12 7"/>

      <!-- Matriz Mitocondrial (MMI Contorno interno) -->
      <path d="M 100 {y_mito + 220} 
               C 250 {y_mito + 45}, 900 {y_mito}, 1520 {y_mito + 35}
               C 1920 {y_mito - 25}, 2620 {y_mito}, 3280 {y_mito + 45}
               C 3780 {y_mito + 35}, 4280 {y_mito + 50}, 4650 {y_mito + 80}
               C 4770 {y_mito + 140}, 4770 {y_mito + 480}, 4750 {y_mito + 850}
               C 4720 {y_mito + 1330}, 4660 {y_mito + 1700}, 4330 {y_mito + 1845}
               C 3850 {y_mito + 1855}, 2800 {y_mito + 1845}, 1900 {y_mito + 1830}
               C 1150 {y_mito + 1845}, 350 {y_mito + 1755}, 130 {y_mito + 1245}
               C 80 {y_mito + 780}, 75 {y_mito + 425}, 100 {y_mito + 220} Z"
            fill="#fef3c7" fill-opacity="0.4" stroke="#d97706" stroke-width="3.5"/>

      <!-- Crestas Mitocondriales Profundas (Pliegues de MMI) -->
      <g fill="none" stroke="#b45309" stroke-width="5" stroke-linecap="round" opacity="0.65">
        <path d="M 450 {y_mito + 780} C 580 {y_mito + 620}, 720 {y_mito + 850}, 860 {y_mito + 710}"/>
        <!-- Cresta ajustada para no cortar el Ciclo de Krebs (α-KG DH en X=1195, Y=2795) -->
        <path d="M 960 {y_mito + 980} C 1090 {y_mito + 880}, 1240 {y_mito + 1020}, 1380 {y_mito + 920}"/>
        <path d="M 1520 {y_mito + 820} C 1650 {y_mito + 650}, 1800 {y_mito + 870}, 1940 {y_mito + 720}"/>
        <path d="M 2100 {y_mito + 850} C 2240 {y_mito + 670}, 2390 {y_mito + 890}, 2530 {y_mito + 740}"/>
        <path d="M 2700 {y_mito + 810} C 2850 {y_mito + 630}, 3000 {y_mito + 860}, 3150 {y_mito + 710}"/>
        <path d="M 650 {y_mito + 1380} C 820 {y_mito + 1220}, 1020 {y_mito + 1450}, 1200 {y_mito + 1310}"/>
        <path d="M 1600 {y_mito + 1420} C 1800 {y_mito + 1240}, 2050 {y_mito + 1480}, 2250 {y_mito + 1320}"/>
      </g>

      <!-- Rótulo de la Matriz integrado orgánicamente (reubicado en la franja inferior libre de la matriz,
           entre la lupa PDH y el borde inferior, para no estorbar a MPC / PC / Acetil-CoA ni a las conexiones) -->
      <g id="rotulo_matriz_mitocondrial" transform="translate(3300, {y_mito + 1720})" opacity="0.85">
        <text x="0" y="0" fill="#78350f" font-size="22" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="4" text-anchor="middle">MATRIZ MITOCONDRIAL</text>
        <text x="0" y="20" fill="#92400e" font-size="12" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Oxidación celular • Descarboxilación • Respiración</text>
      </g>

      <!-- Transportador MPC en el punto de contacto con el Piruvato (X=1680) -->
      <g transform="translate(1645, {y_mito - 55})">
        <rect x="0" y="0" width="70" height="42" rx="10" fill="#92400e" stroke="#78350f" stroke-width="2.5"/>
        <text x="35" y="27" fill="#ffffff" font-size="16" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MPC</text>
      </g>
      <text x="1730" y="{y_mito - 30}" fill="#78350f" font-size="12" font-weight="800" font-family="'Inter', sans-serif">Carrier de Piruvato (MPC1/2)</text>

      <!-- Ancla anatómica sobre la MME lateral derecha para la Lanzadera de Glicerol-3-P -->
      <g id="ancla_lanzadera_g3p" transform="translate(4850, 3060)">
        <rect x="-55" y="-16" width="110" height="32" rx="8" fill="#ea580c" stroke="#c2410c" stroke-width="2"/>
        <text x="0" y="4" fill="#ffffff" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">MME / VDAC</text>
        <text x="0" y="25" fill="#9a3412" font-size="8.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Lanzadera G-3-P</text>
      </g>

      <!-- ================================================================= -->
      <!-- CONOS DE PROYECCIÓN CIENTÍFICOS PARA LAS 4 LUPAS (ZOOM CALLOUTS)   -->
      <!-- ================================================================= -->
      <g id="conos_proyeccion_lupas" opacity="0.45">
        <!-- 1. Cono hacia Lupa Lanzadera Malato-Aspartato (MMI superior ➔ Lupa 8A) -->
        <polygon points="1026,{y_mito - 16} 716,1854 1336,1854" fill="#0284c7" fill-opacity="0.04"/>
        <line x1="1026" y1="{y_mito - 16}" x2="716" y2="1854" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="6 4"/>
        <line x1="1026" y1="{y_mito - 16}" x2="1336" y2="1854" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="6 4"/>

        <!-- 2. Cono hacia Lupa CTE (Cresta MMI ➔ Marco panorámico CTE) -->
        <polygon points="2633,{y_mito + 25} 2553,2440 3743,2440" fill="#0284c7" fill-opacity="0.04"/>
        <line x1="2633" y1="{y_mito + 25}" x2="2553" y2="2440" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="6 4"/>
        <line x1="2633" y1="{y_mito + 25}" x2="3743" y2="2440" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="6 4"/>

        <!-- 4. Cono hacia Lupa Lanzadera Glicerol-3-P (MME derecha ➔ Panel Vía 8B) -->
        <polygon points="4850,3060 5070,2935 5070,3330" fill="#ea580c" fill-opacity="0.04"/>
        <line x1="4850" y1="3060" x2="5070" y2="2935" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="6 4"/>
        <line x1="4850" y1="3060" x2="5070" y2="3330" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="6 4"/>
      </g>
    </g>
    """)

