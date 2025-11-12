# 48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario tenga x oportunidades para ver si letra introducida está en esa palabra.

secret=str(input("Dime una palabra: "))
n=len(secret)
for x in range(0,n):
    p=str(input("Dime una letra: "))
    if p in secret:
        print("La letra existe")
    else:
        print("La letra no existe")