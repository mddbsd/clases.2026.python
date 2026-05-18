#En programación los tipos de datos (datatypes) son un concepto muy importante, ya que 
#cada tipo de dato puede hacer diferntes cosas.
#Las variables pueden almacenar datos de diferentes tipos, y python tiene por defecto
#los siguientes tipos en estas categorias:

#    Cadena/Texto       str
#    numerico           int, float, complex
#    secuencia          list, tuple, range
#    booleano           bool
#    Sin Tipo           NoneType

x = 10
print(type(x))
x = "Hola Mundo"
print(type(x))
x = 3.14
print(type(x))
x = '100'
print(type(x))
x = ["rojo", "verde", "azul"]
print(type(x))
x = ("mesa", "silla", "banco")
print(type(x))
x = True
print(type(x))
x = None
print(type(x))

#Si bien no es necesario definir el tipo de dato de la variable, este se puede especificar
#utilizando funciones de construccion

x = str("Hola mundo")
print(type(x))
x = str(9)
print(type(x))