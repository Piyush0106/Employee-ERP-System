from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import numpy as np
from PIL import Image, ImageTk
import cv2
from connection import connect
from datetime import datetime
import os
from mtcnn import MTCNN
from deepface import DeepFace
class attendance:
    def __init__(self):
        # self.employee_id = employee_id
        self.root = Toplevel()
        self.detector = MTCNN()
        self.root.title("Attendance")
        self.root['background'] = '#148BA6'


        self.font=("Arial", 12, "bold")
        self.conn = connect()
        self.cr = self.conn.cursor()

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

        # Colors
        self.bg_color = "#FFFFFF"
        self.sec_color = "#ADD4D9"
        self.text_color = "#0D2601"
        self.button_color = "#6DDAF2"
        self.button_hover_color = "#F2B28D"

        # Make window responsive
        self.root.pack_propagate(0)
        self.root.geometry("1000x700")
        self.root.minsize(200, 100)  # Set minimum window size

        # Frame for the form (left portion)
        self.left_frame = Frame(self.root, bg=self.sec_color, borderwidth=5, relief="flat")
        self.left_frame.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.9)

        # Frame for the video display (right portion)
        self.right_frame = Frame(self.root, bg=self.sec_color, borderwidth=5, relief="flat")
        self.right_frame.place(relx=0.55, rely=0.05, relwidth=0.4, relheight=0.9)

        # Placeholder labels for the form
        left_label = Label(self.left_frame, text="Employee Details",font=('Arial', 24, 'bold'), bg=self.sec_color, fg=self.text_color)
        left_label.pack(pady=10)

        # Employee Details Form
        self.employee_id_label = Label(self.left_frame, text="Employee ID:", bg=self.sec_color, fg=self.text_color, font=self.font)
        self.employee_id_label.pack(pady=5)

        self.employee_id_entry = Entry(self.left_frame, font=self.font)
        self.employee_id_entry.pack(pady=5)

        self.name_label = Label(self.left_frame, text="Name:", bg=self.sec_color, fg=self.text_color, font=self.font)
        self.name_label.pack(pady=5)

        self.name_entry = Entry(self.left_frame, font=self.font)
        self.name_entry.pack(pady=5)

        self.department_label = Label(self.left_frame, text="Department:", bg=self.sec_color, fg=self.text_color, font=self.font)
        self.department_label.pack(pady=5)

        self.department_entry = Entry(self.left_frame, font=self.font)
        self.department_entry.pack(pady=5)

        self.category_label = Label(self.left_frame, text="Category:", bg=self.sec_color, fg=self.text_color, font=self.font)
        self.category_label.pack(pady=5)

        self.category_entry = Entry(self.left_frame, font=self.font)
        self.category_entry.pack(pady=5)

        # Time and Date Fields
        self.time_label = Label(self.left_frame, text="Time:", bg=self.sec_color, fg=self.text_color, font=self.font)
        self.time_label.pack(pady=5)

        self.time_entry = Entry(self.left_frame, font=self.font)
        self.time_entry.pack(pady=5)

        self.date_label = Label(self.left_frame, text="Date:", bg=self.sec_color, fg=self.text_color, font=self.font)
        self.date_label.pack(pady=5)

        self.date_entry = Entry(self.left_frame, font=self.font)
        self.date_entry.pack(pady=5)

        self.btn = Button(self.left_frame, text="Capture",font=('Arial', 16, 'bold'), bg=self.button_color, fg="white", activebackground=self.button_hover_color, activeforeground="white",width=10, command=self.recFace)
        self.btn.pack(pady=20)
        # Bind hover effects to the login button
        self.btn.bind("<Enter>", self.on_enter)
        self.btn.bind("<Leave>", self.on_leave)





        # Fetch and display current date and time
        self.fetch_current_datetime()


        # Placeholder label for video display
        right_label = Label(self.right_frame, text="Video Display", bg=self.sec_color, fg=self.text_color, font=self.font)
        right_label.pack(pady=10)

        # Video display
        self.video_label = Label(self.right_frame)
        self.video_label.pack(expand=True)
        self.video_capture()  # Start video capture

        self.root.mainloop()

    # def recFace(self):
    #     images = os.listdir('employeeImage')
    #     try:
    #         # Detect faces in the input frame
    #         detections = self.detector.detect_faces(self.frame)
    #
    #         # Extract face embeddings from the input frame
    #         frame_embeddings = []
    #         for detection in detections:
    #             x, y, w, h = detection['box']
    #             face = self.frame[y:y+h, x:x+w]
    #             face_embedding = DeepFace.represent(face, model_name='Facenet')
    #             frame_embeddings.append(face_embedding)
    #
    #         # Convert lists to NumPy arrays
    #         frame_embeddings = np.array(frame_embeddings)
    #
    #         # Iterate over employee images and perform verification
    #         for i in images:
    #             employee_embedding = DeepFace.represent(f"employeeImage/{i}", model_name='Facenet')
    #             employee_embedding = np.array(employee_embedding)  # Convert list to NumPy array
    #             distances = [np.linalg.norm(frame_embedding - employee_embedding) for frame_embedding in frame_embeddings]
    #             min_distance = min(distances)
    #             if min_distance < 0.6:  # Adjust threshold as needed
    #                 self.image = i
    #                 return True  # Return True if a match is found
    #         return False  # Return False if no match is found
    #     except FileNotFoundError as e:
    #         print(f"File not found: {e.filename}")
    #     except Exception as e:
    #         print(f"An error occurred: {str(e)}")
    def on_enter(self, event):
        # Change background color when mouse enters button
        self.btn.config(bg=self.button_hover_color)

    def on_leave(self, event):
        # Restore background color when mouse leaves button
        self.btn.config(bg=self.button_color)
    def recFace(self):
        images = os.listdir('employeeImage')
        # try :
        for i in images:
            result = DeepFace.verify(img1_path=f"employeeImage/{i}",
                                     img2_path=self.frame,
                                     model_name="Facenet512"
                                     )
            if result['verified'] == True:
                self.image = i
                print(self.image)
                self.fetch_employee_data()
                break
            else:
                print("EMPLOYEE NOT REGISTERED")

    def video_capture(self):
        # OpenCV Video Capture
        self.video = cv2.VideoCapture(0)
        self.cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.update_video()

    def update_video(self):
        ret, self.frame = self.video.read()
        if ret:
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            faces = self.cascade.detectMultiScale(self.frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            for (x, y, w, h) in faces:
                cv2.rectangle(img=self.frame, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=5)
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.frame))
            self.video_label.configure(image=self.photo)
            self.video_label.image = self.photo  # Keep a reference to the PhotoImage object
        self.video_label.after(10, self.update_video)


    def fetch_current_datetime(self):
        # Get current date and time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%Y-%m-%d")

        # Display current date and time in the entry fields
        self.time_entry.insert(0, current_time)
        self.date_entry.insert(0, current_date)



    def fetch_employee_data(self):
        image_name = self.image

        # Check if image name is provided
        if not image_name:
            msg.showerror("Error", "Image name not provided.")
            return

        try:
            # Execute SQL query to fetch data based on image name
            query = f"SELECT * FROM employee WHERE image = '{image_name}'"
            self.cr.execute(query)
            employee_data = self.cr.fetchone()  # Fetch the first row

            # Check if employee with provided image name exists
            if not employee_data:
                msg.showerror("Error", "Employee not found.")
                return

            # Populate entry fields with fetched data
            self.employee_id_entry.delete(0, END)
            self.employee_id_entry.insert(0, str(employee_data[0]))  # Employee ID
            self.name_entry.delete(0, END)
            self.name_entry.insert(0, employee_data[1])  # Name
            self.department_entry.delete(0, END)
            self.department_entry.insert(0, employee_data[6])  # Department
            self.category_entry.delete(0, END)
            self.category_entry.insert(0, employee_data[7])  # Category

            # Get current date and time
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_date = now.strftime("%Y-%m-%d")

            # Send attendance data to the database
            self.send_attendance_data(employee_data[0], current_date, current_time)

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            msg.showerror("Error", "An error occurred while fetching employee data.")

    def send_attendance_data(self, employee_id, date, time):
        try:
            # Insert attendance data into the database
            query = f"INSERT INTO attendance (emp_id_A, date, time, type) VALUES ({employee_id}, '{date}', '{time}', 'Null')"
            self.cr.execute(query)
            self.conn.commit()
            msg.showinfo("Success", "Attendance recorded successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            msg.showerror("Error", "An error occurred while recording attendance.")




    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()
        if hasattr(self, 'video'):
            self.video.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    admin = attendance()

