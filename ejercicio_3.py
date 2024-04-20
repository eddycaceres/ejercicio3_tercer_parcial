from num2words import num2words

def convertir_a_palabras(numero):
    return num2words(numero, lang='es').upper()

def main():
    try:
        numero = int(input("Ingrese un numero entero: "))
        if numero < 0:
            print("Por favor, ingrese un numero entero positivo.")
        else:
            resultado = convertir_a_palabras(numero)
            print(f"Salida: {resultado}")
    except ValueError:
        print("Ingrese un número entero válido.")

if __name__ == "__main__":
    main()
