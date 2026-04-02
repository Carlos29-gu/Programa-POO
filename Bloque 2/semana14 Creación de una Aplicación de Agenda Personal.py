# Importamos las librerías necesarias
import tkinter as tk
from tkinter import ttk, messagebox
import re  # Para validar formato de fecha y hora


#--------------------------------------------------------
# Funciones de la Aplicación


def validar_fecha(fecha):
    """
    Valida que la fecha tenga formato YYYY-MM-DD
    """
    patron = r"^\d{4}-\d{2}-\d{2}$"
    return re.match(patron, fecha)


def validar_hora(hora):
    """
    Valida que la hora tenga formato HH:MM
    """
    patron = r"^\d{2}:\d{2}$"
    return re.match(patron, hora)


def agregar_evento():
    """
    Agrega un evento al TreeView
    """
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    # Validar campos vacíos
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    # Validar formato
    if not validar_fecha(fecha):
        messagebox.showerror("Error", "Formato de fecha inválido (YYYY-MM-DD)")
        return

    if not validar_hora(hora):
        messagebox.showerror("Error", "Formato de hora inválido (HH:MM)")
        return

    # Insertar en la tabla
    tree.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar campos
    entry_fecha.delete(0, tk.END)
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)


def eliminar_evento():
    """
    Elimina el evento seleccionado
    """
    seleccion = tree.selection()

    if not seleccion:
        messagebox.showwarning("Error", "Seleccione un evento")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?")

    if confirmar:
        tree.delete(seleccion)


def salir():
    """
    Cierra la aplicación
    """
    ventana.quit()


# Ventana Principal

ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("650x400")


#----------------------------------------------
# FRAME 1 para Listas de Eventos


frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

# Creamos la tabla
columnas = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")

for col in columnas:
    tree.heading(col, text=col)
    tree.column(col, width=180)

tree.pack()


#-----------------------------------------
# FRAME 2 Entrada de Datos


frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Fecha
label_fecha = tk.Label(frame_entrada, text="Fecha (YYYY-MM-DD):")
label_fecha.grid(row=0, column=0, padx=5, pady=5)

entry_fecha = tk.Entry(frame_entrada)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

# Hora
label_hora = tk.Label(frame_entrada, text="Hora (HH:MM):")
label_hora.grid(row=1, column=0, padx=5, pady=5)

entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

# Descripción
label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=2, column=0, padx=5, pady=5)

entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)


#----------------------------------------
# FRAME 3 para los Botones 


frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=10)


# ----------------------------------------
# Ejecutar Programa


ventana.mainloop()
