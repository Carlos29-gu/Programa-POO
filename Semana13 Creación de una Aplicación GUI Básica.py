# Importamos la librería Tkinter para crear interfaces gráficas
import tkinter as tk
from tkinter import messagebox

#Las funciones de las Aplicaciones 

def agregar_dato():
    
    dato = entrada_texto.get()

    if dato != "":
        lista_datos.insert(tk.END, dato)  # Agrega el dato a la lista
        entrada_texto.delete(0, tk.END)   # Limpia el campo de texto
        actualizar_contador()
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato primero")

def limpiar_lista():
    
    #Borra todos los elementos de la lista.
   
    lista_datos.delete(0, tk.END)
    actualizar_contador()


def eliminar_seleccionado():

    #Elimina el elemento seleccionado en la lista.

    seleccion = lista_datos.curselection()

    if seleccion:
        lista_datos.delete(seleccion)
        actualizar_contador()
    else:
        messagebox.showwarning("Advertencia", "Seleccione un elemento para eliminar")


def actualizar_contador():
    
    #Actualiza la etiqueta que muestra
    #cuántos elementos hay en la lista.
    
    
    total = lista_datos.size()
    contador_label.config(text=f"Total de elementos: {total}")


# Creacion de la ventana 

ventana = tk.Tk()
ventana.title("Aplicación de Registro de Datos")
ventana.geometry("420x350")
ventana.resizable(False, False)  # Evita cambiar el tamaño


#Componentes que tiene el Gráfico

#Entrada de datos
frame_superior = tk.Frame(ventana)
frame_superior.pack(pady=10)

etiqueta = tk.Label(frame_superior, text="Ingrese un dato:", font=("Arial", 12))
etiqueta.pack()

entrada_texto = tk.Entry(frame_superior, width=30)
entrada_texto.pack(pady=5)


# Frame de botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=5)

boton_agregar = tk.Button(frame_botones, text="Agregar", width=15, command=agregar_dato)
boton_agregar.grid(row=0, column=0, padx=5)

boton_eliminar = tk.Button(frame_botones, text="Eliminar seleccionado", width=18, command=eliminar_seleccionado)
boton_eliminar.grid(row=0, column=1, padx=5)

boton_limpiar = tk.Button(frame_botones, text="Limpiar lista", width=15, command=limpiar_lista)
boton_limpiar.grid(row=0, column=2, padx=5)


# Lista donde se muestran los datos
lista_datos = tk.Listbox(ventana, width=45, height=10)
lista_datos.pack(pady=10)


# Contador de elementos
contador_label = tk.Label(ventana, text="Total de elementos: 0", font=("Arial", 10))
contador_label.pack()



# Ejecución de la Aplicación 


ventana.mainloop()
