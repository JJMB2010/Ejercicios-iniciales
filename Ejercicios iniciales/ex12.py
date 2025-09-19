# 12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
import math

var1=int(input("dime la altura:"))
var2=int(input("dime la base menor:"))
var3=int(input("dime la base mayor:"))
var4=int(input("dime el lado:"))

per=var4*2+var3+var2
area=(var2+var3)*var1/2

print("el perimetro es",per)
print("el area es",area)