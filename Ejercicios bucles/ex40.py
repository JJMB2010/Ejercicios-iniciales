# 40. Crea un programa que cuente todos los números pares hasta el número 50.

a=int(input("Dime un número: "))

n=a+1
ni=n-a
nu=a
par=0
im=0

for x in range(ni,n):
    if nu%2==0:
        par=par+1
    else:
        im=im+1
    nu=nu-1

print("La cantidad de números pares es:",par)
print("La cantidad de números impares es:",im)