'''
import re
import os
cls.system("cls")

def valid_patente(patente):
    if re.match(r"^([A-Z]{2}\d{4})", patente) or re.match(r"^([A-Z]{4}\d{2})", patente):
        print('Patente valida')
    else:
        print('Patente invalida')
        invalid = True
        
patente = input('Ingresa algo --> ')
valid_patente(patente)
'''

while True:
    try:
        input('something --> ')
    except:
        print('a')