import tkinter as tk
from tkinter import messagebox

class OdevTakipArayuzu:
    def __init__(self, root):
        self.root = root
        self.root.title("Ödev Takip")

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.odev_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Ödevler", menu=self.odev_menu)
        self.odev_menu.add_command(label="Ödev 1", command=self.odev1_ac)

    def odev1_ac(self):
        odev1_pencere = tk.Toplevel(self.root)
        odev1_pencere.title("Ödev 1")

        # Ödev 1 arayüzü içeriği burada eklenecek
        label = tk.Label(odev1_pencere, text="Ödev 1 İçeriği")
        label.pack(padx=10, pady=10)

# Ana uygulama penceresi
root = tk.Tk()
uygulama = OdevTakipArayuzu(root)
root.mainloop()
