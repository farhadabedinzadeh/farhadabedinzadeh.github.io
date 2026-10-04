/* Small, dependency-free enhancements. The full site remains readable without JavaScript. */
(() => {
  const tools = document.querySelector('.publication-tools');
  if (!tools) return;
  const papers = [...document.querySelectorAll('.publication-list .publication')];
  const buttons = [...tools.querySelectorAll('[data-filter]')];
  const count = tools.querySelector('.result-count');
  tools.hidden = false;
  function filter(topic) {
    let visible = 0;
    papers.forEach(paper => {
      paper.hidden = topic !== 'all' && paper.dataset.topic !== topic;
      if (!paper.hidden) visible += 1;
    });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === topic)));
    count.textContent = `${visible} ${visible === 1 ? 'publication' : 'publications'}`;
  }
  buttons.forEach(button => button.addEventListener('click', () => filter(button.dataset.filter)));
  filter('all');
})();
