def palindrom(kalimat):
    if len(kalimat) < 2:
        return True
    elif kalimat[0] == kalimat[-1]:
        return palindrom(kalimat[1:-1])
    return False

kal = input("masukkan kalimat = ")
kal = kal.replace(' ', '').lower()
if palindrom(kal) :
    print("kalimat tersebut palindrom")
else :
    print("kalimat tersebut bukan palindrom")