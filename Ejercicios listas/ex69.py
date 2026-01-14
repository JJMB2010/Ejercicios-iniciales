# 69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.

a=int(input("Cuantos número quiere poner: "))
lista=[]

for x in range(0,a):
    b=int(input("Dime un número: "))
    lista.append(b)

lista.sort()
print(lista)