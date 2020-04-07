def get_number(msg):
“Get and check number”
while True:
try:
n = input(msg)
try:
n = int(n)
print(n, ” is integer”)
break
except ValueError:
pass
try:
n = float(n)
print(n, ” is real”)
break
except ValueError:
print(“This is not number, try again!”)
except ValueError:
pass

x = get_number(“Give number!”)