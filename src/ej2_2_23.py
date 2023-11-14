lineas_completas = 0

while True:
    linea = input("Libro: ")
    
    if linea == "*":
        break
    elif "/" in linea:
        digitos_total = 0
        titulos = linea.split("/")
        
        for titulo in titulos:
            digitos = sum(1 for caracter in titulo if caracter.isdigit())
            digitos_total += digitos

        print(f"Línea completa. Aparecen {digitos_total} dígitos numéricos.")
        lineas_completas += 1

print(f"Fin. Se leyeron {lineas_completas} líneas completas.")
