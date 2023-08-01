def main():
    try:
        # Pedir al usuario que ingrese dos números
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))

        # Realizar la suma
        suma = numero1 + numero2

        # Mostrar el resultado
        print("La suma de {} y {} es: {}".format(numero1, numero2, suma))
    except ValueError:
        print("Error: Ingresa solo números válidos.")


if __name__ == "__main__":
    main()
