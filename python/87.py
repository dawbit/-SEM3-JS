import random
def getInt(msg):
“Get some integer”
while True:
try:
n = int(input(msg))
return n
except ValueError:
print(“This is not int, try again.”)

a = getInt(“Min rand: “)
b = getInt(“Max rand: “)
c = getInt(“Matrix X: “)
d = getInt(“Matrix Y: “)

matrix = []
for i in range(0,d):
temp = []
for x in range(0,c):
temp.append(random.randint(a,b))
matrix.append(temp)

for l in matrix:
for u in l:
u = str(u)
while len(u) < 10:
u += ” ”
print(u, end=”)
print()