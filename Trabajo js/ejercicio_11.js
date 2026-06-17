//Como  fibonacci es a y b asi seran las variables
let a = 0;
let b = 1;

for(let i = 0; i < 15; i++)
{
    console.log(a);

    //como es sucesion  voy a reasignar los valores
    let continuacion = a + b;
    a = b;
    b = continuacion;
}