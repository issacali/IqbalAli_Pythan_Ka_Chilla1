# converting an Image and Renaming it ....

import cv2 as cv
import sys
img = cv.imread("resources/photo.jpg")
img = cv.resize(img,(400,300))
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("MyImage",img)
#cv.imshow("MyImage_gray",gray_img)
cv.imwrite('resources/2_gray1.png',gray_img)
cv.waitKey(0)
cv.destroyAllWindows()