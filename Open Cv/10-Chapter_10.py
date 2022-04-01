# convert into different shades black and white gray
import cv2 as cv
import numpy as np
cap=cv.VideoCapture(700)
while(True):
    (ret,frame)=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    (thresh,binary) = cv.threshold(gray,127,255,cv.THRESH_BINARY)

    cv.imshow("OrriginalCam",frame)
    cv.imshow("GrayCam",gray)
    cv.imshow("Binary",binary)
    if cv.waitKey(1) & 0xFF == ord('q'):
      break
         
   

cap.release() 
cv.destroyAllWindows()

