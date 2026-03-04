import random
import time

# Empezamos creando una lista con todas las palabras del txt
tumadre=0
texto=open('Diccionario.txt', "r+", encoding="utf-8")
texto=texto.read().splitlines()

# Inicio del ahorcado
while tumadre==0:
    # Pregunta de inicio
    ñ=input("Quieres jugar al ahorcado(s/n)? ")

    # Prueba antitontos 1.0
    if ñ.isalpha():
        if str(ñ) in "Nn":
            # Despedida
            print("Adiós :(")
            tumadre=1

        elif str(ñ) in "Ss":
            # Iniciando el ahorcado de verdad
            tumadre2=0

            while tumadre2==0:
                # Elección de modos
                print("MODOS")
                print("     1.Modo normal.")
                print("     2.Modo con tiempo limite de 30 segundos.")
                print("     3.Modo dificil.")
                print("     4.IMPOSIBLE.")
                modo=input("A que modo quieres jugar: ")

                # Prueba antitontos 1.5
                if modo in "1" or modo in "2" or modo in "3" or modo in "4":
                    # Iniciando el ahorcado de verdad, ahora si
                    min=0
                    Lista_partida=[]
                    Lista_ahorcado=["_","_","_","_","_","_","_","_"]
                    Lista_ahorcado2=["A","H","O","R","C","A","D","O"]
                    Lista_acierto=[]
                    Lista_error=[]
                    si="_"
                    c=""
                    dios=1
                    t=1
                    p=0
                    secret=""
                    b=0
                    w=0
                    ex=("áéíóú")
                    ab=("aeiou")

                    # Seleccionamos la palabra secreta
                    secret=str(random.choice(texto))
                    secret2=secret
                    secret=secret.lower()

                    # Creamos los "_" y empezamos el tiempo
                    for z in range(len(str(secret))):
                        Lista_partida.append(si)
                    print(secret)
                    tiktak=time.perf_counter()

                    # Cosas de modos 
                    if modo in "3" or modo in "4":
                        print("Dificultad adquirida, solo tienes 4 intentos.")
                    if modo in "4" or modo in "2":
                        print("Dificultad actualizada, tiempo limite de 30 segundos.")

                    # En busca de la palabra secreta
                    while b==0:
                        x=input("Dime una letra: ")
                        x=x.lower()
                        c=x
                        f=0

                        # Prueba antitontos 2.0
                        if x.isalpha():
                            
                            # Divisando la letra seleccionada
                            for a in range(len(str(secret))):
                                x=c
                                if x in ex:
                                    if x in str(secret[a]):
                                        Lista_partida[a]=x
                                        f=1
                                    else:
                                        v=ex.find(x)
                                        x=ab[v]
                                        if x in str(secret[a]):
                                            Lista_partida[a]=x
                                            f=1
                                else:
                                    if x in str(secret[a]):
                                        Lista_partida[a]=x
                                        f=1
                                    if x in ab:
                                        v=ab.find(x)
                                        x=ex[v]
                                        if x in str(secret[a]):
                                            Lista_partida[a]=x
                                            f=1

                            # Viendo el tiempo
                            tiktak2=time.perf_counter()
                            timef=round(tiktak2-tiktak,0)

                            # Cosas de modos x2
                            if modo in "2" or modo in "4":
                                if timef>=30:
                                    Lista_ahorcado=Lista_ahorcado2
                                    tiktak2=time.perf_counter()
                                    timef=round(tiktak2-tiktak,0)
                                    if timef > 60:
                                        min=min+1
                                        timef=timef-60
                                    print("Has tardado",min,"minutos y",timef,"segundos.")
                                    print("["," , ".join(Lista_partida)+"]")
                                    print("Es DECEPCIONANTE >:(")
                                    print("Era",secret)
                                    print("Errores:",len(Lista_error))
                                    print("Aciertos:",len(Lista_acierto))
                                    b=1
                                    p=1
                                    tumadre2=1

                                    # Añadiendo palabras
                                    while dios==1:
                                        ñ=input("Quieres añadir una palabra(s/n)? ")
                                        if ñ.isalpha():
                                            if str(ñ) in "Nn":
                                                texto.remove(secret2)
                                                dios=0
                                            elif str(ñ) in "Ss":
                                                while t!=0:
                                                    t=input("Dime una nueva palabra: ")
                                                    if t.isalpha():
                                                        texto.append(str(t))
                                                        texto.remove(secret2)
                                                        t=0
                                                        dios=0
                                                    else:
                                                        print("Me estás poniendo nervioso :/")
                                            else:
                                                print("PARA >:(")
                                        else:
                                            print("PARA >:(")

                            # Mirando si lo haces bien
                            if f==1 and p==0:
                                if x not in Lista_acierto:
                                    Lista_acierto.append(x)
                                    print("["," , ".join(Lista_partida)+"]")
                                    print("Errores:","["," , ".join(Lista_error)+"]")
                                    print("Aciertos:","["," , ".join(Lista_acierto)+"]")

                                    # Está perfecto...
                                    if "_" not in Lista_partida and p==0:
                                        b=1
                                        if timef > 60:
                                            min=min+1
                                            timef=timef-60
                                        print("Has tardado",min,"minutos y",timef,"segundos.")
                                        print("Está perfecto :D")
                                        print("["," , ".join(Lista_partida)+"]")
                                        print("Errores totales:",len(Lista_error))
                                        print("Aciertos totales:",len(Lista_acierto))
                                        p=1
                                        tumadre2=1

                                        # Añadiendo palabras
                                        while dios==1:
                                            ñ=input("Quieres añadir una palabra(s/n)? ")
                                            if ñ.isalpha():
                                                if str(ñ) in "Nn":
                                                    texto.remove(secret2)
                                                    dios=0
                                                elif str(ñ) in "Ss":
                                                    while t!=0:
                                                        t=input("Dime una nueva palabra: ")
                                                        if t.isalpha():
                                                            texto.append(str(t))
                                                            texto.remove(secret2)
                                                            t=0
                                                            dios=0
                                                        else:
                                                            print("Me estás poniendo nervioso :/")
                                                else:
                                                    print("PARA >:(")
                                            else:
                                                print("PARA >:(")

                                else:
                                    print("["," , ".join(Lista_partida)+"]")
                                    print("Errores:","["," , ".join(Lista_error)+"]")
                                    print("Aciertos:","["," , ".join(Lista_acierto)+"]")
                                
                            # La letra no está
                            elif f==0 and p==0:
                                Lista_ahorcado[w]=Lista_ahorcado2[w]

                                # Cosas de modos 4.0
                                if modo in "3" or modo in "4" and p==0:
                                    w=w+1
                                    Lista_ahorcado[w]=Lista_ahorcado2[w]
                                if x not in Lista_error:
                                    Lista_error.append(x)
                                print("["," , ".join(Lista_ahorcado)+"]")
                                w=w+1
                                print("["," , ".join(Lista_partida)+"]")
                                print("Errores:","["," , ".join(Lista_error)+"]")
                                print("Aciertos:","["," , ".join(Lista_acierto)+"]")

                                # Eres malísimo...
                                if "_" not in Lista_ahorcado and p==0:
                                    tiktak2=time.perf_counter()
                                    timef=round(tiktak2-tiktak,0)
                                    if timef > 60:
                                        min=min+1
                                        timef=timef-60
                                    print("Has tardado",min,"minutos y",timef,"segundos.")
                                    print("["," , ".join(Lista_partida)+"]")
                                    print("Es DECEPCIONANTE >:(")
                                    print("Era",secret)
                                    print("Errores:",len(Lista_error))
                                    print("Aciertos:",len(Lista_acierto))
                                    p=1
                                    b=1
                                    tumadre2=1

                                    # Añadiendo palabras
                                    while dios==1:
                                        ñ=input("Quieres añadir una palabra(s/n)? ")
                                        if ñ.isalpha():
                                            if str(ñ) in "Nn":
                                                texto.remove(secret2)
                                                dios=0
                                            elif str(ñ) in "Ss":
                                                while t!=0:
                                                    t=input("Dime una nueva palabra: ")
                                                    if t.isalpha():
                                                        texto.append(str(t))
                                                        texto.remove(secret2)
                                                        t=0
                                                        dios=0
                                                    else:
                                                        print("Me estás poniendo nervioso :/")
                                            else:
                                                print("PARA >:(")
                                        else:
                                            print("PARA >:(")

                        else:
                            print("ERROR >:[")
                            print("Pon una letra")
                else:
                    print("MAL")
                    print("1/2/3/4")

        else:
            print("ERROR >:[")
            print("Pon Ss o Nn")

    else:
        print("ERROR >:[")
        print("Pon Ss o Nn")

# Adiós