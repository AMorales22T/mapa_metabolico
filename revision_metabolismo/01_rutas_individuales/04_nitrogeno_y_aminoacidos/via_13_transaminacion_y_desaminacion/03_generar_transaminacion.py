# =============================================================================
# MÓDULO DE REVISIÓN: Generador de Transaminación y Desaminación Oxidativa
# =============================================================================
# Archivo original : 04_NITROGENO_Y_AMINOACIDOS/via_13_transaminacion_y_desaminacion/generar_transaminacion_y_desaminacion.py (líneas 1 a 611 de 611)
# Descripción      : Acción de ALT, AST, glutamato deshidrogenasa (GDH) y glutamina sintetasa.
# =============================================================================

#!/usr/bin/env python3
"""
GENERADOR DE LA RUTA DE TRANSAMINACIÓN Y DESAMINACIÓN OXIDATIVA
==============================================================
Diseñado en concordancia 100% estricta con el estilo editorial de:
- 01_CARBOHIDRATOS/via_01_glucolisis/generar_glucolisis.py
- MANUAL_ESTILO_Y_COMANDOS.txt
- generar_prueba_visual_integrada.py

Características:
1. Vista Individual autónoma (1000 x 2200 px) en HTML y SVG puro.
2. Cero cajas, cero globos: metabolitos y estructuras químicas libres en el espacio biológico.
3. Código de color de la familia de Nitrógeno y Aminoácidos: Verde azulado / Esmeralda (#0d9488 / #059669).
4. Grupos amino (-NH3+ / -NH4+) resaltados en azul cobalto (#2563eb).
5. Cuatro secciones lógicas interconectadas:
   A. Reacción general de Transaminación (Aminoácido + α-KG ⇄ α-Cetoácido + Glutamato) mediada por PLP (Vitamina B6).
   B. Transaminasas clínicas clave con conexión directa a otras rutas:
      - ALT / GPT (Alanina + α-KG ⇄ Piruvato + Glutamato) ➔ Conecta con Glucólisis / Ciclo Glucosa-Alanina.
      - AST / GOT (Aspartato + α-KG ⇄ Oxalacetato + Glutamato) ➔ Conecta con Ciclo de Krebs y Ciclo de la Urea.
   C. Transporte y fijación temporal de Amonio (Citosol):
      - Glutamina Sintetasa (Glutamato + NH4+ + ATP ➔ Glutamina + ADP + Pi).
   D. Desaminación Oxidativa (Matriz Mitocondrial):
      - Importación de Glutamato vía Carrier mitocondrial (AGC / GC1).
      - Glutamato Deshidrogenasa (GLDH): Glutamato + NAD(P)+ + H2O ⇄ α-KG + NH4+ + NAD(P)H + H+.
      - Alosterismo de GLDH: Activada por ADP y GDP; inhibida por ATP y GTP.
      - Salida de NH4+ lista para Carbamoil Fosfato Sintetasa I (CPS-1 / Ciclo de la Urea).
6. Preparado con datos arrastrables ('data-arrastrable="1"') y modularizado para ser integrado directamente al Mapa Gigante.
"""

import os
import sys

DIR_ACTUAL = os.path.dirname(os.path.abspath(__file__))
sys.path.append(DIR_ACTUAL)

from estructuras_aminoacidos import (
    AMINOACIDO_GENERICO,
    ALFACETOACIDO_GENERICO,
    ALANINA,
    PIRUVATO_AMINO,
    ALFA_CETOGLUTARATO,
    GLUTAMATO,
    OXALACETATO_AMINO,
    ASPARTATO_AMINO,
    ION_AMONIO,
    GLUTAMINA,
    PLP_COENZIMA
)
from entorno_aminoacidos import DEFS_ENTORNO_AMINO, generar_entorno_aminoacidos_svg

