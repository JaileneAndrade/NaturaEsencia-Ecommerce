let contador = 0;
const contadorCarrito = document.querySelector("#contador-carrito");

function agregarAlCarrito(id) {
  contador++;

  if (contadorCarrito) {
    contadorCarrito.innerText = contador;
  }
}
