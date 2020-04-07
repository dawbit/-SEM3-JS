while True:
try:
n = int(input(“Give number: “))
break
except ValueError:
print(“This is not a number, try again!”)
print(n, ” is correct!”)