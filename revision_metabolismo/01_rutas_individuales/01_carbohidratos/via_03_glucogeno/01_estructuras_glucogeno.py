# =============================================================================
# MÓDULO DE REVISIÓN: Estructuras del Metabolismo del Glucógeno
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/via_03_glucogenogenesis_y_glucogenolisis/estructuras_glucogeno.py (líneas 1 a 334 de 334)
# Descripción      : G1P, UDP-Glucosa, gránulo de glucógeno y enlaces alfa-1,4 / alfa-1,6.
# =============================================================================

"""
CATÁLOGO DE ESTRUCTURAS QUÍMICAS (SVG) - METABOLISMO DEL GLUCÓGENO
===================================================================
Estructuras con rigor editorial universitario (Haworth, valencias y cofactores):
1. GLUCOSA_6_FOSFATO (G-6-P) - Precursor de entrada desde la glucólisis.
2. GLUCOSA_1_FOSFATO (G-1-P) - Producto de la fosfoglucomutasa con fosfato en C1-α.
3. UDP_GLUCOSA (Uridina Difosfato Glucosa) - Glucosa activada con enlace pirofosfato a uridina.
4. CEBADOR_GLUCOGENINA - Estructura molecular real del dímero de Glucogenina con su residuo
   Tyr-194 y la cadena cebadora autoglucosilada de unidades α(1→4) con extremo libre 4-OH.
5. LUPA_MECANISMO_CEBADOR - Lupa de aumento molecular que muestra el bolsillo catalítico
   de la Glucógeno Sintasa, el ataque nucleofílico del 4-OH sobre el C1 de la UDP-Glucosa
   y la salida del grupo UDP.
6. CADENA_GLUCOGENO - Estructura polimérica ramificada mostrando los enlaces α(1→4) lineales
   y el punto de ramificación α(1→6).
7. PARTICULA_GRANULO_GLUCOGENO - Dibujo anatómico del gránulo de glucógeno citoplasmático
   (partícula de inclusión) anclada entre túbulos del retículo endoplásmico liso.
"""

# 1. GLUCOSA-6-FOSFATO (G6P)
GLUCOSA_6_FOSFATO = """
  <!-- Anillo Piranosa de 6 lados -->
  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
  <circle cx="16" cy="22" r="7" fill="#ffffff"/>
  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle" stroke="none">O</text>

  <line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="0" cy="-2" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="0" y="3" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle" stroke="none">Ⓟ</text>
  <text x="-20" y="2" fill="#ea580c" font-size="9" font-weight="700" text-anchor="end" stroke="none">O-PO₃²⁻</text>

  <line x1="72" y1="36" x2="88" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="98" y="40" fill="#0f172a" font-size="11" font-weight="700" stroke="none">OH</text>
  <line x1="50" y1="58" x2="50" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="50" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle" stroke="none">OH</text>
  <line x1="16" y1="58" x2="16" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="16" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle" stroke="none">HO</text>
  <line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="-24" y="40" fill="#0f172a" font-size="11" font-weight="700" stroke="none">HO</text>
"""

# 2. α-D-GLUCOSA-1-FOSFATO (G-1-P)
GLUCOSA_1_FOSFATO = """
  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
  <circle cx="16" cy="22" r="7" fill="#ffffff"/>
  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle" stroke="none">O</text>

  <line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2.2"/>
  <text x="0" y="7" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle" stroke="none">CH₂OH</text>

  <!-- C1: Configuración ALFA con Grupo Fosfato hacia ABAJO -->
  <line x1="72" y1="36" x2="88" y2="52" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="72" y1="36" x2="84" y2="24" stroke="#0f172a" stroke-width="1.6"/>
  <text x="91" y="22" fill="#64748b" font-size="9" font-weight="700" stroke="none">H</text>

  <circle cx="102" cy="62" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="102" y="67" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle" stroke="none">Ⓟ</text>
  <text x="122" y="66" fill="#ea580c" font-size="9" font-weight="700" stroke="none">O-PO₃²⁻</text>
  <text x="102" y="86" fill="#ea580c" font-size="8.5" font-weight="800" text-anchor="middle" stroke="none">(C1-α)</text>

  <line x1="50" y1="58" x2="50" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="50" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle" stroke="none">OH</text>
  <line x1="16" y1="58" x2="16" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="16" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle" stroke="none">HO</text>
  <line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="-24" y="40" fill="#0f172a" font-size="11" font-weight="700" stroke="none">HO</text>
"""

