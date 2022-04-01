# Video COnversion to Grayscale
# converting Video into grayscale
import cv2 as cv
import sys
cap = cv.VideoCapture("resources/v.mp4")

while(True):
    (ret,frame) = cap.read()
    grayframe = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    if ret == True:
        cv.imshow('video',grayframe)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break 

cap.release()
cv.destroyAllWindows()

