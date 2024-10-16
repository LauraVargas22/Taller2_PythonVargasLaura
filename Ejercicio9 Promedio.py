''' 
Realizar el promedio de los números positivos ingresados
Mariana Vargas
'''
def promedio():
    sumanum = 0  
    totalnum = 0  #
    
    while True:
        num = int(input('Ingrese un número positivo (o un número negativo para terminar): '))
        
        if (num < 0):
            break 
        sumanum += num 
        totalnum += 1  
    
    if (totalnum > 0):
        promedio = sumanum / totalnum  
        print(f"El promedio de los números ingresados es: {promedio}")
    else:
        print("No se ingresaron números positivos.")

if __name__ == '__main__':
    promedio()
