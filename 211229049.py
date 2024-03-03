import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ctypes import windll


# Bu kod Tkinter penceresinin görüntü kalitesini arttırmaya yarıyor. Yazılar daha net gözüküyor.
windll.shcore.SetProcessDpiAwareness(1)


class OdevTakipArayuzu:
    def __init__(self, root):
        # __init__ metodu class'ın constructor metodu olup bu sınıftan bir nesne oluşturulduğunda çalışır.
        self.root = root
        self.root.title("Dijital Görüntü İşleme Ödev Arayüzü")
        self.root.geometry("400x300")

        self.ana_ekran()

    def ana_ekran(self):
        self.odevler = {
            # Yeni ödevler geldikçe buraya eklenecek. Ödevler sözlük halinde tutuluyor ilk kısım menü, 2. kısım açıklama
            "Ödev 1: Temel İşevselliği Oluşturma": "Threshold İşlemi"
        }

        self.odevMenu = tk.Menu(self.root, tearoff=0)
        self.root.config(menu=self.odevMenu)

        for odev, icerik in self.odevler.items():
            self.odevMenu.add_command(label=odev, command=lambda o=odev, i=icerik: self.odevAc(o, i))

        self.authorFont = tk.font.Font(family="Helvetica", size=11, weight="bold")

        self.mainText = tk.StringVar()
        self.mainText.set("Dijital Görüntü İşleme\nEren GÜNER\n211229049")

        self.mainTextEtiket = tk.Label(self.root, textvariable=self.mainText, font=self.authorFont)
        self.mainTextEtiket.pack(padx=10, pady=10)

        self.geri_don_button = tk.Button(self.root, text="Geri Dön", command=self.ana_ekrana_don)
        self.geri_don_button.pack(pady=10)

        # Geri dön butonunu başlangıçta gizle
        self.geri_don_button.pack_forget()
        self.geri_don_goster = False

    def odevAc(self, odev, icerik):
        self.mainText.set(icerik)

        # Ödev penceresi açıldığında geri dön butonunu göster
        if not self.geri_don_goster:
            self.geri_don_button.pack()
            self.geri_don_goster = True

    def ana_ekrana_don(self):
        # Geri dön butonunu gizle
        self.geri_don_button.pack_forget()
        self.geri_don_goster = False

        # Ana ekrana dön
        self.mainTextEtiket.pack_forget()
        self.ana_ekran()

        # self.mainMenu = tk.Menu(self.root)
        # self.root.config(menu=self.mainMenu)
        #
        # self.odevMenu = tk.Menu(self.mainMenu, tearoff=0)
        # self.mainMenu.add_cascade(label="Ödevler", menu=self.odevMenu)
        # self.odevMenu.add_command(label="Ödev 1: Temel İşlevselliği Oluştur", command=self.odev1)
        # self.mainMenu.add_separator()
        # self.mainMenu.add_command(label="ÇIKIŞ", command=root.destroy)
        #
        # self.authorFont = tk.font.Font(family="Helvetica", size=11)
        # self.author = tk.Label(self.root, text="Eren GÜNER - 211229049 - Görüntü İşleme", font=self.authorFont)
        # self.author.pack(side=tk.BOTTOM, padx=10, pady=10)

    # def odev1(self):
    #     odev1Frame = tk.Toplevel(self.root)
    #     odev1Frame.title("Ödev 1: Temel İşlevselliği Oluşturma")
    #     odev1Frame.geometry("700x500")
    #
    #     odev1Header = tk.Label(odev1Frame, text="Ödev 1: Temel İşlevselliği Oluşturma")
    #     odev1Header.pack(side=tk.TOP)
    #
    #     odev1ImageLabel = tk.Label(odev1Frame)
    #     odev1ImageLabel.pack()
    #
    #     image = None
    #
    #     gorselYukleBtn = tk.Button(odev1Frame, text="Görsel Yükle")
    #     gorselYukleBtn.pack()

    # def gorselYukle(self):
    #     filePath = filedialog.askopenfilename(filetypes=[("Resim Dosyaları", "*.png;*.jpg;*.jpeg;*.gif")])
    #     if filePath:
    #
    #         image = Image.open(filePath)


root = tk.Tk()
OdevTakipArayuzu(root)
root.mainloop()
