<?php
echo "_______Numeros pares______\n"
$pares = 0;

foreach(range(1, 50) as $n){
    if($n % 2 == 0){
        $pares += 1;
        echo "Numero par: ". $n."\n";
        echo "Hay: ". $pares. " Numeros pares\n";
    }
    else{
        echo "Numero impar: ". $n. "\n";
    }
}



/*ejercicio numero 2*/
echo "!------------Tablas de multiplicar--------------!"
$numero = (int) readline("Tabla de multiplicar ingrese un numero: ")

foreach(range(1, 9) as $n){
    $n +=1
    $resultado = $numero * $n
    echo "{$numero} x {$n} = {$resultado}"
}


/*Ejercicio 3*/
echo "_-_-_-_ADIVINA EL NUMERO_-_-_-_\n";
$boton = true;

while($boton){
    foreach(range(0, 3) as $intento){
        $numeroSecreto = 12;
        $adivinar = (int)readLine("Intenta adivinar el numero: ");
        if($adivinar == $numeroSecreto){
            echo "Adivinaste el numero!";
            $boton = false;
            break;
        }
        else{
            $intentos = $intento - 1;
            if($intentos > 0){
                echo "fallaste te quedan {$intentos} intentos\n";
            }
            else{
                echo "Fallaste, no adivinaste el numero\n";
                $boton = false;
                continue;
            }
        }
    }
}
/*ejercicio 4*/

foreach(range(1,99) as $impares){
    $impares + 1;
    if($impares % 2 == 1){
        $resultado = $impares + $impares;
        if($resultado == 50){
            echo "la suma de todos los numeros impares es: {$resultado}\n";
        }
    }
}

/*ejercicio 5 */
$licencia = (int) readline("Ingrese su edad: ");

if($licencia > 18 && $licencia <= 65 ){
    echo "Puede conducir";
}
else if($licencia  < 18 || $licencia > 65 ){
    echo "No puede conducir";
}

/*ejercicio 8*/
foreach (range(1,29) as $multiplos){
    $multiplos ++;
    echo $multiplos;
    if($multiplos % 3 = 0){
        echo "Mar";
    }
    else if($multiplos % 5 = 0){
        echo "tierra";
    }
    else if($multiplos % 5 = 0 && $multiplos % 3 = 0){
        echo "Mar y Tierra";
    }
}
?> 