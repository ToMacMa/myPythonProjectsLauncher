i = 0
while 13 > i:
    print("")
    i = i + 1

print("installing/updating required libraries...")

import subprocess
subprocess.run("pip3 install requests")
subprocess.run("pip3 install clipboard")

print("succesfully installed/updated required libraries")

import tkinter as tk
import requests, os, json




def downloadFile(link, saveName):
    url = str(link)
    r = requests.get(url, allow_redirects=True)
    open(str(saveName), 'wb').write(r.content)
def downloads():
    with open("requiredData.json", "w") as file:
        file.write("")
    downloadFile('https://raw.githubusercontent.com/ToMacMa/CopyAndPastePythonCode/main/requiredData.json', 'requiredData.json')

    with open("defaultSettings.json", "w") as file:
        file.write("")
    downloadFile('https://raw.githubusercontent.com/ToMacMa/CopyAndPastePythonCode/main/defaultSettings.json',"defaultSettings.json")

    print("Downloaded/Updated jsons !")

    with open("main.py", "w") as file:
        file.write("")
    downloadFile('https://raw.githubusercontent.com/ToMacMa/CopyAndPastePythonCode/main/main.py', 'main.py')

    print("Dowloaded/Updated main.py !")

    i = 0
    files = list()
    for file in os.listdir():
        files.append(file)

        if file == "copyFiles":
            i = 1

    if i == 0:
        os.mkdir("./copyFiles/")

    i = 0
    for file in os.listdir():

        if file == "settings.json":
            i = 1
    
    if i == 0:
        downloadFile('https://raw.githubusercontent.com/ToMacMa/CopyAndPastePythonCode/main/defaultSettings.json', 'settings.json')

    with open("copyFiles/tkWindowNoContent.txt", "w") as file:
        file.write("")
        downloadFile('https://raw.githubusercontent.com/ToMacMa/CopyAndPastePythonCode/main/copyFiles/tkWindowNoContent.txt', './copyFiles/tkWindowNoContent.txt')

    with open("copyFiles/tkWindowWithBtn.txt", "w") as file:
        file.write("")
        downloadFile('https://raw.githubusercontent.com/ToMacMa/CopyAndPastePythonCode/main/copyFiles/tkWindowWithBtn.txt', './copyFiles/tkWindowWithBtn.txt')
    
    with open("copyFiles/tkWindowWithLabel.txt", "w") as file:
        file.write("")
        downloadFile('https://raw.githubusercontent.com/ToMacMa/CopyAndPastePythonCode/main/copyFiles/tkWindowWithLabel.txt', './copyFiles/tkWindowWithLabel.txt')

    with open("copyFiles/reDownloadFile.txt", "w") as file:
        file.write("")
        downloadFile('https://raw.githubusercontent.com/ToMacMa/CopyAndPastePythonCode/main/copyFiles/tkWindowWithLabel.txt', './copyFiles/reDownloadFile.txt')

    print("Downloaded/Updated copyFiles folder and it's children!")

if 1 == 1:
    downloads()


try:
    import main
except:
    print("idk, this is not meant to happen")

exec("""
YN = str(input('Do you wanna update setup.py ? Y or N')); 
if YN == 'Y': 
    with open('setup.py', 'w') as file: 
        file.write(''); 
        downloadFile('https://raw.githubusercontent.com/ToMacMa/CopyAndPastePythonCode/main/setup.py', 'setup.py');

""")

main.StartWindow("Main window")
