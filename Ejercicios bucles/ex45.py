# 45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:

a=str(input("Dime una palabra: "))
c=len(a)
p=0
rv=""
rc=""
for x in range(0,c):
    s=a[p]
    if s in "aeiouáéíóúàèìòùïü":
        rv=rv+s
    else:
        rc=rc+s
    p=p+1

print("Las vocales de la palabra abrigo son:",rv)
print("Las consonantes de la palabra abrigo son:",rc)