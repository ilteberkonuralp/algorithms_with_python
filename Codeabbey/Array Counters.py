myarrayf=open("Array_Counters.txt","r+")
line1=myarrayf.readline()
line2=myarrayf.readline()
for i in range(int(line1.split()[1])):
    count=0
    for k in range(len(line2.split())):
        if(int(line2.split()[k])==(i+1)):
            count+=1
    print(count,end=" ")