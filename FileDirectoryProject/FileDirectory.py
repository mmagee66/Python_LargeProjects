


from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os, sys



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)
        

        def getDir():
            dir = filedialog.askdirectory(initialdir="C:/")
            self.user1.delete(0,END)
            self.user1.insert(0,dir)
            files = (file for file in os.listdir(dir)
                if os.path.isfile(os.path.join(dir, file)))
           

  
        self.master = master
        self.master.title("Find File")
        self.master.geometry("400x200")    
        self.user1 = Entry(root, width="50")
        self.user1.grid(row=2, column=2)
        self.browse = Button(root, text="Browse", command=getDir)
        self.browse.grid(row=2, column=3)
        

     


root = Tk()
App = ParentWindow(root)
root.mainloop()
