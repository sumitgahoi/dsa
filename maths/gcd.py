# euclidean algorithm to find greatest common divisor
def gcd(a, b):
    if b == 0:
        return abs(a)
    if a == 0:
        return abs(b)

    if a > b:
        r = a % b
    else:
        r = b % a
        
    return gcd(b, r)
 