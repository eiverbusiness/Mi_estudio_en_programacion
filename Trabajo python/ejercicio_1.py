import os
os.system('cls')

numero = int(input("Elije un numero: "))

if numero % 2 == 0:
    print(f"El {numero} es par")
else:
    print(f"El {numero} es impar")
