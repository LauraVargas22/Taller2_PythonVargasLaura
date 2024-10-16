'''
Determinar si la persona es mayor de edad
Mariana Vargas
'''
print ("MAYOR O MENOR DE EDAD")

def determinar_edad (edad:int):
    if (edad >=18):
        print ("Eres mayor de edad")
    else:
        print ("Eres menor de edad")


if (__name__=='__main__'):

    edad = int (input("Ingrese su edad: "))
    edad = determinar_edad (edad)
