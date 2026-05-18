#Solicitar al usuario que ingrese su edad
#con un if mostrar el mensaje "niño" si la edad es menor a 13
#agregar un elif  para mostrar el mensaje "adolecente" si la edad es menor a 18
#agregar un else para mostrar el mensaje "adulto" 
edad = int(input("Ingrese edad: "))
if edad <= 13:
    print("niño")
elif edad <= 18:
    print("adolecente")
else:
    print("adulto")