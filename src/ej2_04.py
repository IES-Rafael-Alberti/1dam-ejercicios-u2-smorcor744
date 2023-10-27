"""
Ejercicio 2.1.4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""
def numero():
    n1 = int(input("Escribe un número entero:")) 
    return n1
def par_impar(n1):
    if n1%2 != 0:
        return False
    else:
        return True

def main():
    n1 = numero()

    if par_impar(n1):
        print("Es par.")
    else:
        print("Es impar.")


if __name__ == "__main__":
    main()
