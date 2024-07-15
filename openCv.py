import cv2

#Using a function called the
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame = cam.read()
    if cv2.waitKey(10) == ord('r'):
        break
    cv2.imshow("Jayant's cam",frame)