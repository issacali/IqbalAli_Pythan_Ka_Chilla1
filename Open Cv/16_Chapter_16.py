# Saving HD recording of cam stream 
import cv2 as cv
import numpy as np 
cap=cv.VideoCapture(700)

def hd_resulotion():
    cap.set(3,1280)
    cap.set(4,720)

# def sd_resulotion():
#     cap.set(3,640)
#     cap.set(4,480)

# def fhd_resulotion():
#     cap.set(3,1920)
#     cap.set(4,1080)
    
hd_resulotion()
# sd_resulotion()
# fhd_resulotion()


# writing Format, video writer object and file Output
frame_width =int(cap.get(3))  # 4:3
frame_height =int(cap.get(4)) # 4:3
#Saving actual video
out = cv.VideoWriter('resources/cam_v.mp4', cv.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
while(True):
    ret, frame = cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    if ret== True:
     out.write(frame)
     cv.imshow('frame', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
