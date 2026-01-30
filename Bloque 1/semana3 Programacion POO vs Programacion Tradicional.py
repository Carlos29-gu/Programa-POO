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
        print("=== INGRESO DE TEMPERATURA SEMANAL(POO) ===")
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
    print(f"Promedio semanal: {promedio:.2f} °C")


# Ahora podemos Ejecutar el programa 
main()


#=================================
# Programación tradicional 
# Programa: Promedio semanal de temperaturas

# Función para ingresar las temperaturas diarias de la semana
def ingresar_temperaturas():
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    # Con esto podemos motrar por pantalla en mensaje que queremos dar 
    print("=== INGRESO DE LA TEMPERATURA SEMANAL Programación Tradicional ===")
    for dia in dias:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temp)

    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio


# Función principal que ayuda a organizar el programa
def main():
    # Con esto podemos ingresamos los datos diarios
    temps = ingresar_temperaturas()

    # Ahora podemos calcular el promedio semanal 
    promedio = calcular_promedio(temps)

    # Mostrara los resultados calculados 
    print("\n=== RESULTADO ===")
    print(f"Promedio semanal: {promedio:.2f} °C")


# Podemos ejecutar el programa 
main()
