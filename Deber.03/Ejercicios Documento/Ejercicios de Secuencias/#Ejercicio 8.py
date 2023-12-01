#Ejercicio 8
#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. 
#El que está detrás viaja a una velocidad mayor. 
#Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) 
#y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

velocidad1 = int(input("Ingrese la velocidad del primer vehículo: "))
velocidad2 = int(input("Ingrese la velocidad del segundo vehículo: "))
distancia = int(input("Ingrese la distancia entre los dos vehículos: "))

tiempo_en_horas = distancia / (velocidad1 - velocidad2)

tiempo_en_minutos =int(tiempo_en_horas * 60)
print("El vehículo más rápido alcanzará al otro en:", tiempo_en_minutos, "minutos")
