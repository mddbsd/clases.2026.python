mes = input("Ingrese numero del mes: ")
bandera = True
while bandera:
    match mes:
        case "1":
            print("Enero")
            bandera = False
        case "2":
            print("Febrero")
            bandera = False
        case "3":
            print("Marzo")
            bandera = False
        case "4":
            print("Abril")
            bandera = False
        case "5":
            print("Mayo")
            bandera = False
        case "6":
            print("Junio")
            bandera = False
        case "7":
            print("Julio")
            bandera = False
        case "8":
            print("Agosto")
            bandera = False
        case "9":
            print("Septiembre")
            bandera = False
        case "10":
            print("Octubre")
            bandera = False
        case "11":
            print("Noviembre")
            bandera = False
        case "12":
            print("Diciembre")
            bandera = False
        case _:
            mes = input("Mes incorrecto, ingrese nuevamente: ")