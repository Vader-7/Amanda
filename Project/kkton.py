import serial
import cx_Oracle
import config as cfg
from datetime import datetime
import geocoder as geo

g = geo.ip("me")
g = g.latlng
h = datetime.now()
print(f"Ubicación:\t{g}\nHora:\t\t{h}")

# arduino = serial.Serial("/dev/cu.usbmodem1101", 9000)


"""def insert_sos(p_cod, p_ubicacion, p_rut, p_fecha):
   
       Insert a row to the SOS table
       :param p_cod:
       :param p_ubicacion:
       :param p_rut:
       :param p_fecha:
       :return:
    
    # construct an insert statement that add a new row to the billing_headers table
    sql = ('insert into SOS(p_cod, p_ubicacion, p_rut, p_fecha) '
           'values(:cod,:ubicacion,:rut,:fecha)')"""


"""while True:
    switch = arduino.readline().decode("ascii")
    if switch == "1":
        insert_sos()
    else:
        pass"""
