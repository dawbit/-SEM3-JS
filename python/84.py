import random
with open(‘zad084lista.txt’) as f:
listFromFile = (f.read().splitlines())

print(listFromFile)

x = random.randint(0,99)
r = random.choice(listFromFile)

file = open(“wynikzadanie84.txt”, ‘w’)
print(x, file=file)
print(r, file=file)
file.close()
