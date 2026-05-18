#Escribir una funcion que encuentre la posicion de un elemento
#especifico en una lista
#Si no se encuentra el elemento, informarlo al usuario
def encontrarPosicion(lista, elemento):
    posicion = 0
    for x in lista:
        if elemento == x:
            return posicion
        posicion += 1
    return False
    
miLista = [5, 8, 7, 9, 6, 1, 2, 9]
buscar = 99
resultado = encontrarPosicion(miLista, buscar)

if resultado:
    print("El elemento", buscar, "se encuentra en la posicion", resultado)
else:
    print("No existe el elemento en la lista")

