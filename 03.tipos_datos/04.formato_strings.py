# utlizar tecnicas para unir string en un solo 
## concatenacion
## para esto usamos el operador de concatenacion
# cuando este operador se encuentra entre 2 textos se convierte en el operador de concatenacion y cuando esta entre 2 numeros es el operador de adcion(suma)
nombre:str = "noemi"
apellido:str = "noseprofesor"
nombre_completo:str = nombre+" "+apellido
print(nombre_completo) # salida: noemi noseprofesor

## opcion mas optima de concatencion
print(nombre,apellido)

## f - string(tarea)

# formato de string esto sirve para formatear string con variables de python y para su uso se requiere de una f antes de escribiri un string se debe encerrar entre llaves {}
nombre:str= "Gianfranco"
edad:int=14
# mensaje de salida me diga hola mi nombre es {} y tengo {}
print("hola mi nombre es",nombre,"y tengo",edad)

print(f"hola mi nonbre es {nombre} y tengo {edad}")

## plantillas de string
nombre_cliente:str=input("ingresa tu nombre ")
ruc_cliente:int=int(input("ingresa ruc "))
direccion_cliente:str=input("digite direccion ")
codigo_producto:str=input("ingrese codigo producto ")
nombre_producto:str=input("ingrese nombre producto ")
precio_unidad:float=float(input("el precio del producto "))
cantidad_producto:float=float(input("cantidad a comprar "))
precio_total:float=precio_unidad*cantidad_producto

plantilla:str=f""""
cliente: {nombre_cliente}....... RUC: {ruc_cliente}
Direccion: {direccion_cliente} ......

codigo producto         nombre producto     p_unidad        cantidad
--------------------------------------------------------------------
{codigo_producto}       {nombre_producto}   {precio_unidad} {cantidad_producto}
--------------------------------------------------------------------
el precio total de su compra es de :{precio_total}
"""
print(plantilla)





