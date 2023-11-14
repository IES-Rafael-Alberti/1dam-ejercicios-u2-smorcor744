"""
Ejercicio 2.1.6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""
def datos():
    nombre = input("Introduce tu nombre: ")
    sexo = input("Introduce tu orientación sexual(hombre o mujer): ")
    return nombre, sexo

def grupoA(nombre,sexo):
    sexo = str(sexo).upper()
    nombre = str(nombre).upper()
    if sexo == "MUJER" and nombre[0] < "M":
        return True
    elif sexo == "HOMBRE" and nombre[0] < "N":
        return True
    else:
        return False

def main():
    nombre, sexo = datos()

    if grupoA(nombre,sexo):
        print("Perteneces al Grupo A.")
    else:
        print("Perteneces al Grupo B.")


if __name__ == "__main__":
    main()
