
entrada01 = input("Ingrese el primer valor booleano (True/False): ")
entrada02 = input("Ingrese el segundo valor booleano (True/False): ")


valor1 = entrada1 == "True"
valor2 = entrada2 == "True"


resultadoand = valor1 and valor2
resultadoor = valor1 or valor2
resultado_not_valor1 = not valor1
resultado_not_valor2 = not valor2


print("\nResultados:")
print("Valor 1:", valor1)
print("Valor 2:", valor2)
print("AND:", resultado_and)
print("OR:", resultado_or)
print("NOT valor1:", resultado_not_valor1)
print("NOT valor2:", resultado_not_valor2)

