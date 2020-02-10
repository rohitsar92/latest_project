import cv2
import numpy as np
from PIL import Image
import os

recognizer = cv2.face.LBPHFaceRecognizer_create()
path='dataSet'
#detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesWithId(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:

       

        #loading the image and converting it to gray scale
        faceImg=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        faceNp=np.array(faceImg,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        
        faces.append(faceNp)
        print(Id)
        #If a face is there then append that in the list as well as Id of it
        Ids.append(Id)
        cv2.imshow("training",faceNp)
        cv2.waitKey(1000)
    return faces,Ids


faces,Ids = getImagesWithId('dataSet')
recognizer.train(faces, np.array(Ids))
recognizer.save('recognizer/trainnerData.yml')
cv2.destroyAllWindows()


