'''
Determinar si se puede formar un triángulo según su longitud
Mariana Vargas 
'''
a = 0.0
b = 0.0
c = 0.0

def desigualdad_triangular (a:float, b:float, c:float):
    if (a+b > c) and (a+c > b) and (b+c > a):
        print ("Si es un triángulo válido")
    else:
        print ("No es un triángulo válido")

if (__name__=='__main__'):

    a = float(input("Ingrese uno de los lados del triángulo: "))
    b = float(input("Ingrese otro de los lados del triángulo: "))
    c = float(input("Ingrese otro de los lados del triángulo: "))
    desigualdad_triangular (a,b,c)


