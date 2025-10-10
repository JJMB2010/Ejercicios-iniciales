
f=str(input("Dime una frase: "))
a=float(input("Dime un numero: "))
b=float(input("Dime un numero: "))
c=float(input("Dime un numero: "))

print("La frase en minusculas es:",(str.lower(f)))
print("La suma es:",a+b+c)
print("la media es:",(a+b+c)/3)
print("el producto es:",a*b*c)
if (a+b+c) < (a*b*c):
    print("la suma es mayor que el producto: false")
else:
    print("la suma es mayor que el producto: true")