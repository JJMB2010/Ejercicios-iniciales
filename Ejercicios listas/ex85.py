# 85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos.

i=[]
cat=[]
cas=[]
x=0
inte=0

while x ==0:
    dd=str(input("Nombre del alumno: "))
    a=float(input("Inglés:"))
    i.append(a)
    b=float(input("Caste:"))
    cas.append(b)
    c=float(input("Cata:"))
    cat.append(c)
    x=int(input("Quieres seguir(s=0),(n=1): "))
    inte=inte+1
print("RESUMEN")
print("La media de inglés es de:",(sum(i)/inte))
print("La media de castellano es de:",(sum(cas)/inte))
print("La media de catalán es de:",(sum(cat)/inte))
if inte%2!=0:
    inte=inte-1
    if inte==0:
        print("La mediana en inglés es:",i)
        print("La mediana de caste es:",cas)
        print("La mediana de cata es:",cat)
    else:
        for g in range(0,inte-1):
            i.pop(0)
            i.reverse()
            cas.pop(0)
            cas.reverse()
            cat.pop(0)
            cat.reverse()
        print("La mediana de inglés es:",i)
        print("La mediana de caste es:",cas)
        print("La mediana de cata es:",cat)
else:
    for g in range(0,inte-2):
        i.pop(0)
        i.reverse()
        cas.pop(0)
        cas.reverse()
        cat.pop(0)
        cat.reverse()
    print("La mediana de inglés es:",sum(i)/2)
    print("La mediana de caste es:",sum(cas)/2)
    print("La mediana de cata es:",sum(cat)/2)
