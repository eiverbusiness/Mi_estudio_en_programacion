import os
os.system('cls')


diccionario_notas = {
    "Eiver" : 20,
    "Eliana" : 20,
    "Moises" : 17,
    "Andres" : 17,
    "Juanito" : 9
    }

suma = 0
aprobados = 0

for nota in diccionario_notas.values():
    suma += nota

    if nota >= 10:
        aprobados += 1

promedio = suma / len(diccionario_notas)

print(f"El promedio general es: {promedio}")
print(f"aprobaron: {aprobados}")