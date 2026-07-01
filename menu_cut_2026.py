import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# ==================================================
# ===   FUNCIÓN GENERAL PARA VOLVER AL MENÚ       ===
# ==================================================
def volver_al_menu(win):
    """
    Cierra la ventana secundaria y vuelve a mostrar
    el menú principal.
    """
    win.destroy()
    root.deiconify()
    root.lift()
    root.focus_force()


# ==================================================
# ===   SUBRUTINA MAIN                           ===
# ==================================================
def ventana_main():
    root.withdraw()

    win = tk.Toplevel(root)
    win.title("Ventana main")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: main",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí main debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==================================================
        # ===   ESPACIO PARA CÓDIGO DE MAIN               ===
        # ==================================================
        # Aquí MAIN debe colocar su rutina.
        # Ejemplo:
        # - ingreso de datos
        # - cálculo matemático
        # - presentación de resultados
        # - llamada a funciones propias

        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de main")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=lambda: volver_al_menu(win)
    )
    boton_volver.pack(pady=10)

    win.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(win))


# ==================================================
# ===   SUBRUTINA AYLEEN    gaaa                     ===
# ==================================================
def ventana_ayleen():
    root.withdraw()

    win = tk.Toplevel(root)
    win.title("Ventana ayleen")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: ayleen_cut",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí ayleen debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==================================================
        # ===   ESPACIO PARA CÓDIGO DE AYLEEN             ===
        # ==================================================
        # Aquí AYLEEN debe colocar su rutina.

        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de ayleen")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=lambda: volver_al_menu(win)
    )
    boton_volver.pack(pady=10)

    win.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(win))


# ==================================================
# ===   SUBRUTINA HARLEY                         ===
# ==================================================
def ventana_Harley():
    root.withdraw()

    win = tk.Toplevel(root)
    win.title("Ventana Harley")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Harley",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Harley debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==================================================
        # ===   ESPACIO PARA CÓDIGO DE HARLEY             ===
        # ==================================================
        # Aquí HARLEY debe colocar su rutina.

        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Harley")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=lambda: volver_al_menu(win)
    )
    boton_volver.pack(pady=10)

    win.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(win))


# ==================================================
# ===   SUBRUTINA IGNACIO                        ===
# ==================================================
def ventana_Ignacio():
    root.withdraw()

    win = tk.Toplevel(root)
    win.title("Ventana Ignacio")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Ignacio",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Ignacio debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==================================================
        # ===   ESPACIO PARA CÓDIGO DE IGNACIO            ===
        # ==================================================
        # Aquí IGNACIO debe colocar su rutina.

        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Ignacio")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=lambda: volver_al_menu(win)
    )
    boton_volver.pack(pady=10)

    win.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(win))

# ==================================================
# ===   SUBRUTINA RAFAEL (CUADRO 4)              ===
# ==================================================
def ventana_Rafael():
    root.withdraw()

    win = tk.Toplevel(root)
    win.title("Ventana Rafael (Cuadro 4)")
    win.geometry("450x350")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Rafael (Cuadro 4)",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=20)

    # Texto con formato especificado en letras rojas
    etiqueta_formato = tk.Label(
        win,
        text="Formato requerido del archivo txt:\nNombre, Este, Norte, Cota",
        font=("Segoe UI", 12, "bold"),
        fg="red",
        bg="#ecf0f1"
    )
    etiqueta_formato.pack(pady=10)

    def mostrar_resultados(puntos):
        # Ventana secundaria para mostrar resultados
        res_win = tk.Toplevel(win)
        res_win.title("Resultados - Área 4")
        res_win.geometry("450x400")
        res_win.configure(bg="#ecf0f1")

        def descargar():
            # Botón para guardar el nuevo .txt
            ruta_guardado = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")],
                title="Guardar puntos filtrados"
            )
            if ruta_guardado:
                try:
                    with open(ruta_guardado, 'w', encoding='utf-8') as f:
                        for p in puntos:
                            f.write(p + "\n")
                    messagebox.showinfo("Éxito", "Archivo guardado correctamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{e}")

        # Botón de descarga al principio
        btn_descargar = ttk.Button(res_win, text="Descargar Archivo .txt", command=descargar)
        btn_descargar.pack(pady=15)

        # Cuadro de texto para mostrar los puntos
        text_area = tk.Text(res_win, wrap="none", height=15, width=50)
        text_area.pack(padx=15, pady=5, fill="both", expand=True)

        # Insertamos los puntos en el cuadro
        for p in puntos:
            text_area.insert(tk.END, p + "\n")
        
        text_area.config(state=tk.DISABLED) # Lo hacemos de solo lectura

    def procesar_archivo():
        ruta_archivo = filedialog.askopenfilename(
            title="Seleccionar archivo de puntos",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        
        if not ruta_archivo:
            return # El usuario canceló la selección

        puntos_filtrados = []
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as file:
                for linea in file:
                    linea_limpia = linea.strip()
                    if not linea_limpia:
                        continue
                    
                    # Separamos asumiendo espacios o tabulaciones. 
                    # Reemplazamos comas por espacios por si acaso viene separado por comas.
                    partes = linea_limpia.replace(',', ' ').split()
                    
                    if len(partes) >= 4:
                        try:
                            # Nombre = partes[0], Este = partes[1], Norte = partes[2], Cota = partes[3]
                            este = float(partes[1])
                            norte = float(partes[2])
                            
                            # Criterio del Cuadro 4
                            if norte >= 7460100 and este >= 361600:
                                puntos_filtrados.append(linea_limpia)
                        except ValueError:
                            # Si no se puede convertir a float, asumimos que es el encabezado y lo agregamos igual
                            if "Norte" in linea_limpia or "Este" in linea_limpia:
                                puntos_filtrados.insert(0, linea_limpia)
            
            if len(puntos_filtrados) > 0:
                mostrar_resultados(puntos_filtrados)
            else:
                messagebox.showinfo("Resultado", "No se encontraron puntos dentro del Área 4.")
                
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al procesar el archivo:\n{e}")

    # Botón para subir el archivo
    boton_subir = ttk.Button(win, text="Subir Archivo", command=procesar_archivo)
    boton_subir.pack(pady=15)

    boton_volver = ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=lambda: volver_al_menu(win)
    )
    boton_volver.pack(pady=10)

    win.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(win))

