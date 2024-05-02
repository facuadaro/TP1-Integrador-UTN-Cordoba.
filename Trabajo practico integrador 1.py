cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

#PROVINCIA Y PAIS

if len(cp) == 9:
    destino = 'Brasil'
    if cp[0] == '0':
        provincia = 'Region 0'
    elif cp[0] == '1':
        provincia = 'Region 1'
    elif cp[0] == '2':
        provincia = 'Region 2'
    elif cp[0] == '3':
        provincia = 'Region 3'
    elif cp[0] == '4':
        provincia = 'Region 4'
    elif cp[0] == '5':
        provincia = 'Region 5'
    elif cp[0] == '6':
        provincia = 'Region 6'
    elif cp[0] == '7':
        provincia = 'Region 7'
    elif cp[0] == '8':
        provincia = 'Region 8'
    elif cp[0] == '9':
        provincia = 'Region 9'
    else:
        provincia = 'No definido'
elif len(cp) == 8:
    destino = 'Argentina'
    if cp[0] == "A":
        provincia = "Salta"
    elif cp[0] == "B":
        provincia = "Provincia de Buenos Aires"
    elif cp[0] == "C":
        provincia = "Ciudad Autónoma de Buenos Aires"
    elif cp[0] == "D":
        provincia = "San Luis"
    elif cp[0] == "E":
        provincia = "Entre Ríos"
    elif cp[0] == "F":
        provincia = "La Rioja"
    elif cp[0] == "H":
        provincia = "Santiago del Estero"
    elif cp[0] == "I":
        provincia = "Chaco"
    elif cp[0] == "J":
        provincia = "San Juan"
    elif cp[0] == "K":
        provincia = "Catamarca"
    elif cp[0] == "L":
        provincia = "La Pampa"
    elif cp[0] == "M":
        provincia = "Mendoza"
    elif cp[0] == "N":
        provincia = "Misiones"
    elif cp[0] == "P":
        provincia = "Formosa"
    elif cp[0] == "Q":
        provincia = "Neuquén"
    elif cp[0] == "R":
        provincia = "Río Negro"
    elif cp[0] == "S":
        provincia = "Santa Fe"
    elif cp[0] == "T":
        provincia = "Tucumán"
    elif cp[0] == "U":
        provincia = "Chubut"
    elif cp[0] == "V":
        provincia = "Tierra del Fuego"
    elif cp[0] == "W":
        provincia = "Corrientes"
    elif cp[0] == "X":
        provincia = "Córdoba"
    elif cp[0] == "Y":
        provincia = "Jujuy"
    elif cp[0] == "Z":
        provincia = "Santa Cruz"
    else:
        provincia = "No aplica"
elif len(cp) == 7:
    destino = 'Chile'
    provincia = 'No definido'
elif len(cp) == 6:
    destino = 'Paraguay'
    provincia = 'No definido'
elif len(cp) == 5:
    destino = 'Uruguay'
    if cp[0] == '1':
        provincia = 'Montevideo'
    else:
        provincia = 'no Montevideo'
elif len(cp) == 4:
    destino = 'Bolivia'
    provincia = 'No definido'
else:
    destino = 'Otros paises'
    provincia = 'No definido'

#PROCESO IMPORTE INICIAL

if tipo == 0:
    inicial = 1100
elif tipo == 1:
    inicial = 1800
elif tipo == 2:
    inicial = 2450
elif tipo == 3:
    inicial = 8300
elif tipo == 4:
    inicial = 10900
elif tipo == 5:
    inicial = 14300
elif tipo == 6:
    inicial = 17900
else:
    inicial = 'No definido'

#DESCUENTO SI EL PAGO ES EN EFECTIVO

if pago == 1:
    inicial = round(inicial - (inicial * 0.10))

#IMPORTE FINAL

if destino == 'Argentina':
    final = round(inicial)
elif destino == "Bolivia" or destino == "Paraguay" or destino == "Uruguay" and provincia == "Montevideo":
    final = round((inicial * 0.2) + inicial)
elif destino == "Uruguay" and provincia == "no Montevideo" or destino == "Chile":
    final = round((inicial * 0.25) + inicial)
elif destino == "Brasil" and provincia == "Region 8" or provincia == "Region 9":
    final = round((inicial * 0.2) + inicial)
elif destino == "Brasil" and provincia == "Region 0" or provincia == "Region 1" or provincia == "Region 2" or provincia == "Region 3":
    final = round((inicial * 0.25) + inicial)
elif destino == "Brasil" and provincia == "Region 4" or provincia == "Region 5" or provincia == "Region 6" or provincia == "Region 7":
    final = round((inicial * 0.3) + inicial)
else:
    final = round((inicial * 0.5) + inicial)

#RESULTADO

print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)
