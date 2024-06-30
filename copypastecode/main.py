import tkinter as tk
import clipboard



def onButtonClick(btnId):
    defaultBtnWindowSettings = list()
    defaultBtnWindowSettings.append("800x200")
    defaultBtnWindowSettings.append("400x400")

    if btnId == "settings":
        btnWindow = tk.Tk()
        btnWindow.title("Settings")
        btnWindow.geometry("1000x800")

        createSettingsMenu(btnWindow)

        btnWindow.mainloop()

    if btnId == 1:
        btnWindow = tk.Tk()
        btnWindow.title("Tkinter copyables")
        btnWindow.geometry(defaultBtnWindowSettings[0])

        createBtnWindowContents(btnWindow,btnId)

        btnWindow.mainloop()
    if btnId == 2:
        btnWindow = tk.Tk()
        btnWindow.title("Random copyables")
        btnWindow.geometry(defaultBtnWindowSettings[0])
        
        createBtnWindowContents(btnWindow,btnId)

        btnWindow.mainloop()
    
    if btnId == 1-1:
        btnWindow = tk.Tk()
        btnWindow.title("Tkinter window with no contents")
        btnWindow.geometry(defaultBtnWindowSettings[1])

        createBtnWindowContents(btnWindow,btnId)

        btnWindow.mainloop()

    if btnId == 1-2:
        btnWindow = tk.Tk()
        btnWindow.title("Tkinter window with a button")
        btnWindow.geometry(defaultBtnWindowSettings[1])

        createBtnWindowContents(btnWindow,btnId)

        btnWindow.mainloop()
    
    if btnId == 1-3:
        btnWindow = tk.Tk()
        btnWindow.title("Tkinter window with a label")
        btnWindow.geometry(defaultBtnWindowSettings[1])

        createBtnWindowContents(btnWindow,btnId)

        btnWindow.mainloop()
    
    if btnId == 2-1:
        btnWindow = tk.Tk()
        btnWindow.title("Download a file (request package)")
        btnWindow.geometry(defaultBtnWindowSettings[1])

        createBtnWindowContents(btnWindow,btnId)

        btnWindow.mainloop()
def createBtnWindowContents(btnWindow, btnId):
    if btnId == 1:
        button = tk.Button(btnWindow, text="Window with no contents",width=20,height=5, command= lambda: onButtonClick(1-1))
        button.place(x=0,y=0)

        button = tk.Button(btnWindow, text="Window with a button",width=20,height=5, command= lambda: onButtonClick(1-2))
        button.place(x=150,y=0)

        button = tk.Button(btnWindow, text="Window with a label",width=20,height=5, command= lambda: onButtonClick(1-3))
        button.place(x=300,y=0)
    
    if btnId == 1-1:


        with open("./copyFiles/tkWindowNoContent.txt", "r") as file:
            contents = file.read()

        text = tk.Text(btnWindow,width=600,height=600); text.insert(1.0, contents); text.place(x=45,y=0)

        text.configure(state="disabled")
        text.configure(inactiveselectbackground=text.cget("selectbackground"))

        buttonRun = tk.Button(btnWindow, text="Run", width=5,height=5,command= lambda: runCode(contents))
        buttonRun.place(x=0,y=0)

        buttonCopy = tk.Button(btnWindow, text="Copy",width=5,height=5,command= lambda: copy2clip(contents))
        buttonCopy.place(x=0,y=90)
    if btnId == 1-2:


        with open("./copyFiles/tkWindowWithBtn.txt", "r") as file:
            contents = file.read()

        text = tk.Text(btnWindow,width=600,height=600); text.insert(1.0, contents); text.place(x=45,y=0)

        text.configure(state="disabled")
        text.configure(inactiveselectbackground=text.cget("selectbackground"))

        buttonRun = tk.Button(btnWindow, text="Run", width=5,height=5,command= lambda: runCode(contents))
        buttonRun.place(x=0,y=0)

        buttonCopy = tk.Button(btnWindow, text="Copy",width=5,height=5,command= lambda: copy2clip(contents))
        buttonCopy.place(x=0,y=90)
    
    if btnId == 1-3:


        with open("./copyFiles/tkWindowWithLabel.txt", "r") as file:
            contents = file.read()

        text = tk.Text(btnWindow,width=600,height=600); text.insert(1.0, contents); text.place(x=45,y=0)

        text.configure(state="disabled")
        text.configure(inactiveselectbackground=text.cget("selectbackground"))

        buttonRun = tk.Button(btnWindow, text="Run", width=5,height=5,command= lambda: runCode(contents))
        buttonRun.place(x=0,y=0)

        buttonCopy = tk.Button(btnWindow, text="Copy",width=5,height=5,command= lambda: copy2clip(contents))
        buttonCopy.place(x=0,y=90)

    if btnId == 2:
        button = tk.Button(btnWindow, text="Download a file (request package)",width=25,height=5, command= lambda: onButtonClick(2-1))
        button.place(x=10,y=0)
    
    if btnId == 2-1:


        with open("./copyFiles/reDownloadFile.txt", "r") as file:
            contents = file.read()

        text = tk.Text(btnWindow,width=600,height=600); text.insert(1.0, contents); text.place(x=45,y=0)

        text.configure(state="disabled")
        text.configure(inactiveselectbackground=text.cget("selectbackground"))


        buttonCopy = tk.Button(btnWindow, text="Copy",width=5,height=5,command= lambda: copy2clip(contents))
        buttonCopy.place(x=0,y=90)
        

def runCode(code):
    exec(code)

def copy2clip(txt):
    clipboard.copy(txt)

def StartWindow(title):
    root = tk.Tk()
    root.title(str(title))
    root.geometry("500x235")

    button = tk.Button(root, text="Tkinter",width=10,height=5, command= lambda: onButtonClick(1))
    button.place(x=0,y=0)

    #button = tk.Button(root, text="Download file (requests)",width=15,height=5, command= lambda: onButtonClick(2-1))
    #button.place(x=100,y=0)

    #button = tk.Button(root, text="Settings",width=10,height=5, command= lambda: onButtonClick("settings"))
    #button.pack()

    root.mainloop()

def createSettingsMenu(btnWindow):
    with open("./settings.json", "r") as file:
            contents = file.read()

    #global textSettings
    textSettings = tk.Text(btnWindow,width=600,height=40)
    textSettings.insert(1.0, contents); textSettings.place(x=45,y=0)

    textSettings.configure(state="normal")
    textSettings.configure(inactiveselectbackground=textSettings.cget("selectbackground"))


    ##buttonSave = tk.Button(btnWindow, text="Save", width=5,height=5,command= lambda: saveSettings())
    ##buttonSave.place(x=0,y=0)

if __name__ == "__main__":
    StartWindow("Main window")
