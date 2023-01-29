
class HashTable:
    def __init__(self) -> None:
        self._arrlen=0
        self.array=[None for i in range(self._arrlen)]
    
    def Gethash(self,key):
        h=0
        
        for char in key:
            h+=ord(char)
        return h% self._arrlen

    def __setitem__(self,key,val):
        self._arrlen+=1
        h=self.Gethash(key)
        self.array[h]=val
    
    def __getitem__(self,key):
        h=self.Gethash(key)
        return self.array[h]
    def __delitem__(self,key):
        h=self.Gethash(key)
        self.array[h]=None
t=HashTable()
t["march 1"]=30.23
t["march 2"]=13.66
t["march 3"]=46.2
t["march 4"]=17.7
t["march 5"]=80.9
t["march 6"]=130.2
print(t["march 6"])
print(t["march 1"])
del t["march 6"]
