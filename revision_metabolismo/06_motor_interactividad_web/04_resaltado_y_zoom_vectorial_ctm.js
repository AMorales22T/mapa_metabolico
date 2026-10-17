/* ============================================================================
 * MÓDULO DE REVISIÓN: Resaltado de Vías y Zoom Animado con Matriz CTM
 * ============================================================================
 * Archivo original : 07_AMPLIACION_TEMARIO/interactividad_html.py (líneas 847 a 1000 de 1638)
 * Descripción      : Funciones highlightPathway, clearPathwayHighlight, cálculo de bounding box con getCTM() y animación cúbica de cámara.
 * ============================================================================ */

    // 1. RESALTADO Y ATENUACIÓN DE VÍAS
    // =========================================================================
    function highlightPathway(viaId, shouldZoom = false) {
      const via = TABLA_VIAS[viaId];
      if (!via) return;

      viaResaltadaActual = viaId;

      TODOS_LOS_GRUPOS_VIAS.forEach(gid => {
        const el = document.getElementById(gid);
        if (el) {
          if (via.grupos.includes(gid)) {
            el.classList.add('ui_highlighted');
            el.classList.remove('ui_dimmed');
          } else {
            el.classList.add('ui_dimmed');
            el.classList.remove('ui_highlighted');
          }
        }
      });

      // Fondo y organelas
      const cxLayer = document.getElementById('capa_conexiones_inter_ruta');
      if (cxLayer) cxLayer.classList.add('ui_dimmed');

      const mitoBio = document.getElementById('mitocondria_biologica');
      const viasMito = ["2", "5", "6", "7", "8", "8B", "9", "11", "13", "14"];
      if (mitoBio) {
        if (viasMito.includes(viaId)) mitoBio.classList.remove('ui_dimmed');
        else mitoBio.classList.add('ui_dimmed');
      }

      // Gluconeogénesis: dejar glucólisis a 0.55
      const glucoTroncal = document.getElementById('ruta_glucolisis');
      if (glucoTroncal) {
        if (viaId === "2") {
          glucoTroncal.classList.remove('ui_dimmed');
          glucoTroncal.style.opacity = '0.55';
        } else {
          glucoTroncal.style.opacity = '';
        }
      }

      // Banner flotante
      const banner = document.getElementById('ui_highlight_banner');
      const bannerTitle = document.getElementById('ui_highlight_title');
      if (banner && bannerTitle) {
        bannerTitle.innerHTML = `<span style="background:${via.color}; color:#fff; border-radius:50%; width:20px; height:20px; display:inline-flex; align-items:center; justify-content:center; font-size:11px; font-weight:900; margin-right:8px;">${via.numero}</span> Vía ${via.numero}: ${via.nombre}`;
        banner.classList.add('ui_visible');
      }

      // Sidebar item activo
      document.querySelectorAll('.ui_sidebar_item').forEach(it => {
        if (it.getAttribute('data-via') === viaId) {
          it.classList.add('ui_active');
          it.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        } else {
          it.classList.remove('ui_active');
        }
      });

      if (shouldZoom) {
        const mainEl = document.getElementById(via.grupos[0]);
        if (mainEl) zoomToElement(mainEl);
      }
    }

    function clearPathwayHighlight() {
      viaResaltadaActual = null;

      const glucoTroncal = document.getElementById('ruta_glucolisis');
      if (glucoTroncal) glucoTroncal.style.opacity = '';

      if (estadoMetabolicoActual !== 'normal') {
        setMetabolicState(estadoMetabolicoActual);
        const banner = document.getElementById('ui_highlight_banner');
        if (banner) banner.classList.remove('ui_visible');
        return;
      }

      TODOS_LOS_GRUPOS_VIAS.forEach(gid => {
        const el = document.getElementById(gid);
        if (el) {
          el.classList.remove('ui_dimmed');
          el.classList.remove('ui_highlighted');
        }
      });

      const cxLayer = document.getElementById('capa_conexiones_inter_ruta');
      if (cxLayer) cxLayer.classList.remove('ui_dimmed');
      const mitoBio = document.getElementById('mitocondria_biologica');
      if (mitoBio) mitoBio.classList.remove('ui_dimmed');

      const banner = document.getElementById('ui_highlight_banner');
      if (banner) banner.classList.remove('ui_visible');

      document.querySelectorAll('.ui_sidebar_item').forEach(it => it.classList.remove('ui_active'));
    }

    // =========================================================================
    // 2. ZOOM VECTORIAL CON MATRIZ CTM Y OFFSET DE LIENZO
    // =========================================================================
    function getElementSvgBounds(el) {
      try {
        const bbox = el.getBBox();
        const svg = document.querySelector('#panLayer svg');
        const ctm = el.getCTM();
        const svgCtm = svg ? svg.getCTM() : null;
        if (ctm && svgCtm) {
          const m = svgCtm.inverse().multiply(ctm);
          const pt1 = svg.createSVGPoint(); pt1.x = bbox.x; pt1.y = bbox.y;
          const pt2 = svg.createSVGPoint(); pt2.x = bbox.x + bbox.width; pt2.y = bbox.y + bbox.height;
          const p1 = pt1.matrixTransform(m);
          const p2 = pt2.matrixTransform(m);
          return {
            x: Math.min(p1.x, p2.x),
            y: Math.min(p1.y, p2.y),
            width: Math.abs(p2.x - p1.x),
            height: Math.abs(p2.y - p1.y)
          };
        }
        return bbox;
      } catch (e) {
        return null;
      }
    }

    function zoomToElement(el, paddingFactor = 1.6) {
      if (!el) return;
      const bounds = getElementSvgBounds(el);
      if (!bounds || bounds.width === 0 || bounds.height === 0) return;

      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;

      const targetScale = Math.min(
        Math.max((vw / (bounds.width * paddingFactor)), 0.35),
        2.5
      );

      const cx = bounds.x + bounds.width / 2;
      const cy = bounds.y + bounds.height / 2;

      // Conversión a coordenadas en panLayer teniendo en cuenta VB_X y VB_Y
      const px = cx - VB_X;
      const py = cy - VB_Y;

      scale = targetScale;
      pointX = vw / 2 - px * scale;
      pointY = vh / 2 - py * scale;
      updateTransform();
    }

    // =========================================================================
