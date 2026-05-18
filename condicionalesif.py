#Los condicionales realizan una operación de comparación
#para determinar un resultado que puede ser verdadero o falso (booleano)
#dependiendo de este resultado, se ejecutara un bloque de codigo u otro

a = 10
b = 30
#El condicional simple solo cuenta con una salida verdadera
if b > a:
    print("b es mayor que a ")

if a > 0:
    print("a es un numero positivo")

#Tambien se pueden utilizar variables booleanas como condicion

estaLogueado = True
if estaLogueado:
    print("BIenvenido al sistema")

#El condicional doble establece bloques de codigo
#para las salida verdadera asi como para la salida falsa

if b > a:
    print("b es mayor que a")
else:
    print("b no es mayor que a")

#Podemos anidar multiples condicionales con la palabra clave
#elif

if b > a:
    print("b es mayor que a")
elif a == b:
    print("a es igual que b")
else:
    print("a es mayor que b")