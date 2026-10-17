/* ============================================================================
 * MÓDULO DE REVISIÓN: Configuración del Lienzo y Catálogo JS de las 25 Vías
 * ============================================================================
 * Archivo original : 07_AMPLIACION_TEMARIO/interactividad_html.py (líneas 719 a 846 de 1638)
 * Descripción      : Constantes geométricas, inyección de estequiometría JSON y diccionario TABLA_VIAS con los grupos SVG de cada ruta.
 * ============================================================================ */


  <script>
    // =========================================================================
    // CONFIGURACIÓN VECTORIAL Y PARÁMETROS GEOMÉTRICOS DEL LIENZO
    // =========================================================================
    const W_CANVAS = __W_CANVAS__;
    const H_CANVAS = __H_CANVAS__;
    const VB_X = __VB_X__;
    const VB_Y = __VB_Y__;

    const viewport = document.getElementById('viewport');
    const panLayer = document.getElementById('panLayer');
    const zoomLevelEl = document.getElementById('zoomLevel');

    let scale = 1;
    let pointX = 0;
    let pointY = 0;
    let startX = 0;
    let startY = 0;
    let isPanning = false;

    function updateTransform() {
      panLayer.style.transform = `translate(${pointX}px, ${pointY}px) scale(${scale})`;
      if (zoomLevelEl) zoomLevelEl.textContent = Math.round(scale * 100) + '%';
    }

    function zoomIn() { scale = Math.min(scale * 1.25, 4.0); updateTransform(); }
    function zoomOut() { scale = Math.max(scale / 1.25, 0.08); updateTransform(); }
    function resetView() { scale = 1; pointX = 0; pointY = 0; updateTransform(); }
    function fitView() {
      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;
      scale = Math.min(vw / W_CANVAS, vh / H_CANVAS) * 0.96;
      pointX = (vw - W_CANVAS * scale) / 2;
      pointY = (vh - H_CANVAS * scale) / 2;
      updateTransform();
    }

    // =========================================================================
    // BASE DE DATOS DE REACCIONES QUÍMICAS Y ESTEQUIOMETRÍA BALANCEADA
    // =========================================================================
    const TABLA_REACCIONES_ESTEQUIOMETRIA = __TABLA_REACCIONES_JSON__;

    // =========================================================================
    // TABLA MAESTRA DE LAS 25 VÍAS METABÓLICAS INTEGRADAS
    // =========================================================================
    const TABLA_VIAS = {
      "1": { numero: "1", id: "1", nombre: "Glucólisis", subtitulo: "Glucosa → 2 Piruvato (+2 ATP, +2 NADH)", grupos: ["ruta_glucolisis", "badge_via_1"], color: "#0284c7" },
      "2": { numero: "2", id: "2", nombre: "Gluconeogénesis", subtitulo: "Piruvato → Glucosa (4 enzimas específicas) · hepática", grupos: ["ruta_gluconeogenesis", "badge_via_2"], color: "#7c3aed" },
      "3": { numero: "3", id: "3", nombre: "Glucogenogénesis y glucogenólisis", subtitulo: "Síntesis y degradación del glucógeno", grupos: ["ruta_glucogeno", "badge_via_3"], color: "#ea580c" },
      "4": { numero: "4", id: "4", nombre: "Vía de las pentosas fosfato", subtitulo: "G6P → NADPH + Ribosa-5-P (fase oxidativa y no oxidativa)", grupos: ["ruta_pentosas", "badge_via_4"], color: "#059669" },
      "5": { numero: "5", id: "5", nombre: "Complejo piruvato deshidrogenasa (PDH)", subtitulo: "Piruvato → Acetil-CoA + CO₂ + NADH", grupos: ["lupa_piruvato_deshidrogenasa", "badge_via_5"], color: "#c2410c" },
      "6": { numero: "6", id: "6", nombre: "Ciclo de Krebs", subtitulo: "Acetil-CoA → 2 CO₂ + 3 NADH + FADH₂ + GTP", grupos: ["ruta_krebs", "badge_via_6"], color: "#d97706" },
      "7": { numero: "7", id: "7", nombre: "Cadena respiratoria y ATP sintasa", subtitulo: "Fosforilación oxidativa (acoplamiento quimiosmótico)", grupos: ["lupa_cadena_respiratoria", "badge_via_7"], color: "#16a34a" },
      "8": { numero: "8", id: "8", nombre: "Lanzadera malato-aspartato", subtitulo: "Transporte de equivalentes redox (NADH citosólico a matriz)", grupos: ["lupa_lanzadera_malato_aspartato", "badge_via_8"], color: "#0284c7" },
      "8B": { numero: "8B", id: "8B", nombre: "Lanzadera glicerol-3-fosfato", subtitulo: "DHAP ➔ G3P (Reoxidación rápida de NADH hacia FAD en MMI)", grupos: ["lupa_lanzadera_glicerol_p", "badge_via_8B"], color: "#0d9488" },
      "9": { numero: "9", id: "9", nombre: "β-oxidación (y lanzadera de carnitina)", subtitulo: "Palmitoil-CoA → 8 Acetil-CoA + FADH₂ + NADH", grupos: ["ruta_beta_ox", "badge_via_9"], color: "#b45309" },
      "10": { numero: "10", id: "10", nombre: "Lipogénesis (síntesis de ácidos grasos)", subtitulo: "Acetil-CoA → Malonil-CoA → Palmitato (FAS)", grupos: ["ruta_lipogenesis", "badge_via_10"], color: "#0d9488" },
      "11": { numero: "11", id: "11", nombre: "Cetogénesis", subtitulo: "Acetil-CoA → Acetoacetato / β-Hidroxibutirato", grupos: ["ruta_ceto", "badge_via_11"], color: "#be123c" },
      "12": { numero: "12", id: "12", nombre: "Síntesis de colesterol", subtitulo: "Acetil-CoA → HMG-CoA → Mevalonato → Colesterol", grupos: ["ruta_colesterol", "badge_via_12"], color: "#4f46e5" },
      "12B": { numero: "12B", id: "12B", nombre: "Destinos esqueletos carbonados AA", subtitulo: "Convergencia de los 20 AA en Krebs, Piruvato y Cuerpos Cetónicos", grupos: ["ruta_destinos_aa", "badge_via_12B"], color: "#6366f1" },
      "13": { numero: "13", id: "13", nombre: "Transaminación y desaminación oxidativa", subtitulo: "Recogida del grupo amino en Glutamato → NH₄⁺", grupos: ["ruta_transaminacion_desaminacion", "badge_via_13"], color: "#2563eb" },
      "14": { numero: "14", id: "14", nombre: "Ciclo de la urea", subtitulo: "NH₄⁺ + HCO₃⁻ + Aspartato → Urea", grupos: ["ruta_ciclo_urea", "badge_via_14"], color: "#0891b2" },
      "15": { numero: "15", id: "15", nombre: "Biosíntesis de nucleótidos", subtitulo: "Rutas convergentes sobre PRPP (purinas y pirimidinas)", grupos: ["ruta_sintesis_nucleotidos", "badge_via_15"], color: "#0284c7" },
      "16": { numero: "16", id: "16", nombre: "Catabolismo de nucleótidos y ácido úrico", subtitulo: "Degradación de purinas a Ácido Úrico y pirimidinas a β-Alanina", grupos: ["ruta_degradacion_nucleotidos", "badge_via_16"], color: "#475569" },
      "17": { numero: "17", id: "17", nombre: "Ciclo de Cori", subtitulo: "Lactato muscular anaeróbico → Sangre → Glucosa hepática (GNG) → Músculo (-4 ATP neto)", grupos: ["ruta_ciclo_cori", "badge_via_17"], color: "#be123c" },
      "18": { numero: "18", id: "18", nombre: "Digestión y transporte de lípidos", subtitulo: "Luz intestinal • Emulsión micelar • Enterocito • Linfa quilífera", grupos: ["ruta_digestion_lipidos", "badge_via_18", "badge_leyenda_18"], color: "#0d9488" },
      "19": { numero: "19", id: "19", nombre: "Tejido adiposo (lipólisis ATGL/HSL/MGL)", subtitulo: "Gota lipídica • Cascada secuencial TAG ➔ DAG ➔ MAG ➔ Glicerol", grupos: ["ruta_tejido_adiposo", "badge_via_19", "badge_leyenda_19"], color: "#ea580c" },
      "20": { numero: "20", id: "20", nombre: "Músculo esquelético y sarcómero (Cori/Cahill)", subtitulo: "Sarcómero estriado en contracción • Cori (Lactato) • Cahill (Alanina)", grupos: ["ruta_musculo_esqueletico", "badge_via_20", "badge_leyenda_20"], color: "#9f1239" },
      "21": { numero: "21", id: "21", nombre: "Cerebro y combustibles neuronales", subtitulo: "Barrera hematoencefálica • GLUT1/3 • Adaptación a cuerpos cetónicos", grupos: ["ruta_cerebro_combustibles", "badge_via_21", "badge_leyenda_21"], color: "#2563eb" },
      "22": { numero: "22", id: "22", nombre: "Lipoproteínas plasmáticas (VLDL/LDL/HDL)", subtitulo: "VLDL ➔ LDL (LDLR) • HDL y transporte reverso de colesterol (SR-B1)", grupos: ["ruta_lipoproteinas", "badge_via_22", "badge_leyenda_22"], color: "#2563eb" },
      "23": { numero: "23", id: "23", nombre: "Biosíntesis de TAG y fosfolípidos (Kennedy)", subtitulo: "Glicerol-3-P ➔ LPA ➔ PA ➔ DAG ➔ TAG / Fosfatidilcolina", grupos: ["ruta_sintesis_tag_fosfolipidos", "badge_via_23", "badge_leyenda_23"], color: "#7c3aed" },
      "24": { numero: "24", id: "24", nombre: "Biosíntesis de aminoácidos no esenciales", subtitulo: "10 aminoácidos desde esqueletos de Glucólisis y Ciclo de Krebs", grupos: ["ruta_biosintesis_aminoacidos", "badge_via_24", "badge_leyenda_24"], color: "#059669" },
      "25": { numero: "25", id: "25", nombre: "Integración y conmutador nutricional", subtitulo: "Flujos de combustible: Posprandial vs Ayuno vs Ejercicio vigoroso", grupos: ["ruta_conmutador_estados", "badge_via_25", "badge_leyenda_25"], color: "#ea580c" }
    };

    const TABLA_ESTADOS_METABOLICOS = {
      normal: {
        id: "normal",
        nombre: "Normal (Mapa Completo)",
        subtitulo: "Visualización de referencia",
        descripcion: "Todas las 25 vías se muestran con su intensidad gráfica estándar.",
        activas: [],
        atenuadas: []
      },
      posprandial: {
        id: "posprandial",
        nombre: "Estado Posprandial",
        hormonas: "Insulina alta ↑ • Glucagón bajo ↓",
        descripcion: "Favorece utilización de glucosa, almacenamiento de glucógeno, lipogénesis, vía de pentosas, digestión lipídica (quilomicrones), VLDL, vía de Kennedy y biosíntesis de aminoácidos.",
        activas: ["1", "3", "4", "5", "6", "7", "10", "12", "18", "22", "23", "24"],
        atenuadas: ["2", "9", "11", "19"]
      },
      ayuno: {
        id: "ayuno",
        nombre: "Estado de Ayuno",
        hormonas: "Glucagón alto ↑ • Insulina baja ↓",
        descripcion: "Favorece gluconeogénesis hepática, lipólisis masiva adiposa (ATGL/HSL/MGL), β-oxidación, cetogénesis, ciclo de la urea, ciclo de Cori/Cahill muscular y adaptación cerebral a cetonas.",
        activas: ["2", "3", "9", "11", "14", "17", "19", "20", "21"],
        atenuadas: ["1", "10", "12", "18", "23"]
      }
    };

    // Variables de estado
    let viaResaltadaActual = null;
    let estadoMetabolicoActual = 'normal';
    let pointerDownX = 0;
    let pointerDownY = 0;
    let searchMatches = [];
    let searchMatchIndex = 0;
    let searchPulseElement = null;

    // Conjunto de todos los grupos registrados
    const TODOS_LOS_GRUPOS_VIAS = new Set();
    Object.values(TABLA_VIAS).forEach(v => {
      v.grupos.forEach(gid => TODOS_LOS_GRUPOS_VIAS.add(gid));
    });

    // Normalizador de texto
    function uiNormalize(str) {
      return (str || '')
        .normalize('NFD')
        .replace(/[\\u0300-\\u036f]/g, '')
        .toLowerCase()
        .trim();
    }

    // =========================================================================
