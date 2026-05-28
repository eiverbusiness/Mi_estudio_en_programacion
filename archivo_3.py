num_usuario = int(input("Ingrese el numero entero:\n"))

if num_usuario >= 10 and num_usuario <= 50:
    print("el numero es valido")
else:
    print("el numero no es valido")


#Ejercicio 2

nivel_seguridad = int(input("Cual es su nivel de seguridad: "))
estado_activo = (input("Su estado es activo: True/False ")).strip().lower() == "true"
codigo_emergencia = (input("cuenta usted con el codigo de emergencia: True/False ")).strip().lower() == "true"

if (nivel_seguridad > 5 and estado_activo == True):
    print("acceso concedido")
elif codigo_emergencia == True:
    print("Tiene acceso por tener el codigo de emergencia")
elif nivel_seguridad > 5 and estado_activo == False:
    print("Acceso denegado por su inactividad")
elif nivel_seguridad < 5 and estado_activo == False:
    print("No cumple con el nivel, y su estado es inactivo")
elif codigo_emergencia == False:
    print("no tiene codigo de emergencia")    
else:
    print("acceso denegado")    

#ejercicio 3 

invitacion = input("Que tipo de invitacion posee?").strip().lower()

if invitacion == "vip":
    edad = int(input("que edad tienes: "))
    if edad >= 18:
        codigo_de_seguridad = int(input("dime el codigo de seguridad: "))
        if codigo_de_seguridad == 777:
            print("Acceso total concedido")
else:
    print("No tiene invitacion autorizada")


# ejercicio 4

nivel_estudio = input("Cual es su nivel de estudio: ").strip().lower()
if nivel_estudio == "universitario":
    años = float(input("cuantos años de experiencia tienes: "))
    if años >= 2.5:
        certificacion = input("tienes certificacion tècnica?: ").strip().lower()
        if certificacion == "si":
            puntaje_prueba = int(input("que puntaje de prueba obtuviste: "))
            if puntaje_prueba >= 80 and puntaje_prueba <= 100:
                print("Estas en revision")
            else:
                print("tu puntaje es muy bajo")
        else:
            print("no tienes certificacion")
    else:
        print("no cumples con los añosde experiencia")
else:
    print("tus estudios academicos no son los requeridos")

#ejercicio 5


estatus = input("que estatus tienes en nuestro establecimiento?: ").strip().lower()

if estatus == "socio":
    dia = input("que dia de la semana es?: ").strip().lower()
    if dia == "martes" or dia == "jueves":
        pago = input("metodo de pago: ").strip().lower()
        if pago == "tarjeta":
            monto = int(input("monto de la compra: "))
            if monto > 500:
                descuento = 500 * 0.80
                print(f"su {monto} con el descuento del 20% es {descuento}")
            else:
                print("su monto no posee descuento")
        else:
            print("Forma de pago no aceptada")
    else:
        print("el dia de la semana no cumple con descuento")
else: 
    print("No cuenta con descuento")

#ejercicio 6

problema = input("el equipo enciende: ").strip().lower()

if problema == "no":
    pregunta1 = input("el cable de poder esta conectado?: ").strip().lower()
    if pregunta1 == "si":
        pregunta2 = input("el enchufe cuenta con electricidad?: ").strip().lower()
        if pregunta2 == "si":
            pregunta3 = input("La fuente hace ruido o gira el ventilador?: ").strip().lower()
            if pregunta3 == "no":
                pregunta4 = input("Emite algún pitido al intentar encender?: ").strip().lower()
                if pregunta4 == "no":
                    print("la fuente esta averiada")
                else:
                    print("No podemos ayudarte")
            else:
                print("el problema puede ser ese")
        else:
            print("espera que llegue la electricidad")
    else:
        print("conecte el cable porfavor")
else:
    print("entonces no requiere nuestros servicios muchas gracias.")


