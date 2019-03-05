from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os, sys

import moveFile_func





class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__ (self)
        

        self.master = master
        self.master.title("Move files")
        self.master.geometry("800x400")
        
        self.box_src = Entry(root, width="50")
        self.box_src.grid(row=2, column=1)
        
        self.btn_src = Button(root, text="Source Folder", command=lambda: moveFile_func.getSource(self))
        self.btn_src.grid(row=2, column=2)

        self.box_dest = Entry(root, width="50")
        self.box_dest.grid(row=2, column=4)
        
        self.btn_dest = Button(root, text="Destination", command=lambda: moveFile_func.getDest(self))
        self.btn_dest.grid(row=2, column=5)

        self.btn_move = Button(root, text="Move text files to new location", command=lambda: moveFile_func.moveTxts(self))
        self.btn_move.grid(row=4, column=1, sticky=W)

        

        

        
          
        

     

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