# =============================================================================
# 1. PLANTILLAS HTML Y SVG
# =============================================================================
CABECERA_HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Transaminación y Desaminación Oxidativa en Entorno Biológico Real</title>
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
    <svg width="1000" height="2200" viewBox="0 0 1000 2200" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <!-- Flecha de flujo metabólico principal (Verde Azulado / Teal) -->
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#0d9488" />
        </marker>
        <!-- Flecha reversible / naranja secundaria -->
        <marker id="arrowOrange" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        <!-- Flecha de gasto de energía (Roja) -->
        <marker id="arrowRed" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#dc2626" />
        </marker>
        <!-- Flecha de salida / subproducto (Gris pizarra) -->
        <marker id="arrowSlate" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#475569" />
        </marker>
        <!-- Flecha de ganancia / poder reductor (Verde esmeralda) -->
        <marker id="arrowGreen" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#059669" />
        </marker>
        <!-- Flecha de agua (Azul cian) -->
        <marker id="arrowBlue" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
          <path d="M 0 0 L 5 2.5 L 0 5 Z" fill="#0284c7" />
        </marker>

        {DEFS_ENTORNO_AMINO}
      </defs>
"""

PIE_HTML = """
    </svg>
  </div>
</body>
</html>
"""

# =============================================================================
# 2. GENERADORES DE ELEMENTOS METABÓLICOS LIBRES
# =============================================================================

def crear_metabolito(x, y, nombre, carbonos, detalle="", svg_estructura="", texto_izquierda=False, id_nodo=""):
    """Construye el bloque SVG de un metabolito libre con su estructura y textos."""
    if texto_izquierda:
        pos_estructura = "translate(150, 0)"
        pos_texto = "translate(130, 25)"
        alineacion = 'text-anchor="end"'
    else:
        pos_estructura = "translate(0, 0)"
        pos_texto = "translate(135, 25)"
        alineacion = ''

    attr_id = f'id="{id_nodo}" data-arrastrable="1"' if id_nodo else 'data-arrastrable="1"'

    return f"""
      <!-- Metabolito: {nombre} -->
      <g {attr_id} transform="translate({x}, {y})">
        <g transform="{pos_estructura}">
          {svg_estructura}
        </g>
        <g transform="{pos_texto}">
          <text x="0" y="0" fill="#0f172a" font-size="16.5" font-weight="800" font-family="'Inter', sans-serif" {alineacion}>{nombre}</text>
          <text x="0" y="18" fill="#0d9488" font-size="12" font-weight="700" font-family="'JetBrains Mono', monospace" {alineacion}>{carbonos}</text>
          <text x="0" y="34" fill="#64748b" font-size="11" font-family="'Inter', sans-serif" {alineacion}>{detalle}</text>
        </g>
      </g>
    """

def crear_reaccion_vertical(x, y, h, enzima, ec="", coenzima="PLP (Vit B₆)", entra="", sale="", 
                            reversible=True, es_ganancia=False, id_rx="", color="#0d9488"):
    """Flecha de reacción con curvas de reactivo/producto y metadatos enzimáticos."""
    curvas = ""
    if entra:
        col_in = "#dc2626" if not es_ganancia else "#475569"
        marcador_in = "url(#arrowRed)" if not es_ganancia else "url(#arrowSlate)"
        curvas += f"""
        <path d="M -75 10 Q -25 10 -4 20" fill="none" stroke="{col_in}" stroke-width="1.8" marker-end="{marcador_in}"/>
        <text x="-80" y="14" fill="{col_in}" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{entra}</text>
        """
    if sale:
        col_out = "#059669" if es_ganancia else "#475569"
        marcador_out = "url(#arrowGreen)" if es_ganancia else "url(#arrowSlate)"
        curvas += f"""
        <path d="M -4 {h - 20} Q -25 {h - 10} -75 {h - 10}" fill="none" stroke="{col_out}" stroke-width="1.8" marker-end="{marcador_out}"/>
        <text x="-80" y="{h - 6}" fill="{col_out}" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{sale}</text>
        """

    if reversible:
        lineas = f"""
        <line x1="-3" y1="0" x2="-3" y2="{h}" stroke="{color}" stroke-width="2" marker-end="url(#arrowFlow)"/>
        <line x1="3" y1="{h}" x2="3" y2="0" stroke="{color}" stroke-width="2" marker-end="url(#arrowFlow)"/>
        """
    else:
        lineas = f"""<line x1="0" y1="0" x2="0" y2="{h}" stroke="{color}" stroke-width="2.6" marker-end="url(#arrowFlow)"/>"""

    attr_id = f'id="{id_rx}" data-arrastrable="1"' if id_rx else 'data-arrastrable="1"'

    return f"""
    <!-- Reacción: {enzima} -->
    <g {attr_id} transform="translate({x}, {y})">
      {lineas}
      {curvas}
      <g transform="translate(18, {h // 2 - 10})">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="800" font-family="'Inter', sans-serif">{enzima}</text>
        <text x="0" y="15" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace">{ec}</text>
        <text x="0" y="28" fill="#0d9488" font-size="10" font-weight="700" font-family="'Inter', sans-serif">Cofactor: {coenzima}</text>
      </g>
    </g>
    """

# =============================================================================
# 3. CONSTRUCCIÓN DE LA RUTA COMPLETA
# =============================================================================

def construir_ruta_aminoacidos_svg():
    partes = []

    # 1. Fondo celular y compartimentos (Citosol arriba y Mitocondria en y=1520)
    partes.append(generar_entorno_aminoacidos_svg(ancho=1000, alto=2200, y_mitocondria=1520))

    # =========================================================================
    # SECCIÓN 1: MECANISMO GENERAL DE TRANSAMINACIÓN Y COENZIMA PLP
    # =========================================================================
    partes.append("""
    <!-- Encabezado de la Sección 1 -->
    <g id="sec1_banner" data-arrastrable="1" transform="translate(500, 105)">
      <rect x="-240" y="-14" width="480" height="28" rx="14" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.8"/>
      <text x="0" y="4" fill="#0f766e" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
        1. PRINCIPIO GENERAL DE LA TRANSAMINACIÓN (TRANSFERENCIA DE ⁺NH₃)
      </text>
    </g>
    """)

    # Aminoácido donador (Izquierda)
    partes.append(crear_metabolito(
        x=70, y=140,
        nombre="L-Aminoácido",
        carbonos="Cualquier Aa donador",
        detalle="Aporta su grupo ⁺NH₃",
        svg_estructura=AMINOACIDO_GENERICO,
        id_nodo="m_aa_gen"
    ))

    # α-Cetoglutarato receptor (Centro-Derecha superior)
    partes.append(crear_metabolito(
        x=490, y=140,
        nombre="α-Cetoglutarato",
        carbonos="5 Carbonos [5C]",
        detalle="Aceptor universal en citosol",
        svg_estructura=ALFA_CETOGLUTARATO,
        id_nodo="m_akg_gen"
    ))

    # Centro de Reacción con Lupa de la Coenzima PLP
    partes.append("""
    <!-- Coenzima PLP y Base de Schiff (Centro) -->
    <g id="plp_focus" data-arrastrable="1" transform="translate(430, 275)">
      <!-- Círculo de aumento -->
      <circle cx="40" cy="40" r="52" fill="#ffffff" stroke="#0d9488" stroke-width="2.2" stroke-dasharray="6 3"/>
      <g transform="translate(0, -10)">
        """ + PLP_COENZIMA + """
      </g>
      <!-- Texto explicativo -->
      <text x="40" y="112" fill="#0f172a" font-size="12" font-weight="800" font-family="'Inter', sans-serif" text-anchor="middle">Aminotransferasa (Transaminasa)</text>
      <text x="40" y="127" fill="#0d9488" font-size="10.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Coenzima: Piridoxal Fosfato (PLP)</text>
      <text x="40" y="141" fill="#64748b" font-size="9.5" font-family="'Inter', sans-serif" text-anchor="middle">Forma Base de Schiff con Lys de la enzima</text>
    </g>
    """)

    # Flechas acopladas cruzadas de transaminación (Bimolecular tipo Ping-Pong)
    partes.append("""
    <!-- Arcos cruzados de transferencia de nitrógeno -->
    <g id="arcos_transaminacion_gen" data-arrastrable="1" stroke-linecap="round" fill="none">
      <!-- Camino 1: Aminoácido ➔ α-Cetoácido (Pierde NH3+) -->
      <path d="M 180 240 Q 220 350 190 450" stroke="#0d9488" stroke-width="2.5" marker-end="url(#arrowFlow)"/>
      <path d="M 175 450 Q 205 350 165 240" stroke="#0d9488" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowFlow)"/>
      <text x="135" y="350" fill="#0f766e" font-size="11" font-weight="800" font-family="'Inter', sans-serif">Transfiere ⁺NH₃</text>

      <!-- Camino 2: α-Cetoglutarato ➔ L-Glutamato (Gana NH3+) -->
      <path d="M 640 240 Q 600 350 630 450" stroke="#2563eb" stroke-width="2.5" marker-end="url(#arrowBlueAmino)"/>
      <path d="M 645 450 Q 615 350 655 240" stroke="#2563eb" stroke-width="1.8" stroke-dasharray="5 3" marker-end="url(#arrowBlueAmino)"/>
      <text x="705" y="350" fill="#1d4ed8" font-size="11" font-weight="800" font-family="'Inter', sans-serif">Recolecta ⁺NH₃</text>
    </g>
    """)

    # α-Cetoácido resultante (Izquierda inferior)
    partes.append(crear_metabolito(
        x=70, y=470,
        nombre="α-Cetoácido",
        carbonos="Esqueleto carbonado",
        detalle="Destino: Glucólisis / Krebs",
        svg_estructura=ALFACETOACIDO_GENERICO,
        id_nodo="m_ceto_gen"
    ))

    # L-Glutamato formado (Centro-Derecha inferior)
    partes.append(crear_metabolito(
        x=490, y=470,
        nombre="L-Glutamato",
        carbonos="5 Carbonos [5C]",
        detalle="Embudo colector de nitrógeno",
        svg_estructura=GLUTAMATO,
        id_nodo="m_glu_gen"
    ))

    # =========================================================================
    # SECCIÓN 2: LAS DOS TRANSAMINASAS CLÍNICAS VITALES (ALT Y AST)
    # =========================================================================
    partes.append("""
    <!-- Encabezado de la Sección 2 -->
    <g id="sec2_banner" data-arrastrable="1" transform="translate(500, 690)">
      <rect x="-270" y="-14" width="540" height="28" rx="14" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.8"/>
      <text x="0" y="4" fill="#0f766e" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
        2. ENCRUCIJADAS METABÓLICAS: ALT (ALANINA) Y AST (ASPARTATO)
      </text>
    </g>
    """)

    # --- RAMA 2A: ALANINA AMINOTRANSFERASA (ALT / GPT) ---
    # Alanina (Citosol izquierda)
    partes.append(crear_metabolito(
        x=50, y=740,
        nombre="L-Alanina",
        carbonos="3 Carbonos [3C]",
        detalle="Desde músculo / sangre",
        svg_estructura=ALANINA,
        id_nodo="m_ala_alt"
    ))

    # Piruvato resultante de ALT
    partes.append(crear_metabolito(
        x=50, y=980,
        nombre="Piruvato",
        carbonos="3 Carbonos [3C]",
        detalle="🔗 Enlace directo con Glucólisis",
        svg_estructura=PIRUVATO_AMINO,
        id_nodo="m_pyr_alt"
    ))

    # Reacción ALT con interconversión α-KG ⇄ Glutamato
    partes.append("""
    <g id="rx_alt_bloque" data-arrastrable="1" transform="translate(170, 860)">
      <!-- Flecha principal Alanina ⇄ Piruvato -->
      <line x1="-3" y1="-20" x2="-3" y2="70" stroke="#0d9488" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="70" x2="3" y2="-20" stroke="#0d9488" stroke-width="2" marker-end="url(#arrowFlow)"/>
      
      <!-- Arco cruzado acoplado con α-KG ➔ Glutamato -->
      <path d="M 65 -10 Q 15 25 65 60" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrowBlueAmino)"/>
      <text x="70" y="-12" fill="#0f172a" font-size="10.5" font-weight="700">α-Cetoglutarato</text>
      <text x="70" y="66" fill="#1d4ed8" font-size="10.5" font-weight="800">Glutamato</text>

      <g transform="translate(-15, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">ALT / GPT</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 2.6.1.2</text>
        <text x="0" y="27" fill="#0d9488" font-size="9.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">PLP • Ciclo Glucosa-Alanina</text>
      </g>
    </g>
    """)

    # Conexión destacada hacia Glucólisis / Gluconeogénesis
    partes.append("""
    <g id="link_glucolisis_alt" data-arrastrable="1">
      <path d="M 110 1080 L 110 1120 L 35 1120" fill="none" stroke="#ea580c" stroke-width="2.5" stroke-dasharray="7 4" marker-end="url(#arrowOrange)"/>
      <text x="40" y="1140" fill="#c2410c" font-size="11" font-weight="800" font-family="'Inter', sans-serif">➔ Hacia Glucólisis / Gluconeogénesis</text>
    </g>
    """)

    # --- RAMA 2B: ASPARTATO AMINOTRANSFERASA (AST / GOT) ---
    # Aspartato (Citosol centro-derecha)
    partes.append(crear_metabolito(
        x=520, y=740,
        nombre="L-Aspartato",
        carbonos="4 Carbonos [4C]",
        detalle="Dador de N para Ciclo Urea",
        svg_estructura=ASPARTATO_AMINO,
        id_nodo="m_asp_ast"
    ))

    # Oxalacetato resultante de AST
    partes.append(crear_metabolito(
        x=520, y=980,
        nombre="Oxalacetato",
        carbonos="4 Carbonos [4C]",
        detalle="🔗 Enlace con Krebs y Lanzadera",
        svg_estructura=OXALACETATO_AMINO,
        id_nodo="m_oaa_ast"
    ))

    # Reacción AST
    partes.append("""
    <g id="rx_ast_bloque" data-arrastrable="1" transform="translate(640, 860)">
      <!-- Flecha principal Aspartato ⇄ Oxalacetato -->
      <line x1="-3" y1="-20" x2="-3" y2="70" stroke="#0d9488" stroke-width="2" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="70" x2="3" y2="-20" stroke="#0d9488" stroke-width="2" marker-end="url(#arrowFlow)"/>
      
      <!-- Arco cruzado acoplado con α-KG ➔ Glutamato -->
      <path d="M 65 -10 Q 15 25 65 60" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrowBlueAmino)"/>
      <text x="70" y="-12" fill="#0f172a" font-size="10.5" font-weight="700">α-Cetoglutarato</text>
      <text x="70" y="66" fill="#1d4ed8" font-size="10.5" font-weight="800">Glutamato</text>

      <g transform="translate(-15, 25)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="900" font-family="'Inter', sans-serif" text-anchor="end">AST / GOT</text>
        <text x="0" y="14" fill="#64748b" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="end">EC 2.6.1.1</text>
        <text x="0" y="27" fill="#0d9488" font-size="9.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="end">PLP • Lanzadera Malato-Asp</text>
      </g>
    </g>
    """)

    # Conexión hacia el Ciclo de la Urea y Krebs (despejada a la derecha)
    partes.append("""
    <g id="link_urea_ast" data-arrastrable="1">
      <path d="M 760 760 Q 820 760 820 810" fill="none" stroke="#0284c7" stroke-width="2.5" stroke-dasharray="7 4" marker-end="url(#arrowBlue)"/>
      <text x="825" y="830" fill="#0369a1" font-size="11" font-weight="800" font-family="'Inter', sans-serif">➔ Aspartato entra directo al</text>
      <text x="825" y="845" fill="#0369a1" font-size="11" font-weight="900" font-family="'Inter', sans-serif">CICLO DE LA UREA</text>
    </g>
    """)

    # Línea que canaliza el Glutamato formado hacia la mitocondria (despejada por el centro libre X=370)
    partes.append("""
    <!-- Ruta de tránsito del Glutamato citosólico hacia la Matriz Mitocondrial -->
    <g id="linea_transito_glutamato" data-arrastrable="1">
      <path d="M 370 630 L 370 670" stroke="#0d9488" stroke-width="2.5" stroke-dasharray="8 5" fill="none"/>
      <path d="M 370 720 L 370 1170" stroke="#0d9488" stroke-width="2.5" stroke-dasharray="8 5" fill="none"/>
      <path d="M 370 1225 L 370 1515" stroke="#0d9488" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrowFlow)" fill="none"/>
      <text x="355" y="1485" fill="#0f766e" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">Glutamato a Matriz ➔</text>
    </g>
    """)

    # =========================================================================
    # SECCIÓN 3: AMONIO CITOSÓLICO Y SÍNTESIS DE GLUTAMINA (DESTOXIFICACIÓN)
    # =========================================================================
    partes.append("""
    <!-- Encabezado de la Sección 3 -->
    <g id="sec3_banner" data-arrastrable="1" transform="translate(500, 1190)">
      <rect x="-260" y="-14" width="520" height="28" rx="14" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.8"/>
      <text x="0" y="4" fill="#0f766e" font-size="12" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle" letter-spacing="1">
        3. TRANSPORTE SEGURO DE AMONIO: GLUTAMINA SINTETASA
      </text>
    </g>
    """)

    # Glutamato + NH4+ ➔ Glutamina (en tejidos periféricos/cerebro)
    partes.append(crear_metabolito(
        x=50, y=1240,
        nombre="L-Glutamato",
        carbonos="5 Carbonos [5C]",
        detalle="Receptor de amonio libre",
        svg_estructura=GLUTAMATO,
        id_nodo="m_glu_glns"
    ))

    # Glutamina resultante
    partes.append(crear_metabolito(
        x=670, y=1240,
        nombre="L-Glutamina",
        carbonos="5 Carbonos [5C]",
        detalle="Transportador no tóxico en sangre",
        svg_estructura=GLUTAMINA,
        id_nodo="m_gln_glns"
    ))

    # Reacción Glutamina Sintetasa
    partes.append("""
    <g id="rx_glutamina_sintetasa" data-arrastrable="1" transform="translate(440, 1285)">
      <line x1="-100" y1="0" x2="60" y2="0" stroke="#0d9488" stroke-width="2.6" marker-end="url(#arrowFlow)"/>
      
      <!-- Entrada de NH4+ y ATP -->
      <path d="M -70 -42 Q -25 -42 -10 -6" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arrowBlueAmino)"/>
      <text x="-75" y="-39" fill="#1d4ed8" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ NH₄⁺ (Amonio libre)</text>

      <path d="M -70 -20 Q -30 -20 5 -4" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrowRed)"/>
      <text x="-75" y="-17" fill="#dc2626" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">- 1 ATP</text>

      <!-- Salida de ADP + Pi -->
      <path d="M 5 6 Q -25 24 -70 24" fill="none" stroke="#475569" stroke-width="1.8" marker-end="url(#arrowSlate)"/>
      <text x="-75" y="28" fill="#475569" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ ADP + Pi</text>

      <!-- Textos Enzymáticos despejados por debajo -->
      <g transform="translate(-20, 52)">
        <text x="0" y="0" fill="#0f172a" font-size="13" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">Glutamina Sintetasa</text>
        <text x="0" y="16" fill="#64748b" font-size="10.5" font-family="'JetBrains Mono', monospace" text-anchor="middle">EC 6.3.1.2 (Mg²⁺)</text>
        <text x="0" y="32" fill="#059669" font-size="10.5" font-weight="700" font-family="'Inter', sans-serif" text-anchor="middle">Fijación de amonio neuroprotectora</text>
      </g>
    </g>
    """)

    # Exportación de Glutamina hacia la sangre / Hígado / Riñón
    partes.append("""
    <g id="link_export_glutamina" data-arrastrable="1">
      <path d="M 850 1240 Q 940 1240 940 1140 L 940 70" fill="none" stroke="#0d9488" stroke-width="2.5" stroke-dasharray="8 5" marker-end="url(#arrowTeal)"/>
      <text x="955" y="600" fill="#0f766e" font-size="11.5" font-weight="900" font-family="'Inter', sans-serif" transform="rotate(90 955 600)">EXPORTACIÓN DE GLUTAMINA AL TORRENTE SANGUÍNEO (HACIA HÍGADO/RIÑÓN) ➔</text>
    </g>
    """)

    # =========================================================================
    # SECCIÓN 4: DESAMINACIÓN OXIDATIVA EN LA MATRIZ MITOCONDRIAL (GLDH)
    # =========================================================================
    # Glutamato dentro de la matriz mitocondrial (debajo del carrier)
    partes.append(crear_metabolito(
        x=330, y=1660,
        nombre="L-Glutamato (Matriz)",
        carbonos="5 Carbonos [5C]",
        detalle="Sustrato de la GLDH",
        svg_estructura=GLUTAMATO,
        id_nodo="m_glu_mito"
    ))

    # Reacción Central: Glutamato Deshidrogenasa (GLDH)
    partes.append("""
    <g id="rx_gldh_bloque" data-arrastrable="1" transform="translate(410, 1830)">
      <!-- Flecha vertical reversible más amplia (120px) para máxima holgura -->
      <line x1="-3" y1="0" x2="-3" y2="120" stroke="#0d9488" stroke-width="2.4" marker-end="url(#arrowFlow)"/>
      <line x1="3" y1="120" x2="3" y2="0" stroke="#0d9488" stroke-width="2.4" marker-end="url(#arrowFlow)"/>

      <!-- Entrada de NAD(P)+ y H2O -->
      <path d="M -90 20 Q -30 20 -5 36" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-95" y="23" fill="#059669" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ NAD(P)⁺ + H₂O</text>

      <!-- Salida de NAD(P)H + H+ -->
      <path d="M -5 54 Q -30 72 -90 72" fill="none" stroke="#059669" stroke-width="2" marker-end="url(#arrowGreen)"/>
      <text x="-95" y="76" fill="#059669" font-size="11" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">+ NAD(P)H + H⁺</text>

      <!-- Salida de NH4+ (Liberación de Amonio libre): curva arqueada hacia la derecha-abajo, sin tocar texto -->
      <path d="M 5 60 Q 70 60 140 100" fill="none" stroke="#2563eb" stroke-width="2.6" marker-end="url(#arrowBlueAmino)"/>
      <text x="145" y="112" fill="#1d4ed8" font-size="12" font-weight="900" font-family="'Inter', sans-serif">➔ + NH₄⁺ (Liberado a Matriz)</text>

      <!-- Textos Enzimáticos y Alosterismo ubicados holgadamente a la derecha, por encima de la flecha azul -->
      <g transform="translate(22, 16)">
        <text x="0" y="0" fill="#0f172a" font-size="14" font-weight="900" font-family="'Inter', sans-serif">Glutamato Deshidrogenasa (GLDH)</text>
        <text x="0" y="16" fill="#64748b" font-size="11" font-family="'JetBrains Mono', monospace">EC 1.4.1.3 (Mitocondrial)</text>
        <text x="0" y="32" fill="#16a34a" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">(+) Activada por ADP, GDP (Baja energía)</text>
        <text x="0" y="47" fill="#e11d48" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">(-) Inhibida por ATP, GTP (Alta energía)</text>
      </g>
    </g>
    """)

    # Productos de la GLDH:
    # 1. α-Cetoglutarato regenerado (vuelve al Ciclo de Krebs)
    partes.append(crear_metabolito(
        x=220, y=1960,
        nombre="α-Cetoglutarato",
        carbonos="5 Carbonos [5C]",
        detalle="🔗 Retorna directo al Ciclo de Krebs",
        svg_estructura=ALFA_CETOGLUTARATO,
        id_nodo="m_akg_mito"
    ))

    # Conexión α-KG ➔ Krebs
    partes.append("""
    <g id="link_akg_krebs" data-arrastrable="1">
      <path d="M 220 2020 Q 140 2020 140 2090 L 140 2150" fill="none" stroke="#b45309" stroke-width="2.6" stroke-dasharray="8 4" marker-end="url(#arrowOrange)"/>
      <text x="150" y="2120" fill="#78350f" font-size="11.5" font-weight="800" font-family="'Inter', sans-serif">➔ Reingreso al Ciclo de Krebs</text>
    </g>
    """)

    # 2. Amonio libre (NH4+) y conexión a la CPS-1 / Ciclo de la Urea
    partes.append(crear_metabolito(
        x=640, y=1960,
        nombre="Ion Amonio (NH₄⁺)",
        carbonos="Grupo Nitrógeno",
        detalle="🔗 Sustrato de CPS-1 en Urea",
        svg_estructura=ION_AMONIO,
        id_nodo="m_nh4_mito"
    ))

    # Conexión hacia CPS-1
    partes.append("""
    <g id="link_nh4_urea" data-arrastrable="1">
      <path d="M 750 2020 Q 840 2020 840 2090 L 840 2150" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-dasharray="8 4" marker-end="url(#arrowBlueAmino)"/>
      <text x="850" y="2110" fill="#1d4ed8" font-size="12" font-weight="900" font-family="'Inter', sans-serif">➔ ENTRADA AL CICLO DE LA UREA</text>
      <text x="850" y="2128" fill="#475569" font-size="10.5" font-family="'Inter', sans-serif">Carbamoil Fosfato Sintetasa I (CPS-1)</text>
    </g>
    """)

    return "".join(partes)

# =============================================================================
# 4. FUNCIÓN PRINCIPAL DE ESCRITURA
# =============================================================================

def main():
    contenido_svg = construir_ruta_aminoacidos_svg()

    # Guardar SVG
    svg_completo = f"""<svg width="1000" height="2200" viewBox="0 0 1000 2200" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#0d9488" />
        </marker>
        <marker id="arrowOrange" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
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
        {DEFS_ENTORNO_AMINO}
      </defs>
      {contenido_svg}
    </svg>"""

    ruta_svg = os.path.join(DIR_ACTUAL, "Transaminacion_y_Desaminacion.svg")
    with open(ruta_svg, "w", encoding="utf-8") as f:
        f.write(svg_completo)

    # Guardar HTML
    html_completo = CABECERA_HTML + contenido_svg + PIE_HTML
    ruta_html = os.path.join(DIR_ACTUAL, "Transaminacion_y_Desaminacion.html")
    with open(ruta_html, "w", encoding="utf-8") as f:
        f.write(html_completo)

    print(f"✅ Archivo SVG generado con éxito en: {ruta_svg}")
    print(f"✅ Archivo HTML generado con éxito en: {ruta_html}")

if __name__ == "__main__":
    main()
