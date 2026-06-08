import os 
os.system ("cls") #Aprendi en un curso este import para limpiar la terminal cada que se ejecute el codigo

print("_BIENVENIDO A HASURA😁_\n")
print("Un juego donde nada es lo que parece👀")

print("Despiertas en el pueblo de Nitch🛖. No sabes como haz llegado ahí, el dia de ayer estuviste batallando con duendes y goblins")

primera_accion = input("Estas agotado😩. Pero necesitas averiguar que te paso, Que haces: LEVANTARSE O DORMIR.\n").lower().capitalize().strip()
if primera_accion == "levantarse" or primera_accion == "Levantarse":
    print("Decidiste levantarte y sales a ver donde estas. Hay mucha gente divirtiendose pero te encuentras con el dueño de la casa🤞\n")
    conversacion = input("Entras en panico, que decides hacer: HABLAR o HUIR\n").lower().capitalize().strip()
    if conversacion == "hablar" or conversacion == "Hablar":
        print("Decidiste hablar con el y te cuenta lo sucedido. Te cuenta que te encontro por ahí y decidio ayudarte😊.")
        print("👴Te parece un poco raro ya que sabes que el bosque es muy peligroso y el es un hombre mayor.")
        decision_1 = input("Que Haces ahora, CONFIAS o dices GRACIAS\n").lower().capitalize().strip()
        if decision_1 == "confias" or decision_1 == "Confias":
            print("❌Pesima opción, El anciano resulto ser un brujo y se gano tu confianza. A los días te asesino...\nGAME OVER❌")
        elif decision_1 == "gracias" or decision_1 == "Gracias":
            print("🙏 Le diste las gracias al anciano, y sigues tu camino.")
            
            print("Al salir de el pueblo de Nitch🛖, te adentras en el peligroso bosque")
            print("Tenias que descansar mas, y te empiezas a sentir cansado. Pero decides continuar")
            espada = input("Hay una extraña espada en el camino, Te parece raro. Que decides hacer: TOMAR, DEJARLA o LANZARLA\n").lower().capitalize().strip()
            if espada == "tomar" or espada == "Tomar":
                print("Un extraño poder abarca todo tu cuerpo, te sientes invencible por un momento, Aparece un joven buscando enemigos")
                print("Pero al ver tu cara, siendo poseido por la fuerza de la espada, decide ayudarte\n")
                print("Cuando logro quitarte la espada, te asustaste... pero el te explica lo sucedido")
                amigo = input("El joven quiere ser tu amigo, que decides hacer: AMISTAD o IRTE\n").lower().capitalize().strip()
                if amigo == "irte" or amigo == "Irte":
                    print("Decidiste irte, al tiempo el joven se junto con un grupo peligroso.")
                    print("Al verte despues que te ayudo, te ataco con su nuevo grupo...\nNo sobreviviste GAME OVER❌")
                elif amigo == "amistad" or amigo == "Amistad":
                    print("Conseguiste una nueva amistad!")
                    nombre = input("Te dice que su nombre es Carl, le dices tu nombre o no?: NOMBRE o IGNORAR\n").capitalize().lower().strip()
                    if nombre == "Nombre" or nombre == "nombre":
                        nombre = input("Cual es tu Nombre: ")
                        
                        print("Decidiste decirle tu nombre, Carl empieza a confiar en ti😅")
                        print(f"Carl y {nombre} deciden adentrarse mas en el bosque, y mas adelante escuchan a una niña gritar😦")
                        salvar = input(f"Carl y {nombre} se miran desconcertados🤨, que decides hacer?: AYUDAR o SEGUIR \n").capitalize().lower().strip()
                        if salvar == "Ayudar" or salvar == "ayudar":
                            
                            print(f"{nombre} y Carl deciden ir a ayudar a la niña, pero al poco tiempo se dan cuenta que es una trampa😠")
                            print(f"Carl al llegar le dice a {nombre}, preparate para pelear.⚔️")
                            print(f"Comienza la pelea de {nombre} y Carl contra el grupo de bandidos🥊.")
                            print(f"{nombre} se da cuenta que Carl es un mago 🧙‍♂️ , al igual que el pero el no sabe usar una espada como el.")
                            print(f"{nombre} y Carl duran poco tiempo ya que los dos son muy fuertes juntos🤼, Y logran hacerse victoriosos.")
                            print("Quieren dejar ir a la niña que ayudo a los bandidos, pero al estar dañada como los bandidos ataca a Carl con un cuchillo rapidamente.")
                            
                            
                            mariposa = input("Necesitas actuar rapido, que haces: SALVAR o DEJAR\n").capitalize().lower().strip()
                            if mariposa == "Dejar" or mariposa == "dejar":
                                print("Dejaste morir a Carl...")
                                
                                print("La niña se rie de ti por matar a tu compañero, te ataca pero tu la asesinas")
                                print("Triste por la muerte de Carl, matas a todo lo que se te cruce")
                                print("El rumor no tarda en llegar en todos los pueblos de lo peligroso que eres👹")
                                print(f"Te apodan {nombre} El Asesino.")
                                print("Eres el Malo de la historia. Gracias por jugar🦹")
                                
                                
                            elif mariposa == "Salvar" or mariposa == "salvar":
                                print("Salvaste a Carl.")
                                print(f"Carl te dice Gracias! {nombre} por salvarme pero que triste por esa niña al morir tan joven")
                                print(f"{nombre} y carl continuan su camino, y llegan a otro pueblo donde te reconocen, es tu pueblo natal!\n")
                                print("Sientes una voz a lo lejos, y es Caty, una amiga de la infancia\n")
                                print("Despues de esa llegada, todo cambio para ustedes... fueron el mejor equipo de la epoca.")
                                print("Incontables aventuras, y muchas victorias... Gracias por jugar! Fuiste feliz en tu historia!")
                                
                                
                            else: 
                                print("Respuesta incorrecta, intentelo de nuevo")
                        elif salvar == "Seguir" or salvar == "seguir":
                            print("Decidiste seguir con Carl.")
                            print("Caminando por el bosque, se encuentran con un templo muy extraño")
                            templo = input("Que quieres hacer: INVESTIGAR o IRTE\n").capitalize().upper().strip()
                            if templo == "INVESTIGAR" or templo == "Investigar":
                                print("Decides entrar con Carl al templo, de pronto se cierra la puerta principal.")
                                print("Se encienden las antorchas de el templo y aparece un Golem gigante.")
                                print(f"Carl y {nombre} se preparan para pelear, {nombre} intenta atacar con su espada, y Carl lo asiste con magía.")
                                print("Pasan varios minutos y Carl se esta quedando sin mana, se empieza a marear y el golem va hacia el")
                                print(f"{nombre} Esta a punto de perder a su compañero, y de la nada todo se le nubla")
                                print(f"Se escucha un grito desgarrador de {nombre}, de la nada vuelve en si y ve a el Golem destruido\n")
                                print(f"Y Carl esta asombrado porque vio a un ser poderoso que no parecia {nombre}")
                                print(f"{nombre} y Carl salen de el templo, descubriendo que {nombre} es un ser poderoso.")
                                print("Continuara.... Gracias por jugar.")
                            elif templo == "Irte" or templo == "IRTE":
                                print("Decidiste irte con carl y ignorar el templo.")
                                print("se hace de noche, deciden acampar y escuchan algo entre los arbustos")
                                arbustos = input("Que decides hacer: ALUMBRAR o IGNORAR").capitalize().upper().strip()
                                if arbustos == "ALUMBRAR" or arbustos == "Alumbrar":
                                    print("Sale de los arbustos una extraña criatura, resulta ser un pseudo hibrido entre Lobo y dragon de comodo")
                                    print("la criatura intenta escupir su saliva hacia ustedes, pero logran esquivar.")
                                    print("Los dos estan cansados por el extenso recorrido, pero la criatura es muy rapida uno tendra que morir")
                                    desenlace = input("Que decides hacer: SALVARTE o a CARL").capitalize().upper().strip()
                                    if desenlace == "CARL" or desenlace == "Carl":
                                        print("le dices a Carl que te abandone, que tu te encargas.")
                                        print("Carl se va confiando en ti... te quedas solo con la criatura")
                                        print("La criatura se avalanza hacia ti y logra morderte la pierna y la arranca")
                                        print("el veneno actua muy rapido y es tu fin... Carl regresa despues de buscar ayuda, y te encuentra tirado sin vida.")
                                        print("Final triste. Gracias por jugar")
                                    elif desenlace == "Salvarte" or desenlace == "SALVARTE":
                                        print("Abandonas a Carl, por culpa de el miedo y la culpa, sales corriendo pero no ves nada")
                                        print("En un instante tropezaste con unas ramas de arbol y caes por un barranco\n GAME OVER")
                                    else:
                                        print("Respuesta incorrecta, intentelo de nuevo")
                                elif arbustos == "IGNORAR" or arbustos == "Ignorar":
                                    print("Decidiste ignorar el sonido, se quedan a pasar la noche en el bosque")
                                    print("En media noche algo los ataca, y no saben que fue... no sobreviven\n GAME OVER")
                                else:
                                    print("Respuesta incorrecta, intentelo de nuevo")
                            else: 
                                print("Respuesta incorrecta, intentelo de nuevo")
                        else:
                            print("Respuesta incorrecta, intentelo de nuevo")
                    elif nombre == "Ignorar" or nombre == "ignorar":
                        print("Carl dice que no va a confiar en alguien, asi de prepotente, Te abandona.")
                        print("Al no tener a alguien que estuviera contigo en el bosque, Un Oso te ataco... pero estabas muy cansado")
                        print("El oso era muy Fuerte, Moriste por el Oso...\nGAME OVER❌")
                    else:
                        print("Respuesta incorrecta, intentelo de nuevo")
                else:
                    print("Respuesta incorrecta, intentelo de nuevo")
            elif espada == "Dejarla" or espada == "dejarla":
                print("Decidiste dejarla atras, continuas con tu aventura por el bosque")
                print("Ves muchas criaturas extrañas, y de pronto hueles algo extraño.")
                niebla = input("Te empieza a rodear una niebla extraña, con un olor extraño que haces?: CUBRIR o OLER\n").capitalize().upper().strip()
                if niebla == "OLER" or niebla == "Oler":
                    print("Decidiste Oler la niebla, te comienzas a sentir mareado... Era niebla venenosa\n GAME OVER❌")
                elif niebla == "Cubrir" or niebla == "CUBRIR":
                    print("Te cubriste a tiempo, una extraña figura se acerca hacia ti, Es un ninja🥷")
                    print("te dice: Que triste que esta sea tu forma de morir, me contrataron para que acabe contigo.")
                    ninja = input("Estas acorralado, no puedes quitar tus manos de tu rostro, pero el ninja viene hacia ti: PELEAR o RENDIRSE\n").capitalize().upper().strip()
                    if ninja == "PELEAR" or ninja == "Pelear":
                        print("No puedes hacer nada, Todo lo que intentes no resultara...\n GAME OVER❌")
                    elif ninja == "Rendirse" or ninja == "RENDIRSE":
                        print("No puedes hacer nada, Todo lo que intentes no resultara...\n GAME OVER❌")
                    else:
                        print("Respuesta incorrecta, intentelo de nuevo")
                else:
                    print("Respuesta incorrecta, intentelo de nuevo")
            elif espada == "Lanzarla" or espada == "lanzarla":
                print("Lanzaste la espada lejos, choca con una roca y se regresa hacia ti... GAME OVER❌")
            else: 
                print("Respuesta incorrecta, intentelo de nuevo")
        else:
            print("Respuesta incorrecta, intentelo de nuevo")
    elif conversacion == "Huir" or conversacion == "huir":
        print("Decidiste huir, pero cuando estabas corriendo recibiste un flechazo porque pensaban que eras peligroso...\nGAME OVER❌")
    else:
        print("Respuesta incorrecta, intentelo de nuevo")
elif primera_accion == "Dormir" or primera_accion == "dormir":
    print("Al quedarte dormido, atacaron el pueblo donde estabas, un grupo de bandidos irrumpio en esa casa...\nGAME OVER❌")
else:
    print("Respuesta incorrecta, intentelo de nuevo")
#EIVER VALENCIA