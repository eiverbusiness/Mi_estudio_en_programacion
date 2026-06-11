const botones = document.querySelectorAll('.btn');
const ventana = document.getElementById('miVentana');
const botonNo = document.getElementById('no');
botones.forEach(boton => {
    boton.addEventListener('click', () => {
        const botonApretado = boton.textContent;
        if(botonApretado === "Si"){
            ventana.className = "modal-visible";
        }
        else{
            return;
        }
    })
})
botonNo.addEventListener('mouseenter', () => {
    const randomY = Math.floor(Math.random() * 240) - 120;
    const randomX = Math.floor(Math.random() * 240) - 120;

    // Aplicamos los estilos directamente al botón No
    botonNo.style.top = `${randomY}px`;
    botonNo.style.left = `${randomX}px`; // 
})