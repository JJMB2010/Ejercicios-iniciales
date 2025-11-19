#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While
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
        print("Fin del programa")
        x=1