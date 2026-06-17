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
print(persona.get('telefono',"no disponible")) # si la calve telefono no exuste no mostrara none si no el segundo parametro que le pasemos al metodo get.
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

