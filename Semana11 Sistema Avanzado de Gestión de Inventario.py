import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Conviete el objeto a línea de texto 
    def to_line(self):
        return f"{self.__id},{self.__nombre},{self.__cantidad},{self.__precio}\n"

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        # Ahora usamos DICCIONARIO para búsqueda rápida por ID
        self.productos = {}  
        self.archivo = archivo
        self.cargar_desde_archivo()

    # Cargar inventario desde archivo
    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            open(self.archivo, "w").close()

        try:
            with open(self.archivo, "r") as file:
                for linea in file:
                    try:
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")
                        producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                        self.productos[id_producto] = producto
                    except ValueError:
                        print("Línea corrupta ignorada.")

            print("Inventario cargado correctamente.")

        except Exception as e:
            print(f"Error al cargar archivo: {e}")

    # Guarda el inventario en archivo
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos.values():
                    file.write(producto.to_line())

        except Exception as e:
            print(f"Error al guardar archivo: {e}")

    # Añade un nuevo producto
    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Ya existe un producto con ese ID.")
            return

        self.productos[producto.get_id()] = producto
        self.guardar_en_archivo()
        print("Producto añadido correctamente.")

    # Elimina el producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    # Actualiza el producto
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]

            if nueva_cantidad is not None:
                producto.set_cantidad(nueva_cantidad)

            if nuevo_precio is not None:
                producto.set_precio(nuevo_precio)

            self.guardar_en_archivo()
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    # Busca e producto por el nombre 
    def buscar_por_nombre(self, nombre):
        encontrados = []

        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                encontrados.append(producto)

        if encontrados:
            print("\nProductos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    # Muestra todos los prodcutos 
    def mostrar_todos(self):
        if self.productos:
            print("\nInventario Completo:")
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            elif opcion == "2":
                id_producto = input("ID a eliminar: ")
                inventario.eliminar_producto(id_producto)

            elif opcion == "3":
                id_producto = input("ID a actualizar: ")
                nueva_cantidad = input("Nueva cantidad (vacío = no cambiar): ")
                nuevo_precio = input("Nuevo precio (vacío = no cambiar): ")

                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

            elif opcion == "4":
                nombre = input("Ingrese el nombre a buscar: ")
                inventario.buscar_por_nombre(nombre)

            elif opcion == "5":
                inventario.mostrar_todos()

            elif opcion == "6":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Cantidad debe ser entero y precio número válido.")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    menu()
