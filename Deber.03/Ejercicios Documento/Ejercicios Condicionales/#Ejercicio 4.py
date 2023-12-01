#Ejercicio 4
#4.	Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. 
#El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:

#Si se cumple Pitágoras entonces es triángulo rectángulo
	#Si sólo dos lados del triángulo son iguales entonces es isósceles.
	#Si los 3 lados son iguales entonces es equilátero.
	#Si no se cumple ninguna de las condiciones anteriores, es escaleno.

#Odaliz Balseca

a=float(input("Ingrese el lado A del triangulo: "))
b=float(input("Ingrese el lado B del trinagulo: "))
c=float(input("Ingrese el lado C del triangulo: "))
if (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
    print("Es un triangulo rectangulo")
elif a==b==c:
    print("Es un triangulo equilatero")
elif a==b or a==c or b==c:
    print("Es un triangulo isosceles") 
else:
    print("Es un triangulo escaleno")
