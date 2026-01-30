# Programa Registro y Eliminación de Estudiantes

class Estudiante:
        # EL Constructor(__init__)
        # Este método se ejecuta automáticamente cuando se crea
        # un objeto de la clase Estudiante.
        # Aquí se inicializan los atributos del objeto nombre y curso 
    def __init__(self, nombre, curso):

        # Se guarda el nombre del estudiante y del curso del estudiante
        self.nombre = nombre      
        self.curso = curso        
        print(f"Estudiante registrado: {self.nombre} en el curso {self.curso}")

    def mostrar_datos(self):
       
        # Este método muestra los datos del estudiante.
       
        print(f"Nombre: {self.nombre}")
        print(f"Curso: {self.curso}")

    def __del__(self):
       
        # Este método DESTRUCTOR (__del__) se ejecuta cuando el objeto es eliminado       
        # de la memoria o cuando termina el programa.
       
        print(f"Registro del estudiante '{self.nombre}' eliminado de la memoria.")


# PROGRAMA DE EJECUCION PRINCIPAL 
# Aquí se crean dos objetos de la clase Estudiante
# Al crearlos, se ejecuta automáticamente el __init__
est1 = Estudiante("Ana", "Programación")
est2 = Estudiante("Luis", "Matemáticas")

# Llamamos al método mostrar_datos para cada objeto
est1.mostrar_datos()
est2.mostrar_datos()

print("Eliminando objetos...")

# Aquí eliminamos manualmente el objeto est1
# Al hacerlo, se ejecuta el método __del__
del est1

print("Fin del programa.")
