
import os
import subprocess


# Muestra el código de un script

def mostrar_codigo(ruta_script):
    # Convierte la ruta del script en una ruta absoluta
    # Esto evita errores si el programa se ejecuta desde otra ubicación
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()
            print("\n" + "-" * 50)
            print(f"CÓDIGO DEL ARCHIVO: {os.path.basename(ruta_script)}")
            print("-" * 50 + "\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print(" El archivo no se encontró.")
        return None
    except Exception as e:
        print(f" Error al leer el archivo: {e}")
        return None



# Ejecutamos un Script Python

def ejecutar_codigo(ruta_script):
    try:
        # El metodo os.name verifica el sistema operativo
        if os.name == 'nt':  # Windows
        # Abre una nueva ventana de consola y ejecuta el script
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Linux / Mac/ 
            subprocess.Popen(['python3', ruta_script])
    except Exception as e:
        print(f" Error al ejecutar el código: {e}")


# Menu principal 

def mostrar_menu():
    # __file__ representa el archivo actual
    # dirname obtiene la carpeta donde está este programa
    ruta_base = os.path.dirname(__file__)

    # Detecta automáticamente las carpetas (unidades / semanas)
    carpetas = [f.name for f in os.scandir(ruta_base) if f.is_dir()]

    while True:
        print("\n MENU PRINCIPAL - DASHBOARD POO")
        print("-" * 40)

        for i, carpeta in enumerate(carpetas, start=1):
            print(f"{i} - {carpeta}")

        print("0 - Salir")

        opcion = input("Elige una carpeta o '0' para salir: ")

        if opcion == '0':
            print(" Saliendo del programa.")
            break

        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(carpetas):
                mostrar_sub_menu(os.path.join(ruta_base, carpetas[indice]))
            else:
                print(" Opción no válida.")
        except ValueError:
            print(" Opción no válida.")



# Creamos el submenú de carpetas

def mostrar_sub_menu(ruta_unidad):
    # Obtiene solo las subcarpetas dentro de la carpeta seleccionada
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print(f"\n Carpeta: {os.path.basename(ruta_unidad)}")
        print("-" * 40)

        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")

        print("0 - Regresar al menú principal")

        opcion = input("Elige una subcarpeta: ")

        if opcion == '0':
            break

        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
            else:
                print("❌ Opción no válida.")
        except ValueError:
            print("❌ Opción no válida.")



# Realizamos menú de scripts

def mostrar_scripts(ruta_sub_carpeta):
    # Filtra solo archivos .py dentro de la subcarpeta
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta)
               if f.is_file() and f.name.endswith('.py')]

    while True:
        print(f"\n Scripts en: {os.path.basename(ruta_sub_carpeta)}")
        print("-" * 40)

        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")

        print("0 - Regresar")
        print("9 - Menú principal")

        opcion = input("Elige un script: ")

        if opcion == '0':
            break
        elif opcion == '9':
            return

        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
        # Muestra el código del script seleccionado
                codigo = mostrar_codigo(ruta_script)

                if codigo:
                    ejecutar = input("\n¿Desea ejecutar el script? (1 = Sí, 0 = No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                    else:
                        print(" Script no ejecutado.")

                    input("\nPresiona Enter para continuar...")
            else:
                print(" Opción no válida.")
        except ValueError:
            print(" Opción no válida.")



# Hacemos la ejecución del programa 

if __name__ == "__main__":
    mostrar_menu()
