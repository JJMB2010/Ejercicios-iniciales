#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
x=0
while x<1:
    a=int(input("Dime un número: "))
    b=int(input("Dime otro número: "))
    print("La suma es",a+b)
    c=str(input("Quieres repetir la operación n/s: "))
    if "n" in c:
        x=1