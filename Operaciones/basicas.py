def main():
    try:
        # Pedir al usuario que ingrese dos números
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))

        # Realizar la suma
        suma = numero1 + numero2
        resta= numero1 - numero2
        multi= numero1 * numero2
        # Mostrar el resultado
        print("La suma de {} y {} es: {}".format(numero1, numero2, suma))
        print("La resta de {} y {} es: {}".format(numero1, numero2, resta))
        print("La multiplicacion de {} y {} es: {}".format(numero1, numero2, multi))
    except ValueError:
        print("Error: Ingresa solo números válidos.")


if __name__ == "__main__":
    main()
