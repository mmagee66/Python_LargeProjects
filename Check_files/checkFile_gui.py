

import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600, 250))
        self.master.title('Check Files')
        self.master.config(bg='lightgray')

        self.varBrowse1 = StringVar()
        self.varBrowse2 = StringVar()

        self.btnBrowse1 = Button(self.master, text = 'Browse...', width=15, height=1)
        self.btnBrowse1.grid(row=1, column=0, padx=(40,10), pady=(80,10), sticky=SE)
        self.btnBrowse2 = Button(self.master, text = 'Browse...', width=15, height=1)
        self.btnBrowse2.grid(row=2, column=0, padx=(40,10), pady=(1,10), sticky=SE)
        self.btnCheck = Button(self.master, text = 'Check for files...', width=15, height=2)
        self.btnCheck.grid(row=3, column=0, padx=(40,10), pady=(1,10), sticky=SE)
        self.btnClose = Button(self.master, text = 'Close Program', width=15, height=2)
        self.btnClose.grid(row=3, column=8, padx=(40,0), pady=(1,10), sticky=SE)

        self.txtBrowse1 = Entry(self.master,text=self.varBrowse1, font=('Helvetica', 16), fg='black', bg='white')
        self.txtBrowse1.grid(row=1, column=2, columnspan= 7, padx=(40,0), pady=(80,10))
        self.txtBrowse2 = Entry(self.master,text=self.varBrowse2, font=('Helvetica', 16), fg='black', bg='white')
        self.txtBrowse2.grid(row=2, column=2, columnspan= 7, padx=(40,0), pady=(1,10))







if __name__ =="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
