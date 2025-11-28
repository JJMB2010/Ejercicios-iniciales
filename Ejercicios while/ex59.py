# 59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random

ns=random.randint(1,1000)
n=int(input("Dime un numero del 1 al 1000: "))
i=1

while ns!=n:

    if n<ns:
        print("Más alto")
    else:
        print("Más bajo")
    n=int(input("Dime un numero del 1 al 1000: "))
    i=i+1

print("Intentos:",i)
print("Numero correcto")