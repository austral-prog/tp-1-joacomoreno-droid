def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100

    impuesto = precio_base * 0.21
    subtotal = precio_base + monto_impuesto
    propina = subtotal * 0.10
    precio_final = subtotal + propina
    
    print(f"El monto del impuesto: {impuesto}")
    print(f"El subtotal: {subtotal}")
    print(f"El monto de la propina: {propina}") 
    print(f"El precio final: {precio_final}")
