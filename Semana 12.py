class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Guardamos título y autor dentro de una TUPLA.
        # Se usa tupla porque es inmutable (no se puede modificar después).
        # Así garantizamos que el título y el autor no cambien.
        self.__info_principal = (titulo, autor)

        self.categoria = categoria
        self.isbn = isbn

    def get_titulo(self):
        # Accedemos al primer elemento de la tupla 
        return self.__info_principal[0]

    def get_autor(self):
        # Accedemos al segundo elemento de la tupla 
        return self.__info_principal[1]

    def __str__(self):
        # Este método permite imprimir el objeto de forma legible
        return f"Título: {self.get_titulo()}, Autor: {self.get_autor()}, Categoría: {self.categoria}, ISBN: {self.isbn}"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

        # Lista porque puede cambiar constantemente (agregar y quitar libros)
        self.libros_prestados = []

    def prestar_libro(self, libro):
        # Agrega el libro a la lista del usuario
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        # Verificamos que el libro esté en la lista antes de eliminarlo
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        # Si la lista está vacía, no tiene préstamos
        if not self.libros_prestados:
            print("No tiene libros prestados.")
        else:
            # Recorremos la lista e imprimimos cada libro
            for libro in self.libros_prestados:
                print(libro)

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

class Biblioteca:
    def __init__(self):
        # Diccionario para acceso rápido por ISBN
        # Estructura: {ISBN: objeto Libro}
        self.libros_disponibles = {}

        # Diccionario para acceder rápidamente a usuarios por ID
        # Estructura: {ID: objeto Usuario}
        self.usuarios = {}

        # Conjunto (set) para evitar IDs repetidos automáticamente
        # Un set no permite elementos duplicados
        self.ids_usuarios = set()


# Gestión de los Libros

    def añadir_libro(self, libro):
        # Verificamos que el ISBN no exista ya en el diccionario
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print("Libro añadido correctamente.")
        else:
            print("El libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        # Eliminamos el libro usando su clave (ISBN)
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print("Libro eliminado correctamente.")
        else:
            print("El libro no existe.")

# Gestión de Usuarios

    def registrar_usuario(self, usuario):
        # Verificamos que el ID no esté en el conjunto
        if usuario.id_usuario not in self.ids_usuarios:
            self.ids_usuarios.add(usuario.id_usuario)  # Se agrega al set
            self.usuarios[usuario.id_usuario] = usuario  # Se agrega al diccionario
            print("Usuario registrado correctamente.")
        else:
            print("El ID ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        # Eliminamos tanto del set como del diccionario
        if id_usuario in self.ids_usuarios:
            self.ids_usuarios.remove(id_usuario)
            del self.usuarios[id_usuario]
            print("Usuario eliminado correctamente.")
        else:
            print("El usuario no existe.")
            
# Préstamo y devolución de los libros 

    def prestar_libro(self, id_usuario, isbn):
        # Verificamos que el usuario exista y que el libro esté disponible
        if id_usuario in self.usuarios and isbn in self.libros_disponibles:

            # Obtenemos el usuario desde el diccionario
            usuario = self.usuarios[id_usuario]

            # pop() elimina el libro del diccionario y lo devuelve al mismo tiempo
            # Esto evita que el libro pueda prestarse dos veces
            libro = self.libros_disponibles.pop(isbn)

            # Se agrega el libro a la lista del usuario
            usuario.prestar_libro(libro)

            print("Préstamo realizado con éxito.")
        else:
            print("Usuario o libro no disponible.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]

            # Buscamos el libro dentro de la lista del usuario
            # porque ya no está en el diccionario principal
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:

                    # Lo eliminamos de la lista del usuario
                    usuario.devolver_libro(libro)

                    # Lo volvemos a agregar al diccionario de disponibles
                    self.libros_disponibles[isbn] = libro

                    print("Libro devuelto correctamente.")
                    return

            print("El usuario no tiene ese libro.")
        else:
            print("Usuario no encontrado.")

# Búsqueda de libros

    def buscar_por_titulo(self, titulo):
        # Recorremos todos los libros disponibles
        for libro in self.libros_disponibles.values():

            # lower() permite comparar sin importar mayúsculas/minúsculas
            if libro.get_titulo().lower() == titulo.lower():
                print(libro)

    def buscar_por_autor(self, autor):
        for libro in self.libros_disponibles.values():
            if libro.get_autor().lower() == autor.lower():
                print(libro)

    def buscar_por_categoria(self, categoria):
        for libro in self.libros_disponibles.values():
            if libro.categoria.lower() == categoria.lower():
                print(libro)

#Ejecucion del Programa Principal 

if __name__ == "__main__":

    biblioteca = Biblioteca()

    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "111")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "222")
    libro3 = Libro("1984", "George Orwell", "Distopía", "333")

    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)
    biblioteca.añadir_libro(libro3)

    usuario1 = Usuario("Carlos", "U001")
    usuario2 = Usuario("Ana", "U002")

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    biblioteca.prestar_libro("U001", "111")

    print("\nLibros prestados a Carlos:")
    usuario1.listar_libros()

    biblioteca.devolver_libro("U001", "111")

    print("\nBuscar por categoría 'Novela':")
    biblioteca.buscar_por_categoria("Novela")
