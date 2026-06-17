import os
os.system("cls")


numero = int(input("Numero: "))

for posicion in [1, 2]:
    resultado = numero << posicion

    factor = 2 if posicion == 1 else 4
    print(f"Multiplicado por {factor} desplazando {posicion} bits: {resultado}")