import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import ipywidgets as widgets
import random
import cv2
import numpy as np

def browseImages(self):
    window = tk.Tk()
    window.wm_attributes('-topmost', 1)
    window.withdraw()

    self.filename = filedialog.askopenfilename(parent=window,
                                               initialdir="test_img",
                                               title="Select File",
                                               filetypes = (("Image files", "*.png *.PNG *.jpg *.JPG *.jpeg *.JPEG"),
                                               ("All files", "*.*")))

    if self.filename == None:
        print("No File Selected")
        window.destroy()
    else:
        return self.filename
        window.destroy()

def showGrayscaleImage(self, image):
    if(len(image.shape) < 3):
        plt.figure()
        plt.axis("off")
        plt.imshow(image, cmap='Greys_r')
    else:
        raise ValueError('Image is not converted to graycsale.')

def start(main):
    button = widgets.Button(
                        description=' START',
                        disabled=False,
                        button_style='success', # 'success', 'info', 'warning', 'danger' or ''
                        icon='play'
                        )
    button.on_click(main)

    box_layout = widgets.Layout(display='flex',
                                flex_flow='column',
                                align_items='center',
                                width='100%')
    
    box = widgets.HBox(children=[button], layout=box_layout)

    return box


def generate_input():

    kernel = np.array([[0 for x in range(3)] for y in range(3)], dtype="int")
    input_image = np.array([[0 for x in range(8)] for y in range(8)], dtype="uint8")

    root = tk.Tk()
    root.title("Bemeneti Kép")
    root.resizable(False, False)

    kern = tk.Toplevel(root)
    kern.title("Kernel")
    kern.resizable(False, False)

    photo = tk.PhotoImage(width=1, height=1)

    def on_click_input(button, row, col):
        if button.cget('text') == "255":
            button.config(text="0", fg="white", bg="black")
            input_image[button.grid_info()['row']][button.grid_info()['column']] = 0
        else:
            button.config(text="255", fg="black", bg="white")
            input_image[button.grid_info()['row']][button.grid_info()['column']] = 255

    def on_click_kernel(button, row, col):
        if button.cget('text') == "0":
            button.config(text="1", fg="black", bg="white")
            kernel[button.grid_info()['row']][button.grid_info()['column']] = 1
        elif button.cget('text') == "1":
            button.config(text="-1", fg="white", bg="black")
            kernel[button.grid_info()['row']][button.grid_info()['column']] = -1
        else:
            button.config(text="0", fg="white", bg='#7f7f7f')
            kernel[button.grid_info()['row']][button.grid_info()['column']] = 0

    for row in range(8):
        for col in range(8):
            button = tk.Button(root, text=f'0')
            button.config(fg="white", bg="black", image=photo, width=50, height=50,
                          command=lambda button=button: on_click_input(button, row, col))
            button.grid(row=row, column=col)

    for row in range(3):
        for col in range(3):
            button = tk.Button(kern, text=f'0')
            button.config(fg="white", bg='#7f7f7f', image=photo,
                          width=50, height=50,
                          command=lambda button=button: on_click_kernel(button, row, col))
            button.grid(row=row, column=col)

    root.mainloop()
    kernel = (kernel + 1) * 127
    kernel = np.uint8(kernel)
    
    #print(kernel)
    #print(input_image)

    return input_image, kernel
