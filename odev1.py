import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ctypes import windll
from tkinter import messagebox
import numpy as np
import cv2


# Bu kod Tkinter penceresinin görüntü kalitesini arttırmaya yarıyor. Yazılar daha net gözüküyor.
windll.shcore.SetProcessDpiAwareness(1)


class Odev1Arayuz(tk.Toplevel):
    # Ödev 1 penceresini açılmasını ve kontrol edilmesini sağlayan class
    def __init__(self, ust_dugme_text, odev_icerik):
        # Ödev 1 constructor metodu
        super().__init__()
        self.title(ust_dugme_text+": "+odev_icerik)
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

        self.metin = tk.Label(self, text="Canny Edge Detection için 2 tane threshold değeri var. Alttaki sürgülerden ayarlanabilir.")
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
        self.title(ust_dugme_text+": "+odev_icerik)
        self.geometry("500x400")

        self.metin = tk.Label(self, text="Bu ödev henüz verilmedi")
        self.metin.pack(padx=10, pady=10)

        self.kapatBtn = tk.Button(self, text="KAPAT", command=self.destroy)
        self.kapatBtn.pack(pady=10, side=tk.BOTTOM)


class AnaSayfa:
    # Uygulama ana ekranı oluşturmamızı ve kontrol etmemizi sağlayan class
    def __init__(self, root):
        # __init__ metodu class'ın constructor metodu olup bu sınıftan bir nesne oluşturulduğunda çalışır.
        self.root = root
        self.root.title("Dijital Görüntü İşleme Ödev Arayüzü")
        self.root.geometry("500x400")

        self.authorFont = tk.font.Font(family="Helvetica", size=12, weight="bold")
        self.authorText = tk.Label(self.root, text="Dijital Görüntü İşleme\nEren GÜNER\n211229049", font=self.authorFont)
        self.authorText.pack(padx=10, pady=10)

        self.odevler = {
            # Yeni ödevler geldikçe buraya eklenecek.
            # Ödevler sözlük halinde tutuluyor ilk kısım menüde yazan, 2. kısım pencere başlığı
            "Ödev 1": "Temel İşlevselliği Oluştur",
            "Ödev 2": "null"
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
        else:
            messagebox.showinfo("Uyarı", "Bu ödev henüz verilmedi :)")


root = tk.Tk()
AnaSayfa(root)
root.mainloop()