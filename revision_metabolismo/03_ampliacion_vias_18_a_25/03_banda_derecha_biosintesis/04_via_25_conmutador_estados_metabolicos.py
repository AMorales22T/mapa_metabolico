# =============================================================================
# MÓDULO DE REVISIÓN: Vía 25: Integración por Estados Metabólicos y Hormonales
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/generar_ampliacion.py (líneas 614 a 680 de 925)
# Descripción      : Cuadro comparativo de flujos en estado Posprandial (Insulina), Ayuno Temprano (Glucagón), Ayuno Prolongado y Ejercicio Intenso.
# =============================================================================

    # -------------------------------------------------------------------------
    # VÍA 25: CONMUTADOR VISUAL DE ESTADOS METABÓLICOS Y HORMONALES
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_conmutador_estados" class="ruta-metabolica">')
    p.append(encabezado_via(5850, 4270, 25, "INTEGRACIÓN POR ESTADOS METABÓLICOS Y HORMONALES", "Conmutador de flujos energéticos • Posprandial vs Ayuno vs Ejercicio", color="#ea580c"))

    p.append("""
    <g transform="translate(5860, 4330)">
      <rect x="0" y="0" width="650" height="540" rx="12" fill="#fffbeb" stroke="#d97706" stroke-width="2.5"/>
      <text x="325" y="32" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#92400e" text-anchor="middle">CONMUTADOR DE FLUJOS ENERGÉTICOS INTERTISULARES</text>

      <g transform="translate(25, 55)">
        <rect x="0" y="0" width="290" height="140" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
        <text x="145" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#15803d" text-anchor="middle">ESTADO POSPRANDIAL (INSULINA ↑)</text>
        <text x="145" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Hígado: Glucógeno ↑ + Lipogénesis ↑</text>
        <text x="145" y="68" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Adipocito: GLUT-4 ↑ + Síntesis TAG ↑</text>
        <text x="145" y="90" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Músculo: Glucógeno ↑ + Síntesis proteica ↑</text>
        <line x1="20" y1="102" x2="270" y2="102" stroke="#bbf7d0" stroke-width="1.5"/>
        <text x="145" y="122" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#166534" text-anchor="middle">ALMACENAMIENTO Y ANABOLISMO</text>
      </g>

      <g transform="translate(335, 55)">
        <rect x="0" y="0" width="290" height="140" rx="8" fill="#ffffff" stroke="#ea580c" stroke-width="2"/>
        <text x="145" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#c2410c" text-anchor="middle">AYUNO TEMPRANO (GLUCAGÓN ↑)</text>
        <text x="145" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Hígado: Glucogenólisis ↑ + GNG ↑</text>
        <text x="145" y="68" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Adipocito: Lipólisis masiva (ATGL/HSL)</text>
        <text x="145" y="90" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Músculo: β-Oxidación de AG (ahorra glucosa)</text>
        <line x1="20" y1="102" x2="270" y2="102" stroke="#fed7aa" stroke-width="1.5"/>
        <text x="145" y="122" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#9a3412" text-anchor="middle">MANTENIMIENTO DE LA NORMOGLUCEMIA</text>
      </g>

      <g transform="translate(25, 215)">
        <rect x="0" y="0" width="290" height="140" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="2"/>
        <text x="145" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#6d28d9" text-anchor="middle">AYUNO PROLONGADO (CETONAS ↑)</text>
        <text x="145" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Hígado: Cetogénesis acelerada</text>
        <text x="145" y="68" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Cerebro: Consume β-Hidroxibutirato (60%)</text>
        <text x="145" y="90" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Proteólisis muscular: Disminuye marcadamente</text>
        <line x1="20" y1="102" x2="270" y2="102" stroke="#ddd6fe" stroke-width="1.5"/>
        <text x="145" y="122" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#5b21b6" text-anchor="middle">PRESERVACIÓN DE LA MASA MUSCULAR</text>
      </g>

      <g transform="translate(335, 215)">
        <rect x="0" y="0" width="290" height="140" rx="8" fill="#ffffff" stroke="#dc2626" stroke-width="2"/>
        <text x="145" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#b91c1c" text-anchor="middle">EJERCICIO VIGOROSO (AMPK ↑)</text>
        <text x="145" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Músculo: Glucógeno local ➔ + ATP rápido</text>
        <text x="145" y="68" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Glucólisis anaerobia: Genera Lactato</text>
        <text x="145" y="90" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• Ciclo de Cori: Lactato ➔ Hígado ➔ Glucosa</text>
        <line x1="20" y1="102" x2="270" y2="102" stroke="#fecaca" stroke-width="1.5"/>
        <text x="145" y="122" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#991b1b" text-anchor="middle">REGENERACIÓN CONTINUA DE NAD⁺</text>
      </g>

      <g transform="translate(25, 375)">
        <rect x="0" y="0" width="600" height="145" rx="8" fill="#ffffff" stroke="#d97706" stroke-width="1.8"/>
        <text x="300" y="26" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#b45309" text-anchor="middle">LEYENDA DE FLUJOS DE COMBUSTIBLE INTERTISULAR</text>
        <text x="300" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">• Glucosa: Cerebro (obligatorio) • Eritrocitos (exclusivo) • Músculo/Hígado (almacén)</text>
        <text x="300" y="74" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">• Ácidos Grasos + Albúmina: Músculo y Miocardio en reposo • Hígado en ayuno</text>
        <text x="300" y="96" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#334155" text-anchor="middle">• Cuerpos Cetónicos: Riñón, Músculo y Adaptación Cerebral durante el ayuno</text>
        <text x="300" y="124" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#047857" text-anchor="middle">El Hígado actúa como el órgano amortiguador y distribuidor central del organismo</text>
      </g>
    </g>
    """)
    p.append('</g>')

    p.append("</g>")
    return "\n".join(p)


