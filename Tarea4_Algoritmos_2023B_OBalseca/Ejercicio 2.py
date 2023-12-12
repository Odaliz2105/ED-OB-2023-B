#Correcion de la prueba con la sentencia SWITCH Case
#Odaliz Balseca Valencia
print ("****Bienvenidos al Carbonero****")
print ("Ingrese los datos para su factura por favor ")
nombre=input("-Ingrese su nombre:")
cedula=int(input("-Ingrese su numero de cedula:"))
correo=input("-Ingrese su correo electronico:")

print("Le ofrecemos los siguientes tipos de hamburguesas:")
print("--Opcion 1. SENCILLA")
print("--Opcion 2. DOBLE")
print("--Opcion 3. TRIPLE")
opcion=int(input("Diguite el numero de opcion de su preferencia:"))
match opcion:
    case 1: precio=1.50
    case 2: precio=2.50
    case 3: precio=2.50
    case other: print("Lo sentimos en el Carbonero no ofrecemos ese tipo de hamburguesas")

cantidad_hamburguesas = int(input("Ingrese la cantidad de hamburguesas que desea comprar: "))
subtotal = cantidad_hamburguesas * precio

print("Por favor ingrese el metodo de pago")
print("Seleccione la forma de pago:")
print("--Opcion 1. TARJETA DE CREDITO")
print("--Opcion 2. EFECTIVO")

pago=int(input("Diguite el metodo de pago de su preferencia:"))
match pago:
    case 1: 
        cargo_tarjeta = subtotal * 0.05 
        total_pagar = subtotal + cargo_tarjeta
        print("Su pago es con tarjeta de credito, debera pagar el 5% adicional del pago:", cargo_tarjeta)
        print("Total a pagar: ", total_pagar)
    case 2: print("Su pago es en efectivo, por favor cancele su pedido sin recarga:", subtotal)
    case other: print("El tipo de pago que ingreso no es válido")

print("Muchas gracias por su compra", nombre, "vuelva pronto :)")
print("Su factura sera enviada a su correo electronico")
print("Hecho por Odaliz Balseca")