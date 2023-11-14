numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("El número ingresado no es positivo.")
else:
    suma_digitos = 0
    while numero > 0:
        digito = numero % 10  
        suma_digitos += digito  
        numero //= 10  

    print(f"La suma de los dígitos es: {suma_digitos}")
