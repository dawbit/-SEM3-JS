lista = [‘element1’, ‘element2’, ‘element3’]
lista2 = [‘element4’, ‘element5’, ‘element6’]
listalist = [lista,lista2]
elem = input(“What to search?: “)
for l in listalist:
if elem in l:
print(elem, ” is in “, l)
break
else:
print(elem, “is not in”, l)