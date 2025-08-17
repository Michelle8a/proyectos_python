import tkinter as tk

main = tk.Tk() #Crea la ventana principal

main.title("Calculadora")
main.geometry("400x300")

'''
Resulta que no puedo usar grid y place al mismo tiempo, es uno o el otro
label = tk.Label(main, text="Calculadora")
label.pack() #ponerlo despues me deja modificar la variable
'''

#Botones de numeros
boton1 = tk.Button(main, text="1")
boton1.grid(row=0, column=0)

boton2 = tk.Button(main, text="2")
boton2.grid(row=0, column=1)

boton3 = tk.Button(main, text="3")
boton3.grid(row=0, column=2)

boton4 = tk.Button(main, text="4")
boton4.grid(row=1, column=0)

boton5 = tk.Button(main, text="5")
boton5.grid(row=1, column=1)

boton6 = tk.Button(main, text="6")
boton6.grid(row=1, column=2)

boton7 = tk.Button(main, text="7")
boton7.grid(row=2, column=0)

boton8 = tk.Button(main, text="8")
boton8.grid(row=2, column=1)

boton9 = tk.Button(main, text="9")
boton9.grid(row=2, column=2)


main.mainloop() #Va al final, mantiene corriendo la ventana