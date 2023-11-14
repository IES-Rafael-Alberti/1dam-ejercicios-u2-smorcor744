def triangulo(n):
    cont = 1 
    cadena = ""
    while cont <= n:
        cadena = "*" * cont
        cont += 1
        print(cadena)
    return ""


def main():
    n = int(input("Introduce un número: "))

    print(triangulo(n))

if __name__ == "__main__":
    main()
    