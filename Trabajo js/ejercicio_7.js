let numero_1 = 20;
let numero_2 = 14;
let operacion = "*";
let resultado = 0;

switch(operacion)
{
    case "+":
        resultado = numero_1 + numero_2;
        console.log(resultado);
        break;
    case "-":
        resultado = numero_1 - numero_2;
        console.log(resultado);
        break;
    case "*":
        resultado = numero_1 * numero_2;
        console.log(resultado);
        break;
    case "/":
        resultado = numero_1 / numero_2;
        console.log(resultado);
        break;
    case "%":
        resultado = numero_1 % numero_2;
        console.log(resultado);
        break;
    default:
        console.log("Operacion invalida");
}
