import cv2
import face_cam_detect
import face_detection
import face_D

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('resources/photo.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
try:
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
     cv2.imshow('img', img)
except Exception as e :
    print(" exception:",e)
    
# Draw rectangle around the faces

# Display the output

cv2.waitKey()