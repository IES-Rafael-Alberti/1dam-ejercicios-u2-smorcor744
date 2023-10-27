"""
Ejercicio 2.1.5
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""
def datos():
    edad = int(input("Introduce tu edad: "))
    ingresos = int(input("Introduce tus ingresos mensuales: "))
    return edad, ingresos

def siono(edad,ingresos):
    if edad > 16 and ingresos >= 1000 :
        return True
    else:
        return False

def main():
    edad, ingresos = datos()

    if siono(edad,ingresos):
        print("Tienes que tributar.")
    else:
        print("No tienes que tributar.")


if __name__ == "__main__":
    main()
