#Las funciones, también conocidas como métodos, son bloques de código reutilizable
#diseñados para realizar una tarea especifica, y pueden ser reutilizados en diferentes
#partes del programa.
#Sirven para dividir el código en partes mas pequeñas y manejables
#Normalente estan compuesta por un identificador y argumentos entre parentesis

def sumarDos(n1, n2):
    print(n1 + n2)

nota1 = 5
nota2 = 8

sumarDos(nota1, nota2)
sumarDos(20, 30)

n1 = 90
n2 = 50

sumarDos(n1, n2)

#En Python creamos funciones con la palabra clave def seguido del nombre de la funcion (identificador)
#Entre los parentesis definimos los parametros de la funcion, que obtendrán los valores de los argumentos
#enviados al momento de invocarla

a = int(input("ingrese nota1: "))
b = int(input("ingrese nota2: "))
c = int(input("ingrese nota3: "))

def promedio(nota1, nota2, nota3):
    prom = (nota1 + nota2 + nota3) / 3
    print(prom)

promedio(a, b, c)

#Las funciones tambien pueden devolver un valor en el lugar
#donde fueron invocadas, lo hacemos con la palabra clave return
#Es imporante aclarar que el programa debe procesar de alguna manera
#este retorno, imprimendolo, almacenandolo en una variable, etc

def promedioConRetorno(a, b, c):
    return (a + b + c) / 3

promedio = promedioConRetorno(a, b, c)

print("El promedio regresado fue:", promedio)