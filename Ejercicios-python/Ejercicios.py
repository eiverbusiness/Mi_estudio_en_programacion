import os

os.system("cls")


for n in range(1, 101):
    print(f"Numero: {n}")

for n in range(1, 11):
    print(f"{n} x 12 = {n*12}")

#Bucle While

n = 1
while n <= 10:
    print(f"{n} x 20 = {n*20}")
    n += 1

#EJERCICIOS EIVER

print("___Buscador de numeros pares___")

n = int(input("Introduce el numero positivo: "))


if n <= 0:
    print("Numero negativo, fin de el programa")
elif n > 0 :
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(f"El numero par de {n}: {i}")



#ejercicio 2
aprobadas = 0
reprobadas = 0
while True:
    notas = int(input("Ingrese las notas de el alumno: "))
    if notas == -1:
        break
    
    if notas >= 60:
        aprobadas  += 1
        
        
    elif notas >= 0:
        reprobadas += 1
        
    else:
        print("Numero invalido, el valor debe ser positivo")
    

print("Notas finales")
print(f"Las notas aprobadas: {aprobadas}")
print(f"Notas reprobadas: {reprobadas}")



#ejercicio 3

while True:
    entero = int(input("Ingrese el numero entero:"))
    if entero < 0:
        print("El numero debe ser positivo intente de nuevo.")
        continue
    resultado = 1
    for i in range(1, entero + 1):
        
        resultado *= i
        print(f"El factorial de {entero} es: {resultado}")
    break

#ejercicio 4

boton_Programa = True
while boton_Programa:
    for intento in range(1, 4):
            usuario = input("Ingrese su usuario: ").lower().strip()
            contraseña = input("Ingrese la contraseña: ").lower().strip()
            if usuario == "admin" and contraseña == "secret123":
                print("Inicio de sesion exitoso")
                boton_Programa = False
                break
            else:
                intentos = 3 - intento
                if intentos > 0:
                    print(f"Usuario o Contraseña incorrecta te quedan {intentos} intentos.")
                else:
                    print("Usuario bloqueado.")
                    boton_Programa = False
                    
print("Programa finalizado")

#ejercicio 5
boton_menu = True

lista = []
suma_total = 0

while boton_menu:
    
    print("\n_Gestion de numeros con filtrado dinamico_")
    print("\n1) ingresar numero a la lista.")
    print("2) mostrar la suma de los numeros ingresados")
    print("3) numeros multipos de 3 y 4")
    print("4) Finalizar programa")
    
    usuario = input("Elije una opcion: ")
    
    
    
    if usuario == "1":
        numero = int(input("Ingrese el numero a la lista: "))
        lista.append(numero)
        print(f"el {numero} se introdujo correctamente a la lista")
        
    elif usuario == "2":
        
        suma_total = 0
        for n in lista:
            suma_total += n
        print(f"La suma de los numeros ingresados es: {suma_total}")
    elif usuario == "3":
        multiplos_3 = []
        multiplos_4 = []
        for n in lista:
            if n % 3 == 0:
                multiplos_3.append(n)
                
            if n % 4 == 0:
                multiplos_4.append(n)
        print(f"mutiplos de 3 son: {multiplos_3}")
        print(f"multiplos de 4 son: {multiplos_4}")
    elif usuario == "4":
        print("Finalizando el programa.")
        boton_menu = False
    else:
        print("Opcion invalida, revise las opciones.")




