#crear asiendo uso de las practicas anteriores , un acalculadora 
# que pirda al usuario dos numeros enteros y luego
# de manera ordenada mostrar por tertminal el resultado
print("""
======================================
=   Bienvenido a la calculadora      =
======================================
""")
num1:int= int(input("Ingresa el primer número entero : "))
num2:int= int(input("Ingresa el segundo número entero: "))
print(f"la suma de : {num1} + {num2} es = {num1+num2} ")
print("""
========================================
=     Gracias por usar la calculadora  =
========================================
""")


mensaje_bienvenida:str="""
======================================
=    Bienvenido a la calculadora     =
======================================
"""
print(mensaje_bienvenida)
print("A continuacion ingrese dos numeros para realizar la suma")
numero_uno:int=int(input("ingrese el primer numero: "))

numero_dos:int=int(input("ingrese el primer numero: "))
resultado_suma:int=numero_uno+numero_dos
mensaje_resultado:str=f"""
    el resultado de la suma del numero
    {numero_uno}
    con el numero
    {numero_dos}
    es igual a {resultado_suma}
"""
print (mensaje_resultado)