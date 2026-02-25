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
            Lista_partida=[]
            Lista_ahorcado=["_","_","_","_","_","_","_","_"]
            Lista_ahorcado2=["A","H","O","R","C","A","D","O"]
            bien=[]
            mal=[]
            si="_"
            c=""
            t=1
            secret=""
            b=0
            w=0
            ex=("áéíóú")
            ab=("aeiou")
            secret=random.choice(Lista_palabrasecreta)
            secret2=secret
            secret.lower()
            for z in range(len(str(secret))):
                Lista_partida.append(si)
            print(secret)

            while b==0:
                x=input("Dime una letra: ")
                x.lower()
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
                        if "_" not in Lista_partida:
                            b=1
                            print("Está perfecto :D")
                            print(Lista_partida)

                        else:
                            print(Lista_partida)

                    elif f==0:
                        Lista_ahorcado[w]=Lista_ahorcado2[w]
                        w=w+1
                        print(Lista_ahorcado)

                        if "_" not in Lista_ahorcado:
                            b=1
                            print(Lista_partida)
                            print("Es DECEPCIONANTE >:(")
                            print("Era",secret)
                else:
                    print("ERROR >:[")
                    print("Pon una letra")

                if "_" not in Lista_ahorcado or "_" not in Lista_partida:
                    while dios!=0:
                        ñ=input("Quieres añadir una palabra(s/n)? ")

                        if ñ.isalpha():
                            if str(ñ) in "Nn":
                                Lista_palabrasecreta.remove(secret)
                                dios=0

                            elif str(ñ) in "Ss":
                                while t!=0:
                                    t=input("Dime una nueva palabra: ")

                                    if t.isalpha():
                                        Lista_palabrasecreta.append(str(t))
                                        Lista_palabrasecreta.remove(secret)
                                        t=0
                                        dios=0
                                    else:
                                        print("Me estás poniendo nervioso :/")
                            else:
                                print("PARA >:(")

        else:
            print("ERROR >:[")
            print("Pon Ss o Nn")

    else:
        print("ERROR >:[")
        print("Pon Ss o Nn")