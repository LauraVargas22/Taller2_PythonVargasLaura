'''
Establecer el valor de la energía eléctrica.
Mariana Vargas
'''

def valorEnergiaElectrica (kw:float, kwconsumidos:float):
    valorEnergiaElectrica = kw * kwconsumidos
    return valorEnergiaElectrica

if (__name__=='__main__'):
    print ("VALOR DE LA ENERGÍA ELÉCTRICA")

    mes = str(input("Ingrese el mes de consumo a evaluar: "))
    estrato = int (input("Ingrese el estrato correspondiente a la factura: "))
    kw = float(input("Ingrese el valor del kilovatio (kw): "))
    kwconsumidos = float(input("Ingrese los kilovatios consumidos en el mes: "))

    preciofactura = valorEnergiaElectrica (kw,kwconsumidos)

    print (f"La factura del mes de {mes} de estrato {estrato} tiene un valor de {preciofactura}")
