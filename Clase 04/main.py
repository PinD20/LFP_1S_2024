'''
from tkinter import filedialog, Tk

#Abrir un archivo con el explorador de archivos
Tk().withdraw()
path = filedialog.askopenfilename(
    title = "Selecciona un archivo",
    initialdir="C:/",
    filetypes=(
        ("Archivos de texto", "*.est"),
        ("Todos los archivos", "*.*")
    )
)

archivo = open(path, "r", encoding="utf-8")
lines = archivo.readlines()

#Ejemplo de split para la práctica
for line in lines:
    if line[-1] == "\n":
        line = line[:-1]
    partes = line.split(":")
    partes[1] = partes[1][1:-1]
    print(partes)

'''

def imprimirTexto():
    txt = textArea.get("1.0", "end-1c")
    print(txt)

#Ejemplo de interfaz gráfica con Tkinter
from tkinter import Tk, Label, Button, Text

#Crear ventana
ventana = Tk()

label1 = Label(ventana, text="Hola Mundo")
#Colocar label centrado horizontalmente en la ventana
#label1.pack()

#Colocar label en una posición específica
label1.place(x=50, y=100)


boton1 = Button(ventana, text="Click aquí", command=imprimirTexto)
boton1.place(x=200, y=100)


textArea = Text(ventana, width=20, height=10)
textArea.place(x=300, y=150)


ventana.title("Clase 4 LFP")

ventana.resizable(False, False)

anchoVentana = 600
altoVentana = 400

#Centrar ventana
x_ventana = ventana.winfo_screenwidth() // 2 - anchoVentana // 2
y_ventana = ventana.winfo_screenheight() // 2 - altoVentana // 2

posicion = str(anchoVentana) + "x" + str(altoVentana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)



#Mantener ventana abierta
ventana.mainloop()