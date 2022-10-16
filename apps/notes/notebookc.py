import os

def newNotebook():
    global nnni
    nnni = input("New Notebook Name \n Please note that your notebook name should be composed of one word or multiple composing of a dash (-) or a underscore (_) or some other character to seperate multiple words for a notebooks name. \n > ")
    nnb = open(f"./notebooks/{nnni}.txt", "w+")
    nnb.close()

def deleteNotebook():
    dnni = input("Notebook to delete name \n > ")
    if os.path.exists(f"./notebooks/{dnni}.txt"):
        os.remove(f"./notebooks/{dnni}.txt")
    else:
        if os.path.exists(f"./notebooks/{dnni}.txt") == False:
            print("This notebook doesn't exist \n Please enter a notebook name again")
            deleteNotebook()
