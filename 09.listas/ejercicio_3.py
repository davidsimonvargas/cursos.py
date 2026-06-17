alumnos:list[str]=['deduardo','noemi','victor','emerson','yo']
print(alumnos)
# eliminar por valor
alumnos.remove('yo')
print(alumnos)
# eliminar el ultimo valor por defecto
alumnos.pop()
print(alumnos)
## pop tambien elimina elementos por indice 
### el metodo pop tinene la caractersica de recuperar el elemebto eliminado eso quiere decir que lo podemos almacenar en una variable

a=alumnos.pop(1)
print(a)
print(f"mi lista de desaprobados sera:{alumnos}")

## tengo una lista marcas de vehiculos (toyota,nissan,datsun,daewod,simo mack,mazda,honda) crear un programa que realise lo siguiente 
""""
1. eliminar el 5 elemento
2. en su lugar agregar la marca mitsubishi
3. buscar nissan y mostrar su valor por terminal
4. mostrar si exite honda en mi lista de vehiculos
"""

marca_vehiculos:list[str]=['toyota','nissan','datsun','daewod','simo mack','mazda','honda']
print(marca_vehiculos)

marca_vehiculos.pop(4)
print(marca_vehiculos)

marca_vehiculos.insert(4,"mitsubishi")
print(marca_vehiculos
      )
buscar:int=marca_vehiculos.index("nissan")
print(marca_vehiculos[buscar])
print(f"valor de nissan es: {buscar}")

existe:bool="honda" in marca_vehiculos
print(f"honda se encuentra en mi lista de marcas: {existe}")
