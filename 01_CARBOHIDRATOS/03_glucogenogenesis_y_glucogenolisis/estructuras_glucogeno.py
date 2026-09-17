"""
CATÁLOGO DE ESTRUCTURAS QUÍMICAS (SVG) - METABOLISMO DEL GLUCÓGENO
===================================================================
Estructuras con rigor editorial universitario (Haworth, valencias y cofactores):
1. GLUCOSA_6_FOSFATO (G-6-P) - Precursor de entrada desde la glucólisis.
2. GLUCOSA_1_FOSFATO (G-1-P) - Producto de la fosfoglucomutasa con fosfato en C1-α.
3. UDP_GLUCOSA (Uridina Difosfato Glucosa) - Glucosa activada con enlace pirofosfato a uridina.
4. CADENA_GLUCOGENO_ALFA_1_4_Y_1_6 - Estructura polimérica detallada mostrando los enlaces
   glicosídicos α(1→4) lineales y el punto de ramificación α(1→6), además del núcleo de Glucogenina.
"""

# 1. GLUCOSA-6-FOSFATO (G6P)
GLUCOSA_6_FOSFATO = """
  <!-- Anillo Piranosa de 6 lados -->
  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Oxígeno del anillo -->
  <circle cx="16" cy="22" r="7" fill="#ffffff"/>
  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>

  <!-- Carbono 6 con Grupo Fosfato en C6 -->
  <line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="0" cy="-2" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="0" y="3" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle">Ⓟ</text>
  <text x="-20" y="2" fill="#ea580c" font-size="9" font-weight="700" text-anchor="end">O-PO₃²⁻</text>

  <!-- C1 (derecha: -OH) -->
  <line x1="72" y1="36" x2="88" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="98" y="40" fill="#0f172a" font-size="11" font-weight="700">OH</text>

  <!-- C2 (abajo derecha: -OH) -->
  <line x1="50" y1="58" x2="50" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="50" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">OH</text>

  <!-- C3 (abajo izquierda: -OH) -->
  <line x1="16" y1="58" x2="16" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="16" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">HO</text>

  <!-- C4 (izquierda: -OH) -->
  <line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="-24" y="40" fill="#0f172a" font-size="11" font-weight="700">HO</text>
"""


# 2. α-D-GLUCOSA-1-FOSFATO (G-1-P)
GLUCOSA_1_FOSFATO = """
  <!-- Anillo Piranosa -->
  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Oxígeno del anillo -->
  <circle cx="16" cy="22" r="7" fill="#ffffff"/>
  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>

  <!-- C6: -CH2OH libre arriba -->
  <line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2.2"/>
  <text x="0" y="7" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂OH</text>

  <!-- C1: Configuración ALFA con Grupo Fosfato hacia ABAJO -->
  <line x1="72" y1="36" x2="88" y2="52" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="72" y1="36" x2="84" y2="24" stroke="#0f172a" stroke-width="1.6"/>
  <text x="91" y="22" fill="#64748b" font-size="9" font-weight="700">H</text>

  <!-- Cápsula de Fosfato en C1 -->
  <circle cx="102" cy="62" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="102" y="67" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle">Ⓟ</text>
  <text x="122" y="66" fill="#ea580c" font-size="9" font-weight="700">O-PO₃²⁻</text>
  <text x="102" y="86" fill="#ea580c" font-size="8.5" font-weight="800" text-anchor="middle">(C1-α)</text>

  <!-- C2 (abajo derecha: -OH) -->
  <line x1="50" y1="58" x2="50" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="50" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">OH</text>

  <!-- C3 (abajo izquierda: -OH) -->
  <line x1="16" y1="58" x2="16" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="16" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">HO</text>

  <!-- C4 (izquierda: -OH) -->
  <line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="-24" y="40" fill="#0f172a" font-size="11" font-weight="700">HO</text>
"""


