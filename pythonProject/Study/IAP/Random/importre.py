import os
import datetime as dt
import re

patente_registrada = 'a'
valid = False
conta = 0


def valid_patente(paten):
    cont = 0
    if re.match(r"^([A-Z]{2}\d{4})", paten) or re.match(r"^([A-Z]{4}\d{2})", paten):
        if len(paten) == 6:
            print('Patente valida')
            cont = 1
        else:
            print('Patente invalida')
            cont = 0
    else:
        print('Patente invalida')
        cont = 0
    return cont


def valid_aniofab(aniofab, valid):
    if 1900 <= aniofab <= 2021:
        print('Año de fabricación validado correctamente')
        valid = True
        return valid
    else:
        print('Año ingresado incorrectamente\nHa de encontrarse en un rango de años desde 1900 a 2021')


def valid_vehiculo(tipo_vehiculo, valid):
    if tipo_vehiculo == 'b' or tipo_vehiculo == 'd' or tipo_vehiculo == 'e' or tipo_vehiculo == 'h':
        print('Tipo valido de vehiculo')
        valid = True
        return valid
    else:
        print('Tipo invalido de producto')


def valid_vacio(string, valid):
    if string is None or string[0] == ' ':
        print('Valor ingresado vacío, ingrese algo')
    else:
        valid += 1


print('Bienvenido a Serviexpress! Seleccione que desea hacer')
while True:
    opc = int(input('''
        1. Registrar automóvil
        2. Registro mantenimiento
        3. Consultar automóvil
        4. Salir
        
        -->\t'''))
    if opc == 4:
        print('Muchas gracias por preferirnos!')
    elif opc == 1:
        # Patente
        while conta == 0:
            patente = input('Ingrese la patente de su auto (formato AA1000 o AAAA10)\n-->\t')
            conta = valid_patente(patente)
            if conta == 1:
                print("PATENTE REGISTRADA")
                break
            else:
                print("PATENTE INVALIDA")

        # Marca 
        while True:
            marca = input('Ingrese la marca de su auto --> ')
            valid_vacio(marca)
            if valid:
                valid = 0
                break
        # Modelo
        while True:
            modelo = input('Ingrese el modelo de su auto --> ')
            valid_vacio(marca)
            if valid:
                valid = 0
                break
        # Año fabricación (entre 1900 y 2021)
        while True:
            try:
                aniofab = int(input('Ingrese el año de fabricación de su auto --> '))
                valid_aniofab(aniofab)
                if valid:
                    valid = 0
                    break
            except:
                print('Tipo de valor ingresado inválido, intentelo nuevamente')
        # Tipo vehículo (solo b, d, e, h)
        while True:
            tipo_vehiculo = input('b: bencina\nd: diesel\ne: eléctrico\nh: hibrido\n-->\t').lower()
            valid_vehiculo(tipo_vehiculo)
            if valid:
                valid = 0
                break
    elif opc == 2:
        # Registros
        patente = input('Por favor ingrese la patente registrada de su auto --> ')
        if patente == patente_registrada:
            print('todo fine')
        else:
            print('nada fine')
