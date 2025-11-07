# 36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.

numb=int(input("Dime un numero: "))
n=numb
s=0
for x in range(numb):
    s=n+s
    n=n-1

print(s)