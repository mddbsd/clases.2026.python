def sumarDos(n1, n2):
    print("La suma es:", n1 + n2)

def restarDos(n1, n2):
    print(n1 - n2)

def multiplicarDos(n1, n2):
    print(n1 * n2)

def dividirDos(n1, n2):
    print(n1 / n2)

#Solicitar al usuario que ingrese 2 numeros y luego
#realizar las operaciones matematicas basicas llamando
#a las funciones

numero1 = int(input("ingrese numero1: "))
numero2 = int(input("ingrese numero2: "))

sumarDos(numero1, numero2)
restarDos(numero1, numero2)
multiplicarDos(numero1, numero2)
dividirDos(numero1, numero2)