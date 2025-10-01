# 31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
import math

si="A quien madruga Dios le ayuda"

yo=str(input("Dime una palabra: "))

if yo in si:
    busca=si.index(yo)
    print("la palabra está en la posición",busca)
else:
    print("La palabra no está en la frase")