#Sprawdzone
import datetime
print("Podaj rok i numer tygodnia")
line = input().split(" ")
rok = line[0]
weekn = line[1]
l = str(rok+" 1 1")
dt  = datetime.datetime.strptime(l,  '%Y %m %d')
u = datetime.timedelta(weeks=int(weekn)-1)
t = dt+u
if t.weekday() == 0:
    print("Najblizszy poniedzialek to :",t)
else :
    d = t.weekday()
    u = datetime.timedelta(days=-d)
    z = t+u
    print(z)


