#Password_v2
error=0

print("Buenos dias, has sido seleccionado para llevar a cabo el testeo de este creador de contraseñas: ")
print("")
print("1. La contraseña debe tener 3 números.")
print("2. La contraseña debe tener 3 letras, 2 mayúsculas y una minúscula.")
print("3. La contraseña debe tener 2 símbolos.")
print("4. La contraseña debe tener 2 números entre el 0 y el 3.")
print("5. La contraseña debe tener 3 números iguales a 5.")
print("6. La contraseña debe tener 1 número igual o superior a 8.")
print("7. La contraseña debe tener 1 @.")
print("")

for x in range(0,3):
    n=0
    l=0
    ll=0
    s=0
    pos=0
    #Aquí añadiremos nuevas variables:
    a=0
    max=0
    min=0
    mid=0
    r=""
    r1=""
    r2=""
    r3=""
    r4=""
    r5=""
    r6=""
    rl=""

    pas=str(input("Dime una contraseña: "))
    print("")
    leng=len(pas)

    #Aquí hay unas contraseñas para poder testear mi código:
    #  1. pPPpPBHJojphu, Bhjuvuiv, YBvyvjkbybju
    #  2. 234b8HBy6, 32h89fhfb2, d7g21873gfr1
    #  3. 27BNdbqi(%), 3hR(sw57HOs), 3snio/kH79Bui3
    #  4. (/)/(Y(/&$R%E@))), """""@@@@@@@", /%&$@@#€#¬
    #  5. 358358358, 84325765887, 5782346589
    #  6.  ,     ,,
    #  7. 27BNdbqi(%), """""@@@@@@@", 358358358
    #  8. HHHhhh&&&@259, IHhuHh·%&@2598,"@2HHl5ai/()9
    #  9. IHhuHh·%&@2598, 234b8HBy6, YBvyvjkbybju
    #  10. "@2HHl5ai/()9,,     a

    for i in range(0,leng):
        p=pas[pos]

        if p.isalpha():
            if p.islower():
                l=l+1
            if p.isupper():
                ll=ll+1
        elif p.isnumeric():
            n=n+1
            if float(p) <= 3:
                min=min+1
            if float(p) == 5:
                mid=mid+1
            if 8 <= float(p):
                max=max+1
        else:
            s=s+1
            if str(p) in "@":
                a=a+1
        pos=pos+1
    
    if (n>=3)and(l>=1)and(ll>=2)and(s>=2)and(a>=1)and(min>=2)and(mid>=3)and(max>=1):
        print("La contraseña es correcta")
    else:
        error=error+1
        if n < 3:
            r="El número de números es incorrecto, porque " + str(n)  + " no es igual o mayor que 3 "
        if l < 1:
            r1="El número de letras es incorrecto, porque " + str(l) + " no es igual o mayor que 3 "
        if ll < 2:
            rl="El número de letras mayúsculas es incorrecto, porque " + str(ll) + " no es igual o mayor que 2"
        if s < 2:
            r2="El número de simbolos es incorrecto, porque " + str(s) + " no es igual o mayor que 2 "
        if a < 1:
            r3="Te falta el símbolo secreto "
        if min < 2:
            r4="La cantidad de números menores es insuficiente "
        if mid < 3:
            r5="La cantidad de números medianos es insuficiente "
        if max < 1:
            r6="La cantidad de números mayores es insuficiente "
        
    
    rf=((r+r1+rl+r2+r4+r5+r6+r3)[:-1])
    print("")

print("Hay "+str(error)+" errores.")
print("Hay "+str(3-error)+" aciertos.")

# RESUMEN
# Prueba 1:
# El número de números es incorrecto, porque 0 no es igual o mayor que 3 El número de simbolos es incorrecto, 
# porque 0 no es igual o mayor que 2 La cantidad de números menores es insuficiente La cantidad de números 
# medianos es insuficiente La cantidad de números mayores es insuficiente Te falta el símbolo secreto.
# 1. Esta prueba me ha servido para poder asegurarme de que mi código puede decir que las letras mayusculas y minusculas son letras.

# Prueba 2:
# El número de simbolos es incorrecto, porque 0 no es igual o mayor que 2 La cantidad de números medianos es 
# insuficiente Te falta el símbolo secreto. El número de simbolos es incorrecto, porque 0 no es igual o mayor 
# que 2 La cantidad de números medianos es insuficiente Te falta el símbolo secreto. El número de simbolos es 
# incorrecto, porque 0 no es igual o mayor que 2 La cantidad de números medianos es insuficiente Te falta el 
# símbolo secreto.
# 2. Esta prueba me ha servido para poder ver como el programa discierne entre números y letras.

# Prueba 3:
# El número de números es incorrecto, porque 2 no es igual o mayor que 3 La cantidad de números menores es 
# insuficiente La cantidad de números medianos es insuficiente La cantidad de números mayores es insuficiente 
# Te falta el símbolo secreto. La cantidad de números menores es insuficiente La cantidad de números medianos 
# es insuficiente La cantidad de números mayores es insuficiente Te falta el símbolo secreto. El número de 
# simbolos es incorrecto, porque 1 no es igual o mayor que 2 La cantidad de números medianos es insuficiente 
# Te falta el símbolo secreto.
# 3. Esta prueba me ha servido para poder ver si el código puede ver letras, números y símbolos.

# Prueba 4:
# El número de números es incorrecto, porque 0 no es igual o mayor que 3 La cantidad de números menores es 
# insuficiente La cantidad de números medianos es insuficiente La cantidad de números mayores es insuficiente. 
# El número de números es incorrecto, porque 0 no es igual o mayor que 3 El número de letras es incorrecto, 
# porque 0 no es igual o mayor que 3 La cantidad de números menores es insuficiente La cantidad de números 
# medianos es insuficiente La cantidad de números mayores es insuficiente. El número de números es incorrecto, 
# porque 0 no es igual o mayor que 3 El número de letras es incorrecto, porque 0 no es igual o mayor que 3 La 
# cantidad de números menores es insuficiente La cantidad de números medianos es insuficiente La cantidad de 
# números mayores es insuficiente.
# 4. Esta prueba me ha permitido comprender como mi código puede discernir entre diferentes símbolos y "@".