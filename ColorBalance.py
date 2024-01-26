import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageColorBalanceApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Color Balance")
        self.image_path = None

        # Load Image button
        self.load_button = tk.Button(
            master, text="Load Image", command=self.load_image)
        self.load_button.pack()

        # Red balance slider
        self.red_scale = tk.Scale(
            master, label="Red Balance", from_=0, to=2, resolution=0.01, orient=tk.HORIZONTAL,
            command=self.update_image)
        self.red_scale.set(1.0)
        self.red_scale.pack()

        # Green balance slider
        self.green_scale = tk.Scale(
            master, label="Green Balance", from_=0, to=2, resolution=0.01, orient=tk.HORIZONTAL,
            command=self.update_image)
        self.green_scale.set(1.0)
        self.green_scale.pack()

        # Blue balance slider
        self.blue_scale = tk.Scale(
            master, label="Blue Balance", from_=0, to=2, resolution=0.01, orient=tk.HORIZONTAL,
            command=self.update_image)
        self.blue_scale.set(1.0)
        self.blue_scale.pack()

        # Canvas to display image
        self.canvas = tk.Canvas(master, bg="white", width=400, height=400)
        self.canvas.pack()

    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.display_image(self.original_image)

    def update_image(self, event=None):
        if self.image_path:
            red_balance = self.red_scale.get()
            green_balance = self.green_scale.get()
            blue_balance = self.blue_scale.get()

            balanced_image = Image.merge(
                "RGB",
                (
                    self.original_image.getchannel("R").point(lambda i: i * red_balance),
                    self.original_image.getchannel("G").point(lambda i: i * green_balance),
                    self.original_image.getchannel("B").point(lambda i: i * blue_balance),
                )
            )
            self.display_image(balanced_image)

    def display_image(self, image):
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

def main():
    root = tk.Tk()
    app = ImageColorBalanceApp(root)
    root.mainloop()

main()