# 3. UDP-GLUCOSA (Uridina Difosfato Glucosa)
UDP_GLUCOSA = """
  <!-- 1. Anillo de Glucosa (Izquierda) -->
  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
  <circle cx="16" cy="22" r="7" fill="#ffffff"/>
  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>
  
  <line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2"/>
  <text x="0" y="7" fill="#0f172a" font-size="10.5" font-weight="800" text-anchor="middle">CH₂OH</text>
  <line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="-22" y="40" fill="#0f172a" font-size="10" font-weight="700">HO</text>
  <line x1="16" y1="58" x2="16" y2="70" stroke="#0f172a" stroke-width="2"/>
  <text x="16" y="81" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">HO</text>
  <line x1="50" y1="58" x2="50" y2="70" stroke="#0f172a" stroke-width="2"/>
  <text x="50" y="81" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">OH</text>

  <!-- 2. Puente Pirofosfato (-O-P-O-P-O-) en C1 -->
  <line x1="72" y1="36" x2="92" y2="48" stroke="#0f172a" stroke-width="2"/>
  <!-- Fosfato 1 (α) -->
  <circle cx="106" cy="54" r="12" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="106" y="58" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
  <line x1="118" y1="54" x2="132" y2="54" stroke="#0f172a" stroke-width="2"/>
  <!-- Fosfato 2 (β) -->
  <circle cx="144" cy="54" r="12" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="144" y="58" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
  
  <!-- Enlace hacia la Ribosa -->
  <line x1="156" y1="54" x2="175" y2="46" stroke="#0f172a" stroke-width="2"/>

  <!-- 3. Anillo de Ribofuranosa (5 lados) -->
  <polygon points="190,20 215,30 205,56 175,56 170,30" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="190" cy="20" r="5" fill="#ffffff"/>
  <text x="190" y="24" fill="#dc2626" font-size="11" font-weight="800" text-anchor="middle">O</text>
  <!-- 2'-OH y 3'-OH -->
  <line x1="175" y1="56" x2="175" y2="68" stroke="#0f172a" stroke-width="1.6"/>
  <text x="175" y="77" fill="#0f172a" font-size="9" font-weight="700" text-anchor="middle">OH</text>
  <line x1="205" y1="56" x2="205" y2="68" stroke="#0f172a" stroke-width="1.6"/>
  <text x="205" y="77" fill="#0f172a" font-size="9" font-weight="700" text-anchor="middle">OH</text>

  <!-- 4. Base Nitrogenada: Uracilo (Pirimidina) -->
  <line x1="215" y1="30" x2="230" y2="24" stroke="#0f172a" stroke-width="2"/>
  <!-- Anillo de Uracilo -->
  <rect x="230" y="10" width="38" height="32" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="2"/>
  <text x="249" y="26" fill="#0369a1" font-size="10.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">URACILO</text>
  <text x="249" y="37" fill="#0284c7" font-size="8" font-weight="700" text-anchor="middle">(Base)</text>
"""


