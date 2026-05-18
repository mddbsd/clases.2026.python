#Juan Perez adquirio recientemente un terreno en la zona de
#lanus. Desea conocer su area y su perimetro.
#Realizar un programa que solicite base y altura, y luego
#que calcule el area y el perimetro. 
altura = int(input("Ingrese altura: "))
base = int(input("Ingrese base: "))
perimetro = 2 * (base + altura)
area = base * altura
print("El area es: ", area, "m2")
print("El perimetro es: ", altura, "m")

#Se estima que el valor por m2 en lanus es de U$D350
#Calcular el precio del terreno

print("El valor del trreno es: ", area * 350, "U$D")
