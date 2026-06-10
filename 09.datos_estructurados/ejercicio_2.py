# crear un programa que me permita agreagar a mi lista de compras los siguientes ingredientes (trucha,cebolla,limon,culandro,pinguita de mono, papa, cancha)
ingredientes:list[str]=[]

for i in range(7):
   ingrediente:str=input("ingrese ingrediente: ")
   ingredientes.append(ingrediente)
print(ingredientes)