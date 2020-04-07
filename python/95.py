import math
import cmath
inputFile = open(“danezadanie95.txt”,’r’)
x = []
for line in inputFile:
x.append(int(line.strip(“\n”)))

a = x[0]
b = x[1]
c = x[2]
x0 = None
x1 = None
x2 = None
sqrDelta = None
delta = b*b -4*a*c
if delta == 0:
x0 = -b/(2*a)
print(“Real result: “, x0)
elif delta > 0:
x1 = (-b+math.sqrt(delta))/(2*a)
x2 = (-b-math.sqrt(delta))/(2*a)
print(“Real result: “, x1, ” and “, x2)
else:
sqrDelta = complex(0,math.sqrt((-1)*delta))
x1 = (-b+sqrDelta)/(2*a)
x2 = (-b-sqrDelta)/(2*a)
print(“Complex result: “, x1, ” and “, x2)
