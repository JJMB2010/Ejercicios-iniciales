# 70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.

a=1
b=int(input("Cuantas palabras quieres poner: "))
lista=[]

for x in range(0,b):
    c=str(input("Introduce " + str(x+1) + "ª palabra:"))
    lista.append(c)

lista.sort()
print("Lista1 contiene:", lista)

lista.sort(reverse=True)
print("Lista2 contiene:", lista)