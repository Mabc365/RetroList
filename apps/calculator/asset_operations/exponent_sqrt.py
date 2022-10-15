import math

def exponentiation():
    a = float(input("Base: "))
    b = float(input("Exponent: "))
    c = float(a**b)

    a = str(a)
    b = str(b)
    c = str(c)

    print(f"{a} ^ {b} = {c}")

def sqrt():
    a = float(input("Radicand: "))
    b = float(math.sqrt(a))

    a = str(a)
    b = str(b)

    print(f"√{a} = {b}")
