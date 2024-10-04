import tkinter as tk
from PIL import Image, ImageTk

image_path = "ganon.jpg"  
image = Image.open(image_path)

rotated_image = image.rotate(70, expand=True)

scaled_image = rotated_image.resize((rotated_image.width * 2, rotated_image.height * 2))

window = tk.Tk()
window.title("Imagen Transformada")
window.geometry(f"{scaled_image.width+100}x{scaled_image.height+100}")  

canvas = tk.Canvas(window, width=scaled_image.width+50, height=scaled_image.height+50)
canvas.pack()

tk_image = ImageTk.PhotoImage(scaled_image)

image_x = 20  
image_y = 20  
canvas.create_image(image_x, image_y, anchor=tk.NW, image=tk_image)  

window.mainloop()