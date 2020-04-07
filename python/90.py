import math
def get_Int(msg):
while True:
try:
x = int(input(msg))
return x
break
except ValueError:
print(“Wrogn. Try again.”)

def product(n,a):
i = 0
result = 1
while i < a:
result = result * (n-i)
i += 1
return result

def a():
print(“sin alfa +- sin beta”)
alfa = get_Int(“Give Alpha: “)
beta = get_Int(“Give Beta: “)
result = 2*math.sin(1/2*(alfa+beta))*math.cos(1/2*(alfa-beta))
print(“Sin(“,alfa,”)+sin(“,beta,”) = “, result)

def b():
print(“(1+x)^n”)
x = get_Int(“Give X: “)
n = get_Int(“Give N: “)
result = 1
for a in range(1, n+1):
result = result + (product(n,a)*x**a)/math.factorial(a)
print(“1+x^n = “, result)

def c():
print(“quadratic equation”)
a = get_Int(“Give a: “)
b = get_Int(“Give b: “)
c = get_Int(“Give c: “)
delta = b**2 – 4*a*c
if delta > 0:
x1 = (-b + math.sqrt(delta))/(2*a)
x2 = (-b – math.sqrt(delta))/(2*a)
print(“x1 = “, x1)
print(“x2 = “, x2)
elif delta == 0:
x0 = -b/(2*a)
print(“x0 = “, x0)
else:
print(“Not real result.”)

def d():
print(“e^x approximation with Taylor series”)
x = get_Int(“Give x: “)
result = 1
for i in range(1, 1000):
result = result + (x**i)/math.factorial(i)
print(“e^”, x, ” = “, result)

a()
b()
c()
d()