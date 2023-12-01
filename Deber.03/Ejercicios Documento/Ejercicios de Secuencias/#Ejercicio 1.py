#Estructura de Secuencia
#Ejercicio 02

#Ejercicio 1
#El perímetro y área de un rectángulo dada su base y su altura.

base=float(input("Ingrese la base del rectangulo:"))
altura=float(input("Ingrese la altura del rectangulo:"))

perimetro=2 * (base + altura)
area=(base*altura)
print("El perimetro del rectangulo es:",perimetro)
print("El area del rectangulo es:",area)

#	El perímetro y área de un círculo dada su radio.
#Area=π* r^2

#Odaliz Balseca
import math
radio=float(input("Ingrese el radio del circulo:"))
area=(math.pi * radio ** 2)
perimetro=(2 * math.pi * radio)

print("El area del circulo es:",area)
print("El perimetro del circulo es:",perimetro)

