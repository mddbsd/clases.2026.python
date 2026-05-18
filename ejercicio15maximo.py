#Crear una funcion que encuentre el valor maximo de una lista dada
def buscarMaximo(lista):
    maximo = lista[0]
    for x in lista:
        if x > maximo:
            maximo = x
    return maximo
#prueba
#miLista = [20, 24, 54, 68, 98, 45, 14]
miLista = []
while True:
    numero = input("Ingrese numero: ")
    if numero == "salir":
        break
    miLista.append(int(numero))
    
elementoMaximo = buscarMaximo(miLista)
print("El elemnto maximo es:", elementoMaximo)

#Modificar este ejercicio para que la lista sea llenada por el usuario.
#No hay un numero maximo de numeros, el usuario deja de ingresar numeros
#cuando escribe salir