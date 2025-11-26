sp=0
sn=0
m=0

for x in range(0,7):
    a=int(input("Dime un numero: "))
    if a < 0:
        sn=sn+a
    else:
        sp=sp+a
    if a>100:
        m=m+1

print("Suma positivos:",sp)
print("Suma negativos:",sn)
print("Mayores que 100:",m)