# 76. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.

lista1=["a","b","D","x","r","X","3","h","w","2","i"]
t=0
n=0
l=0
m=0
s=0

for x in lista1:
    t=t+1
    if x.isnumeric():
        n=n+1
        s=s+int(x)
    if x.isalpha():
        l=l+1
        if x.isupper():
            m=m+1
            

print("Número de valores:",t)
print("Cantidad de números:",n)
print("Cantidad de letras:",l)
print("Cantidad de mayúsculas:",m)
print("Suma total de números:",s)