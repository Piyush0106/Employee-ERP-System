# from tkinter import *
# import tkinter.messagebox as msg
# import tkinter.ttk as ttk
# from connection import connect
# from changeemployeepassword import changePassword
# from leave import LeaveApplication
# from viewleaveemployee import viewleaveemployee
# from messages import messages
# from attendance import attendance
# class employeedashboard:
#     def __init__(self,employeedetails):
#
#         self.employeedetails = employeedetails
#         print(employeedetails)
#         self.root = Tk()
#         self.root.state("zoomed")
#         self.root.title("Welcome to Employee Dashboard")
#         self.font = ("Arial", 14)
#
#         self.mainMenu = Menu(self.root)
#         self.root.configure(menu=self.mainMenu)
#
#         # self.profileSubMenu = Menu(self.mainMenu, tearoff=0)
#         # self.mainMenu.add_cascade(label="Profile", menu=self.profileSubMenu)
#         self.mainMenu.add_cascade(label="Change Password", command=lambda: changePassword(employeedetails[1]))
#         self.mainMenu.add_cascade(label="Leave Application", command=lambda: LeaveApplication(employeedetails[0]))
#         self.mainMenu.add_cascade(label="View Leaves", command=lambda: viewleaveemployee(employeedetails[0]))
#         self.mainMenu.add_cascade(label="Send Message", command=lambda: messages(employeedetails[0]))
#         # self.mainMenu.add_cascade(label="Attendance", command=lambda: attendance(employeedetails[0]))
#         self.mainMenu.add_cascade(label="Logout", command=lambda: self.root.destroy())
#
#
#         self.mainLabel = Label(self.root, text=f"Welcome {self.employeedetails[2]} to your dashboard",
#                                font=('', 28, 'bold'))
#         self.mainLabel.pack(pady=20)
#
#         self.root.mainloop()
#
#
# if __name__ == "__main__":
#     employee = employeedashboard(employeedetails=(1, 'Jatin', 'fwe', 'j@gmail.com','9876543210', 'fdgcbc', 'Computer ', 'Computer Science', 'tyu','0000'))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect
from changeemployeepassword import changePassword
from leave import LeaveApplication
from viewleaveemployee import viewleaveemployee
from messages import messages
from attendance import attendance
from PIL import Image, ImageTk
from datetime import datetime

class employeedashboard:
    def __init__(self, employeedetails):
        self.employeedetails = employeedetails

        self.root = Toplevel()
        self.root.state("zoomed")
        self.root.title("Welcome to Employee Dashboard")
        self.font = ("Arial", 14)

        # self.mainLabel = Label(self.root, text=f"Welcome {self.employeedetails[2]} to your dashboard",
        #                        font=('', 28, 'bold'))
        # self.mainLabel.pack(pady=20)
        button_style = {
            "font": ("Helvetica", 14, "bold"),
            "bg": "#FF7F66",
            "fg": "#FFF6E5",
            "activebackground": "#AFCC2F",
            "activeforeground": "white",
            "relief": "raised",
            "borderwidth": 0,
            "highlightthickness": 0

        }

        # Load background image
        img = Image.open("images/Main_C.jpg")
        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())
        print(width, height)
        img = img.resize((width, height))
        bg = ImageTk.PhotoImage(img)
        c = Canvas(self.root, width=width, height=height)
        c.pack(fill='both', expand=True)
        c.create_image(0, 0, image=bg, anchor='nw')

        # # Create label for background image
        # bg_label = Label(self.root, image=bg_photo)
        # bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        c.create_text(690 + 13, 35 + 43, text=f"Welcome {self.employeedetails[2]} to your dashboard",font=("Arial", 44, "bold"), fill="#6BBFBF")
        c.create_text(690 + 10, 35 + 40, text=f"Welcome {self.employeedetails[2]} to your dashboard", font=("Arial", 44, "bold"), fill="#208C81")

        self.clock_label = Label(self.root, text="", font=("Arial", 20, "bold"), bg="#6BBFBF", fg="white")
        self.clock_label.pack(anchor='nw', padx=20, pady=20)

        self.day_label = Label(self.root, text="", font=("Arial", 20, "bold"), bg="#6BBFBF", fg="white")
        self.day_label.pack(anchor='nw', padx=20, pady=30)

        self.update_clock()  # Update clock initially
        self.update_day()  # Update day initially

        # adLogBtn = Button(self.root, text="Admin Log In", width=15, height=2, command=lambda: adminLogin())
        # adLogBtn.place(x=200, y=150)
        #
        # epLogBtn = Button(self.root, text="Employee Log In", width=15, height=2, command=lambda: employeelogin())
        # epLogBtn.place(x=600, y=150)

        changePwdBtn = Button(self.root, text="Change Password", width=15, height=2,
                              command=lambda: changePassword(employeedetails[1]),**button_style)
        changePwdBtn.place(x=200, y=150)

        leaveAppBtn = Button(self.root, text="Leave Application", width=15, height=2,
                             command=lambda: LeaveApplication(employeedetails[0]),**button_style)
        leaveAppBtn.place(x=600, y=150)

        viewLeavesBtn = Button(self.root, text="View Leaves", width=15, height=2,
                               command=lambda: viewleaveemployee(employeedetails[0]),**button_style)
        viewLeavesBtn.place(x=1000, y=150)

        sendMessageBtn = Button(self.root, text="Send Message", width=15, height=2,
                                command=lambda: messages(employeedetails[0]),**button_style)
        sendMessageBtn.place(x=400, y=350)

        logoutBtn = Button(self.root, text="Logout", width=15, height=2, command=lambda: self.root.destroy(),**button_style)
        logoutBtn.place(x=800, y=350)

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
    employee = employeedashboard(employeedetails=(1, 'Jatin', 'fwe', 'j@gmail.com','9876543210', 'fdgcbc', 'Computer ', 'Computer Science', 'tyu','0000'))
