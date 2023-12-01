#Ejercicio 3
#3.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. 
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos=int(input("Ingrese el tiempo en minutos:"))
horas = minutos // 60
minutos = minutos % 60

print(str(minutos) + " minutos son: " + str(horas) + " horas y " + str(minutos) + " minutos.")