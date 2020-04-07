file = open(“danezadanie89.txt”, ‘r’)
dec = file.readline()
file.close()
dec = int(dec)
hexa = hex(dec).split(‘x’)[-1]
octa = oct(dec).split(‘o’)[-1]

file = open(“wyjsciezadanie89.txt”, ‘w’)
print(“Dec: “, dec, file=file)
print(“Hex: “, hexa, file=file)
print(“Oct: “, octa, file=file)
file.close()