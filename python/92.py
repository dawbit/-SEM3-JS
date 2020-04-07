file = open(“danezadanie92.txt”, ‘r’)
txt = file.read()
words = []
counter = []
word = []
string = “”
for i in txt:
if i!=’ ‘:
word.append(i)
else:
for x in word:
string += str(x)
if string in words:
counter[words.index(string)] += 1
else:
words.append(string)
counter.append(1)
string = “”
word = []
if len(word) > 0:
for x in word:
string += str(x)
if string in words:
counter[words.index(string)] += 1
else:
words.append(string)
counter.append(1)
string = “”
word = []

for i in range(0,len(words)):
print(words[i], ” : “, counter[i])