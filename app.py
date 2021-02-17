import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser

import os
from functions import *

SamplePalette = [{'HEX': "#363636",
                  'RGB': (54, 54, 54),
                  'CMYK': (0, 0, 0, 79),
                  'HSV': (0, 0, 21)},

                 {'HEX': "#363636",
                  'RGB': (54, 54, 54),
                  'CMYK': (0, 0, 0, 79),
                  'HSV': (0, 0, 21)},

                 {'HEX': "#363636",
                  'RGB': (54, 54, 54),
                  'CMYK': (0, 0, 0, 79),
                  'HSV': (0, 0, 21)},

                 {'HEX': "#363636",
                  'RGB': (54, 54, 54),
                  'CMYK': (0, 0, 0, 79),
                  'HSV': (0, 0, 21)},

                 {'HEX': "#363636",
                  'RGB': (54, 54, 54),
                  'CMYK': (0, 0, 0, 79),
                  'HSV': (0, 0, 21)}]

root = tk.Tk()
canvas = tk.Canvas(root, height=1000, width=1000, bg='#000000')
text = tk.Text(root)

image = tk.PhotoImage(file=os.getcwd()+"\static/background.png")
canvas.create_image(0, 0, image=image, anchor='nw')
canvas.pack()


def randomPalette():
    palette, highlightColor = getRandomPalette()

    paletteGen(canvas, palette, (57, 60), (227, 230), (500, 30, "Sampled"))

    compPalette = getComplementaryPalette(palette)
    paletteGen(canvas, compPalette, (57, 310), (227, 480), (500, 270, "Complimentary"))

    highlightPalette = getHighlightColors(palette, highlightColor)
    paletteGen(canvas, highlightPalette, (57, 560), (227, 730), (500, 520, "Highlight Colors"))


def load():
    paletteGen(canvas, SamplePalette, (57, 90), (227, 260), (500, 60, "Sampled"))
    paletteGen(canvas, SamplePalette, (57, 350), (227, 520), (500, 310, "Complimentary"))
    paletteGen(canvas, SamplePalette, (57, 610), (227, 780), (500, 570, "Color of highlights"))


def load_photo():
    filename = filedialog.askopenfile(filetypes=[("Images", ["*.png", "*.jpeg", "*.jpg"])])

    palette = getColorAttributes(filename.name, 5)
    paletteGen(canvas, palette, (57, 90), (227, 260), (500, 60, "Sampled"))

    compPalette = getComplementaryPalette(palette)
    paletteGen(canvas, compPalette, (57, 350), (227, 520), (500, 310, "Complimentary"))

    color_code = colorchooser.askcolor(title="Choose color of the light source")
    highlightPalette = getHighlightColors(palette, color_code[0])
    paletteGen(canvas, highlightPalette, (57, 610), (227, 780), (500, 570, "Color of highlights"))


# Buttons
open_image = tk.Button(root, text="Open Image", bg='#000000', command=load_photo)
open_image.place(x=50, y=850)

reset_canvas = tk.Button(root, text="Reset", bg='#000000', command=load)
reset_canvas.place(x=50, y=931)

random_palette = tk.Button(root, text="Random palette", bg='#000000', command=randomPalette)
random_palette.place(x=50, y=890)

# main
load()
root.title("Image Palette Generator")
root.resizable(False, False)
root.mainloop()
