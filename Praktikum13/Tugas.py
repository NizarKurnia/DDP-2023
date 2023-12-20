class Binatang:
    def __init__(self, nama, makanan, habitat, kembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.kembangbiak = kembangbiak

    def info(self):
        print("nama\t:", self.nama)
        print("makanan\t:", self.makanan)
        print("habitat\t:", self.habitat)
        print("berkembangbiak\t:", self.kembangbiak)
 
class Singa(Binatang):
    def __init__(self, nama, habitat):
        super().__init__(nama, "daging", habitat, "melahirkan")

    def menerkam(self):
        print(self.nama, "menerkam mangsa")
        print("======================")


class Ayam(Binatang):
    def __init__(self, nama, habitat):
        super().__init__(nama, "beras", habitat, "bertelur")

    def matok(self):
        print(self.nama, "matok orang")
        print("======================")


class Elang(Binatang):
    def __init__(self, nama, habitat):
        super().__init__(nama, "hewan kecil", habitat, "bertelur")

    def terbang(self):
        print(self.nama, "terbang dengan cepat")
        print("======================")


# Pemanggilan
singa = Singa("singa afrika", "padang rumput")
ayam = Ayam("ayam hitam", "kandang")
elang = Elang("elang botak", "puncak")

singa.info()
singa.menerkam()

ayam.info()
ayam.matok()

elang.info()
elang.terbang()