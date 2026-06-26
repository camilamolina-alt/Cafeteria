function cambiarCantidad(boton, delta) {
    const contenedor = boton.closest('.producto-controles');
    if (!contenedor) return;

    const stockMaximo = parseInt(contenedor.dataset.stock, 10) || 0;
    const span = contenedor.querySelector('.cantidad');
    const input = contenedor.querySelector('input[name="quantity"]');
    const btnMenos = contenedor.querySelector('.btn-menos');
    const btnMas = contenedor.querySelector('.btn-mas');
    
    let cantidad = parseInt(span.textContent, 10) || 1;
    cantidad = cantidad + delta;
    cantidad = Math.max(1, Math.min(cantidad, stockMaximo));

    span.textContent = cantidad;
    input.value = cantidad;

    if (btnMenos) btnMenos.disabled = (cantidad <= 1);
    if (btnMas) btnMas.disabled = (cantidad >= stockMaximo);

    const contenedorPrecio = document.getElementById('precio-detail');
    const spanTotal = document.getElementById('total-precio');
    if (contenedorPrecio && spanTotal) {
        const preciodetail = parseInt(contenedorPrecio.dataset.precio, 10) || 0;
        const totaldetalle = cantidad * preciodetail;
        spanTotal.textContent = totaldetalle.toLocaleString('es-CL'); 
    }
}
document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll('.producto-controles').forEach(contenedor => {
        const btnMas = contenedor.querySelector('.btn-mas');
        if (btnMas) cambiarCantidad(btnMas, 0);
    });
});