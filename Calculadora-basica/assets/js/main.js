const botones = document.querySelectorAll('.btn');
const pantalla = document.querySelector('.pantalla');

botones.forEach( boton => { // POR CADA BOTON
    boton.addEventListener("click", () => { // agrega un evento que es click
        const botonApretado = boton.textContent; // muestra el contenido de el boton aprentado

        if(boton.id === "c") // Al pulsar el boton C  vuelve a poner en el div pantalla el 0
        {
            pantalla.textContent = "0";
            return; // retorna para no cumplir las demas condiciones
        }
        if(boton.id === "borrar") // si se pulsa el boton borrar que es la flecha, borra todo lo de la pantalla
        {
            if(pantalla.textContent.length === 1 || pantalla.textContent === "Error") // condicion para que cuando se borre hasta el ultimo numero no deje vacia la pantalla, y para no borrar el texto Error

            {
                pantalla.textContent = "0"; //deja en cero cuando se cumple la condicion
            }
            else{
                pantalla.textContent = pantalla.textContent.slice(0, -1); // use el metodo slice para que vaya borrando o tajando cada numero hasta llegar al ultimo
            }
            return;// retorna para no cumplir las demas condiciones
        }
        if(boton.id === "igual") // al pulsar el boton igual ejecuta una funcion de javascript que evalua todo el string matematico de la pantalla, y lo muestra en pantalla
        {
            try// try catch para que se cumpla lo primero pero cuando el string matematico no pueda cumplirse porque es imposible, muestra en pantalla el catch que es el string ERROR
            {
                pantalla.textContent = eval(pantalla.textContent);
            }
            catch
            {
                pantalla.textContent = "Error";
            }
            return;// retorna para no cumplir las demas condiciones
        }
        if(pantalla.textContent === "0" || pantalla.textContent === "Error") // condicional para  colocar los botones apretados en pantalla y para que no se puedan sumar mas numeros despues de un error
        {
            pantalla.textContent = botonApretado;// muestra en pantalla el boton apretado
        }
        else
        {
            pantalla.textContent += botonApretado; // suma en pantalla los numeros apretados
        }
    })
})