import math
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ctypes import windll
from tkinter import messagebox
import numpy as np
import cv2
from numpy.distutils.system_info import blas_src_info

# Bu kod Tkinter penceresinin görüntü kalitesini arttırmaya yarıyor. Yazılar daha net gözüküyor.
windll.shcore.SetProcessDpiAwareness(1)


class Odev1Arayuz(tk.Toplevel):
    # Ödev 1 penceresini açılmasını ve kontrol edilmesini sağlayan class
    def __init__(self, ust_dugme_text, odev_icerik):
        # Ödev 1 constructor metodu
        super().__init__()
        self.title(ust_dugme_text + ": " + odev_icerik)
        self.geometry("800x600")
        self.odev_icerik = odev_icerik
        # Ödev 1 penceresinin özellikleri

        self.gorselKatmani = tk.Label(self)
        self.gorselKatmani.pack()

        self.gorselYukleBtn = tk.Button(self, text="Görsel Yükle", command=self.gorselYukle)
        self.gorselYukleBtn.pack(padx=10, pady=20)

        self.hsvBtn = tk.Button(self, text="HSV'ye Dönüştür", command=self.hsvDonustur)
        self.hsvBtn.pack(pady=5)

        self.cannyBtn = tk.Button(self, text="Canny Edge Detection", command=self.cannyEdgeDtc)
        self.cannyBtn.pack(pady=5)

        self.metin = tk.Label(self,
                              text="Canny için 2 tane threshold değeri var. Alttaki sürgülerden ayarlanabilir.")
        self.metin.pack(padx=10, pady=10)

        self.th1_slider = tk.Scale(self, from_=0, to=255, orient=tk.HORIZONTAL, length=200)
        self.th1_slider.set(128)
        self.th1_slider.pack()

        self.th2_slider = tk.Scale(self, from_=0, to=255, orient=tk.HORIZONTAL, length=200)
        self.th2_slider.set(255)
        self.th2_slider.pack()

        self.kapatBtn = tk.Button(self, text="KAPAT", command=self.destroy)
        # KAPAT butonuna basıldığında "destroy" metodu yardımıyla mevcut pencereyi kapatmaktadır.
        self.kapatBtn.pack(pady=10, side=tk.BOTTOM)

        self.image = None

    def hsvDonustur(self):
        # HSV'ye çevirme işlemi burada yapılmaktadır
        if self.image is not None:
            arrayImg = np.array(self.image)
            hsvImg = cv2.cvtColor(arrayImg, cv2.COLOR_BGR2HSV)
            hsvImg = Image.fromarray(hsvImg)
            hsvImg = ImageTk.PhotoImage(hsvImg)
            self.gorselKatmani.config(image=hsvImg)
            self.gorselKatmani.image = hsvImg

    def cannyEdgeDtc(self):
        # Kenar algılama metodu
        if self.image is not None:
            arrayImg = np.array(self.image)
            edges = cv2.Canny(arrayImg, self.th1_slider.get(), self.th2_slider.get())
            edges_image = Image.fromarray(edges)
            img = ImageTk.PhotoImage(edges_image)
            self.gorselKatmani.config(image=img)
            self.gorselKatmani.image = img

    def gorselYukle(self):
        file_path = filedialog.askopenfilename(filetypes=[("Resim Dosyaları", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        if self.image is not None:
            img = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=img)
            self.gorselKatmani.image = img


class Odev2Arayuz(tk.Toplevel):
    # Ödev 2 penceresini açılmasını ve kontrol edilmesini sağlayan class
    def __init__(self, ust_dugme_text, odev_icerik):
        super().__init__()
        self.title(ust_dugme_text + ": " + odev_icerik)
        self.geometry("700x700")

        self.metin = tk.Label(self, text="Bu ödevde yüklenen fotoğrafa temel görüntü operasyonları ve interpolasyon"
                                         "işlemleri uygulanacaktır.")
        self.metin.pack(padx=10, pady=10)

        self.gorselKatmani = tk.Label(self)
        self.gorselKatmani.pack()

        self.gorselYukleBtn = tk.Button(self, text="Görsel Yükle", command=self.gorselYukle)
        self.gorselYukleBtn.pack(padx=10, pady=20)

        self.gbbBtn = tk.Button(self, text="Görüntü Boyutu Büyütme (x1.1)", command=self.boyutBuyutme)
        self.gbbBtn.pack(pady=5)

        self.gbkBtn = tk.Button(self, text="Görüntü Boyutu Küçültme (x0.9)", command=self.boyutKucultme)
        self.gbkBtn.pack(pady=5)

        self.dondurmeTxt = tk.Label(self, text="Döndürme Açısı")
        self.dondurmeTxt.pack(pady=(30, 0))
        self.dondurme_slider = tk.Scale(self, from_=0, to=359, orient=tk.HORIZONTAL, length=200)
        self.dondurme_slider.set(0)
        self.dondurme_slider.pack()
        self.dondurmeBtn = tk.Button(self, text="Açıya Göre Görüntü Döndürme", command=self.goruntuDondur)
        self.dondurmeBtn.pack(pady=(0, 5))

        self.zoominBtn = tk.Button(self, text="Zoom-In (+0.1x)", command=self.zoomIn)
        self.zoominBtn.pack()

        self.zoomOutBtn = tk.Button(self, text="Zoom-Out")
        self.zoomOutBtn.pack()

        self.kapatBtn = tk.Button(self, text="KAPAT", command=self.destroy)
        self.kapatBtn.pack(pady=10, side=tk.BOTTOM)

        self.image = None

    def gorselYukle(self):
        file_path = filedialog.askopenfilename(filetypes=[("Resim Dosyaları (JPG/JPEG)", "*.jpg;*.jpeg;")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        if self.image is not None:
            img = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=img)
            self.gorselKatmani.image = img

    def boyutBuyutme(self):
        # Bilinear İnterpolasyon
        if self.image is not None:
            # Matris işlemlerinin kolayca yapılabilmesi için görsel PIL türünden NumPy Array türüne çevrildi
            arraySrc = np.array(self.image)
            # Kaynak görüntünün boyutları
            src_height, src_width = arraySrc.shape[:2]
            # En-Boy 1.1 oranında artırıldı
            new_width = int(src_width * 1.1)
            new_height = int(src_height * 1.1)
            x_ratio = float(src_width - 1) / (new_width - 1)
            y_ratio = float(src_height - 1) / (new_height - 1)
            # İstenen boyutta sıfırlardan oluşan yeni bir NumPy array oluşturduk
            new_img = np.zeros((new_height, new_width, arraySrc.shape[2]), dtype=np.uint8)
            for i in range(new_height):
                for j in range(new_width):
                    x = int(x_ratio * j)
                    y = int(y_ratio * i)
                    if x >= src_width - 1:
                        x = src_width - 2
                    if y >= src_height - 1:
                        y = src_height - 2
                    x_diff = (x_ratio * j) - x
                    y_diff = (y_ratio * i) - y
                    # Bilinear interpolasyon formülü
                    pixel_value = (1 - x_diff) * (1 - y_diff) * arraySrc[y, x] + \
                                  x_diff * (1 - y_diff) * arraySrc[y, x + 1] + \
                                  (1 - x_diff) * y_diff * arraySrc[y + 1, x] + \
                                  x_diff * y_diff * arraySrc[y + 1, x + 1]
                    new_img[i, j] = pixel_value.astype(np.uint8)
            # Oluşan son matrisi bir değişkene atıp arayüzde görüntüleyebilmek için tekrar PIL türüne çeviriyoruz
            arrayImg = new_img
            self.image = Image.fromarray(arrayImg)
            # Yeni görüntü için PhotoImage nesnesi oluşturuldu
            img_tk = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=img_tk)
            self.gorselKatmani.image = img_tk
            
    def boyutKucultme(self):
        # En Yakın Komşu İnterpolasyonu
        if self.image is not None:
            arraySrc = np.array(self.image)
            src_height, src_width = arraySrc.shape[:2]
            new_width = int(src_width * 0.9)
            new_height = int(src_height * 0.9)
            width_ratio = src_width / new_width
            height_ratio = src_height / new_height
            newImgArray = np.zeros((new_height, new_width, 3), dtype=np.uint8)
            # En yakın komşu interpolasyonu
            for y in range(new_height):
                for x in range(new_width):
                    # Orjinal piksel koordinatlarını hesapla
                    original_x = int(x * width_ratio)
                    original_y = int(y * height_ratio)
                    # Orjinal piksel değerini al ve yeni görüntüye ekle
                    newImgArray[y, x, :] = arraySrc[original_y, original_x, :]
            arrayImg = newImgArray
            self.image = Image.fromarray(arrayImg)
            # Yeni görüntü için PhotoImage nesnesi oluşturuldu
            img_tk = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=img_tk)
            self.gorselKatmani.image = img_tk

    def goruntuDondur(self):
        if self.image is not None:
            arraySrc = np.array(self.image)
            height, width = arraySrc.shape[:2]

            # ilk olarak açıyı radyan cinsine çevirmemiz gerekiyor.
            aci = self.dondurme_slider.get()
            radyan = math.radians(aci)

            # görüntü döndürülünce oluşan yeni yükseklik ve genişlik değerleri
            height_rot_img = round(abs(height * math.cos(radyan))) + \
                             round(abs(width * math.sin(radyan)))
            width_rot_img = round(abs(width * math.cos(radyan))) + \
                            round(abs(height * math.sin(radyan)))

            rotatedImg = np.uint8(np.zeros((height_rot_img, width_rot_img, arraySrc.shape[2])))

            # orjinal resmin merkezini bulma
            cx, cy = (arraySrc.shape[1] // 2, arraySrc.shape[0] // 2)

            # döndürülmüş resmin merkezini bulma
            midx, midy = (width_rot_img // 2, height_rot_img // 2)

            for i in range(rotatedImg.shape[0]):
                for j in range(rotatedImg.shape[1]):
                    x = (i - midx) * math.cos(radyan) + (j - midy) * math.sin(radyan)
                    y = -(i - midx) * math.sin(radyan) + (j - midy) * math.cos(radyan)

                    x = round(x) + cy
                    y = round(y) + cx

                    if (x >= 0 and y >= 0 and x < arraySrc.shape[0] and y < arraySrc.shape[1]):
                        rotatedImg[i, j, :] = arraySrc[x, y, :]

            sonucImg = rotatedImg
            self.image = Image.fromarray(sonucImg)

            # Yeni görüntü için PhotoImage nesnesi oluşturuldu
            img_tk = ImageTk.PhotoImage(self.image)

            self.gorselKatmani.config(image=img_tk)
            self.gorselKatmani.image = img_tk

    def zoomIn(self):
        if self.image is not None:
            arraySrc = np.array(self.image)
            srcCopy = arraySrc.copy()
            # Kaynak görüntü boyutları alındı
            height, width = srcCopy.shape[:2]
            # Görselin ortasından 0.1 oranında bir kesit alıyoruz. Daha sonra bu kesiti boyut büyütme işlemi ile
            # eski görselin yerine koyacağız
            kWidth = int(width - (width * 0.1))
            kHeight = int(height - (height * 0.1))
            kesitArray = np.zeros((kHeight + 1, kWidth + 1, srcCopy.shape[2]), dtype=np.uint8)
            x = 0
            for i in range(0 + int(width * 0.1)//2, width - int(width * 0.1)//2):
                y = 0
                for j in range(0 + int(height * 0.1)//2, height - int(height * 0.1)//2):
                    kesitArray[x, y] = srcCopy[i, j]
                    y += 1
                x += 1
            x_ratio = float(kWidth - 1) / (width - 1)
            y_ratio = float(kHeight - 1) / (height - 1)
            zoomedImgArray = np.zeros((height, width, kesitArray.shape[2]), dtype=np.uint8)
            for i in range(height):
                for j in range(width):
                    x = int(x_ratio * j)
                    y = int(y_ratio * i)
                    if x >= kWidth - 1:
                        x = kWidth - 2
                    if y >= kHeight - 1:
                        y = kHeight - 2
                    x_diff = (x_ratio * j) - x
                    y_diff = (y_ratio * i) - y
                    # Bilinear interpolasyon formülü
                    pixel_value = (1 - x_diff) * (1 - y_diff) * kesitArray[y, x] + \
                                  x_diff * (1 - y_diff) * kesitArray[y, x + 1] + \
                                  (1 - x_diff) * y_diff * kesitArray[y + 1, x] + \
                                  x_diff * y_diff * kesitArray[y + 1, x + 1]
                    zoomedImgArray[i, j] = pixel_value.astype(np.uint8)
            # Oluşan son matrisi arayüzde görüntüleyebilmek için tekrar PIL türüne çeviriyoruz
            self.image = Image.fromarray(zoomedImgArray)
            # Yeni görüntü için PhotoImage nesnesi oluşturuldu
            zoomedImg_tk = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=zoomedImg_tk)
            self.gorselKatmani.image = zoomedImg_tk


class Odev3Arayuz(tk.Toplevel):
    # Ödev 3 ile ilgili işlemlerin yapıldığı class
    def __init__(self, ust_dugme_text, odev_icerik):
        super().__init__()
        self.title(ust_dugme_text + ": " + odev_icerik)
        self.geometry("700x700")

        self.gorselKatmani = tk.Label(self)
        self.gorselKatmani.pack()

        self.textLabel = tk.Label(self, text="")
        self.textLabel.pack(pady=5)

        self.gorselYukleBtn = tk.Button(self, text="Görsel Yükle", command=self.gorselYukle)
        self.gorselYukleBtn.pack(padx=10, pady=20)

        self.cizgiTespitiBtn = tk.Button(self, text="Cizgi Tespiti", command=self.cizgiTespiti)
        self.cizgiTespitiBtn.pack(pady=5)

        self.gozAlgilaBtn = tk.Button(self, text="Göz Algıla", command=self.gozAlgila)
        self.gozAlgilaBtn.pack(pady=5)

        self.koyuYesilAlgilaBtn = tk.Button(self, text="Koyu Yeşil Algıla", command=self.koyuYesilAlgila)
        self.koyuYesilAlgilaBtn.pack(pady=5)

        self.sigmoidContrastBtn = tk.Button(self, text="Sigmoid Contrast", command=self.sigmoidContrast)
        self.sigmoidContrastBtn.pack(pady=5)

        self.shiftedSigmoidContrastBtn = tk.Button(self, text="Shifted Sigmoid Contrast", command=self.shiftedSigmoidContrast)
        self.shiftedSigmoidContrastBtn.pack(pady=5)

        self.strechSteepSigmoidBtn = tk.Button(self, text="Strech Steep Sigmoid", command=self.strechSteepSigmoid)
        self.strechSteepSigmoidBtn.pack(pady=5)


        self.image = None

    def cizgiTespiti(self):
        if self.image is not None:
            arraySrc = np.array(self.image)
            srcCopy = arraySrc.copy()
            gray = cv2.cvtColor(srcCopy, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (3 , 3), 0)
            edges = cv2.Canny(blurred, 75, 250)
            lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=50, maxLineGap=2)
            # PARAMETRELER: 1.Kaynak Görüntü, 2.Polar koordinat sistemindeki p değerini belirler(Büyük küçük çizgilerin algılanması için)
            #               3. theta değeri -> çizginin açısını ifade eder, 4. threshold eşik değeri

            if lines is not None:
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    cv2.line(srcCopy, (x1, y1), (x2, y2), (0, 255, 0), 2)

            self.image = Image.fromarray(srcCopy)
            lastImg = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=lastImg)
            self.gorselKatmani.image = lastImg

    def gozAlgila(self):
        if self.image is not None:
            arraySrc = np.array(self.image)
            srcCopy = arraySrc.copy()
            gray = cv2.cvtColor(srcCopy, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 80, 160)
            edges = cv2.GaussianBlur(edges, (3, 3), 0)
            circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 50, param1=30, param2=48, minRadius=0,
                                       maxRadius=50)
            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                for (x, y, r) in circles:
                    cv2.circle(srcCopy, (x, y), r, (0, 255, 0), 4)

            self.image = Image.fromarray(srcCopy)
            lastImg = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=lastImg)
            self.gorselKatmani.image = lastImg

    def koyuYesilAlgila(self):
        if self.image is not None:
            srcArray = np.array(self.image)
            img = srcArray.copy()
            contoured_img = srcArray.copy()
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            lowerGreen = np.array([50, 138, 90])
            upperGreen = np.array([80, 255, 180])
            mask = cv2.inRange(hsv, lowerGreen, upperGreen)
            blur = cv2.GaussianBlur(mask, (5, 5), 0)
            threshold = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            eroded = cv2.erode(threshold, None, iterations=1)
            dilated = cv2.dilate(eroded, None, iterations=1)
            contours, _ = cv2.findContours(dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            contoured_img = cv2.drawContours(contoured_img, contours, -1, (0, 0, 255), 2)
            contour_data = []
            for contour in contours:
                area = cv2.contourArea(contour)
                cx, cy, cWidth, cHeight = cv2.boundingRect(contour)
                center = f"{cx}, {cy}"
                width = f"{cWidth} px"
                length = f"{len(contour)} px"
                diagonal = f"{int(np.sqrt(cWidth ** 2 + cHeight ** 2))} px"
                energy = 0
                for point in contour:
                    i, j = point[0]
                    pixel_value = gray_img[j, i] ** 2
                    energy += pixel_value
                c_info = {
                    "Center": center,
                    "Length": length,
                    "Width": width,
                    "Diagonal": diagonal,
                    "Energy": energy,
                }
                contour_data.append(c_info)
            df = pd.DataFrame(contour_data)
            excelFile = "contours.xlsx"
            df.to_excel(excelFile, index=True)
            self.textLabel.config(text=f"Algılanan yeşil bölge sayısı: {len(contours)}")
            self.image = Image.fromarray(contoured_img)
            lastImg = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=lastImg)
            self.gorselKatmani.image = lastImg

    def sigmoidContrast(self):
        if self.image is not None:
            arraySrc = np.array(self.image)
            srcCopy = arraySrc.copy()
            alpha = 1
            a = 0.3
            b = 0.7
            for i in range(srcCopy.shape[0]):
                for j in range(srcCopy.shape[1]):
                    pixel_val = srcCopy[i, j] / 255.0
                    transformed_pixel = 255.0 * (1 / (1 + np.exp(-alpha * (pixel_val - a) / (b - a))))
                    srcCopy[i, j] = transformed_pixel
            self.image = Image.fromarray(srcCopy)
            lastImg = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=lastImg)
            self.gorselKatmani.image = lastImg

    def shiftedSigmoidContrast(self):
        if self.image is not None:
            arraySrc = np.array(self.image)
            srcCopy = arraySrc.copy()
            alpha = 1
            a = 0.3
            b = 0.7
            c = 1.5
            for i in range(srcCopy.shape[0]):
                for j in range(srcCopy.shape[1]):
                    pixel_val = srcCopy[i, j] / 255.0
                    transformed_pixel = 255.0 * (1 / (1 + np.exp(-alpha * (pixel_val - a) / (b - a))))
                    transformed_pixel = c * (transformed_pixel - 127) + 127
                    srcCopy[i, j] = transformed_pixel
            self.image = Image.fromarray(srcCopy)
            lastImg = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=lastImg)
            self.gorselKatmani.image = lastImg

    def strechSteepSigmoid(self):
        if self.image is not None:
            arraySrc = np.array(self.image)
            srcCopy = arraySrc.copy()
            rows, cols = srcCopy.shape
            alpha = 1
            a = 0.3
            b = 0.7
            slope = 10.0
            output_img = np.zeros_like(srcCopy, dtype=np.float64)

            for i in range(rows):
                for j in range(cols):
                    pixel_val = srcCopy[i, j] / 255.0
                    transformed_pixel = 255.0 * (1 / (1 + np.exp(-alpha * slope * (pixel_val - a) / (b - a))))
                    output_img[i, j] = transformed_pixel

            output_img = output_img.astype(np.uint8)
            self.image = Image.fromarray(output_img)
            lastImg = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=lastImg)
            self.gorselKatmani.image = lastImg

    def gorselYukle(self):
        file_path = filedialog.askopenfilename(filetypes=[("Resim Dosyaları (JPG/JPEG)", "*.jpg;*.jpeg;")])
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        if self.image is not None:
            img = ImageTk.PhotoImage(self.image)
            self.gorselKatmani.config(image=img)
            self.gorselKatmani.image = img


