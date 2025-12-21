#Comprar en una tienda viveres
#Caso de la vida real la compra de viveres en una tienda 
#coolocamos los productos en un carro de compras y calculamos el precio total 

# creamos la clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# creamos otra calse Carro de Compras
# En esta clase van a ir todas las compras que vamos a realizar
class Carro_de_compras:
#encasuplamos los atributos
    def __init__(self):
        self.productos = []  

    # Agregar producto al carro
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto agregado: {producto.nombre}")

    # Calculamos el total a pagar
    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    # Mostraamos el contenido del carro de compras
    def mostrar_carro_de_compra(self):
        print("Productos en el carro:")
        for producto in self.productos:
            print(f" - {producto.nombre}: ${producto.precio}")
        print(f"Total a pagar: ${self.calcular_total()}")


# Creamos los productos
producto1 = Producto("Mantequilla", 2)
producto2 = Producto("Leche", 1)
producto3 = Producto("Arroz", 3)

# Creación del carro
carro = Carro_de_compras()

# Mostramos los productos y el total a pagar 
carro.agregar_producto(producto1)
carro.agregar_producto(producto2)
carro.agregar_producto(producto3)

carro.mostrar_carro_de_compra()

    
 
