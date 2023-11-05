pasware = "usuario"

while True:
    pas = input("Introduce la contraseña:")
    if pas == pasware:
        print("Contraseña correcta.")
        break
    else:
        print("Contraseña incorrecta.")