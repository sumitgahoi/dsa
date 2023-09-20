# n is a number to the base 10. This function converts it to the given base.
def expand(n, base):
    result = []
    q = n
    while q > 0:
        q, r = divmod(q, base)
        result.append(r)
    return result[::-1]

# b to the power n mod m
def modular_exponentiation(b, n, m):
    # expand n into binary
    bits = expand(n, 2)

    product = 1
    b_2 = b
    for bit in bits[::-1]:
        if bit == 1:
            product = (product * b_2 % m) % m
        b_2 = b_2 ** 2
    
    return product

# b and n are large numbers
def binary_exponentiation(b, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        tmp = binary_exponentiation(b, n // 2)
        return tmp * tmp
    else:
        return binary_exponentiation(b, n - 1) * b
        

# b and n are large numbers
def binary_exponentiation_iterative(b, n):
    result = 1
    while n > 0:
        q, r = divmod(n,2)
        if r == 1:
            result *= b
        b **= 2
        n = q
    return result