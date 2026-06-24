import tkinter as tk
from tkinter import ttk, messagebox

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
# ===   SUBRUTINA AYLEEN                         ===
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
# ===   SUBRUTINA RAFAEL                         ===
# ==================================================
def ventana_Rafael():
    root.withdraw()

    win = tk.Toplevel(root)
    win.title("Ventana Rafael")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Rafael",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Rafael debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==================================================
        # ===   ESPACIO PARA CÓDIGO DE RAFAEL             ===
        # ==================================================
        # Aquí RAFAEL debe colocar su rutina.

        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Rafael")

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

b5 = ttk.Button(root, text="Rafael", command=ventana_Rafael)
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