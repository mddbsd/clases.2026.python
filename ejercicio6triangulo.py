#Realizar un programa que calcule el perimetro de un triangulo
l1 = float(input("Ingrese lado1: "))
l2 = float(input("Ingrese lado2: "))
l3 = float(input("Ingrese lado3: "))

print("El perimetro es: ", l1 + l2 + l3)

#Determninar si el triangulo es isosceles, escaleno o equilatero
# un triangulo es isoscleles cuando tiene solo 2 lados iguales
# es equilatero cuando todos los lados son iguales
# es escaleno cuando todos los lados son diferentes
# si alguno de los lados es 0 o negativo, no es un triangulo

if l1 <= 0 or l2 <= 0 or l3 <= 0:
    print("No se puede calcular")
elif l1 == l2 and l1 == l3 and l2 == l3:
    print("Es equilatero")
elif (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l2 != l1):
    print("Es iscoceles")
elif (l1 != l2 and l1 != l3 and l2 !=l3):
    print("Es escaleno")