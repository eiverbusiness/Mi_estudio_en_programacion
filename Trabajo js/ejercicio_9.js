let numero = 5;
let primo = true;

if(numero <= 1)
{
    primo = false;
}
else
{
    for(let i = 2; i <= numero / 2; i++) // FOR HASTA LA MITAD DE EL NUMERO
    {
        if(numero % i === 0)
        {
            primo = false;
            break;
        }
    }
}

if(primo)
{
    console.log(numero + " es primo");
}
else
{
    console.log(numero + " No es primo");
}

