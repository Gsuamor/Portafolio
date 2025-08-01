#Ejercicio de pagina de banco en Python en el cual es una cuenta de ahorro  con el 1% de interes en el cual se puede, depositar, retirar y consultar el saldo.
#Autor: Hildemar Hidalgo 

print("Bienvenido a la página del Banco Fondo de  Inversión Tecnológica")
print("introduzca su name id")

name_id = input()

print("----------------------------------------------------")
print("Bienvendido", name_id  + " a tu cuenta de ahorro ")

s = input("introduzca su deposito inicial: ")
s = float(s)
i = float(0.01)

print("Su saldo actual es : ", s )

print("----------------------------------------------------")

movimientos = []

while True:
    opciones = "depositar (d), retirar (r)"
    if movimientos:
        opciones += ", consultar movimientos (c)"
    opciones += ", cerrar sesión (x)"
    print(f"Indique qué desea hacer: {opciones}: ")
    option = input().lower()

    if option == "d":
        print("Indique el monto a depositar: ")
        d = float(input())
        s = (s + d) * (1 + i)
        movimientos.append(f"Depósito: +{d:.2f}, saldo: {s:.2f}")
        print("Su saldo actual es: ", s)

    elif option == "r":
        print("Indique el monto a retirar: ")
        r = float(input())
        if r <= s:
            s = (s - r) * (1 + i)
            movimientos.append(f"Retiro: -{r:.2f}, saldo: {s:.2f}")
            print("Su saldo actual es: ", s)
        else:
            print("Fondos insuficientes para retirar esa cantidad.")

    elif option == "c" and movimientos:
        print("Movimientos realizados:")
        print(f"{'Tipo':<12}{'Monto':<12}{'Saldo':<12}")
        print("-" * 36)
        for m in movimientos:
            # Separar tipo, monto y saldo usando split
            partes = m.replace("Depósito: +", "Depósito,").replace("Retiro: -", "Retiro,").replace(", saldo: ", ",").split(",")
            tipo = partes[0]
            monto = partes[1]
            saldo = partes[2]
            print(f"{tipo:<12}{monto:<12}{saldo:<12}")
        

    elif option == "x":
        print("Sesión cerrada. ¡Gracias por usar el banco!")
        break

    else:
        print("Opción no válida.")










