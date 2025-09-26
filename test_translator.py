from code_translator import translate_code

def test_python_to_js():
    # Test básico de función
    python_code = """def suma(a, b):
    resultado = a + b
    print(resultado)
    return resultado"""
    
    js_result = translate_code(python_code, "python", "javascript")
    print("Test Python -> JS:")
    print(js_result)
    print("-" * 40)

def test_bash_to_ps():
    # Test básico de script
    bash_code = """nombre="test"
echo "Ejecutando $nombre"
ls
mkdir temp"""
    
    ps_result = translate_code(bash_code, "bash", "powershell")
    print("Test Bash -> PowerShell:")
    print(ps_result)
    print("-" * 40)

if __name__ == "__main__":
    test_python_to_js()
    test_bash_to_ps()