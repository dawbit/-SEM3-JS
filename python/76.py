

while True:
try:
n = int(input(“Give number: “))
break
except ValueError as err:
print(err)

if(n > 0):
print(“N is bigger than 0”)
elif(n < 0):
print(“N is smaller than 0”)
else:
print(“N is equal to 0”)
