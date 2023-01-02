#!/bin/python3
from PIL import Image
import math
import os
import time

def colorimetrie(color):
    r, g, b = color[:3]
    luminance = " .,:;i1tfLCG08@"
    lum = 26
    color = f"\u001b[38;2;{r};{g};{b}m"
    char = luminance[min(int(math.sqrt(r**2 + g**2 + b**2)/lum), len(luminance)-1)]
    return color + char

def image(lien):
    im = Image.open(lien)
    # width, height = 39, 20 # dicord tel
    # width, height = 88, 44 # dicord ordi
    # width, height = 180, 90 # jsp

    x, y = im.size
    k = 227
    width, height = k, int(y*k/(x*2))
    im = im.resize((width, height))
    im = im.load()
    ch = ""
    for h in range(0, height):
        for w in range(0, width):
            ch += colorimetrie(im[w, h])
        ch += "\n"
    os.system("clear")
    print(ch)
    return None




lien = "video/frame"
extension = ".png"
i = 1
while True:
    try:    
        image(lien + str(i) + extension)
        i += 1
    except:
        break


