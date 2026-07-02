import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
def calcular():
        # ==================================================
          # Ruta de tu archivo
        archivo = r"C:\Users\aylle\OneDrive\Documentos\github 3\Cut_2026\mejillones_ascii.txt"
        x_lim = [334100, 336600] 
        y_lim = [7455100, 7457600] 
            
        try:
                df = pd.read_csv(archivo, sep=r'\s+', engine='python', header=None, 
                                names=['Letra', 'X', 'Y', 'Z'], on_bad_lines='skip')
                
                mask = (df['X'] >= x_lim[0]) & (df['X'] <= x_lim[1]) & \
                    (df['Y'] >= y_lim[0]) & (df['Y'] <= y_lim[1])
                
                resultado = df[mask]
                datos_puntos = resultado[['X', 'Y', 'Z']]
                
                # --- CAMBIOS PARA ARCGIS ---
                # 1. Cambiamos la extensión a .csv
                # 2. sep=',' usa comas para separar los valores
                # 3. header=True guarda los títulos 'X', 'Y', 'Z' en la primera fila
                datos_puntos.to_csv("resultado_cuadrado_1.csv", index=False, header=True, sep=',')
                
                # Convertimos a texto para mostrarlo en tu ventana
                texto_puntos = datos_puntos.to_string(index=False)
                
                mensaje_final = f"¡Cálculo terminado con éxito!\n\nSe han extraído {len(resultado)} puntos.\nArchivo guardado: 'resultado_cuadrado_1.csv'\n\nPuntos encontrados:\n\n{texto_puntos}"
                
                messagebox.showinfo("Resultado del Cálculo", mensaje_final)
                
        except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al procesar el archivo: {e}")