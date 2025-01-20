from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x710+0+0")  
        self.root.title("Face Recognition System")

        #---------------------------------------------------variable------------------------------------------------------#
        self.var_dep= StringVar()
        self.var_course= StringVar()
        self.var_year= StringVar()
        self.var_semester= StringVar()
        self.var_std_id= StringVar()
        self.var_std_name= StringVar()
        self.var_div= StringVar()
        self.var_roll= StringVar()
        self.var_gender= StringVar()
        self.var_dob= StringVar()
        self.var_email= StringVar()
        self.var_phone= StringVar()
        self.var_address= StringVar()
        self.var_teacher= StringVar()
        self.var_photo = StringVar()
        self.var_radio = StringVar()
        #----------------------------------------------------------------------------------------------------------------#
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

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=45,width=1500,height=650)

        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=45,y=10,width=600,height=490)

        img_left = Image.open(r"C:\Users\Aman\Desktop\FRs\img\student.png")
        img_left= img_left.resize((120,80), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl =Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=200, y=0, width=120,height=80)

        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"))
        current_course_frame.place(x=20,y=70,width=555,height=120)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","BCA","MCA","B.tech","M.Tech")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course 
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","CA","MC","ME","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","2020-2023","2020-2024","2022-2026","2023-2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student course
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        Class_Student_frame.place(x=20,y=190,width=555,height=260)

        #studentID
        studentID_label=Label(Class_Student_frame,text="Student_ID",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,sticky=W)

        studentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=15,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,sticky=W)

        #student Name
        studentName_label=Label(Class_Student_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,sticky=W)

        studentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=15,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,sticky=W)

        #class division
        class_div_label=Label(Class_Student_frame,text="Class_Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=2,column=0,sticky=W)

        #class_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_div,width=15,font=("times new roman",12,"bold"))
        #class_div_entry.grid(row=2,column=1,sticky=W)
        div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=17,state="read only")
        div_combo["values"]=("X","Y","Z")
        div_combo.current(0)
        div_combo.grid(row=2,column=1,padx=0,pady=0,sticky=W)

        #Roll number
        roll_number_label=Label(Class_Student_frame,text="Roll_Number",font=("times new roman",12,"bold"),bg="white")
        roll_number_label.grid(row=2,column=2,sticky=W)

        roll_number_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_roll,width=15,font=("times new roman",12,"bold"))
        roll_number_entry.grid(row=2,column=3,sticky=W)

        #Gender
        Gender_label=Label(Class_Student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        Gender_label.grid(row=3,column=0,sticky=W)

        #Gender_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_gender,width=15,font=("times new roman",12,"bold"))
        #Gender_entry.grid(row=3,column=1,sticky=W)
        Gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="read only")
        Gender_combo["values"]=("Male","Female","Non-Binary")
        Gender_combo.current(0)
        Gender_combo.grid(row=3,column=1,padx=0,pady=0,sticky=W)
        
        #dob
        dob_label=Label(Class_Student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=3,column=2,sticky=W)

        dob_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_dob,width=15,font=("times new roman",12,"bold"))
        dob_entry.grid(row=3,column=3,sticky=W)

        #phone_no
        phone_no_label=Label(Class_Student_frame,text="Ph_No",font=("times new roman",12,"bold"),bg="white")
        phone_no_label.grid(row=4,column=0,sticky=W)

        phone_no_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=15,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=4,column=1,sticky=W)

        #email
        email_label=Label(Class_Student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=4,column=2,sticky=W)

        email_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_email,width=15,font=("times new roman",12,"bold"))
        email_entry.grid(row=4,column=3,sticky=W)

        #address
        address_label=Label(Class_Student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=5,column=0,sticky=W)

        address_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_address,width=15,font=("times new roman",12,"bold"))
        address_entry.grid(row=5,column=1,sticky=W)

        #teacher
        teacher_label=Label(Class_Student_frame,text="Teachers",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=5,column=2,sticky=W)

        teacher_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_teacher,width=15,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=5,column=3,sticky=W)

       # Radio buttons
        self.var_radio = StringVar()  # One StringVar for both radio buttons
        radiobtn1 = ttk.Radiobutton(Class_Student_frame, text="Take Photo Sample", variable=self.var_radio, value="Yes")
        radiobtn1.grid(row=6, column=0, padx=10, pady=5, sticky=W)

        radiobtn2 = ttk.Radiobutton(Class_Student_frame, text="No Photo Sample", variable=self.var_radio, value="No")
        radiobtn2.grid(row=6, column=1, padx=10, pady=5, sticky=W)

        # Button frame
        btn_frame = Frame(Class_Student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=150, width=550, height=77)

        save_btn = Button(btn_frame, text="Save",command=self.add_data,width=13, font=("times new roman",13,"bold"), bg="purple", fg="orange")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update",command=self.update_data, width=13, font=("times new roman",13,"bold"), bg="purple", fg="orange")
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text="Delete",command=self.delete_data, width=13, font=("times new roman",13,"bold"), bg="purple", fg="orange")
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=13, font=("times new roman",13,"bold"), bg="purple", fg="orange")
        reset_btn.grid(row=0, column=3)

        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=550,height=40)

        take_photo_btn = Button(btn_frame, text="Take Photo Sample",command=self.generate_dataset, width=27, font=("times new roman",13,"bold"), bg="purple", fg="orange")
        take_photo_btn.grid(row=2, column=4)

        update_photo_btn = Button(btn_frame, text="Update Photo Sample", width=27, font=("times new roman",13,"bold"), bg="purple", fg="orange")
        update_photo_btn.grid(row=2, column=5)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        Right_frame.place(x=710, y=10, width=600, height=490)

        img_Right = Image.open(r"C:\Users\Aman\Desktop\FRs\img\srch.png")
        img_Right= img_Right.resize((120,80), Image.Resampling.LANCZOS)
        self.photoimg_Right = ImageTk.PhotoImage(img_Right)

        f_lbl=Label(Right_frame,image=self.photoimg_Right)
        f_lbl.place(x=5,y=0,width=590,height=70)

        #---------------------------------------search system-------------------------------------------------#
        search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE,text="Search System", font=("times new roman",13,"bold"))
        search_frame.place(x=5, y=80, width=590, height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=17,state="read only")
        search_combo["values"]=("Select","Roll_Number","Student ID","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,sticky=W)

        search_btn = Button(search_frame, text="Search", width=10, font=("times new roman",12,"bold"), bg="purple", fg="orange")
        search_btn.grid(row=0, column=3)

        show_all_btn = Button(search_frame, text="Show All", width=10, font=("times new roman",12,"bold"), bg="purple", fg="orange")
        show_all_btn.grid(row=0, column=4)

    
        #--------------------------------------table_frame----------------------------------------------------------#
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=155, width=590, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year","sem","id", "name", "div", "roll", "gender", "dob", "phone", "email", "address", "teacher", "photo"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student_ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Class_Division")
        self.student_table.heading("roll", text="Roll_Number")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("phone", text="Ph_No")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teachers")
        self.student_table.heading("photo", text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #-----------------------------------------------------function declaration--------------------------------------------#
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "Fill all the fields ", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="qwerty", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO student (Department, Course, Year, Semester, Student_ID, Name, Class_Division, Roll_Number, Gender, DOB, Ph_No, Email, Address, Teachers, Photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_std_id.get(),
                                    self.var_std_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_phone.get(),
                                    self.var_email.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio.get()
                                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student record has been added successfully", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


#------------------------------------------fetch data-------------------------------------------------------#
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="qwerty", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

#-------------------------------------------get cursor-------------------------------------------------------#
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_email.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio.set(data[14])

#--------------------------------------------------------------update function-------------------------------#
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "Fill all the fields ", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update student details",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="qwerty", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s, Course=%s, Year=%s, Semester=%s,Name=%s,Class_Division=%s,Roll_Number=%s,Gender=%s,DOB=%s,Ph_No=%s,Email=%s,Address=%s,Teachers=%s,Photo=%s where Student_ID=%s",(

                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_std_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_phone.get(),
                                    self.var_email.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio.get(),
                                    self.var_std_id.get()
                                ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Student details Successfully Updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

#---------------------delete-----------------------------------#
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Please select student ID",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="qwerty", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_ID=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)    
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 
#-----------------------------------------------------reset---------------------------------------#
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio.set("")

#------------------------------------------generate data-set or take photo sample-------------@old_school_dev---------#
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "Fill all the fields ", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="qwerty", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student")
                myresult = my_cursor.fetchall()
                
                id=0
                for x in myresult:
                    id+=1
                    my_cursor.execute("update student set Department=%s, Course=%s, Year=%s, Semester=%s,Name=%s,Class_Division=%s,Roll_Number=%s,Gender=%s,DOB=%s,Ph_No=%s,Email=%s,Address=%s,Teachers=%s,Photo=%s where Student_ID=%s",(

                                    self.var_dep.get(),
                                    self.var_course.get(),
                                    self.var_year.get(),
                                    self.var_semester.get(),
                                    self.var_std_name.get(),
                                    self.var_div.get(),
                                    self.var_roll.get(),
                                    self.var_gender.get(),
                                    self.var_dob.get(),
                                    self.var_phone.get(),
                                    self.var_email.get(),
                                    self.var_address.get(),
                                    self.var_teacher.get(),
                                    self.var_radio.get(),
                                    self.var_std_id.get()==id+1
                                ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
                    #----------------------------------load predefined data on face from opencv------------------------#
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #scalling  factor=1.3
                        #minimum neighbour=5

                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped
                        
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(460,460))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(100,100),cv2.FONT_HERSHEY_COMPLEX,3,(0,244,0),3)
                            cv2.imshow("cropped face",face)
                        if cv2.waitKey(1)==13 or int(img_id)==7:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Dataset Compiled")
                    
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 





if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()