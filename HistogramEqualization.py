import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class HistogramEqualization:
    def __init__(self, window):
        self.window = window
        self.window.title("Histogram Equalization")

        self.img = None
        self.img_eq = None

        self.load_button = Button(self.window, text="Load Image", command=self.load_image)
        self.load_button.pack(side="top", fill="both", expand=True)

        self.fig = plt.Figure(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        self.fig_hist = plt.Figure(figsize=(8, 4))
        self.canvas_hist = FigureCanvasTkAgg(self.fig_hist, master=self.window)
        self.canvas_hist.get_tk_widget().pack(side="top", fill="both", expand=True)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        self.img = cv2.imread(file_path)
        self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img_eq = cv2.equalizeHist(self.img_gray)
        self.update_image()

    def update_image(self):
        img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        img_eq_rgb = cv2.cvtColor(self.img_eq, cv2.COLOR_BGR2RGB)

        self.fig.clear()
        axs = self.fig.add_subplot(121)
        axs.imshow(img_rgb)
        axs.set_title("Original Image")

        axs = self.fig.add_subplot(122)
        axs.imshow(img_eq_rgb)
        axs.set_title("Equalized Image")

        self.canvas.draw()

        # Display histograms
        hist_original = cv2.calcHist([self.img], [0], None, [256], [0, 255])
        hist_equalized = cv2.calcHist([self.img_eq], [0], None, [256], [0, 255])

        self.fig_hist.clear()
        axs_hist = self.fig_hist.add_subplot(121)
        axs_hist.plot(hist_original)
        axs_hist.set_title("Original Image Histogram")

        axs_hist = self.fig_hist.add_subplot(122)
        axs_hist.plot(hist_equalized)
        axs_hist.set_title("Equalized Image Histogram")

        self.canvas_hist.draw()

window = Tk()
histogram_equalization = HistogramEqualization(window)
window.mainloop()


