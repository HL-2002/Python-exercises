"""
Escribir una factura de supermercado que incluya el nombre y apellido del 
cliente, su dirección, y el nombre, cantidad y precio de los productos
comprados (incluyendo IVA si no son productos de origen vegetal)
"""

# Inicializar variables
nombre = direccion = producto = tipo = ""
cantidad = 0
valor = precio = iva = 0.0
productos = []
continuar = 1

# Proceso
nombre = input("Nombre y Apellido del cliente: ")
direccion = input("Dirección del cliente: ")

# Ingreso de productos
while continuar == 1:
    producto = input("Ingrese datos del producto 'Nombre, vegetal/otro, cantidad, valor': ")
    productos.append(producto)
    continuar = int(input("Escriba 1 para continuar, 0 para terminar: "))

# Procesamiento de factura
print("\033[H\033[J", end="")
print("Factura \nCliente: {0:15} \nDirección: {1:15}".format(nombre,direccion), end="\n\n")
print("Producto          Cantidad     Precio")
for n in productos:
    (producto, tipo, cantidad, valor) = n.split(", ")
    cantidad = int(cantidad)
    valor = float(valor)
    precio = cantidad * valor

    if tipo != ("vegetal" or "Vegetal"):
        iva = precio * 0.16
        precio += iva

    print("{0:15}         {1:2d}     {2:5.2f}".format(producto,cantidad,precio))