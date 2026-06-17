import os
os.system('cls')

lista_mixta = [1 , -2, 0, 22, -33, -140, 53, 67]

positivos = []

for n in lista_mixta:
    if n > 0:
        positivos.append(n)

print(f"La lista filtrada es: ", positivos)
