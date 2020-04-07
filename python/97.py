gender= [‘male’, ‘female’]
color = [‘white’,’black’,’green’,’red’,’blue’]
size = [‘XL’,’L’,’M’,’S’]
i = 0
for s in gender:
for c in color:
for si in size:
fileName = “zad97/wyjsciezadanie97_metka” + str(i) + “.txt”
newFile = open(fileName, ‘w’)
print(“Gender: ” , str(s), file=newFile)
print(“Color: “, str(c), file=newFile)
print(“Size: “, str(si), file=newFile)
newFile.close()
i += 1