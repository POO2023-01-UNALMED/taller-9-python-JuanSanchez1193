from tkinter import Tk, Button, Entry

def click_boton(numero):

    numero_actual = pantalla.get()

    nuevo_numero = numero_actual + str(numero)

    pantalla.delete(0, "end")
    pantalla.insert(0, nuevo_numero)

def click_igual():

    expresion = pantalla.get()
    try:
        
        resultado = eval(expresion)
        
        pantalla.delete(0, "end")
        pantalla.insert(0, str(resultado))
    except:
       
        pantalla.delete(0, "end")
        pantalla.insert(0, "Error")

def click_punto():
    
    numero_actual = pantalla.get()
    
    if "." not in numero_actual:
        
        nuevo_numero = numero_actual + "."
        
        pantalla.delete(0, "end")
        pantalla.insert(0, nuevo_numero)


root = Tk()
root.title('Calculadora POO')
root.resizable(0, 0)

pantalla = Entry(root, width=22, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones

boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(1)).grid(row=1, column=0, padx=1, pady=1)

boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(2)).grid(row=1, column=1, padx=1, pady=1)


boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(3)).grid(row=1, column=2, padx=1, pady=1)


boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(4)).grid(row=2, column=0, padx=1, pady=1)


boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(5)).grid(row=2, column=1, padx=1, pady=1)


boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(6)).grid(row=2, column=2, padx=1, pady=1)


boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(7)).grid(row=3, column=0, padx=1, pady=1)


boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(8)).grid(row=3, column=1, padx=1, pady=1)


boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: click_boton(9)).grid(row=3, column=2, padx=1, pady=1)




boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=click_punto).grid(row=4, column=2, padx=1, pady=1)


boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2", command=click_igual).grid(row=4, column=0, columnspan=2, padx=1, pady=1)


boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: click_boton("+")).grid(row=1, column=3, padx=1, pady=1)


boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: click_boton("-")).grid(row=2, column=3, padx=1, pady=1)


boton_multiplicacion = Button(root, text="*", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: click_boton("*")).grid(row=3, column=3, padx=1, pady=1)


boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: click_boton("/")).grid(row=4, column=3, padx=0, pady=1)



root.mainloop()