# 3. UDP-GLUCOSA (Uridina Difosfato Glucosa)
UDP_GLUCOSA = """
  <!-- 1. Anillo de Glucosa -->
  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
  <circle cx="16" cy="22" r="7" fill="#ffffff"/>
  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle" stroke="none">O</text>
  
  <line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2"/>
  <text x="0" y="7" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle" stroke="none">CH₂OH</text>
  <line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="-22" y="40" fill="#0f172a" font-size="10" font-weight="700" stroke="none">HO</text>
  <line x1="16" y1="58" x2="16" y2="70" stroke="#0f172a" stroke-width="2"/>
  <text x="16" y="81" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle" stroke="none">HO</text>
  <line x1="50" y1="58" x2="50" y2="70" stroke="#0f172a" stroke-width="2"/>
  <text x="50" y="81" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle" stroke="none">OH</text>

  <!-- 2. Puente Pirofosfato (-O-P-O-P-O-) en C1 -->
  <line x1="72" y1="36" x2="90" y2="48" stroke="#0f172a" stroke-width="2"/>
  <circle cx="104" cy="54" r="12" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="104" y="58" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle" stroke="none">Ⓟ</text>
  <line x1="116" y1="54" x2="128" y2="54" stroke="#0f172a" stroke-width="2"/>
  <circle cx="140" cy="54" r="12" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="140" y="58" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle" stroke="none">Ⓟ</text>
  
  <line x1="152" y1="54" x2="168" y2="46" stroke="#0f172a" stroke-width="2"/>

  <!-- 3. Anillo de Ribofuranosa -->
  <polygon points="182,20 206,30 196,56 168,56 163,30" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="182" cy="20" r="5" fill="#ffffff"/>
  <text x="182" y="24" fill="#dc2626" font-size="11" font-weight="800" text-anchor="middle" stroke="none">O</text>
  <line x1="168" y1="56" x2="168" y2="68" stroke="#0f172a" stroke-width="1.6"/>
  <text x="168" y="77" fill="#0f172a" font-size="8.5" font-weight="700" text-anchor="middle" stroke="none">OH</text>
  <line x1="196" y1="56" x2="196" y2="68" stroke="#0f172a" stroke-width="1.6"/>
  <text x="196" y="77" fill="#0f172a" font-size="8.5" font-weight="700" text-anchor="middle" stroke="none">OH</text>

  <!-- 4. Base Nitrogenada: Uracilo -->
  <line x1="206" y1="30" x2="220" y2="24" stroke="#0f172a" stroke-width="2"/>
  <rect x="220" y="10" width="36" height="30" rx="5" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.8"/>
  <text x="238" y="25" fill="#0369a1" font-size="9.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle" stroke="none">URACILO</text>
  <text x="238" y="35" fill="#0284c7" font-size="7.5" font-weight="700" text-anchor="middle" stroke="none">(Base)</text>
"""

