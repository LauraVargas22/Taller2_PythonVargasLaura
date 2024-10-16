'''
Determinar si la contraseña es válida o no
Mariana Vargas
'''

def ValidarContraseña (contraseña:str):
    ## Se corrobora que tenga los caracteres establecidos
    if (len(contraseña) < 8):
        return False
    ##Valida que al menos tenga un número
    contiene_numero = any(char.isdigit() for char in contraseña)
    if (not contiene_numero):
        return False
        
    return True

if (__name__=='__main__'):

    contraseña = input("Ingrese su contraseña: ")

    if (ValidarContraseña(contraseña)):
        print ("La contraseña es VÁLIDA")
    else:
        print ("La contraseña NO es válida")