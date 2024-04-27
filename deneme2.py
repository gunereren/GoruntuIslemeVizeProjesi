import cv2
import numpy as np


# Trackbar callback fonksiyonu
def update_canny_thresholds(threshold1, threshold2):
    # Canlı kameradan görüntüyü al
    ret, frame = cap.read()
    if not ret:
        return

    # Görüntüyü gri tonlamalıya dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Canny kenar tespiti uygula
    edges = cv2.Canny(gray, threshold1, threshold2)

    # Görüntüyü ekranda göster
    cv2.imshow('Canny Edge Detection', edges)


# Canlı kamera bağlantısını başlat
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera bağlantısı açılamadı!")
    exit()

# İlk değerler için başlangıç eşik değerleri
initial_threshold1 = 50
initial_threshold2 = 150

# Pencere oluştur ve trackbar'ları ekle
cv2.namedWindow('Canny Edge Detection')
cv2.createTrackbar('Threshold1', 'Canny Edge Detection', initial_threshold1, 255, lambda x: None)
cv2.createTrackbar('Threshold2', 'Canny Edge Detection', initial_threshold2, 255, lambda x: None)

while True:
    # Trackbar değerlerini al
    threshold1 = cv2.getTrackbarPos('Threshold1', 'Canny Edge Detection')
    threshold2 = cv2.getTrackbarPos('Threshold2', 'Canny Edge Detection')

    # Görüntüyü işle ve ekranda göster
    update_canny_thresholds(threshold1, threshold2)

    # ESC tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) == 27:
        break

# Kamera bağlantısını ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
