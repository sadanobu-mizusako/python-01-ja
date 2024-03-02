def check_decimal(a, b):
    return (isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float)) 

def add(a, b):
    if check_decimal(a, b):
        return a + b
    else:
        return "bad input"

def subtract(a, b):
    if check_decimal(a, b):
        return a - b
    else:
        return "bad input"


def multiply(a, b):
    if check_decimal(a, b):
        return a * b
    else:
        return "bad input"


def divide(a, b):
    if check_decimal(a, b):
        if b==0:
            return "Cannot divide by zero"
        else:
            return a / b
    else:
        return "bad input"
