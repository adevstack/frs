from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageFilter
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x710+0+0")
        self.root.title("Face Recognition System")

        # Title label
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 25, "bold"), bg="royal blue", fg="white")
        title_lbl.place(x=0, y=0, width=1360, height=45)

        # Background image
        img_top = Image.open(r"img\bg4.jpg")
        img_top = img_top.resize((1360, 1080), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1360, height=650)

        # Developer Names
        dev_names = ["Afroz Aman", "Anishek Gulshan", "Arnab Singha", "Aliva Bain"]
        y_position = 200  # Initial Y position for the names

        for i, name in enumerate(dev_names):
            Label(self.root, text=f"{i+1}. {name}", font=("times new roman", 20, "bold"), fg="black", bg="lightgray").place(
                x=500, y=y_position)
            y_position += 60  # Increment Y position for each name


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
