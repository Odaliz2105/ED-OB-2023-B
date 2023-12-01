#Ejercicio 9
#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
#Odaliz Balseca

nombre = input("Ingrese su nombre:")
apellido1 = input("Ingrese su primer apellido:")
apellido2 = input("Ingrese si segundo apellido:")

inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]

inicial = inicial.upper()
print("Las iniciales son:",inicial)

