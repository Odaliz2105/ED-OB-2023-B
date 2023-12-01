#Ejercicio 1
#1.	Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

cadena=input("Ingrese una palabra: ")
resultado=cadena.isupper()
if resultado:
    print("La palabra ingresada contiene al menos una letra mayúscula.")
else:
    print("La palabra ingresada no contiene letras mayúsculas.")