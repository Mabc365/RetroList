
import os
clear = lambda : os.system('cls')

todoList = []

def view():
    print(todoList)

def new():
    clear()
    newItem = input("New Item: ")
    todoList.append(newItem)
    print(todoList)

def done():
    clear()
    doneItem = input("Done Item: ")
    todoList.remove(doneItem)
    print(todoList)

def help():
    print("Help Menu")
    print("view -> views the current todoList for the current session")
    print("new -> prompts to add a new item to the current todoList for the current session")
    print("done -> prompts to remove a item from the current todoList for the current session")
    print("exit -> exits the todoList app deleting all todo items and not saving the session")

def main():
    clear()
    print(todoList)
    todo = input("Todo: ")
    
    if todo == "view":
        view()
    if todo == "new" or todo == "+":
        new()
    if todo == "done" or todo == "-":
        done()
    if todo == "exit":
        exit()
    if todo == "help":
        help()

while True:
    main()
