# ejercicio 1

"""distancia = int(input("Cuantos km de distancia tiene su paquete?:\n"))

if distancia <= 20:
    estado = input("Tiene Prime activo o es cliente estandar?: ").strip().capitalize()
    if estado == "Prime":
        print("Cuenta con envio rápido, pronto llegara su paquete")
    else:
        print("Su suscripcion es Estandar tardara mas en llegar su paquete.")
else:
    print("En este momento no podemos atenderle.")"""


#ejercicio 2

"""usuario = input("Que tipo de usuario es?: ").strip().lower()

if usuario == "admin":
    contraseña = int(input("Contraseña: "))
    if contraseña == 12345:
        print("logueado correctamente.")
    else:
        print("CONTRASEÑA INCORRECTA.")
else:
    print("Usuario común no tiene permitido el acceso.")"""


#ejercicio 3
"""nota_1 = float(input("Primera nota para aplicar: "))
nota_2 = float(input("Segunda nota: "))
nota_3 = float(input("tercera nota: "))
nota_4 = float(input("Ultima nota: "))

promedio = nota_1 + nota_2 + nota_3 + nota_4 / 4

if promedio  >= 8.5:
    ingreso_familiar = int(input("Cual es su ingreso familiar: "))
    if ingreso_familiar < 1500:
        print("Aplica para la beca")
    else:
        print("No aplica para la beca")
else:
    print("Notas muy bajas, no aplica")"""


#ejercicio 4
"""
edad = int(input("Que edad tienes: "))

if edad < 12:
    print("50% De descuento")
elif edad >= 12 and edad <= 30:
    estudiante = input("Eres estudiante?: ").strip().capitalize()
    if estudiante == "Si":
        print("30% De descuento")
    elif estudiante == "No":
        vip = input("Eres vip?: ").strip().upper()
        if vip == "SI":
            print("10% De descuento")
        else:
            print("No tiene descuento.")
    else:
        print("RESPONDA SI O NO")
else:
    print("Su edad no aplica a descuento.")"""


#ejercicio 5
"""
salario = int(input("¿Cual es el monto de su salario?: "))

if salario > 1000:
    puntaje_credito = int(input("¿Cual es su puntaje de credito?: "))
    if puntaje_credito >600:
        deudas = input("¿Tiene deudas?: ").strip().capitalize()
        if deudas == "No":
            print("Prestamo autorizado.")
        else:
            print("Con deudas no aplica para el prestamo")
    else:
        print("Puntaje de credito bajo")
else:
    print("Su salario no aplica para un prestamo.")"""


#ejercicio 6
"""
destino = input("El destino de el paquete es Nacional o Internacional: ").strip().capitalize()

if destino == "Nacional":
    peso = int(input("Cuantos KG tiene el paquete?: "))
    if peso > 5:
        print("Su paquete tendra cobro extra.")
    else:
        print("Paquete ligero no se le cobrara extra")
elif destino == "Internacional":
    continente = input("Hacia cual continente ira el paquete: Asia/Europa\n").strip().capitalize()
    if continente == "Europa":
        print("La tarifa de su paquete es de 150$")
    elif continente == "Asia":
        print("La tarifa de su paquete es 100$")
    else:
        print("No tenemos disponibilidad para ese contienente")
else:
    print("ERROR respuesta incorrecta")"""


#ejercicio 7
"""
evaluacion = input("Lograste cumplir metas?: ").strip().capitalize()

if evaluacion == "Si":
    puntualidad = int(input("Cuanto % De puntualidad tuviste: "))
    if puntualidad  > 90:
        print("Obtuviste un BONO!")
    else:
        print("Tu puntualidad no aplica para el Bono")
elif evaluacion == "No":
    asistencia = input("Asistio a capacitaciones?: ").strip().upper()
    if asistencia == "SI":
        print("Entro para el sorteo de un Bono")
    else:
        print("El año siguiente ira mejor!")
else:
    print("Responda correctamente solo SI o NO")
"""


#ejercio 8
"""
triangulo = int(input("Cuantos lados tiene su triangulo: "))

if triangulo == 3:
    cm = int(input("Cm de el primer lado: "))
    cm_2 = int(input("Cm de el segundo lado: "))
    cm_3 = int(input("Cm de el tercer lado: "))
    if cm == cm_2 and cm_2 == cm_3:
        print("Su triangulo es un equilátero")
    elif cm == cm_2 and cm_2 != cm_3 or cm_2 == cm_3 and cm != cm_3 or cm_2 != cm and cm == cm_3:
        print("Su triangulo es un isósceles")
    elif cm != cm_2 and cm_2 != cm_3 and cm != cm_3:
        print("Su triangulo es un escaleno.")
    else:
        print("Error")
else:
    print("No es un triangulo")"""

