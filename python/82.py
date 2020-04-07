def get_int(msg):
“This function get some number from user.”
while True:
try:
n = int(input(msg))
return n
except ValueError:
print(“This is not number. Try again”)

x = get_int(“Give number: “)
print(“Your number: “, x)