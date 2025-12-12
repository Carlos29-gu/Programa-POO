# Programación tradicional con funciones

# Programa: Promedio semanal de temperaturas

# Función para ingresar las temperaturas diarias de la semana
def ingresar_temperaturas():
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    # Con esto podemos motrar por pantalla en mensaje que queremos dar 
    print("=== INGRESO DE LA TEMPERATURA SEMANAL ===")
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
    print(f"Temperaturas ingresadas: {temps}")
    print(f"Promedio semanal: {promedio:.2f} °C")


# Podemos ejecutar el programa 
main()
