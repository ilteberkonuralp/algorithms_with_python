fp=open("Arithmetic_Progression.txt","r+")
fp.readline()
fplines=fp.readlines()
result=[]
for i in fplines:
    a=i.split()
    sum=0
    for ii in range(0,int(a[2])):
        sum+=int(a[0])+ii*int(a[1])
    result.append(sum)

for element in result:
    print(element,end=" ")