# current day and time import module required
import datetime

# todo imports
from apps.todo import todo

# calculator imports
from apps.calculator import calculator
from apps.calculator.asset_operations import add_subtract
from apps.calculator.asset_operations import multiply_divide
from apps.calculator.asset_operations import exponent_sqrt

#notes imports
from apps.notes import note
from apps.notes.notebooks import *

print("RetroList Help Menu")
print("todo -> opens the todo app")
print("calculator -> opens the calculator app")
print("notes -> opens the notes app")
print("exit -> exits the RetroList app")

def main():
    print(
    """
    
 ____         _                 _      _       _
|  _ \   ___ | |_  _ __   ___  | |    (_) ___ | |_
| |_) | / _ \| __|| '__| / _ \ | |    | |/ __|| __|
|  _ < |  __/| |_ | |   | (_) || |___ | |\__ \| |_
|_| \_\ \___| \__||_|    \___/ |_____||_||___/ \__|
    
    """
    )

    now = datetime.datetime.now().strftime('%Y/%m/%d %I:%M:%S')
    
    app = input(f"\n Today: {now} \n Which App \n | todo | calculator | notes | exit | \n > ")

    if app == "todo":
        todo.main()
    if app == "calculator":
        calculator.main()
    if app == "notes":
        note.main()
    if app == "exit":
        exit()
     


while True:
    main()
