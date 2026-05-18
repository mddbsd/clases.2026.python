#Las colecciones (Arrays) son estructuras de datos que, a diferencia de las variables, permiten
#almacenar multiples datos con un solo identificador.
#Cada uno de estos datos es identificado internamente con un numero de indice.
#Podemos imaginar las colecciones como un tren: Este tiene un nombre y cada uno de los vagones un numero de indice
#Los vagones pueden almacenar distintos tipos de datos
#En python existen 4 tipos de colecciones, cada una con diferentes caracteristicas:
#Listas (List): colecciones ordenadas y modificables, permiten elementos duplicados
#Tuplas (Tuple): colecciones ordenadas y NO modificables, permite elementos duplicados
#Series (Set): es una coleccion desordenada, NO modificable (los elementos son no modificables) y no indexada, no permite elementos duplicados
#Diccionarios (Dictionary): coleccion ordenada (a partir de Python version 3.7) y modificable, no permite elementos duplicados
#Al momento de elegir un tipo de coleccion, es importante entender las propiedades de dicho tipo. Elegir el tipo correcto para una serie de datos, permite la retencion de su significado
#y podria incrementar eficiencia y seguridad

#Listas: son creadas utilizando corchetes []
miLista = ["Manzana", "Uva", "Limón", "Mandarina"]

#Los items son ordenados, modificables y permiten valores duplicados
#Indexado: Los items estan indexados, el primer elemento tiene un indice [0], el segundo un idice [1], etc...
#Ordenado: Decimos que las listas son ordenadas, los items tienen un orden definido y este no cambia. Si agregamos un nuevo item,
#          este se colocara al final de la lista
#Modificable: Las listas permiten agregar o quitar items, despues de su creación
#Permite duplicados: ya que los items estan indexados, podemos tener multiples items con el mismo valor

miLista = ["Manzana", "Cereza", "Uva", "Mandarina", "Uva"]
print("Mostrar miLista:")
print(miLista)
print()
print("Podemos ver el tamaño de la lista con la función len()")
print(len(miLista))
print()
#Las listas permiten distintos tipos de datos
lista1 = ["Susana", "Marcelo", "Pepe"]
lista2 = [10, 25, 18, 99]
lista3 = [True, False, False]

#A su vez, una lista puede combinar multiples tipos de datos

lista4 = ["VW", 2015, "golf", True]

print("Accedemos a los items invocando a la lista con su indice")
print(lista1[1])
print(lista2[3])
print(miLista[0])
print()
print("indexado negativo: utilizar indices negativos, significa que se comienza desde el final hacia el principio")
print(lista1[-1])
print()
print("Se pueden mostrar rangos utilizando el operador : dentro del indice, [posicion_inicial:posicion_final] como posicion final se toma la longitud, no el indice")
lista5 = ["rojo", "amarillo", "verde", "azul", "naranja", "violeta", "blanco", "turquesa"]
print(lista5[3:7])
print("Si excluimos la posicion incial, esta se tomara desde el principio de la lista. Notar que naranja no se incluyo")
print(lista5[:4])
print()
#Cada uno de los indices puede ser tratado como una variable independiente, por lo que podemos cambiar sus valores
otraLista = ["Argentina", "Uruguay", "España", "Mexico"]
print("Lista original: ", otraLista)
otraLista[2] = "Japon"
print("Elemento cambiado: ", otraLista)
print("Podemos cambiar los valores  de un rango especifico")
otraLista[1:3] = ["Paraguay", "Brazil"]
print("Rango modificado: ", otraLista)
print()
print("Para insertar un nuevo item al final de la lista se utiliza la funcion append()")
otraLista.append("Venezuela")
print(otraLista)
print()
print("Es posible insertar un elemento en cualquier lugar de la lista con la funcion insert()")
#independientemente de donde se inserte el elemento, la lista sigue ordenada
otraLista.insert(1, "Portugal")
print(otraLista)
print()
print("Podemos anexar otra lista a la lista actual con la funcion extend()")
lista1.extend(lista2)
print(lista1)
print()
print("Para eliminar elementos de la lista podemos usar el valor o el indice, dependiendo el metodo utilizado")
print("Lista original:", miLista)
miLista.remove("Uva")
print("remove() elimina la primera ocurrencia del argumento encontrado: ", miLista)
miLista.pop(2)
print("pop() elimina el elemnto con el indice que se indica en su argumento", miLista)
#Si no especificamos un indice, pop() elimina el último
print("del puede eliminar una lista completa, o tambien se puede utilizar como pop() especificando un indice")
del miLista[1]
print("indice 1 eliminado con del", miLista)
del miLista 
#print(miLista) marca error ya que la lista dejo de existir
print()
print("con el metodo clear() podemos vaciar una lista sin eliminarla")
lista1.clear()
print("lista1 vacia:", lista1)
print()
#Recorriendo la lista
print("Se utilizan bucles para recorrer los diferentes tipos de diccionarios, aqui utilizamos el bucle for")
for x in otraLista:
    print(x, end=" ")
print()
#Con este bucle se repite un bloque de código mientras existan elementos en la lista. La sintaxis consta de
#la palabra clave for seguido de una variable auxiliar luego la palabra clave in y por ultimo la lista a recorrer
#Cada uno de los elementos de la lista se irá alamacenando en la variable x y esta se utiliza dentro de al estructura
#Veamos un ejemplo utilizando acumuladores

listaNumeros = [2, 5, 8, 9, 7, 3, 4]
acumulador = 0
for i in listaNumeros:
    acumulador += i
    print("Valor parcial: ", acumulador)
print("Acumulacion de numeros: ", acumulador)