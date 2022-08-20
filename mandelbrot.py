import numpy as np
from PIL import Image


x1 = -2.1
x2 = 0.6
y1 = -1.2
y2 = 1.2

img = np.zeros((x1 - x2, y1 - y2, 3))

def mandelbrot(x, y):
    c = complex(x, y)
    z = 0

    for i in range(50):
        z = z**2 + c
        print(abs(z))

        if abs(z) >= 2:
            break
        # display pixel via x,y ...