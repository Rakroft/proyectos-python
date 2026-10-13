# 🔐 Cifrado y Descifrado César en Python

Implementación práctica del histórico algoritmo criptográfico por sustitución monoalfabética (Cifrado César) desarrollado en Python.

---

## 📖 ¿Cómo funciona?

El cifrado César consiste en sustituir cada letra del texto en claro por otra que se encuentra un número fijo de posiciones (`desplazamiento`) más adelante en el abecedario.

Para la rotación modular se emplea la fórmula matemática:
$$C = (P + k) \pmod{26}$$

Donde:
- $C$: Carácter resultante cifrado.
- $P$: Posición del carácter original en el alfabeto.
- $k$: Clave de desplazamiento ($1 \le k \le 25$).

Para descifrar el mensaje, se aplica la transformación inversa:
$$P = (C - k) \pmod{26} \equiv (C + (26 - k)) \pmod{26}$$

---

## 🚀 Características del Script

- **Soporte de caracteres mixtos**: Respeta mayúsculas y minúsculas sin alterar signos de puntuación, números ni espacios en blanco.
- **Validación de parámetros**: Asegura que el valor de desplazamiento se encuentre estrictamente en el rango válido $[1, 25]$.
- **Comprobación bidireccional**: Realiza el cifrado y la posterior prueba de descifrado automático para verificar la integridad del mensaje.

---

## 💻 Ejecución

```bash
cd cifrado-cesar
python3 cifrado_cesar.py
```

### Ejemplo de uso:
```text
==================================================
       ALGORITMO CRIPTOGRÁFICO: CIFRADO CÉSAR      
==================================================
Introduce el mensaje que deseas procesar: Seguridad en Redes ASIR
Introduce el desplazamiento deseado (1-25): 3

--------------------------------------------------
🔒 Mensaje Original:   Seguridad en Redes ASIR
🔑 Clave (Desplazo):   3
🛡️  Mensaje Cifrado:    Vhjxulgdg HQ Uhghv DVLUB  (o según rotación)
🔓 Mensaje Descifrado:  Seguridad en Redes ASIR
--------------------------------------------------
```

---

## 👨‍💻 Autor

- **Adrián Ortega Martínez** - [@Rakroft](https://github.com/Rakroft)
