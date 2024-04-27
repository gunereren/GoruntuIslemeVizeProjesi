import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Eren\Pictures\Saved Pictures\\1_goz.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
edges = cv2.GaussianBlur(edges, (3, 3), 0)
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 50, param1=30, param2=48, minRadius=0, maxRadius=50)
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 4)
cv2.imshow("edges", edges)
cv2.imshow("frame", img)
if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
    exit(0)
