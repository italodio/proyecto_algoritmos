# SECCIÓN 12V
import numpy as np
import random as rd

def grabar():

    nombre = input("Ingrese su nombre por favor. ")
    tipo = input("Ingrese tipo de vehículo: ")

    while True:
        marca = input("Ingrese marca de su vehículo. Recuerde que debe consistir entre 2 y 15 caracteres.")
        if 1 < len(marca) < 16:
            break 

    while True:        
        try:
            print("Ingrese fecha registro de vehículo utilizando el formato: (DD/MM/AÑO)")
            dia = int(input("Ingrese día. "))
            mes = int(input("Ingrese mes."))
            año = int(input("Ingrese año:"))
            if 0 < dia < 32 and 0 < mes < 13 and 1980 < año < 2024:
                break 
        except ValueError:
            print("Fecha ingresada incorrecta. Utilize números por favor.")

    n_multas = int(input("Ingrese el número de multas registradas a esta patente por favor: "))
    for i in range(n_multas):
        monto = int(input("Ingrese monto de multa"))
        multas_monto.append(monto)
        fecha = input("Ingrese fecha de multa.")
        multas_fecha.append(fecha)
    
    while True:  
        patente = input("Ingrese patente, recuerde que debe seguir el formato de 4 letras y 2 dígitos. ")
        if len(patente) == 6 and patente not in storage:
            break
        else:
            print("La patente ingresada no sigue el formato o bien ya está ingresada. ")

    while True: 
        precio = int(input("Ingrese precio, recuerde que debe ser sobre 5 millones.: "))     
        if precio > 5000000:
            break 
    
    storage[patente] = {'nombre':nombre,'tipo':tipo,'marca':marca,'fecha':(dia,mes,año),'precio':precio,'multas(m)': multas_monto,'multas(f)': multas_fecha}
    print(storage)
    return nombre, tipo, patente, precio, marca

def buscar(patente):
    if patente in storage:
        return(storage[patente])
    else:
        return("Patente no registrada.")

def certificados(patente):
    op = "asd"
    while op != "X":
        op = input("Ingrese 1 para certificado de emisión de contaminantes.\nIngrese 2 para certificado de anotaciones vigentes.\nIngrese 3 para certificado de multas.")
        precio = rd.randrange(1500,3500)
        if op == "1":
            return(f"-------------------------------\nCERTIFICADO DE EMISIÓN DE CONTAMINANTES.\nPatente del vehículo y datos del dueño: {storage[patente]}\nPrecio: ${precio}\n-------------------------------")
        else:
            if op == "2":
                return(f"-------------------------------\nCERTIFICADO DE ANOTACIONES VIGENTES.\nPatente del vehículo y datos del dueño: {storage[patente]}\nPrecio: ${precio}\n-------------------------------")
            if op == "3":
                return(f"-------------------------------CERTIFICADO DE MULTAS.\nPatente del vehículo y datos del dueño: {storage[patente]}\nPrecio: ${precio}\n-------------------------------")
            if op != "1" and op != "2" and op != "3":
                return("Selección de certificado fuera de rango.")
op = "asd"
storage = {} 
multas_monto = []
multas_fecha = []


while op != "X":

    op = input("1.- Grabar.\n2.- Buscar.\n3.-Imprimir certificados.\n4.-Salir.")
    if op == "1":
        print("Usted seleccionó la opción de guardar datos.")
        grabar()
    
    else:
        if op == "2":
            patente = input("Usted ha seleccionado la opción de buscar por patente. Ingrese su patente a buscar por favor. ")
            print(buscar(patente))

        if op == "3":
            patente = input("Usted ha seleccionado la opción de impresión de certificado. Ingrese su patente por favor. ")
            if patente in storage:
                print(certificados(patente))
            else:
                print("Patente no registrada.")
        
        if op == "4":
            op = input("Ingrese X si está seguro de salir, de otra forma ingrese cualquier número.")
            op = op.upper()
        
        if op != "1" and op != "2" and op != "3" and op != "4":
            print("Opción incorrecta, se le devolverá al inicio.")

print("Ha salido de el programa.\nAutor: Italo Inocencio.\nVersión de software: 1.0.0")