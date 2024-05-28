def prima(bil, x = 2):
    if bil == 2 :
        return True
    elif bil < 2 or bil % x == 0 :
        return False
    elif x * x > bil :
        return True
    else:
        return prima(bil, x + 1)

n = int(input("masukkan bilangan = "))
if prima(n):
    print(f"{n} adalah bilangan prima")
else:
    print(f"{n} bukan bilangan prima")