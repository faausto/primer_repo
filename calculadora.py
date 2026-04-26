import os

def limpiar():
    os.system('cls')

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except:
            print("Error: ingreso invalido")

while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")

    if not opcion.isdigit():
        print("Error: ingreso invalido")
        input("Presione una tecla para continuar")
        limpiar()
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: opcion fuera de rango")
        input("Presione una tecla para continuar")
        limpiar()
        continue

    if opcion == 5:
        print("Saliendo del programa")
        break

    num1 = obtener_numero("Ingrese el primer numero: ")
    num2 = obtener_numero("Ingrese el segundo numero: ")

    if opcion == 1:
        print("Resultado:", num1 + num2)
    elif opcion == 2:
        print("Resultado:", num1 - num2)
    elif opcion == 3:
        print("Resultado:", num1 * num2)
    elif opcion == 4:
        if num2 == 0:
            print("Error: no se puede dividir por 0")
        else:
            print("Resultado:", num1 / num2)

    input("Presione una tecla para continuar")
    limpiar()