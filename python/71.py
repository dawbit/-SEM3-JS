while True:
try:
n = input(“Podaj n:”)
n = int(n)
break
except ValueError as err:
print(err)
string = “-0.7e+4.07”
space = “@”
for i in range(1,n+1):
if i != 1:
print(space, string, end=”)
else:
print(string, end=”)
