from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect

class viewleaveemployee:
    def __init__(self, employee_id):
        self.employee_id = employee_id
        # Other initialization code...
        self.root = Toplevel()
        self.root.state("zoomed")

        self.conn = connect()
        self.cr = self.conn.cursor()

        self.mainLabel = Label(self.root, text="Leaves", font=('', 28, 'bold'))
        self.mainLabel.pack()

        self.leavetable = ttk.Treeview(self.root, columns=('id', 'emp_id', 'date', 'remarks', 'status'))
        self.leavetable.heading('id', text='Serial Number')
        self.leavetable.heading('emp_id', text='Employee ID')
        self.leavetable.heading('date', text='Date')
        self.leavetable.heading('remarks', text='Remarks')
        self.leavetable.heading('status', text='Status')
        self.leavetable['show'] = 'headings'
        self.leavetable.column('id', width=50, anchor='center')
        self.leavetable.column('emp_id', width=100, anchor='center')
        self.leavetable.column('date', width=100, anchor='center')
        self.leavetable.column('remarks', width=200, anchor='center')
        self.leavetable.column('status', width=100, anchor='center')

        self.leavetable.pack(expand=True, fill='both', padx=20, pady=20)

        self.populate_leave_table()  # Fetch and display leave data



        self.root.mainloop()
    def populate_leave_table(self):
        try:
            employee_id = self.employee_id  # Extracting employee ID from employeedetails

            # Execute SQL query to fetch data from the leaves table for the specific employee
            self.cr.execute("SELECT * FROM leaves WHERE emp_id = %s", (employee_id,))
            leaves_data = self.cr.fetchall()

            # Clear existing data in the Treeview widget
            for row in self.leavetable.get_children():
                self.leavetable.delete(row)

            # Populate the Treeview widget with fetched data
            for leave in leaves_data:
                # Replace status values
                leave_values = list(leave)
                if leave_values[4] == 'null':
                    leave_values[4] = 'Not Approved'
                elif leave_values[4] == 'ok':
                    leave_values[4] = 'Approved'
                elif leave_values[4] == 'reject':
                    leave_values[4] = 'Rejected'

                # Insert the leave data into the Treeview widget
                self.leavetable.insert('', 'end', values=tuple(leave_values))

        except pymysql.Error as e:
            msg.showerror("Error", f"Error fetching leave data: {e}")


if __name__ == "__main__":
    employee_id = 12345  # Replace with the actual employee ID
    viewleaveemployee_instance = viewleaveemployee(employee_id)


