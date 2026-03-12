def math():
    """
    Ejercicio 1 - Operaciones Matemáticas

    Dado dos números enteros a y b, imprimir:
    1. La suma
    2. La diferencia
    3. El producto
    4. El promedio
    5. El cociente entero
    6. El resto de la división entera
    7. El valor real de la división
    """
    a = 57
    b = 7

    suma = a + b
    diferencia = a - b
    producto = a * b
    promedio = suma / diferencia
    cociente_entero = a // b
    resto = a % b
    valor_real = a / b

    print(f"La suma es: {suma}")
    print(f"La diferencia es: {diferencia}")
    print(f"El promedio es: {promedio}")
    print(f"El cociente es: {cociente_entero}")
    print(f"El resto es: {resto}")
    print(f"El valor real es: {valor_real}")
