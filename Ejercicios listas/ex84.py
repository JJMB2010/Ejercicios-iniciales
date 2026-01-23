# 84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra.
import random
l=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
x=str(random.choice(l))
b=len(x)
respuesta=x
ll=[]
pal=[]
sad=0

for r in x:
    pal.append(r)

for y in range(0,b):
    a=random.choice(pal)
    pal.remove(a)
    ll.append(a)
print(ll)

while sad!=3:
    dec=str(input("Dime la palabra: "))
    if dec == respuesta:
        print("Correcto")
        sad=3
    else:
        print("Incorrecto")
        sad=sad+1
        
print("No acertastes nada")