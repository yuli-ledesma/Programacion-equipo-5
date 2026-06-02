while True:
    try:
    # Mostrar menu
    print("Selecciona la opcion que deseas realizar")
    print("1- Calcular comision")
    print("2- Ver recibos de sueldo de vendedores (Admin)")
    print("3- Salir")
    opc = int(input("Opcion: "))

    # Ralizar accion del menu
    match opc:
        case 1:
            print("|------------------|")
            print("calcular comision")
            print("|------------------|")
        case 2:
            print("|------------------|")
            print("Ver recibos")
            print("|------------------|")
        case 3:
            print("|------------------|")
            print("Saliendo...")
            print("|------------------|")
            exit()
            break
        case _:
            print ("Error: Debes de ingresar una opcion valida (1,2 0 3).")
        
        except ValueError:
            print ("Error: Debes ingresar un número entero.")

