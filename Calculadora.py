import tkinter as tk  # Para crear la interfaz gráfica
from tkinter import messagebox  # Para mostrar mensajes emergentes como errores o alertas
import ttkbootstrap as ttk  # Para mejorar la apariencia de la interfaz con temas modernos
import math  # Para realizar cálculos matemáticos avanzados

# Explicación de las bibliotecas utilizadas:
# 1. tkinter:
#    - Proporciona herramientas para construir interfaces gráficas (ventanas, botones, etiquetas, etc.).
#    - Simplifica la creación de aplicaciones con GUI en Python sin necesidad de bibliotecas externas.
#    - Destaca por su integración nativa en Python y su facilidad de uso.
#
# 2. ttkbootstrap:
#    - Extiende tkinter con estilos modernos y personalizables.
#    - Mejora la apariencia sin necesidad de diseñar manualmente los estilos.
#    - Destaca por su compatibilidad con Bootstrap, permitiendo interfaces más atractivas.
#
# 3. math:
#    - Ofrece funciones matemáticas avanzadas como seno, coseno, raíz cuadrada, logaritmos, exponenciales, etc.
#    - Permite realizar cálculos sin necesidad de escribir fórmulas manualmente.
#    - Destaca por su eficiencia y optimización en cálculos matemáticos complejos.

# Función para manejar la entrada y calcular el resultado
def presionar_tecla(tecla):
    entrada.insert(tk.END, tecla)

def calcular():
    try:
        expresion = entrada.get()
        resultado = eval(expresion, {"__builtins__": None}, math.__dict__)  # Evalúa de manera segura
        salida.config(text=f"Resultado: {resultado}")
        entrada.delete(0, tk.END)  # Borra la operación después de mostrar el resultado
    except Exception as e:
        messagebox.showerror("Error", "Expresión inválida")

def borrar():
    entrada.delete(0, tk.END)

def borrar_ultimo():
    entrada.delete(len(entrada.get())-1, tk.END)

# Crear la ventana principal
ventana = ttk.Window(themename="darkly")  # Usa un tema más elegante
ventana.title("Calculadora Avanzada")
ventana.geometry("500x600")
ventana.resizable(False, False)

# Crear widgets
entrada = ttk.Entry(ventana, width=35, font=("Arial", 20), justify='right', bootstyle="info")
salida = ttk.Label(ventana, text="Resultado:", font=("Arial", 16), bootstyle="success")

botones = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+'),
    ('C', '⌫', 'sin', 'cos'),
    ('tan', 'sqrt', 'log', 'exp'),
    ('(', ')', '^', 'pi')
]

frame_botones = ttk.Frame(ventana)
for fila in botones:
    fila_frame = ttk.Frame(frame_botones)
    for btn_text in fila:
        estilo = "primary outline" if btn_text not in ('=', 'C', '⌫') else "danger solid"
        if btn_text == '=':
            boton = ttk.Button(fila_frame, text=btn_text, command=calcular, width=6, bootstyle="success solid")
        elif btn_text == 'C':
            boton = ttk.Button(fila_frame, text=btn_text, command=borrar, width=6, bootstyle="warning solid")
        elif btn_text == '⌫':
            boton = ttk.Button(fila_frame, text=btn_text, command=borrar_ultimo, width=6, bootstyle="danger solid")
        elif btn_text in ('sin', 'cos', 'tan', 'sqrt', 'log', 'exp'):
            boton = ttk.Button(fila_frame, text=btn_text, command=lambda op=btn_text: presionar_tecla(f"math.{op}(") , width=6, bootstyle=estilo)
        elif btn_text == 'pi':
            boton = ttk.Button(fila_frame, text=btn_text, command=lambda: presionar_tecla("math.pi"), width=6, bootstyle=estilo)
        elif btn_text == '^':
            boton = ttk.Button(fila_frame, text=btn_text, command=lambda: presionar_tecla("**"), width=6, bootstyle=estilo)
        else:
            boton = ttk.Button(fila_frame, text=btn_text, command=lambda t=btn_text: presionar_tecla(t), width=6, bootstyle=estilo)
        boton.pack(side=tk.LEFT, padx=5, pady=5)
    fila_frame.pack()

# Posicionar widgets
entrada.pack(pady=10, padx=10)
salida.pack(pady=5)
frame_botones.pack()

# Iniciar el bucle de la aplicación
ventana.mainloop()