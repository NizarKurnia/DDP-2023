Luasbangundatar =int(input('Apakah luas bangun datar ini?'))

match Luasbangundatar:
    case 1:
        print('maka menghitung luas persegi')
    case 2:
        print('maka menghitung luas lingkaran')
    case 3:
        print('maka menghitung luas segitiga')
    case _:
        print('maka menghitung luas persegi panjang')