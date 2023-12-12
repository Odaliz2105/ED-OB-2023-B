#Ejercicio 3
#Odaliz Balseca Valencia

num1=int(input("-Ingrese un numero:"))
num2=int(input("-Ingrese un numero:"))

print ("Ingrese el numero de operacion que desea realizar:")
print("--Opcion 1. SUMA")
print("--Opcion 2. RESTA")
print("--Opcion 3. MULTIPLICACION")
print("--Opcion 4. DIVISION")
print("--Opcion 5. POTENCIA")
print("--Opcion 6. MODULO")

opcion=int(input("Diguite el numero de opcion de su preferencia:"))
match opcion:
    case 1: 
        resultado=num1+num2
        print("La suma de los numeros es",resultado)
    case 2: 
        resultado=num1-num2
        print("La resta de los numeros es",resultado)
    case 3: 
        resultado=num1*num2
        print("La multiplicacion de los numeros es",resultado)
    case 4: 
        if num2 != 0:
            resultado = num1 / num2
            print("La division de los numeros es", resultado)
        else:
            print("No se puede dividir entre cero.")
    case 5: 
        resultado=num1**num2
        print("La potencia de los numeros es",resultado)
    case 6: 
        if num2 != 0:
            resultado = num1 % num2
            print("El modulo de los numeros es", resultado)
        else:
            print("No se puede calcular el modulo con cero.")
    case other: print("Ingrese una opcion valida")
    
print("Hecho por Odaliz Balseca")