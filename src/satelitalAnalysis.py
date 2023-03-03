import cv2
import numpy as np
import matplotlib.pyplot as plt

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