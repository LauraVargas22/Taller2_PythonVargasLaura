'''
De acuerdo con el país ingresado determinar a que continente pertenece
Mariana Vargas 
'''
isActive = True
def determinar_continente (pais:str):
    match pais:
        case 'Australia':
            print ("El continente es Oceanía")
        case 'España':
            print ("El continente es Europa")
        case 'Colombia':
            print ("El continente es América")
        case 'Egipto':
            print ("El continente es África")
        case 'Rusia':
            print ("El continente es Asia")
        case '0':
            isActive = False  


if (__name__=='__main__'):

    opciones = 'Australia\n, Colombia\n, España\n, Egipto\n, Rusia\n,0.Salir'
    pais = ''
    
    print (opciones)
    pais = str (input("Seleccione el país: _"))
    pais = determinar_continente (pais)
