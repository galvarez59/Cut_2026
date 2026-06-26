import matplotlib.pyplot as plt


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

        plt.title("Mapa de Puntos")
        plt.xlabel("Coordenada Este")
        plt.ylabel("Coordenada Norte")
        plt.axis("equal")
        plt.grid(True)

        plt.show()