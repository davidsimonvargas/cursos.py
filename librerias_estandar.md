# **LIBRERIAS ESTANDAR**

La Biblioteca Estándar de Python es una extensa colección de módulos, funciones y tipos de datos que vienen integrados por defecto al instalar el lenguaje. 

##  **CUALES SON:**

Python agrupa sus herramientas según el propósito principal:

1. **Tipos de datos y matemáticas:** math, random (números aleatorios), datetime (fechas y horas), statistics, decimal.

2. **Manejo de archivos y datos:** os (sistema operativo), pathlib, json, csv, sqlite3.

3. **Internet y redes:** requests no está en la estándar, pero sí urllib, socket y http.

4. **Procesamiento de texto:** re (expresiones regulares), difflib, string.

5. **Depuración y pruebas:** unittest, timeit (medición de rendimiento), pdb

### **LOS MAS USADOS:**

Los módulos más usados y sus funciones principales:

- **`os y pathlib:`** Esenciales para la interacción con el sistema operativo y el manejo de rutas de archivos y directorios de forma segura.

- **`sys:`** Permite interactuar directamente con el entorno de ejecución de Python, procesar argumentos de la línea de comandos y gestionar la memoria.

- **`Json:`** Fundamental para analizar, leer y escribir datos en formato JSON, muy utilizado en el consumo de APIs.

- **`datetime:`** Proporciona clases y funciones para manipular y formatear fechas y horas

- **`re:`** Permite el uso de expresiones regulares para realizar búsquedas, validaciones y manipulaciones avanzadas de texto.

- **`math:`** Contiene funciones matemáticas fundamentales (como trigonometría, logaritmos y constantes).

- **`random:`** Utilizado para generar números pseudoaleatorios, hacer selecciones aleatorias o barajar elementos.

- **`collections:`** Ofrece alternativas avanzadas a los tipos de datos nativos de Python, como defaultdict y Counter.

- **`urllib / http:`** Módulos para realizar solicitudes de red y trabajar con protocolos web (aunque para proyectos más complejos, suele usarse la librería externa requests)

- **`threading / asyncio:`** Herramientas clave para manejar concurrencia, asincronía y mejorar el rendimiento del código.

### **LA FORMA DE INCLUIRLAS EN NUESTROS ARCHIVOS DE PYTHON**

1. Importar otros archivos de Python (Módulos)Para utilizar funciones, clases o variables de otro archivo .py que esté en tu mismo directorio, utiliza la instrucción import en la parte superior de tu archivo.
```python
import nombre_del_archivo  # Sin la extensión .py
# Para usar una función del archivo:
nombre_del_archivo.mi_funcion()
```
Si solo necesitas elementos específicos, usa `from`:
```python
from nombre_del_archivo import mi_funcion, mi_clase

mi_funcion()
```
2. Leer datos desde archivos de texto o externosPara abrir, leer y editar archivos de texto (.txt), datos (.csv), u otros formatos, utiliza la función integrada open().Se recomienda usar with para asegurar que el archivo se cierre automáticamente al terminar:
```python
# 'r' significa modo lectura (read)
with open('tu_archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
```
Otros modos comunes al abrir archivos incluyen:
- `'w'`: Modo escritura. Crea el archivo si no existe y borra el contenido previo si ya existía.
- `'a'`: Modo añadir (append). Agrega el texto al final del archivo sin borrar lo anterior
- 
### **MODULOS DE PYTHON**

Un módulo en Python es un archivo con extensión .py que contiene código reutilizable (funciones, variables y clases)

1. Módulos integrados (Biblioteca estándar)

Python incluye cientos de módulos útiles que no requieren instalación previa.Módulo math: Permite realizar operaciones matemáticas avanzadas.

```PYTHON
import math
# Calcular la raíz cuadrada
print(math.sqrt(16))  # Salida: 4.0
# Obtener el valor de Pi
print(math.pi)        # Salida: 3.141592653589793

```

- Módulo random: Permite generar números aleatorios.

```PYTHON
import random
# Elegir un elemento al azar de una lista
colores = ["rojo", "verde", "azul"]
print(random.choice(colores))
# Generar un número entero aleatorio entre 1 y 10
print(random.randint(1, 10))

```

2.  Módulos propios (Personalizados)
Puedes crear tus propios archivos .py y usarlos en otros programas.
- Por ejemplo, si tienes un archivo llamado operaciones.py con este código:
```PYTHON
# operaciones.py
def sumar(a, b):
    return a + b
```
- Puedes importarlo desde otro archivo en la misma carpeta utilizando import:

```PYTHON
import operaciones

resultado = operaciones.sumar(5, 3)
print(resultado)  # Salida: 8
```

3.   Técnicas de importación
Puedes modificar cómo importas los módulos para que tu código sea más limpio:
- Importar una función específica:
```PYTHON
from math import sqrt
print(sqrt(25)) # Salida: 5.0
```
- Renombrar un módulo (útil para nombres largos):

```PYTHON
import math as m
print(m.factorial(5)) # Salida: 120

```