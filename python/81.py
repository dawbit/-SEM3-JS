numberList = []
sumNumber = 0
mediana = None
average = None
try:
file = open(‘zad081.txt’, ‘r’)
except:
print(“Failed to open file”)

for line in file:
numberList.append(int(line))

file.close()
sumNumber = sum(numberList)
average = sumNumber/len(numberList)
sortedList = sorted(numberList)
if len(sortedList) %2 == 0:
mediana = (sortedList[int(len(sortedList)/2)-1] + sortedList[int((len(sortedList)/2))])/2
else:
mediana = sortedList[int((len(sortedList))/2)]

print(“List: “, numberList)
print(“Sorted List: “, sortedList)
print(“Average: “, average)
print(“Sum: “, sumNumber)
print(“Mediana: “, mediana)
4
5
3
1
2
