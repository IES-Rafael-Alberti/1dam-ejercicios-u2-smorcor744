pares_total = 0
impares_total = 0

while True:
    numero = int(input("Ingresa un número entero positivo (o 0 para terminar): "))
    
    if numero == 0:
        break
    elif numero < 0:
        print("El número ingresado no es positivo.")
    else:
        pares = 0
        impares = 0
        numero_actual = numero

        while numero_actual > 0:
            digito = numero_actual % 10
            if digito % 2 == 0:
                pares += 1
            else:
                impares += 1
            numero_actual //= 10

        print(f"El número {numero} tiene {pares} dígito(s) par(es) y {impares} dígito(s) impar(es).")

        pares_total += pares
        impares_total += impares

print(f"Total de dígitos pares leídos: {pares_total}")
print(f"Total de dígitos impares leídos: {impares_total}")
