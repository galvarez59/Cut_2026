import pandas as pd
import numpy as np
from scipy.ndimage import uniform_filter

def cargar_datos(archivo):
    # 'on_bad_lines="warn"' permite que el programa continúe aunque encuentre filas irregulares
    # 'sep=None' detecta automáticamente si usas espacios o comas
    df = pd.read_csv(archivo, sep=None, engine='python', skiprows=1, on_bad_lines='skip')
    
    # Tomamos solo las columnas numéricas
    datos = df.select_dtypes(include=[np.number]).values
    return datos

def aplicar_filtro_cuadrado(datos, tamano_ventana=3):
    # uniform_filter suaviza los datos usando una ventana cuadrada
    filtro = uniform_filter(datos, size=tamano_ventana, mode='constant')
    return filtro

if __name__ == "__main__":
    archivo = "mejillones_ascii.txt"
    try:
        data = cargar_datos(archivo)
        resultado = aplicar_filtro_cuadrado(data, tamano_ventana=3)
        np.savetxt("resultado_filtrado.txt", resultado)
        print("¡ÉXITO! Filtro aplicado. Resultado guardado en 'resultado_filtrado.txt'.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")