from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x710+0+0")  
        self.root.title("Face Recognition System")

        #_______________________________________________________#
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


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

        title_lbl = Label(text="FACE RECOGNITION SYSTEM",font=("times new roman",15,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0, y=200, width=1360, height=45)

        main_frame=Frame(bd=2,bg="white")
        main_frame.place(x=0,y=235,width=1500,height=650)

        # Left frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=45, y=10, width=600, height=490)

        # Image in the top of the left frame
        img_left = Image.open(r"img\atndns3.jpg")
        img_left = img_left.resize((700, 140), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=700, height=140)

        # Inner frame for the details
        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=145, width=595, height=330)

        # Labels and entry widgets for various attendance details

        # Left side labels and entries (first 4 fields)
        # Attendance ID
        AttendanceID_label = Label(left_inside_frame, text="Attendance_ID:", font=("times new roman", 12, "bold"), bg="white")
        AttendanceID_label.grid(row=0, column=0, sticky=W, padx=10, pady=5)

        AttendanceID_entry = ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20, font=("times new roman", 12, "bold"))
        AttendanceID_entry.grid(row=0, column=1, sticky=W, padx=10, pady=5)

        # Name
        Name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        Name_label.grid(row=1, column=0, sticky=W, padx=10, pady=5)

        Name_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_name,font=("times new roman", 12, "bold"))
        Name_entry.grid(row=1, column=1, sticky=W, padx=10, pady=5)

        # Department
        Department_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        Department_label.grid(row=2, column=0, sticky=W, padx=10, pady=5)

        Department_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_dep,font=("times new roman", 12, "bold"))
        Department_entry.grid(row=2, column=1, sticky=W, padx=10, pady=5)

        # Roll Number
        RollNumber_label = Label(left_inside_frame, text="Roll Number:", font=("times new roman", 12, "bold"), bg="white")
        RollNumber_label.grid(row=3, column=0, sticky=W, padx=10, pady=5)

        RollNumber_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_roll,font=("times new roman", 12, "bold"))
        RollNumber_entry.grid(row=3, column=1, sticky=W, padx=10, pady=5)

        # Right side labels and entries (last 3 fields)
        # Date      
        Date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        Date_label.grid(row=0, column=2, sticky=W, padx=5, pady=5)

        Date_entry = ttk.Entry(left_inside_frame, width=20,textvariable=self.var_atten_date,font=("times new roman", 12, "bold"))
        Date_entry.grid(row=0, column=3, sticky=W, padx=5, pady=5)

        # Time
        Time_label = Label(left_inside_frame, text="Time:",textvariable=self.var_atten_time,font=("times new roman", 12, "bold"), bg="white")
        Time_label.grid(row=1, column=2, sticky=W, padx=5, pady=5)

        Time_entry = ttk.Entry(left_inside_frame, width=20, font=("times new roman", 12, "bold"))
        Time_entry.grid(row=1, column=3, sticky=W, padx=5, pady=5)

        # Attendance (Present/Absent)
        Attendance_label = Label(left_inside_frame, text="Attendance:", font=("times new roman", 12, "bold"), bg="white")
        Attendance_label.grid(row=2, column=2, sticky=W, padx=5, pady=5)

        Attendance_combobox = ttk.Combobox(left_inside_frame, width=18,textvariable=self.var_atten_attendance, font=("times new roman", 12, "bold"), state="readonly")
        Attendance_combobox['values'] = ('Select', 'Present', 'Absent')
        Attendance_combobox.grid(row=2, column=3, sticky=W, padx=5, pady=5)

        # Button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=235, width=610, height=60)

        save_btn = Button(btn_frame, text="Import CSV",command=self.importCsv,width=14, font=("times new roman",13,"bold"), bg="purple", fg="orange")
        save_btn.grid(row=0, column=0,padx=2,pady=2)

        update_btn = Button(btn_frame, text="Export CSV",command=self.exportCsv, width=14, font=("times new roman",13,"bold"), bg="purple", fg="orange")
        update_btn.grid(row=0, column=1,padx=2,pady=2)

        delete_btn = Button(btn_frame, text="Update", width=14, font=("times new roman",13,"bold"), bg="purple", fg="orange")
        delete_btn.grid(row=0, column=2,padx=2,pady=2)

        reset_btn = Button(btn_frame, text="Reset", width=14,command=self.reset_data, font=("times new roman",13,"bold"), bg="purple", fg="orange")
        reset_btn.grid(row=0, column=3,padx=2,pady=2)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=710, y=10, width=600, height=490)

        table_frame = Frame(Right_frame,bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=1, y=10, width=595, height=418)

        #______________scroll bar____________
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendane")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

        #---------------fetch data---------------------#
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")], parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No data to export.", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=[("CSV File", "*.csv"), ("All Files", "*.*")], parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}", parent=self.root)

    def get_cursor(self,event=None):
        cursor_rows=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_rows)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
            
    

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()