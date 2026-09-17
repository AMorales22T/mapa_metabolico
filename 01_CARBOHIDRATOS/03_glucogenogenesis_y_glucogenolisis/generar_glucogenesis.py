#!/usr/bin/env python3
"""
GENERADOR DE LA RUTA DE LA GLUCOGÉNESIS (SÍNTESIS DE GLUCÓGENO)
===============================================================
Ruta completa generada bajo el estándar editorial de Glucólisis y Pentosas:
1. Conexión biológica de entrada: Glucosa-6-Fosfato proveniente de la Glucólisis.
2. Reacción 1: Fosfoglucomutasa (G-6-P ⇄ G-1-P) con cofactor Glucosa-1,6-BP.
3. Reacción 2: UDP-Glucosa Pirofosforilasa (G-1-P + UTP ➔ UDP-Glucosa + PPi).
   Acoplada a la Pirofosfatasa Inorgánica (PPi + H2O ➔ 2 Pi) que impulsa la síntesis.
4. Cebador: Núcleo proteico de Glucogenina (Tyr-194).
5. Reacción 3: Glucógeno Sintasa (Elongación de cadenas con enlaces α-1,4).
6. Reacción 4: Enzima Ramificadora del Glucógeno (Amilo-α(1,4→1,6)-transglucosidasa).
7. Entorno celular: Membrana, citoesqueleto, polirribosomas y vesículas en citosol.
"""

import os
from estructuras_glucogeno import (
    GLUCOSA_6_FOSFATO,
    GLUCOSA_1_FOSFATO,
    UDP_GLUCOSA,
    CADENA_GLUCOGENO
)

ANCHO = 1000
ALTO = 2100

CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ruta de la Glucogénesis - Síntesis de Glucógeno en Citosol</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #e2e8f0;
      color: #0f172a;
      padding: 30px 15px;
      display: flex;
      flex-direction: column;
      align-items: center;
    }}
    .lienzo-svg {{
      width: 1000px;
      background: #ffffff;
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
      overflow: hidden;
    }}
    svg {{ display: block; width: 100%; height: auto; }}
  </style>
</head>
<body>
  <div class="lienzo-svg">
    <svg width="{ANCHO}" height="{ALTO}" viewBox="0 0 {ANCHO} {ALTO}" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Marcadores de flujo -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>
        <marker id="arrowAmber" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#d97706" />
        </marker>

        <!-- Gradiente Citosólico Biológico -->
        <linearGradient id="gradCitosolGlucogeno" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%" stop-color="#ffffff" stop-opacity="1" />
          <stop offset="15%" stop-color="#f8fafc" stop-opacity="0.8" />
          <stop offset="50%" stop-color="#fffbeb" stop-opacity="0.35" />
          <stop offset="85%" stop-color="#f8fafc" stop-opacity="0.8" />
          <stop offset="100%" stop-color="#ffffff" stop-opacity="1" />
        </linearGradient>
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

