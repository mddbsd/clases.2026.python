#Crear un programa que solicite al usuario los valores de temperatura
#de la semana y luego calcular el promedio. Utilizar listas, acumuladores y bucle for}
tempSemana = []
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
contador = 0
while True:
    if contador == 7:
        break
    tempSemana.append(float(input("Ingrese temperatura del dia " + str(dias[contador]) + ": ")))
    contador += 1
print(tempSemana)
acumulador = 0
for x in tempSemana:
    acumulador += x
print("El promedio semanal es:", acumulador / 7)