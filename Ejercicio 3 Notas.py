'''
Determinar si ha aprobado o no el exámen
Mariana Vargas
'''
def determinar_nota (nota:int):
    if (nota >= 60):
        print ("Has aprobado")
    else:
        print ("Has reprobado")

if (__name__=='__main__'):

    nota = int(input("Ingrese la calificación del exámen: "))
    nota = determinar_nota (nota)
    