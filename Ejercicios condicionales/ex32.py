# 32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
import math

si="A quien madruga Dios le ayuda"

yo=str(input("Dime una palabra: "))

casi=yo.lower()
casisi=si.lower()

if casi in casisi:
    busca=casisi.index(casi)
    print("la palabra está en la posición",busca)

else:
    print("La palabra no está en la frase")