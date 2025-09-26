#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
import math

men=int(input("dime cuantos adultos hay: "))
minimen=int(input("dime cuantos niños hay: "))

precio=10.8*men
miniprecio=6*minimen

print("El precio total del cine para ",minimen," menor/es es:",miniprecio)
print("El precio total del cine para ",men," adulto/s es:",precio)