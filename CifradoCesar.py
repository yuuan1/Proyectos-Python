from tkinter import *
import sys
import os

ventana = Tk()
ventana.title ("Cifrado Cesar")
ventana.geometry("400x500")
ventana.config(bg = "#0D1B2A")
ventana.resizable(0, 0)

entry_elemento = None
i = 2
boton_elemento = None
mensaje_cifrado = ""
pepe = 2
mensajemsg = ""
modo = ""
###################################
titulo_label = Label(
    ventana, 
    text="CIFRADO CESAR",
    bg="#0d1B2A",
    fg="#722F37",
    font=("Arial", 20, "bold"),
    padx=20,
    pady=20
)
titulo_label.pack(side="top")
##################################

##################################
def reiniciar_programa():
    ventana.destroy()
    os.execv(sys.executable, ['python'] + sys.argv)
##################################

##################################
def mensaje():
    global entry_elemento, boton_elemento
    entry_elemento = Entry(
        ventana,
        font=("Arial", 15, "bold"),
        bg="#1D3557",
        bd=0,
        insertbackground="#E0E1DD",
        relief="flat",
        justify="center"
    )
    pepe = 4
    entry_elemento.pack(padx=70, pady=90, fill="x")

    boton_elemento = Button(
    ventana,
    text="Actualizar",
    bg="#722F37",
    fg="#E0E1DD",
    activebackground="#E0E1DD",
    activeforeground="#722F37",
    bd=0,
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=10,
    command = clave
    )
    boton_elemento.pack()
###
def clave():
    global msg
    msg =entry_elemento.get()
    menu_label_01.configure(text="Escribe tu la clave que desees\n para encriptar a continuación")
    entry_elemento.delete(0, END)
    if i == 2:
        boton_elemento.config(text="Procesar", command=suma)
    else:
        boton_elemento.config(text="Procesar", command=resta)
#################################

#################################
def suma():
    global mensaje_cifrado, msg

    clave_entry = entry_elemento.get()

    if clave_entry.isdigit():
        clave = int(clave_entry)
    else:
        menu_label_01.pack_forget(),
        entry_elemento.pack_forget(),
        boton_elemento.pack_forget(),
        error = Label(
            ventana,
            text="[ERROR][SEGURO DE VIDA]\nAL NO INTRODUCIR UN NUMERO SE HA" 
            "DEFINIDO\nAUTOMATICAMENTE CON LA CLAVE 5",
            bg="#0D1B2A",
            fg="#722F37",
            font=("Arial", 10, "bold")
        )
        error.pack(pady=20)
        clave = 5
        mensaje_cifrado = ""
        for letra in msg:
            msgASCII = (ord(letra) + clave) % 256  
            mensaje_cifrado += chr(msgASCII)
            
        def transicion_error():
            error.pack_forget()
            resultado()
            
        ventana.after(2500, transicion_error)

    mensaje_cifrado = ""
    
    for letra in msg:
        msgASCII = (ord(letra) + clave) % 256  
        mensaje_cifrado += chr(msgASCII)

    entry_elemento.pack_forget()
    boton_elemento.pack_forget()
    resultado()
###
def resta():
    global mensaje_cifrado, msg

    clave_entry = entry_elemento.get()

    if clave_entry.isdigit():
        clave = int(clave_entry)
    else:
        menu_label_01.pack_forget(),
        entry_elemento.pack_forget(),
        boton_elemento.pack_forget()
        error = Label(
            ventana,
            text="[ERROR][SEGURO DE VIDA]\nAL NO INTRODUCIR UN NUMERO SE HA" 
            "DEFINIDO\nAUTOMATICAMENTE CON LA CLAVE 5",
            bg="#0D1B2A",
            fg="#722F37",
            font=("Arial", 10, "bold")
        )
        error.pack(pady=20)
        clave = 5
        for letra in msg:
            msgASCII = (ord(letra) - clave) % 256  
            mensaje_cifrado += chr(msgASCII)
        def transicion_error():
            error.pack_forget()
            resultado()
            
        ventana.after(2500, transicion_error)

    mensaje_cifrado = ""
    for letra in msg:
        msgASCII = (ord(letra) - clave) % 256  
        mensaje_cifrado += chr(msgASCII)

    entry_elemento.pack_forget()
    boton_elemento.pack_forget()
    resultado()
#################################
def resultado():
    resultado_label = Label(
            ventana,
            text=f"Resultado:\n{mensaje_cifrado}",
            bg="#1D3557",
            fg="#E0E1DD",
            font=("Arial", 14, "bold"),
            padx=20,
            pady=20
        )
    resultado_label.pack()     ###NO OLVIDAAR
##################################

##################################
def encriptar():
    menu_label_01.config(
        text="Escribe el mensaje que desees\nencriptar a continuación",
        bg="#1D3557",
        relief="flat",
        state="disabled",
        cursor="arrow",
        command=""
    )
    menu_label_02.pack_forget(),
    menu_label_03.pack_forget(),
    mensaje()
###
def desencriptar():
    global i
    menu_label_02.config(
        text="Escribe tu mensaje que desees\ndesencriptar a continuación",
        bg="#1D3557",
        relief="flat",
        state="disabled",
        cursor="arrow",
        command=""
    )
    mensaje()
    menu_label_01.pack_forget(),
    menu_label_03.pack_forget(),
    i = 4
###
def salir():
    menu_label_03.config(
        text="NOOOOO\nNo me avandones :(",
        bg="#1D3557",
        relief="flat",
        state="disabled",
        cursor="arrow",
        command=""
    )
    menu_label_01.pack_forget(),
    menu_label_02.pack_forget(),
    ventana.after(1000, ventana.destroy)
###
##################################

##################################
menu_label_01 = Button(
    ventana,
    text="Encripta",
    fg="#E0E1DD",
    bg="#415A77",
    font=("Arial", 13, "bold"),
    anchor = "center",
    height= 5,
    width=10,
    command=encriptar

)
menu_label_01.pack(pady=(0,20))
###
menu_label_02 = Button(
    ventana,
    text="Desencriptar",
    fg="#E0E1DD",
    bg="#415A77",
    font=("Arial", 13, "bold"),
    anchor = "center",
    height= 5,
    width=10,
    command=desencriptar
)
menu_label_02.pack(pady=(0,20))
###
menu_label_03 = Button(
    ventana,
    text="Salir",
    fg="#E0E1DD",
    bg="#415A77",
    font=("Arial", 13, "bold"),
    anchor = "center",
    height= 5,
    width=10,
    command=salir
)
menu_label_03.pack(pady=(0,40))
###
reset_label = Button(
    ventana,
    text="Reset",
    fg="#0D1B2A",
    bg="#E0E1DD",
    activebackground="#722F37",
    activeforeground="#E0E1DD",
    font=("Arial", 13, "bold"),
    relief="flat",
    cursor="hand2",
    anchor="e", 
    padx=12,
    pady=8,
    command=reiniciar_programa
)
reset_label.place(relx=1.0, rely=1.0, anchor="se", x=-15, y=-15)


ventana.mainloop()