# 4. POLÍMERO DE GLUCÓGENO (ENLACES α-1,4 Y RAMIFICACIÓN α-1,6)
CADENA_GLUCOGENO = """
  <!-- A) Glucosa 1 de la cadena principal -->
  <g transform="translate(0, 40)">
    <polygon points="40,16 58,28 40,46 14,46 0,28 14,16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
    <circle cx="14" cy="16" r="5" fill="#ffffff"/>
    <text x="14" y="20" fill="#dc2626" font-size="10" font-weight="800" text-anchor="middle">O</text>
    <line x1="0" y1="28" x2="0" y2="8" stroke="#0f172a" stroke-width="1.8"/>
    <text x="0" y="4" fill="#0f172a" font-size="8" font-weight="700" text-anchor="middle">CH₂OH</text>
  </g>

  <!-- Enlace α(1→4) glicosídico -->
  <path d="M 58 68 Q 72 78 86 68" fill="none" stroke="#ea580c" stroke-width="2.5"/>
  <circle cx="72" cy="73" r="4" fill="#ffffff"/>
  <text x="72" y="76" fill="#dc2626" font-size="9" font-weight="900" text-anchor="middle">O</text>
  <text x="72" y="90" fill="#c2410c" font-size="9" font-weight="800" text-anchor="middle">α(1→4)</text>

  <!-- B) Glucosa 2 de la cadena principal (Punto de Ramificación) -->
  <g transform="translate(86, 40)">
    <polygon points="40,16 58,28 40,46 14,46 0,28 14,16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
    <circle cx="14" cy="16" r="5" fill="#ffffff"/>
    <text x="14" y="20" fill="#dc2626" font-size="10" font-weight="800" text-anchor="middle">O</text>
    
    <!-- C6 modificado: forma el enlace α(1→6) hacia arriba -->
    <line x1="0" y1="28" x2="0" y2="10" stroke="#0f172a" stroke-width="2"/>
    <text x="0" y="4" fill="#d97706" font-size="8.5" font-weight="800" text-anchor="middle">-CH₂-</text>
  </g>

  <!-- Enlace α(1→6) hacia la rama superior -->
  <path d="M 86 36 Q 86 16 110 0" fill="none" stroke="#d97706" stroke-width="2.5"/>
  <circle cx="86" cy="16" r="4" fill="#ffffff"/>
  <text x="86" y="19" fill="#dc2626" font-size="9" font-weight="900" text-anchor="middle">O</text>
  <text x="56" y="18" fill="#d97706" font-size="9" font-weight="800">α(1→6)</text>

  <!-- C) Glucosa en la rama superior -->
  <g transform="translate(110, -35)">
    <polygon points="40,16 58,28 40,46 14,46 0,28 14,16" fill="#fefce8" stroke="#d97706" stroke-width="2"/>
    <circle cx="14" cy="16" r="5" fill="#ffffff"/>
    <text x="14" y="20" fill="#dc2626" font-size="10" font-weight="800" text-anchor="middle">O</text>
    <line x1="0" y1="28" x2="0" y2="8" stroke="#0f172a" stroke-width="1.8"/>
    <text x="0" y="4" fill="#0f172a" font-size="8" font-weight="700" text-anchor="middle">CH₂OH</text>
    <text x="68" y="28" fill="#b45309" font-size="9" font-weight="700">Extremo no reductor</text>
  </g>

  <!-- Enlace α(1→4) continuo en la cadena principal -->
  <path d="M 144 68 Q 158 78 172 68" fill="none" stroke="#ea580c" stroke-width="2.5"/>
  <circle cx="158" cy="73" r="4" fill="#ffffff"/>
  <text x="158" y="76" fill="#dc2626" font-size="9" font-weight="900" text-anchor="middle">O</text>
  <text x="158" y="90" fill="#c2410c" font-size="9" font-weight="800" text-anchor="middle">α(1→4)</text>

  <!-- D) Glucosa 3 de la cadena principal hacia el núcleo -->
  <g transform="translate(172, 40)">
    <polygon points="40,16 58,28 40,46 14,46 0,28 14,16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
    <circle cx="14" cy="16" r="5" fill="#ffffff"/>
    <text x="14" y="20" fill="#dc2626" font-size="10" font-weight="800" text-anchor="middle">O</text>
    <line x1="0" y1="28" x2="0" y2="8" stroke="#0f172a" stroke-width="1.8"/>
    <text x="0" y="4" fill="#0f172a" font-size="8" font-weight="700" text-anchor="middle">CH₂OH</text>
  </g>

  <!-- E) Núcleo de la Proteína GLUCOGENINA (Primer autoglicosilante) -->
  <g transform="translate(250, 48)">
    <circle cx="28" cy="20" r="24" fill="#fef08a" stroke="#ca8a04" stroke-width="2.5"/>
    <text x="28" y="16" fill="#854d0e" font-size="9.5" font-weight="900" text-anchor="middle">GLUCOGENINA</text>
    <text x="28" y="28" fill="#a16207" font-size="8" font-weight="700" text-anchor="middle">(Tyr-194)</text>
    <line x1="-20" y1="20" x2="4" y2="20" stroke="#ca8a04" stroke-width="2.2" stroke-dasharray="3 2"/>
  </g>
"""
