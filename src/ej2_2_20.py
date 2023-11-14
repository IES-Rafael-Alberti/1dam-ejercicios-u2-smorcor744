frase = input("Ingresa una frase: ")
letra_buscada = input("Ingresa una letra a buscar: ")

for posicion, caracter in enumerate(frase):
    if caracter == letra_buscada:
        print(f"Se encontró la letra '{letra_buscada}' en la posición {posicion}.")
        break
    else:
        print(f"No hay coincidencia en la posición {posicion}.")
