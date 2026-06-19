function cambiarCantidad(boton, delta) {
    const contenedor = boton.closest('.producto-controles');
    const span = contenedor.querySelector('.cantidad');
    const input = contenedor.querySelector('input[name="quantity"]');
    const preciodetail = parseInt(document.getElementById('precio-detail').dataset.precio);
    const spanTotal = document.getElementById('total-precio');
    let cantidad = parseInt(span.textContent, 10) || 1;
    cantidad = Math.max(1, cantidad + delta);
    span.textContent = cantidad;
    input.value = cantidad;
    const totaldetalle = cantidad * preciodetail;
    spanTotal.textContent = totaldetalle; 
}