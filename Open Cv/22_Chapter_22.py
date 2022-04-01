# Face Detection 
import cv2 as cv
import face_D
from imutils import paths
import pickle
import cv2

import numpy as np
#Creating cascade to detect face
face_cascade = cv.CascadeClassifier('resources/haarcascade_frontalface_default.xml')
img = cv.imread("resources/f.jpg")

#converting in to grayscale
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#face detection
try:
    faces = face_cascade.detectMultiScale(gray_img,1.1,4)
    for(x,y,w,h) in faces:
      cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

except Exception as e:
    print("Exception:",e)

 #Draw Rectangle


#     print(img.shape) #(2208, 1242, 3)
# #dividing in 2 images
# #img =cv.resize(img,(621,1104))
# print(img.shape) #(2208, 1242, 3)
cv.imwrite("resources/f.jpg",img)

cv.imshow("MyImage",img)

cv.waitKey(0)
cv.destroyAllWindows()