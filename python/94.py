

while True:
try:
counter = int(input(“Give counter: “))
increment = int(input(“Give incrementation: “))
break
except ValueError:
print(“Something went wrong, try again!”)

ex = [[”,’*****’],[‘**’,’**’],[‘*’,’**’],[‘*’,’*’],[”,’*’],[”,”]]

print(“Licznik Suma”)
print(“** 0 ** ** 0 **”)
print(“——- ——–“)
for i in range(1,counter+1):
if len(str(counter*increment)) <= 5:
print(ex[len(str(i))][0],i,ex[len(str(i))][1], ” || “, ex[len(str(i*increment))][0],i*increment,ex[len(str(i*increment))][1] )
else:
print(“Too big numbers“)
break
