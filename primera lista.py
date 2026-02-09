
lista1 = []
cantidad1 = int(input("¿Cuántos elementos tendrá la primera lista?: "))

for i in range(cantidad1):
    elemento = input(f"Ingrese el elemento {i + 1} de la primera lista: ")
    lista1.append(elemento)


lista2 = []
cantidad2 = int(input("\n¿Cuántos elementos tendrá la segunda lista?: "))

for i in range(cantidad2):
    elemento = input(f"Ingrese el elemento {i + 1} de la segunda lista: ")
    lista2.append(elemento)


concatenada = lista1 + lista2
veces = int(input("\n¿Cuántas veces desea repetir la primera lista?: "))
repetida = lista1 * veces


print("\nResultados:")
print("Primera lista:", lista1)
print("Segunda lista:", lista2)
print("Concatenación:", concatenada)
print("Repetición de la primera lista:", repetida)
