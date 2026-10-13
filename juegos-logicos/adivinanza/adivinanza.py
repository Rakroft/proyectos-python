"""
Juego de Adivinanza Numérica
Autor: Adrián Ortega Martínez (@Rakroft)
Descripción: Juego interactivo en consola con generación pseudoaleatoria de números
entre 1 y 1000, gestión configurable de intentos (1 a 6) y pistas dinámicas de rango.
"""

import random
import sys

def main() -> None:
    print("=" * 55)
    print("           JUEGO DE LA ADIVINANZA NUMÉRICA         ")
    print("       Desarrollado en Python por Adrián Ortega    ")
    print("=" * 55)

    # Confirmación inicial de partida
    while True:
        try:
            jugar = int(input("¿Quieres jugar?: Sí (1) / No (2): ").strip())
            if jugar == 1:
                print("\n¡Adelante! Vamos a configurar la partida.")
                break
            elif jugar == 2:
                print("\n¡Nos vemos pronto! 👋")
                sys.exit(0)
            else:
                print("Opción inválida. Digita 1 para jugar o 2 para salir.")
        except ValueError:
            print("Entrada inválida. Introduce 1 o 2.")

    # Generación del número secreto entre 1 y 1000
    numero_secreto = random.randint(1, 1000)

    # Configuración de número de intentos permitidos (entre 1 y 6)
    while True:
        try:
            intentos_totales = int(input("\n¿Cuántos intentos crees que necesitas (entre 1 y 6)?: ").strip())
            if 1 <= intentos_totales <= 6:
                print(f"Tienes {intentos_totales} intentos disponibles. ¡A por ello!")
                break
            else:
                print("El número de intentos debe situarse en el rango de 1 a 6.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    # Bucle de juego y resolución de pistas
    acertado = False
    print("\nHe generado un número secreto entre 1 y 1000. ¡Intenta adivinarlo!")

    for ronda in range(1, intentos_totales + 1):
        intentos_restantes = intentos_totales - ronda + 1
        print(f"\n[Intento {ronda}/{intentos_totales}] (Te quedan {intentos_restantes} intentos)")

        while True:
            try:
                intento_usuario = int(input("Ingresa tu número: ").strip())
                break
            except ValueError:
                print("Error: Debes ingresar un número entero.")

        if intento_usuario == numero_secreto:
            print("\n" + "*" * 50)
            print(f"🎉 ¡HAS ACERTADO! ¡Eres un genio! Lo lograste en el intento {ronda}.")
            print("*" * 50)
            acertado = True
            break
        elif intento_usuario < numero_secreto:
            print("📈 Pista: El número secreto es MÁS ALTO.")
        else:
            print("📉 Pista: El número secreto es MÁS BAJO.")

    # Conclusión si se agotan los intentos
    if not acertado:
        print("\n" + "-" * 50)
        print(f"❌ ¡Oh no! Se han agotado tus intentos.")
        print(f"El número secreto era: {numero_secreto}.")
        print("¡Prueba suerte en la próxima partida!")
        print("-" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPartida interrumpida. ¡Hasta luego!")
