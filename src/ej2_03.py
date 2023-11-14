"""
Ejercicio 2.1.3
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""
def numero():
    n1 = int(input("Escribe un número:")) 
    n2 = int(input("Escribe otro número:"))
    return n1, n2

def division(n1,n2):
    if n2 != 0:
        divi = n1/n2
        return divi
    else:
        return print("error")

def main():
    n1, n2 = numero()
    print(division(n1,n2))


if __name__ == "__main__":
    main()
