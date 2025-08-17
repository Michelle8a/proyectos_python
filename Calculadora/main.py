import tkinter as tk

main = tk.Tk() #Crea la ventana principal

main.title("Calculadora")
main.geometry("400x300")

'''
Resulta que no puedo usar grid y place al mismo tiempo, es uno o el otro
label = tk.Label(main, text="Calculadora")
label.pack() #ponerlo despues me deja modificar la variable
'''




main.mainloop() #Va al final, mantiene corriendo la ventana