mf = open("Array_Checksum.txt" , "r+")
mf.readline()
k = mf.readline()
t = k.split()
result=0
for i in range(0, len(t)):
    dsplit = t[i]
    result=(result+int(dsplit))*113
print(result%10000007)
import numpy as np
a=np.array([[1,2,3],[3,4,5]])
print(np.sum(a[:,2]))