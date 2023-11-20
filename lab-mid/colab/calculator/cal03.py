def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"

def square_root(num):
    if num >= 0:
        return num ** 0.5
    else:
        return "Cannot find square root of a negative number"