import tkinter as tk
from tkinter import messagebox

class OdevTakipArayuzu:
    def __init__(self, root):
        self.root = root
        self.root.title("Ödev Takip")

        self.ana_ekran()

    def ana_ekran(self):
        self.odev_icerikleri = {
            "Ödev 1": "Ödev 1 İçeriği",
            # Buraya ek ödevleri ekleyebilirsiniz.
        }

        self.odev_menu = tk.Menu(self.root, tearoff=0)
        self.root.config(menu=self.odev_menu)

        for odev, icerik in self.odev_icerikleri.items():
            self.odev_menu.add_command(label=odev, command=lambda o=odev, i=icerik: self.odev_ac(o, i))

        self.odev_aciklama = tk.StringVar()
        self.odev_aciklama.set("Burada ödev açıklaması gösterilecek.")

        self.odev_aciklama_etiket = tk.Label(self.root, textvariable=self.odev_aciklama)
        self.odev_aciklama_etiket.pack(padx=10, pady=10)

        self.geri_don_button = tk.Button(self.root, text="Geri Dön", command=self.ana_ekrana_don)
        self.geri_don_button.pack(pady=10)

        # Geri dön butonunu başlangıçta gizle
        self.geri_don_button.pack_forget()
        self.geri_don_goster = False

    def odev_ac(self, odev, icerik):
        self.odev_aciklama.set(icerik)

        # Ödev penceresi açıldığında geri dön butonunu göster
        if not self.geri_don_goster:
            self.geri_don_button.pack()
            self.geri_don_goster = True

    def ana_ekrana_don(self):
        # Geri dön butonunu gizle
        self.geri_don_button.pack_forget()
        self.geri_don_goster = False

        # Ana ekrana dön
        self.odev_aciklama_etiket.pack_forget()
        self.ana_ekran()

# Ana uygulama penceresi
root = tk.Tk()
uygulama = OdevTakipArayuzu(root)
root.mainloop()
