nilai=int(input("Masukan Nilai: "))
def kelulusan(nilai):
    if nilai < 0:
        return "Hadeh..."
    elif nilai <= 60:
        return "Siap-siap aja pas dirumah"
    elif nilai <= 70:
        return "Okelah"
    elif nilai <= 80:
        return "NICE!!!"
    elif nilai <= 100:
        return "SIPPP!!!!"
    else:
        return "Nilai tidak valid"
    
print(kelulusan(nilai))