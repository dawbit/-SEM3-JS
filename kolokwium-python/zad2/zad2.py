def oblicz_wiek(a,b):
    yearA=a.split('.')
    yearB=b.split('.')
    return int(yearB[2])-int(yearA[2])
   
 
f=open('bazadanych.txt', 'r')
p=[]
result=[]
results=[]
tekst = ''
for l in f:
    p=l.split(',')
    result.append(p[0])
    result.append(oblicz_wiek(p[1],p[4]))
    if(p[2]==p[5]):
        result.append('TAK')
    else:
        result.append('NIE')
 
    if(p[3]==p[6]):
        result.append('TAK')
    else:
        result.append('NIE')
    results.append(result)
    result=[]
f.close()
f=open('analizadanych.txt','w')
f.write("Osoba\t\t\tZył lat\t\tUr i Zm. w tym samym mieście\t\tUr i Zm. w tym samym kraju\n")
f.write("________________________________________________________________________________________________________________\n")
for i in results:
    f.write(str(i[0])+'\t\t'+str(i[1]).rjust(7,'*')+'\t\t'+str(i[2]).rjust(13,'-') + tekst.ljust(11,'-') +  '\t\t' + str(i[3]) + '\n')
 
f.close()
