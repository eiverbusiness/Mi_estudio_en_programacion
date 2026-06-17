import os
os.system('cls')

n = int(input("Cuanto de fibonacci deseas mostrar: "))

fibonacci = []
a, b = 0, 1
contador = 0

while contador < n:
    fibonacci.append(a)

    a, b = b, a + b

    contador += 1

print("\nFibonacci generado:")
print(fibonacci)