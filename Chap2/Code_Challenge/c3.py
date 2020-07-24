'''
Enhanced version of trajectory.py
Draw the trajectory of a body in projectile motion
'''

from matplotlib import pyplot as plt
import math

def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordiante')
    plt.ylabel('y-coordiante')
    plt.title('Projectile motion of a ball')

'''
Generate equally spaced floating point
numbers between two given values
'''

def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    
    return numbers

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight =2 * u * math.sin(theta) / g
    # Find the intervals
    intervals = frange(0, t_flight, 0.001)
    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t * t)
    
    draw_graph(x, y)
    return t_flight, max(x), max(y)

if __name__ == '__main__':
    u_list = []
    theta_list = []
    try:
        n = int(input('How many trajectories? '))
    except ValueError:
        print('You entered an invalid input')
    else:
        for i in range(n):
            try:
                u = float(input('Enter the initial velocity for trajectory {} (m/s): '.format(i+1)))
                theta = float(input('Enter the angle of projection for trajectory {} (degrees): '.format(i+1)))
            except ValueError:
                print('You entered an invalid input')
            else:
                u_list.append(u)
                theta_list.append(theta)
    
        for i in range(n):
            t_flight, max_x, max_y = draw_trajectory(u_list[i], theta_list[i])
            print('flight time = {0}, max horizontal dist = {1}, max vertical dist = {2}'.format(t_flight, max_x, max_y))
        plt.legend(['u = {0}, theta = {0}'.format(u_list[0], theta_list[0]),
                     'u = {0}, theta = {1}'.format(u_list[1], theta_list[1]),
                     'u = {1}, theta = {1}'.format(u_list[2], theta_list[2])])
        plt.show()