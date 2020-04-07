

zero = [‘*****’,’* *’,’* *’,’* *’,’* *’,’* *’,’*****’]
one = [‘ * ‘,’ ** ‘,’* * ‘,’ * ‘,’ * ‘,’ * ‘,’*****’]
two = [‘ *** ‘,’* *’,’ * ‘,’ * ‘,’ * ‘,’* ‘,’*****’]
three = [‘*****’,’ *’,’ *’,’*****’,’ *’,’ *’,’*****’]
four = [‘ ** ‘,’ * * ‘,’* * ‘,’*****’,’ * ‘,’ * ‘,’ * ‘]
five = [‘*****’,’* ‘,’* ‘,’*****’,’ *’,’ *’,’*****’]
six = [‘*****’,’* ‘,’* ‘,’*****’,’* *’,’* *’,’*****’]
seven = [‘*****’,’ *’,’ * ‘,’ * ‘,’ * ‘,’* ‘,’* ‘]
eight = [‘*****’,’* *’,’* *’,’*****’,’* *’,’* *’,’*****’]
nine = [‘*****’,’* *’,’* *’,’*****’,’ *’,’ *’,’*****’]
numbers = [zero,one,two,three,four,five,six,seven,eight,nine]
while True:
try:
n = int(input(“Give number: “))
break
except ValueError:
print(“This is not number. Try again!”)
n = str(n)
toPrint = []
for u in n:
toPrint.append(numbers[int(u)])

file = open(“zad086out.txt”,’w’)
for i in range(0,7):
for x in toPrint:
print(x[i], ” “, end=”, file=file)

print(file=file)
file.close()
