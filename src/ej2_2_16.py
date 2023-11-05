mayor_numero = None

while True:
    numero = int(input("Ingresa un número entero positivo (o 0 para terminar): "))

    if numero == 0:
        break
    elif numero > 0:
        if mayor_numero is None or numero > mayor_numero:
            mayor_numero = numero

if mayor_numero is not None:
    print(f"El mayor número ingresado fue: {mayor_numero}")
else:
    print("No se ingresaron números positivos.")
