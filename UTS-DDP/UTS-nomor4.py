#Pseudocode Luas dan Keliling layang-layang
print(''' 
menghitung layang-layang
1 = luas layang-layang
2 = keliling layang-layang
      ''')

luasdankeliling =int(input('Keliling apa Luas?'))

match luasdankeliling:
    case 1:
        diagonal_1 =int(input("Masukkan Nilai Sisi Diagonal 1: "))
        diagonal_2 =int(input("Masukkan Nilai Sisi Diagonal 2: "))
        luas =int(1.2*diagonal_1 * diagonal_2) 
        print('Luas layang-layang adalah',luas)
    case 2:
        panjang =int(input("Masukkan Nilai Panjang: "))
        lebar =int(input("Masukkan Nilai Lebar: "))
        keliling=int(2 * panjang)+(2 * lebar)
        print('Keliling layang-layang adalah',keliling)
    case _:
        print('salah pilih')