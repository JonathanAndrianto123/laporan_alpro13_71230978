def kombinasi(x, y):
    if y == 0 or x == y :
        return 1
    else :
        return kombinasi(x - 1, y - 1) + kombinasi(x - 1, y)
    
bil1 = int(input("masukkan bilangan 1 = "))
bil2 = int(input("masukkan bilangan 2 = "))
print(kombinasi(bil1, bil2))