from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import messagebox
from time import strftime
from datetime import datetime
import cv2
import mysql.connector
import os
import numpy as np


class Recognizer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x710+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNIZER", font=("times new roman", 15, "bold"), bg="royal blue", fg="white")
        title_lbl.place(x=0, y=0, width=1360, height=45)

        # 1st Image
        try:
            img_top = Image.open("img/tdimg2.jpg")
        except:
            img_top = self.create_placeholder_image(700, 700, "Face Recognition")
        img_top = img_top.resize((700, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=700, height=700)

        # 2nd Image
        try:
            img_bottom = Image.open("img/tr2.webp")
        except:
            img_bottom = self.create_placeholder_image(860, 700, "Recognition Panel")
        img_bottom = img_bottom.resize((860, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=700, y=45, width=760, height=700)

        # Button
        b1_1 = Button(f_lbl, text="Start Training", cursor="hand2", font=("times new roman", 20, "bold"), bg="royal blue", fg="white", command=self.face_recog)
        b1_1.place(x=440, y=500, width=200, height=40)

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

    def mark_attendance(self, i, r, n, d):
        with open("oldschooldev.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            nameList = [line.split(",")[0] for line in myDataList]
            if i not in nameList:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="qwerty", database="face_recognition")
                    my_cursor = conn.cursor()

                    my_cursor.execute("SELECT Name FROM student WHERE Student_Id = %s", (id,))
                    n = "+".join(my_cursor.fetchone() or ["Unknown"])

                    my_cursor.execute("SELECT Roll_Number FROM student WHERE Student_Id = %s", (id,))
                    r = "+".join(my_cursor.fetchone() or ["Unknown"])

                    my_cursor.execute("SELECT Department FROM student WHERE Student_Id = %s", (id,))
                    d = "+".join(my_cursor.fetchone() or ["Unknown"])

                    my_cursor.execute("SELECT Student_ID FROM student WHERE Student_Id = %s", (id,))
                    i = "+".join(my_cursor.fetchone() or ["Unknown"])

                except Exception as e:
                    print(f"Database Error: {e}")
                    i, n, r, d = "Unknown", "Unknown", "Unknown", "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID: {i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    cv2.putText(img, f"Department: {d}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.8, color, 3)
                    self.mark_attendance(i, r, n, d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "??? Unknown ???", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 3)

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        if faceCascade.empty():
            print("Error loading Haarcascade!")
            return

        clf = cv2.face.LBPHFaceRecognizer_create()
        if not os.path.exists("classifier.xml"):
            print("Classifier file not found!")
            return
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        try:
            while True:
                ret, img = video_cap.read()
                if not ret:
                    print("Failed to grab frame!")
                    break
                img = recognize(img, clf, faceCascade)
                cv2.imshow("!!! Welcome to Face Recognition !!!", img)

                if cv2.waitKey(1) == 13:  # Enter Key
                    break
        finally:
            video_cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Recognizer(root)
    root.mainloop()
