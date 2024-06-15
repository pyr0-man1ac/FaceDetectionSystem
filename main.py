import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from tkinter import *
import threading
import subprocess

window = Tk()
window.title("Attendance System")
window.config(background="Lime")
window.geometry("400x300")

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%d-%m-%Y')
            dtString1 = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString},{dtString1}')

encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = None

def start_face_recognition():
    global cap
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS= cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex]

                y1,x2,y2,x1 = faceLoc
                y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
                markAttendance(name)

        cv2.imshow('Webcam',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def start_recognition_thread():
    t = threading.Thread(target=start_face_recognition)
    t.start()

def stop_camera():
    global cap
    if cap is not None:
        cap.release()
        cv2.destroyAllWindows()

def open_attendance_file():
    subprocess.Popen(['Attendance.csv'], shell=True)

def open_webcam():
    start_recognition_thread()


check_in_button = Button(window, text="Take Attendance",font=("Times New Roman",15),bg='beige',fg='black', command=open_webcam)
check_in_button.pack(pady=20)

stop_camera_button = Button(window, text="Stop Attendance",font=("Times New Roman",15),bg='beige',fg='black', command=stop_camera)
stop_camera_button.pack(pady=15)

open_attendance_button = Button(window, text="Show Attendance",font=("Times New Roman",15),bg='beige',fg='black', command=open_attendance_file)
open_attendance_button.pack(pady=15)

window.mainloop()
