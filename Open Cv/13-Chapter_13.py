# Basic Function or Manipulation in Open CV
import cv2 as cv
from cv2 import resize
import numpy as np
img=cv.imread("resources/photo.jpg")


# # Resizing the Image :
# re_Size=cv.resize(img,(450,250))

# # Gray Image
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# # Black and White Image
# thresh,b_w=cv.threshold(gray,127,255,cv.THRESH_BINARY)

# # Blurred image
# blurr_image=cv.GaussianBlur(img,(7,7),0)

# Egde detection 
edge_detection=cv.Canny(img,48,48)
mat_karnel=np.ones((3,3),np.uint8)
# Thickness of line 
# dialated_img=cv.dilate(edge_detection,(51,51),iterations=1)
dialated_img=cv.dilate(edge_detection,(mat_karnel),iterations=2)

# Make Thinnner Outline 
ero_img=cv.erode(dialated_img,mat_karnel,iterations=1)

# Cropping Image (we woll use numpy not open cv for cropping )
print("The size of Image is :",img.shape)
crop_ing=img  [0:200,200:300]



cv.imshow("Original:",img)
# cv.imshow("Re size Image:",re_Size)
# cv.imshow("Gray Image:",gray)
# cv.imshow("Black and White:",b_w)
# cv.imshow("Blurr:",blurr_image)
# cv.imshow("Edge:",edge_detection)
# cv.imshow("Dialated:",dialated_img)
# cv.imshow("Thinner Image:",ero_img)
cv.imshow("Resized Image:",crop_ing)
cv.waitKey(0)
cv.destroyAllWindows()