#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS Y ESQUEMAS ANATÓMICOS VECTORIALES (SVG)
=============================================================
Manual de Estilo Editorial Científico del Mapa Metabólico:
- Trazos oscuros grafito (#0f172a, stroke-width: 2.2px)
- Oxígenos (C=O, OH, carboxilatos) en rojo carmesí (#dc2626)
- Grupos fosfato en cápsula naranja (#ffedd5 fondo, #ea580c borde y texto 'P')
- Grupos amino e iones de nitrógeno en azul cobalto (#2563eb / #1d4ed8)
- Enlaces y cadenas alifáticas nítidas sin cajas blancas ni emojis
- Tipografía estricta: 'Inter' para texto y 'JetBrains Mono' para fórmulas y números EC
"""

# =============================================================================
# 1. METABOLISMO DE LÍPIDOS: ESQUELETO DE GLICEROL, ACIL-COA Y ÉSTERES
# =============================================================================

# Triacilglicerol (TAG) con esqueleto de glicerol completo y 3 cadenas de acilos
TRIACILGLICEROL = """
<g class="mol-tag" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 (superior) -->
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="12" x2="88" y2="12" />
  <line x1="88" y1="12" x2="98" y2="4" />
  <line x1="88" y1="12" x2="98" y2="20" stroke="#dc2626" stroke-width="2.2" />
  <line x1="86" y1="15" x2="96" y2="23" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <!-- Cadena R1 (zig-zag saturado) -->
  <path d="M 98 4 L 110 12 L 122 4 L 134 12 L 146 4 L 158 12 L 170 4" stroke="#ea580c" stroke-width="2.2"/>
  <text x="178" y="8" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₁</text>

  <!-- Enlace vertical C1-C2 -->
  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2 (central) -->
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="42" x2="88" y2="42" />
  <line x1="88" y1="42" x2="98" y2="34" />
  <line x1="88" y1="42" x2="98" y2="50" stroke="#dc2626" stroke-width="2.2" />
  <line x1="86" y1="45" x2="96" y2="53" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <!-- Cadena R2 (con insaturación) -->
  <path d="M 98 34 L 110 42 L 122 34 L 132 44 L 145 38 L 158 48 L 170 42" stroke="#ea580c" stroke-width="2.2"/>
  <text x="178" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₂</text>

  <!-- Enlace vertical C2-C3 -->
  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C3 (inferior) -->
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="72" x2="88" y2="72" />
  <line x1="88" y1="72" x2="98" y2="64" />
  <line x1="88" y1="72" x2="98" y2="80" stroke="#dc2626" stroke-width="2.2" />
  <line x1="86" y1="75" x2="96" y2="83" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="84" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <!-- Cadena R3 -->
  <path d="M 98 64 L 110 72 L 122 64 L 134 72 L 146 64 L 158 72 L 170 64" stroke="#ea580c" stroke-width="2.2"/>
  <text x="178" y="68" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₃</text>
</g>
"""

# 2-Monoacilglicerol (2-MAG)
MONOACILGLICEROL_2 = """
<g class="mol-2mag" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 libre (-OH) -->
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>

  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2 esterificado (-O-CO-R2) -->
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="42" x2="88" y2="42" />
  <line x1="88" y1="42" x2="98" y2="34" />
  <line x1="88" y1="42" x2="98" y2="50" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 34 L 110 42 L 122 34 L 134 42 L 146 34 L 158 42 L 170 34" stroke="#ea580c" stroke-width="2.2"/>
  <text x="178" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₂</text>

  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C3 libre (-OH) -->
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>
</g>
"""

# Glicerol libre
GLICEROL_ESTRUCTURA = """
<g class="mol-glicerol-libre" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>
  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>
  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>
</g>
"""

# Lisofosfatidato (LPA / 1-Acil-glicerol-3-P)
LISOFOSFATIDATO = """
<g class="mol-lpa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="12" x2="88" y2="12" />
  <line x1="88" y1="12" x2="98" y2="4" />
  <line x1="88" y1="12" x2="98" y2="20" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 4 L 110 12 L 122 4 L 134 12 L 146 4" stroke="#ea580c" stroke-width="2.2"/>
  <text x="154" y="8" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₁</text>

  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>

  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="72" x2="84" y2="72" />
  <circle cx="98" cy="72" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="98" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
</g>
"""

# Ácido Fosfatídico (PA)
ACIDO_FOSFATIDICO = """
<g class="mol-pa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="12" x2="88" y2="12" />
  <line x1="88" y1="12" x2="98" y2="4" />
  <line x1="88" y1="12" x2="98" y2="20" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 4 L 110 12 L 122 4 L 134 12 L 146 4" stroke="#ea580c" stroke-width="2.2"/>
  <text x="154" y="8" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₁</text>

  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="42" x2="88" y2="42" />
  <line x1="88" y1="42" x2="98" y2="34" />
  <line x1="88" y1="42" x2="98" y2="50" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 34 L 110 42 L 122 34 L 134 42 L 146 34" stroke="#ea580c" stroke-width="2.2"/>
  <text x="154" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₂</text>

  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="72" x2="84" y2="72" />
  <circle cx="98" cy="72" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="98" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
</g>
"""

# 1,2-Diacilglicerol (DAG)
DIACILGLICEROL = """
<g class="mol-dag" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="12" x2="88" y2="12" />
  <line x1="88" y1="12" x2="98" y2="4" />
  <line x1="88" y1="12" x2="98" y2="20" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 4 L 110 12 L 122 4 L 134 12 L 146 4" stroke="#ea580c" stroke-width="2.2"/>
  <text x="154" y="8" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₁</text>

  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="42" x2="88" y2="42" />
  <line x1="88" y1="42" x2="98" y2="34" />
  <line x1="88" y1="42" x2="98" y2="50" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 34 L 110 42 L 122 34 L 134 42 L 146 34" stroke="#ea580c" stroke-width="2.2"/>
  <text x="154" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₂</text>

  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>
</g>
"""

# Fosfatidilcolina (PC)
FOSFATIDILCOLINA = """
<g class="mol-pc" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="12" x2="88" y2="12" />
  <line x1="88" y1="12" x2="98" y2="4" />
  <line x1="88" y1="12" x2="98" y2="20" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 4 L 110 12 L 122 4 L 134 12" stroke="#ea580c" stroke-width="2.2"/>
  <text x="142" y="8" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₁</text>

  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="42" x2="88" y2="42" />
  <line x1="88" y1="42" x2="98" y2="34" />
  <line x1="88" y1="42" x2="98" y2="50" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 34 L 110 42 L 122 34 L 134 42" stroke="#ea580c" stroke-width="2.2"/>
  <text x="142" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₂</text>

  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="72" x2="84" y2="72" />
  <circle cx="98" cy="72" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="98" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
  <line x1="98" y1="85" x2="98" y2="98" stroke="#0f172a" stroke-width="2"/>
  <text x="98" y="112" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#2563eb" stroke="none" text-anchor="middle">O–CH₂CH₂–N⁺(CH₃)₃</text>
</g>
"""

# =============================================================================
# 2. ESQUEMAS DIDÁCTICOS ANATÓMICOS: MICELA, LIPOPROTEÍNAS, ENTEROCITO
# =============================================================================

def esquema_micela_mixta(cx=0, cy=0, radio=68):
    return f"""
    <g class="esquema-micela" transform="translate({cx}, {cy})">
      <circle cx="0" cy="0" r="{radio * 0.72}" fill="#fef3c7" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6 4" opacity="0.9"/>
      <circle cx="0" cy="0" r="{radio}" fill="none" stroke="#0284c7" stroke-width="2.5" opacity="0.4"/>
      
      <g stroke="#0f172a" stroke-width="2" fill="none">
        <path d="M {radio-18} 0 L {radio} 0"/><circle cx="{radio+5}" cy="0" r="5" fill="#38bdf8" stroke="#0284c7"/>
        <path d="M {radio*0.75} {radio*0.43} L {radio*0.88} {radio*0.5}"/><circle cx="{radio*0.96}" cy="{radio*0.55}" r="5" fill="#10b981" stroke="#059669"/>
        <path d="M {radio*0.43} {radio*0.75} L {radio*0.5} {radio*0.88}"/><circle cx="{radio*0.55}" cy="{radio*0.96}" r="5" fill="#38bdf8" stroke="#0284c7"/>
        <path d="M 0 {radio-18} L 0 {radio}"/><circle cx="0" cy="{radio+5}" r="5" fill="#f59e0b" stroke="#d97706"/>
        <path d="M {-radio*0.43} {radio*0.75} L {-radio*0.5} {radio*0.88}"/><circle cx="{-radio*0.55}" cy="{radio*0.96}" r="5" fill="#38bdf8" stroke="#0284c7"/>
        <path d="M {-radio*0.75} {radio*0.43} L {-radio*0.88} {radio*0.5}"/><circle cx="{-radio*0.96}" cy="{radio*0.55}" r="5" fill="#10b981" stroke="#059669"/>
        <path d="M {-radio+18} 0 L {-radio} 0"/><circle cx="{-radio-5}" cy="0" r="5" fill="#38bdf8" stroke="#0284c7"/>
        <path d="M {-radio*0.75} {-radio*0.43} L {-radio*0.88} {-radio*0.5}"/><circle cx="{-radio*0.96}" cy="{-radio*0.55}" r="5" fill="#f59e0b" stroke="#d97706"/>
        <path d="M {-radio*0.43} {-radio*0.75} L {-radio*0.5} {-radio*0.88}"/><circle cx="{-radio*0.55}" cy="{-radio*0.96}" r="5" fill="#38bdf8" stroke="#0284c7"/>
        <path d="M 0 {-radio+18} L 0 {-radio}"/><circle cx="0" cy="{-radio-5}" r="5" fill="#10b981" stroke="#059669"/>
        <path d="M {radio*0.43} {-radio*0.75} L {radio*0.5} {-radio*0.88}"/><circle cx="{radio*0.55}" cy="{-radio*0.96}" r="5" fill="#38bdf8" stroke="#0284c7"/>
        <path d="M {radio*0.75} {-radio*0.43} L {radio*0.88} {-radio*0.5}"/><circle cx="{radio*0.96}" cy="{-radio*0.55}" r="5" fill="#f59e0b" stroke="#d97706"/>
      </g>
      
      <text x="0" y="-8" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#92400e" text-anchor="middle">MICELA MIXTA</text>
      <text x="0" y="10" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#b45309" text-anchor="middle">2-MAG + AG + Colest.</text>
      <text x="0" y="24" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#475569" text-anchor="middle">Sales Biliares (Emulsión)</text>
    </g>
    """

def esquema_lipoproteina(cx=0, cy=0, radio=68, tipo="QUILOMICRÓN", apoproteina="ApoB-48", color_apo="#dc2626"):
    return f"""
    <g class="esquema-lipoproteina" transform="translate({cx}, {cy})">
      <circle cx="0" cy="0" r="{radio}" fill="#f8fafc" stroke="#0284c7" stroke-width="2.6"/>
      <circle cx="0" cy="0" r="{radio - 12}" fill="#fef3c7" stroke="#ea580c" stroke-width="1.8" stroke-dasharray="4 3"/>
      
      <g fill="#38bdf8" stroke="#0284c7" stroke-width="1.2">
        <circle cx="0" cy="{-radio}" r="4"/>
        <circle cx="{radio*0.7}" cy="{-radio*0.7}" r="4"/>
        <circle cx="{radio}" cy="0" r="4"/>
        <circle cx="{radio*0.7}" cy="{radio*0.7}" r="4"/>
        <circle cx="0" cy="{radio}" r="4"/>
        <circle cx="{-radio*0.7}" cy="{radio*0.7}" r="4"/>
        <circle cx="{-radio}" cy="0" r="4"/>
        <circle cx="{-radio*0.7}" cy="{-radio*0.7}" r="4"/>
      </g>
      
      <g fill="#92400e" font-family="'Inter', sans-serif" text-anchor="middle">
        <text x="0" y="-8" font-size="12" font-weight="900" fill="#0f172a">{tipo}</text>
        <text x="0" y="8" font-size="9.5" font-weight="800" fill="#ea580c">Núcleo: TAG + Ésteres</text>
        <text x="0" y="22" font-size="8.5" font-weight="700" fill="#64748b">Monocapa: PL + Colesterol</text>
      </g>
      
      <path d="M {-radio*0.85} {-radio*0.4} C {-radio*0.3} {-radio*1.08} {radio*0.3} {-radio*1.08} {radio*0.85} {-radio*0.4}" 
            fill="none" stroke="{color_apo}" stroke-width="6" stroke-linecap="round"/>
      <rect x="-35" y="{-radio - 20}" width="70" height="17" rx="4" fill="{color_apo}" stroke="#0f172a" stroke-width="1.3"/>
      <text x="0" y="{-radio - 8}" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="900" fill="#ffffff" text-anchor="middle">{apoproteina}</text>
    </g>
    """

def esquema_enterocito(x, y, w=480, h=360):
    x_curr = x + 30
    pts = [f"M {x_curr} {y + 70}"]
    while x_curr < (x + w - 30):
        pts.append(f"L {x_curr} {y + 30} L {x_curr + 9} {y + 30} L {x_curr + 9} {y + 70}")
        x_curr += 16
    pts_str = " ".join(pts)
    
    return f"""
    <g class="esquema-enterocito" id="entorno_enterocito">
      <rect x="{x + 20}" y="{y + 70}" width="{w - 40}" height="{h - 80}" rx="12" fill="#eff6ff" stroke="#0284c7" stroke-width="2.6" opacity="0.9"/>
      <path d="{pts_str}" fill="#dbeafe" stroke="#0284c7" stroke-width="2.2" stroke-linejoin="round"/>
      <line x1="{x + 20}" y1="{y + 70}" x2="{x + w - 20}" y2="{y + 70}" stroke="#0284c7" stroke-width="3"/>
      <text x="{x + w/2}" y="{y + 22}" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0369a1" text-anchor="middle">BORDE EN CEPILLO (LUZ INTESTINAL)</text>
      
      <!-- Transportadores apicales -->
      <g transform="translate({x + 70}, {y + 58})">
        <rect x="0" y="0" width="36" height="20" rx="4" fill="#fed7aa" stroke="#ea580c" stroke-width="1.8"/>
        <text x="18" y="14" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="900" fill="#9a3412" text-anchor="middle">CD36</text>
        <text x="18" y="-5" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#ea580c" text-anchor="middle">AG libres</text>
      </g>
      <g transform="translate({x + w - 120}, {y + 58})">
        <rect x="0" y="0" width="48" height="20" rx="4" fill="#fef08a" stroke="#ca8a04" stroke-width="1.8"/>
        <text x="24" y="14" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="900" fill="#854d0e" text-anchor="middle">NPC1L1</text>
        <text x="24" y="-5" font-family="'Inter', sans-serif" font-size="8" font-weight="800" fill="#ca8a04" text-anchor="middle">Colest.</text>
      </g>

      <!-- REL y Reesterificación -->
      <g transform="translate({x + w/2}, {y + 150})">
        <ellipse cx="0" cy="0" rx="130" ry="46" fill="#e0e7ff" stroke="#4f46e5" stroke-width="1.8" stroke-dasharray="5 3"/>
        <text x="0" y="-22" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#3730a3" text-anchor="middle">RETÍCULO ENDOPLÁSMICO LISO</text>
        <text x="0" y="-4" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#4338ca" text-anchor="middle">MGAT: 2-MAG + Acil-CoA ➔ DAG</text>
        <text x="0" y="14" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#4338ca" text-anchor="middle">DGAT: DAG + Acil-CoA ➔ TAG</text>
      </g>

      <!-- Aparato de Golgi -->
      <g transform="translate({x + w/2}, {y + 245})">
        <path d="M -70 0 Q 0 -12 70 0 M -60 10 Q 0 -2 60 10 M -50 20 Q 0 8 50 20" fill="none" stroke="#0891b2" stroke-width="2.6" stroke-linecap="round"/>
        <text x="0" y="36" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0e7490" text-anchor="middle">Aparato de Golgi (MTP + ApoB-48)</text>
      </g>
    </g>
    """

# =============================================================================
# 3. ILUSTRACIONES ANATÓMICAS CIENTÍFICAS: MÚSCULO Y CEREBRO/NEURONA
# =============================================================================

# Fibra muscular estriada anatómica con sarcómero en contracción (Líneas Z, Actina, Miosina)
def esquema_sarcómero_muscular(cx, cy, w=580, h=260):
    """Dibuja una sección longitudinal anatómica de una miofibrilla muscular estriada con sarcómero."""
    x0 = cx - w/2
    y0 = cy - h/2
    
    # Coordenadas de las 2 líneas Z
    z1_x = cx - 180
    z2_x = cx + 180
    
    # Zig-zag de la línea Z
    def linea_z(zx):
        pts = [f"M {zx} {cy - 70}"]
        for i in range(-6, 7):
            dx = 8 if (i % 2 == 0) else -8
            pts.append(f"L {zx + dx} {cy + i * 10}")
        return " ".join(pts)
    
    return f"""
    <g class="anatomia-sarcomero" transform="translate(0, 0)">
      <!-- Vaina sarcolémica externa -->
      <rect x="{x0 + 10}" y="{y0 + 10}" width="{w - 20}" height="{h - 20}" rx="14" fill="#fff1f2" stroke="#9f1239" stroke-width="2.4"/>
      
      <!-- Túbulo T (invaginación sarcolémica) -->
      <path d="M {cx - 210} {y0 + 10} L {cx - 210} {y0 + 60} Q {cx - 210} {y0 + 75} {cx - 195} {y0 + 75} L {cx + 195} {y0 + 75} Q {cx + 210} {y0 + 75} {cx + 210} {y0 + 10}" fill="none" stroke="#be123c" stroke-width="2.2" stroke-dasharray="4 3"/>
      <text x="{cx}" y="{y0 + 32}" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#9f1239" text-anchor="middle">TÚBULO T · DESPOLARIZACIÓN Y LIBERACIÓN DE Ca²⁺</text>

      <!-- Banda I clara izquierda y derecha -->
      <rect x="{z1_x - 50}" y="{cy - 65}" width="100" height="130" fill="#ffe4e6" opacity="0.6"/>
      <rect x="{z2_x - 50}" y="{cy - 65}" width="100" height="130" fill="#ffe4e6" opacity="0.6"/>

      <!-- Banda A oscura central (superposición miosina-actina) -->
      <rect x="{cx - 130}" y="{cy - 65}" width="260" height="130" fill="#fecdd3" opacity="0.75"/>
      
      <!-- Zona H clara central y Línea M -->
      <rect x="{cx - 45}" y="{cy - 65}" width="90" height="130" fill="#fda4af" opacity="0.5"/>
      <line x1="{cx}" y1="{cy - 65}" x2="{cx}" y2="{cy + 65}" stroke="#9f1239" stroke-width="2" stroke-dasharray="3 3"/>
      <text x="{cx}" y="{cy + 82}" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#881337" text-anchor="middle">LÍNEA M</text>

      <!-- Líneas Z en zig-zag -->
      <path d="{linea_z(z1_x)}" fill="none" stroke="#be123c" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="{linea_z(z2_x)}" fill="none" stroke="#be123c" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
      <text x="{z1_x}" y="{cy - 78}" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#be123c" text-anchor="middle">LÍNEA Z</text>
      <text x="{z2_x}" y="{cy - 78}" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#be123c" text-anchor="middle">LÍNEA Z</text>

      <!-- Filamentos Delgados de Actina (anclados en Z) -->
      <g stroke="#e11d48" stroke-width="2.5" stroke-linecap="round">
        <!-- Desde Z1 hacia el centro -->
        <line x1="{z1_x}" y1="{cy - 40}" x2="{cx - 30}" y2="{cy - 40}"/>
        <line x1="{z1_x}" y1="{cy - 20}" x2="{cx - 30}" y2="{cy - 20}"/>
        <line x1="{z1_x}" y1="{cy}" x2="{cx - 30}" y2="{cy}"/>
        <line x1="{z1_x}" y1="{cy + 20}" x2="{cx - 30}" y2="{cy + 20}"/>
        <line x1="{z1_x}" y1="{cy + 40}" x2="{cx - 30}" y2="{cy + 40}"/>
        <!-- Desde Z2 hacia el centro -->
        <line x1="{z2_x}" y1="{cy - 40}" x2="{cx + 30}" y2="{cy - 40}"/>
        <line x1="{z2_x}" y1="{cy - 20}" x2="{cx + 30}" y2="{cy - 20}"/>
        <line x1="{z2_x}" y1="{cy}" x2="{cx + 30}" y2="{cy}"/>
        <line x1="{z2_x}" y1="{cy + 20}" x2="{cx + 30}" y2="{cy + 20}"/>
        <line x1="{z2_x}" y1="{cy + 40}" x2="{cx + 30}" y2="{cy + 40}"/>
      </g>

      <!-- Filamentos Gruesos de Miosina (centrales con cabezas moleculares) -->
      <g stroke="#9f1239" stroke-width="4.5" stroke-linecap="round">
        <line x1="{cx - 120}" y1="{cy - 30}" x2="{cx + 120}" y2="{cy - 30}"/>
        <line x1="{cx - 120}" y1="{cy - 10}" x2="{cx + 120}" y2="{cy - 10}"/>
        <line x1="{cx - 120}" y1="{cy + 10}" x2="{cx + 120}" y2="{cy + 10}"/>
        <line x1="{cx - 120}" y1="{cy + 30}" x2="{cx + 120}" y2="{cy + 30}"/>
      </g>
      <!-- Cabezas moleculares de miosina (puentes cruzados) -->
      <g fill="#be123c">
        <circle cx="{cx - 80}" cy="{cy - 35}" r="3"/><circle cx="{cx - 50}" cy="{cy - 35}" r="3"/><circle cx="{cx + 50}" cy="{cy - 35}" r="3"/><circle cx="{cx + 80}" cy="{cy - 35}" r="3"/>
        <circle cx="{cx - 80}" cy="{cy + 35}" r="3"/><circle cx="{cx - 50}" cy="{cy + 35}" r="3"/><circle cx="{cx + 50}" cy="{cy + 35}" r="3"/><circle cx="{cx + 80}" cy="{cy + 35}" r="3"/>
      </g>

      <!-- Flechas indicadoras de contracción (acortamiento sarcomérico) -->
      <g fill="none" stroke="#9f1239" stroke-width="2">
        <path d="M {z1_x + 15} {cy + 82} L {z1_x + 60} {cy + 82}" marker-end="url(#arrowRed)"/>
        <path d="M {z2_x - 15} {cy + 82} L {z2_x - 60} {cy + 82}" marker-end="url(#arrowRed)"/>
        <text x="{cx}" y="{cy + 108}" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#9f1239" text-anchor="middle">DESLIZAMIENTO ACTINA-MIOSINA (CONSUMO DE ATP)</text>
      </g>
    </g>
    """

# Ilustración anatómica del encéfalo y de la neurona con axón mielinizado
def esquema_cerebro_y_neurona_didactico(x, y, w=620, h=420):
    """Genera el dibujo anatómico de hemisferio cerebral, cerebelo y neurona mielinizada con flujo didáctico."""
    return f"""
    <g class="anatomia-cerebro-neurona" transform="translate({x}, {y})">
      <!-- Tarjeta base ambiental -->
      <rect x="0" y="0" width="{w}" height="{h}" rx="14" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5"/>
      <text x="{w/2}" y="28" font-family="'Inter', sans-serif" font-size="13.5" font-weight="900" fill="#1e40af" text-anchor="middle">SISTEMA NERVIOSO CENTRAL: BARRERA HEMATOENCEFÁLICA Y NEURONA</text>

      <!-- 1. DIBUJO VECTORIAL DEL ENCÉFALO (Hemisferio + Cerebelo + Tronco) -->
      <g transform="translate(40, 50)">
        <!-- Hemisferio cerebral con circunvoluciones y cisuras nítidas -->
        <path d="M 40 100 C 20 80 20 50 45 35 C 70 20 110 15 145 25 C 180 15 220 25 240 50 C 260 70 265 105 245 125 C 235 145 200 155 175 145 C 150 155 110 150 85 140 C 60 145 40 130 40 100 Z" 
              fill="#dbeafe" stroke="#2563eb" stroke-width="2.6"/>
        
        <!-- Giros y surcos cerebrales (detalles anatómicos continuos) -->
        <g fill="none" stroke="#60a5fa" stroke-width="2" stroke-linecap="round">
          <path d="M 65 45 Q 90 60 115 40 Q 140 60 165 35"/>
          <path d="M 55 75 Q 85 90 120 70 Q 155 90 190 65 Q 220 75 235 60"/>
          <path d="M 60 110 Q 95 125 135 105 Q 175 125 210 100"/>
          <path d="M 85 135 Q 120 145 155 130 Q 185 140 220 125"/>
        </g>
        
        <!-- Cerebelo posterior con estriaciones (folias cerebelosas) -->
        <ellipse cx="230" cy="138" rx="36" ry="24" fill="#bfdbfe" stroke="#2563eb" stroke-width="2.4"/>
        <g fill="none" stroke="#3b82f6" stroke-width="1.6" stroke-linecap="round">
          <path d="M 205 130 Q 230 138 255 130"/>
          <path d="M 200 138 Q 230 146 260 138"/>
          <path d="M 205 146 Q 230 154 255 146"/>
        </g>
        <text x="140" y="162" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#1d4ed8" text-anchor="middle">Hemisferio Cerebral</text>
        <text x="230" y="166" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#1e40af" text-anchor="middle">Cerebelo</text>
      </g>

      <!-- 2. DIBUJO ANATÓMICO DE LA NEURONA MULTIPOLAR CON AXÓN Y MIELINA -->
      <g transform="translate(350, 45)">
        <!-- Soma neuronal estrellado/piramidal -->
        <path d="M 60 60 L 40 40 M 60 65 L 30 65 M 60 70 L 40 90 M 70 80 L 60 110" stroke="#2563eb" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Dendritas apicales y basales ramificadas -->
        <g stroke="#3b82f6" stroke-width="1.8" stroke-linecap="round" fill="none">
          <path d="M 40 40 L 25 30 M 40 40 L 30 45"/>
          <path d="M 30 65 L 15 55 M 30 65 L 15 75"/>
          <path d="M 40 90 L 25 95 M 40 90 L 30 105"/>
        </g>
        <!-- Cuerpo celular (soma) y núcleo -->
        <circle cx="70" cy="70" r="16" fill="#bfdbfe" stroke="#2563eb" stroke-width="2.5"/>
        <circle cx="70" cy="70" r="6" fill="#1d4ed8"/>
        <text x="70" y="44" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#1d4ed8" text-anchor="middle">Soma</text>

        <!-- Cono axónico y axón longitudinal -->
        <line x1="86" y1="70" x2="240" y2="70" stroke="#2563eb" stroke-width="3" stroke-linecap="round"/>

        <!-- Vainas de Mielina (Oligodendrocitos) y Nódulos de Ranvier -->
        <g fill="#dbeafe" stroke="#2563eb" stroke-width="2">
          <!-- Vaina 1 -->
          <rect x="96" y="58" width="34" height="24" rx="6"/>
          <!-- Vaina 2 -->
          <rect x="140" y="58" width="34" height="24" rx="6"/>
          <!-- Vaina 3 -->
          <rect x="184" y="58" width="34" height="24" rx="6"/>
        </g>
        <text x="157" y="50" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#2563eb" text-anchor="middle">Vaina de Mielina</text>
        <text x="135" y="94" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="700" fill="#475569" text-anchor="middle">Nódulo Ranvier</text>

        <!-- Botones sinápticos terminales -->
        <g stroke="#2563eb" stroke-width="2" fill="#bfdbfe">
          <line x1="240" y1="70" x2="255" y2="55"/><circle cx="257" cy="53" r="3.5"/>
          <line x1="240" y1="70" x2="260" y2="70"/><circle cx="262" cy="70" r="3.5"/>
          <line x1="240" y1="70" x2="255" y2="85"/><circle cx="257" cy="87" r="3.5"/>
        </g>
      </g>

      <!-- 3. FLUJO DIDÁCTICO SIN TEXTO INFINITO (Normoglucemia vs Ayuno) -->
      <g transform="translate(25, 230)">
        <!-- Capilar y Barrera Hematoencefálica con GLUT-1 -->
        <rect x="0" y="0" width="570" height="70" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="2"/>
        <text x="285" y="22" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0369a1" text-anchor="middle">BARRERA HEMATOENCEFÁLICA (BHE) &amp; TRANSPORTE CAPILAR</text>
        <text x="285" y="42" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">• GLUT-1 (Endotelio capilar) ➔ GLUT-3 (Neurona, Km = 1.6 mM, alta afinidad permanente)</text>
        <text x="285" y="60" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">Exclusión de ácidos grasos unidos a albúmina (baja penetración BHE)</text>
      </g>

      <g transform="translate(25, 312)">
        <!-- Normoglucemia vs Ayuno Prolongado -->
        <rect x="0" y="0" width="280" height="90" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
        <text x="140" y="22" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#15803d" text-anchor="middle">ESTADO NORMOALIMENTADO</text>
        <text x="140" y="42" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">Glucosa = Combustible Principal</text>
        <text x="140" y="60" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#16a34a" text-anchor="middle">Glucólisis ➔ Krebs ➔ ATP</text>
        <text x="140" y="76" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#475569" text-anchor="middle">Mantiene bombas Na⁺/K⁺-ATPasa</text>

        <rect x="290" y="0" width="280" height="90" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="2"/>
        <text x="430" y="22" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#6d28d9" text-anchor="middle">AYUNO PROLONGADO (> 48 H)</text>
        <text x="430" y="42" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">Inducción de Transportador MCT</text>
        <text x="430" y="60" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#7c3aed" text-anchor="middle">β-Hidroxibutirato ➔ 2 Acetil-CoA</text>
        <text x="430" y="76" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#475569" text-anchor="middle">Aporta hasta el 60-70% del ATP cerebral</text>
      </g>
    </g>
    """

# =============================================================================
# 4. BIOSÍNTESIS DE AMINOÁCIDOS: ESTRUCTURAS VECTORIALES
# =============================================================================

L_SERINA = """
<g class="mol-l-serina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="38" />
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="32" y1="48" x2="20" y2="48" />
  <text x="14" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  <line x1="48" y1="48" x2="60" y2="48" stroke="#2563eb" stroke-width="2"/>
  <rect x="62" y="36" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="81" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
  <line x1="40" y1="56" x2="40" y2="72" />
  <text x="40" y="85" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="40" y1="89" x2="40" y2="102" />
  <text x="40" y="115" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">OH</text>
</g>
"""

L_CISTEINA = """
<g class="mol-l-cisteina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="38" />
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="32" y1="48" x2="20" y2="48" />
  <text x="14" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  <line x1="48" y1="48" x2="60" y2="48" stroke="#2563eb" stroke-width="2"/>
  <rect x="62" y="36" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="81" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
  <line x1="40" y1="56" x2="40" y2="72" />
  <text x="40" y="85" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="40" y1="89" x2="40" y2="102" />
  <text x="40" y="115" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#d97706" stroke="none" text-anchor="middle">SH</text>
</g>
"""

L_GLICINA = """
<g class="mol-l-glicina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />
  <text x="40" y="54" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="56" y1="50" x2="70" y2="50" stroke="#2563eb" stroke-width="2"/>
  <rect x="72" y="38" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="91" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
</g>
"""

L_ASPARAGINA = """
<g class="mol-l-asparagina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="38" />
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="32" y1="48" x2="20" y2="48" />
  <text x="14" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  <line x1="48" y1="48" x2="60" y2="48" stroke="#2563eb" stroke-width="2"/>
  <rect x="62" y="36" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="81" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
  <line x1="40" y1="56" x2="40" y2="72" />
  <text x="40" y="85" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="40" y1="89" x2="40" y2="104" />
  <text x="40" y="117" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="48" y1="113" x2="64" y2="113" stroke="#dc2626" stroke-width="2"/>
  <line x1="48" y1="117" x2="64" y2="117" stroke="#dc2626" stroke-width="2"/>
  <text x="70" y="120" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="32" y1="113" x2="18" y2="113" stroke="#2563eb" stroke-width="2"/>
  <text x="12" y="118" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="end">H₂N</text>
</g>
"""

L_PROLINA = """
<g class="mol-l-prolina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="40,40 68,52 58,82 22,82 12,52" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">N⁺H₂</text>
  <line x1="68" y1="52" x2="88" y2="40" stroke="#0f172a" stroke-width="2.2"/>
  <text x="94" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
"""
