#Python introdujo en su version 3.6 las llamadas F-Strings
#Estas permiten dar formato a ciertas partes del texto.
#para especificar un string como f-string simplemente agregamos
#una f al comienzo del valor literal
cadena = f"Esta cadena literal es un f-string"
print(cadena)
#Marcadores y modificadores
#Para formatear valores, un f-string agrega marcadores {}, estos contienen
#variables, operaciones, funcines y modificadores para dar formato a la cadena
correo = "marcelo@gmail.com"
cadena = f"El e-mail de marcelo es {correo}"
print(cadena)
#Un marcador tambien puede incluir un modificador para formatear el valor
#un modificador se incluye agregando : seguido de un formateo legal como .2f
#que significa un numero con punto fijo de 2 decimales
precio = 2.35678
cadena = f"El precio es {precio:.2f} dolares"
print(cadena)
#Tambien se puede formatear un valor directamente sin alamacenarlo 
#en una variable
cadena = f"El precio es {35.98547:.3f} dolares"
print(cadena)
#Operacion dentro del f-string
#Se pueden realizar operaciones matematicas dentro de los marcadores
#y devolver el resultado
cadena = f"El precio es {3 * 15} dolares"
print(cadena)
precio = 200
iva = 0.21
cadena = f"El precio + iva es {precio + (precio * iva)} pesos"
print(cadena)
#se pueden utilizar condicionales dentro de los marcadores
precio = 60
cadena = f"Es muy {'Caro' if precio > 50 else 'Barato'}"
print(cadena)
#Ejecutar funciones
#Podemos invocar funciones dentro del f-string, como por ejemplo
#pa funcion upper() que convierte los valores a mayusculas
pais = "argentina"
cadena = f"Mi pais es {pais.upper()}"
print(cadena)
#Tambien funciona con funciones definidas por nosotros
def conversor(millas):
    return millas * 1.6093

cadena = f"El auto recorrio {conversor(30):.2f} kilometros"
print(cadena)
#Hay muchos modificadores que se pueden utilizar para dar formato a los valores
# como por ejemplo, la , sirve para separar las unidades de 1000
precio = 59000
cadena = f"El precio es {precio:,} pesos"
print(cadena)
#Lista de operadores
#   :<     Alinea a la izquierda (dentro del espacio disponible)
#   :>     Alinea a la derecha  (dentro del espacio disponible)
#   :^     Alinea al centro
#   :=     Coloca el signo en la posicion mas a la izquierda
#   :+     Utiliza un signo + para indicar si un resultado es positivo o negativo
#   :-     Utiliza el signo - solo para resultados negativos
#   :      Utiliza un espacio para insertar un espacio extra antes de los numeros positivos (y un signo - antes de los numeros negativos)
#   :,     Separador de 1000 con coma
#   :_     Separador de 1000 con guion bajo
#   :b     Formateo binario
#   :d     Formateo decimal
#   :f     Numero de punto fijo
#   :o     Formateo octal
#   :x     Formateo hexadecimal
#   :%     Formateo en porcentaje

#Pruebas: Crear multples cadenas utilizando, los operadores
#de la lista

a = 20
cadena = f"El valor {a} en binario es {a:b}"
print(cadena)

cadena = f"Alinea a la derecha {a:>}"
print(cadena)

cadena = f"Alinea a la izquierda {a:<}"
print(cadena)