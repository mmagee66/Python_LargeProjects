from tkinter import *
import tkinter as tk
import os, sys
import sqlite3
import glob
import shutil

import moveFile_main




def getSource(self):
    dir = filedialog.askdirectory(initialdir="C:/")
    self.box_src.delete(0,END)
    self.box_src.insert(0,dir)
    self.fileArray = os.listdir(dir)
    print(self.fileArray)
   
   
                
def getDest(self):
    dir = filedialog.askdirectory(initialdir="C:/")
    self.box_dest.delete(0,END)
    self.box_dest.insert(0,dir)
    dest = dir
    self.dest1 ="{}{}".format(dest,'/')
    print(self.dest1)
 

def moveTxts(self):
    dest2 = self.dest1
    print(dest2)    
    conn = sqlite3.connect('db_moveText.db')
    with conn:
        cur = conn.cursor()
        for i in self.fileArray:
            if i.endswith('.txt'):
                filePath = os.path.join(dest2, i)
                print(filePath)
                shutil.move(i, dest2)
                cur.execute("INSERT INTO tbl_txtDocs(col_txtDoc) VALUES (?)", (i))
        conn.commit()
    conn.close()
                
           
                                    

def createDB(self):
    conn = sqlite3.connect('db_moveText.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_txtDocs( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_txtDoc TEXT, \
            col_timeStamp FLOAT \
            );" )
        conn.commit()
    conn.close()

        


           
   

    
        
    



        
          
        

     

if __name__ == "__main__":
    pass



    




    



    
    




    



