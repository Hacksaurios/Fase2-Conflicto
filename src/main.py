#!/usr/bin/env python3

from satelitalAnalysis import Analysis, Capture
from meteorologico import estadoTiempo

if __name__ == '__main__':

    while True:
        option = input("Introduce una opción (1 para medir el tiempo meteorológico, 2 para ver la foto de un embalse, 0 para salir): ")
        if option == "1":
            lon = input("Introduce la longitud: ")
            lat = input("Introduce la latitud: ")
            estadoTiempo(lon, lat).get_info()
        elif option == "2":
            route = '../images/imagen_satelital.jpg'
            Capture(-74.0, 4.5, -74.1, 4.6, route).capture()
            analysis = Analysis(route)
            analysis.get_water_volume()
            analysis.show_results()
        elif option == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, introduce 1, 2 o 0.")