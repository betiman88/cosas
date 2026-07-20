def jugar():
    # Estado de la habitación
    puerta_descubierta = False
    llave = False
    salir_habitacion = False
    inventario=[]

    def menu(texto):
        print(texto)
        return input("\nEscribe una opción: ").lower()

    print("""
    Despiertas mareado y a oscuras.

    Un nauseabundo olor te rodea.
    Escuchas cómo un goteo incesante de un líquido maloliente y espeso cae al suelo.

    Te duele la cabeza y no recuerdas nada.

    Un pensamiento te recorre el cerebro como un cuchillo...

    ¿Quién eres?
    """)

    protagonista = False

    while not protagonista:

        nombre = input("Escribe tu nombre: ")

        confirmar_nombre = input(
            "¿Estás seguro de que te llamas así? (S/N): "
        ).upper()

        if confirmar_nombre == "S":

            print(f"\n{nombre}... Así es como te llamaban.")

            protagonista = True

        else:

            print("\nNo... Ese nombre no termina de convencerte.\n")





    while not salir_habitacion:

        if puerta_descubierta and llave:

            opcion = menu("""
    ¿Qué quieres hacer?

    1 - Examinar la puerta.
    2 - Investigar a ciegas tu alrededor.
    3 - Sumergirte en tus terribles pensamientos.
    4 - Intentar beber del líquido espeso.
    5 - Usar la llave en la cerradura.
    6 - Ver inventario.
    """)

        elif puerta_descubierta:

            opcion = menu("""
    ¿Qué quieres hacer?

    1 - Examinar la puerta.
    2 - Investigar a ciegas tu alrededor.
    3 - Sumergirte en tus terribles pensamientos.
    4 - Intentar beber del líquido espeso.
    6 - Ver inventario.
    """)

        else:

            opcion = menu("""
    ¿Qué quieres hacer?

    1 - Ir hacia la luz.
    2 - Investigar a ciegas tu alrededor.
    3 - Sumergirte en tus terribles pensamientos.
    4 - Intentar beber del líquido espeso.
    6 - Ver inventario.
    """)

        if opcion == "1":

            if not puerta_descubierta:

                print("""
    Te acercas lentamente hacia la luz.

    Descubres que la luz procede de un pequeño piloto rojo situado sobre una pesada puerta metálica.
    """)

                puerta_descubierta = True

            else:

                print("""
    La puerta parece muy resistente.

    Está cerrada con una vieja cerradura.
    """)

        elif opcion == "2":

            if not llave:

                print("""
    Palpas el suelo con cuidado.

    Tus manos encuentran varios objetos.

    Entre la suciedad y las inquietantes formas encuentras algo con forma de llave.
    """)

                print("Obtienes una llave oxidada.")

                llave = True
                inventario.append("Llave oxidada")

            else:

                print("""
    Vuelves a registrar el suelo.

    No encuentras nada más de utilidad.
    """)

        elif opcion == "3":

            print("""
    Intentas recordar qué hacías antes de despertar aquí.

    Solo consigues un intenso dolor de cabeza.

    Un profundo pesar te embarga y empiezas a llorar.
    """)

        elif opcion == "4":

            print("""
    Acercas la mano al líquido.

    El hedor es insoportable.

    Cuando tus dedos lo rozan, comprendes que jamás deberías llevártelo a la boca.
    """)

        elif opcion == "5" and puerta_descubierta and llave:

            print("""
    Introduces la llave en la cerradura.

    Con un fuerte chasquido...

    La cerradura gira lentamente.
    """)

            salir_habitacion = True

        elif opcion == "6":

            print("\n===== INVENTARIO =====\n")

            if len(inventario) == 0:
                print("No llevas ningún objeto.")

            else:
                for objeto in inventario:
                    print("-", objeto)

        else:

            print("\nNo puedes hacer eso.\n")

    print("""
    La pesada puerta cede.

    Un chirrido metálico taladra tu cerebro.

    Una luz parpadeante te golpea de lleno en la cara.
    """)

    print("""
    Te encuentras en un pasillo blanco y totalmente aséptico.

    Contrasta sobremanera con la última estáncia, pestilente y sucia.

    Ante ti hay un estrecho pasillo que rodea toda la estáncia.

    En medio hay una pesada puerta blanca.

    Sobre ella, encajado en la pared, un gigantesco ojo orgánico sigue cada uno de tus movimientos.

    Jamás deja de observarte.

    Junto a la puerta hay una pequeña estántería con varios objetos.
    """)

    # ==========================
    # Estado de la escena 2
    # ==========================

    ojo_examinado = False
    estánteria_registrada = False
    criatura_descubierta = False
    criatura_ayudada = False
    cinta_escuchada = False
    puerta_abierta = False

    while not puerta_abierta:

        print("""
    ¿Qué quieres hacer?

    1 - Investigar el ojo gigante.
    2 - Investigar la estántería.
    3 - Recorrer el pasillo.
    4 - Golpear la puerta.
    """)

        if estánteria_registrada:
            print("5 - Escuchar el walkman.")
            print("6 - Examinar el ojo de cristal.")
            print("7 - Apuñalar ojo gigante")
            if criatura_descubierta:
                print("8 - Apuñalar criatura ")


        if criatura_descubierta and cinta_escuchada:
            print("9 - Dar el ojo de cristal a la criatura.")

        if criatura_ayudada:
            print("10 - Tapar el ojo gigante.")

        print("11 - Ver inventario.")

        opcion = input("\nEscribe una opción: ").lower()

        if opcion == "1":

            if not ojo_examinado:

                print("""
    Un inquietante ojo escudriña tu presencia.

    Cada uno de tus movimientos es seguido con una rapidez imposible.

    Su aterradora pupila se clava en ti como un puñal.

    Jamás parpadea.
    """)

                ojo_examinado = True

            else:

                print("""
    El ojo continúa siguiéndote.

    No ha apartado la mirada de ti ni un solo instante.
    """)

        elif opcion == "2":

            if not estánteria_registrada:

                print("""
    Encuentras varios objetos que no parecen guardar relación entre sí.

    • Un cuchillo.

    • Un walkman con una vieja cinta.

    • Un ojo de cristal.
    """)

                print("""
    Obtienes:

    - Cuchillo
    - Walkman
    - Ojo de cristal
    """)

                inventario.append("Cuchillo")
                inventario.append("Walkman")
                inventario.append("Ojo de cristal")

                estánteria_registrada = True

            else:

                print("""
    La estántería está completamente vacía.
    """)

        elif opcion == "3":

            if not criatura_descubierta:

                print("""
    Comienzas a recorrer el pasillo.

    Tras varios metros descubres algo imposible.

    El pasillo forma un círculo perfecto.

    Siempre acabas regresando frente al mismo ojo.

    Mientras intentas comprender lo ocurrido...

    Una pequeña criatura aparece detrás de ti.

    Una masa amorfa de carne intenta llamar tu atención.

    Decenas de ojos y dientes se agitan por toda su superficie.

    No parece agresiva.

    Solo permanece inmóvil observándote.
    """)

                criatura_descubierta = True

            else:

                print("""
    La criatura continúa allí.

    Permanece inmóvil.

    Parece esperar algo de ti.
    """)

        elif opcion == "4":

            print("""
    Golpeas la puerta con todas tus fuerzas.

    No se mueve ni un milímetro.

    El gigantesco ojo entorna su inexistente párpado.

    Te mira.

    Parece enfadado.
    """)

        elif opcion == "5":

            if estánteria_registrada:

                print("""
    Introduces la vieja cinta en el walkman.

    Tras unos segundos de ruido blanco...

    "CONCÉDENOS OJOS..."

    "CONCÉDENOS OJOS..."

    La voz deja de sonar.
    """)

                cinta_escuchada = True

            else:

                print("No tienes ningún walkman.")

        elif opcion == "6":

            if estánteria_registrada:

                print("""
    Es un ojo de cristal sorprendentemente realista.

    Tiene un iris grisáceo.

    Por alguna extraña razón, tienes la sensación de que pertenece a alguien.
    """)

            else:

                print("No tienes ningún ojo de cristal.")

        elif opcion == "7":

            print("""
    Saltas hasta la altura del gran ojo.

    El cuchillo rasga la infernal esclerótica del repugnante ojo.

    Un asqueroso líquido parecido a sangre coagulada empieza a brotar de la pupila,

    bañándote completamente el cuerpo mientras va deshaciendo tu carne y tus huesos.

    Sientes como cada célula de tu cuerpo grita en una infinita agonía.

    Tu cerebro se para y tu último pensamiento no es más que una mancha roja informe

    que te observa y comprendes que nunca debiste tener ojos.

    ========== GAME OVER ==========
    """)
            return

            
        elif opcion == "8":

            print("""
    Cortas la resbaladiza masa informe.

    Acabas con la vida de la desgraciada criatura, que expira en un agónico grito final.

    Suena como un llanto infantil.

    Durante unos segundos permaneces inmóvil, incapaz de apartar la vista de su cuerpo.

    Una insoportable sensación de culpa comienza a devorarte por dentro.

    Comprendes que aquella criatura nunca quiso hacerte daño.

    Solo necesitaba tu ayuda.

    Sientes una repugnancia absoluta hacia ti mismo.

    El cuchillo, aún goteando sangre, permanece en tu mano.

    Sin apenas darte cuenta, la hoja apunta ahora hacia tu cuello.

    No encuentras ninguna razón para seguir viviendo.

    Con un movimiento seco, deslizas el filo sobre tu yugular.

    La sangre brota a borbotones.

    Tus piernas dejan de sostenerte.

    Mientras la oscuridad lo invade todo, el último sonido que escuchas es aquel llanto infantil...

    ========== GAME OVER ==========

    """)

            respuesta = input("¿Quieres volver a empezar? (S/N): ").upper()

            if respuesta == "S":

                return

            else:

                print("Gracias por jugar.")
                exit()

        elif opcion == "9":
            if not criatura_ayudada:
                print ("""Le ofreces amigablemente el ojo de cristal a la criatura.

                   Lo engulle esbozando lo que parece una siniestra sonrisa en sus multiples bocas

                   Uno de sus seudopodos toma forma de un pequeño brazo.

                   Te ofrece una parte de si mismo.

                   Es una membrana redondeada de esa asquerosa carne
                   """)      
                criatura_ayudada=True
                inventario.append("membrana translúcida")

            else: 
                print("La criatura no tiene nada mas que ofrecerte")

        elif opcion=="10":
            if criatura_ayudada:
                print("""Te das cuenta que la extraña membrana tiene forma de ojo.

                  Alzas tus brazos mientras escuchas un desagradable ruido de la membrana moviendose.

                  Consigues encajar la membrana en el ojo gigante a modo de párpado.

                  Por fin el ojo se cierra y dejas de sentir esa sensacion escudriñadora.

                  La puerta esta abierta. Sientes el frio y la soledad del exterior

                  """)
                inventario.remove("membrana translúcida")
                puerta_abierta=True

        elif opcion == "11":

            print("\n===== INVENTARIO =====\n")

            if len(inventario) == 0:

                print("No llevas ningún objeto.")

            else:

                for objeto in inventario:
                    print("-", objeto)

        else:

            print("\nNo puedes hacer eso.\n")



    ### ESCENA 3 : EL PATIO

    print("""
    La puerta se cierra tras de ti con un estruendo metálico.

    Por primera vez desde que despertaste...

    Respiras aire fresco.

    O al menos eso crees.

    Una espesa niebla cubre un inmenso patio pavimentado solo con hormigón.

    Las paredes son demasiado altas para distinguir qué hay al otro lado.

    Parecen los muros de una prisión.

    No hay pájaros.

    No hay viento.

    No hay sonido alguno.

    Solo un leve rasgar de piedra.

    Al girarte descubres su origen.

    Un hombre demacrado y delgado hasta parecer enfermo escribe una y otra vez sobre el muro.

    "CONSUMIR CORAZÓN"

    "CONSUMIR CORAZÓN"

    "CONSUMIR CORAZÓN"
    """)

    orientacion = False
    brujula_obtenida = False
    while not orientacion:

        print("""
    ¿Qué quieres hacer?

    1 - Hablar con el hombre.
    2 - Examinar el patio.
    3 - Caminar hacia el este.
    4 - Caminar hacia el oeste.
    5 - Caminar hacia el norte.
    6 - Caminar hacia el sur.
    7 - Ver inventario.
    """)

        if brujula_obtenida:
            print("8 - Examinar brújula.")

        opcion = input("¿Qué quieres hacer? ")

        if opcion == "1":

            if not brujula_obtenida:

                print("""
    Te acercas a la famélica figura.

    Ves que está escribiendo repetidamente algo en la pared.

    "CONSUMIR CORAZÓN"

    Cuando te acercas te das cuenta de que está escribiendo con la sangre de sus desgastadas yemas de los dedos.

    No sabes cuánto tiempo llevará haciéndolo, pero su otra mano está cubierta por un trapo goteante de sangre.

    Mientras gira su mortecino rostro te dice balbuceando:

    "¿Qué haces aquí? Yo no sé qué hago aquí, no debí apuñalarlo. Ahora no puedo verlos. Debo consumir corazón."
    """)

                print("""
    ¿Quieres decirle algo?

    1 - Necesito ayuda.
    2 - Necesitas ayuda.
    3 - Lo apuñalas en un ojo.
    4 - No dices nada.
    """)

                dialogo = input("¿Qué haces? ")

                if dialogo == "1":

                    print("""
    El hombrecillo se dirige a ti con una anodina mirada.

    Te da una brújula.
    """)

                    print("Obtienes una brújula.")

                    if not brujula_obtenida:
                        inventario.append("Brújula")
                        brujula_obtenida = True

                elif dialogo == "2":

                    print("""
    El hombrecillo empieza a reír histéricamente.

    De repente para y sigue con su siniestro quehacer.
    """)

                elif dialogo == "3":

                    print("""
    Clavas el arma en uno de sus ojos.

    El hombre ni siquiera grita.

    Sigue escribiendo con la misma lentitud.

    "CONSUMIR CORAZÓN"

    La sangre cae por su rostro como si no sintiera absolutamente nada.
    """)

                elif dialogo == "4":

                    print("""
    Permaneces en silencio.

    El hombre continúa escribiendo sin volver a mirarte.
    """)

                else:

                    print("No haces nada.")

            else:

                print("""
    El hombre continúa escribiendo.

    "CONSUMIR CORAZÓN"

    "CONSUMIR CORAZÓN"

    Parece haber olvidado que estás ahí.
    """)

        elif opcion == "2":

            print("""
    Observas a tu inquietante alrededor.

    Todo parece en una calma tensa.

    Solo hay silencio y un cielo gris parece reflejar el suelo de hormigón.
    """)

        elif opcion == "3":
                if not brujula_obtenida:
                   print("No sabes donde esta el este")
                else:
                    print("""Te orientas con la extraña brujula que siempre apunta al este.

                          Mientras te apróximas a un vetusto edificio  vas viendo juguetes de madera tirados por
                           el suelo
                          a medida que te acercas empiezas a ver dibujados con tiza en el suelo multiples ojos.

                          Por los dibujos infantiles en la fachada dirias que era una escuela infantil.

                          ¿Pero que hace una escuela infantil en tan macabro escenario?""")
                    orientacion=True

        elif opcion == "4":
             if not brujula_obtenida:    
               print("No sabes donde esta el oeste")
             else :
                 print("""
                       Orientandote vagamente con la extraña brujula atraviesas la densa niebla

                       Tus pasos te llevan al oeste .

                       """)


        elif opcion == "5":
             if not brujula_obtenida:
              print("No sabes donde esta el norte")
             else:
              print("""No sabes muy bien como orientarte con una brujula que siempre apunta al este

                  Pero crees que llegas a una direccion orientada al norte

                  Dentro de la espesa niebla encuentras lo que parece un bunker.

                  Una puerta blindada con una rendija de cristal te deja entrever que algo se mueve dentro

                  Deberia haber una manivela para abrir la puerta desde fuera pero no esta

                  Quizá puedas volver luego con algo contundente que pueda abrir la misteriosa puerta """)

        elif opcion == "6":

            print("""Avanzas lentamente entre la niebla.

    Cada paso amortigua el sonido del anterior.

    El patio parece no terminar nunca.

    De pronto distingues un enorme socavon en el suelo.

    Parece una distancia salvable con un salto

    Del otro lado se oyen graznidos ininteligibles

    Durante unos segundos hay silencio.

    Empiezas a escuchar una respiración

    Lenta.

    Pesada.

    Como la de algo que acecha al otro.

    Un escalofrío recorre todo tu cuerpo.

    Instintivamente das varios pasos hacia atrás.

    Todavía no.

    No estás preparado para saltar, quizá no lo estés nunca.
    """)

        elif opcion == "7":

            print(inventario)

        elif opcion == "8":
            if brujula_obtenida:
             print ("""Sacas la vieja brújula del bolsillo.

    Su cristal está agrietado y la carcasa cubierta de óxido.

    La aguja vibra constantemente.

    Durante unos segundos gira sin control.

    Finalmente se detiene.

    Siempre señala la misma dirección.

    El este.


    """)



        else:

            print("Opción no válida.")



    #Escena 4 La escuela
    print("""
    Abres la siniestra puerta de la escuela infantil.

    Encuentras un largo pasillo con taquillas a ambos lados.

    Muchas de ellas están decoradas con siniestros ojos dibujados con tizas de colores.

    Escuchas un grifo que gotea.

    Las tuberías chirrían.

    El aire huele a humedad y metal oxidado.

    Al fondo unas escaleras ascienden hacia la oscuridad.

    A ambos lados del pasillo hay varias aulas.
    """)


    escena4 = False

    taquillas = False

    aula_musica = False
    aula_dibujo = False
    aula_ciencias = False

    piano_resuelto = False

    nino_aparecido = False
    persecuciones = 0

    while not escena4:

        print("""
    ¿Qué quieres hacer?

    1 - Examinar las taquillas.
    2 - Entrar al aula de música.
    3 - Entrar al aula de dibujo.
    4 - Entrar al aula de ciencias.
    5 - Subir las escaleras.
    6 - Ver inventario.
    """)

        if nino_aparecido:
            print("7 - Seguir al niño.")
        if 'Pelota roja' in inventario:
            print("8 - Entrar en el aula iluminada.")

        opcion = input("\nEscribe una opción: ")

    #--------------------------------------------------------

        if opcion == "1":

            if not taquillas:

                print("""
    Abres lentamente varias taquillas.

    Dentro hay mochilas infantiles completamente podridas.

    Cuadernos deshechos por la humedad.

    Pequeños zapatos.

    Una muñeca sin cabeza.

    En el interior de casi todas alguien ha dibujado un enorme ojo con ceras de colores.

    En una de ellas lees una frase escrita con letra infantil.

    "1-Do 2-SOL 3-MI"

    Un escalofrío recorre tu espalda.
    """)

                taquillas = True

            else:

                print("""
    Las taquillas continúan igual de silenciosas.

    Tienes la sensación de que alguno de aquellos dibujos acaba de mirarte.
    """)

    #--------------------------------------------------------

        elif opcion == "2":

            if not aula_musica:

                print("""
    Empujas lentamente la puerta.

    Un fuerte olor a madera vieja llena la estáncia.

    Pequeños instrumentos descansan cubiertos de polvo.

    Hay tambores.

    Xilófonos.

    Flautas.

    Y un pequeño piano infantil. 

    Te acercas al instrumento


    """)

                while not piano_resuelto:

                    print("""
    ¿Qué quieres hacer?

    1 - Pulsar DO.
    2 - Pulsar RE.
    3 - Pulsar MI.
    4 - Pulsar FA.
    5 - Pulsar SOL.
    6 - Salir del piano.
    """)

                    notas = []

                    correcta = ["1","5","3"]

                    while len(notas) < 3:

                        tecla = input("Pulsa una nota: ")

                        if tecla in ["1","2","3","4","5"]:

                            notas.append(tecla)

                        else:

                            print("Esa nota no existe.")

                    if notas == correcta:

                        print("""
    La pequeña melodía resuena por toda la escuela.

    El eco tarda varios segundos en desaparecer.

    Después...

    Silencio.

    ...

    Jejeje...

    Una pequeña risa infantil rompe la calma.

    Te giras de golpe.

    Alguien permanece inmóvil junto a la puerta.

    Parece un niño , con un antiguo uniforme escolar

    Lleva una vieja máscara de gas demasiado grande para él.

    Inclina ligeramente la cabeza.

    Levanta un dedo señalándote.

    Y dice alegremente...

    "¡Pilla pilla!"

    Antes de que puedas reaccionar...

    Sale corriendo por el pasillo.
    """)

                        piano_resuelto = True
                        aula_musica = True

                        nino_aparecido = True

                    else:

                        print("""
    Las notas resuenan desafinadas.

    No ocurre absolutamente nada.
    """)

            else:

                print("""
    El aula permanece vacía.

    El piano sigue donde estaba.

    Todavía vibra alguna nota al aire.
    """)

    #--------------------------------------------------------

        elif opcion == "3":

            if not aula_dibujo:

                print("""
    Las paredes están completamente cubiertas por dibujos infantiles.

    Casas.

    Árboles.

    Perros.

    Familias.

    Todos parecen normales.

    Hasta que llegas al fondo.

    Todos los dibujos empiezan a mostrar enormes y siniestros ojos observándolo todo.

    En el centro de las inquietantes miradas aparece un niño con máscara de gas.

    Debajo alguien escribió:

    "Siempre quiere jugar."

    No encuentras nada más de utilidad.
    """)

                aula_dibujo = True

                if nino_aparecido:

                    print("""

    Mientras abandonas el aula...

    Escuchas otra vez aquella alegre risa.

    "Jejeje..."

    Al asomarte al pasillo solo alcanzas a ver al niño girando una esquina.

    "¡Pilla pilla!"
    """)

                    persecuciones += 1

            else:

                print("""
    Ya has inspeccionado todos los dibujos.

    Siguen resultando igual de inquietantes.
    """)

    #--------------------------------------------------------

        elif opcion == "4":

            print("""
    La puerta está cerrada.

    Parece atascada por algo al otro lado.

    Necesitarás encontrar otra forma de entrar.
    """)

    #--------------------------------------------------------

        elif opcion == "5":

            print("""
    Intentas subir las escaleras.

    Después de apenas unos peldaños...

    Un muro enorme de pupitres y sillas desvencijadas impide el paso.
    """)

    #--------------------------------------------------------

        elif opcion == "6":

            print("\n===== INVENTARIO =====\n")

            if len(inventario)==0:

                print("No llevas ningún objeto.")

            else:

                for objeto in inventario:

                    print("-",objeto)

    #--------------------------------------------------------

        elif opcion=="7" and nino_aparecido:

            if "Pelota roja" not in inventario:

                print("""
    Corres tras el niño.

    Escuchas sus pequeñas pisadas alejándose.

    "Jejeje..."

    Cuando giras la esquina...

    Ha desaparecido.

    Solo queda una pequeña pelota roja balanceándose lentamente en el suelo.

    La recoges.

    Te das cuenta que hay una puerta iluminada de la que no te habias percatado antes.

    ¿Siempre ha estado ahí esa puerta?

    Obtienes:

    - Pelota roja
    """)

                inventario.append("Pelota roja")

            else:

                print("""
    No encuentras al niño.

    Solo queda el inquietante silencio del colegio.
    """)

    #--------------------------------------------------------

        elif opcion=="8" and "Pelota roja" in inventario:

            print(f"""
    Empujas la puerta de un aula.

    Todo parece imposible.

    Las paredes están recién pintadas.

    Los juguetes están perfectamente ordenados.

    El ambiente resulta cálido y acogedor.

    Sobre la pizarra alguien ha escrito:

    {nombre}

    Alrededor de tu nombre hay decenas de pequeños círculos rojos dibujados con tiza.

    En una esquina descansa una pequeña canasta de juguete.
    """)

            while True:

                print("""
    1 - Examinar la pizarra.
    2 - Lanzar la pelota a la canasta.
    3 - Salir del aula.
    """)

                accion=input("Elige una opción: ")

                if accion=="1":

                    print("""
    No recuerdas haber estado nunca aquí.

    Entonces...

    ¿Quién escribió tu nombre?
    """)

                elif accion=="2":

                    print("""
    Lanzas la pelota.

    Clonc.

    Entra limpiamente por la canasta.

    "Jejeje..."

    Te giras.

    El niño de la máscara de gas está justo detrás de ti.

    Sin pronunciar una palabra te entrega una vieja chapa y un pesado hacha de incendios.

    Cuando vuelves a mirarlo...

    Ha desaparecido.
    """)

                    if "Chapa" not in inventario:
                        inventario.append("Chapa")

                    if "Hacha de incendios" not in inventario:
                        inventario.append("Hacha de incendios")

                    print("""
    Obtienes:

    - Chapa
    - Hacha de incendios
    """)

                    print("""
    Examinas la chapa.

    En ella puede leerse:

    "Ask me about Loom"

    Parece que ya has investigado toda la estáncia.

    Quizá el hacha pueda servirte para abrirte paso y escapar de esta pesadilla
    """)

                    escena4=True
                    break

                elif accion=="3":
                    break

                else:
                    print("No puedes hacer eso.")

    #--------------------------------------------------------

        else:

            print("\nNo puedes hacer eso.\n")


    #ESCENA 5 FINAL





    # ==========================================================
    # ESCENA 5 - EL BÚNKER
    # ==========================================================

    print("""
    Abandonas la escuela.

    La niebla vuelve a envolverte.

    Regresas al patio de hormigón.

    Ahora llevas contigo una pesada hacha de incendios.
    """)

    escena5=False
    gas=False
    criatura_congelada=False
    corazón=False

    while not escena5:

        print("""
    ¿Qué quieres hacer?

    1 - Ir hacia el este.
    2 - Ir hacia el oeste.
    3 - Ir hacia el norte.
    4 - Ir hacia el sur.
    5 - Ver inventario.
    """)

        opcion=input("Escribe una opción: ")

        if opcion=="1":

            print("La escuela permanece en silencio.")

        elif opcion=="2":

            print("La niebla es demasiado espesa para encontrar nada nuevo.")

        elif opcion=="4":

            print("""
    La respiración del otro lado del socavón continúa allí.

    Todavía no estás preparado.
    """)

        elif opcion=="5":

            print("\n===== INVENTARIO =====\n")
            for objeto in inventario:
                print("-",objeto)

        elif opcion=="3":

            if "Hacha de incendios" not in inventario:

                print("Necesitas algo para abrir el búnker.")

            else:

                print("""

    Ante ti camuflada entre el hormigon aparece una puerta blindada. 

    ¿Quizá hayas estado aqui antes?

    Un vetusto mecanismo impide abrirla.

    Golpeas el mecanismo con el hacha.

    Tras varios impactos...

    La puerta blindada termina cediendo.

    Entras.

    El interior está lleno de tuberías oxidadas.

    Motores gigantes.

    Vapor.

    El aire resulta irrespirable.

    Hay un largo pasillo con luces fluorescentes que parpadean

    A lo lejos al final del pasillo puedes ver un letrero que pone "SALIDA"

    Pero esta tachado con un color rojizo

    Mientras avanzas...

    Dos enormes ojos se abren en la oscuridad.

    Una gigantesca criatura antropomórfica se la alza ante ti

    Su cuerpo cubierto de ojos y tentáculos que asoman de partes imposibles de una anatomía normal.

    Un escalofrío recorre tu espalda y sabes que tu vida está próxima a su fin.

    Debes actuar rapido.
    """)

                while True:

                    print("""
    ¿Qué haces?

    1 - Examinar criatura.
    2 - Atacarla con el hacha.
    3 - Golpear una tubería.
    4 - Huir.
    """)

                    accion=input("Opción: ")

                    if accion=="1":

                        print("""
    La criatura se mueve rápidamente hacia ti

    Su movimiento pesado y amenazante lo convierten en un rival demasiado peligroso para  ti

    Sin embargo...

    Parece alejarse de algunas tuberias determinadas.

    Mientras tu vas reculando lentamente aletargado por el terror.
    """)

                    elif accion=="2":

                        if not criatura_congelada:

                            print("""
    Intentas golpear a la grotesca criatura con tu hacha.

    Tú eres demasiado lento y la criatura lo aprovecha

    Antes siquiera de que puedas levantar el hacha

    Uno de sus afilados tentáculos ya ha atravesado tu pecho

    Tus vísceras caen al suelo antes de que tu mutilado cuerpo llegue a caer.

    Estas muerto y tus ultimos pensamientos se ahogan en una horrible imagen.

    Ojos inyectados en sangre que te observan inquisitorialmente

    ========== GAME OVER ==========
    """)
                            return

                        else:

                            print("""
    El hacha atraviesa el cuerpo congelado.

    La criatura se hace añicos.

    Sus incontables ojos se cierran y se disuelven en una masa sanguinolenta.

    Los tentáculos se marchitan.

    Entre una pestilente mezcla de vísceras algo se mueve

    Es el corazón de la criatura

    Palpita. Sus latidos casi parecen voces

    Una oscura parte de ti tiene hambre y lo encuentra apetitoso.
    """)

                            corazón=True
                            break

                    elif accion=="3":

                        if not gas:

                            print("""
    Golpeas violentamente la tubería.

    Una nube de gas criogénico inunda la sala.

    La criatura intenta avanzar.

    Cada vez más despacio.

    Hasta quedar completamente congelada.
    """)

                            gas=True
                            criatura_congelada=True

                        else:

                            print("La tubería ya está rota.")

                    elif accion=="4":

                        print("""
    Intentas escapar.

    Te das la vuelta y lo unico que sientes es un horrible dolor punzante en la espalda

    Miras hacia tu pecho,

    Ves un tentáculo que atraviesa tu tórax y sostiene tu corazón mientras lo aplasta.


    Tu unico consuelo es que esperas que estalle rápidamente y acabe el indescriptible sufrimiento


    ========== GAME OVER ==========
    """)
                        return

                if corazón:

                    while True:

                        print("""
    Ante ti solo quedan dos posibilidades.

    1 - Comer el corazón.
    2 - Atravesar la puerta.

    Sobre la puerta puede leerse:

    SALIDA

    La palabra está tachada con lo que parece sangre,

    Justo abajo hay escritas tres palabras:

    ENCONTRAR A DIOS
    """)

                        final=input("Elige una opción: ")

                        if final=="1":

                            print("""
    El corazón aún late.

    Lo devoras.

    Sientes que todo el interior de tu cuerpo se está rompiendo.

    Tus huesos se deshacen.

    Sientes brotar ojos por todas partes.

    Tu carne muta, se vuelve blanda.

    Intentas gritar pero no tienes pulmones

    Solo una cantidad de dientes repartidos por la masa informe que ahora es tu cuerpo

    Pero no tienes ninguna boca con la que quejarte

    Se te viene a la mente la extraña criatura del pasillo.

    Nunca intentó hacerte daño.

    Quería impedir que acabaras convirtiéndote en ella.

    ========== FINAL  ==========
    """)
                            criatura=input("Escribe CONCEDENOS OJOS")
                            escena5=True
                            break

                        elif final=="2":

                            print("""
    Cruzas la puerta.

    Todo es luz refulgente y oscuridad eterna

    No existe suelo.

    No existe cielo.

    Una presencia imposible llena el universo.

    Un único ojo se abre.

    Comprendes que jamás podrás entender lo que contempla.

    Tu existencia se disuelve lentamente entre estrellas y planetas salvajes.

    ========== FIN ==========

                GRACIAS POR JUGAR

                   "La emoción más antigua y poderosa del ser humano es el miedo;
                        y el más antiguo y poderoso de los miedos es el miedo a lo desconocido."
                                  "H.P.Lovecraft"

                                  
    """)
                            
                            lovecraft=input("escribe Lovecraft")
                            escena5=True
                            break

        else:

            print("Opción no válida.")


while True:

    jugar()

    respuesta = input("\n¿Quieres volver a empezar? (S/N): ").upper()

    if respuesta != "S":
        print("Gracias por jugar.")
        break
    
if __name__ == "__main__":
    jugar()