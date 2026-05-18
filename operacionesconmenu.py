#Combinando las estructuras while y switch (match en python)
#podemos crear un programa que se mantenga en ejecucion 
#hasta que el usuario ingrese la palabra salir
import libreria_operacionesdos as funciones
bandera = True
while bandera:
    numero1 = int(input("Ingrese numero 1: "))
    numero2 = int(input("Ingrese numero 2: "))
    print("Menú de opciones: Operaciones matematicas")
    print("sumar")
    print("restar")
    print("multiplicar")
    print("dividir")
    opcion = input("Ingrese opcion: ")
    match opcion:
        case "sumar":
            funciones.sumarDos(numero1, numero2)
        case "restar":
            funciones.restarDos(numero1, numero2)
        case "multiplicar":
            funciones.multiplicarDos(numero1, numero2)
        case "dividir":
            funciones.dividirDos(numero1, numero2)
        case "salir":
            print("programa terminado")
            bandera = False
