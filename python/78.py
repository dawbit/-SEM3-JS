vowel = [‘a’,’e’, ‘y’, ‘u’, ‘i’, ‘o’]
newList = []
string = input(“Type your string: “)
for i in string:
if i in vowel:
if i in newList:
pass
else:
newList.append(i)

print(“Vowel in this string: “,newList)