# 4. CEBADOR MOLECULAR DE GLUCOGENINA (ESTRUCTURA QUÍMICA REAL)
CEBADOR_GLUCOGENINA = """
  <!-- Dímero Proteico de Glucogenina -->
  <g transform="translate(0, 10)">
    <ellipse cx="40" cy="35" rx="38" ry="30" fill="#fef9c3" stroke="#ca8a04" stroke-width="2.2"/>
    <ellipse cx="65" cy="55" rx="32" ry="26" fill="#fef08a" stroke="#ca8a04" stroke-width="2"/>
    <text x="45" y="32" fill="#854d0e" font-size="11" font-weight="900" text-anchor="middle" stroke="none">GLUCOGENINA</text>
    <text x="45" y="44" fill="#a16207" font-size="8.5" font-weight="700" text-anchor="middle" stroke="none">(Dímero 37 kDa)</text>
    
    <!-- Residuo Tirosina-194 -->
    <g transform="translate(75, 20)">
      <line x1="0" y1="15" x2="16" y2="15" stroke="#854d0e" stroke-width="2"/>
      <polygon points="16,15 22,8 34,8 40,15 34,22 22,22" fill="#ffffff" stroke="#854d0e" stroke-width="1.8"/>
      <text x="28" y="17" fill="#854d0e" font-size="6.5" font-weight="800" text-anchor="middle" stroke="none">Tyr</text>
      <line x1="40" y1="15" x2="52" y2="15" stroke="#dc2626" stroke-width="2.2"/>
      <circle cx="46" cy="15" r="3.5" fill="#ffffff"/>
      <text x="46" y="17.5" fill="#dc2626" font-size="7.5" font-weight="900" text-anchor="middle" stroke="none">O</text>
      <text x="28" y="33" fill="#a16207" font-size="8" font-weight="800" text-anchor="middle" stroke="none">Tyr-194</text>
    </g>
  </g>

  <!-- Cadena Cebadora Autoglucosilada (Glucosa 1 hasta 8) -->
  <g transform="translate(135, 10)">
    <polygon points="30,12 44,22 30,34 10,34 0,22 10,12" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/>
    <circle cx="10" cy="12" r="3.5" fill="#ffffff"/>
    <text x="10" y="14.5" fill="#dc2626" font-size="7" font-weight="800" text-anchor="middle" stroke="none">O</text>
    <text x="22" y="25" fill="#64748b" font-size="8" font-weight="700" text-anchor="middle" stroke="none">Glc₁</text>
  </g>

  <path d="M 179 32 Q 190 39 201 32" fill="none" stroke="#ea580c" stroke-width="2"/>
  <text x="190" y="37" fill="#dc2626" font-size="7" font-weight="800" text-anchor="middle" stroke="none">O</text>

  <g transform="translate(201, 10)">
    <polygon points="30,12 44,22 30,34 10,34 0,22 10,12" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/>
    <circle cx="10" cy="12" r="3.5" fill="#ffffff"/>
    <text x="10" y="14.5" fill="#dc2626" font-size="7" font-weight="800" text-anchor="middle" stroke="none">O</text>
    <text x="22" y="25" fill="#64748b" font-size="8" font-weight="700" text-anchor="middle" stroke="none">Glc₂</text>
  </g>

  <path d="M 245 32 Q 256 39 267 32" fill="none" stroke="#ea580c" stroke-width="2"/>
  <text x="256" y="37" fill="#dc2626" font-size="7" font-weight="800" text-anchor="middle" stroke="none">O</text>

  <text x="278" y="25" fill="#d97706" font-size="12" font-weight="900" stroke="none">···</text>

  <!-- Glucosa Terminal (Glc8) con extremo 4-OH libre -->
  <g transform="translate(295, 10)">
    <polygon points="30,12 44,22 30,34 10,34 0,22 10,12" fill="#fefce8" stroke="#ea580c" stroke-width="2"/>
    <circle cx="10" cy="12" r="3.5" fill="#ffffff"/>
    <text x="10" y="14.5" fill="#dc2626" font-size="7" font-weight="800" text-anchor="middle" stroke="none">O</text>
    <text x="22" y="25" fill="#ea580c" font-size="8" font-weight="800" text-anchor="middle" stroke="none">Glc₈</text>
    
    <!-- Extremo 4-OH aceptor -->
    <line x1="0" y1="22" x2="-10" y2="22" stroke="#ea580c" stroke-width="2"/>
    <rect x="-42" y="13" width="30" height="18" rx="4" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5"/>
    <text x="-27" y="25" fill="#b91c1c" font-size="9" font-weight="900" text-anchor="middle" stroke="none">4-OH</text>
  </g>
"""

