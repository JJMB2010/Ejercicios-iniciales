# 72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista.

x=0
lista=[]
ex=("áéíóú")
ab=("aeiou")
while x == 0:
    y=1
    while y != 0:
        b=input("Dime una letra: ")
        if b.isalpha():
            if b in ex:
                v=ex.find(b)
                b=ab[v]
                lista.append(str(b))
            else:
                lista.append(str(b))
            y=0
    c=str(input("Quieres seguir (s/n): "))
    if c in ("Nn"):
        x=1
lista=list(set(lista))
print(lista)