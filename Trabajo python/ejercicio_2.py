import os
os.system('cls')

limitUsuario = int(input("Ingrese el limite de la suma: "))
suma = 0

for n in range(1, limitUsuario + 1):
    suma += n

print(f"La suma es: {suma}")