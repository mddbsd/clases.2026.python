#La estructura switch selecciona uno o más bloques de codigo para ser ejecutado
#Esta estructura ejecuta los bloques que coincidan con una expresion
#Es una alternativa mas legible que anidar muchos condicionales if, especialmente
#cuando manejamos multiples valores posibles.
#En Python, no existia esta estructura hasta la version 3.10, que implemento
#un switch llamado "coincidencia de patron estructural" (structural pattern matching)
#se utiliza con las palabras clave match y case

lenguaje = input("que lenguaje queres aprender? ")

match lenguaje: #match compara el valor de la variable lenguaje con diferentes casos
    case "javascript": #en caso de que la variable tenga el valor javascript, se ejecutara este bloque de codigo
        print("Estudias para desarrollador web")

    case "python":
        print("Estudias como cientifico de datos")

    case "php":
        print("Estudias para desarrollo de backend")

    case "solidity":
        print("Estudias para desarrollo de blockchain")

    case "java":
        print("Estudias desarrollo de aplicaciones")

    case _ : #En caso de que no exista una coincidencia, se ejecuta este bloque por defecto
        print("El lenguaje no importa, lo que importa es resolver problemas")