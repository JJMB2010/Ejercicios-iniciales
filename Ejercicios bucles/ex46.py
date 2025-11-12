# 46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.

a=str(input("Dime una palabra: "))
c=len(a)
p=0
rv=""
rc=""
a=a.lower()
for x in range(0,c):
    s=a[p]
    if s in "aeiouáéíóúòìùèà":
        rv=rv+s
    else:
        rc=rc+s
    p=p+1

print("Las vocales de la palabra abrigo son:",rv)
print("Las consonantes de la palabra abrigo son:",rc)