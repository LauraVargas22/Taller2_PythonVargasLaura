'''
Solicitar número positivo e imprimir sus antecesores
Mariana Vargas
'''

def numero_positivo (num:int):
    while (num > 1):
        print (f"Los numeros anteriores al número {num} son {num-1}")
        num -= 1
    return num

if (__name__=='__main__'):

    num = int (input("Ingrese un número: "))
    if (num > 0):
        num = numero_positivo (num)
    else:
        print ("ERROR")

                                             