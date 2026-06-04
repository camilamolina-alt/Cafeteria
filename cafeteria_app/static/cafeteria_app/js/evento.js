function setTab(btn) {
    document.querySelectorAll('.btn-tab').forEach(b => {
        b.classList.remove('btn-dark');
        b.classList.add('btn-light');
    });
    btn.classList.remove('btn-light');
    btn.classList.add('btn-dark');

    const tab = btn.dataset.tab;
    document.querySelectorAll('[data-group]').forEach(card => {
        // Usamos un enfoque compatible con Bootstrap (d-block y d-none) 
        // o style.display directo para ocultar/mostrar las columnas de la grilla
        if (card.dataset.group === tab) {
            card.style.setProperty('display', 'block', 'important');
        } else {
            card.style.setProperty('display', 'none', 'important');
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const primero = document.querySelector('[data-tab]');
    if (primero) setTab(primero);
});