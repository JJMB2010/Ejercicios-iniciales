import math
#Variables sumamente importantes e imposibles de simplificar
lista_intentos=[]
lista_bien=[]
lista_mal=[]
x=0
y=0
z=0
error=0
acierto=0
#Sufrir con el DNI
while y==0:
    dni=input("Dime tu DNI, són 8 números: ")
    lista_letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    y=0
    z=0
#Mirar si lo haces bien
    if len(str(dni))==8:
        if dni.isnumeric():
            a=int(dni)%23
            c=0

            for x in range(0,22):
                if x==a:
                    b=lista_letras[x]
                    c=1

            if c==0:
                lista_intentos.append("2")
                lista_mal.append(dni)
                error=error+1
                print("ERROR")

            else:
                lista_intentos.append("3")
                dni=(str(dni) + "-" + str(b))
                acierto=acierto+1
                lista_bien.append(dni)
                print(dni)

        else:
            lista_intentos.append("1")
            lista_mal.append(dni)
            error=error+1
            print("El valor no es numérico.")

    else:
        lista_intentos.append("0")
        lista_mal.append(dni)
        error=error+1
        print("El valor intoducido no tiene la longitud adecuada.")
#Por si responde alguien sin neuronas
    while z==0:
        x=input("Quieres continuar si(s), no(n): ")

        if x in "sSnN" and x.isalnum():

            if x in "nN" and x.isalnum():
                z=1
                y=1

            if x in "sS" and x.isalnum():
                z=1

        else:
            print("ERROR")

x=0
#Final aprueba de tontos
while x==0:

    print("RESULTADOS, escoje una opción:")
    print("     1. Lista NIF correcto ordenados de mayor a menor.")
    print("     2. Lista DNI incorrecto ordenados de mayor a menor.")
    print("     3. Numero total de errores.")
    print("     4. Numero DNI correctos.")
    print("     5. Porcentajes de intentos con y sin errores.")
    print("     6. Salir.")

    a=input("Dime la opción(1/2...): ")

    if a.isnumeric():

        a=int(a)

        if a==1:
            print(lista_bien)
            x=1

        if a==2:
            print(lista_mal)
            x=1

        if a==3:
            print(error)
            x=1

        if a==4:
            print(acierto)
            x=1

        if a==5:

            print("Intentos totales:", acierto+error)
            print("     % Total de DNI incorrectos:",round((error/(acierto+error))*100,1),"%")
            print("     % Total de DNI correctos:",round((acierto/(acierto+error))*100,1),"%")
            len=lista_intentos.count("0")
            num=lista_intentos.count("1")
            err=lista_intentos.count("2")
            print("     % Total de DNI con error en longitud:",round((len/(acierto+error))*100,1),"%")
            print("     % Total de DNI no numérico:",round((num/(acierto+error))*100,1),"%")
            print("     % Total de DNI inexistentes:",round((err/(acierto+error))*100,1),"%")
            x=1

        if a==6:

            print("Programa finalizado.")
            x=1
#Respuesta para tontos
    if a !=1 and a !=2 and a !=3 and a !=4 and a !=5 and a !=6:

        print("ERROR")