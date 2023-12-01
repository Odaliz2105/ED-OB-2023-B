#Ejercicio 4
# Odaliz Balseca
#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas
#el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas 
#que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

sueldoBase=float(input("Ingrese su sueldo:"))
venta01= float(input("Ingrese el dinero de la venta 1 :"))
venta02= float(input("Ingrese el dinero de la venta 2 :"))
venta03= float(input("Ingrese el dinero de la venta 3 :"))
totalDeVenta = venta01 + venta02 + venta03
comision = totalDeVenta * 0.10 
print("El pago por las ventas realizadas en el mes:", comision)
total = sueldoBase + comision 
print("El pago al mes es:", total)