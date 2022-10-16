def multiplication():
    a = float(input("Multiplicand: "))
    b = float(input("Multiplier: "))
    c = float(a*b)

    a = str(a)
    b = str(b)
    c = str(c)

    print(f"{a} x {b} = {c}")

def division():
    a = float(input("Dividend: "))
    b = float(input("Divisor: "))
    c = float(a/b)

    a = str(a)
    b = str(b)
    c = str(c)

    print(f"{a} ÷ {b} = {c}")

def divisionRemainder():
    a = float(input("Dividend: "))
    b = float(input("Divsor: "))
    c = float(a/b)
    d = float(a%b)

    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)

    print(f"{a} ÷ {b} = {c} R {d}")
