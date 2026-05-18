#Realizar un programa que solicite al usuario una cantidad de dolares
#y mediante una funcion retornar su monto en pesos
def convertirAPesos(dolares, cotizacion):
    return dolares * cotizacion

dolares = float(input("Ingrese cantidad de dolares: "))
cotizacion = float(input("Ingrese cotizacion: "))

print("La cantidad de pesos es:", convertirAPesos(dolares, cotizacion), "$")