import cv2 as cv
import numpy as np
# Draw an Image
imgb=np.zeros((600,600))
imgw=np.ones((600,600))


# Addding colors to the canvas 
col_img=np.zeros((600,600,3),np.uint8)  # 3 is color channel addition 
col_img[:]=100,0,400

# Coloring a part of Image
col_img[0:300,0:300]=255,0,0

# Adding Line 

cv.line(col_img,(0,0),(col_img.shape[0],col_img.shape[1]),(0,0,0),3) #Diagonal Line 
cv.line(col_img,(0,0),(300,300),(255,250,0),3)

# Addomg Rectangles
cv.rectangle(col_img,(50,100),(300,400),(255,255,0),3)
# too fill color 
# cv.rectangle(col_img,(50,100),(300,400),(255,255,0),cv.FILLED)

# Adding Circle 
cv.circle(col_img,(300,400),50,(255,0,100),5)

# Color filling 
# cv.circle(col_img,(300,400),50,(255,0,100),cv.FILLED)

# Adding Text 
cv.putText(col_img," Pyrhon ka chilla with Aamar sir ",(250,300),cv.CALIB_FIX_FOCAL_LENGTH,1,(255,0,300),2)


# cv.imshow("Black Image:",imgb)
# cv.imshow("White Image:",imgw)
# print("The size of Black Image is ",imgb.shape)
# print("The size of White Image is ",imgw.shape)
cv.imshow("colored Image:",col_img)

cv.waitKey(0)
cv.destroyAllWindows()