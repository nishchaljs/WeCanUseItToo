import cv2
import numpy as np
import os
import sqlite3
import settings
import smtplib 
#path='/Users/sanjanasrinivasareddy/Desktop/nmit/20200219_111952.jpeg'
facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#cam = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainingdata.yml")
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
img_name =''

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)

    if k%256 == 32:
        # SPACE pressed
        img_name = "face.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        break

cam.release()

cv2.destroyAllWindows()
# id = 0
# font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)

def getProfile(id):
    conn=sqlite3.connect("FaceBase.db")
    # cmd="SELECT * FROM Peoples WHERE ID="+str(id)
    cursor=conn.execute("SELECT * FROM Peoples WHERE id=?", (id,))
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile
l=[]
i=0
   
#filelist = os.listdir(settings.path)
try:
    xx=0
    
    file='face.png'
    print(file)

    img = cv2.imread(file)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])
        if(id==120):
            id=4
        profile=getProfile(id)
        print(id)
        l.append(id)
    xx=xx+1
except:
    xx=xx+1

print(l)
if(len(l)==0):
	print("Not a valid user")
else:
	p=max(set(l), key = l.count)

	profile=getProfile(p)
	settings.sad=profile
	print('student profile is')
	print(profile)


