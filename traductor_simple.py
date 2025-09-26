from code_translator import translate_code

def main():
    print("=== TRADUCTOR DE CÓDIGO ===")
    print("Opciones disponibles:")
    print("1. Python -> JavaScript")
    print("2. Bash -> PowerShell")
    
    opcion = input("\nElige una opción (1 o 2): ")
    
    if opcion == "1":
        from_lang = "python"
        to_lang = "javascript"
        print("\nEjemplo de código Python:")
        print('def saludar():\n    print("Hola mundo")')
    elif opcion == "2":
        from_lang = "bash"
        to_lang = "powershell"
        print("\nEjemplo de código Bash:")
        print('echo "Hola mundo"\nls')
    else:
        print("Opción inválida")
        return
    
    print(f"\nIngresa tu código {from_lang.upper()}:")
    print("(Escribe 'FIN' en una línea para terminar)")
    
    code_lines = []
    while True:
        line = input()
        if line.upper() == "FIN":
            break
        code_lines.append(line)
    
    if not code_lines:
        print("No ingresaste código")
        return
    
    code = '\n'.join(code_lines)
    
    print(f"\n=== CÓDIGO ORIGINAL ({from_lang.upper()}) ===")
    print(code)
    
    try:
        translated = translate_code(code, from_lang, to_lang)
        print(f"\n=== CÓDIGO TRADUCIDO ({to_lang.upper()}) ===")
        print(translated)
    except Exception as e:
        print(f"Error en la traducción: {e}")

if __name__ == "__main__":
    main()