#ejercicio 9
"""
ingreso = int((input("De cuanto es su ingreso: 20/50k o mayor a 50k\n")))

if ingreso >= 20 and ingreso < 50 or ingreso >= 20000 and ingreso < 50000:
    dependientes = int(input("Cuantos dependientes tienes?: "))
    if dependientes == 0:
        print("No tiene carga")                                                     ### Como no especifico si aqui habia que tambien reducir el impuesto lo hice por carga
    elif dependientes == 1 or dependientes == 2:                                     # me hizo investigar mucho porque nunca me dieron esto 
        print("Carga media de dependientes")                                        ### me estoy esforzando mucho, la verdad me esta ayudando mucho a analizar y solucionar los problemas   
    elif dependientes >= 3:
        print("Carga maxima de dependientes")
elif ingreso >= 50 or ingreso >= 50000:
    impuesto = 995.34
    estado_civil = input("Estado civil?: ").capitalize().lower().upper()
    if estado_civil == "Casado" or estado_civil == "CASADO" or estado_civil == "casado":
        pregunta_dependientes = int(input("Cuantos dependientes tienes?: "))
        if pregunta_dependientes == 0:
            tasa_reducida = 430 + 430 - impuesto
            print(f"Su tasa reducida por casamiento sin dependientes es {tasa_reducida} de {impuesto} de impuesto total monto a pagar 135.34")
        elif pregunta_dependientes == 1:
            tasa_reducida = 430 + 430 + 430 - impuesto
            print(f"Su tasa reducida por casamiento con 1 dependientes es {tasa_reducida} de {impuesto} de impuesto total acumula 294.65 para el estado")
        elif pregunta_dependientes == 2:
            tasa_reducida = 430 + 430 + 430 + 430 - impuesto
            print(f"Su tasa reducida por casamiento con 2 dependientes es {tasa_reducida} de {impuesto} de impuesto total acumula 724.66 para el estado")
        elif pregunta_dependientes == 3:
            tasa_reducida = 430 + 430 + 430 + 430 + 430 - impuesto
            print(f"Su tasa reducida por casamiento con 3 dependientes es {tasa_reducida} de {impuesto} de impuesto total acumula 1154.65 para el estado")
        else:
            print("Su impuesto esta completamente pagado, la reduccion se aplico")
    elif estado_civil == "Viudo" or estado_civil == "VIUDO" or estado_civil == "viudo":
        pregunta_dependientes = int(input("Cuantos dependientes tienes?: "))
        if pregunta_dependientes == 0:
            tasa_reducida = 430 - impuesto
            print(f"Su tasa reducida  sin dependientes es {tasa_reducida} de {impuesto} de impuesto total monto a pagar 565.34")
        elif pregunta_dependientes == 1:
            tasa_reducida = 430 + 430 - impuesto
            print(f"Su tasa reducida con 1 dependientes es {tasa_reducida} de {impuesto} de impuesto total monto a pagar 135.34")
        elif pregunta_dependientes == 2:
            tasa_reducida = 430 + 430 + 430 - impuesto
            print(f"Su tasa reducida con 2 dependientes es {tasa_reducida} de {impuesto} de impuesto total acumula 294.65 para el estado")
        elif pregunta_dependientes == 3:
            tasa_reducida = 430 + 430 + 430 + 430 - impuesto
            print(f"Su tasa reducida con 3 dependientes es {tasa_reducida} de {impuesto} de impuesto total acumula 724.66 para el estado")
        else:
            print("Su impuesto esta completamente pagado, la reduccion se aplico")
    elif estado_civil == "Soltero" or estado_civil == "SOLTERO" or estado_civil == "soltero":
        pregunta_dependientes = int(input("Cuantos dependientes tienes?: "))
        if pregunta_dependientes == 0:
            tasa_reducida = 430 - impuesto
            print(f"Su tasa reducida  sin dependientes es {tasa_reducida} de {impuesto} de impuesto total monto a pagar 565.34")
        elif pregunta_dependientes == 1:
            tasa_reducida = 430 + 430 - impuesto
            print(f"Su tasa reducida con 1 dependientes es {tasa_reducida} de {impuesto} de impuesto total monto a pagar 135.34")
        elif pregunta_dependientes == 2:
            tasa_reducida = 430 + 430 + 430 - impuesto
            print(f"Su tasa reducida con 2 dependientes es {tasa_reducida} de {impuesto} de impuesto total acumula 294.65 para el estado")
        elif pregunta_dependientes == 3:
            tasa_reducida = 430 + 430 + 430 + 430 - impuesto
            print(f"Su tasa reducida con 3 dependientes es {tasa_reducida} de {impuesto} de impuesto total acumula 724.66 para el estado")
        else:
            print("Su impuesto esta completamente pagado, la reduccion se aplico")
    else:
        print("Responda entre estas opciones CASADO/VIUDO O SOLTERO")"""


#ejercicio 10 

estado = input("Ataque O Defensa:\n").capitalize().lower().upper()

