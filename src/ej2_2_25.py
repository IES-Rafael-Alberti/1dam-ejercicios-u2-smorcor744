frase = input("Ingresa una frase: ")
palabras = frase.split()

palabra_mas_larga = ""
cantidad_palabras = len(palabras)

for palabra in palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

print(f"La palabra más larga es: {palabra_mas_larga}")
print(f"Total de palabras en la frase: {cantidad_palabras}")
