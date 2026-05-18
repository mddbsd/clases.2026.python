#Realizar un programa que solicite al usuario 3 notas del 0 al 100.
#calcular el promedio de las notas y mostralo en pantalla
#Tambien mostrar los mensajes siguientes:
# si el promedio es mayor o igual a 90 mostar sobresaliente
# si el promedio es mayor o igual a 70 mostrar bueno
# si el promedio es mayor o igual a 50 mostrar regular
# en caso contrario mostrar insuficinte
nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))
nota3 = float(input("Ingrese nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3

if nota1 < 0 or nota1 > 100 or nota2 < 0 or nota2 > 100 or nota3 < 0 or nota3 > 100:
    print("Alguno de los datos es invalido")
elif promedio >= 90:
    print("Sobresaliente")
elif promedio >= 70:
    print("Bueno")
elif promedio >= 50:
    print("Regular")
else:
    print("Insuficiente")
