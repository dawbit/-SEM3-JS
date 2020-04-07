

numberList = []
sumNumber = 0
mediana = None
average = None
print(“Give a number, type something else to stop.”)
while True:
try:
n = int(input(“Give new number: “))
sumNumber += n
numberList.append(n)
except ValueError:
break
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
