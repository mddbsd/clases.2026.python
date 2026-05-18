#Escribe un programa que pregunte el nombre del usuario 
#y un numero entero e imprima en lineas distintas el nombbre
#del usuario tantas veces como el numero introducido

#nombre = input("Ingrese nombre: ")
#ciclos = int(input("Ingrese cantidad de ciclos: "))

#for x in range(ciclos):
#    print(nombre)

##Escribe un programa que solicite un usuario y contraseña.
#Si las credenciales coinciden, mostrar el mensaje "Bienvenido al sistema"
#Caso contrario mostrar el mensaje "Credenciales incorrectas"
#Las credenciales las define el programador

#usuario = "admin"
#password = "123456"

#usuarioIngresado = input("Ingrese usuario: ")
#passwordIngresado = input("Ingrese contraseña: ")

#if usuario == usuarioIngresado and password == passwordIngresado:
    #print("Bienvenido al sistema")
#else:
    #print("Credenciales incorrectas")

#Expandir el ejercicio anterior para que se le permita al usuario
#3 intentos de ingreso. Mostrar tambien el numero de intento

#usuario = "admin"
#password = "123456"
#contador = 0

#while True:
#    usuarioIngresado = input("Ingrese usuario: ")
#    passwordIngresado = input("Ingrese contraseña: ")

#    if usuario == usuarioIngresado and password == passwordIngresado:
#        print("Bienvenido al sistema")
#        break
#    elif contador < 3:
#        print(f"Credenciales incorrectas, intento {contador + 1} de 3")
#        contador += 1
#    else:
#        print("Intentos agotados")
#        break
#Crear una lista de compras: El usuario puede ingresar multiples elementos
#con su nombre y precio, No se sabe cuantos elementos hay, el usuario
#termina de ingresarlos con la palabra terminar en el ingreso del producto
#Al final mostrar la lista de productos con sus precios y el total

#listaProductos = []
#listaPrecios = []
#while True:
#    productoNombre = input("Ingrese producto: ")
#    if productoNombre == "terminar":
#        break
#    productoPrecio = float(input("Ingrese precio: "))
#    listaProductos.append(productoNombre)
#    listaPrecios.append(productoPrecio)

#contador = 0
#acumulador = 0

#for x in listaProductos:
#    print(f"Producto: {x} Precio:{listaPrecios[contador]}$")
#    acumulador += listaPrecios[contador]
#    contador += 1
#print(f"El total es: {acumulador}$")

#Combinar el ejercicio de login con el de productos
#Presentarle al usuario la pantalla de login, si las credenciales
#son correctas se le aplicara un descuento del 20% al total
#sino, se mostrara el precio sin descuento

usr = "admin"
pwd = "12345"
esVip = False
usrIngresado = input("Ingrese usuario: ")
pwdIngresada = input("Ingrese contraseña: ")
if usrIngresado == usr and pwdIngresada == pwd:
    print("El usuario es VIP, tiene descuento del 20%")
    esVip = True
else:
    print("Usuario publico, sin descuento")

listaProductos = []
listaPrecios = []
while True:
    productoNombre = input("Ingrese producto: ")
    if productoNombre == "terminar":
        break
    productoPrecio = float(input("Ingrese precio: "))
    listaProductos.append(productoNombre)
    listaPrecios.append(productoPrecio)

contador = 0
acumulador = 0

for x in listaProductos:
    print(f"Producto: {x} Precio:{listaPrecios[contador]}$")
    acumulador += listaPrecios[contador]
    contador += 1

if esVip:
    print(f"Total: {acumulador - (acumulador * 0.20)} con descuento")
else:
    print(f"Total: {acumulador} sin descuento")

#Otra manera de expresar el total con f-strings
#print(f"Total: {acumulador if not esVip else acumulador-(acumulador * 0.20)}")

#Crear una funcion para cada uno de los ejercicios en esete archivo, y luego permitir al usuario
#que elija cual ejercicio quiere probar