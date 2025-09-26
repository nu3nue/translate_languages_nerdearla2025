from code_translator import translate_code

# Ejemplos de uso del traductor de código

def ejemplo_python_a_javascript():
    print("=== Ejemplo: Python -> JavaScript ===")
    
    python_code = """def saludar(nombre):
    print("Hola", nombre)
    edad = 25
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    
    for i in range(3):
        print("Número:", i)"""
    
    print("Código Python original:")
    print(python_code)
    print("\nCódigo JavaScript traducido:")
    
    js_code = translate_code(python_code, "python", "javascript")
    print(js_code)

def ejemplo_bash_a_powershell():
    print("\n=== Ejemplo: Bash -> PowerShell ===")
    
    bash_code = """#!/bin/bash
nombre="Juan"
echo "Hola $nombre"
ls -la
mkdir nueva_carpeta
cp archivo.txt backup.txt
if [ -f "archivo.txt" ]
then
    echo "El archivo existe"
fi

for archivo in *.txt
do
    echo "Procesando: $archivo"
done"""
    
    print("Código Bash original:")
    print(bash_code)
    print("\nCódigo PowerShell traducido:")
    
    ps_code = translate_code(bash_code, "bash", "powershell")
    print(ps_code)

def ejemplo_casos_complejos():
    print("\n=== Ejemplos más complejos ===")
    
    # Ejemplo Python con funciones y loops anidados
    python_complex = """def procesar_lista(numeros):
    resultado = []
    for num in numeros:
        if num > 0:
            resultado.append(num * 2)
        else:
            resultado.append(0)
    return resultado

lista = [1, -2, 3, -4, 5]
nueva_lista = procesar_lista(lista)
print("Lista procesada:", nueva_lista)"""
    
    print("Python complejo:")
    print(python_complex)
    print("\nJavaScript traducido:")
    print(translate_code(python_complex, "python", "javascript"))
    
    # Ejemplo Bash con variables y condicionales
    bash_complex = """#!/bin/bash
contador=0
archivo_log="sistema.log"

while [ $contador -lt 5 ]
do
    echo "Iteración $contador" >> $archivo_log
    contador=$((contador + 1))
    
    if [ $contador -eq 3 ]
    then
        echo "Punto medio alcanzado"
    fi
done

echo "Proceso completado"
cat $archivo_log"""
    
    print("\nBash complejo:")
    print(bash_complex)
    print("\nPowerShell traducido:")
    print(translate_code(bash_complex, "bash", "powershell"))

if __name__ == "__main__":
    ejemplo_python_a_javascript()
    ejemplo_bash_a_powershell()
    ejemplo_casos_complejos()