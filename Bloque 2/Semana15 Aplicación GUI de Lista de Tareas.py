# Importamos Tkinter
import tkinter as tk
from tkinter import messagebox

# Ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("400x400")

# ---------------------------------------------------
# Lista donde guardaremos las tareas

# ---------------------------------------------------
tareas = []

# ------------------------------
# Funciones


def añadir_tarea(event=None):
    """
    Esta función se ejecuta cuando se presiona el botón
    'Añadir Tarea' o la tecla Enter.
    """
    texto = entrada.get()

    # Validamos que no esté vacío
    if texto == "":
        messagebox.showwarning("Aviso", "Escribe una tarea")
        return

    # Agregamos la tarea como diccionario
    tarea = {"texto": texto, "completada": False}
    tareas.append(tarea)

    actualizar_lista()
    entrada.delete(0, tk.END)  # Limpia el campo de texto


def actualizar_lista():
   
    #Esta función actualiza el Listbox
    #Recorre todas las tareas y las muestra
    

    #Si la tarea está completada, se muestra con *
    
    lista_tareas.delete(0, tk.END)  # Limpia la lista visual

    for tarea in tareas:
        if tarea["completada"]:
            lista_tareas.insert(tk.END, "* " + tarea["texto"])
        else:
            lista_tareas.insert(tk.END, tarea["texto"])


def marcar_completada(event=None):

    #Marca una tarea como completada.


    #Usamos curselection() para saber qué tarea seleccionó el usuario
    #Cambiamos su estado a True

    try:
        indice = lista_tareas.curselection()[0]
        tareas[indice]["completada"] = True
        actualizar_lista()
    except:
        messagebox.showwarning("Aviso", "Selecciona una tarea")


def eliminar_tarea():
   
    #Elimina la tarea seleccionada de la lista.
    
    try:
        indice = lista_tareas.curselection()[0]
        tareas.pop(indice)
        actualizar_lista()
    except:
        messagebox.showwarning("Aviso", "Selecciona una tarea")


def doble_click(event):
   

    #Si haces doble clic en una tarea, se marca como completada.
    marcar_completada()



# Componentes de la Interfaz
# ------------------------------

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Permite usar ENTER para añadir tarea
entrada.bind("<Return>", añadir_tarea)

# Botón añadir
btn_añadir = tk.Button(ventana, text="Añadir Tarea", command=añadir_tarea)
btn_añadir.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(ventana, width=40, height=10)
lista_tareas.pack(pady=10)

# Evento doble clic
lista_tareas.bind("<Double-Button-1>", doble_click)

# Botón completar
btn_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

# Botón eliminar
btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# ------------------------------
# Ejecución 
ventana.mainloop()
