def cuenta_atras(n):
    cadena = ""

    while n != 0:  
        cadena += f"{n}, "
        n -= 1

    cadena += str(n)  

    return cadena


def main():
    n = int(input("Introduce un número entero: "))
    print(cuenta_atras(n))

if __name__ == "__main__":
    main()