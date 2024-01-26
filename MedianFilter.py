import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class MedianFilterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Median Filter')

        self.image_data = None

        self.button_load = tk.Button(self, text='Load image', command=self.load_image)
        self.button_load.pack(pady=10)

        self.label_filter_size = tk.Label(self, text='Filter size:')
        self.label_filter_size.pack()

        self.entry_filter_size = tk.Entry(self)
        self.entry_filter_size.pack()

        self.button_filter = tk.Button(self, text='Apply median filter', command=self.median_filter)
        self.button_filter.pack(pady=10)

        self.label_image = tk.Label(self)
        self.label_image.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[('Image files', '*.png *.jpg *.jpeg')])
        if file_path:
            self.image_data = cv2.imread(file_path)
            image_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(self.image_data, cv2.COLOR_BGR2RGB)))
            self.label_image.config(image=image_tk)
            self.label_image.image = image_tk

    def median_filter(self):
        if self.image_data is None:
            return
        filter_size = int(self.entry_filter_size.get())
        if filter_size % 2 == 0:
            filter_size += 1
        self.image_data = cv2.medianBlur(self.image_data, filter_size)
        image_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(self.image_data, cv2.COLOR_BGR2RGB)))
        self.label_image.config(image=image_tk)
        self.label_image.image = image_tk

app = MedianFilterApp()
app.mainloop()


