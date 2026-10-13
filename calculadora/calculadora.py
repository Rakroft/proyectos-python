"""
Calculadora Modular en Python
Autor: Adrián Ortega Martínez (@Rakroft)
Descripción: Aplicación interactiva de consola que permite realizar 7 operaciones matemáticas
con validación de entradas numéricas y control de excepciones (ZeroDivisionError, ValueError).
"""

def mostrar_menu() -> None:
    """Muestra el menú de operaciones disponibles."""
    print("\n" + "=" * 45)
    print("        MENÚ DE OPERACIONES MATEMÁTICAS      ")
    print("=" * 45)
    print(" 1. Suma (+)")
    print(" 2. Resta (-)")
    print(" 3. Multiplicación (*)")
    print(" 4. División (/)")
    print(" 5. División entera (//)")
    print(" 6. Potencia (**)")
    print(" 7. Resto módulo (%)")
    print("=" * 45)

def calcular(operacion: int, num1: float, num2: float) -> float:
    """
    Realiza la operación seleccionada sobre los operandos proporcionados.
    """
    if operacion == 1:
        return num1 + num2
    elif operacion == 2:
        return num1 - num2
    elif operacion == 3:
        return num1 * num2
    elif operacion == 4:
        return num1 / num2
    elif operacion == 5:
        return num1 // num2
    elif operacion == 6:
        return num1 ** num2
    elif operacion == 7:
        return num1 % num2
    else:
        raise ValueError("Operación fuera de rango.")

def main() -> None:
    print("¡Bienvenido a la Calculadora Modular en Python!")
    
    while True:
        mostrar_menu()
        
        # Selección de la operación con validación de rango (1-7)
        while True:
            try:
                operacion = int(input("¿Qué operación quieres realizar (1-7)?: "))
                if operacion in range(1, 8):
                    print(f"Has escogido la opción {operacion}. ¡Perfecto!")
                    break
                else:
                    print("Error: Selecciona un número válido del menú (1 al 7).")
            except ValueError:
                print("Error: Debes ingresar un número entero válido.")

        # Entrada de operandos con validación de tipo y división por cero
        while True:
            try:
                num1 = float(input("\nIntroduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))

                # Verificación de división entre cero para operaciones 4 (/), 5 (//) y 7 (%)
                if operacion in [4, 5, 7] and num2 == 0:
                    print("Error matemático: No se puede dividir entre 0. Elige otro número para el segundo operando.")
                    continue
                break
            except ValueError:
                print("Error: Debes introducir valores numéricos válidos (usa punto '.' para decimales).")

        # Cálculo y visualización del resultado
        try:
            resultado = calcular(operacion, num1, num2)
            print("-" * 45)
            # Mostrar resultado formateado (entero si no tiene decimales)
            if resultado.is_integer():
                print(f"✅ El resultado de tu operación es: {int(resultado)}")
            else:
                print(f"✅ El resultado de tu operación es: {resultado:.4f}".rstrip('0').rstrip('.'))
            print("-" * 45)
        except Exception as e:
            print(f"Ha ocurrido un error inesperado al calcular: {e}")

        # Preguntar al usuario si desea continuar
        continuar = input("\n¿Deseas realizar otra operación? (s/N): ").strip().lower()
        if continuar not in ("s", "si", "y", "yes"):
            print("\n¡Hasta la próxima! Espero haberte ayudado. 👋")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nOperación cancelada por el usuario. ¡Hasta pronto!")
