total_compras = 0

while True:
    monto = float(input("Ingrese el monto de la compra (o 0 para finalizar): "))
    
    if monto == 0:
        break  
    elif monto < 0:
        print("El monto ingresado es negativo. Por favor, ingrese un nuevo monto.")
    else:
        total_compras += monto  

if total_compras > 1000:
    descuento = total_compras * 0.10
    total_a_pagar = total_compras - descuento
    print(f"Total a pagar con descuento del 10%: ${total_a_pagar:.2f}")
else:
    total_a_pagar = total_compras
    print(f"Total a pagar: ${total_a_pagar:.2f}")
