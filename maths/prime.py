from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    
    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # See https://en.wikipedia.org/wiki/Primality_test#Simple_methods
    # using 6k ± 1 optimization 
    for i in range(5, int(sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

#Linear Congruential method
def generate_pseudo_random(seed, multiplier, increment, modulus, count = 5):
    result = []
    while count > 0:
        seed = (seed * multiplier + increment) % modulus
        result.append(seed / modulus)
        count-=1
    return result