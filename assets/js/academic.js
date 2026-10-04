/* Dependency-free enhancements. Content remains readable without JavaScript. */
(() => {
  const tools = document.querySelector('.publication-tools');
  if (tools) {
    const papers = [...document.querySelectorAll('.publication-list .publication')];
    const groups = [...document.querySelectorAll('[data-publication-group]')];
    const topics = [...tools.querySelectorAll('[data-filter]')];
    const types = [...tools.querySelectorAll('[data-type-filter]')];
    const count = tools.querySelector('.result-count');
    const empty = document.querySelector('.publication-empty');
    let topic = 'all', type = 'all';
    tools.hidden = false;
    function filter() {
      let visible = 0;
      papers.forEach(paper => {
        paper.hidden = (topic !== 'all' && paper.dataset.topic !== topic) || (type !== 'all' && paper.dataset.type !== type);
        if (!paper.hidden) visible += 1;
      });
      groups.forEach(group => group.hidden = ![...group.querySelectorAll('.publication')].some(paper => !paper.hidden));
      topics.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === topic)));
      types.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.typeFilter === type)));
      count.textContent = `${visible} ${visible === 1 ? 'publication' : 'publications'}`;
      if (empty) empty.hidden = visible !== 0;
    }
    topics.forEach(button => button.addEventListener('click', () => { topic = button.dataset.filter; filter(); }));
    types.forEach(button => button.addEventListener('click', () => { type = button.dataset.typeFilter; filter(); }));
    filter();
  }
  const panels = [...document.querySelectorAll('[data-scholar-stats]')];
  if (!panels.length || typeof fetch !== 'function') return;
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 5000);
  fetch(panels[0].dataset.statsUrl, { signal: controller.signal, cache: 'no-cache' })
    .then(response => { if (!response.ok) throw new Error('Citation data unavailable'); return response.json(); })
    .then(data => {
      if (data.scholar_id !== panels[0].dataset.scholarId || data.source !== 'Google Scholar' || !Number.isSafeInteger(data.citedby) || data.citedby < 0) return;
      const updated = new Date(data.updated);
      if (!Number.isFinite(updated.getTime()) || updated > new Date(Date.now() + 86400000)) return;
      panels.forEach(panel => {
        if (updated <= new Date(panel.dataset.snapshotDate)) return;
        panel.querySelector('[data-citation-count]').textContent = data.citedby.toLocaleString('en-GB');
        panel.querySelector('[data-citation-label]').textContent = 'Google Scholar citations ↗';
        const date = updated.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' });
        panel.querySelector('[data-stats-source]').textContent = `Google Scholar · Last checked ${date}`;
      });
    })
    .catch(() => { /* Keep the dated snapshot if the latest data cannot be loaded. */ })
    .finally(() => clearTimeout(timeout));
})();
