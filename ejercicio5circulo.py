#Realizar un programa que calcule el area y perimetro de un circulo
import math
radio = int(input("Ingrese radio: "))

perimetro = 2 * math.pi * radio
area = math.pi * (radio * radio)

print("El area es;" ,area)
print("El perimetro es: ", perimetro)