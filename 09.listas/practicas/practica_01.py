## una ferreteria tiene separada en dos listas los siguientes productos
"""""
1. lista de productos de limpieza (10 productos)
2. lista de materiales de construccion (10 productos)
---------------------------------------------------------
el dueño desea realizar ls siguientes acciones:
1. en su lista de productos de limpieza existe un material de construccion,
debes eliminarlos y pasar el producto a la lista que corresponde.
2. indicar si en la lista de M.C exisye cemento
3. eb la lista de P.L buscar el producto lejia y su valor por lejia sapolio
4. mostrar un mensaje donde se detalle cual es la listade M.C y la lista de P.L formateado.
"""

Productos_limpiesa:list[str]=["Detergente multiusos","Lejía","Desengrasante","Limpiavidrios","trapeador","escoba","Paños de microfibra","Detergente lavavajillas","piedra chancada","Limpiador de baños"]
print(Productos_limpiesa)
materiales_construccion:list[str]=["Cemento","Hormigón","Acero","Ladrillos","Madera","Vidrio","Arena","Bloques de hormigón","Yeso","Fibrocemento"]
print(materiales_construccion)

# 1. 
print(Productos_limpiesa.index("piedra chancada"))
elemento_retirado=Productos_limpiesa.pop(Productos_limpiesa.index("piedra chancada"))
print(Productos_limpiesa)
materiales_construccion.append(elemento_retirado)
print(materiales_construccion)

#2. 
existe:bool="Cemento" in materiales_construccion 
print(f"existe cemento en la lista materiales_construccion: {existe}") 
print("cemento si existe" if existe else "cemento no existe")
#3. 
buscar=Productos_limpiesa.index("Lejía")
Productos_limpiesa[buscar]='LEJIA SAPOLIO'
print(Productos_limpiesa)

#4. 
mensaje_bienvenida:str="""
======================================
=   LISTA DE PRODUCTOS DE LIMPIEZA   =
======================================
"""
print(F"{mensaje_bienvenida} {Productos_limpiesa}")
mensaje_bienvenida:str="""
=======================================
= LISTA DE MATERIALES DE CONSTRUCCION =
=======================================
"""
print(F"{mensaje_bienvenida} {materiales_construccion}")