import tkinter as tk
import botones 

main = tk.Tk() #Crea la ventana principal

main.title("Calculadora")
main.geometry("300x500")
main.resizable(False, False)

'''
Resulta que no puedo usar grid y place al mismo tiempo, es uno o el otro
label = tk.Label(main, text="Calculadora")
label.pack() #ponerlo despues me deja modificar la variable
'''

entrada = tk.Entry(main)


#Botones de numeros
b1 = botones.boton_numeros(main, "1", 0, 0)
b2 = botones.boton_numeros(main, "2", 0, 1)
b3 = botones.boton_numeros(main, "3", 0, 2)
b4 = botones.boton_numeros(main, "4", 1, 0)
b5 = botones.boton_numeros(main, "5", 1, 1)
b6 = botones.boton_numeros(main, "6", 1, 2)
b7 = botones.boton_numeros(main, "7", 2, 0)
b8 = botones.boton_numeros(main, "8", 2, 1)
b9 = botones.boton_numeros(main, "9", 2, 2)


main.mainloop() #Va al final, mantiene corriendo la ventana