'''
Quadratic function calculator
'''

# Assue value of x
x_values = [-1, 1, 2, 3, 4, 5]
for x in x_values:
    # Calculate the value of the quadratic function
    y = x ** 2 + 2 * x + 1
    print('x={0} y={1}'.format(x, y))

x_values = [-3, -2, -1, 1, 2, 3, 4, 5, 6, 7]
y_values = []
for x in x_values:
    # Calculate the value of the quadratic function
    y = x ** 2 + 2 * x + 1
    print('x={0} y={1}'.format(x, y))
    y_values.append(y)

from matplotlib import pyplot as plt

plt.plot(x_values, y_values, marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = x^2 + 2x + 1')
plt.show()