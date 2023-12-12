def persegi(sisi):
    luas= sisi * sisi
    keliling= 4 * sisi
    print("Luas Persegi", luas)
    print("Keliling Persegi", keliling)

def persegi_panjang(panjang, lebar):
    luas= panjang * lebar
    keliling= 2 * (panjang + lebar)
    print("Luas Persegi Panjang", luas)
    print("Keliling Persegi Panjang", keliling)

def lingkaran(jari2):
    pi= 3.14

    luas= pi * jari2 * jari2
    keliling= 2 * pi * jari2
    print("Luas Lingkaran", luas)
    print("Keliling Lingkaran", keliling)
    
def segitiga_sama_sisi(alas, tinggi):
    luas= 1.2 * alas * tinggi
    keliling= alas * 3
    print("Luas Segitiga sama sisi", luas)
    print("Keliling Segitiga sama sisi", keliling)

def belah_ketupat(d1, d2, sisi):
    luas= 0.5 * d1 * d2
    keliling= 4 * sisi
    print("Luas Belah Ketupat", luas)
    print("Keliling Belah Ketupat", keliling)

def layang_layang(d1, d2, sisia, sisib):
    luas= d1 * d2 * 0.5
    keliling= (sisia * 2) + (sisib * 2)
    print("Luas Layang-Layang", luas)
    print("Keliling Layang-Layang", keliling)

def jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling = 2 * alas + sisi_miring
    print("Luas Jajar Genjang: ", luas)
    print("Keliling Jajar Genjang: ", keliling)