class AnaSayfa:
    # Uygulama ana ekranı oluşturmamızı ve kontrol etmemizi sağlayan class
    def __init__(self, root):
        # __init__ metodu class'ın constructor metodu olup bu sınıftan bir nesne oluşturulduğunda çalışır.
        self.root = root
        self.root.title("Dijital Görüntü İşleme Ödev Arayüzü")
        self.root.geometry("500x400")

        self.authorFont = tk.font.Font(family="Helvetica", size=12, weight="bold")
        self.authorText = tk.Label(self.root, text="Dijital Görüntü İşleme\nEren GÜNER\n211229049",
                                   font=self.authorFont)
        self.authorText.pack(padx=10, pady=10)

        self.odevler = {
            # Yeni ödevler geldikçe buraya eklenecek.
            # Ödevler sözlük halinde tutuluyor ilk kısım menüde yazan, 2. kısım pencere ismi
            "Ödev 1": "Temel İşlevselliği Oluştur",
            "Ödev 2": "Temel Görüntü Operasyonları ve İnterpolasyon",
            "Ödev 3": "Vize Ödevi"
        }

        self.odevMenu = tk.Menu(self.root, tearoff=0)
        self.root.config(menu=self.odevMenu)

        for odev, icerik in self.odevler.items():
            self.odevMenu.add_command(label=odev, command=lambda o=odev, i=icerik: self.odevAc(o, i))

    def odevAc(self, odev, icerik):
        # Yeni ödevler buraya eklenecek
        if odev == "Ödev 1":
            Odev1Arayuz(odev, icerik)
        elif odev == "Ödev 2":
            Odev2Arayuz(odev, icerik)
        elif odev == "Ödev 3":
            Odev3Arayuz(odev, icerik)
        else:
            messagebox.showinfo("Uyarı", "Bu ödev henüz verilmedi :)")


root = tk.Tk()
AnaSayfa(root)
root.mainloop()
