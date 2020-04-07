

lista = [‘element’, 23, ‘test’]
lista .append(“e1”)
lista .append(3)

lista2 = ['element','element1', 'element2']
lista2.append('element3')
lista2.extend([‘elem4’, 32, 3.6, “xD”])
print(“lista \t\t lista2 “)
for i in range(0, max(len(lista),len(lista2))):
if i < len(lista):
print(lista[i], end=”)
print(“\t\t”, end=”)
if i < len(lista2):
print(lista2[i])
