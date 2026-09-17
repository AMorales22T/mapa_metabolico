#!/usr/bin/env python3
"""
DIBUJO DEL ENTORNO BIOLÓGICO CELULAR (SVG)
===========================================
Este módulo contiene el dibujo artístico vectorial de la célula:
1. Arriba: Membrana Plasmática con bicapa fosfolipídica y canal GLUT por donde entra la Glucosa.
2. Centro: Citosol real con filamentos de citoesqueleto, vesículas y polirribosomas (sin carteles de texto).
3. Abajo: Mitocondria real con doble membrana, crestas onduladas y transportador MPC esperando al Piruvato.

Coordenadas calibradas para alinearse con la Glucólisis (X=385 central, Ancho=1000, Alto=2150).
"""

import os

# =============================================================================
# DEFINICIONES DE RECURSOS GRÁFICOS CELULARES (GRADIENTES Y TEXTURAS)
# =============================================================================
DEFS_ENTORNO_CELULAR = """
    <!-- Gradiente acuoso citosólico biológico -->
    <linearGradient id="gradCitosol" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="5%" stop-color="#f0fdf4" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#f8fafc" stop-opacity="0.5" />
      <stop offset="90%" stop-color="#f0fdf4" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#f8fafc" stop-opacity="1" />
    </linearGradient>

    <!-- Gradiente del medio extracelular (arriba) -->
    <linearGradient id="gradExtracelular" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#e2e8f0" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#f1f5f9" stop-opacity="0.9" />
    </linearGradient>

    <!-- Gradiente de la Matriz Mitocondrial (abajo, ámbar cálido) -->
    <radialGradient id="gradMitocondria" cx="50%" cy="100%" r="90%">
      <stop offset="0%" stop-color="#fef3c7" stop-opacity="0.95" />
      <stop offset="60%" stop-color="#fffbeb" stop-opacity="0.9" />
      <stop offset="100%" stop-color="#fef9c3" stop-opacity="0.85" />
    </radialGradient>
"""

