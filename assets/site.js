// Menú móvil
const btn = document.querySelector('.menu-btn');
const nav = document.getElementById('nav');
if (btn && nav) {
  btn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}

// Formularios de demostración: no envían datos
document.querySelectorAll('form[data-demo]').forEach((form) => {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const note = form.querySelector('.form-note');
    if (note) { note.classList.add('show'); note.focus(); }
  });
});

// Filtro de noticias / marcas por categoría
document.querySelectorAll('[data-filter-group]').forEach((group) => {
  const target = document.querySelector(group.dataset.filterGroup);
  group.querySelectorAll('.chip').forEach((chip) => {
    chip.addEventListener('click', () => {
      group.querySelectorAll('.chip').forEach((c) => c.setAttribute('aria-pressed', 'false'));
      chip.setAttribute('aria-pressed', 'true');
      const f = chip.dataset.filter;
      target.querySelectorAll('[data-cat]').forEach((el) => {
        el.hidden = f !== 'all' && !el.dataset.cat.split(' ').includes(f);
      });
    });
  });
});

// Búsqueda de demo en catálogos: muestra el término buscado
const q = new URLSearchParams(location.search).get('q');
const qOut = document.getElementById('q-result');
if (q && qOut) {
  qOut.hidden = false;
  qOut.querySelector('strong').textContent = q;
  const input = document.getElementById('q');
  if (input) input.value = q;
}
