import numpy as np 

def ingresarDatos():
        nombrePasajero= input("Ingrese su nombre por favor: ")

        while True: 
            rut = input("ingrese su rut SIN GUIÓN: ")
            if (len(rut) == 9 or len(rut) == 8) and rut not in storage:
                break
            elif len(rut) != 9 and len(rut) != 8:
                print("Largo de RUT inválido.")
            elif rut in storage:
                print("RUT ya ingresado.")
        
        bancoPasajero = input("Ingrese su banco: ")

        while True:
            fonoPasajero = (input("Ingrese su Numero: (8 dígitos) "))
            if len(fonoPasajero) == 8:
                break
        fonoPasajero = "+56 9 " + fonoPasajero
        storage[rut] = [nombrePasajero,bancoPasajero,fonoPasajero,num]
        print(storage)
        return nombrePasajero,rut,bancoPasajero,fonoPasajero

def encontrarIndices(matrix,num):
    target = num
    for fila, list in enumerate(matrix):     
        for col, value in enumerate(list): 
            if value == target:
                return (fila, col)

            
def printMatrix(matrix):
    i = 1
    for f in range(7):
        if f == 5 and i == 1:
            print(" ------------  ","  ------------- ")
            print(" ------------  ","  ------------- ")
            i = 2
            f == 6
        print("|", end = "  ")
        for c in range(6):
            if len(matrix[f][c]) == 1: 
                if c == 2:
                    print((matrix[f][c]), end = "      ")
                else:
                    print((matrix[f][c]), end = "   ")
            else:
                if c == 2:
                    print((matrix[f][c]), end = "     ")
                else:
                    print((matrix[f][c]), end = "  ")
        print(" |\n")

def comprarAsiento(matrix,num):
        
        if num in matrix:
            fila,col = (encontrarIndices(matrix,num))
            matrix[fila][col] = "X"
            if fila > 4:
                precio = 240000
            else:
                precio = 78900
        return precio 


def anularAsiento(matrix,og_matrix,num):

    if num not in matrix:
        fila,col = encontrarIndices(og_matrix,num)
        matrix[fila,col] = og_matrix[fila,col]
        return("Su asiento ha sido deleteado exitosamente.")

    else:
        return("Asiento no ha sido reservado.")

###############################################################################
############################################## INICIO PROGRAMA ################
###############################################################################
og_matrix = np.array((["1","2","3","4","5","6"], ## MANTENER COPIA ORIGINAL DE LA MATRIZ.
                  ["7","8","9","10","11","12"],
                  ["13","14","15","16","17","18"],
                  ["19","20","21","22","23","24"],
                  ["25","26","27","28","29","30"],
                  ["31","32","33","34","35","36"],
                  ["37","38","39","40","41","42"]))

matrix = np.array((["1","2","3","4","5","6"],
                  ["7","8","9","10","11","12"],
                  ["13","14","15","16","17","18"],
                  ["19","20","21","22","23","24"],
                  ["25","26","27","28","29","30"],
                  ["31","32","33","34","35","36"],
                  ["37","38","39","40","41","42"]))

op = "asd"
storage = {}

while op != "X":
    print("1.- Ver asiento disponibles.")
    print("2.- Comprar asiento.")
    print("3.- Anular vuelo.")
    print("4.- Modificar datos.")
    print("5.- Salir.")

    op = input("OP: ")

    if op == "1":
        printMatrix(matrix)
    else:
        if op == "2":
            num = input("Usted seleccionó la opción de comprar asiento, elija su número de asiento por favor.\n Recuerde que puede pulsar 1 para volver a ver el modelo del avión. ")
            while num not in matrix:
                num = input("Su opción de asiento puede o estar ocupada o fuera de rango, elija un número entre 1 y 42 por favor.")
            try:
                nombrePasajero,rut,bancoPasajero,fonoPasajero = ingresarDatos()
                print("----------------------------------")
                print(f"Nombre: {nombrePasajero}\nRUT: {rut}\nBanco: {bancoPasajero}\nTeléfono: {fonoPasajero}.")
                if bancoPasajero.lower() == "bancoduoc":
                    print(f"Precio asiento: ${comprarAsiento(matrix,num)*0.85}\n(descuento 15% banco DUOC.)")
                    print("----------------------------------")
                else:
                    print(f"Precio asiento: ${comprarAsiento(matrix,num)}")
                    print("----------------------------------")
            except ValueError:
                print("Rut ya ingresado.")
    
        if op == "3":
            try:
                num = input("Usted seleccionó la opción de anular vuelo. Indique el asiento que compró por favor.")
                if num in matrix:
                    print("Asiento no ha sido reservado.")
                rut_prueba = input("Ingrese su RUT. ")
                print(anularAsiento(matrix,og_matrix,num))
                if rut_prueba in storage:
                    del storage[rut]
                else:
                    print("Rut no guardado.")
            except TypeError:
                print("Datos no congruentes.") #????
        
        if op == "4":
            num = input("Usted seleccionó la opción de modificar datos, ingrese su número de asiento por favor.")
            rut_prueba = input("Ingrese su RUT. ")
            if num not in matrix and (storage[rut_prueba] == [nombrePasajero,bancoPasajero,fonoPasajero,num]): #DEJA CAMBIAR SOLO EL ÚLTIMO
                op = input("Debe elegir una opción para modificar, tenemos permitido modificar su nombre o su teléfono. Eliga 1 o 2 respectivamente.")
                while op != "1" and op != "2":
                    op = input("Opción incorrecta. Ingrese 1 o 2.")
                if op == "1":
                    nombrePasajero = input("Ingrese el nombre al cual desea cambiar.")
                    storage[rut_prueba] = [nombrePasajero,bancoPasajero,fonoPasajero,num]
                    print(storage)    
                if op == "2":
                    fonoPasajero = input("Ingrese el fono al cual desea cambiar.")
                    storage[rut_prueba] = [nombrePasajero,bancoPasajero,fonoPasajero,num]
                    print(storage)           
            else:
                print("Datos no congruentes.")

        if op == "5":
            op = input("Ingrese X si está seguro de salir, de otra manera pulse cualquier tecla para volver al inicio del menú.")
            op = op.upper()
            if op == "X":
                break

print("Ha salido exitosamente del programa.")
