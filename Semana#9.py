class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos privados
        # Esto evita que se modifiquen directamente desde fuera de la clase
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    # Método especial que define cómo se imprime el objeto
    # Se ejecuta automáticamente cuando usamos print
    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"

class Inventario:
    def __init__(self):
        # Lista que almacenará todos los objetos de tipo Producto
        self.productos = []

    def añadir_producto(self, producto):
        # Se recorre la lista para verificar que el ID no esté repetido
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return  # Se detiene la función si el ID ya existe

        # Si no se encontró un ID repetido, se agrega el producto
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        # Se busca el producto por ID dentro de la lista
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)  # Se elimina el objeto de la lista
                print("Producto eliminado correctamente.")
                return
        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        # Se busca el producto por ID
        for p in self.productos:
            if p.get_id() == id_producto:
                
                # Solo se actualiza si el usuario ingresó un valor
                # Si deja vacío, el valor no se modifica
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                print("Producto actualizado correctamente.")
                return
        print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        # List comprehension: crea una nueva lista con los productos
        # cuyo nombre contenga el texto ingresado (búsqueda parcial)
        # lower() permite que la búsqueda no distinga mayúsculas/minúsculas
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

        if encontrados:
            print("Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        # Verifica si la lista está vacía
        if self.productos:
            print("\nInventario Completo:")
            for p in self.productos:
                print(p)
        else:
            print("El inventario está vacío.")

def menu():
    inventario = Inventario()  # Se crea una instancia del inventario

    while True:  # Bucle infinito hasta que el usuario elija salir
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                # Conversión de datos para asegurar tipos correctos
                id_producto = input("Ingrese ID del producto: ")
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))  # Convertido a entero
                precio = float(input("Ingrese precio: "))    # Convertido a decimal

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            # Captura error si el usuario escribe algo que no sea número
            except ValueError:
                print("Error: Cantidad debe ser entero y precio debe ser número.")

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            try:
                nueva_cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
                nuevo_precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")

                # Operador ternario:
                # Si el usuario deja vacío, se guarda como None
                # Si escribe algo, se convierte al tipo correspondiente
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

            except ValueError:
                print("Error: Datos inválidos.")

        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break  # Rompe el bucle while y termina el programa

        else:
            print("Opción inválida. Intente nuevamente.")

# Este bloque solo se ejecuta si el archivo se corre directamente
if __name__ == "__main__":
    menu()

