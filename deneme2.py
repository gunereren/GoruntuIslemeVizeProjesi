import cv2
import numpy as np


def estimate_blur_direction(gray_image):
    # Sobel filtreleri kullanarak X ve Y yönlü türevleri hesapla
    sobelX = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
    sobelY = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)

    # Türevlerin mutlak değerlerini al
    abs_sobelX = np.abs(sobelX)
    abs_sobelY = np.abs(sobelY)

    # X ve Y türevlerinin toplamını bul
    magnitude = cv2.addWeighted(abs_sobelX, 0.5, abs_sobelY, 0.5, 0)

    # Türevlerin toplamı üzerinde bir eşikleme uygula
    _, blurred_mask = cv2.threshold(magnitude, 50, 255, cv2.THRESH_BINARY)

    # Maskenin yönünü belirle
    orientation = np.arctan2(sobelY, sobelX)

    return blurred_mask, orientation


def deblur_image(image, blur_mask, blur_orientation):
    # Motion blur'ı tersine çevirme (deconvolution) için bir kernel oluştur
    kernel_size = 21
    motion_kernel = np.zeros((kernel_size, kernel_size))

    # Blur yönüne göre kerneli doldur
    orientation_degrees = np.degrees(blur_orientation)
    angle = orientation_degrees + 90.0
    angle_rad = np.radians(angle)

    cos_theta = np.cos(angle_rad)
    sin_theta = np.sin(angle_rad)

    center = kernel_size // 2
    for i in range(kernel_size):
        offset = i - center
        x_offset = int(round(offset * cos_theta))
        y_offset = int(round(offset * sin_theta))
        x = center + x_offset
        y = center + y_offset
        if 0 <= x < kernel_size and 0 <= y < kernel_size:
            motion_kernel[y, x] = 1.0 / kernel_size

    # Blur maskesini kullanarak deconvolution işlemi yap
    deblurred_image = cv2.filter2D(image, -1, motion_kernel)

    return deblurred_image


# Görüntüyü yükle
image = cv2.imread("C:\\Users\\Eren\\Pictures\\Saved Pictures\\1.1_blurcar.jpg")

# Görüntüyü gri tonlamalıya çevir
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Motion blur'ın yönünü tahmin et
blur_mask, blur_orientation = estimate_blur_direction(gray_image)

# Motion blur'ı tersine çevir
deblurred_image = deblur_image(image, blur_mask, blur_orientation)

# Sonuçları göster
cv2.imshow('Original Image', image)
cv2.imshow('Deblurred Image', deblurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
