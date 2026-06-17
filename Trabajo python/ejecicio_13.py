import os
os.system('cls')


texto = input("Introduce el texto: ").lower().split()

conteo = {}

for palabra in texto:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("------- CONTEO PALABRAS DE CONFIANZA XDD -------")

for palabra, cantidad in conteo.items():
    print(f"{palabra}: se repite {cantidad} veces")

