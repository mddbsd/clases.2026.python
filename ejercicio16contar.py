#Escribir una funcion que cuente cuantas veces
#aparece un elemento especifico en una lista

def contarElemento(lista, elemento):
    contador = 0
    for x in lista:
        if x == elemento:
            contador += 1
    return contador
#prueba
#miLista = [4, 5, 6, 3, 5, 4, 4, 7, 6, 8 ,7]
miLista = []
while True:
    numero = input("Ingrese numero: ")
    if numero == "salir":
        break
    miLista.append(int(numero))
elemento = int(input("Ingrese numero a contar: "))
resultado = contarElemento(miLista, elemento)
print("El elemento", elemento, "se repite", resultado, "veces")

#Modificar este ejercicio para que el usuario llene la lista (ingresa numeros hasta que ingrese salir)
#y que tambien permita ingresear el elemento a buscar