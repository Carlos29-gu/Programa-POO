#Comparar en un supermecado

# creamos la clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# creamos otra calse Carro de Compras
class Carro_de_compras:
#Elaboramos 
    def __init__(self):
        self.productos = []  

    # Agregar producto al carro
    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto agregado: {producto.nombre}")

    # Calcular el total a pagar
    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    # Mostrar el contenido del carro
    def mostrar_carro_de_compra(self):
        print("Productos en el carro:")
        for producto in self.productos:
            print(f" - {producto.nombre}: ${producto.precio}")
        print(f"Total a pagar: ${self.calcular_total()}")


# Creación de productos
producto1 = Producto("Mantequilla", 2)
producto2 = Producto("Leche", 1)
producto3 = Producto("Arroz", 3)

# Creación del carro
carro = Carro_de_compras()

# Uso del sistema
carro.agregar_producto(producto1)
carro.agregar_producto(producto2)
carro.agregar_producto(producto3)

carro.mostrar_carro_de_compra()

    
    
