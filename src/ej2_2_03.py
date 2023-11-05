def numero_impar(n):
    cont = 1
    cadena = ""

    while cont < n:  
        cadena += f"{cont}, "
        cont += 2

    cadena += str(n)  

    return cadena


def main():
    n = int(input("Introduce un número entero: "))
    print(numero_impar(n))

if __name__ == "__main__":
    main()