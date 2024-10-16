'''
Solicitar información personal de un empleado e imprimir la antigüedad
con la empresa.
Mariana Vargas
'''
from datetime import datetime
def antigüedad (añoIngreso:int):
    añoactual = datetime.now().year
    antigüedad = añoactual - añoIngreso
    return antigüedad

def datospersonales ():
    print ("INGRESE SUS DATOS PERSONALES")
    nombre = input ("Su nombre es: ")
    apellido = input ("Su apellido es:")
    edad = int(input ("Su edad es: "))
    añoIngreso = int (input ("Su año de ingreso a la empresa fue: "))
    telefono = input ("Su teléfono es: ")

    añoEmpresa = antigüedad (añoIngreso)

    print (f"Sr@ Usuario {nombre} {apellido} \n Su edad es {edad} años \n Su número telefónico {telefono}\nTiene una antiguedad en la empresa de {añoEmpresa} ")


if (__name__=='__main__'):
    datospersonales ()
