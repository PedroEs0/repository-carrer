from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os

#ventana principal

def users_ventana():
    global users_ventana
    pestas_color="coral"
    users_ventana=Tk()
    users_ventana.geometry("600x400")#DIMENSIONES DE LA VENTANA
    users_ventana.title("SUPERMERCADO SMK")#TITULO DE LA VENTANA
    users_ventana.configure(bg='ivory3')

    Label(text="Escoja su opción", bg="green3", width="300", height="2", font=("Calibri", 13, "bold")).pack()#ETIQUETA CON TEXTO
    Label(text="", bg='ivory3').pack()
    Button(text="Empleado", height="2", width="20", bg=pestas_color,font=("Calibri", 15,'bold'), command=empleado).pack() #BOTÓN "empleado"
    Label(text="", bg='ivory3').pack()
    Button(text="Cliente", height="2", width="20", bg=pestas_color,font=("Calibri", 15,'bold'), command=cliente).pack() #BOTÓN "cliente".
    Label(text="", bg='ivory3').pack()
    users_ventana.mainloop()

def cliente():
    users_ventana.withdraw()
    global ventana_cliente
    ventana_cliente = Toplevel(users_ventana)
    ventana_cliente.title("CLIENTE")
    ventana_cliente.geometry(("600x400"))
    ventana_cliente.configure(bg='ivory3')

    global id_usuario
    id_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "id_usuario"
    
    Label(ventana_cliente, text="Introduzca datos", bg="green3").pack()
    Label(ventana_cliente, text="", bg= 'ivory3').pack()
    etiqueta_id = Label(ventana_cliente, text="IDENTIFICACION DEL USUARIO * ", bg='green3')
    etiqueta_id.pack()
    entrada_id = Entry(ventana_cliente, textvariable=id_usuario) #ESPACIO PARA INTRODUCIR la id.
    entrada_id.pack()
    Label(ventana_cliente, text="", bg= 'ivory3').pack()
    Button(ventana_cliente, text="Acceder", width=10, height=1, bg='coral', command=carro1).pack()
    Label(ventana_cliente, text="", bg= 'ivory3').pack()
    Button(ventana_cliente, text="Regresar", width=10, height=1, bg='coral', command=regreso_clnt).pack()
    ventana_cliente.mainloop()

def regreso_clnt():
    global regreso_clnt
    ventana_cliente.withdraw()
    users_ventana.deiconify()

