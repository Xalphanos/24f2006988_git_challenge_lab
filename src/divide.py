def div(a, b):
    if float(b) == 0.0:
        raise ZeroDivisionError("divide by zero")
    return a / b

def idiv(a, b):
    b = int(b)
    if b == 0:
        raise ZeroDivisionError("divide by zero")
    return int(a) // b

def mod(a, b):
    b = int(b)
    if b == 0:
        raise ZeroDivisionError("divide by zero")
    return int(a) % b
