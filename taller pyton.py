# Solicitar dos números enteros al usuario
numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

# Verificar que el segundo número no sea cero
if numero2 != 0:
    division_entera = numero1 // numero2
    modulo = numero1 % numero2

    print("\nResultados:")
    print("División entera (//):", division_entera)
    print("Módulo (%):", modulo)
else:
    print("Error: No se puede dividir entre cero.")
