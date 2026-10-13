"""
Aventura RPG por Consola: Pokémon Rojo Fuego
Autor: Adrián Ortega Martínez (@Rakroft)
Descripción: Simulación interactiva por consola inspirada en el inicio y la batalla final
de Pokémon Rojo Fuego. Implementa toma de decisiones con condicionales anidados,
gestión de estados (apodos, nivel, dinero), tienda de objetos y combate contra el Campeón Azul.
"""

def main() -> None:
    print("=" * 60)
    print("           POKÉMON ROJO FUEGO: AVENTURA EN CONSOLA         ")
    print("=" * 60)

    # 1. Introducción y Registro de Entrenador
    print("\nProfesor Oak: ¡Hola! Te doy la bienvenida al mundo de Pokémon.")
    nombre_pj = input("Antes de comenzar tu viaje, por favor, dime cómo te llamas: ").strip()
    if not nombre_pj:
        nombre_pj = "Rojo"

    print(f"\nProfesor Oak: ¡Encantado de conocerte, {nombre_pj}!")
    print("Este fascinante mundo está habitado por criaturas llamadas Pokémon.")
    print("Tu misión es convertirte en un Maestro Pokémon. Para lograrlo, debes elegir a tu compañero inicial.\n")

    # 2. Selección del Pokémon Inicial
    print("Opciones disponibles:")
    print("  1. Bulbasaur   (Tipo Planta / Veneno)")
    print("  2. Charmander  (Tipo Fuego)")
    print("  3. Squirtle    (Tipo Agua)")
    print("  4. Pikachu     (Tipo Eléctrico)")

    pokemons_disponibles = {
        1: ("Bulbasaur", "Planta/Veneno"),
        2: ("Charmander", "Fuego"),
        3: ("Squirtle", "Agua"),
        4: ("Pikachu", "Eléctrico")
    }

    while True:
        try:
            opcion_inicial = int(input("\n¿Cuál eliges? (1-4): ").strip())
            if opcion_inicial in pokemons_disponibles:
                pokemon_elegido, tipo = pokemons_disponibles[opcion_inicial]
                print(f"\n¡Has elegido a {pokemon_elegido}, un Pokémon de tipo {tipo}! ¡Excelente elección!")
                break
            else:
                print("Opción no válida. Por favor, selecciona un número entre 1 y 4.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número del 1 al 4.")

    # 3. Asignación opcional de apodo
    while True:
        try:
            quiere_apodo = int(input(f"\n¿Deseas ponerle un apodo a {pokemon_elegido}? Sí (1) / No (2): ").strip())
            if quiere_apodo == 1:
                apodo = input(f"¿Qué apodo deseas ponerle a {pokemon_elegido}?: ").strip()
                if apodo:
                    nombre_combate = apodo
                    print(f"¡Perfecto! Ahora {pokemon_elegido} será conocido como '{nombre_combate}'.")
                else:
                    nombre_combate = pokemon_elegido
                break
            elif quiere_apodo == 2:
                nombre_combate = pokemon_elegido
                print(f"De acuerdo, mantendremos el nombre original: {nombre_combate}.")
                break
            else:
                print("Por favor, digita 1 (Sí) o 2 (No).")
        except ValueError:
            print("Entrada inválida. Digita 1 o 2.")

    # 4. Salto temporal al Desafío del Alto Mando y Campeón Azul
    print("\n" + "=" * 60)
    print("           LIGA POKÉMON: EL COMBATE FINAL                  ")
    print("=" * 60)
    print(f"\nHan transcurrido meses de duro entrenamiento para {nombre_pj} y {nombre_combate}.")
    print("Has superado todas las medallas de gimnasio y vencido al Alto Mando.")
    print("Solo queda el desafío supremo: el Campeón de la Liga Pokémon, ¡Azul!\n")

    while True:
        try:
            nivel_pokemon = int(input(f"¿A qué nivel has entrenado a {nombre_combate}?: ").strip())
            if nivel_pokemon > 0:
                break
            print("El nivel debe ser un número positivo.")
        except ValueError:
            print("Por favor, introduce un nivel numérico válido.")

    # 5. Condicional de nivel para el combate final
    if nivel_pokemon < 50:
        print(f"\n❌ Tu Pokémon {nombre_combate} se encuentra en nivel {nivel_pokemon}.")
        print("El Campeón Azul es demasiado fuerte. Necesitas alcanzar al menos el nivel 50 para retarlo.")
        print("¡Sigue entrenando duro por las rutas de Kanto! Nos vemos en el próximo desafío.")
        return

    print(f"\n🔥 ¡Felicidades! Tu {nombre_combate} se encuentra en nivel {nivel_pokemon}.")
    print("¡Cumples con el nivel necesario para desafiar al Campeón Azul!")

    # 6. Preparación y Tienda Pokémon (Poké Mart)
    print("\nPara resistir el combate contra los poderosos Pokémon de Azul, necesitarás Hiperpociones.")
    
    while True:
        try:
            dinero = float(input("¿Cuánto dinero tienes ahorrado en tu monedero Pokémon (ej. 15.0)?: ").strip())
            break
        except ValueError:
            print("Por favor, ingresa una cantidad numérica válida.")

    precio_hiperpocion = 10.5
    print(f"\nPrecio por Hiperpoción en la tienda: {precio_hiperpocion:.2f} ₽")
    if dinero >= precio_hiperpocion:
        print(f"Tienes {dinero:.2f} ₽: Tienes fondos suficientes para adquirir provisiones.")
    else:
        print(f"Tienes {dinero:.2f} ₽: Tus fondos son limitados, tendrás que administrar tus recursos.")

    # Interacción con la tienda
    while True:
        try:
            entrar_tienda = int(input("\n¿Deseas entrar a la Tienda Pokémon? Sí (1) / No (2): ").strip())
            if entrar_tienda == 1:
                print("\n🏪 Bienvenido al Poké Mart.")
                comprar = int(input("¿Te gustaría comprar Hiperpociones? Sí (1) / No (2): ").strip())
                if comprar == 1:
                    max_pociones = int(dinero // precio_hiperpocion)
                    if max_pociones > 0:
                        cantidad = int(input(f"¿Cuántas Hiperpociones deseas comprar? (Puedes comprar hasta {max_pociones}): ").strip())
                        if 1 <= cantidad <= max_pociones:
                            gasto = cantidad * precio_hiperpocion
                            dinero -= gasto
                            print(f"✅ ¡Has comprado {cantidad} Hiperpoción(es) por {gasto:.2f} ₽!")
                            print(f"Te quedan {dinero:.2f} ₽ en el monedero. ¡Úsalas con sabiduría frente a Azul!")
                        else:
                            print("Cantidad no válida o fondos insuficientes.")
                    else:
                        print("No dispones de suficiente dinero para adquirir Hiperpociones.")
                print("¡Gracias por tu visita a la Tienda Pokémon!")
                break
            elif entrar_tienda == 2:
                print("\nDecides ir directo al combate sin pasar por la tienda.")
                break
            else:
                print("Digita 1 (Sí) o 2 (No).")
        except ValueError:
            print("Entrada inválida. Digita 1 o 2.")

    # 7. Desenlace de la Aventura
    print("\n" + "*" * 60)
    print(f"🏆 ¡VICTORIA! ¡{nombre_pj} Y {nombre_combate} HAN DERROTADO A AZUL!")
    print("*" * 60)
    print(f"\n¡Felicidades, {nombre_pj}! Has completado tu aventura en el mundo Pokémon.")
    print("¡Eres oficialmente el nuevo Campeón de la Liga Pokémon en la región de Kanto!")
    print(f"Junto a tu inseparable {nombre_combate}, tu nombre ha quedado grabado en el Hall de la Fama.")
    print("\n¡Gracias por jugar a Pokémon Rojo Fuego en Consola! 👋🎮")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nPartida interrumpida por el usuario. ¡Hasta pronto!")
