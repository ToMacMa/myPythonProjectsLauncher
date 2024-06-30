import tkinter as tk
Font1 = ("Courier New CE", 20) 
Font2 = ("Courier New CE", 10) 

def downloadLibraries():
    import tkinter as tk

    print("downloading/updating required libraries")


    import subprocess
    subprocess.run("pip3 install requests")
    subprocess.run("pip3 install clipboard")
    subprocess.run("pip3 install pathlib")

    print("task succesfull")
#downloadLibraries()
import os, json


def runFile(file):
    exec(open(file).read(), globals())


root = tk.Tk()
root.geometry("500x500")
root.title("GAMES")
def loadGamesData():
    with open('games.json') as f:
        data = json.load(f)
    
    stop = 0
    for i in range(0,9999):
        try:
            if stop == 0:
                with open("./games.json") as f:
                    data = json.load(f)
        

            d = loadGameData(data['games'][i]['installPath'])
            print(d)
            


            name = d['displayTitle']
            gameButton = tk.Button(root,text=name,font=Font1,
                                   command=lambda d=d: runFile(d['runFile']))
            gameButton.place(x=i*100,y=40)
            

            description = d['description']

            descriptionLabel = tk.Label(root, text=description,font=Font2)
            descriptionLabel.place(x=i*100,y=100)


        except:
            stop = 1

def loadGameData(game):
    with open(game) as f:
        data = json.load(f)
        return data

def createRootWindowContent():
    titleScreenText = tk.Label(root,text="Games")
    titleScreenText.pack()

    loadGamesData()

createRootWindowContent()

root.mainloop()