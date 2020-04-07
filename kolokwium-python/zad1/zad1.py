f=open("tekstwejsciowy.txt","r")
tekst=f.read()
wyrazy=[0]
czestosc=[5]
slowo=''
for i in range(1000):
    czestosc.append(0)
licznik=0
z=0
wyraz=""
tekst+=" "
for litera in tekst:
    if litera==' ':
        for i in range(0,len(wyrazy)):
            if wyraz==wyrazy[i]:
                czestosc[i]+=1
                wyraz=""
            elif i==len(wyrazy)-1:
                wyrazy.append(wyraz)
                czestosc[i+1]+=1
                wyraz=""
    else:
        wyraz+=litera
 
f.close()
f=open('tekstwyjsciowy.txt','w')
f.write(str('słowo').ljust(16,' ')+'|'+str('liczba wystąpnień').rjust(25,' ')+'\n')
f.write("_________________________________________\n")
for i in range(1,len(wyrazy)):
    if wyrazy[i]=="":
        continue
    f.write(str(wyrazy[i]).ljust(16,' ')+'|'+ slowo.rjust(15,' ') + str(czestosc[i]).rjust(10,'*')+'\n')
 
f.close()
