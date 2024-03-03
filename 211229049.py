import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ctypes import windll
from tkinter import messagebox


# Bu kod Tkinter penceresinin görüntü kalitesini arttırmaya yarıyor. Yazılar daha net gözüküyor.
windll.shcore.SetProcessDpiAwareness(1)


class Odev1Arayuz(tk.Toplevel):
    def __init__(self, ust_dugme_text, odev_icerik):
        super().__init__()
        self.title(ust_dugme_text+": "+odev_icerik)
        self.geometry("500x400")
        self.odev_icerik = odev_icerik

        self.metin = tk.Label(self, text="Threshold yapılabilir")
        self.metin.pack(padx=10, pady=10)

        self.kapatBtn = tk.Button(self, text="KAPAT", command=self.destroy)
        self.kapatBtn.pack(pady=10, side=tk.BOTTOM)


class Odev2Arayuz(tk.Toplevel):
    def __init__(self, ust_dugme_text, odev_icerik):
        super().__init__()
        self.title(ust_dugme_text+": "+odev_icerik)
        self.geometry("500x400")

        self.metin = tk.Label(self, text="Bu ödev henüz verilmedi")
        self.metin.pack(padx=10, pady=10)

        self.kapatBtn = tk.Button(self, text="KAPAT", command=self.destroy)
        self.kapatBtn.pack(pady=10, side=tk.BOTTOM)


class AnaSayfa:
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
