import os
os.system('cls')

print("-_-_-VERIFICADOR DE NUMEROS PRIMOS-_-_-")

def es_primo(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        
        if n % i == 0:
            return False
    return True


numero = int(input('Numero: '))
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} No es primo")