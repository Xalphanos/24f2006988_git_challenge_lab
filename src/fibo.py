def fib(n):
    n = int(n)
    if n < 0:
        raise ValueError("negative n")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
