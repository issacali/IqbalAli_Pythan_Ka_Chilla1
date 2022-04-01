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


while(True):
    ret,frame=cap.read()
    if ret== True:
        cv.imshow("Camera",frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()
