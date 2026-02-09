
numero1 = float(input("Ingrese el primer número decimal: "))
numero2 = float(input("Ingrese el segundo número decimal: "))


potencia = numero1 ** numero2


redondeonumero1 = round(numero1)
redondeonumero2 = round(numero2)
redondeopotencia = round(potencia, 2)  

print("\nResultados:")
print("Potencia (numero1 ** numero2):", potencia)
print("Redondeo del primer número:", redondeonumero1)
print("Redondeo del segundo número:", redondeonumero2)
print("Potencia redondeada a 2 decimales:", redondeopotencia)
