import tkinter as tk
from tkinter import messagebox

# -------------------------------
# VENTANA PRINCIPAL
# -------------------------------
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("400x450")


tareas = []

# -----------------------------------------------------------------------
# FUNCIONES


def actualizar_lista():
    """
    Actualiza visualmente la lista de tareas
    """
    lista_tareas.delete(0, tk.END)
    
    for i, tarea in enumerate(tareas):
        texto = tarea["texto"]
        
        if tarea["completada"]:
            lista_tareas.insert(tk.END, "/ " + texto)
            lista_tareas.itemconfig(i, fg="gray")
        else:
            lista_tareas.insert(tk.END, texto)
            lista_tareas.itemconfig(i, fg="black")


def añadir_tarea(event=None):
    """
    Añade una nueva tarea
    """
    texto = entrada.get().strip()
    
    if texto == "":
        messagebox.showwarning("Advertencia", "Escribe una tarea")
        return
    
    tareas.append({"texto": texto, "completada": False})
    entrada.delete(0, tk.END)
    
    actualizar_lista()


def completar_tarea(event=None):
    """
    Marca como completada la tarea seleccionada
    """
    try:
        indice = lista_tareas.curselection()[0]
        tareas[indice]["completada"] = True
        actualizar_lista()
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea")


def eliminar_tarea(event=None):
    """
    Elimina la tarea seleccionada
    """
    try:
        indice = lista_tareas.curselection()[0]
        tareas.pop(indice)
        actualizar_lista()
    except:
        messagebox.showwarning("Advertencia", "Selecciona una tarea")


def cerrar_app(event=None):
    ventana.quit()


# -------------------------------
# INTERFAZ


# Campo de entrada
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Botón de añadir
btn_agregar = tk.Button(ventana, text="Añadir Tarea", command=añadir_tarea)
btn_agregar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=40, height=15)
lista_tareas.pack(pady=10)

# Botón de completar tarea
btn_completar = tk.Button(ventana, text="Marcar como completada", command=completar_tarea)
btn_completar.pack(pady=5)

# Botón eliminar
btn_eliminar = tk.Button(ventana, text="Eliminar tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# ---------------------------------------------------------------
# ATAJOS DE TECLADO


ventana.bind("<Return>", añadir_tarea)     # Enter - añadir tarea
ventana.bind("<Tab>",  completar_tarea) # Tab - completar tarea
ventana.bind("<Delete>", eliminar_tarea)  # Delete - eliminar
ventana.bind("<Escape>", cerrar_app)      # Escape - salir

# ---------------------------------------------------------------
# EJECUCIÓN

ventana.mainloop()
