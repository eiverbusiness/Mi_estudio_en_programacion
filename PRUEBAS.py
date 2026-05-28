import math
import random
"""
boton_programa = True

lista= []
resultado = 0
while boton_programa:
    print("\n__CALCULADORA PROMEDIO__")
    print("1. para introducir un numero")
    print("Para finalizar el programa escriba fin.")
    opcion = input("Elija la opcion: ").lower().strip()
    
    if opcion == "1":
        numero = int(input("Ingrese el numero:"))
        lista.append(numero)
        print(f"el {numero} se introdujo correctamente")
        continue
    elif opcion == "fin":
        for n in lista:
            resultado += n
            promedio = math.pow(resultado)
            print(f"la suma de los numeros ingresados es: {promedio}")
            boton_programa =False
            break
    else:
        print("Opcion invalida. ingrese un nuevo numero")
"""
# ejercicio 2 de el examen

def contador(usuario):
    vocales = "aeiouAEIOU"
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    numero_vocales = 0
    consonante_numero = 0


    for l in usuario:
        if l in vocales:
            numero_vocales += 1
        elif l in consonantes:
            consonante_numero +=1    
    print(f"La palabra {usuario} tiene {numero_vocales} vocales y {consonante_numero} consonantes")
    
print(contador("Eiver"))


#ejercicio 3

triangulo = int(input("ingrese un numero: "))

for n in range(1, triangulo + 1):
    print("*" * n)

#ejercicio 4

programa = True

numero_aleatorio = random.randint(1, 100)
while programa:
    adivinar = int(input("Ingrese un numero para adivinar: "))
    if adivinar < numero_aleatorio:
        print(f"{adivinar} es menor que el numero aleatorio")
    elif adivinar > numero_aleatorio:
        print(f"{adivinar} es mayor que el numero aleatorio")
    elif adivinar == numero_aleatorio:
        print("adivinaste el numero aleatorio.")
        programa = False
        break
    else:
            print("Introduzca un numero")
    







    



    

    

    
        



    

    
    







