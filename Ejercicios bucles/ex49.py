# 49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.

secret=str(input("Dime una palabra: "))
n=len(secret)
for x in range(0,n):
    p=str(input("Dime una letra: "))
    if p in secret:

        for x in range(0,n):
            if p in secret[x]:
                print("La palabra se encuentra en la posición",x+1)
        
    else:
        print("La letra no existe")