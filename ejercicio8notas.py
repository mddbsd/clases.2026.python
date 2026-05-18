#Realizar un programa que solicite al usuario 3 notas del 0 al 100.
#calcular el promedio de las notas y mostralo en pantalla
#Tambien mostrar los mensajes siguientes:
# si el promedio es mayor o igual a 90 mostar sobresaliente
# si el promedio es mayor o igual a 70 mostrar bueno
# si el promedio es mayor o igual a 50 mostrar regular
# en caso contrario mostrar insuficinte
def validarNota(n):
    while n < 0 or n > 100:
        n = float(input("Nota invalida, intente nuevamente: "))

nota1 = float(input("Ingrese nota 1: "))
validarNota(nota1)
nota2 = float(input("Ingrese nota 2: "))
validarNota(nota2)
nota3 = float(input("Ingrese nota 3: "))
validarNota(nota3)

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 90:
    print("Sobresaliente")
elif promedio >= 70:
    print("Bueno")
elif promedio >= 50:
    print("Regular")
else:
    print("Insuficiente")
