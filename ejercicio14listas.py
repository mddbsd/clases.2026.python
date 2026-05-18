#Crear un programa que solicite al usuario los valores de temperatura
#de la semana y luego calcular el promedio. Utilizar listas, acumuladores y bucle for}
import os
def dias(dia):
    match dia:
        case 0:
            return "Lunes"
        case 1:
            return "Martes"
        case 2:
            return "Miercoles"
        case 3:
            return "Jueves"
        case 4:
            return "Viernes"
        case 5:
            return "Sabado"
        case 6:
            return "Domingo"
os.system("clear")
temeperaturasSemana = []
contador = 0
while True:
    if contador == 7:
        break
    temeperaturasSemana.append(float(input("Ingrese temperatura del día " + dias(contador) + ": ")))
    contador += 1
    os.system("clear")

print("|L\t|M\t|M\t|J\t|V\t|S\t|D\t|")
acumulador = 0
for i in temeperaturasSemana:
    print("|" + str(i) + "°C", end="\t")
    acumulador += i
print("\n")
print("Temperatura promedio de la semana: ", acumulador / 7)