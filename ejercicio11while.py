#Realizar uhn programa que solicite numeros al usuario
#y termine cuando el numero ingresado sea 99
#numero = int(input("ingrese numero: "))
bandera = False
while not bandera:
    numero = int(input("ingrese numero: "))
    if numero == 99:
        bandera = True
print("Fin del programa")