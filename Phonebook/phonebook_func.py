
import os
from tkinter import *
import tkinter as tk
import sqlite3

#import the other modules
#so as to have access to them
import phonebook_main
import phonebook_gui



def center_window(self, w, h): #pass in the tkinter frame (master) reference and the width and height
    #get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate the x and y coordinates to paint the app on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

#catch if the user clicks on the upper right corner X to make sure that they want to close the window
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)

#======================================================================================

def create_db(self):
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        # You must commit () to save changes and close the database connection
        conn.commit()
    conn.close()

def first_run(self):
    conn = sqlite.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_fullname, col_phone, col_email) VALUES (?,?,?,?)""", ('John', 'Doe', 'John Doe', '111-111-1111', 'jdoe@email.com'))
            conn.commit()
        conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur,count


# Select item in listbox
def onSelect(self,event):
    # calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname, col_lname, col_phone, col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            self.text_fname.delete(0,END)
            self.text_fname.insert(0,data[0])
            self.text_lname.delete(0,END)
            self.text_lname.insert(0,data[1])
            self.text_phone.delete(0,END)
            self.text_phone.insert(0,data[2])
            self.text_email.delete(0,END)
            self.text_email.insert(0,data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    # normalize the data to keep it consistant in the database
    var_fname = var_fname.strip() # this will remove any blank spaces before and after the user's entry
    var_lname = var_lname.strip() 
    var_fname = var_fname.title()# this will ensure that the first character in each word is capitalized
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname, var_lname)) # combine our normalized names into a fullname
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email: #will use this soon
        print("Incorrect email format!!!")
    if(len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0): #enforce user to prive all info
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cursor = conn.cursor()
            # Check the database for existance of the fullname, if so we will alert the user and disregard the request
            cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0: #if this is 0 then there is no existance of the fullname and we can add the entry
                print('chkName: {}'.format(chkName))
                cursor.execute("""INSERT INTO tbl_phonebook (col_fname, col_lname, col_phone, col_email) VALUES (?,?,?,?)""",(var_fname, var_lname, var_phone, var_email))
                self.lstList1.insert(END, var_fullname) #update listbox with new fullname
                onClear(self) #call the function to clear all of the textboxes
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database! Please dhose a different name.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing text error", "Please ensure that there is data in all four fields.")



def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.cuselction()) # Listbox's selected value
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in
        # the database...cannot delete the last reord or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with {}\nwill be permanentaly deleted from this database. \n \nProceed with deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_phonebook.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDelete(self) # call the function to clear all of the textboxes and the selected index of listbox
######                onRefresh(self) #update the listbox of the changes
                conn.commit()
            else:
                confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record before you can delete({}).".format(var_select, var_select))
        conn.close()

def onDeleted(self):
    # clear the txt in the textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
##     onRefresh(self) #update the listbox of changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    #clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)

def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_phonebook.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cursor.fetchone()[0]
        i = 0
        while i <count:
            cursor.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cursor.fetchone()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()


def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] #index of list selection
        var_value = self.lstList1.get(var_select) # list selections text value
    except:
        messagebox.showinfo("Missing Selection", "No name was selected from the list box. \nCancelling the update request.")
        return
    #The user will only be allowed to update infor for phone and email.
    #For name changes, the user will need to delete the entire record and start over
    var_phone = self.txt.phone.get().strip()
    var_email = self.txt.email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0): #ensure that there is data present
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cur = conn.cursor()
            #count the records to see if the users changes are already in the database
            #meaning there are no changes to update
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = conn.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            print(count2)
            if count == 0 or count2 == 0: #if proposed changes are not alreay in the database, then proceed
                response = messagebox.askokcancel("Update Request", "The following changes({}) and ({}) with be implemented for ({}). \n\nProceed with the update request?".format(var_phone, var_email, var_value))
                print(response)
                if response:
                    #conn = sqlite3.connect('db_phonebook.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}',col_email = '{1}' WHERE col_fullname = '{2}'""".format(var_phone, var_email, var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel Request","No changes have been made to ({})".format(var_value))
            else:
                messagebox.showinfo("No changes detected", "Both ({}) and ({}) \nalready exist in the database for this name \n\nYour update request has been canceled.".format(var_phone,var_email))
                        
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list \nThen edit the phone and email information.")
    onClear(self)
        



    





if __name__ == "__main__":
    pass
