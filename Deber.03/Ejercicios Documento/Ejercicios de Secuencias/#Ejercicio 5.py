#Ejercicio 5
#Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. 
#Dicha calificación se compone de los siguientes porcentajes:
    # 55% del promedio de sus tres calificaciones parciales.
    # 30% de la calificación del examen final.
    # 15% de la calificación de un trabajo final.

nota1=float(input("Ingrese su nota 1 al parcial:"))
nota2=float(input("Ingrese su nota 2 al parcial:"))
nota3=float(input("Ingrese su nota 3 al parcial:"))
examen_final=float(input("Ingrese su nota del examen final:"))
trabajo_final=float(input("Ingrese su nota del trabajo final:"))

promedio=(nota1+nota2+nota3)*0.55
c_examen_final=examen_final*0.30
c_trabajo_final=trabajo_final*0.15
calificacion_final=(promedio+c_examen_final+c_trabajo_final)/3

print("Su calificacion final en la materia de Algoritmos:",calificacion_final)


