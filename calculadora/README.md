# 🧮 Calculadora Modular en Python

Aplicación interactiva por consola desarrollada en Python que permite realizar operaciones matemáticas básicas y avanzadas con validación estricta de datos y control de excepciones en tiempo de ejecución.

---

## 🚀 Características

- **7 Operaciones Matemáticas**:
  1. Suma (`+`)
  2. Resta (`-`)
  3. Multiplicación (`*`)
  4. División (`/`)
  5. División entera (`//`)
  6. Potenciación (`**`)
  7. Módulo o Resto (`%`)
- **Validación robusta de entradas**: Captura de excepciones `ValueError` cuando el usuario ingresa cadenas o caracteres no numéricos.
- **Prevención de errores aritméticos**: Detección y tratamiento de división entre cero (`ZeroDivisionError`) antes de ejecutar el cálculo.
- **Bucle interactivo**: Permite encadenar múltiples cálculos hasta que el usuario decida salir.

---

## 📋 Requisitos

- Python 3.8 o superior (no requiere librerías externas).

---

## 💻 Uso e Instalación

Para ejecutar la calculadora desde tu terminal:

```bash
cd calculadora
python3 calculadora.py
```

### Ejemplo de Ejecución:
```text
=============================================
        MENÚ DE OPERACIONES MATEMÁTICAS      
=============================================
 1. Suma (+)
 2. Resta (-)
 3. Multiplicación (*)
 4. División (/)
 5. División entera (//)
 6. Potencia (**)
 7. Resto módulo (%)
=============================================
¿Qué operación quieres realizar (1-7)?: 6
Has escogido la opción 6. ¡Perfecto!

Introduce el primer número: 2
Introduce el segundo número: 8
---------------------------------------------
✅ El resultado de tu operación es: 256
---------------------------------------------

¿Deseas realizar otra operación? (s/N): n

¡Hasta la próxima! Espero haberte ayudado. 👋
```

---

## 👨‍💻 Autor

- **Adrián Ortega Martínez** - [@Rakroft](https://github.com/Rakroft)
