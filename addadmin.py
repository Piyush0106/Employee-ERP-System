from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect

class addAdmin:
    def __init__(self):
        self.root=Tk()
        self.root.title("Add Admin")
        self.root.state("zoomed")

        self.conn=connect()
        self.cr= self.conn.cursor()

        self.mainLabel=Label(self.root,text="Add Admin",font=('',16,'bold'))
        self.mainLabel.pack(pady=10,padx=10)

        self.form=Frame(self.root)
        self.form.pack()


        self.l2 = Label(self.form, text="Enter Name", font=('', 12))
        self.l2.grid(row=1, column=0, padx=10, pady=10)
        self.t2 = Entry(self.form, font=('', 12), width=20)
        self.t2.grid(row=1, column=1, padx=10, pady=10)

        self.l3 = Label(self.form, text="Enter E-Mail", font=('', 12))
        self.l3.grid(row=2, column=0, padx=10, pady=10)
        self.t3 = Entry(self.form, font=('', 12), width=20)
        self.t3.grid(row=2, column=1, padx=10, pady=10)

        self.l4 = Label(self.form, text="Enter Mobile", font=('', 12))
        self.l4.grid(row=3, column=0, padx=10, pady=10)
        self.t4 = Entry(self.form, font=('', 12), width=20)
        self.t4.grid(row=3, column=1, padx=10, pady=10)

        self.l5 = Label(self.form, text="Enter Password", font=('', 12))
        self.l5.grid(row=4, column=0, padx=10, pady=10)
        self.t5 = Entry(self.form, font=('', 12), width=20,show='*')
        self.t5.grid(row=4, column=1, padx=10, pady=10)

        self.l1 = Label(self.form, text="Role", font=('', 12))
        self.l1.grid(row=5, column=0, padx=10, pady=10)
        self.c1=ttk.Combobox(self.form,values=['SuperAdmin','Admin'],state="readonly",width=25)
        self.c1.grid(row=5,column=1, padx=10, pady=10)

        self.b1=Button(self.root,text="ADD",width=20,command=self.addAdmin)
        self.b1.pack(pady=10,padx=10)
        self.root.mainloop()

    def addAdmin(self):
        email=self.t3.get()
        if self.t2.get()=='' and self.t3.get()=='' and self.t4.get()=='' and self.c1.get()=='' and self.t5.get()=='':
            msg.showwarning("Not Running","Enter all fields")

        else:
            if len(self.t4.get())==10 and self.t4.get().isdigit() :
                if '@' in email and '.' in email:
                    q=("insert into admin values(null,'"+self.t2.get()+"','"+self.t3.get()+"',"+self.t4.get()
                    +",'"+self.c1.get()+"','"+self.t5.get()+"')")
                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo("Success","Added Successfully")
                else:
                    msg.showwarning("warning","Invaild email")
            else:
                msg.showwarning("Not Running","Invalid Mobile Number")
if __name__=="__main__":

    addAdmin()
