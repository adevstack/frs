from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
from attendance import Attendance
from student import Student
import os
from traindata import Traindata
from face_recognizer import Recognizer
from developer import Developer
from helpdesk import Helpdesk


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x710+0+0")  
        self.root.title("Face Recognition System")

        # 1st image
        img1 = Image.open(r"C:\Users\Aman\Desktop\FRs\img\logo1.jpg")
        img1 = img1.resize((350, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0, y=0, width=350, height=130)

        # 2nd image
        img2 = Image.open(r"C:\Users\Aman\Desktop\FRs\img\logo1.jpg")
        img2 = img2.resize((350, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=350, y=0, width=350, height=135)

        # 3rd image
        img3 = Image.open(r"C:\Users\Aman\Desktop\FRs\img\logo.png")
        img3 = img3.resize((350, 130), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=500, y=0, width=350, height=135)

        # 4th image
        img4 = Image.open(r"C:\Users\Aman\Desktop\FRs\img\logo1.jpg")
        img4 = img4.resize((350, 130), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        f_lbl4 = Label(self.root, image=self.photoimg4)
        f_lbl4.place(x=840, y=0, width=350, height=135)
        
        # 5th image
        img14 = Image.open(r"C:\Users\Aman\Desktop\FRs\img\logo1.jpg")
        img14 = img14.resize((350, 130), Image.Resampling.LANCZOS)
        self.photoimg14 = ImageTk.PhotoImage(img14)

        f_lbl4 = Label(self.root, image=self.photoimg4)
        f_lbl4.place(x=1050, y=0, width=350, height=135)

        # bg image
        img5 = Image.open(r"C:\Users\Aman\Desktop\FRs\img\bg2.jpg")
        img5 = img5.resize((1360,710), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        bg_img = Label(self.root, image=self.photoimg5) 
        bg_img.place(x=0, y=130, width=1360, height=710)

        title_lbl = Label(bg_img,text="FACE RECOGNITION SYSTEM",font=("times new roman",15,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0, y=0, width=1360, height=45)

        #student button1
        img6=Image.open(r"C:\Users\Aman\Desktop\FRs\img\student.png")
        img6=img6.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img, image=self.photoimg6,command=self.student_details,cursor="hand2")
        b1.place(x=60, y=70, width=150, height=150)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="purple",fg="orange")
        b1_1.place(x=60, y=190, width=150, height=40)

        #Face Recognizer2
        img7=Image.open(r"C:\Users\Aman\Desktop\FRs\img\fre.jpg")
        img7=img7.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img, image=self.photoimg7,cursor="hand2",command=self.face_data)
        b1.place(x=230, y=70, width=150, height=150)

        b1_1=Button(bg_img,text="Face Recognizer", cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="purple",fg="orange")
        b1_1.place(x=230, y=190, width=150, height=40)

        #Attendance3
        img8=Image.open(r"C:\Users\Aman\Desktop\FRs\img\attendance.png")
        img8=img8.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img, image=self.photoimg8,cursor="hand2",command=self.attendance_data)
        b1.place(x=400, y=70, width=150, height=150)

        b1_1=Button(bg_img,text="Attendance", cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="purple",fg="orange")
        b1_1.place(x=400, y=190, width=150, height=40)

        #Help Desk4
        img9=Image.open(r"C:\Users\Aman\Desktop\FRs\img\helpdesk.png")
        img9=img9.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img, image=self.photoimg9,cursor="hand2",command=self.helpdesk_data)
        b1.place(x=570, y=70, width=150, height=150)

        b1_1=Button(bg_img,text="Help Desk", cursor="hand2",command=self.helpdesk_data,font=("times new roman",15,"bold"),bg="purple",fg="orange")
        b1_1.place(x=570, y=190, width=150, height=40)

        #Train Data5
        img10=Image.open(r"C:\Users\Aman\Desktop\FRs\img\train data.jfif")
        img10=img10.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img, image=self.photoimg10,cursor="hand2",command=self.train_data)
        b1.place(x=60, y=300, width=150, height=150)

        b1_1=Button(bg_img,text="Train Data", cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="purple",fg="orange")
        b1_1.place(x=60, y=420, width=150, height=40)

        #Photos6
        img11=Image.open(r"C:\Users\Aman\Desktop\FRs\img\photos.jpg")
        img11=img11.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img, image=self.photoimg11,cursor="hand2",command=self.open_img)
        b1.place(x=230, y=300, width=150, height=150)

        b1_1=Button(bg_img,text="Photos", cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="purple",fg="orange")
        b1_1.place(x=230, y=415, width=150, height=40)

        #Developer7
        img12=Image.open(r"C:\Users\Aman\Desktop\FRs\img\developer.jpg")
        img12=img12.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img, image=self.photoimg12,cursor="hand2",command=self.developer_data)
        b1.place(x=400, y=300, width=150, height=150)

        b1_1=Button(bg_img,text="Developer", cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="purple",fg="orange")
        b1_1.place(x=400, y=415, width=150, height=40)

        #exit8
        img13=Image.open(r"C:\Users\Aman\Desktop\FRs\img\exit.jpg")
        img13=img13.resize((200,180),Image.Resampling.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(img13)

        b1=Button(bg_img, image=self.photoimg13,cursor="hand2",command=self.iExit)
        b1.place(x=570, y=300, width=150, height=150)

        b1_1=Button(bg_img,text="Exit", cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="purple",fg="orange")
        b1_1.place(x=570, y=415, width=150, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Attendance Management System","Are you sure?",parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
  #--------------------------------------------------function-------------------------------------------------------------#
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Traindata(self.new_window)
    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Recognizer(self.new_window)
    
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpdesk_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpdesk(self.new_window)
    

    


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
