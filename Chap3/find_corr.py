def find_corr_x_y(x, y):
    n = len(x)

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

if __name__ == "__main__":
    high_school_grades = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
    college_admission_test_scores = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]

    from matplotlib import pyplot as plt
    plt.plot(high_school_grades, college_admission_test_scores, 'o')
    plt.xlabel('High school grades')
    plt.ylabel('College admission test scores')
    plt.show()

    corr = find_corr_x_y(high_school_grades, college_admission_test_scores)
    print('The correlation is {0}'.format(corr))

    high_school_math_grades = [83, 85, 84, 96, 94, 86, 87, 97, 97, 85]
    plt.plot(high_school_math_grades, college_admission_test_scores, 'o')
    plt.xlabel('High school math grades')
    plt.ylabel('College admission test scores')
    plt.show()

    corr = find_corr_x_y(high_school_math_grades, college_admission_test_scores)
    print('The correlation is {0}'.format(corr))
