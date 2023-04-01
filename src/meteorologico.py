import requests
from config import weatherbit

class estadoTiempo:
    def __init__(self, lon, lat):
        self.lon = lon
        self.lat = lat
    
    def get_info(self):
        # Introduce el nombre de la ciudad y el país para el que deseas obtener el tiempo

        # Construye la URL de la API de Weatherbit
        url = f"https://api.weatherbit.io/v2.0/current?lat={self.lat}&lon={self.lon}&key={weatherbit.weatherbit_apikey}"

        # Realiza una solicitud GET a la API de Weatherbit
        respuesta = requests.get(url)

        # Parsea la respuesta JSON
        datos = respuesta.json()

        # Imprime los datos del tiempo
        print(f"Descripción: {datos['data'][0]['weather']['description']}")
        print(f"Temperatura: {datos['data'][0]['temp']}°C")
        print(f"Sensación térmica: {datos['data'][0]['app_temp']}°C")
        print(f"Humedad: {datos['data'][0]['rh']}%")