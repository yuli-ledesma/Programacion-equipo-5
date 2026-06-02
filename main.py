def mostrar_liquidacion():
    pass

def calcular_comision(monto_total):
    if monto_total <= 100000:
        comision = monto_total * 0.05
    if monto_total > 100000 and monto_total <= 300000:
        comision = monto_total * 0.10
    if monto_total > 300000:
        comision = monto_total * 0.15
    return comision

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
            nombre_vendedor= input("Ingrese su nombre:")
            cantidad_ventas= int(input("Ingrese la cantidad de ventas realizadas:"))
            monto_total= float(input("Ingrese el monto total de las ventas:"))
            comision = calcular_comision(monto_total)
            print(f"El vendedor {nombre_vendedor} ha realizado {cantidad_ventas} ventas por un monto total de ${monto_total:.2f}. Su comisión es de ${comision:.2f}.")
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

