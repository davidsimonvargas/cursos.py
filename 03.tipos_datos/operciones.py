# operaciones aritmeticas con numeros en python
# 1. suma - operador  binario
# variables globales
## son datos que se puden utiliosar en cualquier parte del software que este construyendo
# variables locales
## son datos que solo son acesibles en pequeñas porciones de codigo o " scope"
first_numb:int|float=20
second_numb:int|float=5 
print(f"la suma de {first_numb} + {second_numb} es: {first_numb+second_numb}")

print(f"la resta de {first_numb} - {second_numb} es: {first_numb-second_numb}")
#multi
print(f"la multiplicacion de {first_numb} * {second_numb} es: {first_numb*second_numb}")
#division
print(f"la division de {first_numb} / {second_numb} es: {first_numb/second_numb}")
#division exacta
print(f"la diviecax de {first_numb} // {second_numb} es: {first_numb//second_numb}")
##incremento OJO:(numero+=1)
print(f"el incremento de {first_numb} es: {++first_numb}")
##decremento(numero-=1)
print(f"el decremento de {first_numb} es: {--first_numb}")
##potencicion
print(f"la potenciacion de {first_numb} ** {second_numb} es: {first_numb**second_numb}")