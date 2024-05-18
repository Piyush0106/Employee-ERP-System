from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect
from PIL import Image,ImageTk
from customtkinter import ctk_tk
from adminlogin import adminLogin
from attendance import attendance
from employeelogin import employeelogin
from datetime import datetime

class mainwindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main Window")
        self.root.state("zoomed")
        self.frame=Frame(self.root)
        button_style = {
            "font": ("Helvetica", 14,"bold"),
            "bg": "#FF7F66",
            "fg": "#FFF6E5",
            "activebackground": "#AFCC2F",
            "activeforeground": "white",
            "relief": "raised",
            "borderwidth": 0,
            "highlightthickness": 0

        }


        img=Image.open("images/Mainwindow.jpg")
        width=int(self.root.winfo_screenwidth())
        height=int(self.root.winfo_screenheight())
        print(width,height)
        img=img.resize((width,height))
        bg=ImageTk.PhotoImage(img)
        c=Canvas(self.root,width=width,height=height)
        c.pack(fill='both',expand=True)
        c.create_image(0,0,image=bg,anchor='nw')

        # c.create_text(690 + 10, 35 + 20, text="Employee ERP System", font=("Arial", 34, "bold"), fill="white")
        self.clock_label = Label(self.root, text="", font=("Arial", 20,"bold"), bg="#6BBFBF", fg="white")
        self.clock_label.pack(anchor='nw', padx=20, pady=20)
        x_window = c.create_window(20, 20, anchor="nw", window=self.clock_label)

        self.day_label = Label(self.root, text="", font=("Arial", 20,"bold"), bg="#6BBFBF", fg="white")
        self.day_label.pack(anchor='nw', padx=20, pady=30)
        x_window = c.create_window(20, 80, anchor="nw", window=self.day_label)

        self.update_clock()  # Update clock initially
        self.update_day()  # Update day initially
        c.create_text(690 + 13, 35 + 43, text="Employee ERP System", font=("Arial", 44, "bold"), fill="#6BBFBF")
        c.create_text(690+10, 35+40, text="Employee ERP System", font=("Arial", 44, "bold"), fill="#208C81")

        self.adLogBtn = Button(self.root, text="Admin Log In", width=15, height=2, command=lambda: adminLogin(),**button_style)
        a_window=c.create_window(200,150,anchor="nw",window=self.adLogBtn)
        self.epLogBtn = Button(self.root, text="Employee Log In", width=15, height=2, command=lambda: employeelogin(),**button_style)
        e_window = c.create_window(600, 150, anchor="nw", window=self.epLogBtn)
        self.back = Button(self.root, text="Exit", width=15, height=2, command=lambda: self.root.destroy(),**button_style,)
        x_window = c.create_window(1000, 150, anchor="nw", window=self.back)
        # Camera Button
        self.cameraBtn = Button(self.root, text="Camera", width=15, height=2, command=lambda :attendance(),
                                **button_style)
        x_window = c.create_window(600, 390, anchor="nw", window=self.cameraBtn)



        self.root.mainloop()

        self.root.mainloop()

    def update_clock(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)  # Update every second

    def update_day(self):
        now = datetime.now()
        current_day = now.strftime("%A")
        self.day_label.config(text=current_day)
        self.root.after(86400000, self.update_day)  # Update every day (86400000 milliseconds)

if __name__ == "__main__":
    mainwindow = mainwindow()