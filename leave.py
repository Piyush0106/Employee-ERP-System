from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from tkcalendar import DateEntry  # Import DateEntry widget from tkcalendar
import pymysql
from connection import connect


class LeaveApplication:
    def __init__(self,employee_id):
        self.employee_id=employee_id
        self.root = Toplevel()
        self.root.title("Leave Application")
        self.root['background'] = '#FFFFFF'

        self.font = ("Arial", 20, "bold")
        self.conn = connect()
        self.cr = self.conn.cursor()

        # Colors
        self.bg_color = "#FFFFFF"
        self.sec_color = "#ADD4D9"
        self.text_color = "#0D2601"
        self.button_color = "#6DDAF2"
        self.button_hover_color = "#F2B28D"

        self.mainLabel = Label(self.root, text="Leave Application", font=('Arial', 24, 'bold'), bg=self.bg_color, fg=self.text_color)
        self.mainLabel.pack(pady=20)

        self.leaveForm = Frame(self.root, bg=self.bg_color)
        self.leaveForm.pack()

        self.lb1 = Label(self.leaveForm, text="Employee ID", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb1.grid(row=0, column=0, pady=10, padx=20)

        self.t1 = Entry(self.leaveForm, font=self.font, width=30)
        self.t1.grid(row=0, column=1, pady=10, padx=20)
        self.t1.insert(END,self.employee_id)
        self.t1.configure(state='readonly')

        self.lb2 = Label(self.leaveForm, text="Date", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb2.grid(row=1, column=0, pady=10, padx=20)

        # Replace Entry with DateEntry for calendar date selection
        self.t2 = DateEntry(self.leaveForm, font=self.font, width=30, background='darkblue', foreground='white',
                            borderwidth=2, date_pattern='Y-m-d')
        self.t2.grid(row=1, column=1, pady=10, padx=20)

        self.lb3 = Label(self.leaveForm, text="Remarks", font=self.font, bg=self.bg_color, fg=self.text_color)
        self.lb3.grid(row=2, column=0, pady=10, padx=20)
        # Replace Entry with Text for larger text box
        self.t3 = Text(self.leaveForm, font=self.font, width=30, height=5)
        self.t3.grid(row=2, column=1, pady=10, padx=20)

        self.submitButton = Button(self.root, text="Submit", width=15, font=self.font, command=self.submitLeave, bg=self.button_color, fg="white", activebackground=self.button_hover_color, activeforeground="white")
        self.submitButton.pack(pady=20)

        # Bind hover effects to the submit button
        self.submitButton.bind("<Enter>", self.on_enter)
        self.submitButton.bind("<Leave>", self.on_leave)

        self.root.mainloop()


    def submitLeave(self):
        emp_id = self.t1.get()
        date = self.t2.get()
        remarks = self.t3.get("1.0", "end-1c")  # Get text from Text widget

        try:
            # Fetch the employee's name based on the provided emp_id
            sql_fetch_name = "SELECT name FROM employee WHERE employee_id = %s"
            self.cr.execute(sql_fetch_name, (emp_id,))
            name_result = self.cr.fetchone()
            if name_result:
                name = name_result[0]
            else:
                name = "Unknown"  # Set a default name if emp_id not found

            # Insert leave information into the database table
            sql_insert_leave = "INSERT INTO leaves (emp_id, date, remarks, status, name) VALUES (%s, %s, %s, 'null', %s)"
            self.cr.execute(sql_insert_leave, (emp_id, date, remarks, name))
            self.conn.commit()
            msg.showinfo("Leave Application", "Leave submitted successfully.")
        except Exception as e:
            self.conn.rollback()
            msg.showerror("Error", f"An error occurred: {e}")
    def on_enter(self, event):
        # Change background color when mouse enters button
        self.submitButton.config(bg=self.button_hover_color)

    def on_leave(self, event):
        # Restore background color when mouse leaves button
        self.submitButton.config(bg=self.button_color)

if __name__ == "__main__":
    leave_application = LeaveApplication()


# from tkinter import *
# import tkinter.messagebox as msg
# import tkinter.ttk as ttk
# import pymysql
# from connection import connect
# # from admindashboard import adminDashboard
#
#
# class leave:
#     def __init__(self):
#         self.root = Tk()
#         self.root.geometry("800x600")
#         self.root.title("Admin Login")
#         self.root['background']='#3E454C'
#
#         self.font=("Arial", 20, "bold")
#         self.conn = connect()
#         self.cr = self.conn.cursor()
#
#         # Colors
#         self.bg_color = "#3E454C"
#         self.text_color = "#FFF6E5"
#         self.button_color = "#FF7F66"
#         self.button_hover_color = "#7ECEFD"
#
#         self.mainLabel = Label(self.root, text="Leave", font=('Arial', 24, 'bold'), bg=self.bg_color, fg=self.text_color)
#         self.mainLabel.pack(pady=20)
#
#         self.leaveForm = Frame(self.root, bg=self.bg_color)
#         self.leaveForm.pack()
#
#         self.lb1 = Label(self.leaveForm, text="Employee ID", font=self.font, bg=self.bg_color, fg=self.text_color)
#         self.lb1.grid(row=0, column=0, pady=10, padx=20)
#
#         self.t1 = Entry(self.leaveForm, font=self.font, width=30)
#         self.t1.grid(row=0, column=1, pady=10, padx=20)
#
#         self.lb2 = Label(self.leaveForm, text="Date", font=self.font, bg=self.bg_color, fg=self.text_color)
#         self.lb2.grid(row=1, column=0, pady=10, padx=20)
#
#         self.t2 = Entry(self.leaveForm, font=self.font, width=30)
#         self.t2.grid(row=1, column=1, pady=10, padx=20)
#
#         self.lb3 = Label(self.leaveForm, text="Remarks", font=self.font, bg=self.bg_color, fg=self.text_color)
#         self.lb3.grid(row=2, column=0, pady=10, padx=20)
#         # Replace Entry with Text for larger text box
#         self.t3 = Text(self.leaveForm, font=self.font, width=30, height=5)
#         self.t3.grid(row=2, column=1, pady=10, padx=20)
#
#         self.submitButton = Button(self.root, text="Submit", width=15, font=self.font, command=self.submitLeave, bg=self.button_color, fg="white", activebackground=self.button_hover_color, activeforeground="white")
#         self.submitButton.pack(pady=20)
#
#         # Bind hover effects to the login button
#         self.submitButton.bind("<Enter>", self.on_enter)
#         self.submitButton.bind("<Leave>", self.on_leave)
#
#         self.root.mainloop()
#
#     def submitLeave(self):
#         email = self.t1.get()
#         password = self.t2.get()
#
#         q = f"SELECT id,email,name,mobile,role  FROM admin WHERE email = '{email}' and password = '{password}'"
#         self.cr.execute(q)
#         result = self.cr.fetchone()
#         if result is None:
#             msg.showwarning("Not Found", "Enter a valid e-mail or password")
#         else:
#             print(result)
#             msg.showinfo("Found", "Login Successful")
#             self.root.destroy()
#             # adminDashboard(adminDetails=result)
#
#     def on_enter(self, event):
#         # Change background color when mouse enters button
#         self.submitButton.config(bg=self.button_hover_color)
#
#     def on_leave(self, event):
#         # Restore background color when mouse leaves button
#         self.submitButton.config(bg=self.button_color)
#
#
# if __name__ == "__main__":
#     leave = leave()
#
#
#
