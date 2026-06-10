## deseamos agregar en una lista vacia los nombres de los paises que participaran en el mundial desarrollar el programa que haga posible esta tarea
#primera forma
paises:list[str]=[]
paises.append('Peru')
paises.append('Bolivia')
paises.append('Chile')
print(paises)
# segunda forma
pais:str=input("ingresa el nombre del pais: ")
paises.append (pais)
print(paises)
# tercera forma
rango:int=int(input("ingrese la cantidad de paises que deseas agregar: "))
for i in range(rango):
    nuevos_paises:str=input("ingrese un pais: ")
    paises.append(nuevos_paises)
print(paises)