# 5. LUPA DE ZOOM MOLECULAR: ACOPLAMIENTO ENTRE CEBADOR Y GLUCÓGENO SINTASA
LUPA_MECANISMO_CEBADOR = """
  <!-- Marco Circular de la Lupa de Aumento -->
  <circle cx="0" cy="0" r="105" fill="#ffffff" stroke="#ea580c" stroke-width="3.5"/>
  <circle cx="0" cy="0" r="100" fill="#f8fafc" stroke="#fed7aa" stroke-width="1"/>

  <!-- Bolsillo Catalítico de la Glucógeno Sintasa (Cleft proteico) -->
  <path d="M -85,-40 C -40,-75 40,-75 85,-40 C 95,-10 80,70 50,85 C 0,95 -60,85 -85,50 Z" 
        fill="#eff6ff" stroke="#3b82f6" stroke-width="2" stroke-dasharray="6 3"/>
  <text x="0" y="-72" fill="#1d4ed8" font-size="9.5" font-weight="900" text-anchor="middle" stroke="none">
    BOLSILLO ACTIVO: GLUCÓGENO SINTASA
  </text>

  <!-- 1. Extremo No Reductor del Cebador (Izquierda dentro de la lupa) -->
  <g transform="translate(-65, -15)">
    <polygon points="26,10 38,20 26,30 8,30 0,20 8,10" fill="#fefce8" stroke="#ea580c" stroke-width="2"/>
    <circle cx="8" cy="10" r="3" fill="#ffffff"/>
    <text x="8" y="12.5" fill="#dc2626" font-size="6.5" font-weight="800" text-anchor="middle" stroke="none">O</text>
    <text x="18" y="23" fill="#9a3412" font-size="7.5" font-weight="800" text-anchor="middle" stroke="none">Glc(n)</text>
    
    <!-- Oxígeno 4-OH nucleofílico -->
    <circle cx="-2" cy="20" r="5" fill="#fee2e2" stroke="#dc2626" stroke-width="1.8"/>
    <text x="-2" y="23" fill="#b91c1c" font-size="8" font-weight="900" text-anchor="middle" stroke="none">O:⁻</text>
    <text x="-2" y="34" fill="#dc2626" font-size="7" font-weight="800" text-anchor="middle" stroke="none">4-OH</text>
  </g>

  <!-- Flecha de Ataque Nucleofílico hacia el Carbono 1 de la UDP-Glucosa -->
  <path d="M -60 5 Q -25 -15 5 -5" fill="none" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arrowRed)"/>
  <text x="-28" y="-14" fill="#dc2626" font-size="7.5" font-weight="900" text-anchor="middle" stroke="none">Ataque Sn2</text>

  <!-- 2. Molécula entrante de UDP-Glucosa (Derecha dentro de la lupa) -->
  <g transform="translate(10, -25)">
    <!-- Glucosa entrante -->
    <polygon points="26,10 38,20 26,30 8,30 0,20 8,10" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
    <circle cx="8" cy="10" r="3" fill="#ffffff"/>
    <text x="8" y="12.5" fill="#dc2626" font-size="6.5" font-weight="800" text-anchor="middle" stroke="none">O</text>
    <text x="18" y="23" fill="#0f172a" font-size="7.5" font-weight="800" text-anchor="middle" stroke="none">Glc</text>
    <!-- Carbono 1 electrophilic -->
    <circle cx="0" cy="20" r="3" fill="#fed7aa"/>
    <text x="0" y="31" fill="#ea580c" font-size="7" font-weight="900" text-anchor="middle" stroke="none">C1-α</text>

    <!-- Enlace saliente hacia el UDP -->
    <line x1="38" y1="20" x2="52" y2="20" stroke="#0284c7" stroke-width="2" stroke-dasharray="3 2"/>
    <circle cx="58" cy="20" r="8" fill="#dbeafe" stroke="#0284c7" stroke-width="1.5"/>
    <text x="58" y="23" fill="#0369a1" font-size="7" font-weight="900" text-anchor="middle" stroke="none">UDP</text>
    <text x="58" y="34" fill="#0284c7" font-size="6.5" font-weight="700" text-anchor="middle" stroke="none">(Sale)</text>
  </g>

  <!-- 3. Formación del nuevo enlace α(1→4) y salida de UDP -->
  <g transform="translate(0, 48)">
    <rect x="-85" y="-12" width="170" height="24" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
    <text x="0" y="3" fill="#15803d" font-size="8.5" font-weight="800" text-anchor="middle" stroke="none">
      Nuevo Enlace α(1→4) Creado + UDP Libre
    </text>
  </g>

  <!-- Etiqueta de la lupa -->
  <rect x="-65" y="86" width="130" height="15" rx="4" fill="#0f172a" opacity="0.9"/>
  <text x="0" y="97" fill="#ffffff" font-size="7.5" font-weight="800" text-anchor="middle" letter-spacing="0.5" stroke="none">
    MECANISMO DE ELONGACIÓN
  </text>
"""

