'''
Enhanced correlation calculation
'''

def find_corr_x_y(x, y):
    n = len(x)
    if n != len(y):
        raise Exception('Two lists must have the same length.')

    # Find the sum of the products
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi * yi)
    
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2

    x_squares = []
    for xi in x:
        x_squares.append(xi ** 2)
    # Find the sum
    x_square_sum = sum(x_squares)

    y_squares = []
    for yi in y:
        y_squares.append(yi ** 2)
    # Find the sum
    y_square_sum = sum(y_squares)

    # Use the formula to calculate correlation
    numerator = n * sum_prod_x_y - sum_x * sum_y
    denominator_term1 = n * x_square_sum - squared_sum_x
    denominator_term2 = n * y_square_sum - squared_sum_y
    denominator = (denominator_term1 * denominator_term2) ** 0.5
    correlation = numerator / denominator

    return correlation

if __name__ == '__main__':
    a = [1, 2, 3]
    b = [9, 8, 7, 6]
    corr = find_corr_x_y(a, b)
