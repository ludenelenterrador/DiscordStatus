import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Función para minimizar la ventana  en lugarr de cerrarla

# Crear una ventana
ventana = tk.Tk()
ventana.title("Título Inicial")
ventana.geometry("600x100")  # Establecer las dimensiones de la ventana (ancho x alto)
ventana.resizable(width=False, height=False)  # Deshabilitar el redimensionamiento

# Descargar la imagen de fondo desde la URL
fondo_url = "https://img.freepik.com/vector-premium/nube-acuarela-azul-cielo-primavera-fondso-cian_439591-456.jpg"
response = requests.get(fondo_url)
imagen_fondo = Image.open(BytesIO(response.content))
imagen_fondo = imagen_fondo.resize((1920, 1080))  # Ajustar el tamaño de la imagen al tamaño de la ventana
fondo = ImageTk.PhotoImage(imagen_fondo)

# Crear un widget de etiqueta para mostrar el fondo
fondo_label = tk.Label(ventana, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Colocar la imagen de fondo en toda la ventana

# Establecer el icono de la aplicación
icono_url = "https://luden.x10.mx/assets/imgs/favicon.ico"
response = requests.get(icono_url)
icono_data = BytesIO(response.content)
icono_pil = Image.open(icono_data)
icono = ImageTk.PhotoImage(icono_pil)
ventana.iconphoto(True, icono)

# Crear un campo de entrada (input) más grande
entrada = tk.Entry(ventana, width=80)  # Ajustar el ancho del campo de entrada
entrada.pack(pady=20)  # Añadir un espacio en blanco (padding) debajo del campo de entrada

# Crear un botón
def actualizar_título():
    nuevo_título = entrada.get()  # Obtener el texto ingresado en el campo de entrada
    ventana.title(nuevo_título)  # Actualizar el título de la ventana

boton_actualizar = tk.Button(ventana, text="Actualizar Título", command=actualizar_título)
boton_actualizar.pack()

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
