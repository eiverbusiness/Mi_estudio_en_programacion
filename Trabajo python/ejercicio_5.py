import random
import os
os.system('cls')

numero = random.randint(1, 20)
intento = 0

print("--JUEGO DE ADIVINAR EL NUMERO--")
while True:
    intento_usuario = int(input("Elije un numero de el 1 al 10: "))
    intento += 1

    if intento_usuario < numero:
        print("El numero es mas alto!")
    elif(intento_usuario > numero):
        print("El numero es mas bajo!")
    else:
        print(f"Felicidades ganaste! adivinaste en {intento} intentos")
        break