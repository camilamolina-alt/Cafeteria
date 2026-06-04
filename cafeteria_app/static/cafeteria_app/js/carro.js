let cart = [];

<<<<<<< HEAD
function agregarAlCarro(nombre, precio){
    const item = cart.find(producto => producto.nombre === nombre);
    if (item){
        item.cantidad+=1;    
    } else {
        cart.push({nombre, precio, cantidad:1})
=======
function agregarAlCarro(nombre, precio) {
    const item = cart.find(producto => producto.nombre === nombre);
    if (item) {
        item.cantidad += 1;
    } else {
        cart.push({ nombre, precio, cantidad: 1 });
>>>>>>> a703090129edd1969c6580ae9478498ba281f414
    }
    actualizarCarro();
}

<<<<<<< HEAD
function RemoverDelCarro(nombre){
    cart = cart.filter(producto => producto.nombre !==nombre);
    actualizarCarro();
}

function actualizarCarro(){
=======
function removerDelCarro(nombre) {
    cart = cart.filter(producto => producto.nombre !== nombre);
    actualizarCarro();
}

function actualizarCarro() {
>>>>>>> a703090129edd1969c6580ae9478498ba281f414
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    cartItems.innerHTML = '';
    let total = 0;
<<<<<<< HEAD
    cart.forEach(producto => {
        const li = document.createElement('li');
        li.textContent = '${producto.nombre} - $${producto.precio} x ${producto.cantidad}';
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Eliminar';
        removeButton.onclick = () => removerDelCarro(producto.nombre);
=======

    cart.forEach(producto => {
        const li = document.createElement('li');
        li.textContent = `${producto.nombre} - $${producto.precio} x ${producto.cantidad}`;
        
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Eliminar';
        removeButton.onclick = () => removerDelCarro(producto.nombre);
        
>>>>>>> a703090129edd1969c6580ae9478498ba281f414
        li.appendChild(removeButton);
        cartItems.appendChild(li);
        total += producto.precio * producto.cantidad;
    });
<<<<<<< HEAD
    cartTotal.textContent = 'total: $${total}';
}
const pagarRequest = new pagarRequest(
    [
        {
            metodoSoportado: 'Tarjeta',
            data: {
                tiposDeTarjeta: ['visa', 'mastercard'], 
            },
        },
    ],
    {
        total: {
            label: 'Total',
            cantidad: { currency: 'CLP', value: '0.00'},
        },
    }
);
pagarRequest.show().then((pagarRespuesta) => {
    console.log(pagarRespuesta);

    pagarRespuesta.complete('Exito').then(() => {
        console.log('Pago completado con éxito');
    });
}).catch((error) => {
    console.error('Error en el pago');
});
=======

    cartTotal.textContent = `Total: $${total}`;
}

async function procesarPago() {
    const totalCarrito = cart.reduce((sum, p) => sum + p.precio * p.cantidad, 0);

    const paymentRequest = new PaymentRequest(
        [
            {
                supportedMethods: 'basic-card',
                data: {
                    supportedNetworks: ['visa', 'mastercard'],
                },
            },
        ],
        {
            total: {
                label: 'Total',
                amount: { currency: 'CLP', value: totalCarrito.toString() },
            },
        }
    );

    try {
        const paymentResponse = await paymentRequest.show();
        console.log(paymentResponse);
        await paymentResponse.complete('success');
        console.log('Pago completado con éxito');
    } catch (error) {
        console.error('Error en el pago:', error);
    }
}
>>>>>>> a703090129edd1969c6580ae9478498ba281f414
