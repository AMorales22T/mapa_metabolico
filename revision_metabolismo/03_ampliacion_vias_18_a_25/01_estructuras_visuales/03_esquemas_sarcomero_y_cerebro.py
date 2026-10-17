# =============================================================================
# MÓDULO DE REVISIÓN: Esquemas Anatómicos de Sarcómero Muscular y Cerebro/Neurona
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/estructuras_ampliacion.py (líneas 348 a 532 de 611)
# Descripción      : Miofibrilla con líneas Z/bandas A-I/túbulo T y encéfalo con neurona multipolar mielinizada.
# =============================================================================

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

