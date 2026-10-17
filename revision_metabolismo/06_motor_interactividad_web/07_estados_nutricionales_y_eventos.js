/* ============================================================================
 * MÓDULO DE REVISIÓN: Modulador de Estados Nutricionales, Eventos Táctiles y Teclado
 * ============================================================================
 * Archivo original : 07_AMPLIACION_TEMARIO/interactividad_html.py (líneas 1305 a 1620 de 1638)
 * Descripción      : Filtro Posprandial/Ayuno, distinción clic vs arrastre (<=4px), pinch-to-zoom multitáctil y atajos (/, Esc, F).
 * ============================================================================ */

    // 6. ESTADOS METABÓLICOS
    // =========================================================================
    function setMetabolicState(stateId) {
      const st = TABLA_ESTADOS_METABOLICOS[stateId] || TABLA_ESTADOS_METABOLICOS.normal;
      estadoMetabolicoActual = st.id;

      document.querySelectorAll('.ui_state_btn').forEach(btn => {
        if (btn.id === `ui_btn_state_${st.id === 'posprandial' ? 'fed' : st.id === 'ayuno' ? 'fasting' : 'normal'}`) {
          btn.classList.add('ui_active');
        } else {
          btn.classList.remove('ui_active');
        }
      });

      const banner = document.getElementById('ui_state_banner');
      const bannerText = document.getElementById('ui_state_banner_text');

      if (st.id === 'normal') {
        TODOS_LOS_GRUPOS_VIAS.forEach(gid => {
          const el = document.getElementById(gid);
          if (el) {
            el.classList.remove('ui_dimmed');
            el.classList.remove('ui_state_active');
          }
        });
        const cxLayer = document.getElementById('capa_conexiones_inter_ruta');
        if (cxLayer) cxLayer.classList.remove('ui_dimmed');
        const mitoBio = document.getElementById('mitocondria_biologica');
        if (mitoBio) mitoBio.classList.remove('ui_dimmed');
        if (banner) banner.classList.remove('ui_visible');
        return;
      }

      const gruposActivos = new Set();
      st.activas.forEach(vid => {
        const v = TABLA_VIAS[vid];
        if (v) v.grupos.forEach(gid => gruposActivos.add(gid));
      });

      const gruposAtenuados = new Set();
      st.atenuadas.forEach(vid => {
        const v = TABLA_VIAS[vid];
        if (v) v.grupos.forEach(gid => gruposAtenuados.add(gid));
      });

      TODOS_LOS_GRUPOS_VIAS.forEach(gid => {
        const el = document.getElementById(gid);
        if (el) {
          if (gruposActivos.has(gid)) {
            el.classList.add('ui_state_active');
            el.classList.remove('ui_dimmed');
          } else if (gruposAtenuados.has(gid)) {
            el.classList.add('ui_dimmed');
            el.classList.remove('ui_state_active');
          } else {
            el.classList.add('ui_dimmed');
            el.classList.remove('ui_state_active');
          }
        }
      });

      if (banner && bannerText) {
        bannerText.innerHTML = `<strong>${st.nombre} (${st.hormonas})</strong> • ${st.descripcion}`;
        banner.classList.add('ui_visible');
      }
    }

    // =========================================================================
    // 7. DISTINCIÓN CLIC VS ARRASTRE Y EVENTOS DE INTERACCIÓN
    // =========================================================================
    function manejarClicEnLienzo(e, clientX, clientY) {
      const target = document.elementFromPoint(clientX, clientY);
      if (!target) return;

      // Clic en badge de vía (en mapa, leyenda o encabezado)
      const badge = target.closest('.badge-via');
      if (badge) {
        const dataVia = badge.getAttribute('data-via');
        if (dataVia && TABLA_VIAS[dataVia]) {
          highlightPathway(dataVia, false);
          return;
        }
        const viaEntry = Object.values(TABLA_VIAS).find(v => v.grupos.includes(badge.id));
        if (viaEntry) {
          highlightPathway(viaEntry.id, false);
          return;
        }
      }

      // Clic en encabezado de sección
      const enc = target.closest('.encabezado-seccion');
      if (enc) {
        const badgeChild = enc.querySelector('.badge-via');
        if (badgeChild) {
          const dataVia = badgeChild.getAttribute('data-via');
          if (dataVia && TABLA_VIAS[dataVia]) {
            highlightPathway(dataVia, false);
            return;
          }
          const viaEntry = Object.values(TABLA_VIAS).find(v => v.grupos.includes(badgeChild.id));
          if (viaEntry) {
            highlightPathway(viaEntry.id, false);
            return;
          }
        }
      }

      // Clic en ruta o sección
      const ruta = target.closest('[id^="ruta_"], [id^="lupa_"]');
      if (ruta) {
        const viaEntry = Object.values(TABLA_VIAS).find(v => v.grupos.includes(ruta.id));
        if (viaEntry) {
          highlightPathway(viaEntry.id, false);
          return;
        }
      }

      // Clic en enzima o metabolito -> FIJAR FICHA ESTEQUIOMÉTRICA
      const targetRx = target.closest('[id^="rx_"], [id^="m_"]');
      if (targetRx) {
        pinTooltip(targetRx, clickX, clickY);
        return;
      }

      // Clic fuera de reacción y fuera de tooltip -> desanclar ficha
      if (!target.closest('#ui_tooltip_card')) {
        unpinTooltip();
      }

      // Clic en fondo o espacio vacío
      if (target.tagName === 'svg' || target.id === 'viewport' || target.id === 'panLayer' || target.id === 'print_fondo_base' || target.id === 'print_fondo_izq' || target.id === 'print_fondo_der' || target.tagName === 'rect') {
        clearPathwayHighlight();
      }
    }

    viewport.addEventListener('mousedown', (e) => {
      if (e.target.closest('#ui_sidebar_panel, .header-bar, #ui_btn_sidebar_floating, #ui_highlight_banner, #ui_state_banner, #ui_tooltip_card')) return;
      isPanning = true;
      startX = e.clientX - pointX;
      startY = e.clientY - pointY;
      pointerDownX = e.clientX;
      pointerDownY = e.clientY;
      viewport.classList.add('grabbing');
    });

    window.addEventListener('mousemove', (e) => {
      if (!isPanning) return;
      pointX = e.clientX - startX;
      pointY = e.clientY - startY;
      updateTransform();
    });

    window.addEventListener('mouseup', (e) => {
      if (isPanning) {
        isPanning = false;
        viewport.classList.remove('grabbing');
        const dist = Math.hypot(e.clientX - pointerDownX, e.clientY - pointerDownY);
        if (dist <= 4) {
          manejarClicEnLienzo(e, e.clientX, e.clientY);
        }
      }
    });

    viewport.addEventListener('wheel', (e) => {
      e.preventDefault();
      const xs = (e.clientX - pointX) / scale;
      const ys = (e.clientY - pointY) / scale;
      const delta = -e.deltaY;
      const factor = delta > 0 ? 1.15 : 0.85;
      scale = Math.min(Math.max(scale * factor, 0.08), 5.0);
      pointX = e.clientX - xs * scale;
      pointY = e.clientY - ys * scale;
      updateTransform();
    }, { passive: false });

    // Tooltip en movimiento de ratón
    viewport.addEventListener('mousemove', (e) => {
      if (isPanning) {
        if (!isTooltipPinned) ocultarTooltip();
        return;
      }
      if (isTooltipPinned) return; // Si está fijada, no la movemos con el cursor
      const target = e.target.closest('[id^="m_"], [id^="rx_"]');
      if (target) {
        mostrarTooltip(target, e.clientX, e.clientY, false);
      } else {
        ocultarTooltip();
      }
    });

    viewport.addEventListener('mouseleave', () => {
      if (!isTooltipPinned) ocultarTooltip();
    });

    // =========================================================================
    // 8. SOPORTE TÁCTIL (PAN Y PELLIZCO PARA ZOOM)
    // =========================================================================
    let touchPinching = false;
    let touchStartDist = 0;
    let touchStartScale = 1;
    let touchMidX = 0;
    let touchMidY = 0;

    viewport.addEventListener('touchstart', (e) => {
      ocultarTooltip();
      if (e.target.closest('#ui_sidebar_panel, .header-bar, #ui_btn_sidebar_floating, #ui_highlight_banner, #ui_state_banner, #ui_tooltip_card')) return;
      if (e.touches.length === 1) {
        isPanning = true;
        startX = e.touches[0].clientX - pointX;
        startY = e.touches[0].clientY - pointY;
        pointerDownX = e.touches[0].clientX;
        pointerDownY = e.touches[0].clientY;
      } else if (e.touches.length === 2) {
        isPanning = false;
        touchPinching = true;
        touchStartDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
        touchStartScale = scale;
        touchMidX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
        touchMidY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
      }
    }, { passive: true });

    viewport.addEventListener('touchmove', (e) => {
      if (isPanning && e.touches.length === 1) {
        pointX = e.touches[0].clientX - startX;
        pointY = e.touches[0].clientY - startY;
        updateTransform();
      } else if (touchPinching && e.touches.length === 2) {
        const curDist = Math.hypot(
          e.touches[0].clientX - e.touches[1].clientX,
          e.touches[0].clientY - e.touches[1].clientY
        );
        const xs = (touchMidX - pointX) / scale;
        const ys = (touchMidY - pointY) / scale;
        const newScale = Math.min(Math.max(touchStartScale * (curDist / touchStartDist), 0.08), 5.0);
        scale = newScale;
        pointX = touchMidX - xs * scale;
        pointY = touchMidY - ys * scale;
        updateTransform();
      }
    }, { passive: true });

    viewport.addEventListener('touchend', (e) => {
      if (isPanning && e.changedTouches.length === 1) {
        isPanning = false;
        const dist = Math.hypot(e.changedTouches[0].clientX - pointerDownX, e.changedTouches[0].clientY - pointerDownY);
        if (dist <= 6) {
          manejarClicEnLienzo(e, e.changedTouches[0].clientX, e.changedTouches[0].clientY);
        }
      }
      if (e.touches.length < 2) touchPinching = false;
    });

    // =========================================================================
    // 9. ATAJOS DE TECLADO
    // =========================================================================
    window.addEventListener('keydown', (e) => {
      const activeTag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
      if (activeTag === 'input' || activeTag === 'textarea') {
        if (e.key === 'Escape') {
          document.activeElement.blur();
          clearSearch();
        } else if (e.key === 'Enter') {
          e.preventDefault();
          if (e.shiftKey) searchPrev();
          else searchNext();
        }
        return;
      }

      if (e.key === '/') {
        e.preventDefault();
        const searchInput = document.getElementById('ui_search_input');
        if (searchInput) searchInput.focus();
      } else if (e.key === 'Escape') {
        unpinTooltip();
        clearPathwayHighlight();
        clearSearch();
        const panel = document.getElementById('ui_sidebar_panel');
        if (panel && panel.classList.contains('ui_open')) toggleSidebar();
        const menuViews = document.getElementById('ui_menu_views');
        if (menuViews) menuViews.style.display = 'none';
      } else if (e.key.toLowerCase() === 'f') {
        fitView();
      }
    });

    // Dropdown menú de vistas
    function toggleMenuViews(event) {
      event.stopPropagation();
      const menu = document.getElementById('ui_menu_views');
      if (menu) menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
    }
    document.addEventListener('click', () => {
      const menu = document.getElementById('ui_menu_views');
      if (menu) menu.style.display = 'none';
    });

    // Inicialización del buscador y vista
    const searchInputEl = document.getElementById('ui_search_input');
    if (searchInputEl) {
      searchInputEl.addEventListener('input', ejecutarBusqueda);
    }

    window.addEventListener('resize', fitView);

    window.addEventListener('DOMContentLoaded', () => {
      poblarSidebarVias();
      construirIndiceBusqueda();
      fitView();
    });

    // Por si el DOM ya estaba listo
