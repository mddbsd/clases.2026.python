#Instalacion de pandas:
#Para instalar pandas primero tenemos que aseguras de que este instalado
#el gestor de paquetes de python PIP.
#podemos reconocer su instalacion escribiendo pip en la terminal (puedes una terminal del vscode)
#si no esta instalado, hay que descargar el scrip y guardarlo en un archivo
#    Invoke-webRequest -Uri 'https://bootstrap.pypa.io/get-pip.py' -OutFile 'get-pip.py'
#Este comando, lee un archivo de la web y lo escribe. con la primera opcion -Uri
#indicamos la direccion remota del archivo, y la segunda opcion -OutFile lo escribe con el nombre 
#que se le dio como argumento
#Cabe destacar que este archivo se guarda en el directorio donde se ejecuto el comando
#Una vez finalizada la descarga, ejecutamos el script con el siguitente comando
#   py get-pip.py
#Esto instala pip en el sistema.
#El ultimo paso es instalar pandas
#python -m pip install pandas
#Una vez cumplidos estos requerimientos, ya podemos importa pandas a nuestros programas

#PANDAS es la libreria por excelencia, de python para manipulacion y analisis de datos.
#Proporciona esctructuras rápidas y flexibles que hacen que trabajar con datos estructurados (tablas, series, etc..)
#sea mas sencillo e intuitivo.
import pandas as pd
#Estructuras principales
#Series: es una columna unica (1D), como una lista con indice:
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)
#Dataframe: es la estructura que mas vamos a utilizar. 
#           Es una tabla completa (2D) como una hoja de calculo
df = pd.DataFrame({
    "Nombre": ["Marcelo", "Susana", "Mirtha"],
    "Edad": [57, 79, 99],
    "Ciudad": ["Buenos Aires", "Punta del Este", "Miami"]
})
print(df)
#Cargar datos: Los datos que queremos analizar, suelen estar
#              en bases de datos o archivos. Estos pueden ser
#              .cvs .json .xlsx o una consulta SQL
#df = pd.read_excel("archivo.xslx")
#df = pd.read_cvs("archivo.svs")
#df = pd.read_sql("SELECT * FROM tabla", conexion)
df = pd.read_json("libros.json")
#Primer vistazo al dataframe.
print(df)
#Si imprimimos el df directamente, se vera la estructura completa
#del mismo, pero pandas nos da funciones para analizarlo por partes
print("Muestra las primeras 5 filas", df.head())
print("Muestra las ultimas 3 filas", df.tail(3))
print("Muestra columnas, tipos y nulos", df.info())
print("Muestra estadisticas descriptivas",df.describe())
print("Conteo de Filas y columnas",df.shape)
print("Nombres de las columnas", df.columns)

#Seleccion y filtrado
#Seleccionar una columnas
filtroTitulo = df["titulo"]
print("titulo", filtroTitulo)

#seleccionar multiples columnas
filtroTituloPrecio = df[["titulo", "stock"]]
print(filtroTituloPrecio)

#filtrar filas con expresiones
preciosMenores12 = df[df["precio"] < 12]
print("Se muestran los precios menores a 12", preciosMenores12)

fantasiaMayores12 = df[(df["precio"] > 12) & (df["genero"] == "Fantasía")]
print("Titulos de genero fantasía con precios mayores a  12", fantasiaMayores12)