#primer proyecto en py

# para empezar el codigo tenemos que importar la libreria random y string

import random as r
import  string as s

#creamos un diccionario para almacenar y asociar la url larga con la corta
url_larga_a_corta = {}
url_corta_a_larga = {}

#crear variable de caracteres posibles y base de url corta
CARACTERES_POSIBLES = s.ascii_letters + s.digits
base_url_corta = "http://tuacortador.com/"

#Ahora creamos una funcion que sirva como una secuencia aletoria de caracteres asegurando su unicidad antes de devolverla

# implementamos un bucle while para verificar si el codigo generado ya existe si existe genera un nuevo codigo hasta que sea unico
def generar_codigo_corto(longitud=6):
  while True:
    codigo_corto = "".join(r.choice(CARACTERES_POSIBLES) for _ in range(longitud))
    # Verifico si el código ya existe en url_corta_a_larga
    if codigo_corto not in url_corta_a_larga:
      return codigo_corto

# ahora creamos una funcion que tome una url larga genere una url corta y los almacene en ambos diccionarios que creamos anteriormente
def acortar_url(url_larga):
    # 1. Verificar si url_larga ya existe
    if url_larga in url_larga_a_corta:
        return url_larga_a_corta[url_larga]

    # 2. Generar un código corto único
    codigo_corto = generar_codigo_corto()

    # 3. Construir la URL corta completa
    url_corta = base_url_corta + codigo_corto

    # 4. Almacenar el mapeo en ambos diccionarios
    url_larga_a_corta[url_larga] = url_corta
    url_corta_a_larga[url_corta] = url_larga

    # 5. Retornar la URL corta generada
    return url_corta

#despues de creamos una funcion que tome una url corta y devuelva la url larga original asociada

def obtener_url_original(url_corta):
    # 1. Busca la url_corta como clave en el diccionario url_corta_a_larga
    if url_corta in url_corta_a_larga:
        # 2. Si la url_corta se encuentra, retorna la url_larga asociada
        return url_corta_a_larga[url_corta]
    else:
        # 3. Si no se encuentra, retorna un mensaje de error
        return "URL corta no encontrada."

#ahora creamos la interfaz del menu con el bucle while
print("\n--- Bienvenido al Acortador de URLs ---")

while True:
    print("\n--- Menú Acortador de URLs ---")
    print("1. Acortar una URL")
    print("2. Visitar una URL corta")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        url_larga_input = input("Ingrese la URL larga que desea acortar: ")
        url_corta_generada = acortar_url(url_larga_input)
        print(f"URL corta generada: {url_corta_generada}")
    elif opcion == '2':
        url_corta_input = input("Ingrese la URL corta que desea visitar: ")
        url_original = obtener_url_original(url_corta_input)
        print(f"URL original: {url_original}")
    elif opcion == '3':
        print("¡Gracias por usar el acortador de URLs! ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo con 1, 2 o 3.")