from sympy import FiniteSet

def probability(space, event):
    return len(event) / len(space)

def check_prime(number):
    if number != 1:
        for factor in range(2, number):
            if number % factor == 0:
                return False
    else:
        return False
    return True

if __name__ == "__main__":
    space = FiniteSet(*range(1, 21))
    primes = []
    for num in space:
        if check_prime(num):
            primes.append(num)
    event = FiniteSet(*primes)
    p = probability(space, event)

    print(f'Sample space: {space}')
    print(f'Event: {event}')
    print(f'Probability of rolling a prime: {p:.5f}')

    space = range(1, 21)
    p = probability(space, primes)
    print(f'Probability of rolling a prime: {p:.5f}')