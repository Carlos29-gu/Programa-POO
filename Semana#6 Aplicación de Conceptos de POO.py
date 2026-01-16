# Ponemos la clase base empleado

class Empleado:
    def __init__(self, nombre, salario):
        # Atributos que van a ser encapsulados 
        self.__nombre = nombre
        self.__salario = salario

    # Métodos getters de encapsulación
    def get_nombre(self):
        return self.__nombre

    def get_salario(self):
        return self.__salario

    # Método que será sobrescrito de polimorfismo para calcular el bono
    def calcular_bono(self):
        return self.__salario * 0.10
    
    def mostrar_info(self):
        print(f"Empleado: {self.__nombre}, Salario: ${self.__salario}")

# Ponemos la clase derivada gerente 
# Derivado de la clase base Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        # Llamamos al constructor de la clase base
        super().__init__(nombre, salario)
        self.departamento = departamento

    # Utilizamos el polimorfismo para sobrescribir el método
    def calcular_bono(self):
        return self.get_salario() * 0.20

    def mostrar_info(self):
        print(
            f"Gerente: {self.get_nombre()}, "
            f"Departamento: {self.departamento}, "
            f"Salario: ${self.get_salario()}"
        )

        
# PROGRAMA PRINCIPAL

if __name__ == "__main__":
    # Ponemos lo que se va a mostrar en pantalla
    empleado1 = Empleado("Carlos", 850)
    gerente1 = Gerente("Ana", 2000, "Finanzas")

    # Usamos los metodos a ejecutar 
    empleado1.mostrar_info()
    print("Bono del empleado:", empleado1.calcular_bono())

    print("---------------------------")

    gerente1.mostrar_info()
    print("Bono del gerente:", gerente1.calcular_bono())
