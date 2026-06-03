lista_vacia:list=[]
print(len(lista_vacia))
# por regla  el nombre de la variable no debe tener el tipo de dato que se va almacenar.
amores:list[str]=['wicho','pocohuanca','cesar','guido','percy']
print(f"la cantidad de elementos que tiene la variable amores es: {len(amores)}")

frutas:list[str]=['🍎','🍌','🍒','🍑']
# posicion o indice
# acceder al tercer elemento
print(frutas[2])
#acceder al segundo elemento por su indice negativo
print(frutas[-3])

## modificar el ultimo elemento con un nanaranja
frutas[-1]="🍊"
print (frutas)

### slicing
ciudades:list[str]=['lima','ica','chincha','pauza','urcos']
#si deseamos que los datos extraidos sean persistentes o se mantengan almacenados durante la ejecucion de mi programa los almaceni en una variable
datos_extraidos:list[str]=ciudades[-2:]
#si solo deseo mostrar y no almacenar el slicing lo realizo en el print
print (ciudades[0:3])
print(datos_extraidos)

## REMPLAZODE ELEMENTOS POR SLICING
num_pares:list[int]=[1,3,5,6,8,10]
print(num_pares)
num_pares[0:3]=[2,4]
print(f"mi lista modificada es:{num_pares}")
