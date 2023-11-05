numeros_pares = 0

while True:
    numero = int(input("Ingresa un número entero positivo (o -1 para terminar): "))

    if numero == -1:
        break  
    if numero < 0:
        print("El número ingresado no es positivo.")
        continue  

    suma_digitos = 0
    numero_original = numero

    while numero > 0:
        digito = numero % 10  
        suma_digitos += digito  
        numero //= 10  

    print(f"La suma de los dígitos de {numero_original} es: {suma_digitos}")

    if suma_digitos % 2 == 0:
        numeros_pares += 1

print(f"Total de números pares ingresados: {numeros_pares}")
