# Diccionarios
Los diccionarios son la forma mas comun para almacenar datos estructurados de objetos que nos rodea en el mundo, al igual que las listas que guardan informacion en `elementos`, de igual manera los diccionarios almacenan sus datos en `elemenetos` separados por comas.
La diferencia es que las listas almacenan los elementos por `indice` y `valor`.
Y los diccionarios almacenan los elementos por `clave:valor`.

**Ejemplos:**
```python
vocales:list[str]=['a','e','i','o','u']
#                   0   1   2   3   4
# un elemento en una lista esta conformado por dos cositas el indice y su valor.
# para accedera aun valor en una lista
vocales[2] # i
alumno:dict={'nombre':'eduardo','edad':40}
# un elemento en un diccionario esta conformadopor clave y valor
# para acceder a un diccionario 
alumno['nombre'] # eduardo
```
## acceder a elementos
-**por clave(forma directa)**
```python
persona:dict={
    'nombre':'celia',
    'edad':16,
    'ciudad':'cabo verde',
    'email':'celi@gmail.com'
}
print(persona['edad']) # 16
print(persona['email']) # celi@gmail.com
```
-**por su metodo(forma mas segura)**
```python
persona:dict={
    'nombre':'celia',
    'edad':16,
    'ciudad':'cabo verde',
    'email':'celi@gmail.com'
}
print(persona.get('nombre')) # celia
# la diferenvia de este metodo es que nos permite manejar errores 
print(persona.get('telefono') # none
print(persona.get('telefono',"no disponible")) # si la clave telefono no existe nos mostrara none si no el segundo parametro que le pasemos al metodo get.
```
## modificar elementos 
**cambiar un valor existente**
```python
persona:dict={
    'nombre':'celia',
    'edad':16,
}
persona['edad']=19
# agregar una nueva clave:valor
persona['carrera']='agro'
# si la clave no existe se crea automaticamente. si existe se actualisara 
```
## agregar/actualizar mulitiples elementos
Para esto tenemos que hacer uso del metodo `.update` se puede agregar si lo pares de  `clave:valor` no existe y actualizar si el `clave:valor` existe.
```python
tienda:dict[str:str|int]={
    'razon_social':'bigote',
    'RUC': 201547789632
}
# actualizar usando el metodo .update tengo dos maneras de usar este metodo:
# 1. diccionarios 
tienda.update({'RUC':4587232089564,'telefono':987456123})

# 2. pares clave:valor
tienda.update(h_atencion='9-12',gerente='kevin')
```
## eliminar elementos
```python
tienda:dict[str:str|int]={
    'razon_social':'bigote',
    'RUC': 201547789632
}
el_eliminado=tienda.pop('RUC')
tienda.popitem() # elimina el ultimo elemento

# para limpiar todo el diccionario 
tienda.clear()
```

## recorre dicionario
Recorrer un diccionario en programación (como en Python) es el proceso de iterar sobre sus elementos. Para ello, se utilizan bucles for que permiten extraer sus claves (keys), valores (values), o ambos de manera rápida.Aquí te muestro las formas más eficientes de hacerlo usando la estructura de datos básica:
```python
usuario = {"nombre": "Ana", "edad": 25}
```
1. Recorrer solo las CLAVESPor defecto, al recorrer un diccionario, iteras sobre sus claves.
```python
usuario = {"nombre": "Ana", "edad": 25}

for clave in usuario:
    print(clave)
    # Imprime: nombre, edad
```
2. Recorrer solo los VALORESUtilizas el método .values() para acceder únicamente a la información.
``` python
usuario = {"nombre": "Ana", "edad": 25}

for valor in usuario.values():
    print(valor)
    # Imprime: Ana, 25

```
3. Recorrer CLAVES y VALORES a la vezUtilizas el método .items() para obtener ambos datos en cada paso.
```python
usuario = {"nombre": "Ana", "edad": 25}

for clave, valor in usuario.items():
    print(f"{clave}: {valor}")
    # Imprime: nombre: Ana \n edad: 25

```