# 6. POLÍMERO DE GLUCÓGENO RAMIFICADO COMPLETO
CADENA_GLUCOGENO = """
  <!-- Glucosa 1 principal -->
  <g transform="translate(0, 40)">
    <polygon points="40,16 58,28 40,46 14,46 0,28 14,16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
    <circle cx="14" cy="16" r="5" fill="#ffffff"/>
    <text x="14" y="20" fill="#dc2626" font-size="10" font-weight="800" text-anchor="middle" stroke="none">O</text>
    <line x1="0" y1="28" x2="0" y2="8" stroke="#0f172a" stroke-width="1.8"/>
    <text x="0" y="4" fill="#0f172a" font-size="8" font-weight="700" text-anchor="middle" stroke="none">CH₂OH</text>
  </g>

  <!-- Enlace α(1→4) -->
  <path d="M 58 68 Q 72 78 86 68" fill="none" stroke="#ea580c" stroke-width="2.5"/>
  <circle cx="72" cy="73" r="4" fill="#ffffff"/>
  <text x="72" y="76" fill="#dc2626" font-size="9" font-weight="900" text-anchor="middle" stroke="none">O</text>
  <text x="72" y="90" fill="#c2410c" font-size="9" font-weight="800" text-anchor="middle" stroke="none">α(1→4)</text>

  <!-- Glucosa 2 de ramificación -->
  <g transform="translate(86, 40)">
    <polygon points="40,16 58,28 40,46 14,46 0,28 14,16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
    <circle cx="14" cy="16" r="5" fill="#ffffff"/>
    <text x="14" y="20" fill="#dc2626" font-size="10" font-weight="800" text-anchor="middle" stroke="none">O</text>
    <line x1="0" y1="28" x2="0" y2="10" stroke="#0f172a" stroke-width="2"/>
    <text x="0" y="4" fill="#d97706" font-size="8.5" font-weight="800" text-anchor="middle" stroke="none">-CH₂-</text>
  </g>

  <!-- Enlace α(1→6) -->
  <path d="M 86 36 Q 86 16 110 0" fill="none" stroke="#d97706" stroke-width="2.5"/>
  <circle cx="86" cy="16" r="4" fill="#ffffff"/>
  <text x="86" y="19" fill="#dc2626" font-size="9" font-weight="900" text-anchor="middle" stroke="none">O</text>
  <text x="56" y="18" fill="#d97706" font-size="9" font-weight="800" stroke="none">α(1→6)</text>

  <!-- Glucosa en la rama superior -->
  <g transform="translate(110, -35)">
    <polygon points="40,16 58,28 40,46 14,46 0,28 14,16" fill="#fefce8" stroke="#d97706" stroke-width="2"/>
    <circle cx="14" cy="16" r="5" fill="#ffffff"/>
    <text x="14" y="20" fill="#dc2626" font-size="10" font-weight="800" text-anchor="middle" stroke="none">O</text>
    <line x1="0" y1="28" x2="0" y2="8" stroke="#0f172a" stroke-width="1.8"/>
    <text x="0" y="4" fill="#0f172a" font-size="8" font-weight="700" text-anchor="middle" stroke="none">CH₂OH</text>
    <text x="68" y="28" fill="#b45309" font-size="8.5" font-weight="700" stroke="none">Extremo no reductor</text>
  </g>

  <path d="M 144 68 Q 158 78 172 68" fill="none" stroke="#ea580c" stroke-width="2.5"/>
  <circle cx="158" cy="73" r="4" fill="#ffffff"/>
  <text x="158" y="76" fill="#dc2626" font-size="9" font-weight="900" text-anchor="middle" stroke="none">O</text>
  <text x="158" y="90" fill="#c2410c" font-size="9" font-weight="800" text-anchor="middle" stroke="none">α(1→4)</text>

  <g transform="translate(172, 40)">
    <polygon points="40,16 58,28 40,46 14,46 0,28 14,16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
    <circle cx="14" cy="16" r="5" fill="#ffffff"/>
    <text x="14" y="20" fill="#dc2626" font-size="10" font-weight="800" text-anchor="middle" stroke="none">O</text>
    <line x1="0" y1="28" x2="0" y2="8" stroke="#0f172a" stroke-width="1.8"/>
    <text x="0" y="4" fill="#0f172a" font-size="8" font-weight="700" text-anchor="middle" stroke="none">CH₂OH</text>
  </g>

  <g transform="translate(250, 48)">
    <circle cx="28" cy="20" r="24" fill="#fef08a" stroke="#ca8a04" stroke-width="2.5"/>
    <text x="28" y="16" fill="#854d0e" font-size="9.5" font-weight="900" text-anchor="middle" stroke="none">GLUCOGENINA</text>
    <text x="28" y="28" fill="#a16207" font-size="8" font-weight="700" text-anchor="middle" stroke="none">(Tyr-194)</text>
    <line x1="-20" y1="20" x2="4" y2="20" stroke="#ca8a04" stroke-width="2.2" stroke-dasharray="3 2"/>
  </g>
"""

