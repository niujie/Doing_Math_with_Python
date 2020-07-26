'''
在正方形中填充圆形
'''

from matplotlib import pyplot as plt

def draw_square(ax):
    square = plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], closed=True)
    ax.add_patch(square)

def draw_circles(ax):
    y = 1.5
    while y < 5:
        x = 1.5
        while x < 5:
            c = create_circle(x, y)
            ax.add_patch(c)
            x += 1.0
        y += 1.0

def create_circle(x, y):
    circle = plt.Circle((x, y), radius = 0.5, fc = 'g', ec = 'r')
    return circle

if __name__ == '__main__':
    ax = plt.axes (xlim = (0, 6), ylim = (0, 6))
    ax.set_aspect('equal')
    draw_square(ax)
    draw_circles(ax)
    plt.show()