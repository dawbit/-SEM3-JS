def Cezar(T, k):
    n = len(T)
    nowy = ""
    for i in range(n):
        nowy += chr((ord(T[i])+k)%256)
    return nowy

def InverseCezar(Z, k): #Zaszyfrowany i klucz
    nowy = ""
    for i in Z:
        nowy += chr((ord(i)-k)%256)
    return nowy

print(Cezar("Seminarium dyplomowe", 3))
print(InverseCezar("Vhplqdulxp#g|sorprzh", 3))