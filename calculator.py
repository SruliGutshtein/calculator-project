def add(a,b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Dividing two numbers"""
    try:
        return a / b
    except ZeroDivisionError:
        return f"Dividing by 0 is not allowed"