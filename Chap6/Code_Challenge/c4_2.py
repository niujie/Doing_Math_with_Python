'''
绘制Mandelbrot集
'''

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import random

def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image

def create_Mandelbrot(x_p, y_p):
    image = initialize_image(x_p, y_p)
    x = np.linspace(-2.5, 1.0, x_p)
    y = np.linspace(-1.0, 1.0, y_p)
    max_iter = 10000
    for k in range(y_p):
        for i in range(x_p):
            iter = 0
            c = complex(x[i], y[k])
            z = 0 + 0j
            while abs(z) < 2 and iter < max_iter:
                z = z**2 + c
                iter += 1
            image[k][i] = iter
    return image

def color_points():
    x_p = 400
    y_p = 400
    image = create_Mandelbrot(x_p, y_p)
    
    plt.imshow(image, origin='lower', extent=(-2.5, 1, -1, 1))
    plt.colorbar()
    plt.show()

if __name__ == '__main__':
    color_points()