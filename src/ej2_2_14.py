sumatoria = 0

while True:
    numero = int(input("Ingresa un número entero (o 0 para terminar): "))
    
    if numero == 0:
        break  
    else:
        sumatoria += numero  

print(f"La sumatoria de los números ingresados es: {sumatoria}")
