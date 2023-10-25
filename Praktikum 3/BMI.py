tinggi=int(input('masukan tinggi badan anda:'))

#Laki-laki
beratL=(tinggi-100)-(tinggi-100)*0.1
#Perempuan
beratP=(tinggi-100)-(tinggi-100)*0.15

print('Berat badan ideal laki-laki:',beratL,'kg')
print('Berat badan ideal perempuan:',beratP,'kg')

