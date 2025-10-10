
nombre=input("introduce tu nombre:")
edad=int(input("Introduce tu edad: "))
nombre=str.upper(nombre)
if edad>0 and edad<100:
    año_actual=int(2025)
    futuro=año_actual+(100-edad)
    print("Hola",nombre,"cumpliras 100 años en el año",futuro)
else:
    print("Edad no valida")