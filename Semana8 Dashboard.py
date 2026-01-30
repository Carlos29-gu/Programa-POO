import os
import subprocess

def mostrar_codigo(ruta_script):
    # Convierte la ruta a absoluta para evitar errores
    # si el programa se ejecuta desde otra carpeta
    ruta_script_absoluta = os.path.abspath(ruta_script)

    try:
        # Abre el archivo en modo lectura con codificación utf-8
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            codigo = archivo.read()

            print("\n" + "-" * 50)
            print(f"CÓDIGO DEL ARCHIVO: {os.path.basename(ruta_script)}")
            print("-" * 50 + "\n")
            print(codigo)

            return codigo

    except FileNotFoundError:
        # Evita que el programa se caiga si el archivo no existe
        print(" El archivo no se encontró.")
        return None

    except Exception as e:
        print(f" Error al leer el archivo: {e}")
        return None



# Funciónde Ejecutar un script 

def ejecutar_codigo(ruta_script):
    try:
        # os.name detecta el sistema operativo
        # 'nt' significa Windows
        if os.name == 'nt':
            # Abre una nueva consola y ejecuta el script
            # /k mantiene la ventana abierta
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:
            # Para Linux o Mac
            subprocess.Popen(['python3', ruta_script])

    except Exception as e:
        print(f" Error al ejecutar el código: {e}")


# Menú principal
def mostrar_menu():
    # __file__ representa este archivo (Dashboard)
    # dirname obtiene la carpeta donde está ubicado
    ruta_base = os.path.dirname(__file__)

    # os.scandir detecta automáticamente las carpetas
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
            # Captura letras u otros valores inválidos
            print(" Opción no válida.")

# Submenú de carpetas
def mostrar_sub_menu(ruta_unidad):
    # Detecta solo subcarpetas dentro de la carpeta seleccionada
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    # Si no hay subcarpetas (como en Bloque 1)
    # entra directamente a mostrar scripts
    if not sub_carpetas:
        mostrar_scripts(ruta_unidad)
        return

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

# Menú de scripts
def mostrar_scripts(ruta_sub_carpeta):
    # Filtra solo archivos .py
    scripts = [
        f.name for f in os.scandir(ruta_sub_carpeta)
        if f.is_file() and f.name.endswith('.py')
    ]

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

                # Muestra el código antes de ejecutarlo
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

# Ejecucion del programa 
if __name__ == "__main__":
    mostrar_menu()


