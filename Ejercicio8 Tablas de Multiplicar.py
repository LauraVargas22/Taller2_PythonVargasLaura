'''
De acuerdo con el número ingresado mostrar un número del 1 al 10
'''
print ("Tabla de Multiplicar")
def tabla_numero (num:int):
    for i in range (1,11):
        resultado = num * i
        input (f"La tabla de multiplicar del numero {num} es {num} * {i} = {resultado}")

if (__name__=='__main__'):
    
    num = int (input("Ingrese un número: "))
    tabla_numero (num)