# =============================================================================
# DIBUJO DEL ENTORNO BIOLÓGICO COMPLETO
# =============================================================================
def generar_entorno_celular_svg(ancho=1000, alto=2150):
    """
    Retorna todo el código SVG del dibujo celular orgánico.
    No incluye carteles ni palabras tipo 'CITOSOL', todo es dibujo puramente biológico.
    """
    return f"""
    <!-- ================================================================= -->
    <!-- CAPA 1: FONDO ACUOSO DEL CITOSOL                                  -->
    <!-- ================================================================= -->
    <rect x="0" y="0" width="{ancho}" height="{alto}" fill="url(#gradCitosol)" />

    <!-- ================================================================= -->
    <!-- CAPA 2: ESTRUCTURAS DEL CITOPLASMA (CITOESQUELETO Y VESÍCULAS)    -->
    <!-- ================================================================= -->
    <!-- Red sutil de microfilamentos de citoesqueleto que cruzan el citoplasma -->
    <g opacity="0.35" stroke="#94a3b8" fill="none">
      <!-- Filamento largo superior -->
      <path d="M 40 220 Q 250 160 500 240 T 960 210" stroke-width="1.6" stroke-dasharray="8 6" />
      <path d="M 60 410 Q 300 480 580 430 T 940 450" stroke-width="1.4" stroke-dasharray="6 6" />
      <!-- Filamentos medios (zona de triosas) -->
      <path d="M 30 730 Q 320 680 620 740 T 970 700" stroke-width="1.5" stroke-dasharray="8 5" />
      <path d="M 50 1020 Q 280 1080 540 1030 T 950 1060" stroke-width="1.6" stroke-dasharray="7 7" />
      <!-- Filamentos inferiores hacia la mitocondria -->
      <path d="M 40 1380 Q 350 1330 680 1390 T 960 1350" stroke-width="1.5" stroke-dasharray="8 6" />
      <path d="M 70 1680 Q 380 1740 650 1690 T 940 1720" stroke-width="1.4" stroke-dasharray="6 6" />
    </g>

    <!-- Polirribosomas celulares flotando libres en el citoplasma (agrupaciones biológicas) -->
    <g fill="#94a3b8" opacity="0.25">
      <!-- Grupo 1 (arriba izquierda) -->
      <circle cx="120" cy="160" r="2.5"/><circle cx="126" cy="162" r="2"/><circle cx="124" cy="168" r="2.3"/><circle cx="118" cy="167" r="2.1"/>
      <!-- Grupo 2 (arriba derecha) -->
      <circle cx="850" cy="310" r="2.5"/><circle cx="857" cy="312" r="2"/><circle cx="854" cy="318" r="2.3"/><circle cx="848" cy="317" r="2.1"/>
      <!-- Grupo 3 (medio) -->
      <circle cx="140" cy="620" r="2.5"/><circle cx="146" cy="623" r="2.2"/><circle cx="143" cy="628" r="2"/><circle cx="138" cy="626" r="2.3"/>
      <circle cx="880" cy="790" r="2.5"/><circle cx="887" cy="793" r="2"/><circle cx="883" cy="798" r="2.2"/><circle cx="877" cy="796" r="2.1"/>
      <!-- Grupo 4 (fase rendimiento) -->
      <circle cx="150" cy="1220" r="2.5"/><circle cx="156" cy="1222" r="2"/><circle cx="153" cy="1228" r="2.3"/>
      <circle cx="860" cy="1490" r="2.5"/><circle cx="867" cy="1493" r="2"/><circle cx="863" cy="1498" r="2.2"/>
    </g>

    <!-- Vesículas citosólicas de transporte (pequeñas microburbujas translúcidas) -->
    <g opacity="0.3">
      <!-- Vesícula izquierda alta -->
      <circle cx="160" cy="360" r="22" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="160" cy="360" r="16" fill="none" stroke="#7dd3fc" stroke-width="1"/>
      <!-- Vesícula derecha baja -->
      <circle cx="870" cy="1200" r="26" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8" stroke-dasharray="4 2"/>
      <circle cx="870" cy="1200" r="19" fill="none" stroke="#7dd3fc" stroke-width="1"/>
    </g>


    <!-- ================================================================= -->
    <!-- CAPA 3: MEDIO EXTRACELULAR Y MEMBRANA PLASMÁTICA (ARRIBA)        -->
    <!-- ================================================================= -->
    <!-- Medio Extracelular (Fluido intersticial / Sangre) -->
    <path d="M 0 0 L {ancho} 0 L {ancho} 45 Q 500 65 0 45 Z" fill="url(#gradExtracelular)" stroke="#cbd5e1" stroke-width="1"/>

    <!-- Bicapa Fosfolipídica Ondulada (Azul membrana con doble línea orgánica) -->
    <path d="M 0 45 Q 500 65 {ancho} 45" fill="none" stroke="#0284c7" stroke-width="5" stroke-linecap="round"/>
    <path d="M 0 52 Q 500 72 {ancho} 52" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>

    <!-- Cabezas polares fosfolipídicas (pequeños destellos sutiles a lo largo de la membrana) -->
    <g stroke="#0284c7" stroke-width="1.2" opacity="0.4">
      <line x1="100" y1="45" x2="100" y2="52"/>
      <line x1="180" y1="47" x2="180" y2="54"/>
      <line x1="260" y1="49" x2="260" y2="56"/>
      <line x1="620" y1="49" x2="620" y2="56"/>
      <line x1="740" y1="47" x2="740" y2="54"/>
      <line x1="860" y1="45" x2="860" y2="52"/>
    </g>

    <!-- Poro de Transporte Proteico GLUT (Incrustado en la membrana en X=385) -->
    <g transform="translate(355, 40)">
      <!-- Lóbulo izquierdo de la proteína transportadora -->
      <path d="M 0 0 C 8 -8, 20 -8, 24 2 C 26 10, 24 22, 18 26 C 10 28, 2 22, 0 14 Z" fill="#0284c7" stroke="#0369a1" stroke-width="1.8"/>
      <!-- Lóbulo derecho de la proteína transportadora -->
      <path d="M 60 0 C 52 -8, 40 -8, 36 2 C 34 10, 36 22, 42 26 C 50 28, 58 22, 60 14 Z" fill="#0284c7" stroke="#0369a1" stroke-width="1.8"/>
      <!-- Canal de transporte central por donde cruza la molécula -->
      <ellipse cx="30" cy="12" rx="7" ry="12" fill="#0ea5e9" opacity="0.6"/>
      <!-- Etiqueta técnica sutil del canal transportador -->
      <text x="30" y="16" fill="#ffffff" font-size="9" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT</text>
    </g>

    <!-- Flecha biológica de entrada: la glucosa cruzando el canal de la membrana -->
    <line x1="385" y1="18" x2="385" y2="65" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>


    <!-- ================================================================= -->
    <!-- CAPA 4: LA MITOCONDRIA BIOLÓGICA REAL (ABAJO)                     -->
    <!-- ================================================================= -->
    <!-- Forma orgánica arriñonada mitocondrial que envuelve el fondo -->
    <g transform="translate(0, 1980)">
      <!-- Membrana Mitocondrial Externa Lisa (Ámbar) -->
      <path d="M 0 50 Q 250 15 500 35 T {ancho} 25 L {ancho} 200 L 0 200 Z" fill="url(#gradMitocondria)" stroke="#b45309" stroke-width="3.5"/>
      
      <!-- Espacio Intermembrana (Separación visible) -->
      <path d="M 0 65 Q 250 30 500 50 T {ancho} 40" fill="none" stroke="#78350f" stroke-width="2" stroke-dasharray="6 3"/>

      <!-- Crestas Mitocondriales Reales (Invaginaciones profundas de la membrana interna) -->
      <!-- Cresta izquierda -->
      <path d="M 60 120 C 120 70, 150 140, 220 90 C 270 140, 230 170, 120 160 Z" fill="#fef3c7" stroke="#b45309" stroke-width="2.5" opacity="0.85"/>
      <!-- Cresta derecha grande -->
      <path d="M 650 110 C 720 60, 770 130, 840 80 C 910 130, 860 170, 720 155 Z" fill="#fef3c7" stroke="#b45309" stroke-width="2.5" opacity="0.85"/>
      <!-- Cresta central inferior -->
      <path d="M 280 145 C 340 115, 420 115, 480 145" fill="none" stroke="#b45309" stroke-width="2.5" stroke-linecap="round"/>

      <!-- Transportador MPC (Complejo Carrier de Piruvato) incrustado en la membrana -->
      <g transform="translate(360, 22)">
        <rect x="0" y="0" width="50" height="24" rx="6" fill="#b45309" stroke="#78350f" stroke-width="1.8"/>
        <text x="25" y="16" fill="#ffffff" font-size="10" font-weight="800" font-family="'JetBrains Mono', monospace" text-anchor="middle">MPC</text>
      </g>

      <!-- Flecha del Piruvato cruzando el MPC hacia la Matriz Mitocondrial -->
      <line x1="385" y1="-5" x2="385" y2="55" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>

      <!-- Destino dentro de la matriz (Conexión natural con PDH y Krebs) -->
      <g transform="translate(385, 80)">
        <text x="0" y="0" fill="#78350f" font-size="12" font-weight="800" text-anchor="middle">Hacia Complejo Piruvato DH</text>
        <text x="0" y="15" fill="#92400e" font-size="10" font-weight="600" text-anchor="middle">Matriz Mitocondrial • Ciclo de Krebs</text>
      </g>
    </g>
    """


# =============================================================================
# VISTA PREVIA INDEPENDIENTE (Para probar el dibujo sin alterar tu mapa)
# =============================================================================
if __name__ == "__main__":
    plantilla_prueba = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Prueba de Entorno Celular (Dibujo Puro)</title>
  <style>
    body {{ background: #e2e8f0; display: flex; justify-content: center; padding: 20px; margin: 0; font-family: sans-serif; }}
    .lienzo {{ width: 1000px; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.15); border-radius: 8px; overflow: hidden; }}
  </style>
</head>
<body>
  <div class="lienzo">
    <svg width="1000" height="2150" viewBox="0 0 1000 2150" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrowFlow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M 0 0 L 6 3 L 0 6 Z" fill="#ea580c" />
        </marker>
        {DEFS_ENTORNO_CELULAR}
      </defs>
      
      {generar_entorno_celular_svg(1000, 2150)}
      
    </svg>
  </div>
</body>
</html>
"""
    ruta_prueba = os.path.join(os.path.dirname(__file__), "prueba_entorno.html")
    with open(ruta_prueba, "w", encoding="utf-8") as f:
        f.write(plantilla_prueba)
    print(f"✅ ¡Dibujo del entorno celular creado para prueba en: {ruta_prueba}!")
