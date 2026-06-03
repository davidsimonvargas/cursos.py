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
## Diccionarios:
