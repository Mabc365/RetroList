from asset_operations import add_subtract
from asset_operations import multiply_divide
from asset_operations import exponent_sqrt

import os
clear = lambda : os.system('cls')

def help():
    print("Help Menu")
    print("+ -> stands for the addition operation")
    print("- -> stands for the subtraction operation")
    print("x -> stands for the multiplication operation")
    print("/ -> stands for the division operation")
    print("% -> stands for the division operation but also presents the remainder. please note that there will still be a decimal, but just ignore all numbers after the decimal point")
    print("^ -> stands for exponentiation, which is multipliying a number multiple times by itself")
    print("sqrt -> stands for square roots, it will root any number")
    print("clear -> clears the app window of all previous actions and calculations")
    print("exit - exits the calculator app")

def main():
    op = input("\n Which operations \n | + | - | x | / | % | ^ | sqrt | clear | exit | help | \n > ")

    if op == "+":
        print()
        add_subtract.addition()
    if op == "-":
        add_subtract.subtraction()
    if op == "x":
        print()
        multiply_divide.multiplication()
    if op == "/":
        print()
        multiply_divide.division()
    if op == "%":
        print()
        multiply_divide.divisionRemainder()
    if op == "^":
        print()
        exponent_sqrt.exponentiation()
    if op == "sqrt":
        print()
        exponent_sqrt.sqrt()
    if op == "exit":
        exit()
    if op == "help":
        print()
        help()
    if op == "clear":
        clear()


while True:
    main()
