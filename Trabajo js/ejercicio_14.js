// me voy a volver loco
let numero = 25;
let primero = numero;
let binario = "";

if(numero === 0)
{
    binario = "0";
}

while(numero > 0)
{
    let bit = numero % 2;
    binario = bit + binario;
    numero = Math.floor(numero / 2);
}
console.log("Numero " + primero + " Binario: " + binario);