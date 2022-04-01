import cv2

# 1.creating a video object
video = cv2.VideoCapture(700) 
# 2. Variable
a = 0
# 3. While loop
while True:
    a = a + 1
    # 4.Create a frame object
    check, frame = video.read()
    # Converting to grayscale
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 5.show the frame!
    cv2.imshow("Capturing",frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
    # 6.for playing 
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# 7. image saving
showPic1 = cv2.imwrite("frame.jpg",frame)
showPic2 = cv2.imwrite("gray.jpg",gray)
print(showPic1)
print(showPic2)
# 8. shutdown the camera
video.release()
cv2.destroyAllWindows 