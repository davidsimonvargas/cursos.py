# modulos y librerira estandar py

# lilobreira estaqndar typing tipar datos a list y diccionario para hacer mas optimo el codigo.

# modulo es una porcion de codigo utilisable, para poder usarl nesecitamos importar la parte del codigop que deseamos utilizar.

# en este codigo estoy importando desde la libreria typing la funcion union,

# me permite tipar una coleccion de tipos de datos con uion los podemos pasar  una lista de los posibles tipo de datos que puede tener mi valor.

from typing import Union,Dict,List
alumno:dict[str:Union[str,int,float,bool]]={
    'id_alumno':1,
    'dni':78451289,
    'nombre':'mio',
    'edad':20,
    'matricula':True
}
# acceder
print(alumno['dni'])
# codigo erroneo print(alumno['tricula'])
## metodos
print(alumno.get('edad','valor no encontrado'))

# crear/modificar on valor
print(alumno)
alumno['nombre']='otro' #  si eciste la clave se actualiza el valor
alumno['ruc']=45612389745 # si no exixte la clave se crea
print(alumno)

# crear/modificar varios
alumno.update({'nombre':'celia','edad':15})
print(alumno)
alumno.update({'carrera':'agro','semestre':'III'})
print(alumno)
# eliminar
eliminado=alumno.pop('carrera')
print(f"el elemento eliminado: {eliminado}")
print(f"mi nuevo diccionario: {alumno}")

# sin libreria
# alumno:dict[str:str|int]