def generar_entorno_celular_glucogeno():
    """Genera la ambientación celular: citoesqueleto, ribosomas, vesículas y membrana."""
    return f"""
    <!-- Fondo acuoso del citosol -->
    <rect x="0" y="0" width="{ANCHO}" height="{ALTO}" fill="url(#gradCitosolGlucogeno)"/>

    <!-- Membrana plasmática biológica (borde superior) -->
    <g opacity="0.85">
      <path d="M 0 60 Q 250 45 500 55 T 1000 50" fill="none" stroke="#0284c7" stroke-width="6"/>
      <path d="M 0 68 Q 250 53 500 63 T 1000 58" fill="none" stroke="#38bdf8" stroke-width="2.5" stroke-dasharray="6 4"/>
      <g fill="#0284c7" opacity="0.6">
        <circle cx="80" cy="56" r="2.5"/><circle cx="95" cy="57" r="2.5"/><circle cx="110" cy="58" r="2.5"/>
        <circle cx="450" cy="54" r="2.5"/><circle cx="465" cy="55" r="2.5"/><circle cx="480" cy="56" r="2.5"/>
        <circle cx="820" cy="51" r="2.5"/><circle cx="835" cy="52" r="2.5"/><circle cx="850" cy="53" r="2.5"/>
      </g>
    </g>

    <!-- Filamentos de Citoesqueleto que cruzan el citoplasma -->
    <g opacity="0.32" stroke="#94a3b8" fill="none">
      <path d="M 40 180 Q 300 120 600 190 T 960 160" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 50 480 Q 350 540 650 490 T 950 510" stroke-width="1.5" stroke-dasharray="7 7"/>
      <path d="M 40 920 Q 280 860 620 930 T 960 890" stroke-width="1.6" stroke-dasharray="8 5"/>
      <path d="M 60 1380 Q 340 1440 680 1390 T 950 1410" stroke-width="1.5" stroke-dasharray="8 6"/>
      <path d="M 50 1820 Q 350 1760 650 1830 T 960 1790" stroke-width="1.6" stroke-dasharray="6 6"/>
    </g>

    <!-- Polirribosomas flotando en el citosol -->
    <g fill="#94a3b8" opacity="0.25">
      <circle cx="140" cy="140" r="2.5"/><circle cx="146" cy="142" r="2"/><circle cx="144" cy="148" r="2.3"/>
      <circle cx="820" cy="220" r="2.5"/><circle cx="826" cy="222" r="2"/><circle cx="824" cy="228" r="2.3"/>
      <circle cx="150" cy="720" r="2.5"/><circle cx="156" cy="722" r="2"/><circle cx="154" cy="728" r="2.3"/>
      <circle cx="880" cy="1150" r="2.5"/><circle cx="886" cy="1152" r="2"/><circle cx="884" cy="1158" r="2.3"/>
      <circle cx="140" cy="1620" r="2.5"/><circle cx="146" cy="1622" r="2"/><circle cx="144" cy="1628" r="2.3"/>
    </g>

    <!-- Vesículas citosólicas translúcidas -->
    <g opacity="0.28">
      <circle cx="180" cy="380" r="22" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="180" cy="380" r="16" fill="none" stroke="#7dd3fc" stroke-width="1"/>
      <circle cx="850" cy="820" r="24" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="850" cy="820" r="17" fill="none" stroke="#fbbf24" stroke-width="1"/>
      <circle cx="160" cy="1250" r="26" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="160" cy="1250" r="19" fill="none" stroke="#7dd3fc" stroke-width="1"/>
    </g>
    """

def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False):
    """Bloque SVG de metabolito alineado con estilo editorial."""
    if texto_izquierda:
        pos_estructura = "translate(150, 0)"
        pos_texto = "translate(130, 25)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = "translate(135, 25)"
        alineacion = ''

    return f"""
    <!-- Metabolito: {nombre} -->
    <g transform="translate({x}, {y})">
      <g transform="{pos_estructura}">
        {svg_estructura}
      </g>
      <g transform="{pos_texto}">
        <text x="0" y="0" fill="#0f172a" font-size="16" font-weight="800" {alineacion}>{nombre}</text>
        <text x="0" y="18" fill="#ea580c" font-size="12" font-weight="700" {alineacion}>{carbonos}</text>
        <text x="0" y="34" fill="#64748b" font-size="11" {alineacion}>{detalle}</text>
      </g>
    </g>
    """

