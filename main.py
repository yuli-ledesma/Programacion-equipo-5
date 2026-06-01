while True:
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

