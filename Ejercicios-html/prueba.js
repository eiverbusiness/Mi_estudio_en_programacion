import PromptSync from "prompt-sync";
const prompt = PromptSync({sigint: true});

let dato = prompt("Ingresa tu nombre:");
console.log("Tu nombre es:", dato);

let edad= Number(prompt("Cual es tu edad:"));
console.log("Tu edad es:", edad);


let Nombre = "EIVER";

console.log(`Hola mi nombre es ${eiver}`);


let edad_cumplir = Number(prompt("Dime tu edad para entrar:"));
let mensaje;

if(edad_cumplir < 18){
    mensaje = "No puedes pasar eres menor de edad"
}

else{
    mensaje = "Eres mayor de edad, adelante"
}

console.log(mensaje)


const Rol_usuario = prompt("Ingrese su rol en la empresa: ");

switch(Rol_usuario){
    case "admin":
        console.log("Acceso concedido, tiene acceso a todo nuestra base de datos");
        break;
    case "usuario":
        console.log("No tienes acceso a muchas cosas");
        break;
    default:
        console.log("Rol no reconocido, intentalo de nuevo")
    
}


let numero = 0;

for (numero = 1; numero <= 10; numero ++){
    const resultado = numero + 1;
    console.log(`${resultado}`)
}

let numero = 1;
let conteo = 0;
let objetivo = 10

while (numero <= objetivo){
    conteo += 1
    console.log(conteo)
    if (objetivo == conteo){
        break;
    }
}
