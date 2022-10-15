import os
clear = lambda : os.system('cls')

def startup():
    global notebooksList
    notebooksList = os.listdir('./notebooks')
    print(notebooksList)
    global globalnotebook
    status = bool(False)
    globalnotebook = input("Which notebook: ")
    global nnbi

    def newNotebook():
        global nnbi
        nnbi = input("New Notebook Name \n Please note that your notebook name should be composed of one word or multiple composing of a dash (-) or a underscore (_) or some other character to seperate mutliple words for a notebook name. \n > ")
        global sortednnbi
        sortednnbi = repr(nnbi)
        nni = open(f"./notebooks/{nnbi}.txt", "w+")
        nni.write("")
        nni.close()
        nnni = open(f"./notebooks/{nnbi}.txt", "r")
        nnni.close()

    def help():
        print("Notebook Commands Help Menu")
        print("new -> creates a new notebook")
        print("remove -> removes the notebook specified")
        print("exit -> exits the note app in the RetroList app")


    if (globalnotebook == "new"):
        newNotebook()
        globalnotebook = (f"./notebooks/{nnbi}.txt")
        startup()

    if (globalnotebook == "remove"):
        deleteNotebook()
        startup()

    if (globalnotebook == "exit"):
        exit()
        
    if (f"{globalnotebook}.txt") in notebooksList:
        status = True
    else:
        status = False

    if status is False:
        print("This notebook doesn't exist \n Please enter a note book again")
        startup()
        

def viewNote():
    vn = open(f"./notebooks/{globalnotebook}.txt", "r")
    print(vn.read())
    vn.close()

def newNote():
    newNotei = input("New Note: ")
    nn = open(f"./notebooks/{globalnotebook}.txt", "a")
    nn.write(f"\n{newNotei}")
    nn.close()

def clearNotes():
    clearNotesi = input("Are you sure you want to clear all notes from notebook \n Please enter y for yes and n for no as there is no way to recover notes after they were deleted \n > ")
    if clearNotesi == "y":
        cn = open(f"./notebooks/{globalnotebook}", "w")
        cn.close()
        print("Your notes were erased from your notebook")
    if clearNotesi == "n":
        print("Your notes from your notebook have not been deleted")

def help():
    print("Notes Commands Help Menu")
    print("selectNotebook -> Opens the notebook selection menu")
    print("newNotebook -> Creates a new notebook")
    print("removeNotebook -> deletes the ntoebook specified permenantly")
    print("view -> views all notes from your notebook")
    print("new -> allows you to add a new note to your notebook")
    print("clearNotes -> allows you to clear your notebook of all notes")
    print("exit -> exits the note app in the RetroList app")


def parentMain():
    clear()
    notebook = input("Notebook Command: ")
    
    if notebook == "selectNotebook":
        startup()
    if notebook == "view":
        viewNote()
    if notebook == "newNotebook":
        newNotebook()
    if notebook == "removeNotebook":
        deleteNotebook()
    if notebook == "new":
        newNote()
    if notebook == "clearNotes":
        clearNotes()
    if notebook == "exit":
        exit()
    if notebook == "help":
        help()

def main():
    startup()
    while True:
        parentMain()
