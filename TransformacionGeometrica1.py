import tkinter as tk
from PIL import Image, ImageTk

image_path = "ganon.jpg"  
image = Image.open(image_path)

rotated_image = image.rotate(-60, expand=True)

scaled_image = rotated_image.resize((int(rotated_image.width / 5), int(rotated_image.height / 5)))

window = tk.Tk()
window.title("Imagen Transformada")
window.geometry("600x600") 

canvas = tk.Canvas(window, width=600, height=600)
canvas.pack()

tk_image = ImageTk.PhotoImage(scaled_image)

image_x = (600 - scaled_image.width) // 2 + 10  
image_y = (600 - scaled_image.height) // 2 + 10  
canvas.create_image(image_x, image_y, image=tk_image)

window.mainloop()