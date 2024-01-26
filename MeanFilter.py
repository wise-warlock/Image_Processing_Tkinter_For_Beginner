import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import numpy as np

class MeanFilterTkinter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mean Filter Image Processing")

        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(pady=10)

        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()

        self.filtered_image_frame = tk.Frame(self.root)
        self.filtered_image_frame.pack(pady=10)

        self.filtered_image_label = tk.Label(self.filtered_image_frame)
        self.filtered_image_label.pack()

        self.load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=10)

    def mean_filter(self, image_array):
        kernel_size = (3, 3)
        kernel = np.ones(kernel_size, dtype=int) / np.prod(kernel_size)
        filtered_image = cv2.blur(image_array, kernel_size)
        return filtered_image

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg *.jpeg *.png')])
        if file_path:
            image = cv2.imread(file_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            image_photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=image_photo)
            self.image_label.image = image_photo
            img_array = np.array(image)
            filtered_img = self.mean_filter(img_array)
            filtered_image = Image.fromarray(filtered_img)
            filtered_image_photo = ImageTk.PhotoImage(filtered_image)
            self.filtered_image_label.config(image=filtered_image_photo)
            self.filtered_image_label.image = filtered_image_photo

    def run(self):
        self.root.mainloop()

app = MeanFilterTkinter()
app.run()


