def Silnia(z):
    if z < 2:
        return 1
    else:
        return z*Silnia(z-1)
