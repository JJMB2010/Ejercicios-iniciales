import math

lista_intentos=[]
lista_bien=[]
lista_mal=[]
x=0
error=0
acierto=0

while x==0:
    dni=input("Dime tu DNI, són 8 números: ")
    lista_letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
    x=0
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
    x=int(input("Quieres continuar si(0), no(1): "))

print("RESULTADOS, escoje una opción:")
print("     1. Lista NIF correcto ordenados de mayor a menor.")
print("     2. Lista DNI incorrecto ordenados de mayor a menor.")
print("     3. Numero total de errores.")
print("     4. Numero DNI correctos.")
print("     5. Porcentajes de intentos con y sin errores.")
print("     6. Salir.")
a=int(input("Dime la opción(1/2...): "))
if a==1:
    print(lista_bien)
if a==2:
    print(lista_mal)
if a==3:
    print(error)
if a==4:
    print(acierto)
if a==5:
    print("Intentos totales:", acierto+error)
    print("     % Total de DNI incorrectos:",round((error/(acierto+error))*100,1))
    print("     % Total de DNI correctos:",round((acierto/(acierto+error))*100,1))
    len=lista_intentos.count("0")
    num=lista_intentos.count("1")
    err=lista_intentos.count("2")
    print("     % Total de DNI con error en longitud:",round((len/(acierto+error))*100,1))
    print("     % Total de DNI no numérico:",round((num/(acierto+error))*100,1))
    print("     % Total de DNI inexistentes:",round((err/(acierto+error))*100,1))
if a==6:
    print("Programa finalizado.")