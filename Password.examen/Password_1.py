#Se mostrará por pantalla las características del password que tiene que insertar
print("INTRODUCCION")
print("1. La longitud tiene que tener una longitud de 6 a 8 caracteres")
print("2. Fuerza estos valores segun la posición indicada")
print("     Posición 1 Un numero mayor o igual que 1 i menor o igual que 5")
print("     Posición 2 Una letra minúscula")
print("     Posición 3 Una Letra mayúscula")
print("     Posición 4 Uno de los siguientes símbolos *, _, @")
print("     Posición 5 Una letra minúscula")
print("     Posición 6 Un número mayor o igual a 6 y menor o igual a 9")
print("     Posición 7 Uno de los siguientes símbolos &, /, #")
print("     Posición 8 Un número menor o igual que 5")

#Pregunta asociada a la contraseña
password=input("Dime la contraseña:")

#Numero de errores iniciales
e=0

#Codigo para observar la longitud de la contraseña
long=len(password)

if (long <= 8) and (long >= 6):
#Dar valor a los 6 primeros dígitos
    p0=password[0]
    p1=password[1]
    p2=password[2]
    p3=password[3]
    p4=password[4]
    p5=password[5]
#Dar valor a todas las respuestas
    r1=("")
    r2=("")
    r3=("")
    r4=("")
    r5=("")
    r6=("")
    r7=("")
    r8=("")
#n1
    if p0.isnumeric():
        p0=int(p0)
        if 1 <= p0 <= 5:
            r1=("")
        else:
            e=int(e+1)
            r1=("Error en el carácter 1 ")

    else:
        e=int(e+1)
        r1=("Error en el carácter 1 ")
#n2  
    if p1.isalpha():
        p1=str(p1)
        if p1.islower():
            r2=("")
        else:
            e=int(e+1)
            r2=("Error en el carácter 2 ")

    else:
        e=int(e+1)
        r2=("Error en el carácter 2 ")
#n3
    if p2.isalpha():
        p2=str(p2)
        if p2.isupper():
            r3=("")
        else:
            e=int(e+1)
            r3=("Error en el carácter 3 ")

    else:
        e=int(e+1)
        r3=("Error en el carácter 3 ")
#n4
    if p3 in ("_@*"):
        r4=("")

    else:
        e=int(e+1)
        r4=("Error en el carácter 4 ")
#n5
    if p4.isalpha():
        p4=str(p4)
        if p4.islower():
            r5=("")

        else:
            e=int(e+1)
            r5=("Error en el carácter 5 ")

    else:
        e=int(e+1)
        r5=("Error en el carácter 5 ")
#n6
    if p5.isnumeric():
        p5=int(p5)
        if 6 <= p5 <= 9:
            r6=("")

        else:
            e=int(e+1)
            r6=("Error en el carácter 6 ")

    else:
        e=int(e+1)
        r6=("Error en el carácter 6 ")
#n7
    if 7 <= long <= 8:
#Dar valor al 7 dígito
        p6=password[6]

        if long == 7:
            
            if p6 in ("/#&"):
                r7=("")

            else:
                e=int(e+1)
                r7=("Error en el carácter 7 ")
#n8
        if long == 8:
#Dar valor al 8 dígito
            p7=password[7]
                        
            if p6 in ("/#&"):
                r7=("")

            else:
                e=int(e+1)
                r7=("Error en el carácter 7 ")
                            
            if p7.isnumeric():
                p7=int(p7)

                if 0 <= p7 <= 5:
                    r8=("")

                else:
                    e=int(e+1)
                    r8=("Error en el carácter 8 ")
#Respuesta final
    if e == 0:
        print("El formato del PASSWORD és correcto")
    
    else:
        print(r1+r2+r3+r4+r5+r6+r7+r8)
#Error en el numero de dígitos
else:
    print("Error, el password tiene una longitud de",long,"caracteres y no cumple los requisitos")