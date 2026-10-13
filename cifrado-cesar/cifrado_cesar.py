"""
Cifrado y Descifrado César en Python
Autor: Adrián Ortega Martínez (@Rakroft)
Descripción: Implementación del algoritmo criptográfico clásico por sustitución monoalfabética.
Aplica un desplazamiento modular de 1 a 25 posiciones respetando caracteres especiales, espacios
y distinguiendo mayúsculas y minúsculas.
"""

def cifrar_letra(caracter: str, desplazamiento: int) -> str:
    """
    Aplica el desplazamiento modular a una letra individual.
    Mantiene mayúsculas (ASCII 65-90) y minúsculas (ASCII 97-122).
    """
    if not (1 <= desplazamiento <= 25):
        raise ValueError("El desplazamiento debe estar comprendido entre 1 y 25.")

    if not caracter.isalpha():
        return caracter

    # Base ASCII según si es mayúscula o minúscula
    base = ord('A') if caracter.isupper() else ord('a')
    codigo = ord(caracter)
    
    # Rotación modular en el alfabeto de 26 letras
    nuevo_codigo = base + (codigo - base + desplazamiento) % 26
    return chr(nuevo_codigo)

def cifrar_mensaje(mensaje: str, desplazamiento: int) -> str:
    """
    Cifra una cadena de texto completa utilizando el desplazamiento indicado.
    """
    resultado = []
    for caracter in mensaje:
        resultado.append(cifrar_letra(caracter, desplazamiento))
    return "".join(resultado)

def descifrar_mensaje(mensaje_cifrado: str, desplazamiento: int) -> str:
    """
    Descifra un mensaje previamente cifrado aplicando la rotación inversa (26 - desplazamiento).
    """
    desplazamiento_inverso = (26 - desplazamiento) % 26
    return cifrar_mensaje(mensaje_cifrado, desplazamiento_inverso)

def main() -> None:
    print("=" * 50)
    print("       ALGORITMO CRIPTOGRÁFICO: CIFRADO CÉSAR      ")
    print("=" * 50)

    mensaje_original = input("Introduce el mensaje que deseas procesar: ").strip()
    if not mensaje_original:
        print("El mensaje no puede estar vacío.")
        return

    while True:
        try:
            desplazamiento = int(input("Introduce el desplazamiento deseado (1-25): "))
            if 1 <= desplazamiento <= 25:
                break
            else:
                print("Error: El número de desplazamiento debe estar entre 1 y 25.")
        except ValueError:
            print("Error: Debes ingresar un valor numérico entero.")

    # Cifrado
    texto_cifrado = cifrar_mensaje(mensaje_original, desplazamiento)
    # Descifrado de comprobación
    texto_descifrado = descifrar_mensaje(texto_cifrado, desplazamiento)

    print("\n" + "-" * 50)
    print(f"🔒 Mensaje Original:   {mensaje_original}")
    print(f"🔑 Clave (Desplazo):   {desplazamiento}")
    print(f"🛡️  Mensaje Cifrado:    {texto_cifrado}")
    print(f"🔓 Mensaje Descifrado:  {texto_descifrado}")
    print("-" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProceso interrumpido por el usuario.")
