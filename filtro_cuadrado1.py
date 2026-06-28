import numpy as np
from scipy.ndimage import uniform_filter

def cargar_datos(archivo):
    # Asumimos que tu archivo tiene formato: X Y Z
    # Si tiene encabezados, agrega skip_header=1
    datos = np.loadtxt(archivo)
    return datos

def aplicar_filtro_cuadrado(datos, tamano_ventana=3):
    # 'datos' debe ser una matriz 2D (grid).
    # Si tus datos son puntos sueltos (X, Y, Z),
    # primero deberías transformarlos a un grid.
    
    # Aquí aplicamos el filtro de media (filtro cuadrado)
    filtro = uniform_filter(datos, size=tamano_ventana, mode='constant')
    return filtro

if __name__ == "__main__":
    archivo = "mejillones_ascii.txt"
    try:
        data = cargar_datos(archivo)
        
        # Aquí estamos asumiendo que tu archivo es una matriz rectangular 
        # (si es una lista de puntos, necesitarías un paso previo de interpolación)
        resultado = aplicar_filtro_cuadrado(data, tamano_ventana=3)
        
        # Guardar resultado
        np.savetxt("resultado_filtrado.txt", resultado)
        print("¡Filtro aplicado con éxito! Resultado guardado en 'resultado_filtrado.txt'.")
        
    except Exception as e:
        print(f"Ocurrió un error: {e}")