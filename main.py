while True:
    # Mostrar menu
    print("Selecciona la opcion que deseas realizar")
    print("1) Calcular comision")
    print("2) Ver recibos de sueldo de vendedores (Admin)")
    print("3) Salir")
    opc = int(input("Opcion: "))

    # Ralizar accion del menu
    match opc:
        case 1:
            print("calcular comision")
        case 2:
            print("Ver recibos")
        case 3:
            print("Saliendo...")
            exit()

