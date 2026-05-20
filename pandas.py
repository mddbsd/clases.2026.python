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