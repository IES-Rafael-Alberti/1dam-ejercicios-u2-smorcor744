"""
Ejercicio 2.1.2
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
contraseña = "usuario"
def pedircontra():
    contra = input("Introduce la contraseña: ")
    contra = contra.upper()
    return contra

def igual(contraseña,contra):
    contraseña = "usuario"
    contraseña = contraseña.upper()
    if contraseña.upper() == contra:
        return True
    else:
        return False

def main():
    contra = pedircontra()

    if igual(contraseña,contra):
        print("La contraseña es correcta.")
    else:
        print("Incorrecto.")


if __name__ == "__main__":
    main()
