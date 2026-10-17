# =============================================================================
# MÓDULO DE REVISIÓN: Estructuras Químicas del Ciclo de la Urea
# =============================================================================
# Archivo original : 04_NITROGENO_Y_AMINOACIDOS/via_14_ciclo_de_la_urea/estructuras_urea.py (líneas 1 a 360 de 360)
# Descripción      : Carbamoil-P, citrulina, argininosuccinato, arginina, ornitina, urea y NAG.
# =============================================================================

#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS VECTORIALES SVG - CICLO DE LA UREA
======================================================
Manual de Estilo Editorial Bioquímico (Estilo Glucólisis):
- 100% de los carbonos explicitados con texto ('C', 'CH', 'CH₂', 'COO⁻').
- CERO puntos o bolitas negras como átomos de carbono.
- Oxígenos en rojo (#dc2626) y nitrógenos en azul cobalto (#2563eb).
- Trazos de enlaces oscuros grafito (#0f172a, stroke-width: 2.2px).
- Grupos fosfato en cápsula naranja (#ffedd5, borde #ea580c, Ⓟ).
- Cargas y estados de ionización fisiológicos a pH 7.4.
"""

# =============================================================================
# 1. SUSTRATOS INICIALES (AMONIO Y BICARBONATO)
# =============================================================================
IONES_INICIALES = """
<g class="mol-iones-inicio" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Ion Amonio libre (NH4+) -->
  <g transform="translate(0, 0)">
    <rect x="0" y="8" width="68" height="30" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.8"/>
    <text x="34" y="29" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH₄⁺</text>
  </g>
  <text x="80" y="30" font-family="'Inter', sans-serif" font-size="16" font-weight="800" fill="#64748b" stroke="none">+</text>
  <!-- Bicarbonato (HCO3-) -->
  <g transform="translate(98, 0)">
    <rect x="0" y="8" width="76" height="30" rx="8" fill="#fef2f2" stroke="#dc2626" stroke-width="1.8"/>
    <text x="38" y="29" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">HCO₃⁻</text>
  </g>
</g>
"""

# =============================================================================
# 2. CARBAMOIL FOSFATO (1 Carbono activado)
# =============================================================================
CARBAMOIL_FOSFATO = """
<g class="mol-carbamoil-p" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo Amino (H2N) -->
  <text x="12" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">H₂N</text>
  <!-- Enlace simple N-C -->
  <line x1="28" y1="34" x2="44" y2="34" stroke="#2563eb" stroke-width="2.2"/>
  
  <!-- Carbono Carbonilo (C) -->
  <text x="52" y="38" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  
  <!-- Doble enlace C=O (arriba) -->
  <line x1="49" y1="26" x2="49" y2="12" stroke="#dc2626" stroke-width="2.2"/>
  <line x1="55" y1="26" x2="55" y2="12" stroke="#dc2626" stroke-width="2.2"/>
  <text x="52" y="8" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  
  <!-- Enlace simple C-O -->
  <line x1="60" y1="34" x2="76" y2="34" stroke="#dc2626" stroke-width="2.2"/>
  <text x="84" y="38" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  
  <!-- Enlace O-P -->
  <line x1="92" y1="34" x2="108" y2="34" stroke="#ea580c" stroke-width="2.2"/>
  <!-- Grupo Fosfato de alta energía -->
  <circle cx="122" cy="34" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2.2"/>
  <text x="122" y="39" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
</g>
"""

# =============================================================================
# 3. L-ORNITINA (5 Carbonos)
# =============================================================================
ORNITINA = """
<g class="mol-ornitina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Grupo Carboxilato (COO-) -->
  <text x="36" y="16" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="36" y1="21" x2="36" y2="35" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: Carbono Alfa (CH) -->
  <text x="36" y="47" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <!-- Grupo Amino Alfa (+NH3) -->
  <line x1="48" y1="43" x2="64" y2="43" stroke="#2563eb" stroke-width="2"/>
  <rect x="66" y="31" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
  <text x="85" y="47" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

  <!-- Enlace C2-C3 -->
  <line x1="36" y1="52" x2="36" y2="66" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C3: CH2 -->
  <text x="36" y="78" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Enlace C3-C4 -->
  <line x1="36" y1="83" x2="36" y2="97" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C4: CH2 -->
  <text x="36" y="109" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Enlace C4-C5 -->
  <line x1="36" y1="114" x2="36" y2="128" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C5: CH2 -->
  <text x="36" y="140" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Enlace C5 a Grupo Amino Delta -->
  <line x1="36" y1="145" x2="36" y2="159" stroke="#2563eb" stroke-width="2"/>
  <rect x="17" y="161" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
  <text x="36" y="177" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
</g>
"""

# =============================================================================
# 4. L-CITRULINA (6 Carbonos)
# =============================================================================
CITRULINA = """
<g class="mol-citrulina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: COO- -->
  <text x="36" y="16" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="36" y1="21" x2="36" y2="35" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: Carbono Alfa (CH) -->
  <text x="36" y="47" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <!-- Amino Alfa (+NH3) -->
  <line x1="48" y1="43" x2="64" y2="43" stroke="#2563eb" stroke-width="2"/>
  <rect x="66" y="31" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
  <text x="85" y="47" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

  <!-- Enlace C2-C3 -->
  <line x1="36" y1="52" x2="36" y2="66" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C3: CH2 -->
  <text x="36" y="78" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Enlace C3-C4 -->
  <line x1="36" y1="83" x2="36" y2="97" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C4: CH2 -->
  <text x="36" y="109" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Enlace C4-C5 -->
  <line x1="36" y1="114" x2="36" y2="128" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C5: CH2 -->
  <text x="36" y="140" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Enlace C5 a Nitrogeno Delta (NH) -->
  <line x1="36" y1="145" x2="36" y2="159" stroke="#2563eb" stroke-width="2"/>
  <text x="36" y="171" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>

  <!-- Enlace horizontal hacia Grupo Ureido -->
  <line x1="48" y1="167" x2="64" y2="167" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C6: Carbono Ureido (C) -->
  <text x="72" y="171" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>

  <!-- Doble enlace C=O (hacia abajo) -->
  <line x1="69" y1="175" x2="69" y2="189" stroke="#dc2626" stroke-width="2.2"/>
  <line x1="75" y1="175" x2="75" y2="189" stroke="#dc2626" stroke-width="2.2"/>
  <text x="72" y="202" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Enlace simple C-NH2 -->
  <line x1="80" y1="167" x2="96" y2="167" stroke="#2563eb" stroke-width="2"/>
  <text x="110" y="171" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH₂</text>
</g>
"""

# =============================================================================
# 5. L-ASPARTATO (4 Carbonos)
# =============================================================================
ASPARTATO = """
<g class="mol-aspartato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: COO- superior -->
  <text x="36" y="16" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="36" y1="21" x2="36" y2="35" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: Carbono Alfa (CH) -->
  <text x="36" y="47" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <!-- Amino Alfa (+NH3) donador al ciclo -->
  <line x1="48" y1="43" x2="64" y2="43" stroke="#2563eb" stroke-width="2"/>
  <rect x="66" y="31" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
  <text x="85" y="47" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

  <!-- Enlace C2-C3 -->
  <line x1="36" y1="52" x2="36" y2="66" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C3: CH2 -->
  <text x="36" y="78" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Enlace C3-C4 -->
  <line x1="36" y1="83" x2="36" y2="97" stroke="#dc2626" stroke-width="2.2"/>
  <!-- C4: COO- distal -->
  <text x="36" y="109" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

# =============================================================================
# 6. ARGININOSUCCINATO (10 Carbonos)
# =============================================================================
ARGININOSUCCINATO = """
<g class="mol-argininosuccinato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- PARTE IZQUIERDA: ESQUELETO DE LA CITRULINA (C1 a C5) -->
  <g transform="translate(0, 0)">
    <!-- C1: COO- -->
    <text x="36" y="16" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
    <line x1="36" y1="21" x2="36" y2="35" stroke="#0f172a" stroke-width="2.2"/>
    <!-- C2: CH -->
    <text x="36" y="47" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
    <line x1="48" y1="43" x2="64" y2="43" stroke="#2563eb" stroke-width="2"/>
    <rect x="66" y="31" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
    <text x="85" y="47" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

    <!-- C3: CH2 -->
    <line x1="36" y1="52" x2="36" y2="66" stroke="#0f172a" stroke-width="2.2"/>
    <text x="36" y="78" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

    <!-- C4: CH2 -->
    <line x1="36" y1="83" x2="36" y2="97" stroke="#0f172a" stroke-width="2.2"/>
    <text x="36" y="109" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

    <!-- C5: CH2 -->
    <line x1="36" y1="114" x2="36" y2="128" stroke="#0f172a" stroke-width="2.2"/>
    <text x="36" y="140" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

    <!-- Enlace a NH -->
    <line x1="36" y1="145" x2="36" y2="159" stroke="#2563eb" stroke-width="2"/>
    <text x="36" y="171" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>

    <!-- Enlace horizontal hacia Carbono Guanidino C6 -->
    <line x1="48" y1="167" x2="64" y2="167" stroke="#0f172a" stroke-width="2.2"/>
    <!-- C6: Carbono Central Guanidino -->
    <text x="72" y="171" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>

    <!-- Doble enlace C = ⁺NH2 (arriba) -->
    <line x1="69" y1="159" x2="69" y2="145" stroke="#2563eb" stroke-width="2.2"/>
    <line x1="75" y1="159" x2="75" y2="145" stroke="#2563eb" stroke-width="2.2"/>
    <rect x="53" y="123" width="38" height="20" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
    <text x="72" y="137" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₂</text>

    <!-- Enlace simple C6 - NH puente -->
    <line x1="80" y1="167" x2="96" y2="167" stroke="#2563eb" stroke-width="2"/>
    <text x="108" y="171" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  </g>

  <!-- PARTE DERECHA: FRAGMENTO DEL SUCCINATO / ASPARTATO (C7 a C10) -->
  <g transform="translate(108, 0)">
    <!-- Enlace NH puente a C7 (CH) -->
    <line x1="12" y1="167" x2="28" y2="167" stroke="#0f172a" stroke-width="2.2"/>
    <!-- C7: CH -->
    <text x="38" y="171" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>

    <!-- Enlace arriba C7 a C8 (COO-) -->
    <line x1="38" y1="159" x2="38" y2="145" stroke="#dc2626" stroke-width="2.2"/>
    <text x="38" y="139" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>

    <!-- Enlace abajo C7 a C9 (CH2) -->
    <line x1="38" y1="176" x2="38" y2="190" stroke="#0f172a" stroke-width="2.2"/>
    <text x="38" y="202" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

    <!-- Enlace C9 a C10 (COO-) -->
    <line x1="38" y1="207" x2="38" y2="221" stroke="#dc2626" stroke-width="2.2"/>
    <text x="38" y="233" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  </g>
</g>
"""

# =============================================================================
# 7. FUMARATO (4 Carbonos - trans-Dicarboxilato)
# =============================================================================
FUMARATO = """
<g class="mol-fumarato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: COO- superior izquierdo -->
  <text x="24" y="16" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="32" y1="22" x2="48" y2="38" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: Carbono alqueno (CH) -->
  <text x="56" y="47" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>

  <!-- Doble enlace trans C2 = C3 -->
  <line x1="66" y1="45" x2="88" y2="63" stroke="#0f172a" stroke-width="2.6"/>
  <line x1="70" y1="39" x2="92" y2="57" stroke="#0f172a" stroke-width="1.8"/>

  <!-- C3: Carbono alqueno (CH) -->
  <text x="98" y="73" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>

  <!-- C4: COO- inferior derecho -->
  <line x1="106" y1="78" x2="122" y2="94" stroke="#dc2626" stroke-width="2.2"/>
  <text x="130" y="106" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

# =============================================================================
# 8. L-ARGININA (6 Carbonos)
# =============================================================================
ARGININA = """
<g class="mol-arginina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: COO- -->
  <text x="36" y="16" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="36" y1="21" x2="36" y2="35" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: Carbono Alfa (CH) -->
  <text x="36" y="47" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <!-- Amino Alfa (+NH3) -->
  <line x1="48" y1="43" x2="64" y2="43" stroke="#2563eb" stroke-width="2"/>
  <rect x="66" y="31" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
  <text x="85" y="47" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

  <!-- Enlace C2-C3 -->
  <line x1="36" y1="52" x2="36" y2="66" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C3: CH2 -->
  <text x="36" y="78" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Enlace C3-C4 -->
  <line x1="36" y1="83" x2="36" y2="97" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C4: CH2 -->
  <text x="36" y="109" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Enlace C4-C5 -->
  <line x1="36" y1="114" x2="36" y2="128" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C5: CH2 -->
  <text x="36" y="140" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Enlace C5 a Nitrogeno Delta (NH) -->
  <line x1="36" y1="145" x2="36" y2="159" stroke="#2563eb" stroke-width="2"/>
  <text x="36" y="171" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>

  <!-- Enlace horizontal hacia Carbono Guanidino C6 -->
  <line x1="48" y1="167" x2="64" y2="167" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C6: Carbono Central Guanidino -->
  <text x="72" y="171" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>

  <!-- Doble enlace C = ⁺NH2 (arriba) -->
  <line x1="69" y1="159" x2="69" y2="145" stroke="#2563eb" stroke-width="2.2"/>
  <line x1="75" y1="159" x2="75" y2="145" stroke="#2563eb" stroke-width="2.2"/>
  <rect x="53" y="123" width="38" height="20" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
  <text x="72" y="137" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₂</text>

  <!-- Enlace simple C6 - NH2 -->
  <line x1="80" y1="167" x2="96" y2="167" stroke="#2563eb" stroke-width="2"/>
  <text x="110" y="171" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH₂</text>
</g>
"""

# =============================================================================
# 9. UREA (1 Carbono de excreción)
# =============================================================================
UREA = """
<g class="mol-urea" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Oxígeno Carbonilo (arriba) -->
  <text x="44" y="16" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <!-- Doble enlace C=O -->
  <line x1="41" y1="21" x2="41" y2="35" stroke="#dc2626" stroke-width="2.2"/>
  <line x1="47" y1="21" x2="47" y2="35" stroke="#dc2626" stroke-width="2.2"/>

  <!-- Carbono central (C) -->
  <text x="44" y="48" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>

  <!-- Enlace diagonal hacia H2N izquierdo -->
  <line x1="36" y1="52" x2="22" y2="64" stroke="#2563eb" stroke-width="2.2"/>
  <text x="12" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">H₂N</text>

  <!-- Enlace diagonal hacia NH2 derecho -->
  <line x1="52" y1="52" x2="66" y2="64" stroke="#2563eb" stroke-width="2.2"/>
  <text x="76" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH₂</text>
</g>
"""

# =============================================================================
# 10. N-ACETILGLUTAMATO (NAG - Regulador alostérico)
# =============================================================================
N_ACETILGLUTAMATO = """
<g class="mol-nag" stroke="#0f172a" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <rect x="0" y="0" width="130" height="48" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.6"/>
  <text x="65" y="20" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#15803d" stroke="none" text-anchor="middle">N-Acetilglutamato</text>
  <text x="65" y="36" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#166534" stroke="none" text-anchor="middle">⊕ Activador CPS-1</text>
</g>
"""
