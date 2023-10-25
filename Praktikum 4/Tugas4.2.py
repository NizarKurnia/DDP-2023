#Laki-laki
#beratL=(tinggi-100)-(tinggi-100)*0.1
#Perempuan
#beratP=(tinggi-100)-(tinggi-100)*0.15

print('''
sistem penghitungan berat badan ideal

pilih jenis kelamin:
1 = laki-laki
2 = perempuan
''')

jk= int(input('masukan pilihan jenis kelamin:'))
tinggi = int(input('masukan tinggi badan:'))

match jk:
    case 1:
        ideal=(tinggi-100)-(tinggi-100)*0.1
        print('berat badan ideal laki-laki untuk tinggi', tinggi, 'adalah', ideal)
    case 2:
        ideal=(tinggi-100)-(tinggi-100)*0.15
        print('berat badan ideal perempuan untuk tinggi', tinggi, 'adalah', ideal)
    case _:
        print('pilihan yang anda masukan tidak valid')