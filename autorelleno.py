from pynput.keyboard import Key, Controller
import pyperclip as pc
import os
import io
from io import open
from datetime import datetime
from datetime import date
import datetime


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

def autorelleno3(n,m):#verifica nobre de usuario
    return f'''
#Devuelve True si el nombre usuario es aceptado y verificado
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
def autorelleno4(n):
    return f'''
def contraseña():
  global passw
  passw=input("Introduce contraseña: ")
  if len(passw)<={n-1}:
    print("La contraseña debe tener al menos {n} caractéres")
    contraseña()
  elif passw.isalnum()==True:
    print ("La contraseña debe tener al menos un carácter no alfanumérico")
    contraseña()
  elif passw.lower() == passw:
    print("Debe haber por lo menos una mayúscula")
    contraseña()
  elif passw.upper()==passw:
    print("Debe haber por lo menos una minúscula")
    contraseña()

  for i in passw:
    if i==" ":
      print("La contraseña no debe tener espacios en blanco")
      contraseña()
  print(True)
    
    
    '''
def autorelleno5():
    return f'''
    #NO OLVIDES DARLE UNA EXTENSION AL NOMBRE DEL ARCHIVO DEL PRIMER ARGUMENTO
    #SUSTITUYE EN LA LLAMADA A LA FUNCION escribir(); EL ARCHIVO POR EL NOMBRE DEL ARCHIVO Y DOCUMENTACIÓN POR LO QUE QUIERAS DENTRO DEL ARCHIVO.
    def escribir(archivo,documentacion):
        fichero = open(archivo, 'a')
        fichero.write(documentacion)
        fichero.close()
    escribir(archivo,documentacion)
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

def verifica_password(n):#AUTOCOMPLETA FUNCION DE VERIFICACION DE PASSWORD PASANDO COMO ARGUMENTO CANTIDAD MAX DE CARACTERES
    prueba01=pc.copy(autorelleno4(n))
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')

def guarda_en_archivo():#CREA EL ARCHIVO CON EL NOMBRE DEL PRIMER ARGUMENTO Y GUARDA LA INFORMACION QUE GUARDAS EN EL SEGUNDO ARGUMENTO QUE DEBES INTRODUCIR LUEGO.
    prueba01=pc.copy(autorelleno5())
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):
        keyboard.press('v')
        keyboard.release('v')



