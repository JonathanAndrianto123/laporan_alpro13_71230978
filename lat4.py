def jumlah_digit(x) :
    if x == 0 :
        return 0
    else :
        return x % 10 + jumlah_digit(x // 10)

bil = int(input("masukkan bilangan = "))
print(jumlah_digit(bil))