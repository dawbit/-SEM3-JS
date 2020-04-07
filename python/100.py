import timeit

def bubbleSort(itemList):
for i in range(0,len(itemList)-1):
for j in range(0,len(itemList)-1):
if itemList[j] > itemList[j+1]:
temp = itemList[j]
itemList[j] = itemList[j+1]
itemList[j+1] = temp
return itemList
def insertionSort(itemList):
for i in range(0,len(itemList)-1):
for j in range(i+1,len(itemList)):
if itemList[i] > itemList[j]:
temp = itemList[i]
itemList[i] = itemList[j]
itemList[j] = temp
return itemList
def partition(itemList,begin,end):
pivot = itemList[end]
index = end
i = begin
while True:
if itemList[i] <= pivot:
if i >= index -1:
return index
i += 1

else:
itemList.insert(end+1,itemList[i])
itemList.pop(i)
index -= 1

def quickSort(itemList,begin,end):
if begin < end:
index = partition(itemList,begin,end)
quickSort(itemList,begin,index-1)
quickSort(itemList,index+1,end)
else:
return itemList
return itemList

inputFile = open(“danezadanie99.txt”, ‘r’)
listToSort = []
for line in inputFile:
listToSort.append(line.strip(‘\n’))
toBubble = list(listToSort)
toInsertion = list(listToSort)
toQuick = list(listToSort)
quickTime = timeit.default_timer()
file = open(“quickSort.txt”, ‘w’)
quickTime = timeit.default_timer() – quickTime
print(quickSort(toQuick,0,len(toQuick)-1),file=file)
file.close()
print(“Quick Time: “, quickTime)
file = open(“bubbleSort.txt”, ‘w’)
bubbleTime = timeit.default_timer()
print(bubbleSort(toBubble), file=file)
bubbleTime = timeit.default_timer() – bubbleTime
file.close()
print(“Bubble Time: “, bubbleTime)
file = open(“insertionSort.txt”, ‘w’)
insertTime = timeit.default_timer()
print(insertionSort(toInsertion), file=file)
insertTime = timeit.default_timer() – insertTime
file.close()
print(“Insertion Time: “, insertTime)

file = open(“raport100.txt”, ‘w’)
print(“RAPORT ALGORYTMOW SORTOWANIA:”, file=file)
print(“SORTOWANIE: LICZBA SORTOWANYCH LICZB: CZAS: “, file=file)
print(“Babelkowe: “,len(listToSort),” “, bubbleTime, file=file)
print(“Wstawianie: “,len(listToSort),” “, insertTime, file=file)
print(“Szybkie: “,len(listToSort),” “, quickTime, file=file)
file.close()