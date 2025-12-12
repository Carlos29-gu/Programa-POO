#Programación Orientada a Objetos 

# Programa: Promedio semanal de temperaturas (POO)

# Colocamos la clase Padre 
class RegistroClima:
    def calcular_promedio(self):
        # metodo base para calcular el promedio del clima
        return 0
    
# Heredamos a la Clase hija 
class ClimaSemanal(RegistroClima):

    def __init__(self):
        # Estos atributos van hacer encapsulados 
        self.__temperaturas = []
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Metodo para poder ingresar la temperatura de cada día de la semana
    def ingresar_temperaturas(self):
    # Con esto podemos motrar por pantalla en mensaje que queremos dar 
        print("=== INGRESO DE TEMPERATURA SEMANAL ===")
        for dia in self.dias:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.__temperaturas.append(temp)

    # Usamos get para poder obtener el valor encapsulado fuera de la clase
    def get_temperaturas(self):
        return self.__temperaturas

    # El metodo base que pusimos modificamos usamos la tecnica de polimorfismo 
    def calcular_promedio(self):
        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)


# Función principal del programa 
def main():
    clima = ClimaSemanal()

    # Podremos ingresar los datos de las temperaturas 
    clima.ingresar_temperaturas()

    # Con esto podremos calcular el promedio semanal
    promedio = clima.calcular_promedio()

    # Esto mostrara el resultado calculado
    print("\n=== RESULTADOS ===")
    print("Temperaturas registradas:", clima.get_temperaturas())
    print(f"Promedio semanal: {promedio:.2f} °C")


# Ahora podemos Ejecutar el programa 
main()
