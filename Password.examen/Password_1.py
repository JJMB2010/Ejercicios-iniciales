#Se mostrará por pantalla las características del password que tiene que insertar
print("INTRODUCCION")
print("1. La longitud tiene que tener una longitud de 6 a 8 caracteres")
print("2. Fuerza estos valores segun la posición indicada")
print("     Posición 1 Un numero mayor o igual que 1 i menor o ogual que 5")
print("     Posición 2 Una letra minúscula")
print("     Posición 3 Una Letra mayúscula")
print("     Posición 4 Uno de los siguientes símbolos *, _, @")
print("     Posición 5 Una letra minúscula")
print("     Posición 6 Un número mayor o igual a 6 y menor o igual a 9")
print("     Posición 7 Uno de los siguientes símbolos &, /, #")
print("     Posición 8 Un número menor o igual que 5")

#Pregunta asociada a la contraseña
password=input("Dime la contraseña:")

p0=password[0]
p1=password[1]
p2=password[2]
p3=password[3]
p4=password[4]
p5=password[5]
p6=password[6]
p7=password[7]

#Codigo para observar la longitud de la contraseña
long=len(password)

if (long <= 8) and (long >= 6):
        
    if p0.isnumeric():
        p0=int(p0)
        if 1 <= p0 <= 5:
            r1=("")
        else:
            r1=("Error en el carácter 1")

    else:
        r1=("Error en el carácter 1")
        
    if p1.isalpha():
        p1=str(p1)
        if p1.islower():
            r2=("")
        else:
            r2=("Error en el carácter 2")

    else:
        r2=("Error en el carácter 2")

    if p2.isalpha():
        p2=str(p2)
        if p2.isupper():
            r3=("")
        else:
            r3=("Error en el carácter 3")

    else:
        r3=("Error en el carácter 3")
    
    if p3.isalpha():
        p3=str(p3)
        if p3.islower():
            r4=("")
        else:
            r4=("Error en el carácter 4")

    else:
        r4=("Error en el carácter 4")

else:
    print("Error, el password tiene una longitud de",long,"caracteres y no cumple los requisitos")