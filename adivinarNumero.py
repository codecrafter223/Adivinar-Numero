from tkinter import *
import random

root = Tk()
root.geometry("350x350")
frame = Frame()
frame.pack()
pista = StringVar()
intentos = 0

# Generar un número aleatorio solo una vez al inicio
numero_aleatorio = random.randint(1, 100)

def adivinar():
    global pista, intentos
    numero_ingresado = int(numero_entry.get())
    intentos += 1  # Contar el número de intentos

    if numero_ingresado == numero_aleatorio:
        pista.set(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
    elif numero_ingresado > numero_aleatorio:
        pista.set("El número aleatorio es más pequeño.")
    elif numero_ingresado < numero_aleatorio:
        pista.set("El número aleatorio es más grande.")

# Entry para ingresar el número
numero_entry = Entry(frame)
numero_entry.grid(row=2, column=1)

# Entry para mostrar la pista
mostrarPista_entry = Entry(frame, textvariable=pista, state='readonly',width=35)
mostrarPista_entry.grid(row=2, column=2)

# Labels
numero_label = Label(frame, text="Escribe el número:")
numero_label.grid(row=1, column=1)

mostrarPista_label = Label(frame, text="Mostrar pista:")
mostrarPista_label.grid(row=1, column=2)

# Botón
adivinar_button = Button(frame, text="Adivinar", command=adivinar)
adivinar_button.grid(row=3, column=1, columnspan=2)

root.mainloop()
