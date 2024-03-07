# database/database.py
import mysql.connector

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
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return True
        except mysql.connector.Error as error:
            print(f"Error al crear la cuenta: {error}")
            return False

    def iniciar_sesion(self, usuario, contraseña):
        query = "SELECT Saldo FROM usuario WHERE Usuario = %s AND Contraseña = %s"
        values = (usuario, contraseña)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        return result[0] if result else None  # Retorna el saldo si la sesión es exitosa

    def depositar_dinero(self, usuario, cantidad):
        query = "UPDATE usuario SET Saldo = Saldo + %s WHERE Usuario = %s"
        values = (cantidad, usuario)
        self.cursor.execute(query, values)
        self.connection.commit()

    def retirar_dinero(self, usuario, cantidad):
        query = "UPDATE usuario SET Saldo = Saldo - %s WHERE Usuario = %s"
        values = (cantidad, usuario)
        self.cursor.execute(query, values)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