def main():
    contenido_svg = []

    # 1. Capa de entorno biológico
    contenido_svg.append(generar_entorno_celular_glucogeno())

    # =========================================================================
    # ENTRADA BIOLÓGICA Y CONECTOR DESDE LA GLUCÓLISIS
    # =========================================================================
    # Anuncio de conexión: esta flecha muestra de dónde viene en el citosol global
    contenido_svg.append("""
    <!-- Conector de Entrada desde la Glucólisis -->
    <g transform="translate(480, 85)">
      <!-- Flecha horizontal que entra desde la derecha (donde está el eje de Glucólisis) -->
      <path d="M 380 0 L 120 0" fill="none" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <rect x="135" y="-14" width="230" height="26" rx="13" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
      <text x="250" y="3" fill="#c2410c" font-size="10.5" font-weight="800" text-anchor="middle">
        PROVIENE DE LA GLUCÓLISIS (G-6-P)
      </text>
    </g>
    """)

    # =========================================================================
    # METABOLITO 1: GLUCOSA-6-FOSFATO (PUNTO DE PARTIDA)
    # =========================================================================
    X_EJE = 380
    Y_G6P = 140

    contenido_svg.append(crear_metabolito(
        x=340, y=Y_G6P,
        nombre="Glucosa-6-Fosfato",
        carbonos="6 Carbonos (Hexosa Ⓟ)",
        detalle="Substrato inicial desviado al almacén",
        svg_estructura=GLUCOSA_6_FOSFATO
    ))

    # =========================================================================
    # REACCIÓN 1: FOSFOGLUCOMUTASA (ISOMERIZACIÓN DEL FOSFATO C6 ⇄ C1)
    # =========================================================================
    # Reacción reversible con el cofactor Glucosa-1,6-Bisfosfato
    contenido_svg.append("""
    <!-- Reacción: Fosfoglucomutasa -->
    <g transform="translate(385, 275)">
      <line x1="-3" y1="0" x2="-3" y2="52" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="52" x2="3" y2="0" stroke="#ea580c" stroke-width="1.8" marker-end="url(#arrowFlow)"/>
      
      <!-- Cofactor acoplado (G-1,6-BP) -->
      <path d="M -65 10 Q -25 10 -4 20" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-70" y="13" fill="#475569" font-size="10" font-weight="800" text-anchor="end">Ser-OH Fosforilada</text>
      <path d="M -4 30 Q -25 42 -65 42" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-70" y="45" fill="#475569" font-size="9.5" font-weight="700" text-anchor="end">(Interm. G-1,6-BP)</text>

      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">Fosfoglucomutasa</text>
        <text x="0" y="14" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 5.4.2.2 (Mg²⁺, Reversible ⇄)</text>
        <text x="0" y="28" fill="#d97706" font-size="9.5" font-weight="700">Mecanismo: Transferencia intramolecular de Ⓟ</text>
      </g>
    </g>
    """)

    # =========================================================================
    # METABOLITO 2: α-D-GLUCOSA-1-FOSFATO (G-1-P)
    # =========================================================================
    Y_G1P = 385

    contenido_svg.append(crear_metabolito(
        x=340, y=Y_G1P,
        nombre="α-D-Glucosa-1-Fosfato",
        carbonos="6 Carbonos (Fosfato en C1-α)",
        detalle="Fosfato activo en carbono anomérico",
        svg_estructura=GLUCOSA_1_FOSFATO
    ))

    # =========================================================================
    # REACCIÓN 2: UDP-GLUCOSA PIROFOSFORILASA + PIROFOSFATASA INORGÁNICA
    # =========================================================================
    # Este paso consume UTP y genera PPi, que es rápidamente hidrolizado por la
    # pirofosfatasa inorgánica (desplazamiento termodinámico irreversible)
    contenido_svg.append("""
    <!-- Reacción: UDP-Glucosa Pirofosforilasa -->
    <g transform="translate(385, 545)">
      <line x1="0" y1="0" x2="0" y2="70" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de UTP -->
      <path d="M -75 12 Q -25 12 -4 24" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-80" y="15" fill="#dc2626" font-size="11" font-weight="800" text-anchor="end">- 1 UTP</text>

      <!-- Salida de PPi -->
      <path d="M -4 36 Q -25 48 -75 48" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-80" y="52" fill="#475569" font-size="10.5" font-weight="800" text-anchor="end">+ PPᵢ (Pirofosfato)</text>

      <!-- ACOPLAMIENTO EXERGÓNICO: Pirofosfatasa Inorgánica -->
      <path d="M -80 60 Q -110 75 -130 65" fill="none" stroke="#059669" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
      <g transform="translate(-85, 78)">
        <text x="0" y="0" fill="#059669" font-size="9.5" font-weight="800" text-anchor="end">PPᵢ + H₂O ➔ 2 Pᵢ</text>
        <text x="0" y="12" fill="#047857" font-size="8.5" font-weight="700" text-anchor="end">ΔG'° = -19.2 kJ/mol (Irreversible)</text>
      </g>

      <g transform="translate(20, 20)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">UDP-Glucosa Pirofosforilasa</text>
        <text x="0" y="14" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 2.7.7.9 (Mg²⁺)</text>
        <text x="0" y="28" fill="#16a34a" font-size="9.5" font-weight="700">⊕ Impulsada por hidrólisis de PPᵢ</text>
      </g>
    </g>
    """)

    # =========================================================================
    # METABOLITO 3: UDP-GLUCOSA (DONADOR ACTIVADO DE MONÓMEROS)
    # =========================================================================
    Y_UDPG = 690

    contenido_svg.append(crear_metabolito(
        x=280, y=Y_UDPG,
        nombre="UDP-Glucosa",
        carbonos="Nucleótido-Azúcar activado",
        detalle="Donador de glucosa de alta energía libre",
        svg_estructura=UDP_GLUCOSA
    ))

    # =========================================================================
    # CEBADOR BIOLÓGICO: GLUCOGENINA (EL INICIO DE LA PARTÍCULA)
    # =========================================================================
    contenido_svg.append("""
    <!-- Cuadro explicativo del cebador Glucogenina -->
    <g transform="translate(250, 860)">
      <rect x="0" y="0" width="500" height="90" rx="8" fill="#fefce8" stroke="#ca8a04" stroke-width="1.8"/>
      
      <!-- Icono proteína dímero -->
      <g transform="translate(35, 45)">
        <circle cx="0" cy="0" r="22" fill="#fde047" stroke="#a16207" stroke-width="2"/>
        <text x="0" y="4" fill="#713f12" font-size="9.5" font-weight="900" text-anchor="middle">GLG</text>
      </g>

      <g transform="translate(80, 25)">
        <text x="0" y="0" fill="#854d0e" font-size="12" font-weight="900">CEBADOR REQUERIDO: PROTEÍNA GLUCOGENINA (EC 2.4.1.186)</text>
        <text x="0" y="16" fill="#713f12" font-size="10" font-weight="600">
          La Glucógeno Sintasa NO puede iniciar cadenas de novo; requiere un cebador.
        </text>
        <text x="0" y="32" fill="#a16207" font-size="9.5" font-weight="700">
          • La Glucogenina se autoglucosila en su Tyr-194 uniendo hasta 8 residuos de glucosa.
        </text>
        <text x="0" y="47" fill="#64748b" font-size="9">
          • Una vez formado el cebador (Glucosa)₈, la Glucógeno Sintasa toma el control.
        </text>
      </g>
    </g>
    """)

    # =========================================================================
    # REACCIÓN 3: GLUCÓGENO SINTASA (ELONGACIÓN LINEAL α-1,4)
    # =========================================================================
    contenido_svg.append("""
    <!-- Reacción: Glucógeno Sintasa -->
    <g transform="translate(385, 980)">
      <line x1="0" y1="0" x2="0" y2="65" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

      <!-- Salida de UDP libre que será fosforilado a UTP por el ATP -->
      <path d="M -4 30 Q -25 42 -75 42" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrowBlue)"/>
      <text x="-80" y="45" fill="#0284c7" font-size="11" font-weight="800" text-anchor="end">+ UDP libre</text>
      <text x="-80" y="58" fill="#64748b" font-size="9" text-anchor="end">(Regenerable: UDP + ATP ⇄ UTP + ADP)</text>

      <g transform="translate(20, 16)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">Glucógeno Sintasa</text>
        <text x="0" y="14" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">EC 2.4.1.11 (Paso Limitante Clave)</text>
        <text x="0" y="28" fill="#16a34a" font-size="9.5" font-weight="700">⊕ Insulina (vía Fosfoproteína Fosfatasa PP1), G-6-P</text>
        <text x="0" y="41" fill="#e11d48" font-size="9.5" font-weight="700">⊣ Glucagón, Adrenalina (vía PKA / GSK-3 fosforilante)</text>
      </g>
    </g>
    """)

    # =========================================================================
    # REACCIÓN 4: ENZIMA RAMIFICADORA DEL GLUCÓGENO (AMILO α-1,4 ➔ α-1,6)
    # =========================================================================
    contenido_svg.append("""
    <!-- Reacción: Enzima Ramificadora -->
    <g transform="translate(385, 1130)">
      <line x1="0" y1="0" x2="0" y2="55" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

      <g transform="translate(20, 14)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800">Enzima Ramificadora del Glucógeno</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace">Amilo-α(1,4→1,6)-transglucosidasa (EC 2.4.1.18)</text>
        <text x="0" y="27" fill="#b45309" font-size="9.5" font-weight="700">Corta bloque de 6-7 glucosas y lo une en C6 formando rama α(1→6)</text>
        <text x="0" y="40" fill="#64748b" font-size="9">Genera ramificaciones cada 8 a 12 glucosas (aumenta solubilidad y velocidad de degradación)</text>
      </g>
    </g>
    """)

    # =========================================================================
    # PRODUCTO FINAL: EL POLÍMERO DE GLUCÓGENO RAMIFICADO
    # =========================================================================
    Y_GLUC = 1270

    contenido_svg.append(f"""
    <!-- Polímero de Glucógeno Completo -->
    <g transform="translate(260, {Y_GLUC})">
      <g transform="translate(0, 40)">
        {CADENA_GLUCOGENO}
      </g>
      <g transform="translate(380, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="17" font-weight="900">Glucógeno (n + 1)</text>
        <text x="0" y="18" fill="#d97706" font-size="12" font-weight="800">Polisacárido de Reserva Energética</text>
        <text x="0" y="34" fill="#64748b" font-size="10.5">Enlaces principales: α(1→4) glicosídicos</text>
        <text x="0" y="48" fill="#b45309" font-size="10.5" font-weight="700">Puntos de ramificación: α(1→6) cada 8-12 glucosas</text>
        <text x="0" y="63" fill="#64748b" font-size="10">Partícula esférica citoplasmática (Gránulos β en músculo e hígado)</text>
      </g>
    </g>
    """)

    # =========================================================================
    # RESUMEN BIOENERGÉTICO Y CONEXIÓN CON LA GLUCOGENÓLISIS
    # =========================================================================
    contenido_svg.append("""
    <g transform="translate(200, 1580)">
      <rect x="0" y="0" width="600" height="150" rx="10" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.8"/>
      
      <text x="20" y="26" fill="#0f172a" font-size="13" font-weight="900">BALANCE ENERGÉTICO DE LA GLUCOGÉNESIS</text>
      <text x="20" y="48" fill="#475569" font-size="11" font-weight="700">
        Glucosa + ATP + UTP + Glucógeno(n) + H₂O ➔ Glucógeno(n+1) + ADP + UDP + 2 Pᵢ
      </text>
      <text x="20" y="70" fill="#b91c1c" font-size="10.5" font-weight="700">
        • Costo energético neto: 2 enlaces fosfato de alta energía (1 ATP en Hexoquinasa + 1 UTP en UDPG-Pirofosforilasa).
      </text>
      <text x="20" y="90" fill="#047857" font-size="10.5" font-weight="700">
        • Eficiencia de almacenamiento: ~97% de la energía original de la glucosa se conserva en el gránulo.
      </text>

      <line x1="20" y1="108" x2="580" y2="108" stroke="#cbd5e1" stroke-width="1"/>
      
      <!-- Anticipo de la Glucogenólisis -->
      <g transform="translate(20, 128)">
        <text x="0" y="0" fill="#d97706" font-size="10.5" font-weight="800">
          ⇄ RETORNO A GLUCOLISIS (GLUCOGENÓLISIS):
        </text>
        <text x="260" y="0" fill="#64748b" font-size="10">
          Glucógeno Fosforilasa (+ Pᵢ) libera G-1-P sin gastar ATP ➔ Fosfoglucomutasa ➔ G-6-P.
        </text>
      </g>
    </g>
    """)

    # Ensamblar todo
    html_final = CABECERA_HTML + "\n".join(contenido_svg) + PIE_HTML

    ruta_salida = os.path.join(os.path.dirname(__file__), "Glucogenesis.html")
    with open(ruta_salida, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"✅ Lámina de la Glucogénesis generada con éxito en: {ruta_salida}")

if __name__ == "__main__":
    main()
