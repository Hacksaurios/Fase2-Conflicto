#!/usr/bin/env python3

from satelitalAnalysis import Analysis, Capture
from meteorologico import estadoTiempo
# import sqlite3

if __name__ == '__main__':

    lon = "-78.6382"
    lat = "35.7796"

    estadoTiempo(lon, lat).get_info()

    # conn = sqlite3.connect('../db/database.db')
    # c = conn.cursor()
    # c.execute('CREATE TABLE IF NOT EXISTS presas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, ubicacion TEXT, potencia INTEGER, latitud REAL, longitud REAL, max REAL, min REAL, indice_agua REAL, indice_area TEXT)')
    
    # route = '../images/imagen_satelital.jpg'
    # Capture(-74.0, 4.5, -74.1, 4.6, route).capture()

    # analysis = Analysis(route)
    # analysis.get_water_volume()
    # analysis.show_results()