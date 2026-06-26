import os

def filtrar_poligono_6(archivo_entrada, archivo_salida):
    print(f"Iniciando segmentación de la nube de puntos desde: {archivo_entrada}")

    try:
        # Primer avance: Solo intentamos abrir y leer el archivo original
        with open(archivo_entrada, 'r') as f_in:
            for linea in f_in:
                pass # Aquí procesaremos los datos más adelante
                    
        print("Lectura de archivo finalizada.")

    except FileNotFoundError:
        print(f"Error crítico: No se encontró el archivo de origen {archivo_entrada}.")

archivo_origen = 'batimetria_mejillones.asc'
archivo_destino = 'segmentacion_poligono_6.txt'

filtrar_poligono_6(archivo_origen, archivo_destino)