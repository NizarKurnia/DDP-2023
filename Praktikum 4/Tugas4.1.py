print(''' 
menghitung luas bangun datar
1 = luas persegi
2 = luas lingkaran
3 = luas segitiga
      ''')

Luasbangundatar =int(input('Apakah luas bangun datar ini?'))

match Luasbangundatar:
    case 1:
        sisi=int(input('masukan sisi:'))
        persegi=int(sisi*sisi*sisi)
        print('luas persegi untuk',sisi,'adalah',persegi)
    case 2:
        jarijari=int(input('masukan jarijari:'))
        lingkaran=int(3,14*jarijari*jarijari)
        print('luas lingkaran',jarijari,'adalah',lingkaran)
    case 3:
        alas=int(input('masukan alas:'))
        tinggi=int(input('masukan tinggi:'))
        segitiga=int(1.2*alas*tinggi)
        print('luas segitiga',alas,'dan tinggi',tinggi,'adalah',segitiga)
    case _:
        print('salah pilih')