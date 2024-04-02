import subprocess
import tkinter as tk

def button1_click():
    subprocess.run(["python", "ColorBalance.py"])

def button2_click():
    subprocess.run(["python", "HistogramEqualization.py"])

def button3_click():
    subprocess.run(["python", "MedianFilter.py"])

def button4_click():
    subprocess.run(["python", "MeanFilter.py"])

def button5_click():
    subprocess.run(["python", "GaussianSmoothing.py"])

root = tk.Tk()
root.title("Image Processing")

button1 = tk.Button(root, text="Color Balance", command=button1_click)
button1.grid(row=0, column=0)

button2 = tk.Button(root, text="Histogram Equalization", command=button2_click)
button2.grid(row=0, column=1)

button3 = tk.Button(root, text="Median Filter", command=button3_click)
button3.grid(row=0, column=2)

button4 = tk.Button(root, text="Mean Filter", command=button4_click)
button4.grid(row=1, column=0)

button5 = tk.Button(root, text="Gaussian Smoothing", command=button5_click)
button5.grid(row=1, column=1)

root.mainloop()
