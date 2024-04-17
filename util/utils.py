import sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import matplotlib.pyplot as plt
import cv2


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



