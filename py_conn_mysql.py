import mysql.connector

conn = mysql.connector.connect(host="localhost", username="root", password="qwerty", database="face_recognition")
my_cursor = conn.cursor()

conn.commit()
conn.close()

print("Connection Successfully Stablished!!!!!!")