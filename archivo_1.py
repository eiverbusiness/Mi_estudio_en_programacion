import os

os.system("cls")

"""
for n in range(1, 101):
    print(f"Numero: {n}")

for n in range(1, 11):
    print(f"{n} x 12 = {n*12}")

#Bucle While

n = 1
while n <= 10:
    print(f"{n} x 20 = {n*20}")
    n += 1
   

"""
#EJERCICIOS EIVER
"""
print("___Buscador de numeros pares___")

n = int(input("Introduce el numero positivo: "))


if n <= 0:
    print("Numero negativo, fin de el programa")
elif n > 0 :
    for n in range(1, n):
       resultado = int(n % 2 == 0  )
       print(f"El numero par de {n}: {resultado}")"""
       
        
        

  
    
       


#ejercicio 2

notas = int(input("Ingrese las notas de el alumno: "))

while notas:
    if notas >= 60:
        notas += 1
        print(f"Notas aprobadas {notas}")
        
    elif notas < 60:
        notas += 1
        print(f"Notas reprobadas {notas}")
    break
notas == -1


#Mala gestion de mi parte muy poco tiempo para procesarla



    

