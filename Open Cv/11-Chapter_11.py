# Writing videos from cam 
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(700)

# writing Format, video writer object and file Output
frame_width =int(cap.get(8))  # 4:3
frame_height =int(cap.get(10)) # 4:3
#Saving actual video
out = cv.VideoWriter('resources/cam_v.mp4', cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height),isColor=False )
while(True):
    ret, frame = cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if ret== True:
     out.write(gray)
     cv.imshow('frame', gray)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()