def empleado():
    users_ventana.withdraw()
    def ventana_inicio():
        global ventana_principal
        ventana_principal = Toplevel(users_ventana)
        pestas_color="coral"
        ventana_principal.geometry("600x400")#DIMENSIONES DE LA VENTANA
        ventana_principal.title("EMPLEADOS")#TITULO DE LA VENTANA
        ventana_principal.configure(bg='ivory3')
        Label(ventana_principal, text="Escoja su opción", bg="green3", width="300", height="2", font=("Calibri", 13, 'bold')).pack()#ETIQUETA CON TEXTO
        Label(ventana_principal, text="", bg='ivory3').pack()
        Button(ventana_principal, text="Acceder", height="2", width="30", bg=pestas_color, command=login,).pack() #BOTÓN "Acceder"
        Label(ventana_principal, text="", bg='ivory3').pack()
        Button(ventana_principal, text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack() #BOTÓN "Registrarse".
        Label(ventana_principal, text="", bg='ivory3').pack()
        Button(ventana_principal, text="Regresar", height="2", width="30", bg=pestas_color, command=regreso_emp).pack() #BOTÓN "regresar".

        ventana_principal.mainloop()

    def regreso_emp():
        ventana_principal.withdraw()
        users_ventana.deiconify()

    #CREAMOS VENTANA PARA REGISTRO.
    def registro():
        ventana_principal.withdraw()
        global ventana_registro
        ventana_registro = Toplevel(ventana_principal)
        ventana_registro.title("Registro")
        ventana_registro.geometry("600x400")
        ventana_registro.configure(bg='ivory3')

        global nombre_usuario
        global clave
        global entrada_nombre
        global entrada_clave
        nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
        clave = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "clave"

        Label(ventana_registro, text="Introduzca datos", bg="green3").pack()
        Label(ventana_registro, text="", bg='ivory3').pack()
        etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ", bg='green3')
        etiqueta_nombre.pack()
        entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
        entrada_nombre.pack()
        etiqueta_clave = Label(ventana_registro, text="Contraseña * ", bg='green3')
        etiqueta_clave.pack()
        entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
        entrada_clave.pack()
        Label(ventana_registro, text="",bg='ivory3').pack()
        Button(ventana_registro, text="Registrarse", width=10, height=1, bg="coral", command = registro_usuario).pack() #BOTÓN "Registrarse"
        Label(ventana_registro, text="",bg='ivory3').pack()
        Button(ventana_registro, text="Regresar", width=10, height=1, bg="coral", command = regreso_rgt).pack() #BOTÓN "Regresar"

    def regreso_rgt():
        global regreso_rgt
        ventana_registro.withdraw()
        ventana_principal.deiconify()
#CREAMOS VENTANA PARA LOGIN.

    def login():
        ventana_principal.withdraw()
        global ventana_login
        ventana_login = Toplevel(ventana_principal)
        ventana_login.title("Acceso a la cuenta")
        ventana_login.geometry("300x250")
        ventana_login.configure(bg='ivory3')
        Label(ventana_login, text="Introduzca nombre de usuario y contraseña", bg='green3').pack()
        Label(ventana_login, text="", bg='ivory3').pack()

        global verifica_usuario
        global verifica_clave

        verifica_usuario = StringVar()
        verifica_clave = StringVar()

        global entrada_login_usuario
        global entrada_login_clave

        Label(ventana_login, text="Nombre usuario * ",bg='green3').pack()
        entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
        entrada_login_usuario.pack()
        Label(ventana_login, text="", bg='ivory3').pack()
        Label(ventana_login, text="Contraseña * ", bg='green3').pack()
        entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
        entrada_login_clave.pack()
        Label(ventana_login, text="",bg='ivory3').pack()
        Button(ventana_login, text="Acceder", width=10, height=1,bg='coral', command = verifica_login).pack()
        tk.Label(ventana_login, text="", bg='ivory3').pack()
        Button(ventana_login, text="Regresar", width=10, height=1,bg='coral', command = regreso_log).pack()

    def regreso_log():
        ventana_login.withdraw()
        ventana_principal.deiconify()

#VENTANA login

    def verifica_login():
        usuario1 = verifica_usuario.get()
        clave1 = verifica_clave.get()
        entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
        entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.

        lista_archivos = os.listdir() #generacion de lista de archivos
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS
        if usuario1 in lista_archivos:
            archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
            verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
            if clave1 in verifica:
                carro2()
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
            else:
                no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
        else:
            no_usuario() #..EJECUTA "no_usuario()".

#VENTANA DE "Contraseña incorrecta".

    def no_clave():
        global ventana_no_clave
        ventana_no_clave = Toplevel(ventana_login)
        ventana_no_clave.title("ERROR")
        ventana_no_clave.geometry("150x100")
        ventana_login.configure(bg='ivory3')
        Label(ventana_no_clave, text="Contraseña incorrecta ", bg='ivory3',font=("Calibri", 13, "bold")).pack()
        Button(ventana_no_clave, text="OK", bg='coral',font=("Calibri", 13, "bold"), command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".

#VENTANA DE "Usuario no encontrado".

    def no_usuario():
        global ventana_no_usuario
        ventana_no_usuario = Toplevel(ventana_login)
        ventana_no_usuario.title("ERROR")
        ventana_no_usuario.geometry("200x150")
        ventana_no_usuario.configure(bg='ivory3')
        Label(ventana_no_usuario, text="Usuario no encontrado", bg='ivory3',font=("Calibri", 12, "bold")).pack()
        Button(ventana_no_usuario, text="OK", bg='coral', command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS    

    def borrar_no_clave():
        ventana_no_clave.destroy()

    def borrar_no_usuario():
        ventana_no_usuario.destroy()

#REGISTRO USUARIO

    def registro_usuario():

        usuario_info = nombre_usuario.get()
        clave_info = clave.get()

        file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
        file.write(usuario_info + "\n")
        file.write(clave_info)
        file.close()

        entrada_nombre.delete(0, END)
        entrada_clave.delete(0, END)

        Label(ventana_registro, text="Registro completado con éxito", fg="snow", font=("calibri", 11, 'bold'), bg='ivory3').pack()

    ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.

#VENTANA carrito
def carro1():
    ventana_cliente.withdraw()
    carrito()
def carro2():
    ventana_login.withdraw()
    carrito()

def carrito():
    class InterfazCompra:
        def __init__(self, master):
            self.master = master
            self.master.title("SUPERMERCADO SMK")
            self.master.configure(bg='ivory3')

            self.productos = {
                "Leche 1L": 5.000,
                "Pan x unidad": 1.000,
                "Huevos x carton": 15.000,
                "Manzanas x unidad": 1.500,
                "Pasta en conchitas Doria 250 g.": 1.150,
                "Spaguetti Doria 250 g.": 1.090,
                "Cereal desayuno Zucaritas 420 g.": 8.790,
                "Fríjol rojo 1K": 5.750,
                "Duraznos en almíbar 822 g. neto": 6.290,
                "Mantequilla con sal Alpina 250 g.": 2.690,
                "Margarina Rama 500 g.": 5.840,
                "Chocolate Sol 1 lb.": 3.250,
                "Café instantáneo Colcafe 170 g.": 7.560,
                "Azúcar blanca Manuelita 1 K.": 2.160,
                "Aceite Girasoli 1L": 6.950,
                "Sal Refisal 1K": 1.000,
                "Huevos bandeja 30 unidades": 8.190,
                "Leche Alquería larga vida 900 ml x 6": 12.090,
                "Arroz FlorHuila 1lb": 2.390,
                "Lentejas 1K": 3.450,
            }

            self.carrito = {}

            self.label_producto = tk.Label(master, text="Selecciona un producto:", bg= 'ivory3')
            self.label_producto.pack()

            self.producto_var = tk.StringVar()
            self.producto_var.set(list(self.productos.keys())[0])

            self.producto_menu = tk.OptionMenu(master, self.producto_var, *self.productos.keys())
            self.producto_menu.pack()

            self.label_cantidad = tk.Label(master, text="Cantidad:", bg='ivory3')
            self.label_cantidad.pack()

            self.cantidad_entry = tk.Entry(master)
            self.cantidad_entry.pack()

            self.agregar_button = tk.Button(master, text="Agregar al carrito", bg='coral', command=self.agregar_al_carrito)
            self.agregar_button.pack()

            self.carrito_label = tk.Label(master, text="Carrito de compras:", bg='green3')
            self.carrito_label.pack()

            self.carrito_text = tk.Text(master, height=10, width=40,bg='ivory3')
            self.carrito_text.pack()

            self.total_label = tk.Label(master, text="Total: $0.000", bg='ivory3')
            self.total_label.pack()

            self.realizar_compra_button = tk.Button(master, text="Realizar compra",bg='coral', command=self.realizar_compra)
            self.realizar_compra_button.pack()

        def agregar_al_carrito(self):
            producto = self.producto_var.get()
            cantidad = self.cantidad_entry.get()

            try:
                cantidad = int(cantidad)
                if cantidad > 0:
                    if producto in self.carrito:
                        self.carrito[producto] += cantidad
                    else:
                        self.carrito[producto] = cantidad

                    self.actualizar_carrito()
                    self.actualizar_total()
                else:
                    messagebox.showwarning("Error", "La cantidad debe ser un número positivo.")
            except ValueError:
                messagebox.showwarning("Error", "Por favor, ingresa una cantidad válida.")

        def actualizar_carrito(self):
            self.carrito_text.delete(1.0, tk.END)
            for producto, cantidad in self.carrito.items():
                self.carrito_text.insert(tk.END, f"{producto}: {cantidad}\n")

        def actualizar_total(self):
            total = sum(self.productos[producto] * cantidad for producto, cantidad in self.carrito.items())
            self.total_label.config(text=f"Total: ${total:.3f}")

        def realizar_compra(self):
            mensaje = "Compra realizada\n\nProductos:\n"
            for producto, cantidad in self.carrito.items():
                mensaje += f"{producto}: {cantidad}\n"

            total = sum(self.productos[producto] * cantidad for producto, cantidad in self.carrito.items())
            mensaje += f"\nTotal: ${total:.3f}"

            messagebox.showinfo("Compra realizada", mensaje)
            self.master.destroy()
            users_ventana.deiconify()

    if __name__ == "__main__":
        root = tk.Tk()
        app = InterfazCompra(root)
        root.mainloop()

users_ventana()
