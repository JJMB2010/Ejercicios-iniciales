#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
x=0
st=0
r=0
while x<1:
    a=int(input("Dime un número: "))
    b=int(input("Dime otro número: "))
    print("La suma es",a+b)
    st=st+a+b
    r=r+1
    c=str(input("Quieres repetir la operación n/s: "))
    if "n" in c:
        x=1
        print("La suma total es:",st," y el número de repeticiones es:",r)