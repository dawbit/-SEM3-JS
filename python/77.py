myList = []
print(“Make a list. Enter new element or STOP to stop.”)
newElement = None
while newElement != “STOP”:
newElement = input(“New element: “)
myList.append(newElement)
myList.remove(“STOP”)
for e in myList:
print(e)