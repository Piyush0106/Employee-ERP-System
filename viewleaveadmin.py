# from tkinter import *
# import tkinter.messagebox as msg
# import tkinter.ttk as ttk
# import pymysql
# from connection import connect
#
#
# class viewleaveadmin:
#     # def __init__(self):
#     #     self.root = Toplevel()
#     #     self.root.state("zoomed")
#     #
#     #     self.conn = connect()
#     #     self.cr = self.conn.cursor()
#     #
#     #     self.leavetable = ttk.Treeview(self.root, columns=('id', 'emp_id', 'date', 'remarks', 'status'))
#     #     self.leavetable.heading('id', text='ID')
#     #     self.leavetable.heading('emp_id', text='Employee ID')
#     #     self.leavetable.heading('date', text='Date')
#     #     self.leavetable.heading('remarks', text='Remarks')
#     #     self.leavetable.heading('status', text='Status')
#     #     self.leavetable['show'] = 'headings'
#     #     self.leavetable.column('id', width=50, anchor='center')
#     #     self.leavetable.column('emp_id', width=100, anchor='center')
#     #     self.leavetable.column('date', width=100, anchor='center')
#     #     self.leavetable.column('remarks', width=200, anchor='center')
#     #     self.leavetable.column('status', width=100, anchor='center')
#     #
#     #     self.style = ttk.Style()
#     #     self.style.configure("Treeview.Heading", font=('', 14))
#     #     self.style.configure("Treeview", font=('', 12))
#     #
#     #     self.leavetable.pack(expand=True, fill='both', padx=20, pady=20)
#     #
#     #     self.populate_leave_table()  # Fetch and display leave data
#     #
#     #     self.leavetable.bind("<Button-3>", self.show_popup_menu)
#     #
#     #     self.root.mainloop()
#
#     def __init__(self):
#         self.root = Toplevel()
#         self.root.state("zoomed")
#
#         self.conn = connect()
#         self.cr = self.conn.cursor()
#
#         self.leavetable = ttk.Treeview(self.root, columns=('id', 'emp_id', 'date', 'remarks', 'status'))
#         self.leavetable.heading('id', text='ID')
#         self.leavetable.heading('emp_id', text='Employee ID')
#         self.leavetable.heading('date', text='Date')
#         self.leavetable.heading('remarks', text='Remarks')
#         self.leavetable.heading('status', text='Status')
#         self.leavetable['show'] = 'headings'
#         self.leavetable.column('id', width=50, anchor='center')
#         self.leavetable.column('emp_id', width=100, anchor='center')
#         self.leavetable.column('date', width=100, anchor='center')
#         self.leavetable.column('remarks', width=200, anchor='center')
#         self.leavetable.column('status', width=100, anchor='center')
#
#         # Set background color for headings
#         self.leavetable.heading('id', background='#CCCCCC')
#         self.leavetable.heading('emp_id', background='#CCCCCC')
#         self.leavetable.heading('date', background='#CCCCCC')
#         self.leavetable.heading('remarks', background='#CCCCCC')
#         self.leavetable.heading('status', background='#CCCCCC')
#
#         # Set background color for alternate rows
#         for index, tag in enumerate(['oddrow', 'evenrow']):
#             self.leavetable.tag_configure(tag, background='#FFFFFF' if index % 2 == 0 else '#ECECEC')
#
#         self.leavetable.pack(expand=True, fill='both', padx=20, pady=20)
#
#         self.populate_leave_table()  # Fetch and display leave data
#
#         self.leavetable.bind("<Button-3>", self.show_popup_menu)
#
#         self.root.mainloop()
#
#     def populate_leave_table(self):
#         try:
#             self.cr.execute("SELECT * FROM leaves")
#             leaves_data = self.cr.fetchall()
#             for leave in leaves_data:
#                 # Replace status values
#                 leave_values = list(leave)
#                 if leave_values[4] == 'null':
#                     leave_values[4] = 'Not Approved'
#                 elif leave_values[4] == 'ok':
#                     leave_values[4] = 'Approved'
#                 elif leave_values[4] == 'reject':
#                     leave_values[4] = 'Rejected'
#
#                 self.leavetable.insert('', 'end', values=tuple(leave_values))
#         except pymysql.Error as e:
#             msg.showerror("Error", f"Error fetching leave data: {e}")
#
#     def update_status(self, leave_id, new_status):
#         try:
#             self.cr.execute("UPDATE leaves SET status=%s WHERE id=%s", (new_status, leave_id))
#             self.conn.commit()
#             msg.showinfo("Success", "Status updated successfully")
#             # Refresh table after updating status
#             self.leavetable.delete(*self.leavetable.get_children())
#             self.populate_leave_table()
#         except pymysql.Error as e:
#             msg.showerror("Error", f"Error updating status: {e}")
#
#     def show_popup_menu(self, event):
#         item = self.leavetable.identify_row(event.y)
#         if item:
#             popup_menu = Menu(self.root, tearoff=0)
#             popup_menu.add_command(label="Accept",
#                                    command=lambda: self.update_status(self.leavetable.item(item, 'values')[0], 'ok'))
#             popup_menu.add_command(label="Reject",
#                                    command=lambda: self.update_status(self.leavetable.item(item, 'values')[0],
#                                                                       'reject'))
#             popup_menu.post(event.x_root, event.y_root)
#
#
# if __name__ == "__main__":
#     viewleaveadmin()

from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect


class viewleaveadmin:
    def __init__(self):
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

        self.leavetable.bind("<Button-3>", self.show_popup_menu)

        self.root.mainloop()

    def populate_leave_table(self):
        try:
            self.cr.execute("SELECT * FROM leaves")
            leaves_data = self.cr.fetchall()
            for index, leave in enumerate(leaves_data):
                # Replace status values
                leave_values = list(leave)
                if leave_values[4] == 'null':
                    leave_values[4] = 'Not Approved'
                elif leave_values[4] == 'ok':
                    leave_values[4] = 'Approved'
                elif leave_values[4] == 'reject':
                    leave_values[4] = 'Rejected'

                # Insert row with appropriate tag for alternate row coloring
                self.leavetable.insert('', 'end', values=tuple(leave_values))

                # Set background color for alternate rows
                if index % 2 == 0:
                    self.leavetable.tag_configure('evenrow', background='#FFFFFF')
                else:
                    self.leavetable.tag_configure('oddrow', background='#ECECEC')
        except pymysql.Error as e:
            msg.showerror("Error", f"Error fetching leave data: {e}")

    def update_status(self, leave_id, new_status):
        try:
            self.cr.execute("UPDATE leaves SET status=%s WHERE id=%s", (new_status, leave_id))
            self.conn.commit()
            msg.showinfo("Success", "Status updated successfully")
            # Refresh table after updating status
            self.leavetable.delete(*self.leavetable.get_children())
            self.populate_leave_table()
        except pymysql.Error as e:
            msg.showerror("Error", f"Error updating status: {e}")

    def show_popup_menu(self, event):
        item = self.leavetable.identify_row(event.y)
        if item:
            popup_menu = Menu(self.root, tearoff=0)
            popup_menu.add_command(label="Accept",
                                   command=lambda: self.update_status(self.leavetable.item(item, 'values')[0], 'ok'))
            popup_menu.add_command(label="Reject",
                                   command=lambda: self.update_status(self.leavetable.item(item, 'values')[0],
                                                                      'reject'))
            popup_menu.post(event.x_root, event.y_root)


if __name__ == "__main__":
    viewleaveadmin()
