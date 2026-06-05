let cart = [];

function agregarAlCarro(nombre, precio) {
    const item = cart.find(producto => producto.nombre === nombre);
    if (item) {
        item.cantidad += 1;
    } else {
        cart.push({ nombre, precio, cantidad: 1 });
    }
    actualizarCarro();
}

function removerDelCarro(nombre) {
    cart = cart.filter(producto => producto.nombre !== nombre);
    actualizarCarro();
}

function actualizarCarro() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    cartItems.innerHTML = '';
    let total = 0;

    cart.forEach(producto => {
        const li = document.createElement('li');
        li.textContent = `${producto.nombre} - $${producto.precio} x ${producto.cantidad}`;
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Eliminar';
        removeButton.onclick = () => removerDelCarro(producto.nombre);
        li.appendChild(removeButton);
        cartItems.appendChild(li);
        total += producto.precio * producto.cantidad;
    });

    cartTotal.textContent = `$${total}`;
}