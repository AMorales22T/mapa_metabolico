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
    <!-- CAPA 3: MEDIO EXTRACELULAR, MEMBRANA Y ZOOM MOLECULAR (ARRIBA)   -->
    <!-- ================================================================= -->
    <!-- Medio Extracelular (Fluido intersticial / Sangre) -->
    <path d="M 0 0 L {ancho} 0 L {ancho} 60 Q 500 85 0 60 Z" fill="url(#gradExtracelular)" stroke="#cbd5e1" stroke-width="1"/>
    <text x="35" y="32" fill="#64748b" font-size="11" font-weight="800" letter-spacing="1.5">ESPACIO EXTRACELULAR (SANGRE / LÍQUIDO INTERSTICIAL)</text>

    <!-- Bicapa Fosfolipídica Ondulada Celular -->
    <path d="M 0 60 Q 500 85 {ancho} 60" fill="none" stroke="#0284c7" stroke-width="8" stroke-linecap="round"/>
    <path d="M 0 68 Q 500 93 {ancho} 68" fill="none" stroke="#38bdf8" stroke-width="3" stroke-linecap="round"/>

    <!-- Cabezas de fosfolípidos decorativas a lo largo de la bicapa -->
    <g fill="#0284c7" opacity="0.6">
      <circle cx="80" cy="58" r="3"/><circle cx="95" cy="59" r="3"/><circle cx="110" cy="60" r="3"/>
      <circle cx="200" cy="65" r="3"/><circle cx="215" cy="66" r="3"/><circle cx="230" cy="67" r="3"/>
      <circle cx="650" cy="67" r="3"/><circle cx="665" cy="66" r="3"/><circle cx="680" cy="65" r="3"/>
      <circle cx="850" cy="60" r="3"/><circle cx="865" cy="59" r="3"/><circle cx="880" cy="58" r="3"/>
    </g>

    <!-- ============================================================= -->
    <!-- EL TRANSPORTADOR GLUT EN LA MEMBRANA REAL (MÁS GRANDE)        -->
    <!-- ============================================================= -->
    <g transform="translate(345, 45)">
      <!-- Lóbulo proteico izquierdo -->
      <path d="M 0 5 C 10 -12, 28 -12, 34 5 C 38 18, 34 36, 25 42 C 12 45, 2 35, 0 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      <!-- Lóbulo proteico derecho -->
      <path d="M 80 5 C 70 -12, 52 -12, 46 5 C 42 18, 46 36, 55 42 C 68 45, 78 35, 80 22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2.2"/>
      
      <!-- Poro o canal transmembrana central acuoso -->
      <ellipse cx="40" cy="20" rx="10" ry="18" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.8"/>
      
      <!-- Pequeña glucosa cruzando por el canal -->
      <polygon points="40,14 45,17 45,23 40,26 35,23 35,17" fill="#ffffff" stroke="#ea580c" stroke-width="1.6"/>
      <circle cx="35" cy="17" r="2" fill="#dc2626"/>

      <!-- Rótulo en la proteína -->
      <text x="40" y="49" fill="#0369a1" font-size="10" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">GLUT-4</text>
    </g>

    <!-- Línea guía de entrada hacia el citoplasma -->
    <line x1="385" y1="20" x2="385" y2="45" stroke="#ea580c" stroke-width="2.2"/>
    <line x1="385" y1="85" x2="385" y2="105" stroke="#ea580c" stroke-width="2.5" marker-end="url(#arrowFlow)"/>


    <!-- ============================================================= -->
    <!-- ZOOM MOLECULAR / LUPA CIENTÍFICA (A la izquierda del GLUT)    -->
    <!-- ============================================================= -->
    <!-- Líneas de proyección cónica que nacen en el GLUT y van hacia la lupa -->
    <g stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="4 3" opacity="0.6">
      <line x1="345" y1="65" x2="225" y2="90" />
      <line x1="355" y1="45" x2="190" y2="40" />
    </g>

    <!-- Ventana Circular de Zoom (Lupa de Aumento Molecular) -->
    <g transform="translate(130, 85)">
      <!-- Sombra y fondo blanco del lente -->
      <circle cx="0" cy="0" r="65" fill="#ffffff" stroke="#0284c7" stroke-width="3.5" />
      <circle cx="0" cy="0" r="62" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />

      <!-- Bicapa lipídica ampliada cortando la lupa horizontalmente -->
      <g opacity="0.85">
        <!-- Capa exterior de fosfolípidos (arriba) -->
        <g fill="#0284c7">
          <circle cx="-52" cy="-8" r="5"/><circle cx="-38" cy="-8" r="5"/><circle cx="-24" cy="-8" r="5"/>
          <circle cx="24" cy="-8" r="5"/><circle cx="38" cy="-8" r="5"/><circle cx="52" cy="-8" r="5"/>
        </g>
        <!-- Colas de ácidos grasos (onduladas) -->
        <g stroke="#94a3b8" stroke-width="1.4" fill="none">
          <path d="M -52 -3 Q -54 2 -50 7"/><path d="M -38 -3 Q -40 2 -36 7"/><path d="M -24 -3 Q -26 2 -22 7"/>
          <path d="M 24 -3 Q 22 2 26 7"/><path d="M 38 -3 Q 36 2 40 7"/><path d="M 52 -3 Q 50 2 54 7"/>
          <path d="M -52 17 Q -54 12 -50 7"/><path d="M -38 17 Q -40 12 -36 7"/><path d="M -24 17 Q -26 12 -22 7"/>
          <path d="M 24 17 Q 22 12 26 7"/><path d="M 38 17 Q 36 12 40 7"/><path d="M 52 17 Q 50 12 54 7"/>
        </g>
        <!-- Capa interior de fosfolípidos (abajo) -->
        <g fill="#0284c7">
          <circle cx="-52" cy="22" r="5"/><circle cx="-38" cy="22" r="5"/><circle cx="-24" cy="22" r="5"/>
          <circle cx="24" cy="22" r="5"/><circle cx="38" cy="22" r="5"/><circle cx="52" cy="22" r="5"/>
        </g>
      </g>

      <!-- Proteína Transportadora GLUT en grande dentro de la lupa -->
      <!-- Subunidad izquierda -->
      <path d="M -16 -22 C -8 -26, -4 -15, -4 0 C -4 15, -8 26, -16 22 C -24 18, -22 -18, -16 -22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
      <!-- Subunidad derecha -->
      <path d="M 16 -22 C 8 -26, 4 -15, 4 0 C 4 15, 8 26, 16 22 C 24 18, 22 -18, 16 -22 Z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>

      <!-- Canal abierto central acuoso -->
      <ellipse cx="0" cy="0" rx="6" ry="18" fill="#bae6fd" opacity="0.6"/>

      <!-- LA MOLÉCULA DE GLUCOSA EN PLENO CRUCE (Haworth esquemático ampliado) -->
      <g transform="translate(0, -6)">
        <polygon points="0,-10 9,-4 9,6 0,12 -9,6 -9,-4" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
        <circle cx="-9" cy="-4" r="3" fill="#ffffff"/>
        <text x="-9" y="-2" fill="#dc2626" font-size="6" font-weight="900" text-anchor="middle">O</text>
        <circle cx="14" cy="6" r="4" fill="#ffedd5" stroke="#ea580c" stroke-width="1.2"/>
        <text x="14" y="8" fill="#ea580c" font-size="5" font-weight="900" text-anchor="middle">OH</text>
      </g>

      <!-- Flecha de difusión facilitada atravesando el canal hacia abajo -->
      <path d="M 0 -26 L 0 -15" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>
      <path d="M 0 10 L 0 26" stroke="#ea580c" stroke-width="2.2" marker-end="url(#arrowFlow)"/>

      <!-- Etiqueta explicativa de la lupa -->
      <rect x="-55" y="44" width="110" height="15" rx="4" fill="#0f172a" opacity="0.85"/>
      <text x="0" y="55" fill="#ffffff" font-size="8" font-weight="800" text-anchor="middle" letter-spacing="0.5">DIFUSIÓN FACILITADA</text>
    </g>



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
