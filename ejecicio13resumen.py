#Crear una libreria de funciones que permita realizar 
#los siguientes calculos:
#   area de recangulo
#   perimetro de rectangulo
#   area de circulo
#   permietro de circulo
#   tipo de triangulo
#El programa principal debe mostrar un menu
#y una opcion de salida
import libreria_calculos as calculos
print("Bienvenido al ejercicio")
print("Ingrese una opcion: ")
while True:
    print("1: Operaciones de circulo")
    print("2: Operaciones de rectangulos")
    print("3: Operaciones de triangulo")
    print("4: Salir")
    opcion = input()
    match opcion:
        case "1":
            radio = float(input("Ingrese radio: "))
            print("Que desea calcular?")
            print("1: area")
            print("2: perimetro")
            opcionCirculo = input()
            match opcionCirculo:
                case "1":
                    print("El area es:", calculos.areaCirculo(radio))
                case "2":
                    print("El perimetro es:", calculos.perimetroCirculo(radio))
                case _:
                    print("Error!")
        case "2":
            base = float(input("Ingrese base: "))
            altura = float(input("Ingrese altura"))
            print("Que desea calcular?")
            print("1: area")
            print("2: perimetro")
            opcionRectangulo = input()
            match opcionRectangulo:
                case 1:
                    print("El area es:", calculos.areaRectangulo(base, altura))
                case 2:
                    print("El perimetro es:",calculos.perimetroRectangulo(base, altura))
                case _:
                    print("Error!")
        case "3":
            lado1 = float(input("Ingrese lado 1: "))
            lado2 = float(input("Ingrese lado 2: "))
            lado3 = float(input("Ingrese lado 3: "))
            calculos.tipoTriangulo(lado1, lado2, lado3)

        case "4":
            print("Hasta luego!")
            break
        case _:
            print("opcion incorrecta, intente nuevamente")