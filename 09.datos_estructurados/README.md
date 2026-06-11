# **Datos estructurados:**
- tenemos 3 tipos de datos primarios (string, numerico, boleano)
- tenemos 2 tipos de datos estructurados (lista, diccionario)
## Listas:
Son la manera de como python pude organizar multiples tipos de datos en una sola variable.
se puede tener:
- listas de tipo numerico
- listas de tipo texto 
- lista de tipo mixto
Python nos permite acceder a estas listas a travez de indices, los indices son ascendentes del numero 0.
### creacion de listas:
la listas solo basta encerrar los elementos que deseamos almacenar con `[]` inmediante despues del operador de asignacion.
```python
# creando una lista vacia 
lista:list=[] # lista vacia
#lista numerica
## OJO: los elementos de una lista se separan por comas 
lista_numerica:list[int]=[3,8,4] #lisra de numeros enteros
lista_num_mixto:list[int|float]=[3.6,7,.7] 
# lista de texto
amigos:list[str]=['eduardo','kevin',]
# lista mixta
lista_mixta:list=['pedro',20,False,1.67]
```
### Acceder y modificar elementos de una lista:
Para poder acceder a un elemntos de ua lsita trabajamos con los indices que python le asigna a cada elemento:
- los indices positivos (comienza de 0 y van de izquierda a derecha)
- los indices negativos(comienzan de -1 y van de derecha a izquierda)
Con estos indoces podemos acceder al valor del elemento y tambien podremos modificarlos.
Tenemos dos formas de acceder a los elementos:
- acceder y modificar por indice (posicion)
```python
frutas:list[str]=['🍎','🍌','🍒','🍑']
# posicion o indice
# acceder al tercer elemento
print(frutas[2])
#acceder al segundo elemento por su indice negativo
print(frutas[-3])
```
## modificar
- acceder y modificar por rango (slicing)
```python
vocales:str=['a','e','i','o','u']
# acceder a elementos por slicing
# esta tecnica nos permite acceder a mas de un elemento en una sola linea de codigo
vocales[0:3]
## remplazar elementos por slicing
vocales[0:3]=['A','E'.'I']

```
### Metodos para listas
un metodo es un accion que puedo realizar en una lista, los metyodso por lo general se utilisan despues de la variable y se accede al metodo atraves de un punto.
Los metodos mas comunes son aquellso que nos permiten agregar, modificar y eliminar.
```python
# agregar elementos 
## appened:
animales:list[str]=[]
animales.append('leon')
animales.append('gato')
# el metodo appened agrega elementos en la ultima posicion de nuestra lista
### insert:
numeros_pares:list[int]=[4,6,10]
numeros_pares.insert(0,2)
numeros_pares.insert(3,8)

amigos:list[str]=["juan","jose"]
amigos.insert(1,"deduardo")
# eliminar elementos
## eliminar por indice:
vocales:list[str]=['a','e','i','o','U']
del vocales[-1]

## eliminar por valor:
vocales:list[str]=['a','e','i','o','U']
vocales.remove('U')

## usando metodo pop:
vocales:list[str]=['a','e','i','o','U']
vocales.pop()
# en este caso pop elimina por defecto el ultimo elemento
vocales.pop(2)
# en este caso eliminara el elemento que se encuntre en la posicion 3

# buscar 
## este metodo permite ubicar atraves del valor el primer elemento (la primera coincidencia) dentro de una lista, y devolvera el indice de es valor, este metodo es index

amantes:list[str]=['chapo','cristian','emerson','victor']
# quiero ubicar en mi lista de infieles existe victor
buscar:int=amantes.index("victor")#retorna un indice si existe 3
amantes[buscar] # victor

## busqueda por pertenecia
existe:bool="chapo" in amantes

```

## Diccionarios:



