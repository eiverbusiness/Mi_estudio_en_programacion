let cuadrado = 5;

for(let i = 0; i < cuadrado; i++)
{
    //como es un cuadrado agrego una variable en for  una fila vacia
    let fila = "";

    // agrego otro for para controlar la columna
    for(let c = 0; c < cuadrado; c++)
    {
        fila += "* ";// le coloco un espacio a el * para que quede cuadrado
    }
    console.log(fila); // en python hubiera colocado un .join xddd

}