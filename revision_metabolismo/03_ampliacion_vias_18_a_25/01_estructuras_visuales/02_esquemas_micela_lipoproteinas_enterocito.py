# =============================================================================
# MÓDULO DE REVISIÓN: Esquemas de Micela Mixta, Lipoproteínas y Enterocito
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/estructuras_ampliacion.py (líneas 244 a 347 de 611)
# Descripción      : Ilustraciones vectoriales de micela biliar, quilomicrón/VLDL/LDL/HDL y enterocito con borde en cepillo.
# =============================================================================

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

