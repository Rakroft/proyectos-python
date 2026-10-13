# 🐍 Proyectos y Prácticas en Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/Arquitectura-Modular-6c63ff?style=for-the-badge" alt="Arquitectura Modular"/>
  <img src="https://img.shields.io/badge/Licencia-MIT-22c55e?style=for-the-badge" alt="MIT License"/>
  <a href="https://rakroft.github.io/Rakroft/">
    <img src="https://img.shields.io/badge/🌐_Portfolio-Rakroft-00f5ff?style=for-the-badge" alt="Portfolio Web"/>
  </a>
</p>

Repositorio centralizado con proyectos, algoritmos y prácticas de desarrollo en **Python** creados por **Adrián Ortega Martínez** ([@Rakroft](https://github.com/Rakroft)). Cada herramienta está diseñada aplicando principios de modularidad, tipado estático opcional, validación rigurosa de entradas y control metódico de excepciones.

---

## 📂 Estructura del Repositorio

```text
proyectos-python/
├── .gitignore
├── README.md                          # Documentación general del repositorio
│
├── calculadora/                       # Calculadora interactiva por consola
│   ├── README.md                      # Documentación y guía de operaciones
│   └── calculadora.py                 # Script principal con 7 operaciones matemáticas
│
├── cifrado-cesar/                     # Algoritmo criptográfico clásico
│   ├── README.md                      # Fundamentos matemáticos del algoritmo
│   └── cifrado_cesar.py               # Cifrador y descifrador con rotación modular
│
└── juegos-logicos/                    # Prácticas algorítmicas y toma de decisiones
    ├── README.md                      # Documentación general de juegos
    ├── adivinanza/
    │   └── adivinanza.py              # Adivinanza con límites de intentos y pistas
    └── pokemon-aventura/
        └── pokemon_aventura.py        # Aventura RPG interactiva con tienda y combate
```

---

## 🛠️ Resumen de Proyectos

| Proyecto | Descripción | Conceptos Clave | Enlace |
| :--- | :--- | :--- | :--- |
| **Calculadora Modular** | Menú con 7 operaciones aritméticas (básicas, enteras, potencia y módulo) con captura estricta de errores. | `ZeroDivisionError`, `ValueError`, bucles de validación, modularidad. | [Ver proyecto →](calculadora/) |
| **Cifrado César** | Algoritmo de cifrado por sustitución monoalfabética con desplazamiento de 1 a 25 posiciones. | Criptografía clásica, tablas ASCII, aritmética modular, preservación de mayúsculas/minúsculas. | [Ver proyecto →](cifrado-cesar/) |
| **Adivinanza Numérica** | Juego de predicción de números aleatorios (1-1000) con dificultad configurable y pistas de proximidad. | `random`, control de intentos, búsqueda iterativa. | [Ver proyecto →](juegos-logicos/adivinanza/) |
| **Pokémon Rojo Fuego** | Aventura interactiva por consola con selección de criaturas, personalización, gestión económica y combate contra el Campeón Azul. | Diccionarios, condicionales anidados, control de estado, interactividad CLI. | [Ver proyecto →](juegos-logicos/pokemon-aventura/) |

---

## ⚡ Instalación y Ejecución

Todos los scripts utilizan exclusivamente la **biblioteca estándar de Python**, por lo que no es necesario instalar dependencias de terceros ni crear entornos virtuales complejos.

### 1. Clonar el repositorio
```bash
git clone https://github.com/Rakroft/proyectos-python.git
cd proyectos-python
```

### 2. Ejecutar cualquiera de los proyectos

- **Calculadora**:
  ```bash
  python3 calculadora/calculadora.py
  ```

- **Cifrado César**:
  ```bash
  python3 cifrado-cesar/cifrado_cesar.py
  ```

- **Adivinanza Numérica**:
  ```bash
  python3 juegos-logicos/adivinanza/adivinanza.py
  ```

- **Aventura Pokémon**:
  ```bash
  python3 juegos-logicos/pokemon-aventura/pokemon_aventura.py
  ```

---

## 🧪 Pruebas y Validación

Todos los scripts han sido testeados con Python 3.8+ bajo entornos Linux, verificando:
- Manejo correcto de entradas anómalas (letras en campos numéricos, saltos de línea vacíos).
- Salida limpia y controlada ante interrupciones de teclado (`Ctrl + C`).
- Coherencia en operaciones matemáticas límite (división por cero, restos y potencias).

---

## 👨‍💻 Sobre el Autor

**Adrián Ortega Martínez**  
Estudiante de 2º curso de **ASIR** (Administración de Sistemas Informáticos en Red) en Barcelona.  
Interesado en administración de sistemas Linux/Windows, redes, automatización con scripts y ciberseguridad.

- 🌐 **Portfolio Web:** [rakroft.github.io/Rakroft](https://rakroft.github.io/Rakroft/)
- 💼 **LinkedIn:** [adrian-ortega-martinez](https://linkedin.com/in/adrian-ortega-martinez)
- 🐙 **GitHub:** [@Rakroft](https://github.com/Rakroft)
- ✉️ **Contacto:** [adrianoft07@gmail.com](mailto:adrianoft07@gmail.com)

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más información.
