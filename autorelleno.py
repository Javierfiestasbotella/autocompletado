from pynput.keyboard import Key, Controller
import pyperclip as pc

#completa_conexion(n):TE AUTOCOMPLETA UNA CLASE CON LA CONEXXION A UNA BBDD PASANDO COMO ARGUMENTO NOMBRE DE LA CLASE
#completa_interfaz(n):AUTOCOMPLETA LOS MÉTODOS DE INTERFAZ DE LA VARIABLE PRIVADA QUE PASAS COMO ARGUMENTO

def autorelleno1(clave):
    return f'''
    @property
    def {clave}(self):
        return self._{clave}
    @{clave}.setter
    def {clave}(self,valor):
        self._{clave}=valor
    @{clave}.deleter
    def {clave}(self):
        del self._{clave}'''



def autorelleno2(clave):
    return f'''
    #SE REQUIERE IMPORTAR:
    #import mysql.connector
    #from mysql.connector import Error
    class {clave}():

        def __init__(self):
            try:
                self.conexion = mysql.connector.connect(
                    host=,
                    user=,
                    password=,
                    db=
                )
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))'''

def autorelleno3(n,m):
    return f'''
def usuario():
        usser=input("Introduce un usuario : ")
        if len(usser)<{n} or len(usser)>{m}:
            print("El usuario debe tener entre {n} y {m} caracteres")
            usuario()
        elif usser.isalnum()==False:
            print("Los valores del usurio deben ser únicamente letras o números")
            usuario()
        else:
            print(True)
        '''



def completa_conexion(n):#TE AUTOCOMPLETA UNA CLASE CON LA CONEXXION A UNA BBDD PASANDO COMO ARGUMENTO NOMBRE DE LA CLASE
    prueba01=pc.copy(autorelleno2(n))
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')
    

def completa_interfaz(n):#AUTOCOMPLETA LOS MÉTODOS DE INTERFAZ DE LA VARIABLE PRIVADA QUE PASAS COMO ARGUMENTO
    prueba01=pc.copy(autorelleno1(n))
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')

def verifica_ususario(n,m):#AUTOCOMPLETA VERIFICACION DE USUARIO; SOLO PUEDEN SER NÚMEROS O LETRAS Y PASARLE POR ARGUMENTO EL MÍNIMO Y MÁXIMO DE CARACTERES QUE QUIERES QUE TENGA.
    prueba01=pc.copy(autorelleno3(n,m))
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')