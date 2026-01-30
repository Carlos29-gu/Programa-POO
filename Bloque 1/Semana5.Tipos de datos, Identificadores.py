#Programa para calcular el área de un rectángulo
#Este programa pide datos al usuario, calcula el área y muestra el resultado

def calcular_area(base, altura):
    # Esta función recibe la base y la altura del rectángulo
    # Multiplica ambos valores para obtener el área
    area = base * altura
    # Devuelve el área calculada
    return area


#ENTRADA DE DATOS
# Pedimso al usuario que ingrese su nombre 
nombre_usuario = input("Ingrese su nombre: ")

# Se pide la base del rectángulo 
base = float(input("Ingrese la base del rectángulo: "))

# Se pide la altura del rectángulo
altura = float(input("Ingrese la altura del rectángulo: "))


#PROCESO

# Se llama a la función para calcular el área usando la base y la altura
area_rectangulo = calcular_area(base, altura)

# Se verifica si el área es mayor a 50
# Si es mayor, el resultado será True; si no, será False
es_area_grande = area_rectangulo > 50

# Se guarda la cantidad de cálculos realizados
cantidad_calculos = 1


#SALIDA DE DATOS

# Se muestran los resultados en pantalla
print("\nResultado")
print("Usuario:", nombre_usuario)
print("Área del rectángulo:", area_rectangulo)
print("¿El área es grande?", es_area_grande)
print("Cantidad de cálculos realizados:", cantidad_calculos)
