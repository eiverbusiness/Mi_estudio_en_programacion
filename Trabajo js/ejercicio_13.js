// voy a usar como variables sus ejemplos en numeros xdd
let numero = 28;
let divisoresSum = 0;

for(let i = 1; i < numero; i++)
{
    if(numero % i === 0)
    {
        divisoresSum += i;
    }
}
if(divisoresSum === numero)
{
    console.log("Es numero perfecto "+ numero);
}
else
{
    console.log("No es un numero perfecto " + numero);
}