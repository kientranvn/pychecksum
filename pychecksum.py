#Author     Date            Version     Descriptions
#KTR        Dec 16 2019     1.0         Init document
#This script will be help you for get the md5 string. You just select an file.

import subprocess
import os
import tkinter
from tkinter import *
from tkinter import filedialog

import hashlib

#GUI
class GUI(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root)
        self.root = root
        self.initMenu()
        self.initGui()

    def initMenu(self):
        self.filepaths = []
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
        
        self.MD5 = tkinter.StringVar()

        self.PathValue = tkinter.StringVar()
        self.statusValue = StringVar()
        self.statusValue.set('Please select your files')
        self.MD5 = tkinter.StringVar()

        self.InputGroupLabel = Label(self.inputFrame, text = "-----> Input files <-----", width = 60).grid(row = 1, column = 1, columnspan = 2)
        self.ChooserButton = Button(self.inputFrame, text='Input', command=self.OpenFile).grid(row=2, column=1)
        self.PathEntry = Entry(self.inputFrame, width=60, bd=2, textvariable=self.PathValue).grid(row=2, column=2)
        self.Md5Label = Label(self.inputFrame, text = 'MD5').grid(row = 3, column = 1)
        self.Md5Entry = Entry(self.inputFrame, width = 60, bd = 2, textvariable = self.MD5).grid(row = 3, column = 2)

        self.RunGroupLabel = Label(self.LeftBotLabelFrame, text='-----> Run Automation Scripts <-----', width = 60).grid(row=1, column=1, columnspan = 2)
        self.generateButton = Button(self.LeftBotLabelFrame, text='Generate', command=self.myGUI).grid(row=2, column=1, columnspan=2)
        self.statusLabel = Label(self.LeftBotLabelFrame, textvariable=self.statusValue).grid(row=3, column=1, columnspan=2)


    def OpenFile(self):
        file_path = tkinter.filedialog.askopenfilename(filetype = (("PDF", "*.pdf"), ("All files", "*.*")), parent=self,)
        self.file_paths = file_path
        self.PathValue.set(self.file_paths)

    
    # This functions will be used for get the Md5 string from file.
    def CheckMd5(self, inputFile):
        with open(inputFile, "rb") as f:
            file_hash = hashlib.md5()
            while chunk := f.read(8192):
                file_hash.update(chunk)

        return (file_hash.hexdigest())

    def setStatus(self, status):
        self.statusValue.set(status)

    def myGUI(self):
        if not (self.PathValue.get()):
            self.setStatus('Missing input file')
        else:
            self.setStatus('Get MD5...')
            file = self.file_paths
            #name = os.path.splitext(file)[0]
            #name = os.path.basename(name)
            self.MD5.set(self.CheckMd5(file))
            self.setStatus('Finished! Get your md5')
        
def runGUI():
    root = tkinter.Tk()
    runGUI = GUI(root)
    runGUI.pack()
    root.mainloop()

if __name__ == "__main__":
    runGUI()