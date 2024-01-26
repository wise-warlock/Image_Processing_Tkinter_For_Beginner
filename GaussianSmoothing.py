import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class GaussianBlurApp:
    def __init__(self, window):
        self.window = window
        self.image = None
        self.blurred_image = None

        # Create a button to load an image
        load_button = tk.Button(window, text="Load Image", command=self.load_image)
        load_button.pack()

        # Create a label to display the image
        self.image_label = tk.Label(window)
        self.image_label.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        self.image = cv2.imread(file_path)
        self.blurred_image = cv2.GaussianBlur(self.image, (5, 5), 0)
        self.update_image()

    def update_image(self):
        blurred_image_rgb = cv2.cvtColor(self.blurred_image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(blurred_image_rgb)
        image_tk = ImageTk.PhotoImage(pil_image)
        self.image_label.configure(image=image_tk)
        self.image_label.image = image_tk

# Initialize the Tkinter window
window = tk.Tk()
window.title("Gaussian Blurring")

# Run the application
app = GaussianBlurApp(window)

# Start the Tkinter mainloop
window.mainloop()


