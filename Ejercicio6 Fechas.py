'''
Validar una fecha ingresada teniendo en cuenta la cantidad de día y los años bisiestos.
Mariana Vargas
'''
def añobisiesto(año: int):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        pass
    return añobisiesto 

def validar_fecha(dia: int, mes: int, año: int):
    # Días máximos por cada mes
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (mes < 1) or (mes > 12):
        return False
    ## Evaluar para año bisiesto
    if (mes == 2) and (añobisiesto(año)):
        dias_por_mes[2] = 29

    if (dia < 1) or (dia > dias_por_mes[mes]):
        return False
    return True

if (__name__ == '__main__'):

    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    if (validar_fecha(dia, mes, año)):
        print(f"La fecha {dia}/{mes}/{año} es válida.")
    else:
        print(f"La fecha {dia}/{mes}/{año} no es válida.")
