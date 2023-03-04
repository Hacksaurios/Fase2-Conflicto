#!/usr/bin/env python3

from satelitalAnalysis import Analysis, Capture

if __name__ == '__main__':

    route = '../images/imagen_satelital.jpg'
    Capture(-74.0, 4.5, -74.1, 4.6, route).capture()

    analysis = Analysis(route)
    analysis.get_water_volume()
    analysis.show_results()