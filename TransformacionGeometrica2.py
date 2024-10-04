import tkinter as tk
from PIL import Image, ImageTk

image_path = "ganon.jpg"  
image = Image.open(image_path)

rotated_image_30 = image.rotate(-30, expand=True)

rotated_image_60 = rotated_image_30.rotate(60, expand=True)

scaled_image = rotated_image_60.resize((rotated_image_60.width * 2, rotated_image_60.height * 2))

window = tk.Tk()
window.title("Imagen Transformada")
window.geometry(f"{scaled_image.width+50}x{scaled_image.height+50}")  

canvas = tk.Canvas(window, width=scaled_image.width, height=scaled_image.height)
canvas.pack()

tk_image = ImageTk.PhotoImage(scaled_image)

canvas.create_image(scaled_image.width // 2, scaled_image.height // 2, image=tk_image)

window.mainloop()