from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
from tkinter import messagebox
import cv2.face
import mysql.connector
import cv2
import os 
import numpy as np


class Traindata:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x710+0+0")  
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="Test Dataset",font=("times new roman",15,"bold"),bg="royal blue",fg="white")
        title_lbl.place(x=0, y=0, width=1360, height=45)

        try:
            img_top= Image.open("img/tdimg1.jpg")
        except:
            img_top= self.create_placeholder_image(1360, 285, "Train Data Top")
        img_top= img_top.resize((1360,285), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl =Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1360,height=285)

        #-----------------------------button----------#
        b1_1=Button(self.root,text="Start Testing",command=self.train_classifier,cursor="hand2",font=("times new roman",15,"bold"),bg="royal blue",fg="white")
        b1_1.place(x=0, y=328, width=1360, height=60)

        try:
            img_bottom= Image.open("img/tdimg2.jpg")
        except:
            img_bottom= self.create_placeholder_image(1360, 285, "Train Data Bottom")
        img_bottom= img_bottom.resize((1360,285), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl =Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0, y=390, width=1360,height=285)

    def create_placeholder_image(self, width, height, text):
        """Create a placeholder image with text"""
        img = Image.new('RGB', (width, height), color='lightgray')
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("Arial", 20)
        except:
            font = ImageFont.load_default()
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        x = (width - text_width) // 2
        y = (height - text_height) // 2
        draw.text((x, y), text, fill='black', font=font)
        return img

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')    #grey scale image  (algo start from here)
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)   # here we used numpy coz it enhances the process of converting in array by 88%

#------------------------------------------Train the classifier---------------------------------------------------------#
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,np.array(ids))
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Data Compilation Completed")





if __name__=="__main__":
    root=Tk()
    obj=Traindata(root)
    root.mainloop()