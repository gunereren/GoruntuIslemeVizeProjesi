import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ctypes import windll


# Bu kod Tkinter penceresinin görüntü kalitesini arttırmaya yarıyor. Yazılar daha net gözüküyor.
windll.shcore.SetProcessDpiAwareness(1)


class odevClass:
    def __init__(self, odevWindow):
        print("Constructor")



class MasterClass:
    def __init__(self, master):
        # __init__ metodu class'ın constructor metodu olup bu sınıftan bir nesne oluşturulduğunda çalışır.
        self.master = master
        self.master.title("Dijital Görüntü İşleme Ödev Arayüzü")
        self.master.geometry("700x500")

        self.mainMenu = tk.Menu(self.master)
        self.master.config(menu=self.mainMenu)

        self.odevMenu = tk.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Ödevler", menu=self.odevMenu)
        self.odevMenu.add_command(label="Ödev 1: Temel İşlevselliği Oluştur", command=self.odev1)
        self.mainMenu.add_separator()
        self.mainMenu.add_command(label="ÇIKIŞ", command=master.destroy)

        self.authorFont = tk.font.Font(family="Helvetica", size=11)
        self.author = tk.Label(self.master, text="Eren GÜNER - 211229049 - Görüntü İşleme", font=self.authorFont)
        self.author.pack(side=tk.BOTTOM, padx=10, pady=10)

    def odev1(self):
        odev1Frame = tk.Toplevel(self.master)
        odev1Frame.title("Ödev 1: Temel İşlevselliği Oluşturma")
        odev1Frame.geometry("700x500")

        odev1Header = tk.Label(odev1Frame, text="Ödev 1: Temel İşlevselliği Oluşturma")
        odev1Header.pack(side=tk.TOP)

        odev1ImageLabel = tk.Label(odev1Frame)
        odev1ImageLabel.pack()

        image = None

        gorselYukleBtn = tk.Button(odev1Frame, text="Görsel Yükle")
        gorselYukleBtn.pack()

    def gorselYukle(self):
        filePath = filedialog.askopenfilename(filetypes=[("Resim Dosyaları", "*.png;*.jpg;*.jpeg;*.gif")])
        if filePath:

            image = Image.open(filePath)






def main():
    root = tk.Tk()
    MasterClass(root)
    root.mainloop()


if __name__ == "__main__":
    main()
