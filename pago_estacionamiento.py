def pago_estacionamiento():
    total = 0

    # Solicitar el total a cobrar hasta que sea un valor válido y esté dentro del rango permitido
    while total <= 0 or total > 75:
        total_input = input("Introduce el total a cobrar por el estacionamiento (hasta 75): ")
        try:
            total = float(total_input)
        except ValueError:
            print("Error: Ingrese un número válido.")
            continue

        if total <= 0:
            print("El total a cobrar debe ser mayor que cero. Por favor, ingrese un valor válido.")
        elif total > 75:
            print("El total a cobrar no puede exceder los 75. Por favor, ingrese un valor válido.")

    pago = 0

    # Solicitar el monto pagado hasta que sea suficiente y esté dentro del rango permitido
    while pago < total or pago > 150:
        pago_input = input("Introduce el monto que paga el cliente (hasta 150): ")
        try:
            pago = float(pago_input)
        except ValueError:
            print("Error: Ingrese un número válido.")
            continue

        if pago < total:
            print("El monto pagado es insuficiente. Por favor, pague el monto total del estacionamiento.")
        elif pago > 150:
            print("El monto pagado no puede exceder los 150. Por favor, ingrese un valor válido.")

    # Calcular el cambio y los billetes/monedas a entregar
    cambio = pago - total

    denominaciones = [
        ("billete de 100 dólares", 100),
        ("billete de 50 dólares", 50),
        ("billete de 20 dólares", 20),
        ("billete de 10 dólares", 10),
        ("billete de 5 dólares", 5),
        ("billete de 2 dólares", 2),
        ("billete de 1 dólar", 1),
        ("moneda de 50 centavos de dólar", 0.5),
        ("moneda de 25 centavos de dólar", 0.25),
        ("moneda de 10 centavos de dólar", 0.1),
        ("moneda de 5 centavos de dólar", 0.05),
        ("moneda de 1 centavo de dólar", 0.01)
    ]
    billetes_entregados = []
    monedas_entregadas = []
    for denominacion, valor in denominaciones:
        cantidad = int(cambio / valor)
        cambio -= cantidad * valor
        if valor >= 1:
            billetes_entregados.append((denominacion, cantidad))
        else:
            monedas_entregadas.append((denominacion, cantidad))

    # Mostrar los resultados
    print("\n=== Resultados ===")
    print("Total a cobrar: {:.2f} dólares".format(total))
    print("Monto pagado: {:.2f} dólares".format(pago))
    print("Cambio: {:.2f} dólares".format(pago - total))
    print("Billetes a entregar:")
    for denominacion, cantidad in billetes_entregados:
        print("- {}: {}".format(denominacion, cantidad))
    print("Monedas a entregar:")
    for denominacion, cantidad in monedas_entregadas:
        print("- {}: {}".format(denominacion, cantidad))
    total_billetes = sum(cantidad for _, cantidad in billetes_entregados)
    total_monedas = sum(cantidad for _, cantidad in monedas_entregadas)
    print("Total de billetes a entregar: {}".format(total_billetes))
    print("Total de monedas a entregar: {}".format(total_monedas))
pago_estacionamiento()
