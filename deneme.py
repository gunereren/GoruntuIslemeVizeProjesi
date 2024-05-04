import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Eren\\Pictures\\Saved Pictures\\1.1_blurcar.jpg")
grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = img.shape[:2]

_, binaryImg = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((3, 3), np.uint8)

skeleton = np.zeros(binaryImg.shape, np.uint8)
while cv2.countNonZero(binaryImg) > 0:
    erode = cv2.erode(binaryImg, kernel)
    opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, kernel)
    temp = cv2.subtract(erode, opening)
    skeleton = cv2.bitwise_or(skeleton, temp)
    binaryImg = erode.copy()


cv2.imshow("skeleton", skeleton)
cv2.imshow("image", img)
if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
    exit(0)
