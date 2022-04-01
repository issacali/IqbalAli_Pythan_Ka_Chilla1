# Joining Two Images 
import cv2 as cv
import numpy as np

img=  cv.imread("resources/2_gray1.png")

# Stacking same image
# Horizontal stack 
# hor_img=np.hstack((img,img))

# Vertical Stacking 
ver_img=np.vstack((img,img))

# cv.imshow("Horizontal Stack",hor_img)
cv.imshow("Vertical Stack",ver_img)


cv.waitKey(0)
cv.destroyAllWindows()


# You can stack images with same shape i.e (color channel,width ,height)
# We cant resize stacked images (have to create your own function to do that )
# same number of channels np functions 
