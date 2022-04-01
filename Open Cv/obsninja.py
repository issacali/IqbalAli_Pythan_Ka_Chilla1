# Import essential libraries
from email.headerregistry import Address
import requests
import cv2 as cv
import time 
import numpy as np
import imutils
cap =cv.VideoCapture(0)
add = "https://vdo.ninja/?view=zxw8bYu&label=Iqbal"
cap.open(add)

while (cap.isOpened()):
    #capture fram by frame
    # Step 3 display frame by frame 
    ret,frame=cap.read()
    if ret==True:
        cv.imshow("Frame:",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    # step4 Release webcam easly
    cap.release()
    cv.destroyAllWindows()  
