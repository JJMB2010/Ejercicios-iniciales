# 80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
a=list(input("Pon un decimal: "))
dec=0

for x in a:
    if str(x) in ".":
        dec=dec+1
    if str(x).isalpha():
        dec=dec+2
if dec==1:
    print("Es un decimal")
else:
    print("No es un decimal")
