import matplotlib.pyplot as plt
import numpy as np

class MapaPuntos:

    def __init__(self, archivo):
        self.archivo = archivo
        self.este = []
        self.norte = []
        self.cota = []

    def leer_archivo(self):
        """Lee el archivo ASCII"""

        with open(self.archivo, "r") as f:

            for linea in f:

                datos = linea.split()

                if len(datos) >= 4:

                    # datos[0] = número del punto
                    # datos[1] = Este
                    # datos[2] = Norte
                    # datos[3] = Elevación

                    self.este.append(float(datos[1]))
                    self.norte.append(float(datos[2]))
                    self.cota.append(float(datos[3]))

    def graficar(self):
  
        plt.figure(figsize=(10,8))
        plt.scatter(
            self.este,
            self.norte,
            s=2,
            color="black"
        )
        # Vértices del rombo 2
        vertice_izq = (341100, 7457600)
        vertice_sup = (346100, 7462600)
        vertice_der = (351100, 7457600)
        vertice_inf = (346100, 7452600)
        
        # Dibujar el rombo
        x_rombo = [
            vertice_izq[0],
            vertice_sup[0],
            vertice_der[0],
            vertice_inf[0],
            vertice_izq[0]     
        ]

        y_rombo = [
            vertice_izq[1],
            vertice_sup[1],
            vertice_der[1],
            vertice_inf[1],
            vertice_izq[1]
        ]
        plt.plot(
            x_rombo,
            y_rombo,
            color="red",
            linewidth=2,
            label="Polígono 2"
        )
        plt.title("Mapa de Puntos")
        plt.xlabel("Coordenada Este")
        plt.ylabel("Coordenada Norte")
        plt.axis("equal")
        plt.xlim(333600, 363600)
        plt.ylim(7442600, 7462600)
        # Configurar la retícula cada 5000
        xticks = np.arange(333600, 363601, 5000)
        yticks = np.arange(7442600, 7462601, 5000)

        plt.xticks(xticks, rotation=45)
        plt.yticks(yticks)
        plt.grid(True)
        plt.legend()
        plt.show()