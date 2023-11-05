def inversion(cantidad,interes,años):
    cantidad *= 1 + interes / 100 
    cadena = ""
    cont = 1
    while años >= cont:
        cantidad *= cont
        cadena = f"Has obtenido en {cont} años {cantidad}€.\n"
        cont += 1
        print(cadena)
    return ":)"

def main():
    cantidad = float(input("Introduce una cantidad a invertir: "))
    interes = float(input("Introduce el interes anual: "))
    años = int(input("Introduce el número de años: "))

    print(inversion(cantidad,interes,años))

if __name__ == "__main__":
    main()