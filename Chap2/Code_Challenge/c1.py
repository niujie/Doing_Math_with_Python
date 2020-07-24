'''
温度如何变化
'''

from matplotlib import pyplot as plt

def create_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('time')
    plt.ylabel('temperature')

if __name__ == '__main__':
    time_nyc = ['12:00 PM', '15:00 PM', '18:00 PM', '21:00 PM', '00:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '11:59 AM']
    temp_nyc = [24, 27, 27, 26, 25, 24, 24, 24, 29]
    create_graph(time_nyc, temp_nyc)
    time_sf = ['12:00 PM', '15:00 PM', '18:00 PM', '21:00 PM', '00:00 AM', '03:00 AM', '06:00 AM', '09:00 AM', '11:59 AM']
    temp_sf = [13, 15, 17, 16, 15, 14, 14, 14, 19]
    create_graph(time_sf, temp_sf)
    plt.legend(['NYC', 'SF'])
    plt.show()