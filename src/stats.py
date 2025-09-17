def mean(xs):
    if not xs: raise ValueError("empty")
    return sum(xs) / len(xs)

def median(xs):
    if not xs: raise ValueError("empty")
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    if n % 2: return s[mid]
    return (s[mid-1] + s[mid]) / 2

def mode(xs):
    if not xs: raise ValueError("empty")
    counts = {}
    for x in xs: counts[x] = counts.get(x, 0) + 1
    best = max(counts.items(), key=lambda kv: (kv[1], -float(kv[0])))
    return best[0]

def variance(xs):
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)

def stdev(xs):
    from math import sqrt
    return sqrt(variance(xs))
