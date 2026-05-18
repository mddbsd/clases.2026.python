#Los bucles se utilizan para ejecutar una serie de instrucciones
#siempre que una condicion sea verdadera.
#Existen 2 tipos de bucles en python, while y for
print("Ejemplo 1")
i = 1
while i < 6:
    print(i)
    i = i + 1

#Este bucle while se repetira siempre que la condicion sea verdadera
#Podemos interrumpir el bucle utilizando la sentencia break
print("ejemplo 2: break")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#Con la sentencia continue podemos detener el ciclo actual y continuar con el siguiente
print("Eje,plo 3: continue ")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#La sentencia else nos permite ejecutar un bloque de codigo
#Una vez que la condicion ya no es mas verdadera
print("Ejemplo 4: else")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i ya no es menor a 6")