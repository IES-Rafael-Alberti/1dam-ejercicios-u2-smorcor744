while True:
    print("Menú:")
    print("1 - Comenzar programa")
    print("2 - Imprimir listado")
    print("3 - Finalizar programa")
    
    opcion = input("Elige una opción (1, 2 o 3): ")

    if opcion == "1":
        print("Comenzando programa...")
    elif opcion == "2":
        print("Imprimiendo listado...")
    elif opcion == "3":
        print("Finalizando programa.")
        break  
    else:
        print("Opción incorrecta. Por favor, elija 1, 2 o 3.")
