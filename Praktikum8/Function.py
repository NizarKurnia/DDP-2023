def hello():
    print("hallo semua")

hello()
hello()

def say(nama, prodi):
    print("hello nama saya adalah", nama)
    print("program studi saya adalah", prodi)
say("tono", "TI")

def jumlah(no1, no2):
    aa = no1+no2
    print(aa)

jumlah(3,5)

def dia(*nama):
    print("hayuk",+nama[2])
dia("dodo","bobo")

def my(x):
    return x*2
print(my(4))

def h(sisi):
    luas= sisi*sisi
    return luas
print(h(6))

def p(a,b):
    return a**b
print(2,3)

def angka_ganjil(*angka):
        for i in angka:
                if i % 2==1:
                        print("angka ganjil nya: ", i)
                        return
angka_ganjil (2,344,544,666,244,886,542,13,788,111,567)