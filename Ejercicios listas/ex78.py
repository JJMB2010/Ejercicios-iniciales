# 78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir

lista1=["a","b","D","x","r","X","3","h","w","2","i"]
x=1
while x==1:
    a=input("Que valor quieres obliterar: ")
    if a.isnumeric():
        lista1.remove(a)
        print(lista1)
    else:
        print("Introduce valor numérico.")
    b=str(input("Deseas seguir(s/n): "))
    if b in "nN":
        x=0