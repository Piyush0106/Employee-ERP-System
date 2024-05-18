from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect
import pymysql
class AddCategory:
    def __init__(self):
        self.root=Tk()
        self.root.title("Add Category")
        self.conn=connect()
        self.cr=self.conn.cursor()
        self.ml=Label(self.root,text="Add Category",font=('',36,'bold'),anchor='center')
        self.ml.pack(pady=20,padx=20)
        self.form = Frame(self.root)
        self.form.pack(pady=20,padx=20)

        self.l2=Label(self.form,text="Enter Name",font=('',16,'bold'))
        self.l2.grid(row=1,column=0,pady=10,padx=10)
        self.t2=Entry(self.form,font=('',16,'bold'))
        self.t2.grid(row=1,column=1,pady=10,padx=10)
        self.l3=Label(self.form,text="Description",font=('',16,'bold'))
        self.l3.grid(row=2,column=0,pady=10,padx=10)
        self.t3=Entry(self.form,font=('',16,'bold'))
        self.t3.grid(row=2,column=1,pady=10,padx=10)
        self.b1=Button(self.root,text='ADD',font=('',16,'bold'),width=20,command=self.addCategory)
        self.b1.pack(pady=20,padx=20)

        self.root.mainloop()
    def addCategory(self):
        if self.t2.get() and self.t3.get():
            q = "INSERT INTO category VALUES (%s, %s)"
            values = (self.t2.get(), self.t3.get())

            self.cr.execute(q, values)
            self.conn.commit()
            msg.showinfo("Success", "Category Added")
        else:
            msg.showerror("Error", "Please fill in all fields.")
if __name__ =="__main__":
    addCategory=AddCategory()