# class
class Orang:
    # properti
    nama = ""
    umur = ""

    # method
    def _init_(self, name, age):
        self.nama = name
        self.umur = age
    
    def bernafas(self):
        print("saya bisa bernafas")

    # method
    def berjalan(self):
        print("Saya bisa berjalan")

# Object
mahasiswa = Orang()
print(mahasiswa.nama)
print(mahasiswa.umur)
mahasiswa.berjalan()

# Object 2


