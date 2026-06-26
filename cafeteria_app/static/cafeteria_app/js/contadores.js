function cambiarCantidad(boton, delta) {
    const contenedor = boton.closest('.producto-controles');
    if (!contenedor) return;
    const span = contenedor.querySelector('.cantidad');
    const input = contenedor.querySelector('input[name="quantity"]');
    let cantidad = parseInt(span.textContent, 10) || 1;
    cantidad = Math.max(1, cantidad + delta);
    span.textContent = cantidad;
    input.value = cantidad;
    const contenedorPrecio = document.getElementById('precio-detail');
    const spanTotal = document.getElementById('total-precio');
    if (contenedorPrecio && spanTotal) {
        const preciodetail = parseInt(contenedorPrecio.dataset.precio, 10) || 0;
        const totaldetalle = cantidad * preciodetail;
        spanTotal.textContent = totaldetalle.toLocaleString('es-CL'); 
    }
}