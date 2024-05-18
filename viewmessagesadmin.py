# from tkinter import *
# import tkinter.messagebox as msg
# import tkinter.ttk as ttk
# import pymysql
# from connection import connect
#
#
# class viewmessagesadmit:
#     def __init__(self):
#         self.root = Tk()
#         self.root.state("zoomed")
#
#         self.conn = connect()
#         self.cr = self.conn.cursor()
#
#         self.messagestable = ttk.Treeview(self.root, columns=('id', 'title', 'description', 'date','time', 'emp_id_B'))
#         self.messagestable.heading('id', text='ID')
#         self.messagestable.heading('title', text='Title')
#         self.messagestable.heading('description', text='Description')
#         self.messagestable.heading('date', text='Date')
#         self.messagestable.heading('time', text='Time')
#         self.messagestable.heading('emp_id_B', text='Employee ID')
#         self.messagestable['show'] = 'headings'
#         # self.messagestable.column('id', width=50, anchor='center')
#         # self.messagestable.column('emp_id', width=100, anchor='center')
#         # self.messagestable.column('date', width=100, anchor='center')
#         # self.messagestable.column('remarks', width=200, anchor='center')
#         # self.messagestable.column('status', width=100, anchor='center')
#
#         self.messagestable.column('id',  width=50, anchor='center')
#         self.messagestable.column('title', width=100, anchor='center')
#         self.messagestable.column('description',  width=100, anchor='center')
#         self.messagestable.column('date', width=100, anchor='center')
#         self.messagestable.column('time',  width=100, anchor='center')
#         self.messagestable.column('emp_id_B', width=200, anchor='center')
#
#         self.style = ttk.Style()
#         self.style.configure("Treeview.Heading", font=('', 14))
#         self.style.configure("Treeview", font=('', 12))
#
#         self.messagestable.pack(expand=True, fill='both', padx=20, pady=20)
#
#         self.populate_messages_table()  # Fetch and display leave data
#
#         # self.messagestable.bind("<Button-3>", self.show_popup_menu)
#
#         self.root.mainloop()
#
#     def populate_messages_table(self):
#         try:
#             # Execute SQL query to fetch data from the messages table
#             self.cr.execute("SELECT * FROM messages")
#             messages_data = self.cr.fetchall()
#
#             # Clear existing data in the Treeview widget
#             self.messagestable.delete(*self.messagestable.get_children())
#
#             # Populate the Treeview widget with fetched data
#             for message in messages_data:
#                 # Reorder the values to match the column order
#                 id_, emp_id_B, date, time, title, description = message
#
#                 # Insert the reordered data into the Treeview widget
#                 self.messagestable.insert('', 'end', values=(id_, emp_id_B, date, time, title, description))
#
#         except pymysql.Error as e:
#             msg.showerror("Error", f"Error fetching messages data: {e}")
#
#     # def update_status(self, leave_id, new_status):
#     #     try:
#     #         self.cr.execute("UPDATE leaves SET status=%s WHERE id=%s", (new_status, leave_id))
#     #         self.conn.commit()
#     #         msg.showinfo("Success", "Status updated successfully")
#     #         # Refresh table after updating status
#     #         self.leavetable.delete(*self.leavetable.get_children())
#     #         self.populate_leave_table()
#     #     except pymysql.Error as e:
#     #         msg.showerror("Error", f"Error updating status: {e}")
#
#     # def show_popup_menu(self, event):
#     #     item = self.leavetable.identify_row(event.y)
#     #     if item:
#     #         popup_menu = Menu(self.root, tearoff=0)
#     #         popup_menu.add_command(label="Accept",
#     #                                command=lambda: self.update_status(self.leavetable.item(item, 'values')[0], 'ok'))
#     #         popup_menu.add_command(label="Reject",
#     #                                command=lambda: self.update_status(self.leavetable.item(item, 'values')[0],
#     #                                                                   'reject'))
#     #         popup_menu.post(event.x_root, event.y_root)
#
#
# if __name__ == "__main__":
#     viewmessagesadmit()
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import pymysql
from connection import connect


class viewmessagesadmit:
    def __init__(self):
        self.root = Tk()
        self.root.state("zoomed")

        self.conn = connect()
        self.cr = self.conn.cursor()
        self.mainLabel = Label(self.root, text="Messages", font=('', 28, 'bold'))
        self.mainLabel.pack()

        self.messagestable = ttk.Treeview(self.root, columns=('id', 'title', 'description', 'date', 'time', 'emp_id_B'))
        self.messagestable.heading('id', text='ID')
        self.messagestable.heading('title', text='Title')
        self.messagestable.heading('description', text='Description')
        self.messagestable.heading('date', text='Date')
        self.messagestable.heading('time', text='Time')
        self.messagestable.heading('emp_id_B', text='Employee ID')
        self.messagestable['show'] = 'headings'

        self.messagestable.column('id', width=50, anchor='center')
        self.messagestable.column('title', width=200, anchor='center')
        self.messagestable.column('description', width=300, anchor='center')
        self.messagestable.column('date', width=100, anchor='center')
        self.messagestable.column('time', width=100, anchor='center')
        self.messagestable.column('emp_id_B', width=100, anchor='center')

        self.messagestable.pack(expand=True, fill='both', padx=20, pady=20)

        self.populate_messages_table()

        self.root.mainloop()

    # def populate_messages_table(self):
    #     try:
    #         self.cr.execute("SELECT * FROM messages")
    #         messages_data = self.cr.fetchall()
    #
    #         for message in messages_data:
    #             (id_, title, description, date, time, emp_id_B) = message
    #             self.messagestable.insert('', 'end', values=(id_, title, description, date, time, emp_id_B))
    #
    #         # Configure alternate row colors
    #         for index, _ in enumerate(messages_data):
    #             if index % 2 == 0:
    #                 self.messagestable.tag_configure('evenrow', background='#ECECEC')
    #             else:
    #                 self.messagestable.tag_configure('oddrow', background='#FFFFFF')
    #
    #     except pymysql.Error as e:
    #         msg.showerror("Error", f"Error fetching messages data: {e}")

    def populate_messages_table(self):
        try:
            self.cr.execute("SELECT * FROM messages ORDER BY date DESC, time DESC")
            messages_data = self.cr.fetchall()

            for message in messages_data:
                (id_, title, description, date, time, emp_id_B) = message
                self.messagestable.insert('', 'end', values=(id_, title, description, date, time, emp_id_B))

            # Configure alternate row colors
            for index, _ in enumerate(messages_data):
                if index % 2 == 0:
                    self.messagestable.tag_configure('evenrow', background='#ECECEC')
                else:
                    self.messagestable.tag_configure('oddrow', background='#FFFFFF')

        except pymysql.Error as e:
            msg.showerror("Error", f"Error fetching messages data: {e}")


if __name__ == "__main__":
    viewmessagesadmit()
