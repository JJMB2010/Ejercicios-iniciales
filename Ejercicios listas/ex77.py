# 77. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.

lista1=["a","b","D","x","r","X","3","h","w","2","i"]
num=[]
let=[]

for x in lista1:
    if x.isnumeric():
        num.append(x)
    if x.isalpha():
        let.append(x)
a=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: "))
if a==1:
    let.sort(key=str.lower)
    num.sort()
    print(num)
    print(let)
else:
    let.sort(reverse=True, key=str.lower)
    num.sort(reverse=True)
    print(num)
    print(let)
