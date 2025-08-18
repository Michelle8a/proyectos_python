import tkinter as tk


def boton_numeros(main, texto, linea, columna,):
    
    boton = tk.Button(main, 
                      text = texto,
                      width = 10, 
                      height = 5,
                      justify= 'center',
                      font = ("Arial", 10))
    
    boton.grid(row=linea, column=columna, padx=5, pady=5) #esto solo recibe posicion
    return boton