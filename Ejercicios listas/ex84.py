# 84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra.
import random
l=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
x=str(random.choice(l))
for y in range(1,len(x)):
    list(x)
    a=random.choice(x)
    list(x).remove(a)
    print(a)