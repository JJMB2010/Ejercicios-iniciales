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

#Codigo para observar la longitud de la contraseña
long=len(password)

if (long <= 8) and (long >= 6):
    a
