from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2


class Helpdesk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x710+0+0")  
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="Help Desk",font=("times new roman",25,"bold"),bg="royal blue",fg="white")
        title_lbl.place(x=0, y=0, width=1360, height=45)

        img_top= Image.open(r"img\bg3.webp")
        img_top= img_top.resize((1360,1080), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl =Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1360,height=650)

        #frame
        main_frame=Frame(f_lbl,bd=2,bg="royal blue")
        main_frame.place(x=900,y=0,width=500,height=650)

        self.photoimg1 = ImageTk.PhotoImage(Image.open(r"img\dev0.jpg").resize((150, 150), Image.Resampling.LANCZOS))
        lbl1 = Label(main_frame, image=self.photoimg1)
        lbl1.place(x=0, y=5, width=150, height=150)

        lbl1_name = Label(main_frame, text="Afroz Aman", font=("Arial", 12, "bold"), bg="royal blue", fg="white")
        lbl1_name.place(x=0, y=160, width=150, height=30)

        self.photoimg2 = ImageTk.PhotoImage(Image.open(r"img\dev1.jpg").resize((150, 150), Image.Resampling.LANCZOS))
        lbl2 = Label(main_frame, image=self.photoimg2)
        lbl2.place(x=280, y=5, width=150, height=150)

        lbl2_name = Label(main_frame, text="Anishek Gulshan", font=("Arial", 12, "bold"), bg="royal blue", fg="white")
        lbl2_name.place(x=280, y=160, width=150, height=30)

        self.photoimg3 = ImageTk.PhotoImage(Image.open(r"img\dev0.jpg").resize((150, 150), Image.Resampling.LANCZOS))
        lbl3 = Label(main_frame, image=self.photoimg3)
        lbl3.place(x=0, y=400, width=150, height=150)

        lbl3_name = Label(main_frame, text="Arnab Kr Singha", font=("Arial", 12, "bold"), bg="royal blue", fg="white")
        lbl3_name.place(x=0, y=560, width=150, height=30)

        self.photoimg4 = ImageTk.PhotoImage(Image.open(r"img\dev3.jpg").resize((150, 150), Image.Resampling.LANCZOS))
        lbl4 = Label(main_frame, image=self.photoimg4)
        lbl4.place(x=280, y=400, width=150, height=150)

        lbl4_name = Label(main_frame, text="Aliva Bain", font=("Arial", 12, "bold"), bg="royal blue", fg="white")
        lbl4_name.place(x=280, y=560, width=150, height=30)



if __name__=="__main__":
    root=Tk()
    obj=Helpdesk(root)
    root.mainloop()