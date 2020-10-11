def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"Subtract {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"Multiply {a} * {b}")
    return a * b

def divide(a,b):
    print(f"Divide {a} / {b}")
    return a / b

print("Let's do some math with just functions.")

age = add(30,5)
height = subtract(190,11)
weight = multiply(77,3)
iq = divide(221,2)

print(f"Age is: {age}, Height is: {height}, Weight is: {weight}, IQ is: {iq}")
