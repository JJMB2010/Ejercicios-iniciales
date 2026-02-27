import random
import time

tumadre=0
Lista_palabrasecreta=["Estrenar","Pasear","Cuñado","Desvelarse","Destripar","Incisión","Lujuria","Inquisición","Ultimátum","Bonapártista"]

while tumadre==0:
    ñ=input("Quieres jugar al ahorcado(s/n)? ")
    dios=1
    if ñ.isalpha():
        if str(ñ) in "Nn":
            print("Adiós :(")
            tumadre=1
        elif str(ñ) in "Ss":
            modos=0

            while modos == 0:
                print("MODOS")
                print("     1.Modo normal.")
                print("     2.Modo con tiempo limite de 45 segundos.")
                print("     3.Modo dificil.")
                print("     4.IMPOSIBLE.")
                modo=input("A que modo quieres jugar:")
                
                if modo in "1" or modo in "2" or modo in "3" or modo in "4":
                    min=0
                    Lista_partida=[]
                    Lista_ahorcado=["_","_","_","_","_","_","_","_"]
                    Lista_ahorcado2=["A","H","O","R","C","A","D","O"]
                    Lista_acierto=[]
                    Lista_error=[]
                    si="_"
                    c=""
                    t=1
                    secret=""
                    b=0
                    w=0
                    texto=open('Diccionario.txt')
                    ex=("áéíóú")
                    ab=("aeiou")
                    secret=random.choice(texto)
                    secret2=secret
                    secret=secret.lower()
                    for z in range(len(str(secret))):
                        Lista_partida.append(si)
                    print(secret)

                    if modo in"1":
                        tiktak=time.perf_counter()

                        while b==0:
                            x=input("Dime una letra: ")
                            x=x.lower()
                            c=x
                            f=0

                            if x.isalpha():
                            
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
                                if f==1:
                                    Lista_acierto.append(x)
                                    if "_" not in Lista_partida:
                                        b=1
                                        tiktak2=time.perf_counter()
                                        timef=round(tiktak2-tiktak,0)
                                        if timef > 60:
                                            min=min+1
                                            timef=timef-60
                                        print("Has tardado",min,"minutos y",timef,"segundos.")
                                        print("Está perfecto :D")
                                        print(Lista_partida)
                                        print("Errores totales:",len(Lista_error))
                                        print("Aciertos totales:",len(Lista_acierto))

                                    else:
                                        print(Lista_partida)
                                        print("Errores:",Lista_error)
                                        print("Aciertos:",Lista_acierto)

                                elif f==0:
                                    Lista_ahorcado[w]=Lista_ahorcado2[w]
                                    Lista_error.append(x)
                                    w=w+1
                                    print(Lista_ahorcado)
                                    print("Errores:",Lista_error)
                                    print("Aciertos:",Lista_acierto)

                                    if "_" not in Lista_ahorcado:
                                        b=1
                                        tiktak2=time.perf_counter()
                                        timef=round(tiktak2-tiktak,0)
                                        if timef > 60:
                                            min=min+1
                                            timef=timef-60
                                        print("Has tardado",min,"minutos y",timef,"segundos.")
                                        print(Lista_partida)
                                        print("Es DECEPCIONANTE >:(")
                                        print("Era",secret)
                                        print("Errores:",len(Lista_error))
                                        print("Aciertos:",len(Lista_acierto))
                            else:
                                print("ERROR >:[")
                                print("Pon una letra")

                            if "_" not in Lista_ahorcado or "_" not in Lista_partida:
                                while dios!=0:
                                    ñ=input("Quieres añadir una palabra(s/n)? ")

                                    if ñ.isalpha():
                                        if str(ñ) in "Nn":
                                            Lista_palabrasecreta.remove(secret2)
                                            dios=0

                                        elif str(ñ) in "Ss":
                                            while t!=0:
                                                t=input("Dime una nueva palabra: ")

                                                if t.isalpha():
                                                    Lista_palabrasecreta.append(str(t))
                                                    Lista_palabrasecreta.remove(secret2)
                                                    t=0
                                                    dios=0
                                                else:
                                                    print("Me estás poniendo nervioso :/")
                                        else:
                                            print("PARA >:(")
                                    else:
                                        print("PARA >:(")
                    
                    if modo in"2":
                        a=a
                    if modo in"3":
                        tiktak=time.perf_counter()

                        while b==0:
                            x=input("Dime una letra: ")
                            x=x.lower()
                            c=x
                            f=0

                            if x.isalpha():
                            
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
                                if f==1:
                                    Lista_acierto.append(x)
                                    if "_" not in Lista_partida:
                                        b=1
                                        tiktak2=time.perf_counter()
                                        timef=round(tiktak2-tiktak,0)
                                        if timef > 60:
                                            min=min+1
                                            timef=timef-60
                                        print("Has tardado",min,"minutos y",timef,"segundos.")
                                        print("Está perfecto :D")
                                        print(Lista_partida)
                                        print("Errores totales:",len(Lista_error))
                                        print("Aciertos totales:",len(Lista_acierto))

                                    else:
                                        print(Lista_partida)
                                        print("Errores:",Lista_error)
                                        print("Aciertos:",Lista_acierto)

                                elif f==0:
                                    Lista_ahorcado[w]=Lista_ahorcado2[w]
                                    w=w+1
                                    Lista_ahorcado[w]=Lista_ahorcado2[w]
                                    Lista_error.append(x)
                                    w=w+1
                                    print(Lista_ahorcado)
                                    print("Errores:",Lista_error)
                                    print("Aciertos:",Lista_acierto)

                                    if "_" not in Lista_ahorcado:
                                        b=1
                                        tiktak2=time.perf_counter()
                                        timef=round(tiktak2-tiktak,0)
                                        if timef > 60:
                                            min=min+1
                                            timef=timef-60
                                        print("Has tardado",min,"minutos y",timef,"segundos.")
                                        print(Lista_partida)
                                        print("Es DECEPCIONANTE >:(")
                                        print("Era",secret)
                                        print("Errores:",len(Lista_error))
                                        print("Aciertos:",len(Lista_acierto))
                            else:
                                print("ERROR >:[")
                                print("Pon una letra")

                            if "_" not in Lista_ahorcado or "_" not in Lista_partida:
                                while dios!=0:
                                    ñ=input("Quieres añadir una palabra(s/n)? ")

                                    if ñ.isalpha():
                                        if str(ñ) in "Nn":
                                            Lista_palabrasecreta.remove(secret2)
                                            dios=0

                                        elif str(ñ) in "Ss":
                                            while t!=0:
                                                t=input("Dime una nueva palabra: ")

                                                if t.isalpha():
                                                    Lista_palabrasecreta.append(str(t))
                                                    Lista_palabrasecreta.remove(secret2)
                                                    t=0
                                                    dios=0
                                                else:
                                                    print("Me estás poniendo nervioso :/")
                                        else:
                                            print("PARA >:(")
                                    else:
                                        print("PARA >:(")
                    if modo in"4":
                        a=a

        else:
            print("ERROR >:[")
            print("Pon Ss o Nn")

    else:
        print("ERROR >:[")
        print("Pon Ss o Nn")