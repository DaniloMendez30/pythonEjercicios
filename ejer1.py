import random as rd
def calculo(total_factura, DESC):
    numero_descuento = rd.randint(1,5)
    color = [var["color"] for var in DESC if var["id"] == numero_descuento]
    color = color[0]
    descuento_final = [var["descuento"] for var in DESC if var["id"] == numero_descuento]
    descuento_final = int(descuento_final[0])

    calculo_decuento = total_factura - ( total_factura * (descuento_final/100))

    print("sacaste el color "+ str(color) + " y tu descuento es del " + str(descuento_final) + "%" + " su nuevo total a pagar es " + str(calculo_decuento))


def run():

    DESC = [
    {
        'id': 1,
        'color': 'Blanco',
        'descuento': 0,
    },
    {
        'id': 2,
        'color': 'Roja',
        'descuento': 10,
    },
    {
        'id': 3,
        'color': 'Azul',
        'descuento': 20,
    },
    {
        'id': 4,
        'color': 'Verde',
        'descuento': 25,
    },
    {
        'id': 5,
        'color': 'Amarilla',
        'descuento': 50,
    },
              ]

    total_factura = int(input("Introdusca la cantidad total de la compra: "))

    if total_factura < 100000:
        print("El valor de tu factura no aplica para un decuento")
    else: 
        print(calculo(total_factura, DESC))

        
    





if __name__ == "__main__":
  run()
  
