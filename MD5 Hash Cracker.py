# Importamos las 2 librerías que nos harán falta para este proyecto
import hashlib
import pyfiglet

# Creamos un Banner para nuestro programa ayudándonos de Pyfiglet
banner = pyfiglet.figlet_format("Russoski Tools \n MD5 Cracker")
print(banner)

# Generamos una variable para almacenar la ruta y lectura del diccionario utilizado
# Generamos una variable para solicitar al usuario el Hash que desee crackear
archivo = open("common.txt", "r")
hash_solicitado = str(input('-> Introduce el Hash a crackear: '))

# Creamos un bucle For que recorrerá cada línea del diccionario de contraseñas utilizado
# Se cogerá cada palabra, se codificará en formato MD5 y se almacenará en Hash_obtenido
for linea in archivo.readlines():
    hash_codificado = hashlib.md5(linea.strip().encode())
    hash_obtenido = hash_codificado.hexdigest()
    # Si la variable Hash_obtenido tiene el mismo valor que lo que introdujo el usuario,
    # la contraseña habrá sido encontrada con éxito y se imprimirá por pantalla
    if hash_obtenido == hash_solicitado:
        print("------------------------------------------------------------------")
        print("<ESTELA> encontró la siguiente Contraseña: " + linea.strip())
        print("------------------------------------------------------------------")
        exit(0)