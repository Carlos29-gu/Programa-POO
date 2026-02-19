import os  #Permite trabajar con archivos y verificar si existen

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
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

    #Este método convierte el objeto en una línea de texto
    #Sirve para guardar el producto dentro del archivo
    #Los datos se separan por comas para poder reconstruirlos luego
    def to_line(self):
        return f"{self.__id},{self.__nombre},{self.__cantidad},{self.__precio}\n"

    def __str__(self):
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        
        #Al iniciar el programa se cargan automáticamente
        #los datos guardados en el archivo.
        self.cargar_desde_archivo()

    # NUEVO: Cargar datos desde archivo
    def cargar_desde_archivo(self):
        try:
            #Verifica si el archivo existe.
            #Si no existe, lo crea automáticamente vacío.
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                print("Archivo creado automáticamente.")

            # Se abre el archivo en modo lectura.
            with open(self.archivo, "r") as file:
                for linea in file:
                    try:
                        #Se separan los datos usando la coma como delimitador.
                        id_producto, nombre, cantidad, precio = linea.strip().split(",")

                        #Se reconstruye el objeto Producto con los datos leídos.
                        producto = Producto(
                            id_producto,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )

                        self.productos.append(producto)

                    #Si una línea tiene formato incorrecto,
                    #el programa no se detiene, simplemente la ignora.
                    except ValueError:
                        print("Línea corrupta ignorada.")

            print("Inventario cargado correctamente.")

        #Maneja el caso en que no existan permisos de lectura.
        except PermissionError:
            print("No tienes permisos para leer el archivo.")

        #Captura cualquier otro error inesperado.
        except Exception as e:
            print(f"Error inesperado al cargar archivo: {e}")


    #Guardar datos en archivo
    def guardar_en_archivo(self):
        try:
            #Se abre el archivo en modo escritura.
            #Esto reemplaza el contenido anterior completamente.
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    #Se escribe cada producto convertido en texto.
                    file.write(producto.to_line())

            print("Cambios guardados correctamente en el archivo.")

        #Maneja el caso en que no existan permisos de escritura.
        except PermissionError:
            print("No tienes permisos para escribir en el archivo.")

        except Exception as e:
            print(f"Error inesperado al guardar: {e}")

    #Ahora cada modificación guarda automáticamente en el archivo.

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Ya existe un producto con ese ID.")
                return

        self.productos.append(producto)

        #Cada vez que se agrega un producto,
        #se actualiza el archivo automáticamente.
        self.guardar_en_archivo()

        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)

                #Se guarda el cambio en el archivo.
                self.guardar_en_archivo()

                print("Producto eliminado correctamente.")
                return

        print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:

                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                #También se guarda automáticamente después de actualizar.
                self.guardar_en_archivo()

                print("Producto actualizado correctamente.")
                return

        print("Producto no encontrado.")

    def mostrar_todos(self):
        if self.productos:
            print("\nInventario Completo:")
            for p in self.productos:
                print(p)
        else:
            print("El inventario está vacío.")


def menu():
    inventario = Inventario()

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar todos los productos")
        print("5. Salir")

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
                inventario.mostrar_todos()

            elif opcion == "5":
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
