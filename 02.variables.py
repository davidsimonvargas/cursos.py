# para declarar una variable en pyton usaremos la convencion snake_case
## reglas 
### 1. el nombre de la variable debe indicar que dato se esta almacenando.
### 2. las variables no deben contener numeros ni caracteres especiales(@,/,!,?).
nombre_curso="lenguaje de programacion"
creditos_curso=3
horas_semanales_curso=6
# ADVERTENCIA - las variables son mutables
print(creditos_curso) #salida: 3
creditos_curso=10
print(creditos_curso) #salida: 10

#NOTA IMPORTANTE PRA TODO EL CURSO - cada ves que declaremos variables usaremos anotaciones para indicar que tipo de datos sr va a almacenar

nombre_alumno:str = "deduardo"
edad_alumno:int = 28
estatura_alumno:float = 1.59
asistencia_alumno:bool = True
amigos_alumno:list = []
direccion_alumno:dict = {
"n_calle":"psj belen",
"numero_casa":230,
"barrio":"ccayao"
}

# asignacion de una variable a otra variable
edad_alumno: int = 20
edad_docente: int = edad_alumno

## IMPORTANTE NO OLVIDAR
### un decorador en python nos indica qye tipo de dato va a almacenar nuestra variable:
### los decoradores de python trae por defecto son:

############ Datos primitivos ############
# decoradores para datos primitivos
### : int - enteros
### : float - decimal, coma flotante
### : str - string texto
### : bool - datos boleanos True o False

############ Datos estructurados ############
# decoradores para datos estructurados
### : list - litas
### : dict - diccionario

## como hacemos yso de las variables
## para hacer uso del dato almacenado en una variable basta con hacer el llamado del nombre de la variable:
primer_numero: int = 30
segundo_numero: int = 20
suma: int = primer_numero+segundo_numero

