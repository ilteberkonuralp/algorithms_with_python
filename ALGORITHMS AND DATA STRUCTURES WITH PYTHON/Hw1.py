# Task 1
def tensionCalculator(m:float,v:float,r:float):
    return m*v**2/r
tensionCalculator(2, 5.0, 2.0)

# Task 2
def deleteConsecutiveSimilar(integerList:list):
    if (len(integerList)==1) or (len(integerList)==0):
            return integerList
    numhold=[]
    startingpoint=list(integerList)
    for k in range(len(integerList)-1):
        
        if(any(item in integerList[k] for item in integerList[k+1])):
            #print(integerList[k])
            numhold.append(k)
    
    for k in range(len(numhold),0,-1):
        
            for j in range(2):
                integerList.pop(numhold[k-1])
    if integerList==startingpoint:
        return integerList
    else:
        return (deleteConsecutiveSimilar(integerList))
deleteConsecutiveSimilar([[2,5,10],[7,-1],[3,-1],[2,0],[-5,0]])

# Task 3
def modifyTxt(filename,*args):
    file = open(filename, 'r')
    linelist= list(map(str.split,file.readlines()))
    file.close()
    mode=str.lower(args[0])
    if (mode=="update"):
        id=args[1]
        field=str.lower(args[2])
        newValue=args[3]
        
        for k in linelist:
            if(int(k[0])==int(id)):
                if(field=="name"):
                    k[1]=newValue
                elif(field=="surname"):
                    k[2]=newValue
                elif(field=="job"):
                    k[3]==newValue
                elif(field=="age"):
                    k[4]=newValue
        with open(filename, 'w') as file:
            for k in linelist:
                wlrt=' '.join(map(str, k))+"\n"
                file.write(wlrt)
        
        
            
    elif(mode=="delete"):
        recordlist=[]
        for t in linelist:
            if(int(t[0])==args[1]):
                pass
            else:
                recordlist.append(t)
        with open(filename, 'w') as file:
            for k in recordlist:
                wlrt=' '.join(map(str, k))+"\n"
                file.write(wlrt)

    else:
        return None
    
modifyTxt("simplefile.txt", "update", 12, "age", 26)
modifyTxt("simplefile.txt", "delete", 30)