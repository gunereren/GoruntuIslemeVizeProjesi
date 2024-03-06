import tkinter as tk
from tkinter import messagebox

class Odev1Arayuzu(tk.Toplevel):
    def __init__(self, ust_dugme_text, odev_icerik):
        super().__init__()

        self.title(ust_dugme_text)

        self.odev_icerik = odev_icerik

        self.label = tk.Label(self, text=self.odev_icerik)
        self.label.pack(padx=10, pady=10)

        self.geri_don_button = tk.Button(self, text="Geri Dön", command=self.destroy)
        self.geri_don_button.pack(pady=10)

class Odev2Arayuzu(tk.Toplevel):
    def __init__(self, ust_dugme_text, odev_icerik):
        super().__init__()

        self.title(ust_dugme_text)

        # Odev2'nin özel işlevselliği burada eklenebilir

        self.label = tk.Label(self, text=odev_icerik)
        self.label.pack(padx=10, pady=10)

        self.geri_don_button = tk.Button(self, text="Geri Dön", command=self.destroy)
        self.geri_don_button.pack(pady=10)

class OdevTakipArayuzu:
    def __init__(self, root):
        self.root = root
        self.root.title("Ödev Takip")

        self.odevler = {
            "Ödev 1": "Ödev 1 İçeriği",
            "Ödev 2": "Ödev 2 İçeriği",
            # Buraya ek ödevleri ekleyebilirsiniz.
        }

        self.odev_menu = tk.Menu(self.root, tearoff=0)
        self.root.config(menu=self.odev_menu)

        for odev in self.odevler:
            self.odev_menu.add_command(label=odev, command=lambda o=odev: self.odev_ac(o))

    def odev_ac(self, odev):
        icerik = self.odevler.get(odev, "Ödev içeriği bulunamadı.")

        if odev == "Ödev 1":
            Odev1Arayuzu(odev, icerik)
        elif odev == "Ödev 2":
            Odev2Arayuzu(odev, icerik)
        # Buraya ek ödevler için sınıfları ekleyebilirsiniz.
        else:
            messagebox.showinfo("Uyarı", "Bu ödev için özel sınıf bulunamadı.")

# Ana uygulama penceresi
root = tk.Tk()
uygulama = OdevTakipArayuzu(root)
root.mainloop()
