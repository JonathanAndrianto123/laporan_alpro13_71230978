def deret_ganjil(x):
    if x <= 0:
        return 0
    else:
        return (2 * x - 1) + deret_ganjil(x - 1)

bil = int(input("masukkan bilangan = "))
print(deret_ganjil(bil))