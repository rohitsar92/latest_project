import cv2
import numpy as np

cascadePath = "Haar/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

cam = cv2.VideoCapture(0)
idd=input('enter user id')
sampleNum=0

while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        
        sampleNum=sampleNum+1
        cv2.imwrite("dataSet/"+str(idd)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(im, (x,y), (x+w,y+h), (0,255,0),2)
            
        cv2.waitKey(100)
    cv2.imshow('im',im)
    cv2.waitKey(1)
    if(sampleNum>1):
        break
cam.release()
cv2.destroyAllWindows()

