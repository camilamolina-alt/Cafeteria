function setTab(btn) {
    document.querySelectorAll('.btn-tab').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const tab = btn.dataset.tab;
    document.querySelectorAll('[data-group]').forEach(card => {
        if (tab === 'Todos') {
            card.classList.remove('d-none');
        } else if (card.dataset.group === tab) {
            card.classList.remove('d-none');
        } else {
            card.classList.add('d-none');
        }
    });
}

function abrirReserva(nombreEvento) {
    const seccionReserva = document.getElementById('seccion-reserva');
    const textoEvento = document.getElementById('evento-seleccionado');
    const inputOculto = document.getElementById('input-evento-nombre');

    seccionReserva.classList.remove('d-none');
    textoEvento.textContent = nombreEvento.toUpperCase();
    inputOculto.value = nombreEvento;

    seccionReserva.scrollIntoView({ behavior: 'smooth' });
}

function cancelarReserva() {
    const seccionReserva = document.getElementById('seccion-reserva');
    seccionReserva.classList.add('d-none');
    document.getElementById('form-reserva').reset();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}