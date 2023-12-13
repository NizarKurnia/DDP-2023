class gempa:
    lokasi =""
    skala = 0

    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
        
    def dampak(self):
        if self.skala < 2:
             print (f"Dampak gempa di {self.lokasi} : tidak terasa")
        elif 2 <= self.skala < 4:
             print (f"Dampak gempa di {self.lokasi} : Bangunan retak-retak")
        elif 4 <= self.skala < 6:
             print (f"Dampak gempa di {self.lokasi} : Bangunan roboh")
        elif self.skala >= 6:
             print (f"Dampak gempa di {self.lokasi} : Bangunan roboh dan berpotensi tsunami")
        else:
             print ("Skala gempa di  tidak valid")


lokasi1 = gempa("Banten", 1.2)
lokasi2 = gempa("Palu", 6.1)
lokasi3 = gempa("Cianjur", 5.6)
lokasi4 = gempa("Jayapura", 3.3)
lokasi5 = gempa("Garut", 4.0)

