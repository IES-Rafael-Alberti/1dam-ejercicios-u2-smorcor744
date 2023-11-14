def años_cumplidos(n):
    cont = 1
    cadena = ""

    while cont < n:  
        cadena += f"{cont}, "
        cont += 1

    cadena += str(n)  

    return cadena

def main():
    n = int(input("Introduce tu edad: "))
    print(f"Has cumplido {años_cumplidos(n)} años")

if __name__ == "__main__":
    main()
