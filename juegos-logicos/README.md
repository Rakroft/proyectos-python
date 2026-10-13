# 🎮 Juegos de Lógica y Algoritmos en Consola

Colección de scripts interactivos desarrollados en Python enfocados en la resolución de problemas lógicos, estructuras de control de flujo, bucles y gestión de estados en terminal.

---

## 🕹️ Proyectos Incluidos

### 1. 🎯 Juego de la Adivinanza Numérica (`adivinanza/`)
- **Descripción**: Genera un número pseudoaleatorio entre 1 y 1000 con la librería `random`.
- **Mecánica**: El jugador define cuántos intentos necesita (entre 1 y 6). Tras cada intento, el sistema proporciona retroalimentación dinámica indicando si el número objetivo es más alto o más bajo.
- **Conceptos**: Búsqueda binaria intuitiva, condicionales `if/elif/else`, bucles `for/while`, manejo de excepciones con `ValueError`.

### 2. ⚡ Pokémon Rojo Fuego: Aventura en Consola (`pokemon-aventura/`)
- **Descripción**: Simulador interactivo por consola que recrea la elección de inicial y la batalla decisiva de la Liga Pokémon contra el Campeón Azul.
- **Mecánica**: 
  - Selección de inicial (Bulbasaur, Charmander, Squirtle o Pikachu).
  - Sistema opcional de apodos con persistencia en el flujo de la partida.
  - Validación de nivel mínimo requerido ($\ge 50$) para acceder al reto final.
  - Tienda Poké Mart con cálculo aritmético de saldo disponible y compra de Hiperpociones.
- **Conceptos**: Diccionarios de datos, condicionales anidados, control de inventario/saldo y narrativa interactiva.

---

## 💻 Cómo Ejecutarlos

### Adivinanza Numérica:
```bash
cd juegos-logicos/adivinanza
python3 adivinanza.py
```

### Aventura Pokémon:
```bash
cd juegos-logicos/pokemon-aventura
python3 pokemon_aventura.py
```

---

## 👨‍💻 Autor

- **Adrián Ortega Martínez** - [@Rakroft](https://github.com/Rakroft)
