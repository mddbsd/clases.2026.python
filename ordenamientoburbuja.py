#EL ordenamiento burbuja (Bubble Sorting) es un algoritmo
#que ordena una coleccion de numeros de menor a mayor
#La palabra burbuja surge de la manera en que el algoritmo trabaja
#hace que los valores mas grandes "burbujeen" hacia arriba
#Mecanismo:
#El algoritmo sigue 4 pasos:
#   1: Recorrer la coleccion, un valor a la vez
#   2: Por cada valor, comparar el siguiente
#   3: Si el valor es mas grande que el siguiente, intercambiarlos
#   4: Recorrer la coleccion mientras esta tenga valores
#
#Simulacion:
#Antes de implementar el algoritmo de burbujeo en python, vamos a hacer
#una simulacion manual para darnos una idea de como trabaja
#
#Paso 1: Comenzamos con una lista desordenada
# [7, 12, 9, 11, 3]
#Paso 2: Tomamos los 2 primeros valores y los comparamos. El siguiente, es mayor al primero? si, por lo tanto se quedan igual.
# [(7, 12), 9 ,11, 3]
#Paso 3: Avazanamos en la coleccion y tomamos los valores 12 y 9, el siguiente, es mayor al primero? no
# [7, (12, 9), 11, 3]
#Paso 4: Intercambiamos los valores para que el mayor quede a la derecha
# [7, (9, 12), 11, 3]
#Paso 5: Avanzamos y tomamos los valores 12 y 13
# [7, 9, (12, 11), 3]
#Paso 6: Intercambiamos los valores para que el mayor quede a la derecha
# [7, 9, (11, 12), 3]
#Paso 7; Tomamos los valores 12
# [7, 9 ,11 ,(12, 3)]
#paso 8: 12 es mayor a 3, asi que se intercambian.
# [7, 9, 11, (3, 12)]
#Repetir hasta que no queden mas valores a ordenar
#Para implementarlo en codigo, necesitamos lo siguiente:
# 1: Un array con valores a ordenar
# 2: Un bucle interno que recorra el array e intercambie los valores
#    si el siguiente es mayor al primero. Este bucle deve recorrerse
#    un valor menos por cada repeticion.
# 3: Un bucle externo que controle cuantas veces debe recorrer el bucle interno
#    Para una lista de n valores, este bucle externo debe recorrer n-1 veces

miLista = [64, 34, 25, 12, 22, 11, 90, 5]
#Alamcenar longitud de la listaprint(n)
print("Lista desordenada:", miLista)
n = len(miLista)
for i in range(n - 1): #la funcion range crea un rango de numeros entre 0 y el valor que le entregamos como agumento:
    for j in range(n - i -1 ):
        if miLista[j] > miLista[j + 1]:
            miLista[j], miLista[j + 1] = miLista[j +  1], miLista[j]
print("Lista ordendada con bubble sort:", miLista)

#Mejora del ordenamiento burbuja
#Este algorimo se puede mejorar un poco. Imaginemos que la lista
#se encuentra casi ordenada desde el principio
# [7, 3, 9, 12, 11]
#En este caso, la lista queda ordenada desde la primera vuelta, pero
#el algorimo continuara corriendo sin intercambiar elmentos lo que lo hace
#ineficiente.
#Si el algoritmo recorre la lista sin intercambiar valores, el array ya debe estar ordenado,
#y podemos detener el algorimo de esta manera:
i = 0
j = 0
miLista1 = [7, 3, 9, 12, 11]
n = len(miLista1)
for i in range(n -1):
    intercambiado = False
    for j in range(n - i - 1):
        if miLista1[j] > miLista1[j + 1]:
            miLista1[j], miLista1[j + 1] = miLista1[j + 1], miLista1[j]
            intercambiado = True
    if not intercambiado:
        break
print("Lista ordenada con bubble sort optimizado:", miLista1)
miLista2 = [23, 2, 54, 12, 8, 7]
miLista2.sort()
print("Lista ordenada con sort:", miLista2)