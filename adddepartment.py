from tkinter import *
import tkinter.messagebox as msg
from connection import connect
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class addDepartment:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Add Department")
        self.root.state("zoomed")
        self.font= ("Arial", 16,)
        self.root['background'] = '#FFFFFF'

        # Colors
        self.bg_color = "#FFFFFF"
        self.sec_color = "#ADD4D9"
        self.text_color = "#0D2601"
        self.button_color = "#6DDAF2"
        self.button_hover_color = "#F2B28D"

        self.conn=connect()
        self.cr = self.conn.cursor()

        # Load and resize image
        image = Image.open("images/Reports 2.jpg")  # Change to your image file path
        image = image.resize((280, 140))  # Resize image as per your requirement
        photo = ImageTk.PhotoImage(image)

        # Create label to display image
        self.image_label = Label(self.root, image=photo, bg=self.bg_color)
        self.image_label.image = photo  # Keep a reference to avoid garbage collection
        self.image_label.pack(side=TOP, fill=Y, padx=20, pady=20)  # Pack image label on the left side

        self.mainLabel = Label(self.root, text="Add Department", font=('Arial', 24, "bold"),bg=self.bg_color, fg=self.text_color)
        self.mainLabel.pack(pady=20)

        self.form = Frame(self.root,bg=self.bg_color)
        self.form.pack(pady=10)

        self.lb1 = Label(self.form, text=" Department Name : ",font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb1.grid(row=0, column=0, padx=20, pady= 20)
        self.t1 = Entry(self.form, width=35, font=self.font,bg=self.sec_color)
        self.t1.grid(row=0, column=1, padx=20)

        self.lb2 = Label(self.form, text=" Email : ", font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb2.grid(row=1, column=0, padx=20, pady=20)
        self.t2 = Entry(self.form, width=35, font=self.font,bg=self.sec_color)
        self.t2.grid(row=1, column=1, padx=20)

        self.lb3 = Label(self.form, text=" Phone No. : ", font=self.font,bg=self.bg_color, fg=self.text_color)
        self.lb3.grid(row=2, column=0, padx=20, pady=20)
        self.t3 = Entry(self.form, width=35, font=self.font,bg=self.sec_color)
        self.t3.grid(row=2, column=1, padx=20)

        # self.lb4 = Label(self.form, text=" HOD ID : ", font=self.font)
        # self.lb4.grid(row=3, column=0, padx=20, pady=20)
        # self.t4 = Entry(self.form, width=35, font=self.font)
        # self.t4.grid(row=3, column=1, padx=20)

        self.l1 = Label(self.form, text="HOD ID", font=self.font,bg=self.bg_color, fg=self.text_color)
        self.l1.grid(row=5, column=0, padx=20, pady=20)
        self.c1 = ttk.Combobox(self.form, values= self.fetchhod(), state="readonly", width=35)
        self.c1.grid(row=5, column=1, padx=20, pady=20)

        self.btn = Button(self.root, text="Add Department", font=self.font, command=self.addDepartment,bg=self.button_color, fg="white", activebackground=self.button_hover_color, activeforeground="white")
        self.btn.pack(pady=20)



        self.root.mainloop()


    def addDepartment(self):
        if self.t1.get()=='' or self.t2.get()=='' or self.t1.get()=='' or self.c1.get()=='' :
            msg.showwarning("Warning", "Please Enter all field")
        else:
            if len(self.t3.get())==10 and self.t3.get().isdigit():
                if '@' in self.t2.get() and '.' in self.t2.get():
                    q = ("insert into department values('"+ self.t1.get() + "','" + self.t2.get() + "'," + self.t3.get() +
                    ",'" + self.c1.get() + "')")

                    self.cr.execute(q)
                    self.conn.commit()
                    msg.showinfo("Success", "Department added successfully")
                else:
                    msg.showwarning("Warning", " Enter vaild Email")
            else:
                msg.showwarning("Warning", " Enter vaild Phone Number")

    def fetchhod(self):
        q=" select * from hod "
        self.cr.execute(q)
        result = self.cr.fetchall()
        list=[]
        for i in result :
            list.append(i[0])

        return list


if __name__ == '__main__':
    addDepartment()