# ==================================================
# ===   SUBRUTINA WILSON                         ===
# ==================================================
def ventana_Wilson():
    root.withdraw()

    win = tk.Toplevel(root)
    win.title("Ventana Wilson")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Wilson",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Wilson debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==================================================
        # ===   ESPACIO PARA CÓDIGO DE WILSON             ===
        # ==================================================
        # Aquí WILSON debe colocar su rutina.

        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Wilson")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=lambda: volver_al_menu(win)
    )
    boton_volver.pack(pady=10)

    win.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(win))


# ==================================================
# ===   SUBRUTINA ANDRES                         ===
# ==================================================
def ventana_Andres():
    root.withdraw()

    win = tk.Toplevel(root)
    win.title("Ventana Andres")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Andres",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Andres debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==================================================
        # ===   ESPACIO PARA CÓDIGO DE ANDRES             ===
        # ==================================================
        # Aquí ANDRES debe colocar su rutina.

        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Andres")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=lambda: volver_al_menu(win)
    )
    boton_volver.pack(pady=10)

    win.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(win))


# ==================================================
# ===   SUBRUTINA PANTOJA                        ===
# ==================================================
def ventana_pantoja():
    root.withdraw()

    win = tk.Toplevel(root)
    win.title("Ventana pantoja")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: pantoja",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí pantoja debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==================================================
        # ===   ESPACIO PARA CÓDIGO DE PANTOJA            ===
        # ==================================================
        # Aquí PANTOJA debe colocar su rutina.

        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de pantoja")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=lambda: volver_al_menu(win)
    )
    boton_volver.pack(pady=10)

    win.protocol("WM_DELETE_WINDOW", lambda: volver_al_menu(win))


# ==================================
# ===   VENTANA PRINCIPAL MENÚ    ===
# ==================================
root = tk.Tk()
root.title("Proyecto Polígonos")
root.geometry("500x650")
root.configure(bg="#ecf0f1")

banner = ttk.Label(
    root,
    text="Filtrado de Nube de Puntos",
    anchor="center",
    font=("Segoe UI", 20, "bold"),
    background="#0984e3",
    foreground="white"
)
banner.pack(fill="x", pady=(0, 20))

instruccion = ttk.Label(
    root,
    text="Seleccione una opción del menú",
    font=("Segoe UI", 12),
    background="#ecf0f1"
)
instruccion.pack(pady=(10, 30))


# ==================================
# ===   BOTONES DEL MENÚ          ===
# ==================================
b1 = ttk.Button(root, text="main", command=ventana_main)
b1.pack(pady=10, ipadx=20, ipady=5)

b2 = ttk.Button(root, text="ayleen", command=ventana_ayleen)
b2.pack(pady=10, ipadx=20, ipady=5)

b3 = ttk.Button(root, text="Harley", command=ventana_Harley)
b3.pack(pady=10, ipadx=20, ipady=5)

b4 = ttk.Button(root, text="Ignacio", command=ventana_Ignacio)
b4.pack(pady=10, ipadx=20, ipady=5)

b5 = ttk.Button(root, text="Rafael (Cuadro 4)", command=ventana_Rafael)
b5.pack(pady=10, ipadx=20, ipady=5)

b6 = ttk.Button(root, text="Wilson", command=ventana_Wilson)
b6.pack(pady=10, ipadx=20, ipady=5)

b7 = ttk.Button(root, text="Andres", command=ventana_Andres)
b7.pack(pady=10, ipadx=20, ipady=5)

b8 = ttk.Button(root, text="pantoja", command=ventana_pantoja)
b8.pack(pady=10, ipadx=20, ipady=5)


# ==================================
# ===   EJECUCIÓN DEL PROGRAMA    ===
# ==================================
root.mainloop()