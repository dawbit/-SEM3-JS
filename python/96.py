while True:
try:
a = int(input(“Give start: “))
b = int(input(“Give end: “))
break
except ValueError:
print(“Wrong values, try again!”)

for i in range(a,b+1):
if (i%4==0 and i%100 != 0) or i%400==0:
print(i, ” is leap year!”)