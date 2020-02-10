import cv2 
import numpy as np

cascadePath = "Haar/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

cam = cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read( "recognizer\\trainnerData.yml")


Id=0
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0),4)
        Id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(Id<50):
            if(Id==1):
                Id=("rohit")
                print("rk")
            elif(Id==2):
                Id=("Unknown")
                print("Unknown")
        else:
            Id="unk"
       
        
            
        
        cv2.rectangle(im, (x-22,y-90), (x+w+22,y-22), (0,255,0),-1)
        
        cv2.putText((im),str(Id),(x,y-40), font,2,(255),1)
        
    cv2.imshow('im',im)
    if(cv2.waitKey(2)==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()



