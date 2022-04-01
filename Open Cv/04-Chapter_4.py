# converting color image into Black and white 


import cv2 as cv
import sys
img = cv.imread("resources/photo.jpg")
img = cv.resize(img,(400,300))
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
(thresh, b_w) = cv.threshold(gray_img,127,255,cv.THRESH_BINARY)
cv.imshow("MyImage",img)
cv.imshow("MyImage_gray",gray_img)
cv.imshow("MyImage_black_White",b_w)
cv.waitKey(0)
cv.destroyAllWindows()

