#En cualquier programa, se suele solicitar al usuario que ingrese información,
#Esta info que se ingresa se debe almacenar en una variable.
#Para que el usuario ingrese datos usamos la función input()
print("Ingrese su nombre")
x = input()
print("Buenos dias", x )

y = input("Ingrese su edad")
print("Te llamas", x, "y tenes", y , "años de edad")

#El valor que devuelve la funcion input es del tipo str
#Si queremos procesar estos valores en operaciones matematicas
#tenemos que hacer un "casting"
#Casting es el proceso de cambiar un tipo de dato a otro

base = int(input("Ingrese base: "))
altura = int(input("Ingrese altura: "))
area = base * altura
print("El area es", area)
