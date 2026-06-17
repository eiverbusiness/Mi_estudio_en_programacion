import os
os.system('cls')


texto = input("Introduce el texto: ").lower()
contador = 0

vocales = "aeiou"

for letra in texto:
    if letra in vocales:
        contador += 1

print(f"Tu texto tiene {contador} vocales")