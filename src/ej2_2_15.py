sumatoria = 0

while True:
    numero = int(input("Ingresa un número entero (o 0 para terminar): "))
    
    if numero == 0:
        break 
    elif numero > 0:
        sumatoria += numero  

print(f"La sumatoria de los números positivos ingresados es: {sumatoria}")
