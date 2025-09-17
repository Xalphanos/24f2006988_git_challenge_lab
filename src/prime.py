def is_prime(n):
    n = int(n)
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def next_prime(n):
    n = int(n) + 1
    while not is_prime(n):
        n += 1
    return n
