def duplikat(buah):
    hasil= []
    for buah in buah:
        hasil.append(buah)
        hasil.append(buah)
    return hasil

fruits = ["pepaya", "mangga", "pisang", "durian", "jambu"]
hasil = duplikat(fruits)
print(hasil)