import mysql.connector
import tkinter as tk

# Clase para interactuar con la base de datos
class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cajero"
        )
        self.cursor = self.connection.cursor()

    def crear_cuenta(self, usuario, contraseña):
        query = "INSERT INTO usuario (Usuario, Contraseña) VALUES (%s, %s)"
        values = (usuario, contraseña)
        self.cursor.execute(query, values)
        self.connection.commit()

    def iniciar_sesion(self, usuario, contraseña):
        query = "SELECT * FROM usuario WHERE Usuario = %s AND Contraseña = %s"
        values = (usuario, contraseña)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        return result is not None

# Función para manejar el evento de crear cuenta
def crear_cuenta():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    db = Database()
    db.crear_cuenta(usuario, contraseña)
    print("Cuenta creada con éxito.")

# Función para manejar el evento de iniciar sesión
def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    db = Database()
    if db.iniciar_sesion(usuario, contraseña):
        print("Inicio de sesión exitoso.")
    else:
        print("Error: Nombre de usuario o contraseña incorrectos.")

# Crear una instancia de la ventana principal
ventana = tk.Tk()

# Configurar las dimensiones de la ventana
ventana.geometry("400x200")

# Añadir un título a la ventana
ventana.title("Cajero")

# Etiqueta y campo de entrada para el nombre de usuario
label_usuario = tk.Label(ventana, text="Nombre de usuario:")
label_usuario.pack()
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

# Etiqueta y campo de entrada para la contraseña
label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack()
entry_contraseña = tk.Entry(ventana, show="*")  # Para ocultar la contraseña
entry_contraseña.pack()

# Botón para crear una cuenta
boton_crear_cuenta = tk.Button(ventana, text="Crear cuenta", command=crear_cuenta)
boton_crear_cuenta.pack()

# Botón para iniciar sesión
boton_iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
boton_iniciar_sesion.pack()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
