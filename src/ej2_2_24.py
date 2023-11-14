def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    for i in range(3, int(numero**0.5) + 1, 2):
        if numero % i == 0:
            return False

    return True

cantidad_primos = 0

while True:
    numero = int(input("Ingresa un número mayor que 1 (o 0 para terminar): "))
    
    if numero == 0:
        break
    elif numero <= 1:
        print("El número ingresado debe ser mayor que 1.")
    else:
        if es_primo(numero):
            cantidad_primos += 1

print(f"Se ingresaron {cantidad_primos} número(s) primo(s).")
