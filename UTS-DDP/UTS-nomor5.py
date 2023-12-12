#Kalkulator Sederhana
angka1=int(input("Masukkan angka 1: "))
angka2=int(input("Masukkan angka 2: "))

print(''' 
menghitung layang-layang
1 = +(Tambah)
2 = -(Kurang)
3 = *(Kali)
4 = /(Bagi)
5 = **(Pangkat)
      ''')
Kalkulator =int(input('Pilih yang mana?'))

match Kalkulator:
    case 1:
        tambah=int(angka1 + angka2) 
        print('Hasil dari',angka1, 'Tambah' ,angka2,'adalah',tambah)
    case 2:
        kurang=int(angka1 - angka2)   
        print('Hasil dari',angka1, 'Kurang' ,angka2,'adalah',kurang)
    case 3:
        kali=int(angka1 * angka2)   
        print('Hasil dari',angka1, 'Kali' ,angka2,'adalah',kali)
    case 4:
        bagi=int(angka1 / angka2)   
        print('Hasil dari',angka1, 'Bagi' ,angka2,'adalah',bagi)
    case 5:
        pangkat=int(angka1 ** angka2)   
        print('Hasil dari',angka1, 'Pangkat' ,angka2,'adalah',pangkat)
    case _:
        print('salah pilih')