def main():
    try:
        # Pedir al usuario que ingrese dos números
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))

        # Realizar la suma
        suma = numero1 + numero2
        resta= numero1 - numero2
        multi= numero1 * numero2
        div = numero1 / numero2
        # Mostrar el resultado
        print("La suma de {} y {} es: {}".format(numero1, numero2, suma))
        print("La resta de {} y {} es: {}".format(numero1, numero2, resta))
        print("La multiplicacion de {} y {} es: {}".format(numero1, numero2, multi))
        print("La Division de {} y {} es: {}".format(numero1, numero2, div))

    except ValueError:
        print("Error: Ingresa solo números válidos.")

def cuadrado_double(numero):
    resultado = round(numero ** 2, 2)
    return resultado


if __name__ == "__main__":
    main()

    try:
        print("--CUADRADO DE UN NUMERO--")
        num = float(input("Ingresa un número: "))

        resultado = cuadrado_double(num)

        print("El cuadrado del número es:", resultado)
    except ValueError:
        print("Error: Asegúrate de ingresar solo números válidos.")


