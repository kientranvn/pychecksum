#Author     Date            Version     Descriptions
#KTR        Dec 16 2019     1.0         Init document

import subprocess
import os
import tkinter
from tkinter import *
from tkinter import filedialog

import hashlib


# This functions will be used for get the Md5 string from file.
def CheckMd5(inputFile):
    with open(inputFile, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    return (file_hash.hexdigest())


#GUI
class GUI(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root)
        self.root = root
        self.initMenu()
        self.initGui()

    def initMenu(self):
        self.filepath = ""
        self.root.title("Get Md5 with Python - Pychecksum | version 1.0")
        self.pack(fill=BOTH, expand=1)

        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        #File menu
        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)

         #Help menu
        helpMenu = Menu(menubar, tearoff=0)
        helpMenu.add_command(label="Help")
        helpMenu.add_command(label="About")
        menubar.add_cascade(label="Help", menu=helpMenu)

    def initGui(self):
        # Giao dien
        self.inputFrame = LabelFrame(self)
        self.optionFrame = LabelFrame(self)
        self.LeftBotLabelFrame = LabelFrame(self)
        self.RightBotLabelFrame = LabelFrame(self)

        self.inputFrame.grid(row=1, column=1, sticky = W)
        self.optionFrame.grid(row=1, column=2, sticky = W)
        self.LeftBotLabelFrame.grid(row=2, column=1, sticky = W)
        self.RightBotLabelFrame.grid(row=2, column=2, sticky = W)
        

        self.PathValue = tkinter.StringVar()
        self.statusValue = StringVar()
        self.statusValue.set('Please select your files')
        self.NameVar = tkinter.StringVar()

        self.InputGroupLabel = Label(self.inputFrame, text = "-----> Input files <-----", width = 60).grid(row = 1, column = 1, columnspan = 2)


        self.RunGroupLabel = Label(self.LeftBotLabelFrame, text='-----> Run Automation Scripts <-----', width = 60).grid(row=1, column=1, columnspan = 2)
        self.generateButton = Button(self.LeftBotLabelFrame, text='Generate', command=self.myGUI).grid(row=2, column=1, columnspan=2)
        self.statusLabel = Label(self.LeftBotLabelFrame, textvariable=self.statusValue).grid(row=3, column=1, columnspan=2)







    def OpenFile(self):
        file_path = tkinter.filedialog.askopenfilename(filetype = (("PDF", "*.pdf"), ("All files", "*.*")), parent=self,)
        self.file_path = file_path
        self.PathValue.set(self.file_path)

    def myGUI(self):
        print("Jueb")
        





def runGUI():
    root = tkinter.Tk()
    runGUI = GUI(root)
    runGUI.pack()
    root.mainloop()

if __name__ == "__main__":
    runGUI()