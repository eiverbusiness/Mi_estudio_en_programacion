let numero = 7;

while(numero !== 1)
{
    console.log(numero);

    if(numero % 2 === 0)
    {
        numero = numero / 2;
    }
    else
    {
        numero = (numero * 3) + 1;
    }
}
console.log(numero);