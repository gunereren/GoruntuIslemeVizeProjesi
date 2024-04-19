import cv2

image = cv2.imread("C:\\Users\\Eren\\Pictures\\Saved Pictures\\3.jpg")

if image is not None:
    cv2.imshow("Image", image)

    gaussianBlur = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow("Gaussian Blur", gaussianBlur)


    gray = cv2.cvtColor(gaussianBlur, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)
    hsv = cv2.cvtColor(gaussianBlur, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", hsv)
    if cv2.waitKey(0) == ord("q"):
        cv2.destroyAllWindows()
