while True:
try:
i = int(input(“Number: “))
break
except ValueError:
print(“This is not int. Try again!”)

n = 1
result = 1
while n <= i:
result *= n
n += 1

print(i,”! = “,result)