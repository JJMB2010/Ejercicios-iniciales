#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
x=0
st=0
r=0
while x<1:
    a=int(input("Dime un número: "))
    b=int(input("Dime otro número: "))
    print("La suma es",a+b)
    st=st+a+b
    r=r+1
    print("La suma total es:",st," y el número de repeticiones es:",r)
    if st>50:
        if st % 2 != 0:
            print("Fin del programa")
            x=1