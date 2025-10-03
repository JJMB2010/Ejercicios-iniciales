# 33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años
import math

fra=str(input("dime una frase: "))

fra=fra.lower()

a=fra.count("a")
e=fra.count("e")
i=fra.count("i")
o=fra.count("o")
u=fra.count("u")

print("El número de a es",a,"el número de e es",e,"el número de i es",i,"el número de o es",o,"el número de u es",u)