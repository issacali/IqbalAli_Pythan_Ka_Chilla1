# Settimng of Video and Camera
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(700)
# cap.set(10,100)   # 10 is the key for brighness 
cap.set(3,1920)  # 3 is key for width  
cap.set(4,1080)  # 4 is key for height 

while(True):
    ret, frame = cap.read()
    if ret== True:
    #  out.write(gray)
     cv.imshow('frame',frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
 
cap.release()
cv.destroyAllWindows()