if estado == "Ataque" or estado == "ATAQUE" or estado == "ataque":
    pregunta_enemigos = input("Hay un Duende con escudo y Un Goblin Mago, Quieres Pelear con tu magia o Con tu espada?:\n").lower().upper().capitalize()
    if pregunta_enemigos == "Espada" or pregunta_enemigos == "espada" or pregunta_enemigos == "ESPADA":
        combate_1 = input("Aparecio un duende misterioso con un gran escudo. Quieres atacarlo?:\n").lower().capitalize().upper()
        if combate_1 == "SI" or combate_1 == "si" or combate_1 == "Si":
            ataque_1 = input("Haz atacado pero el duende se a cubierto, quieres seguir atacando o te escudas?: Si ataco/Me escudo\n").lower().capitalize().upper()
            if ataque_1 == "si ataco" or ataque_1 == "Si ataco" or ataque_1 == "SI ATACO":
                ataque_2 = "tu ataque fue fulminante, Acabaste con el duende"
                print(ataque_2, "FELICIDADES")
            elif ataque_1 == "Me escudo" or ataque_1 == "me escudo" or ataque_1 == "ME ESCUDO":
                game_over = "Game over el duende encontro la manera de atacarte y daño un punto vital, muerte instantánea"
                print(game_over, "Suerte la proxima")
        elif combate_1 == "No" or combate_1 == "NO" or combate_1 == "no":
            duende = input("El duende te ataco rapidamente, pero fallo... Debes atacar ya o vas a morir, Atacas?: Si/No\n").lower().capitalize().upper()
            if duende == "No" or duende == "NO" or duende == "no":
                print("Game over")
            else:
                print("Felicidades te salvaste por poco, regresas a tu casa")
        else:
            print("Tardaste demasiado, llegaron refuerzos para el duende y acabaron contigo")
    elif pregunta_enemigos == "Magia" or pregunta_enemigos == "magia" or pregunta_enemigos == "MAGIA":
        combate_2 = input("Decidiste usar tu magia contra el Goblin, Que hechizo quieres hacer?: Bola de fuego o Avada kedavra :D\n").lower().capitalize().upper()
        if combate_2 == "Bola de fuego" or combate_2 == "BOLA DE FUEGO" or combate_2 == "bola de fuego":
            esquive = input("El goblin esquivo tu ataque, y te lanza una roca gigante... que vas a hacer?: Romper la roca/Lanzar otra bola de fuego\n").lower().capitalize().upper()
            if esquive == "Romper la roca" or esquive == "romper la roca" or esquive == "ROMPER LA ROCA":
                game_over = "La roca te cayo encima, GAME OVER"
                print(game_over)
            elif esquive == "Lanzar otra bola de fuego" or esquive == "LANZAR OTRA BOLA DE FUEGO" or esquive == "lanzar otra bola de fuego":
                game_over = "Le diste al goblin mago pero no murio, y la roca te cayo encima... GAME OVER"
                print(game_over)
            else:
                print("No hiciste nada y la roca te cayo encima... GAME OVER")
        elif combate_2 == "avada kedavra" or combate_2 == "Avada kedavra" or combate_2 == "AVADA KEDAVRA":
            ataque_1 = input("Fallaste el ataque, pero el goblin tuvo mucho miedo... quieres volverlo a intentar?: Si/No\n").lower().capitalize().upper()
            if ataque_1 == "Si" or ataque_1 == "SI" or ataque_1 == "si":
                print("El duende murio instantaneamente, Bien hecho!, !Viva Harry Potter!")
            elif ataque_1 == "No" or ataque_1 == "NO" or ataque_1 == "no":
                print("GAME OVER por miedoso, sangre sucia.")
            else:
                print("Muy lento el goblin volvio a atacar y te mato")
        else:
            print("el goblin lanzo el avada kedavra y te mato")
    else:
        print("Viste a los dos enemigos y te orinaste encima, GAME OVER por humillacion")
elif estado == "Defensa" or estado == "DEFENSA" or estado == "defensa":
    combate = input("Ahora tendras que pelear con los dos enemigos, que vas a hacer: Seguir escudandote/Intentar atacar\n").lower().capitalize().upper()
    if combate == "Seguir escudandote" or combate == "SEGUIR ESCUDANDOTE" or combate == "seguir escudandote":
        escudo_1 = input("Decides escudarte pero los enemigos son muy fuertes y te rompen el escudo... Que vas a hacer: Correr/Atacar\n").lower().capitalize().upper()
        if escudo_1 == "Correr" or escudo_1 == "CORRER" or escudo_1 == "correr":
            print("Te estan golpeando intentas escapar pero llegan mas refuerzos... GAME OVER")
        elif escudo_1 == "Atacar" or escudo_1 == "ATACAR" or escudo_1 == "atacar":
            print("Intentaste defenderte, acabaste con el primer enemigo... pero ya es tarde para ti, GAME OVER")
        else:
            print("No hiciste nada, y acabaron contigo... GAME OVER")
    elif combate == "INTENTAR ATACAR" or combate == "Intentar atacar" or combate == "intentar atacar":
        print("Intentaste defenderte, intentaste de todo... quedaste inconciente pero estas a salvo. . . ¿QUE PASO?")  # Parte 2?
    else:
        print("Quedaste paralizado y... moriste GAME OVER")
else:
    print("¿QUE HACES? Ataca!... GAME OVER")