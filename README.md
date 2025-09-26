# Traductor de código realizado con Amazon Q

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/91edac64-7379-48dc-9b44-8449531d74f1" />

Un traductor automático que convierte código entre diferentes lenguajes de programación.

## 🚀 Lenguajes Soportados

- **Python** → **JavaScript**
- **Bash** → **PowerShell**

## 📁 Archivos del Proyecto

- `code_translator.py` - Traductor principal
- `traductor_simple.py` - Interfaz fácil de usar
- `demo_rapida.py` - Ejemplos automáticos
- `examples.py` - Ejemplos completos
- `test_translator.py` - Tests básicos

## 🎯 Uso Rápido

### 1. Ver ejemplos automáticos
```bash
python demo_rapida.py
```

### 2. Traducir tu código
```bash
python traductor_simple.py
```
- Elige opción (1 o 2)
- Escribe tu código línea por línea
- Escribe `FIN` para terminar
- Ve la traducción

### 3. Usar en tu programa
```python
from code_translator import translate_code

codigo = "print('Hola mundo')"
resultado = translate_code(codigo, "python", "javascript")
print(resultado)  # console.log('Hola mundo');
```

## 📝 Ejemplos

### Python → JavaScript
**Entrada:**
```python
def saludar(nombre):
    print("Hola", nombre)
    if nombre == "Juan":
        print("¡Bienvenido!")
```

**Salida:**
```javascript
function saludar(nombre) {
  console.log("Hola", nombre);
  if (nombre == "Juan") {
    console.log("¡Bienvenido!");
  }
}
```

### Bash → PowerShell
**Entrada:**
```bash
nombre="Usuario"
echo "Hola $nombre"
ls
mkdir nueva_carpeta
```

**Salida:**
```powershell
$nombre = "Usuario"
Write-Host "Hola $nombre"
Get-ChildItem
New-Item -ItemType Directory -Path nueva_carpeta
```

## ⚡ Características Traducidas

### Python → JavaScript
- ✅ Funciones (`def` → `function`)
- ✅ Variables (`=` → `let =`)
- ✅ Print (`print()` → `console.log()`)
- ✅ Condicionales (`if/else`)
- ✅ Loops (`for`, `while`)
- ✅ Listas (`.append()` → `.push()`)

### Bash → PowerShell
- ✅ Variables (`var=` → `$var =`)
- ✅ Echo (`echo` → `Write-Host`)
- ✅ Comandos de archivos (`ls`, `cat`, `mkdir`, etc.)
- ✅ Condicionales (`if [ ]` → `if ( )`)
- ✅ Loops (`for/while`)

## 🛠️ Instalación

1. Descarga todos los archivos
2. Asegúrate de tener Python instalado
3. Ejecuta cualquiera de los archivos Python

## 📋 Requisitos

- Python 3.6+
- No requiere librerías externas

## 🎮 Comandos Rápidos

```bash
# Ver demo
python demo_rapida.py

# Usar traductor interactivo
python traductor_simple.py

# Ver todos los ejemplos
python examples.py

# Ejecutar tests
python test_translator.py
```

## 🔧 Extensión

Para agregar más lenguajes, edita `code_translator.py`:

1. Crea una nueva clase que herede de `CodeTranslator`
2. Implementa el método `translate()`
3. Agrégala al `CodeTranslatorFactory`

## ⚠️ Limitaciones

- Traduce sintaxis básica, no semántica compleja
- Algunos casos específicos pueden requerir ajustes manuales
- No maneja librerías específicas de cada lenguaje

## 📞 Uso

Ejecuta `python demo_rapida.py` para ver ejemplos o `python traductor_simple.py` para traducir tu código.
