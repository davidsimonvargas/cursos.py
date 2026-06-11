# crear un programa que me permita agreagar a mi lista de compras los siguientes ingredientes (trucha,cebolla,limon,culandro,pinguita de mono, papa, cancha)
ingredientes:list[str]=[]

for i in range(7):
   ingrediente:str=input("ingrese ingrediente: ")
   ingredientes.append(ingrediente)
print(ingredientes)
## crear un programa que agregue al principio de la lista el grupo A de los paises en el mundial:
grupo_A:list[str]=[]

grupo_A.insert(0,"rep.checa")
# ["rep. checa"]
grupo_A.insert(0,"corea del sur")
# ["corea del sur","rep. checa"]
grupo_A.insert(0,"sudafrica")
# ["sudafrica","corea del sur","rep. checa"]
grupo_A.insert(0,"mexico")
# ["mexico","sudafrica","corea del sur","rep. checa"]
print(grupo_A)
