import cv2
import numpy as np
from sentinelhub import SHConfig, DataCollection, BBox, CRS, WmsRequest
import matplotlib.pyplot as plt
from config import sentinelhub

class Capture:
    def __init__(self, lon_min, lat_min, lon_max, lat_max, saveinto):
        self.lon_min = lon_min
        self.lat_min = lat_min
        self.lon_max = lon_max
        self.lat_max = lat_max
        self.saveinto = saveinto

    def plot_image(self, image, factor=1):
        """
        Utility function for plotting RGB images.
        """
        plt.subplots(nrows=1, ncols=1, figsize=(15, 7))

        if np.issubdtype(image.dtype, np.floating):
            plt.imshow(np.minimum(image * factor, 1))
            plt.savefig(self.saveinto)
        else:
            plt.imshow(image)
            plt.savefig(self.saveinto)

    def capture(self):
        # Configura la conexión con la API de Sentinel Hub
        config = SHConfig()
        config.sh_client_id = sentinelhub.sentinelhub_client_id
        config.sh_client_secret = sentinelhub.sentinelhub_client_secret
        config.instance_id = sentinelhub.sentinelhub_instance_id

        # Define las coordenadas de interés
        coordenadas = BBox(bbox=(self.lon_min, self.lat_min, self.lon_max, self.lat_max), crs=CRS.WGS84)

        # Crea una consulta para obtener las imágenes de satélite
        consulta = WmsRequest(
            data_collection=DataCollection.SENTINEL2_L1C,
            layer='TRUE-COLOR-S2L2A',
            bbox=coordenadas,
            time="latest",
            width=2500,
            height=2500,
            maxcc=0.3,
            config=config,
        )

        # Obtén los datos de la imagen
        datos_imagen = consulta.get_data()

        self.plot_image(datos_imagen[-1])

class Analysis:
    def __init__(self, img_path):
        self.img_path = img_path
        self.img = cv2.imread(self.img_path)

        # ESTABLECER PARAMETROS DEPENDIENDO DE LA PRESA
        self.max_area = 100
        self.index_water = 50

    def get_water_volume(self):

        # Convertir imagen escala de grises
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # Crear un índice de agua que identifique las áreas de agua en la imagen
        self.water_index = cv2.threshold(gray, self.index_water, 255, cv2.THRESH_BINARY)[1]

        # Calcular el área de agua en la imagen
        water_area = np.sum(self.water_index == 255)

        # Calcular el volumen de agua en la presa
        self.water_volume = water_area * (water_area / self.max_area)

    def show_results(self):
        fig, axs = plt.subplots(1, 2, figsize=(10, 5))
        axs[0].imshow(cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB))
        axs[0].set_title('Imagen satelital')
        axs[1].imshow(self.water_index, cmap='gray')
        axs[1].set_title('Índice de agua')
        plt.suptitle(f'Volumen de agua en la presa: {self.water_volume} m^3')
        plt.show()