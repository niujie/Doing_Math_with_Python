'''
探索Henon函数
'''
from matplotlib import pyplot as plt
from matplotlib import animation

def transform(p):
    x = p[0]
    y = p[1]
    x1 = y + 1 - 1.4 * x**2
    y1 = 0.3 * x

    return x1, y1

def update_points(i, x, y, plot, ax):
    ax.set_title(f'Henon with {i} points')
    plot.set_data(x[:i], y[:i])
    return plot,

def draw_Henon():
    N = 20000
    x = [0]
    y = [0]
    x1, y1 = 1, 1
    for i in range(N):
        x1, y1 = transform([x1, y1])
        x.append(x1)
        y.append(y1)
    
    fig = plt.gcf()
    ax = plt.axes(xlim = (min(x), max(x)), ylim = (min(y), max(y)))
    plot, = ax.plot([], [], '.')
    anim = animation.FuncAnimation(fig, update_points, fargs=(x, y, plot, ax), frames = len(x), interval = 25, blit=False)
    plt.title(f'Henon with {N} points')
    plt.show()

if __name__ == '__main__':
    draw_Henon()