# 7. EL GRÁNULO CITOSÓLICO DE INCLUSIÓN (BIOLOGÍA CELULAR REAL)
GRANULO_CITOSOLICO_INCLUSION = """
  <!-- Gránulo esférico densamente ramificado (Inclusión Citoplasmática ~20-30 nm) -->
  <g transform="translate(0, 0)">
    <!-- Fondo del cuerpo de inclusión -->
    <circle cx="65" cy="65" r="58" fill="#fffbeb" stroke="#d97706" stroke-width="2.5" stroke-dasharray="6 3"/>
    <circle cx="65" cy="65" r="48" fill="#fef3c7" opacity="0.6"/>
    
    <!-- Centro del gránulo: Dímero de Glucogenina -->
    <circle cx="65" cy="65" r="10" fill="#ca8a04"/>
    <text x="65" y="68" fill="#ffffff" font-size="7" font-weight="900" text-anchor="middle" stroke="none">GLG</text>

    <!-- Ramas concéntricas de glucosa (12 niveles concéntricos) -->
    <g fill="#d97706" opacity="0.85">
      <!-- Nivel 1 -->
      <circle cx="52" cy="55" r="3.5"/><circle cx="78" cy="55" r="3.5"/><circle cx="52" cy="75" r="3.5"/><circle cx="78" cy="75" r="3.5"/>
      <!-- Nivel 2 -->
      <circle cx="40" cy="45" r="3"/><circle cx="90" cy="45" r="3"/><circle cx="40" cy="85" r="3"/><circle cx="90" cy="85" r="3"/>
      <circle cx="65" cy="38" r="3"/><circle cx="65" cy="92" r="3"/><circle cx="38" cy="65" r="3"/><circle cx="92" cy="65" r="3"/>
      <!-- Nivel 3 (superficie externa con extremos no reductores) -->
      <circle cx="30" cy="35" r="2.5"/><circle cx="100" cy="35" r="2.5"/><circle cx="30" cy="95" r="2.5"/><circle cx="100" cy="95" r="2.5"/>
      <circle cx="65" cy="20" r="2.5"/><circle cx="65" cy="110" r="2.5"/><circle cx="20" cy="65" r="2.5"/><circle cx="110" cy="65" r="2.5"/>
      <circle cx="45" cy="24" r="2.5"/><circle cx="85" cy="24" r="2.5"/><circle cx="45" cy="106" r="2.5"/><circle cx="85" cy="106" r="2.5"/>
    </g>

    <!-- Líneas de ramificación -->
    <g stroke="#d97706" stroke-width="1.2" opacity="0.6">
      <line x1="65" y1="65" x2="52" y2="55"/><line x1="65" y1="65" x2="78" y2="55"/>
      <line x1="65" y1="65" x2="52" y2="75"/><line x1="65" y1="65" x2="78" y2="75"/>
      <line x1="52" y1="55" x2="40" y2="45"/><line x1="78" y1="55" x2="90" y2="45"/>
      <line x1="52" y1="75" x2="40" y2="85"/><line x1="78" y1="75" x2="90" y2="85"/>
    </g>

    <!-- Enzimas asociadas ancladas a la superficie del gránulo -->
    <rect x="95" y="45" width="28" height="16" rx="4" fill="#fed7aa" stroke="#ea580c" stroke-width="1.2"/>
    <text x="109" y="56" fill="#c2410c" font-size="7" font-weight="900" text-anchor="middle" stroke="none">SINTASA</text>

    <rect x="5" y="70" width="34" height="16" rx="4" fill="#fecdd3" stroke="#e11d48" stroke-width="1.2"/>
    <text x="22" y="81" fill="#9f1239" font-size="6.5" font-weight="900" text-anchor="middle" stroke="none">FOSFORILASA</text>
  </g>
"""
