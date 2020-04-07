file = open(“danezadanie91.txt”, ‘r’)
txt = file.read()
chars = []
counter = []
for x in txt:
if x in chars:
counter[chars.index(x)] += 1
else:
chars.append(x)
counter.append(int(1))

for i in range(0,len(chars)):
print(chars[i], ” : “, counter[i])