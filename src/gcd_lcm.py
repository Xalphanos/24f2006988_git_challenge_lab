def gcd(a, b):
    a, b = int(a), int(b)
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    a, b = int(a), int(b)
    if a == 0 or b == 0:
        return 0
    from math import prod
    g = gcd(a, b)
    return abs(a*b) // g
